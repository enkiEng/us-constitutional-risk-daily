# Constitutional Risk Dashboard (0-100)

- Generated: 2026-08-16 13:03:44 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **13 / 100** (Baseline Institutional Noise)
- Previous day delta: **0.0**
- Delta vs 7-day average: **+3.0**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 1.52 | 3.79 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Alternate Elector Scheme Activity | elections_transfer | 2.00 (Yellow) | ai | 1 | 4 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 0 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Independent Agency Capture | civil_service_integrity | 1.95 (Yellow) | ai | 0 | 0 |
| Inspector General Retaliation | civil_service_integrity | 0.60 (Green) | ai | 0 | 0 |

## Evidence Samples

### Alternate Elector Scheme Activity
- Assessment: This item reports that a Nevada judge dismissed a case against individuals accused of forging an electoral certificate in the 2020 election. The underlying conduct—alternate electors accused of forging a certificate—is direct evidence that alternate elector scheme activity did occur in Nevada in 2020. The case dismissal itself is a judicial ruling, but the summary indicates the judge faulted the AG's office for withholding evidence, suggesting prosecutorial failure rather than absence of the underlying alleged conduct. The signal concerns efforts to substitute unauthorized electoral slates; the accusation of forged certificates by alternate electors is a direct match. However, without confirmation that the forgery actually occurred (as opposed to being merely alleged and then dismissed), and given that this is historical (2020 election), the severity is conservatively set at 2—a confirmed but past-tense occurrence of attempted unauthorized elector slate substitution, now subject to judicial dismissal.
- [California Globe] Nevada Judge Dismisses ‘Fake Electors’ Case a Second Time, Faults AG Ford’s Office for Withholding Evidence - California Globe (2026-08-14) - https://news.google.com/rss/articles/CBMi0AFBVV95cUxQcTZ5ZHVwOFJycTJoMXd5VUhiaWJnTHJ5TUR4OEVjQmxPVkMxRDAzc1dNU1NIQnV1cGd6dzVRQXNfeDVkUy1qN0xhTjFTUUpFTlNnSGh1NmFEZGJfSjZWVUJZZjRmSjV4SFo5VElFZXQ2SVFIMFFWWFJSM1AyY2VXRXBhNTVhaWZILTdUN2FHRzFwQ3BVZGVZSFpmNlotcW5UOFBRdTNxclF3V0lXVkMtX1RoVVZNUS1qMHNLVml0bk9taXVKXzZ1ZVotZWlhamRW?oc=5

### Emergency Powers Expansion
- Assessment: This is an official Federal Register document recording a presidential continuation of a declared national emergency. The act of continuing an emergency declaration is a real, verifiable action that invokes emergency powers. However, continuation of an existing emergency (rather than a new declaration) and routine exercise of established emergency authorities for a narrowly-tailored domain (export controls) represents a credible but contained stress signal rather than a serious structural breach. The executive is operating within formal statutory frameworks (likely the National Emergencies Act), and there is no indication of bypass of legislative process beyond what the existing emergency framework permits. Severity 2 reflects that this is a real use of emergency authority but not a novel or sweeping expansion.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Export Control Regulations (2026-08-14) - https://www.federalregister.gov/documents/2026/08/14/2026-16748/continuation-of-the-national-emergency-with-respect-to-export-control-regulations

### Civil Service Purge / Schedule F
- Assessment: This is an official Federal Register document recording a direct final rule issued by OPM to amend Civil Service Rules pursuant to Executive Order 14410 regarding 'Schedule Policy/Career in the Excepted Service.' The rule has been issued (not merely proposed), representing a real administrative action. The language about moving positions to the excepted service aligns with Schedule F concerns (reclassifying career positions to at-will status). However, the summary characterizes the changes as updating 'obsolete and outdated provisions' that 'do not substantively affect agency operations,' suggesting limited scope. This is a real, verifiable action matching the signal, but the characterization of impact and scope as non-substantive constrains severity to 2 (repeated or credible stress signal, real but contained action) rather than higher.
- [federalregister.gov] **[official record]** Updates and Amendments to the Civil Service Rules (2026-08-14) - https://www.federalregister.gov/documents/2026/08/14/2026-16630/updates-and-amendments-to-the-civil-service-rules

### Independent Agency Capture
- [courtlistener.com] **[official record]** Queerdoc, Pllc v. DOJ - United States Department of Justice (2026-08-14) - https://www.courtlistener.com/opinion/10948557/queerdoc-pllc-v-doj-united-states-department-of-justice/
- [courtlistener.com] **[official record]** Michael Washington v. City of Cincinnati (2026-08-13) - https://www.courtlistener.com/opinion/10947377/michael-washington-v-city-of-cincinnati/
- [courtlistener.com] **[official record]** Frank William Bonan, II v. FDIC (2026-08-12) - https://www.courtlistener.com/opinion/10945915/frank-william-bonan-ii-v-fdic/

### Inspector General Retaliation
- [courtlistener.com] **[official record]** State of Illinois v. United States Department of Homeland Security (2026-08-13) - https://www.courtlistener.com/docket/74645299/3/17/v-united-states-department-of-homeland-security/
- [courtlistener.com] **[official record]** State of Illinois v. United States Department of Transportation (2026-08-13) - https://www.courtlistener.com/docket/74643629/1/3/state-of-illinois-v-united-states-department-of-transportation/
- [courtlistener.com] **[official record]** Jenkins v. NEOGOV (2026-08-12) - https://www.courtlistener.com/docket/74644547/1/jenkins-v-neogov/

## Data Quality

- Query feeds attempted: 22
- Query feeds successful: 22
- Query feeds failed: 0
- Primary-source lookups: 20 signals, 13 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 2
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
