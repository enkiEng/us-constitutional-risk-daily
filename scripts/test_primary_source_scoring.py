#!/usr/bin/env python3
"""
Regression tests for how primary-source evidence affects scoring.

Run with: python scripts/test_primary_source_scoring.py

These cover the two rules that primary-source ingestion introduced, both of
which are easy to break by accident and neither of which shows up in a normal
day's output (a red-level severity has never yet occurred):

1. An official record can anchor a red-level (4) severity on its own, but only
   when it confirms the top-severity event itself. A primary document that
   confirms something milder must not act as corroboration for a severity-4
   news claim, and must not count as a second "publisher".
2. The keyword fallback path scores identically whether or not primary
   documents were fetched. Without the AI layer the pipeline cannot judge
   whether an official record is on point, so it must not move the number.
"""

from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import update_constitutional_risk as u  # noqa: E402


CONFIG = json.loads(
    (Path(__file__).resolve().parent.parent / "config" / "constitutional_risk_config.json")
    .read_text(encoding="utf-8")
)
SIGNAL = next(s for s in CONFIG["signals"] if s["id"] == "court_order_noncompliance")


def entry(title: str, publisher: str, tier: str = "news") -> u.FeedEntry:
    return u.FeedEntry(
        title=title,
        link="https://example.test/" + title.replace(" ", ""),
        summary=title,
        publisher=publisher,
        published=dt.datetime.now(u.UTC),
        source_tier=tier,
    )


def judgment(severity: int, primary_url: str = "") -> dict:
    return {
        "is_us_domestic": True,
        "event_occurred": True,
        "matches_signal": True,
        "severity": severity,
        "actor": "Executive branch",
        "primary_source_url": primary_url,
        "rationale": f"severity {severity}",
        "confidence": 0.9,
    }


def test_severity_anchoring() -> list[str]:
    cases = [
        ("single news outlet claiming red is held at orange",
         [entry("a", "outlet1")], [judgment(4)], 3.0),
        ("two independent outlets corroborate red",
         [entry("a", "outlet1"), entry("b", "outlet2")], [judgment(4), judgment(4)], 4.0),
        ("an official record alone anchors red",
         [entry("EO", "federalregister.gov", "primary")], [judgment(4)], 4.0),
        ("official record confirming the same red event anchors it",
         [entry("a", "outlet1"), entry("EO", "federalregister.gov", "primary")],
         [judgment(4), judgment(4)], 4.0),
        ("official record confirming only a milder fact does not anchor red",
         [entry("a", "outlet1"), entry("EO", "federalregister.gov", "primary")],
         [judgment(4), judgment(2)], 3.0),
        ("a primary URL cited by the model anchors red",
         [entry("a", "outlet1")], [judgment(4, "https://supremecourt.gov/x.pdf")], 4.0),
        ("orange stays orange without corroboration rules applying",
         [entry("EO", "federalregister.gov", "primary")], [judgment(3)], 3.0),
        ("no qualifying judgment is an explicit zero",
         [entry("a", "outlet1")], [None], 0.0),
    ]
    failures = []
    for name, entries, judgments, expected in cases:
        score = u._ai_auto_score(SIGNAL, entries, judgments, CONFIG)[0]
        if score != expected:
            failures.append(f"{name}: expected {expected}, got {score}")
    return failures


def test_keyword_path_is_unaffected() -> list[str]:
    news = [
        entry("government defied court order", "outlet1"),
        entry("agency ignored injunction", "outlet2"),
    ]
    primary = [
        entry("Notice mentioning contempt", "federalregister.gov", "primary"),
        entry("Doe v. Warden motion to enforce", "courtlistener.com", "primary"),
    ]
    news_only = u._keyword_auto_score(SIGNAL, news, CONFIG)
    with_primary = u._keyword_auto_score(SIGNAL, u.merge_entries(news, primary), CONFIG)

    failures = []
    if news_only[:5] != with_primary[:5]:
        failures.append(
            f"keyword scoring changed when primary docs were present: "
            f"{news_only[:5]} vs {with_primary[:5]}"
        )
    if not any(e.source_tier == "primary" for e in with_primary[5]):
        failures.append("primary documents should still be listed as evidence")
    return failures


def main() -> int:
    failures = test_severity_anchoring() + test_keyword_path_is_unaffected()
    for failure in failures:
        print(f"FAIL: {failure}")
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("all primary-source scoring tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
