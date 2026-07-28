# Constitutional Risk Dashboard (0-100)

- Generated: 2026-07-28 02:36:33 UTC
- Methodology: **v2** (extraction: keyword volume (AI extraction unavailable))
- Score: **4 / 100** (Baseline Institutional Noise)
- Previous day delta: **-7.0**
- Delta vs 7-day average: **-7.9**
- Data status: **No successful feed pulls. Treat today's numeric score as unavailable/provisional.**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.00 | 0.00 |
| Judicial Independence and Rule of Law | 15 | 0.10 | 0.37 |
| Opposition Rights and Political Pluralism | 14 | 0.10 | 0.35 |
| Executive Constraints and Emergency Powers | 13 | 0.53 | 1.73 |
| Civil Service and Agency Independence | 10 | 0.20 | 0.50 |
| Civil Liberties and Information Environment | 10 | 0.47 | 1.19 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Martial Law or Military Governance Language | executive_constraints | 1.30 (Watch) | keyword | 0 | 0 |
| Press Restrictions or Retaliation | civil_liberties_information | 0.95 (Watch) | keyword | 0 | 0 |
| Independent Agency Capture | civil_service_integrity | 0.60 (Green) | keyword | 0 | 0 |
| Opposition Ballot Exclusion | opposition_pluralism | 0.30 (Green) | keyword | 0 | 0 |
| Judge Intimidation Campaign | judiciary_rule_of_law | 0.30 (Green) | keyword | 0 | 0 |
| Legislative Bypass by Executive | executive_constraints | 0.30 (Green) | keyword | 0 | 0 |

## Evidence Samples

### Martial Law or Military Governance Language
- No fresh evidence links in the current lookback window.
### Press Restrictions or Retaliation
- No fresh evidence links in the current lookback window.
### Independent Agency Capture
- No fresh evidence links in the current lookback window.
### Opposition Ballot Exclusion
- No fresh evidence links in the current lookback window.
### Judge Intimidation Campaign
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 22
- Query feeds successful: 0
- Query feeds failed: 22
- Evidence extraction: keyword volume (AI extraction unavailable)
- Confidence: **Low**
- Fetch errors:
  - election_certification_interference: <urlopen error Tunnel connection failed: 403 Forbidden>
  - election_administration_capture: <urlopen error Tunnel connection failed: 403 Forbidden>
  - election_delay_or_cancellation: <urlopen error Tunnel connection failed: 403 Forbidden>
  - alternate_elector_scheme: <urlopen error Tunnel connection failed: 403 Forbidden>
  - politicized_prosecution_opposition: <urlopen error Tunnel connection failed: 403 Forbidden>
  - opposition_ballot_exclusion: <urlopen error Tunnel connection failed: 403 Forbidden>
  - retaliation_architecture: <urlopen error Tunnel connection failed: 403 Forbidden>
  - judge_intimidation_campaign: <urlopen error Tunnel connection failed: 403 Forbidden>
  - court_order_noncompliance: <urlopen error Tunnel connection failed: 403 Forbidden>
  - jurisdiction_stripping_targeted: <urlopen error Tunnel connection failed: 403 Forbidden>

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
