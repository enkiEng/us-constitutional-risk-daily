# US Constitutional Risk Daily

Public daily early-warning dashboard for constitutional-order risk in the United States.

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

## Local run

```bash
python3 -m venv .venv
.venv/bin/python scripts/run_daily.py
```

## GitHub Actions automation

This repo includes `.github/workflows/daily-update.yml`:

- Scheduled daily run
- Manual run with `workflow_dispatch`
- Recomputes score and regenerates site
- Commits updated `data/`, `outputs/`, and `site/`
- Deploys `site/` via GitHub Pages

## Domain mapping note

This repository will have its own Pages URL:

- `https://enkieng.github.io/us-constitutional-risk-daily/`

Your custom root domain (`https://progressive-mandate.org/`) is currently served from `enkiEng/project2029`.

If you want this dashboard specifically at:

- `https://progressive-mandate.org/US-constitutional-risk-daily`

then `project2029` must route that path (for example by adding a link/redirect page or copying this built `site/` output into a folder there).

## Files

- `config/constitutional_risk_config.json`: domains, signals, thresholds, weights
- `scripts/update_constitutional_risk.py`: daily scoring engine
- `scripts/render_site.py`: static site renderer
- `scripts/run_daily.py`: one-command pipeline
- `docs/constitutional-risk-deep-dive.md`: model details
