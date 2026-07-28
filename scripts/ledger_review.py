#!/usr/bin/env python3
"""
Daily AI review pass for the Cumulative Erosion Ledger.

Reads the day's confirmed signals (from ``data/latest_dashboard.json``) plus
the current structural-condition ledger and asks a model one question: did
anything happen that durably changes the ledger — a new structural condition,
a magnitude change, or a verified reversal?

Proposals land in ``data/erosion_ledger_proposals.json`` under ``pending``.
Nothing touches the published CEI until a human merges a proposal into
``data/erosion_ledger.json`` and reruns ``backfill_erosion_pressure.py`` —
same philosophy as the acute index's manual overrides: the model proposes,
the maintainer disposes.

This step is strictly optional: any failure (no SDK, no credentials, API or
parse error) logs a warning and exits 0 so the daily pipeline never fails on
it. Most days the correct output is an empty proposal list — the prompt says
so explicitly.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import ai_classifier

CONFIG_PATH = Path("config/constitutional_risk_config.json")
DASHBOARD_PATH = Path("data/latest_dashboard.json")
PROPOSALS_PATH = Path("data/erosion_ledger_proposals.json")

_PROPOSAL_SCHEMA = {
    "type": "object",
    "properties": {
        "proposals": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["add", "update", "reverse"]},
                    "id": {"type": "string"},
                    "domain_id": {"type": "string"},
                    "title": {"type": "string"},
                    "class": {
                        "type": "string",
                        "enum": ["statute", "ruling", "executive_action", "practice"],
                    },
                    "magnitude": {"type": "integer", "enum": [1, 2, 3, 4]},
                    "status": {
                        "type": "string",
                        "enum": ["active", "partially_reversed", "reversed"],
                    },
                    "established": {"type": "string"},
                    "evidence": {"type": "array", "items": {"type": "string"}},
                    "rationale": {"type": "string"},
                    "confidence": {"type": "number"},
                },
                "required": [
                    "action",
                    "id",
                    "domain_id",
                    "title",
                    "class",
                    "magnitude",
                    "status",
                    "established",
                    "evidence",
                    "rationale",
                    "confidence",
                ],
                "additionalProperties": False,
            },
        }
    },
    "required": ["proposals"],
    "additionalProperties": False,
}

_SYSTEM_PROMPT = (
    "You maintain the Structural Condition Ledger for a U.S. constitutional-risk "
    "dashboard. The ledger records durable STATES — rulings in force, statutes, "
    "executed orders, entrenched practices — that remove or weaken a constitutional "
    "check. It is not an event log. Magnitude rubric (1-4): 1 = norm/informal "
    "practice abandoned, check legally intact; 2 = check weakened for a targeted "
    "scope; 3 = check broadly weakened or made discretionary (survives only if the "
    "executive chooses restraint); 4 = check effectively eliminated. Be strictly "
    "conservative: propose a change ONLY when today's confirmed evidence shows a "
    "durable structural change — a final ruling, an executed order taking effect, a "
    "verified reversal or repair of an existing entry. Proposals, filings, pending "
    "litigation, rhetoric, and news volume are NOT ledger material. On most days "
    "the correct answer is an empty proposals list. Every proposal is reviewed by "
    "a human before it affects anything."
)


def _load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError):
        return None


def _ledger_digest(ledger: dict[str, Any] | None) -> list[dict[str, Any]]:
    entries = (ledger or {}).get("entries", [])
    return [
        {
            "id": e.get("id"),
            "domain_id": e.get("domain_id"),
            "title": e.get("title"),
            "magnitude": e.get("magnitude"),
            "status": e.get("status"),
            "established": e.get("established"),
        }
        for e in entries
        if isinstance(e, dict)
    ]


def _todays_evidence(dashboard: dict[str, Any] | None) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for signal in (dashboard or {}).get("top_signals", []):
        try:
            severity = float(signal.get("severity", 0))
        except (TypeError, ValueError):
            severity = 0.0
        if severity <= 0:
            continue
        out.append(
            {
                "signal": signal.get("name"),
                "severity": severity,
                "rationale": signal.get("rationale"),
                "evidence": [
                    {"title": item.get("title"), "publisher": item.get("publisher"), "link": item.get("link")}
                    for item in (signal.get("evidence") or [])[:4]
                ],
            }
        )
    return out


def main() -> int:
    config = _load_json(CONFIG_PATH) or {}
    ai_cfg = config.get("ai", {}) or {}
    cumulative_cfg = config.get("cumulative", {}) or {}
    ledger_path = Path(cumulative_cfg.get("ledger_path", "data/erosion_ledger.json"))

    if not ai_classifier.is_available(ai_cfg):
        print("ledger_review: AI layer unavailable (no SDK or credentials); skipping.")
        return 0

    dashboard = _load_json(DASHBOARD_PATH)
    ledger = _load_json(ledger_path)
    proposals_doc = _load_json(PROPOSALS_PATH) or {}
    pending: list[dict[str, Any]] = list(proposals_doc.get("pending", []))
    evidence = _todays_evidence(dashboard)

    if not evidence:
        print("ledger_review: no confirmed signals today; skipping model call.")
        return 0

    payload = {
        "date": (dashboard or {}).get("generated_at", ""),
        "current_ledger": _ledger_digest(ledger),
        "already_pending_proposal_ids": [p.get("id") for p in pending],
        "todays_confirmed_signals": evidence,
    }
    prompt = (
        "Review today's confirmed dashboard signals against the current ledger. "
        "Propose ledger changes only per the rules in your instructions; do not "
        "re-propose anything in already_pending_proposal_ids. For action=update "
        "or reverse, the id must match an existing entry; for action=add, mint a "
        "new snake_case id. Return an empty proposals list if nothing qualifies.\n\n"
        + json.dumps(payload, indent=2)
    )

    try:
        import anthropic

        client = anthropic.Anthropic()
        response = client.messages.create(
            model=str(ai_cfg.get("ledger_model", "claude-sonnet-5")),
            max_tokens=4096,
            system=_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
            output_config={"format": {"type": "json_schema", "schema": _PROPOSAL_SCHEMA}},
        )
        text = next((b.text for b in response.content if b.type == "text"), "")
        result = json.loads(text)
    except Exception as exc:  # noqa: BLE001 - daily run must never fail on this step
        print(f"ledger_review: model call failed ({type(exc).__name__}: {exc}); skipping.")
        return 0

    new_proposals = []
    pending_keys = {(p.get("action"), p.get("id")) for p in pending}
    for proposal in result.get("proposals", []):
        if (proposal.get("action"), proposal.get("id")) in pending_keys:
            continue
        proposal["proposed_on"] = str((dashboard or {}).get("generated_at", ""))[:10]
        new_proposals.append(proposal)

    if not new_proposals:
        print("ledger_review: no new ledger proposals today.")
        return 0

    pending.extend(new_proposals)
    doc = {
        "note": (
            "Pending CEI ledger proposals awaiting human review. To accept one: move "
            "it into data/erosion_ledger.json (entries[]), adjust magnitude/status as "
            "needed, delete it from pending, then rerun "
            "scripts/backfill_erosion_pressure.py. Generated daily by "
            "scripts/ledger_review.py; nothing here affects the published CEI."
        ),
        "pending": pending,
    }
    with PROPOSALS_PATH.open("w", encoding="utf-8") as handle:
        json.dump(doc, handle, indent=2)
        handle.write("\n")
    print(f"ledger_review: {len(new_proposals)} new proposal(s) pending review in {PROPOSALS_PATH}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
