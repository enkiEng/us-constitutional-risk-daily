# Automation Guide

## Daily pipeline

`scripts/run_daily.py` runs:

1. `scripts/update_constitutional_risk.py`
2. `scripts/render_site.py`

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
