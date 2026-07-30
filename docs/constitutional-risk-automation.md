# Automation Guide

## Daily pipeline

`scripts/run_daily.py` runs:

1. `scripts/update_constitutional_risk.py`
2. `scripts/render_site.py`

`run_daily.py` runs the keyword scorer plus, when configured, the AI event
extraction layer (below). It does **not** run the one-time v2 history backfill.

## AI event extraction (optional)

The scorer uses an LLM to confirm whether each candidate event actually
occurred before scoring it (see the deep-dive). It activates only when both are
present:

1. The `anthropic` Python SDK is installed (`pip install anthropic`).
2. Credentials are available — set the `ANTHROPIC_API_KEY` GitHub Actions
   secret (or `ANTHROPIC_AUTH_TOKEN`).

If either is missing the run automatically falls back to the deterministic
keyword scorer and marks the day's extraction mode as `keyword`. Tune the model
and limits under the `ai` block in
`config/constitutional_risk_config.json` (default model `claude-haiku-4-5`,
chosen because this is a high-volume, short-input classification task). Set
`ai.enabled` to `false` to disable the layer entirely.

## Primary-source ingestion

Alongside the Google News feeds, each signal that declares a `primary_sources`
block in the config is checked against the official record:

- **Federal Register** (`federalregister.gov/api/v1`) — executive orders,
  presidential memoranda and proclamations, agency rules and notices.
- **CourtListener** (`courtlistener.com/api/rest/v4`) — federal docket entries
  via RECAP, and published opinions.

Both APIs are free and work without a key. `COURTLISTENER_API_TOKEN` is
optional; requests are spaced by
`primary_sources.courtlistener.request_delay_seconds` either way and a 429 is
retried with backoff.

CourtListener's documented limits for authenticated callers are **5 requests
per minute, 50 per hour and 125 per day** on a rolling window, so the spacing
is set to ~13s. Ten signals use about ten of the daily budget and add roughly
two minutes to the job. To get a token: create a CourtListener account and copy
it from <https://www.courtlistener.com/profile/api-token/>, then store it as the
`COURTLISTENER_API_TOKEN` GitHub Actions secret. Raising the limits further
requires a Free Law Project membership.

Documents are merged into the same evidence list as news items and judged by
the same AI extraction layer, but they carry `source_tier="primary"`. That tier
does one thing to the score: it satisfies the anchor requirement for a
red-level (4) severity on its own, where a news item still needs two
independent publishers. In the keyword fallback path a primary document gets no
special standing — without the AI layer the pipeline cannot tell whether the
document is on point.

Two query quirks are worth knowing before editing the config:

- Federal Register `conditions[term]` is an **AND over every word** and has no
  boolean OR, so each signal supplies a **list** of tight quoted phrases and
  each is issued as its own request. A single long phrase matches nothing.
  Type filters (`PRESDOCU`, `RULE`, `PRORULE`, `NOTICE`) do most of the
  precision work, since the search hits full document text.
- CourtListener's `party:` field does not combine with phrase queries in
  parent-child RECAP searches — it silently returns zero results. Government-
  party filtering is therefore applied in Python against the party list the API
  returns (`government_party_only`, on by default for RECAP).

`judge_intimidation_campaign` and `jurisdiction_stripping_targeted` have no
primary-source block on purpose: their authoritative record is congressional
action or informal conduct that neither API covers, and a vague query there
would return noise rather than evidence.

## Methodology versioning / backfill

The live series is `data/constitutional_risk_history_v2.csv`; the v1 CSV is
frozen. To (re)seed the v2 series from the stored per-signal severities after a
config change:

```bash
python scripts/backfill_v2_history.py
```

This re-aggregates existing severities under the current v2 formula and does not
touch the v1 CSV.

## Manual override file

Edit:

- `data/manual_signal_overrides.json`

Override schema:

- `severity`: float `0-4`
- `mode`: `"set"` or `"max"`
- `note`: explanation for audit trail
- `expires`: optional `YYYY-MM-DD`

## GitHub Pages deploy

Workflow:

- `.github/workflows/daily-update.yml`

Required repo settings after first push:

1. Open repository settings.
2. Go to `Pages`.
3. Set source to `GitHub Actions`.
4. Save.

## Timezone

Score generation timestamp is UTC in the report payload.

If needed, change timezone metadata in:

- `config/constitutional_risk_config.json`
