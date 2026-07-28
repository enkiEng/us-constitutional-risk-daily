# Constitutional Risk Dashboard Deep Dive

> **Methodology v2.** The published index now uses escalation-max domain
> aggregation, trip-wire floors, and an optional AI event-extraction layer.
> The v1 score history is frozen at `data/constitutional_risk_history.csv`; the
> live series is `data/constitutional_risk_history_v2.csv`. See
> [`constitutional-risk-improvement-proposal.md`](constitutional-risk-improvement-proposal.md)
> for why each change was made.

## Objective

Create a daily, structured early-warning measure of constitutional-order risk on a `0-100` scale:

- `0` = no meaningful constitutional-order stress
- `100` = constitutional failure / overturn conditions

This is an indicator model, not proof. It is designed to enforce consistent reasoning about incentives, institutions, and observable events.

## Scoring Architecture

Signal severity uses a `0-4` scale:

- `0` Green: no material signal
- `1` Watch: isolated or weak signal
- `2` Yellow: repeated or credible stress signal
- `3` Orange: serious multi-source stress or direct high-severity trigger
- `4` Red: confirmed structural constitutional failure condition

Domain severity (v2 — escalation-max):

`domain_severity = max(mean_signal_severity, max_signal_severity - 1)`

This leaves ordinary watch-level noise (several signals at `1`) at its mean so
baseline days are not inflated, but the moment any one signal reaches
orange/red it pulls the domain toward that signal's severity instead of
averaging it away. In v1 a single confirmed red event contributed only a small
fraction of its domain's weight; three simultaneous red-level crisis events
scored ~15/100 ("Baseline"). Under v2 the same three events reach the crisis
bands. (Setting `domain_aggregation.method` to `"mean"` restores the v1
formula for comparison.)

Domain points:

`domain_points = domain_weight * (domain_severity / 4)`

Total score:

`total_score = max( sum(all domain_points), active_trip_wire_floor )` clamped to `0-100`.

## Trip-Wires

Some events are catastrophic on their own and should not have to accumulate
weighted points to register. A trip-wire raises the whole index to a floor band
when a listed signal reaches a configured severity — e.g. a confirmed defied
court order floors the index at 45 ("Crisis Trajectory"), a cancelled election
or martial law tied to an electoral dispute floors it at 60 ("Acute
Constitutional Crisis"). Trip-wires are configured in
`config/constitutional_risk_config.json` under `trip_wires.rules` and the fired
rules are surfaced on the page and in the daily report.

## AI Event Extraction (optional)

The weakest part of v1 was turning articles into severities by counting keyword
hits — which measures media volume, not whether an event happened, and is
fooled by negation, hypotheticals, opinion, historical retrospectives, and
foreign coverage. When the `anthropic` SDK is installed and `ANTHROPIC_API_KEY`
is set, `scripts/ai_classifier.py` reads each candidate article and returns a
schema-validated judgment: is it US-domestic? did the event actually occur (vs
hypothetical/denied/historical/opinion)? which signal? severity `0-4` against
the rubric? primary source? one-line rationale? Severity is then derived from
*confirmed events* instead of raw coverage volume, and the model's rationale is
shown on the page.

Design guarantees:

- The model runs only at the extraction step; aggregation and the published
  number stay pure Python, so every score is reproducible from the stored
  judgments.
- If the SDK or key is unavailable the run falls back to the keyword scorer and
  labels the extraction mode accordingly (the page shows an "AI extraction
  unavailable" badge).
- Per-(signal, article) judgments are cached in
  `data/ai_classification_cache.json` so the same article is not re-billed
  across daily runs.
- Only the AI path (or a manual override) may assign a red-level `4`, and a `4`
  only stands when anchored to a primary source or independently corroborated;
  the keyword path is capped at `auto_max_severity`.

## Methodology Versioning

`methodology_version` in the config records the scoring generation. The v1 CSV
is kept frozen so historical trends are not silently redefined; the v2 series
was seeded from the stored per-signal severities (re-aggregated under v2, no new
data) via `scripts/backfill_v2_history.py` so the public trend is continuous.

## Domain Weights (100 total)

| Domain | Weight |
|---|---:|
| Elections and Transfer of Power | 22 |
| Opposition Rights and Political Pluralism | 14 |
| Judicial Independence and Rule of Law | 15 |
| Executive Constraints and Emergency Powers | 13 |
| Civil Service and Agency Independence | 10 |
| Civil Liberties and Information Environment | 10 |
| Security Sector Neutrality | 8 |
| Federalism and Legislative Oversight | 8 |

## Signal Catalog

### Elections and Transfer of Power
- Election Certification Interference
- Election Administration Capture
- Election Delay or Cancellation
- Alternate Elector Scheme Activity

### Opposition Rights and Political Pluralism
- Politicized Prosecution of Opposition
- Opposition Ballot Exclusion
- Retaliation Architecture

### Judicial Independence and Rule of Law
- Judge Intimidation Campaign
- Court Order Noncompliance
- Targeted Jurisdiction Stripping

### Executive Constraints and Emergency Powers
- Emergency Powers Expansion
- Legislative Bypass by Executive
- Martial Law or Military Governance Language

### Civil Service and Agency Independence
- Civil Service Purge / Schedule F
- Independent Agency Capture
- Inspector General Retaliation

### Civil Liberties and Information Environment
- Press Restrictions or Retaliation
- Political Speech Criminalization or Surveillance

### Security Sector Neutrality
- Domestic Military Use in Political Conflict
- Security Sector Loyalty Tests

### Federalism and Legislative Oversight
- Federal Preemption of State Election Authority
- Legislative Oversight Obstruction

## Alert Bands

| Score | Band |
|---:|---|
| 0-14 | Baseline Institutional Noise |
| 15-29 | Elevated Strain |
| 30-44 | Serious Constitutional Stress |
| 45-59 | Crisis Trajectory |
| 60-74 | Acute Constitutional Crisis |
| 75-89 | Near-Failure |
| 90-100 | Constitutional Failure / Overturn |

## Daily Automation Workflow

1. Pull fresh query-based evidence from RSS feeds.
2. Score each signal automatically using hit volume, source diversity, and severe/critical terms.
3. Apply persistence decay so risk fades gradually instead of hard-resetting daily.
4. Apply optional manual overrides for legally confirmed high-severity events.
5. Write:
   - `outputs/constitutional-risk-daily.md`
   - `data/constitutional_risk_history.csv`
   - `data/constitutional_signal_scores.csv`
   - `data/latest_signal_state.json`

## Why Manual Overrides Exist

Some red-level constitutional events should be scored from primary legal evidence (court orders, statutes, official directives), not news frequency. Manual overrides are the explicit mechanism for this.

## Guardrails

- Avoid interpreting correlation as causation.
- Treat single-source spikes as provisional.
- Validate high-severity shifts with primary documents.
- Review false positives monthly and tune keywords/queries in `config/constitutional_risk_config.json`.
