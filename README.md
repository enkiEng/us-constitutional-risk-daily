# US Constitutional Risk Daily

Public daily early-warning dashboard for constitutional-order risk in the United States.

This is *HIGHLY SUBJECTIVE!*  **Ideally, this risk metric should stay near "0" in a normally functioning democracy.**

- Score range: `0-100`
- `0`: baseline institutional noise
- `100`: constitutional failure / overturn conditions
- Method: weighted domain model with explicit warning signals and daily evidence pulls

### Methodology v2

The scoring engine is now **v2**:

- **Escalation-max domain aggregation** — `max(mean, max−1)` per domain, so one
  confirmed red-level signal is no longer averaged away (the v1 flaw where three
  simultaneous crisis events scored only ~15/100).
- **Trip-wires** — a single confirmed catastrophic event (defied court order,
  cancelled election, martial law) floors the whole index at a crisis band.
- **Optional AI event extraction** — when `ANTHROPIC_API_KEY` is set, each
  article is read by a model that confirms whether the event actually occurred
  (vs hypothetical / denied / historical / foreign) before it is scored;
  otherwise the run falls back to the keyword scorer.
- **Primary-source ingestion** — signals are also checked against the official
  record: the **Federal Register** (executive orders, presidential memoranda
  and proclamations, agency rules and notices) and **CourtListener** (federal
  dockets via RECAP, published opinions). Both APIs are free and keyless. These
  documents are judged alongside news items but can anchor a red-level severity
  on their own, where a news item still needs two independent publishers.

See [`docs/constitutional-risk-deep-dive.md`](docs/constitutional-risk-deep-dive.md)
and [`docs/constitutional-risk-improvement-proposal.md`](docs/constitutional-risk-improvement-proposal.md).

## What this repo publishes

- Public webpage (`site/index.html`) for daily tracking
- Daily markdown report (`outputs/constitutional-risk-daily.md`)
- Live v2 time series (`data/constitutional_risk_history_v2.csv`)
- Frozen v1 time series (`data/constitutional_risk_history.csv`)
- Per-signal daily history (`data/constitutional_signal_scores.csv`)
- Latest machine-readable snapshot (`data/latest_dashboard.json`)

### Evidence links

Google News RSS hands out redirect links of 260-340 characters rather than the
publisher's URL. `scripts/resolve_links.py` resolves the published evidence to
real publisher URLs (typically 100-140 characters) and the dashboard carries
both:

- `evidence[].link` — the original Google redirect, never rewritten, so the
  provenance of a citation stays intact and dedupe keys stay stable
- `evidence[].canonical_link` — the resolved publisher URL, or `null` when
  resolution was not attempted or did not succeed

Consumers should prefer `canonical_link` and fall back to `link`. This matters
beyond tidiness for anything with a length budget: a Bluesky post is capped at
300 graphemes and counts the whole URL against it, so an unresolved redirect
cannot fit in a post at all.

Resolution uses an undocumented Google endpoint and is expected to break
eventually. Every failure degrades to the original link and never fails the
run; failures are reported in the run's `fetch_errors`. Results are cached
by article id in `data/link_resolution_cache.json` and never expire.

## GitHub -> GitLab Bluesky Trigger

The daily GitHub Action (`.github/workflows/daily-update.yml`) now triggers
`enkiEng/bluesky-scheduler` after each run:

- Success path: sends dashboard URL + status/score/band/date from
  `data/latest_dashboard.json`.
- Failure path: sends `DASHBOARD_STATUS=failed` with fallback URL/metadata.

Required GitHub secret:

- `GITLAB_TRIGGER_TOKEN`: pipeline trigger token created in the GitLab
  `bluesky-scheduler` project.

Optional GitHub secrets:

- `ANTHROPIC_API_KEY`: enables the AI event-extraction layer.
- `COURTLISTENER_API_TOKEN`: raises the CourtListener rate limit. Primary-source
  ingestion works without it.

Optional GitHub repository variables:

- `GITLAB_PROJECT_ID_OR_PATH`: defaults to `enkieng/bluesky-scheduler`.
  Set this to a numeric GitLab project ID (recommended) or full path.
- `GITLAB_TRIGGER_REF`: defaults to `main`.
- `DASHBOARD_PUBLIC_URL`: defaults to
  `https://progressive-mandate.org/US-constitutional-risk-daily/`.
- `DASHBOARD_TAGS`: optional hashtag string passed through to Bluesky post
  formatting (example: `#ConstitutionalRisk #DemocracyWatch #USPolitics`).

Variables sent to the GitLab trigger:

- `DASHBOARD_URL`
- `DASHBOARD_STATUS` (`live` or `provisional`)
- `DASHBOARD_STATUS` can also be `failed` if the daily workflow errors
- `DASHBOARD_SCORE`
- `DASHBOARD_BAND`
- `DASHBOARD_CEI` (Cumulative Erosion Index, `n/a` on failure)
- `DASHBOARD_CEI_BAND`
- `DASHBOARD_DELTA_PREVIOUS_DAY`
- `DASHBOARD_CONFIDENCE`
- `DASHBOARD_DATE`
- `DASHBOARD_TAGS`
- `DASHBOARD_REPOSITORY`
- `DASHBOARD_RUN_ID`
