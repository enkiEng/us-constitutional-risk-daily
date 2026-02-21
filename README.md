# US Constitutional Risk Daily

Public daily early-warning dashboard for constitutional-order risk in the United States.

This is *HIGHLY SUBJECTIVE!*  **Ideally, this risk metric should stay near "0" in a normally functioning democracy.**

- Score range: `0-100`
- `0`: baseline institutional noise
- `100`: constitutional failure / overturn conditions
- Method: weighted domain model with explicit warning signals and daily evidence pulls

## What this repo publishes

- Public webpage (`site/index.html`) for daily tracking
- Daily markdown report (`outputs/constitutional-risk-daily.md`)
- Historical time series (`data/constitutional_risk_history.csv`)
- Per-signal daily history (`data/constitutional_signal_scores.csv`)
- Latest machine-readable snapshot (`data/latest_dashboard.json`)

## GitHub -> GitLab Bluesky Trigger

The daily GitHub Action (`.github/workflows/daily-update.yml`) now triggers
`enkiEng/bluesky-scheduler` after each run:

- Success path: sends dashboard URL + status/score/band/date from
  `data/latest_dashboard.json`.
- Failure path: sends `DASHBOARD_STATUS=failed` with fallback URL/metadata.

Required GitHub secret:

- `GITLAB_TRIGGER_TOKEN`: pipeline trigger token created in the GitLab
  `bluesky-scheduler` project.

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
- `DASHBOARD_DELTA_PREVIOUS_DAY`
- `DASHBOARD_CONFIDENCE`
- `DASHBOARD_DATE`
- `DASHBOARD_TAGS`
- `DASHBOARD_REPOSITORY`
- `DASHBOARD_RUN_ID`
