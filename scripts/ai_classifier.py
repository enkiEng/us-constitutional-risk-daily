#!/usr/bin/env python3
"""
Optional AI extraction layer for the Constitutional Risk Dashboard.

The deterministic scorer in ``update_constitutional_risk.py`` turns news items
into severities by counting keyword hits. That measures how loudly the press is
covering a topic, not whether a constitutional-stress event actually happened,
and it is fooled by negation ("will NOT cancel the election"), hypotheticals,
opinion pieces, historical retrospectives, and foreign coverage.

This module replaces that brittle step with an LLM judgment *when it is
available*. Each candidate article is read by the model and returned as a
structured, schema-validated verdict:

    is_us_domestic     - is this a U.S. domestic event at all?
    event_occurred     - did it actually happen (vs hypothetical/denied/
                         historical/opinion/satire)?
    matches_signal     - does it match THIS signal specifically?
    severity           - 0-4 against the dashboard rubric
    actor              - who did it
    primary_source_url - court order / filing / official record, if cited
    rationale          - one-line human-readable reason
    confidence         - 0..1

Design constraints, on purpose:

  * The model runs ONLY at the extraction step. Aggregation and the published
    0-100 number stay pure Python in ``update_constitutional_risk.py`` so every
    score is reproducible from the stored judgments.
  * Graceful fallback: if the ``anthropic`` SDK is not installed or no API
    credentials are present, ``is_available()`` returns False and the caller
    keeps using the keyword scorer (and marks the day's confidence lower).
  * Per-(signal, article) results are cached on disk so the same article is not
    re-billed across daily runs.

The scoring semantics that turn these judgments into a severity live in the
caller, not here; this module only produces the judgments.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Availability / credentials
# ---------------------------------------------------------------------------

def _sdk() -> Any | None:
    try:
        import anthropic  # type: ignore
    except Exception:
        return None
    return anthropic


def has_credentials() -> bool:
    """True if the environment looks like it can authenticate to the API.

    An unset ``ANTHROPIC_API_KEY`` does not strictly prove there are no
    credentials (an ``ant`` OAuth profile also works), but for the CI cron the
    realistic and explicit contract is an env var, so we key on that.
    """
    for var in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN"):
        if os.environ.get(var, "").strip():
            return True
    return False


def is_available(ai_cfg: dict[str, Any]) -> bool:
    if not ai_cfg or not ai_cfg.get("enabled", False):
        return False
    if _sdk() is None:
        return False
    return has_credentials()


# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------

def load_cache(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def save_cache(path: Path, cache: dict[str, dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(cache, handle, indent=2, sort_keys=True)
        handle.write("\n")


def _cache_key(entry: Any) -> str:
    link = (getattr(entry, "link", "") or "").strip()
    title = (getattr(entry, "title", "") or "").strip()
    return link or title


# ---------------------------------------------------------------------------
# Schema for structured output
# ---------------------------------------------------------------------------

_JUDGMENT_SCHEMA = {
    "type": "object",
    "properties": {
        "judgments": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "index": {"type": "integer"},
                    "is_us_domestic": {"type": "boolean"},
                    "event_occurred": {"type": "boolean"},
                    "matches_signal": {"type": "boolean"},
                    "severity": {"type": "integer", "enum": [0, 1, 2, 3, 4]},
                    "actor": {"type": "string"},
                    "primary_source_url": {"type": "string"},
                    "rationale": {"type": "string"},
                    "confidence": {"type": "number"},
                },
                "required": [
                    "index",
                    "is_us_domestic",
                    "event_occurred",
                    "matches_signal",
                    "severity",
                    "actor",
                    "primary_source_url",
                    "rationale",
                    "confidence",
                ],
                "additionalProperties": False,
            },
        }
    },
    "required": ["judgments"],
    "additionalProperties": False,
}


_SEVERITY_RUBRIC = (
    "Severity rubric (0-4): "
    "0 = no material signal / irrelevant / not a real occurrence; "
    "1 = isolated or weak signal, a single low-credibility mention; "
    "2 = a repeated or credible stress signal (a real but contained action); "
    "3 = serious, confirmed high-severity action (e.g. an official openly "
    "defies a court order, an official campaign to remove judges over rulings); "
    "4 = confirmed structural constitutional-failure condition (e.g. an "
    "election is actually cancelled, military directed to decide an election, "
    "opposition leaders jailed as policy)."
)


def _build_prompt(signal: dict[str, Any], entries: list[Any], indices: list[int]) -> str:
    lines: list[str] = []
    lines.append(f"SIGNAL: {signal.get('name', '')}")
    lines.append(f"SIGNAL MEANING: {signal.get('description', '')}")
    lines.append("")
    lines.append(_SEVERITY_RUBRIC)
    lines.append("")
    lines.append(
        "For EACH item below decide, conservatively, whether it is real "
        "evidence that THIS signal's event occurred in the United States. Mark "
        "event_occurred=false for hypotheticals, denials, opinion/analysis, "
        "satire, historical retrospectives, and non-U.S. events. Only assign "
        "severity >= 3 when a specific, serious action has verifiably taken "
        "place (not merely been proposed, feared, or alleged). Return one "
        "judgment object per item, echoing its index."
    )
    lines.append("")
    lines.append(
        "Items tagged OFFICIAL RECORD are not press coverage: they are the "
        "government's or a court's own documents (Federal Register documents, "
        "federal docket entries, published opinions). Judge them as the act "
        "itself rather than as a report about an act, and set "
        "primary_source_url to the item's own URL when it confirms the event. "
        "Take the same care in the other direction: a proposed rule, a filed "
        "motion, or a routine notice is a request or a proposal, not an "
        "accomplished action, and an unrelated document that merely happens to "
        "contain the search words is severity 0."
    )
    lines.append("")
    lines.append("ITEMS:")
    for idx in indices:
        entry = entries[idx]
        title = (getattr(entry, "title", "") or "").strip()
        summary = (getattr(entry, "summary", "") or "").strip()
        publisher = (getattr(entry, "publisher", "") or "").strip()
        published = getattr(entry, "published", None)
        date = published.strftime("%Y-%m-%d") if published else "unknown date"
        tier = (getattr(entry, "source_tier", "news") or "news").strip()
        source_name = (getattr(entry, "source_name", "") or "").strip()
        if tier == "primary":
            marker = f"OFFICIAL RECORD - {source_name or publisher}"
        else:
            marker = publisher
        lines.append(f"[{idx}] ({marker}, {date}) {title}")
        if summary and summary.lower() != title.lower():
            lines.append(f"     summary: {summary[:400]}")
        link = (getattr(entry, "link", "") or "").strip()
        if tier == "primary" and link:
            lines.append(f"     url: {link}")
    return "\n".join(lines)


def _extract_json(response: Any) -> dict[str, Any] | None:
    try:
        for block in response.content:
            if getattr(block, "type", None) == "text":
                return json.loads(block.text)
    except (json.JSONDecodeError, AttributeError):
        return None
    return None


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def classify_entries(
    signal: dict[str, Any],
    entries: list[Any],
    ai_cfg: dict[str, Any],
    cache: dict[str, dict[str, Any]],
) -> list[dict[str, Any]] | None:
    """Return one judgment dict per entry (aligned by position).

    Returns ``None`` if the AI layer is unavailable *and no cached judgments
    exist* so the caller can fall back to the keyword scorer. If some entries
    are cached, cached judgments are returned and only uncached ones are sent
    to the model (or left as ``None`` when the model is unavailable).
    """
    signal_id = str(signal.get("id", ""))
    signal_cache = cache.setdefault(signal_id, {})

    results: list[dict[str, Any] | None] = [None] * len(entries)
    to_query: list[int] = []
    for idx, entry in enumerate(entries):
        key = _cache_key(entry)
        if key and key in signal_cache:
            results[idx] = signal_cache[key]
        elif key:
            to_query.append(idx)

    available = is_available(ai_cfg)
    if to_query and available:
        anthropic = _sdk()
        limit = int(ai_cfg.get("max_articles_per_signal", 12))
        batch = to_query[:limit]
        try:
            client = anthropic.Anthropic()
            response = client.messages.create(
                model=str(ai_cfg.get("model", "claude-haiku-4-5")),
                max_tokens=4096,
                system=str(ai_cfg.get("system_prompt", "")),
                messages=[{"role": "user", "content": _build_prompt(signal, entries, batch)}],
                output_config={"format": {"type": "json_schema", "schema": _JUDGMENT_SCHEMA}},
            )
            payload = _extract_json(response)
            if payload:
                by_index = {
                    int(j["index"]): j
                    for j in payload.get("judgments", [])
                    if isinstance(j, dict) and "index" in j
                }
                for idx in batch:
                    judgment = by_index.get(idx)
                    if judgment is not None:
                        judgment = {k: v for k, v in judgment.items() if k != "index"}
                        results[idx] = judgment
                        key = _cache_key(entries[idx])
                        if key:
                            signal_cache[key] = judgment
        except Exception:
            # Any API/parse failure degrades to keyword mode for this signal.
            pass

    if all(r is None for r in results):
        return None
    return results


def qualifies(judgment: dict[str, Any] | None, min_confidence: float) -> bool:
    """A judgment counts as real evidence for its signal."""
    if not judgment:
        return False
    try:
        conf = float(judgment.get("confidence", 0.0))
    except (TypeError, ValueError):
        conf = 0.0
    return bool(
        judgment.get("is_us_domestic")
        and judgment.get("event_occurred")
        and judgment.get("matches_signal")
        and conf >= min_confidence
    )
