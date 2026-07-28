#!/usr/bin/env python3
"""
Seed the v2 score history by re-aggregating stored per-signal severities.

Methodology v2 changes only how per-signal severities are *combined* into the
0-100 index (escalation-max aggregation + trip-wire floors); it does not need
any new per-signal data. Every signal's daily severity is already recorded in
``data/constitutional_signal_scores.csv``. This script replays that history
through the v2 aggregation so the public trend line is continuous from day one
instead of starting empty.

It does NOT touch the v1 history CSV (``constitutional_risk_history.csv``),
which stays frozen as the archived v1 series.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import update_constitutional_risk as u


@dataclass
class _Row:
    signal_id: str
    domain_id: str
    final_score: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Backfill v2 history from signal scores.")
    parser.add_argument("--config", type=Path, default=Path("config/constitutional_risk_config.json"))
    parser.add_argument(
        "--signal-history",
        type=Path,
        default=Path("data/constitutional_signal_scores.csv"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/constitutional_risk_history_v2.csv"),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = u.read_json(args.config, None)
    if not config:
        raise SystemExit(f"Missing or invalid config: {args.config}")

    domains = {d["id"]: d for d in config["domains"]}

    by_date: dict[str, list[_Row]] = defaultdict(list)
    with args.signal_history.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            try:
                score = float(row["final_score"])
            except (TypeError, ValueError, KeyError):
                continue
            by_date[row["date"]].append(_Row(row["signal_id"], row["domain_id"], score))

    domain_keys = sorted(domains.keys())
    fieldnames = ["date", "score", "score_raw", "band"] + domain_keys
    out_rows: list[dict[str, str]] = []

    for date_str in sorted(by_date.keys()):
        rows = by_date[date_str]
        severities_by_domain: dict[str, list[float]] = defaultdict(list)
        score_by_signal: dict[str, float] = {}
        for r in rows:
            severities_by_domain[r.domain_id].append(r.final_score)
            score_by_signal[r.signal_id] = max(score_by_signal.get(r.signal_id, 0.0), r.final_score)

        raw = 0.0
        domain_points: dict[str, float] = {}
        for dom_id, dom in domains.items():
            sev = u.domain_severity(severities_by_domain.get(dom_id, []), config)
            points = float(dom["weight"]) * (sev / 4.0)
            domain_points[dom_id] = points
            raw += points
        raw = u.clamp(raw, 0.0, 100.0)

        # Trip-wires: re-apply floors from the stored per-signal severities.
        floor = 0
        for rule in (config.get("trip_wires", {}) or {}).get("rules", []):
            sev = score_by_signal.get(rule.get("signal_id"), 0.0)
            if sev >= float(rule.get("min_severity", 4)):
                floor = max(floor, int(rule.get("floor_score", 0)))
        raw = max(raw, float(floor))

        score = int(round(raw))
        band = u.score_band(score, config["risk_bands"])
        record = {
            "date": date_str,
            "score": str(score),
            "score_raw": f"{raw:.2f}",
            "band": band["label"],
        }
        for dom_id in domain_keys:
            record[dom_id] = f"{domain_points.get(dom_id, 0.0):.2f}"
        out_rows.append(record)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out_rows)

    print(f"Backfilled {len(out_rows)} days of v2 history into {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
