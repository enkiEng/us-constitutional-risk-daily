#!/usr/bin/env python3
"""
Regression tests for Google News link resolution.

Run with: python scripts/test_link_resolution.py

These are deliberately offline. The resolver depends on an undocumented Google
endpoint that will eventually change shape, and a test that called it would go
red for that reason rather than for a regression in this repo — turning the
suite into something people learn to ignore. What is tested here is everything
around the network call, which is where a change in this repo can break things:

1. Google links are recognised and non-Google links are left alone. Primary
   sources (Federal Register, CourtListener) already carry real URLs; spending
   a request on one would be pure waste and rewriting one would be wrong.
2. A failed resolution keeps the original link. The whole design premise is
   that a broken resolver costs the run nothing.
3. The cache is honoured, so a second run spends no requests.
4. The per-run budget is enforced, so a day with unusually many signals cannot
   turn into an unbounded number of requests against that endpoint.

The live endpoint itself is exercised by running the pipeline; the run report
counts resolved/failed links, which is the signal that it has changed.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import resolve_links  # noqa: E402

GOOGLE = ("https://news.google.com/rss/articles/CBMixwFBVV95cUxPcmpTZGx4MkpaUW1Xb0"
          "FHX21iTS1rVk9PN1FDMlV5MzVNNlZOdmxKdGt5dFdwdnZfa195TzYyZERTdGRmaFgtdzIz"
          "US1hT0NCZHdfTHlZSGNvR0tRTEFMWm5ielIwR1JNNjliSW5jZ2Y5WVdfZURCY1JBTkRoUj"
          "ZzVHdMUEYzVnZpNF92Skk4aXhiNTFXTFRDcndlU2FfRUJ0UUZGSDdlMDUxc3QwUlNsQWI2"
          "akNGTGxyYmFHU3pEQXFRNFhHU2RF?oc=5")
FEDREG = "https://www.federalregister.gov/documents/2026/07/30/2026-14321/example"
CONFIG = {"enabled": True, "max_requests_per_run": 40, "delay_seconds": 0}


class Entry:
    def __init__(self, link: str) -> None:
        self.link = link
        self.canonical_link = ""


class Result:
    def __init__(self, *links: str) -> None:
        self.evidence = [Entry(link) for link in links]


def _with_resolver(returns, calls: list):
    """Swap the network call for a stub, returning the original."""
    original = resolve_links.resolve_one

    def stub(link, *, timeout, user_agent):
        calls.append(link)
        return returns

    resolve_links.resolve_one = stub
    return original


def test_article_id_discrimination() -> list[str]:
    failures = []
    if resolve_links.article_id(GOOGLE) is None:
        failures.append("did not recognise a Google News article link")
    for other in (FEDREG, "https://www.courtlistener.com/docket/1/doe-v-warden/", ""):
        if resolve_links.article_id(other) is not None:
            failures.append(f"treated a non-Google link as one: {other!r}")
    return failures


def test_primary_sources_untouched() -> list[str]:
    calls: list[str] = []
    original = _with_resolver("https://example.com/resolved", calls)
    try:
        result = Result(FEDREG)
        stats = resolve_links.resolve_evidence([result], {}, CONFIG, timeout=1, user_agent="t")
    finally:
        resolve_links.resolve_one = original

    failures = []
    if calls:
        failures.append(f"spent {len(calls)} request(s) on a non-Google link")
    if result.evidence[0].canonical_link != FEDREG:
        failures.append("a primary-source URL should pass through as its own canonical link")
    if stats["skipped"] != 1:
        failures.append(f"expected skipped=1, got {stats}")
    return failures


def test_failure_keeps_original_link() -> list[str]:
    calls: list[str] = []
    original = _with_resolver(None, calls)          # resolution fails
    try:
        result = Result(GOOGLE)
        cache: dict[str, str] = {}
        stats = resolve_links.resolve_evidence([result], cache, CONFIG, timeout=1, user_agent="t")
    finally:
        resolve_links.resolve_one = original

    failures = []
    if result.evidence[0].canonical_link:
        failures.append("a failed resolution must not set a canonical link")
    if result.evidence[0].link != GOOGLE:
        failures.append("the original link must survive a failed resolution")
    if cache:
        failures.append("a failure must not be cached as if it were an answer")
    if stats["failed"] != 1:
        failures.append(f"expected failed=1, got {stats}")
    return failures


def test_cache_is_honoured() -> list[str]:
    art_id = resolve_links.article_id(GOOGLE)
    cache = {art_id: "https://publisher.example/story"}
    calls: list[str] = []
    original = _with_resolver("https://should-not-be-called.example", calls)
    try:
        result = Result(GOOGLE)
        stats = resolve_links.resolve_evidence([result], cache, CONFIG, timeout=1, user_agent="t")
    finally:
        resolve_links.resolve_one = original

    failures = []
    if calls:
        failures.append("a cached link must not cost a request")
    if result.evidence[0].canonical_link != "https://publisher.example/story":
        failures.append("cached canonical link was not applied")
    if stats["cached"] != 1:
        failures.append(f"expected cached=1, got {stats}")
    return failures


def test_budget_is_enforced() -> list[str]:
    # Distinct ids so nothing is served from cache.
    links = [GOOGLE.replace("CBMixwFB", f"CBMixwF{n}") for n in range(6)]
    calls: list[str] = []
    original = _with_resolver("https://publisher.example/story", calls)
    try:
        result = Result(*links)
        stats = resolve_links.resolve_evidence(
            [result], {}, {**CONFIG, "max_requests_per_run": 2}, timeout=1, user_agent="t"
        )
    finally:
        resolve_links.resolve_one = original

    failures = []
    if len(calls) != 2:
        failures.append(f"budget of 2 allowed {len(calls)} request(s)")
    if stats["resolved"] != 2 or stats["failed"] != 4:
        failures.append(f"expected resolved=2 failed=4, got {stats}")
    return failures


def test_disabled_is_a_no_op() -> list[str]:
    calls: list[str] = []
    original = _with_resolver("https://publisher.example/story", calls)
    try:
        result = Result(GOOGLE)
        resolve_links.resolve_evidence([result], {}, {"enabled": False}, timeout=1, user_agent="t")
    finally:
        resolve_links.resolve_one = original

    failures = []
    if calls:
        failures.append("disabled resolution still made a request")
    if result.evidence[0].canonical_link:
        failures.append("disabled resolution still set a canonical link")
    return failures


def main() -> int:
    failures = (
        test_article_id_discrimination()
        + test_primary_sources_untouched()
        + test_failure_keeps_original_link()
        + test_cache_is_honoured()
        + test_budget_is_enforced()
        + test_disabled_is_a_no_op()
    )
    for failure in failures:
        print(f"FAIL: {failure}")
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("all link resolution tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
