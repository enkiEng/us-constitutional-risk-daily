# Constitutional Risk Dashboard Deep Dive

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

Domain points:

`domain_points = domain_weight * (average_signal_severity / 4)`

Total score:

`total_score = sum(all domain_points)` clamped to `0-100`.

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
