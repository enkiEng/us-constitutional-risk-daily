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
