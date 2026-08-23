# Constitutional Risk Dashboard (0-100)

- Generated: 2026-08-23 13:05:05 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **4 / 100** (Baseline Institutional Noise)
- Previous day delta: **-1.0**
- Delta vs 7-day average: **-2.5**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.00 | 0.00 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.43 | 1.41 |
| Civil Service and Agency Independence | 10 | 1.10 | 2.75 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Independent Agency Capture | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 1 |
| Emergency Powers Expansion | executive_constraints | 1.30 (Watch) | keyword | 0 | 0 |
| Civil Service Purge / Schedule F | civil_service_integrity | 1.30 (Watch) | keyword | 0 | 0 |

## Evidence Samples

### Independent Agency Capture
- Assessment: This is an official DOJ OLC opinion concluding that the Foreign Service Grievance Board's structure violates the Appointments Clause due to insufficient oversight of inferior officers. This represents a real legal finding that an independent agency's decision-making authority lacks adequate political accountability safeguards—a direct match to the signal. However, severity is capped at 2 because this is an OLC opinion (legal analysis) rather than a confirmed structural breakdown or defiance of court order. The opinion identifies a constitutional weakness but does not demonstrate that safeguards have already been dismantled or that the agency has begun operating in violation of the ruling.
- [courtlistener.com] **[official record]** Constitutionality of the Foreign Service Grievance Board's Oversight Authority (2026-08-20) - https://www.courtlistener.com/opinion/10954524/constitutionality-of-the-foreign-service-grievance-boards-oversight/

### Emergency Powers Expansion
- No fresh evidence links in the current lookback window.
### Civil Service Purge / Schedule F
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 22
- Query feeds successful: 22
- Query feeds failed: 0
- Primary-source lookups: 20 signals, 11 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 1
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
