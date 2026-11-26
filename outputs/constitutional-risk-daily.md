# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-26 12:30:27 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **8 / 100** (Baseline Institutional Noise)
- Previous day delta: **-4.0**
- Delta vs 7-day average: **-0.9**
- Data status: **No successful feed pulls. Treat today's numeric score as unavailable/provisional.**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.65 | 3.57 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.65 | 2.11 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.10 | 2.75 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 1.65 (Watch) | keyword | 0 | 0 |
| Legislative Bypass by Executive | executive_constraints | 1.65 (Watch) | keyword | 0 | 0 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.65 (Watch) | keyword | 0 | 0 |
| Public Funds for Political Promotion | civil_liberties_information | 1.65 (Watch) | keyword | 0 | 0 |

## Evidence Samples

### Election Administration Capture
- No fresh evidence links in the current lookback window.
### Legislative Bypass by Executive
- No fresh evidence links in the current lookback window.
### Press Restrictions or Retaliation
- No fresh evidence links in the current lookback window.
### Public Funds for Political Promotion
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 0
- Query feeds failed: 25
- Primary-source lookups: 22 signals, 0 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **Low**
- Fetch errors:
  - election_certification_interference: HTTP Error 503: Service Unavailable
  - election_certification_interference: courtlistener: HTTP Error 401: Unauthorized
  - election_administration_capture: HTTP Error 503: Service Unavailable
  - election_administration_capture: federal_register ["election administration"]: HTTP Error 403: Forbidden
  - election_administration_capture: federal_register ["voter registration list"]: HTTP Error 403: Forbidden
  - election_delay_or_cancellation: HTTP Error 503: Service Unavailable
  - election_delay_or_cancellation: courtlistener: HTTP Error 401: Unauthorized
  - alternate_elector_scheme: HTTP Error 503: Service Unavailable
  - alternate_elector_scheme: courtlistener: HTTP Error 401: Unauthorized
  - politicized_prosecution_opposition: HTTP Error 503: Service Unavailable

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
