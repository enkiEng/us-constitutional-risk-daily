# Constitutional Risk Dashboard (0-100)

- Generated: 2026-08-20 13:14:39 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **7 / 100** (Baseline Institutional Noise)
- Previous day delta: **0.0**
- Delta vs 7-day average: **-2.9**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.15 | 0.82 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 1 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Alternate Elector Scheme Activity | elections_transfer | 0.60 (Green) | keyword | 0 | 0 |
| Independent Agency Capture | civil_service_integrity | 0.55 (Green) | ai | 0 | 5 |

## Evidence Samples

### Emergency Powers Expansion
- Assessment: This is an official Federal Register document recording a presidential continuation of a declared national emergency. The act of continuing an emergency declaration is a real, verifiable action that invokes emergency powers. However, continuation of an existing emergency (rather than a new declaration) and routine exercise of established emergency authorities for a narrowly-tailored domain (export controls) represents a credible but contained stress signal rather than a serious structural breach. The executive is operating within formal statutory frameworks (likely the National Emergencies Act), and there is no indication of bypass of legislative process beyond what the existing emergency framework permits. Severity 2 reflects that this is a real use of emergency authority but not a novel or sweeping expansion.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Export Control Regulations (2026-08-14) - https://www.federalregister.gov/documents/2026/08/14/2026-16748/continuation-of-the-national-emergency-with-respect-to-export-control-regulations

### Civil Service Purge / Schedule F
- Assessment: This is an official Federal Register document recording a direct final rule issued by OPM to amend Civil Service Rules pursuant to Executive Order 14410 regarding 'Schedule Policy/Career in the Excepted Service.' The rule has been issued (not merely proposed), representing a real administrative action. The language about moving positions to the excepted service aligns with Schedule F concerns (reclassifying career positions to at-will status). However, the summary characterizes the changes as updating 'obsolete and outdated provisions' that 'do not substantively affect agency operations,' suggesting limited scope. This is a real, verifiable action matching the signal, but the characterization of impact and scope as non-substantive constrains severity to 2 (repeated or credible stress signal, real but contained action) rather than higher.
- [federalregister.gov] **[official record]** Updates and Amendments to the Civil Service Rules (2026-08-14) - https://www.federalregister.gov/documents/2026/08/14/2026-16630/updates-and-amendments-to-the-civil-service-rules

### Alternate Elector Scheme Activity
- No fresh evidence links in the current lookback window.
### Independent Agency Capture
- [courtlistener.com] **[official record]** Centerline Logistics Corp. v. United States Department of Labor (2026-08-18) - https://www.courtlistener.com/opinion/10953371/centerline-logistics-corp-v-united-states-department-of-labor/
- [courtlistener.com] **[official record]** Queerdoc, Pllc v. DOJ - United States Department of Justice (2026-08-14) - https://www.courtlistener.com/opinion/10948557/queerdoc-pllc-v-doj-united-states-department-of-justice/
- [courtlistener.com] **[official record]** Michael Washington v. City of Cincinnati (2026-08-13) - https://www.courtlistener.com/opinion/10947377/michael-washington-v-city-of-cincinnati/

## Data Quality

- Query feeds attempted: 22
- Query feeds successful: 22
- Query feeds failed: 0
- Primary-source lookups: 20 signals, 18 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 2
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
