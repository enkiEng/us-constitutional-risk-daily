#!/usr/bin/env python3
"""
Compute the Cumulative Erosion Sub-Index (CEI) history from stored data.

The acute daily score is a flow measure: confirmed events in a 2-day window
that decay within days. The CEI is the stock counterpart (see
docs/cumulative-erosion-subindex-proposal.md). It has two components:

  pressure_score  Per-signal EWMA of each day's stored final_score with a
                  long half-life (config: cumulative.pressure_half_life_days),
                  aggregated to 0-100 with the same escalation-max domain
                  aggregation and weights as the acute index. Fully automatic,
                  derived from data/constitutional_signal_scores.csv.

  ledger_score    Human-vetted structural conditions in
                  data/erosion_ledger.json. Each active entry contributes its
                  magnitude (1-4) to its domain; per-domain sums saturate via
                  4*(1-exp(-sum/4)) before weighting. An absent or empty
                  ledger scores 0 and marks the CEI provisional.

  CEI = min(100, ledger_score + pressure_coefficient * pressure_score)

The script recomputes the full series from day one on every invocation
(idempotent — a few thousand rows, so there is no incremental state to
corrupt) and rewrites data/cumulative_erosion_history.csv. run_daily.py calls
it after the acute update so the series stays current.

Ledger timeline approximation: an entry counts from its "established" date;
a "reversed" date ends it; status "partially_reversed" halves the magnitude
from the established date onward (per-date status history is not tracked in
v1 — the ledger stores current state plus the two dates).
"""

from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from dataclasses import dataclass
from datetime import date as date_cls
from datetime import timedelta
from pathlib import Path
from typing import Any

import update_constitutional_risk as u


@dataclass
class _Row:
    signal_id: str
    domain_id: str
    final_score: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Backfill/update the CEI history.")
    parser.add_argument("--config", type=Path, default=Path("config/constitutional_risk_config.json"))
    parser.add_argument(
        "--signal-history",
        type=Path,
        default=Path("data/constitutional_signal_scores.csv"),
    )
    parser.add_argument("--ledger", type=Path, default=None,
                        help="Override cumulative.ledger_path from config.")
    parser.add_argument("--output", type=Path, default=None,
                        help="Override cumulative.history_path from config.")
    return parser.parse_args()


def load_ledger(path: Path) -> list[dict[str, Any]]:
    data = u.read_json(path, None)
    if not data:
        return []
    entries = data.get("entries", data) if isinstance(data, dict) else data
    return [e for e in entries if isinstance(e, dict)]


def effective_magnitude(entry: dict[str, Any], on: date_cls) -> float:
    """Magnitude an entry contributes on a given date (0 if not in effect)."""
    established = _parse_date(entry.get("established"))
    if established is None or on < established:
        return 0.0
    reversed_on = _parse_date(entry.get("reversed"))
    if reversed_on is not None and on >= reversed_on:
        return 0.0
    try:
        magnitude = float(entry.get("magnitude", 0.0))
    except (TypeError, ValueError):
        return 0.0
    if str(entry.get("status", "active")) == "partially_reversed":
        magnitude *= 0.5
    return u.clamp(magnitude, 0.0, 4.0)


def ledger_score_for_date(
    entries: list[dict[str, Any]], domains: dict[str, dict[str, Any]], on: date_cls
) -> float:
    magnitude_by_domain: dict[str, float] = defaultdict(float)
    for entry in entries:
        dom_id = str(entry.get("domain_id", ""))
        if dom_id in domains:
            magnitude_by_domain[dom_id] += effective_magnitude(entry, on)
    score = 0.0
    for dom_id, dom in domains.items():
        total = magnitude_by_domain.get(dom_id, 0.0)
        erosion = 4.0 * (1.0 - math.exp(-total / 4.0))
        score += float(dom["weight"]) * (erosion / 4.0)
    return u.clamp(score, 0.0, 100.0)


def _parse_date(value: Any) -> date_cls | None:
    if not value:
        return None
    try:
        return date_cls.fromisoformat(str(value))
    except ValueError:
        return None


def main() -> int:
    args = parse_args()
    config = u.read_json(args.config, None)
    if not config:
        raise SystemExit(f"Missing or invalid config: {args.config}")

    cumulative_cfg = config.get("cumulative", {}) or {}
    half_life = float(cumulative_cfg.get("pressure_half_life_days", 180))
    coefficient = float(cumulative_cfg.get("pressure_coefficient", 0.35))
    ledger_path = args.ledger or Path(cumulative_cfg.get("ledger_path", "data/erosion_ledger.json"))
    output_path = args.output or Path(cumulative_cfg.get("history_path", "data/cumulative_erosion_history.csv"))
    decay = 0.5 ** (1.0 / half_life)

    domains = {d["id"]: d for d in config["domains"]}
    signal_domain = {s["id"]: s["domain_id"] for s in config["signals"]}
    ledger_entries = load_ledger(ledger_path)

    by_date: dict[str, dict[str, float]] = defaultdict(dict)
    with args.signal_history.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            try:
                score = float(row["final_score"])
            except (TypeError, ValueError, KeyError):
                continue
            day = by_date[row["date"]]
            sig = row["signal_id"]
            day[sig] = max(day.get(sig, 0.0), score)

    pressure: dict[str, float] = {sig: 0.0 for sig in signal_domain}
    fieldnames = ["date", "pressure_score", "ledger_score", "cei", "cei_band", "provisional"]
    out_rows: list[dict[str, str]] = []
    bands = cumulative_cfg.get("bands") or config["risk_bands"]

    previous_day: date_cls | None = None
    for date_str in sorted(by_date.keys()):
        day = _parse_date(date_str)
        if day is None:
            continue

        # Calendar gaps (missed runs) decay the EWMA as zero-severity days so
        # a stretch of downtime is not silently treated as elapsed-time-free.
        if previous_day is not None:
            gap = (day - previous_day).days - 1
            if gap > 0:
                factor = decay**gap
                for sig in pressure:
                    pressure[sig] *= factor
        previous_day = day

        scores = by_date[date_str]
        for sig in pressure:
            pressure[sig] = decay * pressure[sig] + (1.0 - decay) * scores.get(sig, 0.0)

        severities_by_domain: dict[str, list[float]] = defaultdict(list)
        for sig, value in pressure.items():
            severities_by_domain[signal_domain[sig]].append(value)

        pressure_score = 0.0
        for dom_id, dom in domains.items():
            sev = u.domain_severity(severities_by_domain.get(dom_id, []), config)
            pressure_score += float(dom["weight"]) * (sev / 4.0)
        pressure_score = u.clamp(pressure_score, 0.0, 100.0)

        ledger_score = ledger_score_for_date(ledger_entries, domains, day)
        active_ledger = any(effective_magnitude(e, day) > 0 for e in ledger_entries)
        cei = min(100.0, ledger_score + coefficient * pressure_score)
        band = u.score_band(int(round(cei)), bands)

        out_rows.append(
            {
                "date": date_str,
                "pressure_score": f"{pressure_score:.2f}",
                "ledger_score": f"{ledger_score:.2f}",
                "cei": f"{cei:.2f}",
                "cei_band": band["label"],
                "provisional": "false" if active_ledger else "true",
            }
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out_rows)

    if out_rows:
        latest = out_rows[-1]
        print(
            f"CEI history: {len(out_rows)} days -> {output_path} | latest {latest['date']}: "
            f"cei={latest['cei']} (pressure={latest['pressure_score']}, "
            f"ledger={latest['ledger_score']}, provisional={latest['provisional']})"
        )
    else:
        print(f"CEI history: no usable rows in {args.signal_history}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
