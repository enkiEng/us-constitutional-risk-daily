#!/usr/bin/env python3
"""
Primary-source evidence ingestion for the Constitutional Risk Dashboard.

Why this module exists
----------------------
Until now the only evidence feed was Google News RSS. That measures coverage,
and coverage is a lagging, noisy proxy for the thing the index claims to track.
Measured over the first 164 days of the v2 series, no signal ever exceeded
severity 2.0 -- which means every trip-wire in the config was unreachable and
the bands above "Elevated Strain" were decorative. The missing ingredient was
never the aggregation math; it was that the pipeline had no way to *see* the
authoritative record of what the government actually did.

This module adds that record. Two free, keyless, machine-readable sources:

* **Federal Register** (``federalregister.gov/api/v1``) -- executive orders,
  presidential memoranda and proclamations, and agency rules/notices. This is
  where "the executive did a thing" is published as an official act, on the day
  it becomes operative.
* **CourtListener** (``courtlistener.com/api/rest/v4``) -- federal dockets via
  RECAP and published opinions. This is where "someone asked a court to enforce
  its order against the government" appears, weeks before it is a news story.

Documents from these sources are merged into the same per-signal evidence list
as news items and judged by the same AI extraction layer. They differ in one
respect that matters: they carry ``source_tier="primary"``, which lets the
scorer treat them as the primary-source anchor that a red-level (4) severity
requires, instead of demanding two independent news publishers.

Design constraints, matching the rest of the pipeline:

  * Standard library only -- no new dependencies in the daily CI job.
  * Never raise into the caller. Every failure is captured as a string in the
    returned error list so a dead API degrades the run to news-only instead of
    failing the cron.
  * Both APIs work anonymously. ``COURTLISTENER_API_TOKEN`` is optional and only
    raises CourtListener's rate limit; nothing requires a secret to be set.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


UTC = dt.timezone.utc

FEDERAL_REGISTER_ENDPOINT = "https://www.federalregister.gov/api/v1/documents.json"
COURTLISTENER_ENDPOINT = "https://www.courtlistener.com/api/rest/v4/search/"
COURTLISTENER_BASE = "https://www.courtlistener.com"


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

def _get_json(
    url: str,
    *,
    timeout: int,
    user_agent: str,
    headers: dict[str, str] | None = None,
    retries: int = 2,
) -> Any:
    """GET and decode JSON, backing off once or twice on a throttle response.

    CourtListener throttles anonymous callers by burst, and the daily run makes
    a dozen searches back to back. Rather than lose those signals for the day,
    honour ``Retry-After`` when it is offered and otherwise back off linearly.
    """
    request_headers = {"User-Agent": user_agent, "Accept": "application/json"}
    if headers:
        request_headers.update(headers)

    attempt = 0
    while True:
        request = urllib.request.Request(url, headers=request_headers)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            throttled = exc.code in (429, 503)
            if not throttled or attempt >= retries:
                raise
            retry_after = exc.headers.get("Retry-After") if exc.headers else None
            try:
                wait = float(retry_after) if retry_after else 0.0
            except (TypeError, ValueError):
                wait = 0.0
            time.sleep(min(max(wait, 2.0 * (attempt + 1)), 30.0))
            attempt += 1


def _truncate(text: str, limit: int = 600) -> str:
    text = " ".join((text or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def _iso_date(value: Any) -> str | None:
    """Normalize an API date into an ISO 8601 UTC timestamp string."""
    if not value:
        return None
    try:
        parsed = dt.date.fromisoformat(str(value)[:10])
    except ValueError:
        return None
    return dt.datetime(parsed.year, parsed.month, parsed.day, tzinfo=UTC).isoformat()


# ---------------------------------------------------------------------------
# Federal Register
# ---------------------------------------------------------------------------

def _federal_register_query(
    term: str,
    types: list[str],
    *,
    since: dt.date,
    limit: int,
    timeout: int,
    user_agent: str,
    endpoint: str,
) -> tuple[list[dict[str, Any]], list[str]]:
    params: list[tuple[str, str]] = [
        ("per_page", str(max(1, min(int(limit), 20)))),
        ("order", "newest"),
        ("conditions[term]", term),
        ("conditions[publication_date][gte]", since.isoformat()),
    ]
    for field in (
        "title",
        "abstract",
        "html_url",
        "publication_date",
        "type",
        "document_number",
        "agencies",
    ):
        params.append(("fields[]", field))
    for doc_type in types:
        params.append(("conditions[type][]", str(doc_type)))

    url = f"{endpoint}?{urllib.parse.urlencode(params)}"
    try:
        payload = _get_json(url, timeout=timeout, user_agent=user_agent)
    except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
        return [], [f"federal_register [{term}]: {exc}"]

    documents: list[dict[str, Any]] = []
    for item in (payload or {}).get("results", [])[:limit]:
        if not isinstance(item, dict):
            continue
        agencies = [
            str(a.get("name") or a.get("raw_name") or "").strip()
            for a in item.get("agencies", []) or []
            if isinstance(a, dict)
        ]
        agency_text = ", ".join(a for a in agencies if a)
        doc_type = str(item.get("type") or "").strip()
        context = " | ".join(part for part in (doc_type, agency_text) if part)
        abstract = _truncate(str(item.get("abstract") or ""))
        documents.append(
            {
                "title": str(item.get("title") or "").strip(),
                "link": str(item.get("html_url") or "").strip(),
                "summary": f"{context}. {abstract}".strip(". ").strip(),
                "publisher": "federalregister.gov",
                "published": _iso_date(item.get("publication_date")),
                "source": "federal_register",
                "doc_type": doc_type,
            }
        )
    return documents, []


def fetch_federal_register(
    spec: dict[str, Any],
    *,
    since: dt.date,
    limit: int,
    timeout: int,
    user_agent: str,
    endpoint: str = FEDERAL_REGISTER_ENDPOINT,
    delay: float = 0.0,
) -> tuple[list[dict[str, Any]], list[str]]:
    """Fetch Federal Register documents matching a signal's search spec.

    ``spec`` accepts:
        terms -- list of full-text search strings; each is issued as its own
                 request and the results are merged. ``term`` (a single string)
                 is accepted as a shorthand.
        types -- optional list of document type codes: PRESDOCU (presidential
                 documents), RULE, PRORULE (proposed rule), NOTICE

    One request per term is deliberate. ``conditions[term]`` is an AND across
    every word supplied and has no boolean OR, so a single long phrase like
    "national emergency declaration emergency powers" matches nothing at all.
    Quoted phrases work, so a list of tight phrases is how you actually express
    "any of these". Type filters matter as much as the phrase: the search hits
    full document text, so an unfiltered "National Guard" surfaces procurement
    lists, while the same phrase restricted to PRESDOCU surfaces the order.
    """
    raw_terms = spec.get("terms")
    if raw_terms is None:
        raw_terms = [spec.get("term", "")]
    terms = [str(t).strip() for t in raw_terms if str(t).strip()]
    if not terms:
        return [], []

    types = [str(t) for t in (spec.get("types") or [])]
    documents: list[dict[str, Any]] = []
    errors: list[str] = []
    seen: set[str] = set()

    for index, term in enumerate(terms):
        docs, errs = _federal_register_query(
            term,
            types,
            since=since,
            limit=limit,
            timeout=timeout,
            user_agent=user_agent,
            endpoint=endpoint,
        )
        errors.extend(errs)
        for doc in docs:
            key = doc.get("link", "")
            if key and key not in seen:
                seen.add(key)
                documents.append(doc)
        if delay and index < len(terms) - 1:
            time.sleep(delay)

    documents.sort(key=lambda d: str(d.get("published") or ""), reverse=True)
    return documents[:limit], errors


# ---------------------------------------------------------------------------
# CourtListener
# ---------------------------------------------------------------------------

def _courtlistener_headers(token_env: str) -> dict[str, str]:
    token = os.environ.get(token_env, "").strip()
    return {"Authorization": f"Token {token}"} if token else {}


# A docket only interests this dashboard when a government body is a party to
# it. Without this filter a search for "motion to enforce" returns landlord
# disputes and bankruptcy adversary proceedings that merely use the phrase.
# CourtListener's own ``party:`` field does not combine with phrase queries in
# parent-child RECAP searches (it silently returns nothing), so the filter is
# applied here against the party list the API already returns.
DEFAULT_GOVERNMENT_PARTY_PATTERNS = [
    "united states",
    "u.s. ",
    "usa",
    "department of",
    "secretary",
    "attorney general",
    "administrator",
    "commissioner",
    "director",
    "warden",
    "bureau of",
    "agency",
    "commission",
    "board of",
    "office of",
    "federal",
    "national",
    "state of",
    "county",
    "city of",
]


def _is_government_matter(item: dict[str, Any], patterns: list[str]) -> bool:
    parties = [str(p) for p in (item.get("party") or []) if p]
    haystack = " | ".join(parties + [str(item.get("caseName") or "")]).lower()
    return any(pattern in haystack for pattern in patterns)


def _recap_document(item: dict[str, Any]) -> dict[str, Any]:
    """Flatten a RECAP docket hit into a single evidence document."""
    case_name = str(item.get("caseName") or "").strip()
    court = str(item.get("court") or "").strip()
    docket_number = str(item.get("docketNumber") or "").strip()

    entries = [d for d in item.get("recap_documents", []) or [] if isinstance(d, dict)]
    descriptions = [
        _truncate(str(d.get("description") or d.get("short_description") or ""), 300)
        for d in entries
    ]
    descriptions = [d for d in descriptions if d]

    link_path = ""
    if entries and entries[0].get("absolute_url"):
        link_path = str(entries[0]["absolute_url"])
    elif item.get("docket_absolute_url"):
        link_path = str(item["docket_absolute_url"])

    filed = None
    if entries and entries[0].get("entry_date_filed"):
        filed = entries[0]["entry_date_filed"]
    filed = filed or item.get("dateFiled")

    context = " | ".join(part for part in (court, docket_number) if part)
    body = " ".join(descriptions[:3])
    cause = str(item.get("cause") or "").strip()
    summary = ". ".join(part for part in (context, body or cause) if part)

    return {
        "title": case_name or "(docket entry)",
        "link": f"{COURTLISTENER_BASE}{link_path}" if link_path else "",
        "summary": _truncate(summary),
        "publisher": "courtlistener.com",
        "published": _iso_date(filed),
        "source": "courtlistener",
        "doc_type": "docket_entry",
    }


def _opinion_document(item: dict[str, Any]) -> dict[str, Any]:
    """Flatten a published-opinion hit into a single evidence document."""
    case_name = str(item.get("caseName") or "").strip()
    court = str(item.get("court") or "").strip()
    docket_number = str(item.get("docketNumber") or "").strip()
    opinions = [o for o in item.get("opinions", []) or [] if isinstance(o, dict)]
    snippet = _truncate(str(opinions[0].get("snippet") or "")) if opinions else ""
    context = " | ".join(part for part in (court, docket_number) if part)
    return {
        "title": case_name or "(opinion)",
        "link": (
            f"{COURTLISTENER_BASE}{item['absolute_url']}"
            if item.get("absolute_url")
            else ""
        ),
        "summary": _truncate(". ".join(part for part in (context, snippet) if part)),
        "publisher": "courtlistener.com",
        "published": _iso_date(item.get("dateFiled")),
        "source": "courtlistener",
        "doc_type": "opinion",
    }


def fetch_courtlistener(
    spec: dict[str, Any],
    *,
    since: dt.date,
    limit: int,
    timeout: int,
    user_agent: str,
    endpoint: str = COURTLISTENER_ENDPOINT,
    token_env: str = "COURTLISTENER_API_TOKEN",
    government_party_patterns: list[str] | None = None,
) -> tuple[list[dict[str, Any]], list[str]]:
    """Fetch CourtListener search hits matching a signal's search spec.

    ``spec`` accepts:
        query        -- CourtListener search syntax (required)
        search_type  -- "r" for RECAP dockets (default), "o" for opinions
        courts       -- optional list of court ids (e.g. ["dcd", "ca9"])
        government_party_only -- keep only dockets with a government party
                        (default True for RECAP, False for opinions)
    """
    query = str(spec.get("query", "")).strip()
    if not query:
        return [], []

    search_type = str(spec.get("search_type", "r")).strip().lower()
    if search_type not in {"r", "o"}:
        search_type = "r"

    params = {
        "q": query,
        "type": search_type,
        "order_by": "dateFiled desc",
        "filed_after": since.strftime("%m/%d/%Y"),
    }
    courts = [str(c).strip() for c in (spec.get("courts") or []) if str(c).strip()]
    if courts:
        params["court"] = " ".join(courts)

    url = f"{endpoint}?{urllib.parse.urlencode(params)}"
    try:
        payload = _get_json(
            url,
            timeout=timeout,
            user_agent=user_agent,
            headers=_courtlistener_headers(token_env),
        )
    except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
        return [], [f"courtlistener: {exc}"]

    government_only = bool(spec.get("government_party_only", search_type == "r"))
    patterns = [
        p.lower()
        for p in (government_party_patterns or DEFAULT_GOVERNMENT_PARTY_PATTERNS)
    ]

    flatten = _recap_document if search_type == "r" else _opinion_document
    documents: list[dict[str, Any]] = []
    for item in (payload or {}).get("results", []):
        if not isinstance(item, dict):
            continue
        if government_only and not _is_government_matter(item, patterns):
            continue
        documents.append(flatten(item))
        if len(documents) >= limit:
            break
    return documents, []


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def is_enabled(cfg: dict[str, Any]) -> bool:
    return bool((cfg or {}).get("enabled", False))


def fetch_for_signal(
    signal: dict[str, Any],
    cfg: dict[str, Any],
    *,
    today: dt.date,
    timeout: int,
    user_agent: str,
) -> tuple[list[dict[str, Any]], list[str]]:
    """Return (documents, errors) for one signal's declared primary sources.

    A signal opts in by declaring a ``primary_sources`` block; signals without
    one are skipped entirely, so this adds no requests for the signals where an
    official record would not exist anyway.
    """
    if not is_enabled(cfg):
        return [], []

    spec = signal.get("primary_sources") or {}
    if not isinstance(spec, dict) or not spec:
        return [], []

    lookback = int(cfg.get("lookback_days", 7))
    since = today - dt.timedelta(days=max(1, lookback))
    limit = int(cfg.get("max_documents_per_source", 8))
    default_delay = float(cfg.get("request_delay_seconds", 0.0))

    documents: list[dict[str, Any]] = []
    errors: list[str] = []

    fr_cfg = cfg.get("federal_register", {}) or {}
    fr_spec = spec.get("federal_register")
    if fr_cfg.get("enabled", True) and isinstance(fr_spec, dict):
        fr_delay = float(fr_cfg.get("request_delay_seconds", default_delay))
        docs, errs = fetch_federal_register(
            fr_spec,
            since=since,
            limit=limit,
            timeout=timeout,
            user_agent=user_agent,
            endpoint=str(fr_cfg.get("endpoint", FEDERAL_REGISTER_ENDPOINT)),
            delay=fr_delay,
        )
        documents.extend(docs)
        errors.extend(f"{signal.get('id', '?')}: {e}" for e in errs)
        if fr_delay:
            time.sleep(fr_delay)

    cl_cfg = cfg.get("courtlistener", {}) or {}
    cl_spec = spec.get("courtlistener")
    if cl_cfg.get("enabled", True) and isinstance(cl_spec, dict):
        docs, errs = fetch_courtlistener(
            cl_spec,
            since=since,
            limit=limit,
            timeout=timeout,
            user_agent=user_agent,
            endpoint=str(cl_cfg.get("endpoint", COURTLISTENER_ENDPOINT)),
            token_env=str(cl_cfg.get("token_env", "COURTLISTENER_API_TOKEN")),
            government_party_patterns=cl_cfg.get("government_party_patterns"),
        )
        documents.extend(docs)
        errors.extend(f"{signal.get('id', '?')}: {e}" for e in errs)
        # CourtListener throttles anonymous callers by burst, so it gets its own
        # (longer) spacing knob; set COURTLISTENER_API_TOKEN to lift the limit.
        cl_delay = float(cl_cfg.get("request_delay_seconds", default_delay))
        if cl_delay:
            time.sleep(cl_delay)

    # Drop anything without a usable identity or link; an evidence item the
    # reader cannot click is not evidence.
    return [d for d in documents if d.get("title") and d.get("link")], errors
