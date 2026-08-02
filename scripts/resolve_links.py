#!/usr/bin/env python3
"""
resolve_links.py — turn Google News redirect links into publisher URLs.

Google News RSS does not give out the publisher's URL. Every ``link`` in the feed
is a redirect of the form::

    https://news.google.com/rss/articles/CBMixwFBVV95cUxPcmpTZGx4MkpaUW1Xb0FH…?oc=5

which runs 260-340 characters. That is fine for the dashboard, where the link is
an ``href`` behind anchor text, and expensive for a consumer whose citation has
to sit inside the text it is citing from — the Bluesky commentary drafter is
capped at 300 graphemes per post, so one of these leaves nothing to write with.

(That cap is Bluesky's, but a URL only spends it because that repo's scheduler
lacks link-card support and linkifies URLs already present in the post text. This
resolver is worth having regardless of whether that changes: a citation reading
``news.google.com`` does not tell a reader who actually reported the story.)

Resolving them once here means every consumer gets the short link: the rendered
site shows a real domain on hover instead of ``news.google.com``, and downstream
repos do not each grow their own resolver that drifts from this one.

WHY THIS IS NOT A REDIRECT FOLLOW
---------------------------------
The obvious implementation — issue a HEAD and read the final URL — does not work,
and it fails *quietly*, which is worse. Google serves HTTP 200 with a client-side
redirect, so ``geturl()`` hands back the same URL with locale parameters appended
(it gets *longer*, 314 -> 340). The base64 segment used to decode straight to the
target URL; it no longer does, and decodes to an opaque 204-byte protobuf token.

What does work is the endpoint the page's own JavaScript calls: post the article
id back to ``batchexecute`` along with the signature and timestamp embedded in the
article page as ``data-n-a-sg`` / ``data-n-a-ts``. Hence two requests per article.

That endpoint is undocumented and unversioned. It will break without notice. Every
failure path here therefore degrades to the original Google link rather than
raising: a broken resolver must cost the daily run nothing but a slightly uglier
citation. If resolution starts failing wholesale, the run still succeeds and the
counts reported by ``resolve_evidence`` are the signal that something changed.

Requests are cached on disk by article id and never expire — a published article's
canonical URL does not change, and re-resolving would be pure cost against an
endpoint we are already using on sufferance.
"""
from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Iterable

BATCH_URL = "https://news.google.com/_/DotsSplashUi/data/batchexecute"
_ARTICLE_RE = re.compile(r"news\.google\.com/(?:rss/)?articles/([^?/#]+)")
_SIGNATURE_RE = re.compile(r'data-n-a-sg="([^"]+)"')
_TIMESTAMP_RE = re.compile(r'data-n-a-ts="([^"]+)"')
_RESULT_RE = re.compile(r'\[\\"garturlres\\",\\"(.*?)\\"')


# ---------------------------------------------------------------------------
# Cache  (same shape and failure behaviour as ai_classifier's)
# ---------------------------------------------------------------------------

def load_cache(path: Path) -> dict[str, str]:
    if not Path(path).exists():
        return {}
    try:
        with Path(path).open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def save_cache(path: Path, cache: dict[str, str]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(cache, handle, indent=2, sort_keys=True)
        handle.write("\n")


# ---------------------------------------------------------------------------
# Resolution
# ---------------------------------------------------------------------------

def article_id(link: str) -> str | None:
    """The opaque id Google keys an article by, or None if not a Google link.

    Primary-source entries (Federal Register, CourtListener) already carry real
    URLs and must fall through untouched.
    """
    match = _ARTICLE_RE.search(link or "")
    return match.group(1) if match else None


def _fetch(url: str, timeout: int, user_agent: str, data: bytes | None = None) -> str:
    headers = {"User-Agent": user_agent}
    if data is not None:
        headers["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8"
    request = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", "replace")


def _payload(art_id: str, timestamp: str, signature: str) -> bytes:
    """The request body the article page's own script sends.

    The nested-JSON-inside-JSON and the run of magic constants are Google's
    wire format, not ours; they are copied verbatim because there is no
    specification to derive them from.
    """
    inner = json.dumps([
        "garturlreq",
        [["X", "X", ["X", "X"], None, None, 1, 1, "US:en", None, 1, None, None,
          None, None, None, 0, 1],
         "X", "X", 1, [1, 1, 1], 1, 1, None, 0, 0, None, 0],
        art_id, int(timestamp), signature,
    ])
    outer = json.dumps([[["Fbv4je", inner, None, "generic"]]])
    return urllib.parse.urlencode({"f.req": outer}).encode()


def resolve_one(link: str, *, timeout: int, user_agent: str) -> str | None:
    """Canonical publisher URL for one Google News link, or None.

    Returns None on every failure mode — not a Google link, no signature on the
    page, endpoint changed shape, network error. Callers keep the original link.
    """
    art_id = article_id(link)
    if not art_id:
        return None
    try:
        html = _fetch(link, timeout, user_agent)
        signature = _SIGNATURE_RE.search(html)
        timestamp = _TIMESTAMP_RE.search(html)
        if not (signature and timestamp):
            return None
        body = _payload(art_id, timestamp.group(1), signature.group(1))
        raw = _fetch(BATCH_URL, timeout, user_agent, data=body)
        match = _RESULT_RE.search(raw)
        if not match:
            return None
        url = match.group(1).encode().decode("unicode_escape")
        return url if url.startswith("http") else None
    except Exception:  # noqa: BLE001 - see module docstring: never break the run
        return None


def resolve_evidence(
    results: Iterable[Any],
    cache: dict[str, str],
    config: dict[str, Any],
    *,
    timeout: int,
    user_agent: str,
) -> dict[str, int]:
    """Populate ``entry.canonical_link`` for the evidence about to be published.

    Deliberately called on the *published* evidence rather than at ingest: a run
    fetches hundreds of entries and publishes a couple of dozen, and there is no
    reason to spend requests on articles that never reach the dashboard.

    Mutates entries in place. Returns counts for the run report.
    """
    stats = {"cached": 0, "resolved": 0, "failed": 0, "skipped": 0}
    if not config.get("enabled", True):
        return stats

    budget = int(config.get("max_requests_per_run", 40))
    delay = float(config.get("delay_seconds", 1.0))
    spent = 0

    for result in results:
        for entry in getattr(result, "evidence", []) or []:
            link = getattr(entry, "link", "") or ""
            art_id = article_id(link)
            if not art_id:
                # Already a real URL (primary sources). Treat it as canonical so
                # consumers can read one field instead of two.
                entry.canonical_link = link
                stats["skipped"] += 1
                continue
            if art_id in cache:
                entry.canonical_link = cache[art_id]
                stats["cached"] += 1
                continue
            if spent >= budget:
                stats["failed"] += 1
                continue
            if spent and delay:
                time.sleep(delay)
            spent += 1
            url = resolve_one(link, timeout=timeout, user_agent=user_agent)
            if url:
                cache[art_id] = url
                entry.canonical_link = url
                stats["resolved"] += 1
            else:
                stats["failed"] += 1
    return stats
