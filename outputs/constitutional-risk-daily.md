# Constitutional Risk Dashboard (0-100)

- Generated: 2026-08-25 13:14:48 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **10 / 100** (Baseline Institutional Noise)
- Previous day delta: **+6.0**
- Delta vs 7-day average: **+3.5**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.00 | 0.00 |
| Judicial Independence and Rule of Law | 15 | 1.00 | 3.75 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 5 | 5 |
| Targeted Jurisdiction Stripping | judiciary_rule_of_law | 2.00 (Yellow) | ai | 1 | 1 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 1 |
| Independent Agency Capture | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Emergency Powers Expansion | executive_constraints | 0.60 (Green) | keyword | 0 | 0 |

## Evidence Samples

### Legislative Bypass by Executive
- Assessment: Multiple credible sources report that the Supreme Court allowed Trump to implement parts of a mail-in voting executive order. This represents a shift of voting-rule authority from statutory/legislative control to unilateral executive action via EO. The Court's allowance (likely through stay or injunction ruling) enabled executive implementation without requiring legislative authorization. This is a real, confirmed action that transfers governance authority from statute to executive fiat, but is narrowly scoped to mail-voting procedures rather than a broader structural dismantling. Severity 2 reflects this as a real, credible stress signal of limited scope, not yet structural failure.
- [ABC News - Breaking News, Latest News and Videos] Supreme Court allows Trump to implement parts of his mail-in voting executive order - ABC News - Breaking News, Latest News and Videos (2026-08-24) - https://news.google.com/rss/articles/CBMigAFBVV95cUxQLUpWVmxZNkVNNGxlamhNRjkteVhjUVJNMXhDQ3Vyc3V3UkdTVEcyeUM0ZnEzTUlJQXRYMUZsNkZ5LTN5Q0VzWDFrVmVFSVlpOFBSaEpwa19qd0Q4SExzankxMEpIQjMxT2k5R0Z3emE0cDFCNng3V3lwVjBQUDg1NNIBhgFBVV95cUxOWGtmd1BpZ1U2QlJOeTZIcXhKMTVTOVFEZDJKcDJPS1NzX2NsOG1RT2w2TkpUMDkwTWY1QzlZcGt4LVlmNV9NZlFVUG04S0Y1U2hUSUdFSk5sUlFId1VsZzlnd1JvOGlWQnY2LThiN1J6cjZDSjdSWHd3elNWS3FpYWJqMXFnUQ?oc=5
- [CBS News] Supreme Court allows Trump to implement key parts of order restricting mail voting ahead of midterms - CBS News (2026-08-24) - https://news.google.com/rss/articles/CBMiggFBVV95cUxQLVZTaUM5SDFJZUJEQTd6V2hOLWVNMlg5U1BkWFFWUGVQNmN1aWpMblE4TUhMSl9CeVNmSmZZX0VLRzJXYjd4ZDRYQkp4TWNVVkJSVXQwRlhkZFp1WnV0bkRkZGtNeXJieGVieEN0T3dEWW85WWNUQVVQVVFWbHJ1QzVn?oc=5
- [CNN] What Trump’s Supreme Court win means for mail ballots - CNN (2026-08-25) - https://news.google.com/rss/articles/CBMie0FVX3lxTFAzWEtRUjJjZXdLa2tLUkhXMDNvaHdqSVIyWjFmWENTVjktaDI2NkVmZEZaVjhyeW01S3RGZnFqcVVUWXYzMkxXRjZwWTZIYlFZN2hJNzFKdFlKdURIRFF1cERRZGVEU0Uxd2laVW1hd0RLbWNXNlM2NGs4RQ?oc=5

### Targeted Jurisdiction Stripping
- Assessment: The Fifth Circuit issued a ruling that removes or severely limits court review over a specific category of disputes (IRS penalty suits). This constitutes a targeted jurisdiction-stripping action—a court has determined that certain constitutional disputes or statutory claims fall outside its reviewable jurisdiction. This is a real judicial action that has taken place (the ruling has issued), not a proposal or hypothetical. However, severity is 2 rather than 3 because this appears to be a single appellate ruling on a narrow category of cases, not a systematic campaign or structural defect. The ruling does strip review authority over this specific category, but without additional context suggesting this is part of a broader effort to eliminate constitutional safeguards, it remains a contained, albeit credible, stress signal.
- [Law360] 5th Circ. Says IRS Penalty Suit Is Beyond Court Review - Law360 (2026-08-24) - https://news.google.com/rss/articles/CBMitgFBVV95cUxQdGlPVE96STFsaTJwTXI1bVBKLTJCcUMxQ0R3eVBBR094M2Z0bVdoc21QZ3RVX2VvWmpBYk14QjBTQnJ3MkFqbXdKUzBsRXJ0NE9rWkphNW5tMVQyb0JyVjJhZmRZWjJTNUZHTlVfNzN2WGgwU3JKbWphdW9xUlpJdW44S0FPN1czdkdfbFFMdHQtWG9NZ3JaeG9MWXN5ODVJaVNLTXo2Y2Q5TGhFMTROWnJFbzFiUdIBaEFVX3lxTE5aUnpFdkFMWFFwYmVZWjc3dWJpUjZRZVoyZlotV1RzNHhCWTRXdGxrMDBMaHpCMkc4REFLaC1FOExtOVBBUHBhZks2bmN1YkpFb2J4OVVOSENseDhMSlJ1S0J4NE5RV19o?oc=5

### Civil Service Purge / Schedule F
- Assessment: This is an official Federal Register document confirming that OPM has issued a final rule titled 'Improving Performance, Accountability and Responsiveness in the Civil Service' (published February 6, 2026, effective March 9, 2026). The August 25, 2026 entry is a technical correction to that rule. The original February rule directly addresses civil service structure and performance accountability, consistent with Schedule F concerns about reclassification of career positions. As an issued final rule effective before this correction, it represents a material structural change to civil service rules. The correction itself confirms the underlying rule exists and operates. Severity is 2 (repeated/credible stress signal, real but contained action) rather than higher because the document excerpt does not detail the specific reclassification powers granted, only that such a rule has been issued and corrected. The fact that a major civil service reform rule exists and is being administratively refined constitutes verifiable evidence of civil service policy change, though the full scope of at-will reclassification authority is not detailed in this excerpt.
- [federalregister.gov] **[official record]** Improving Performance, Accountability and Responsiveness in the Civil Service, and Recruitment and Relocation Incentive Waivers; Correcting Amendments (2026-08-25) - https://www.federalregister.gov/documents/2026/08/25/2026-17334/improving-performance-accountability-and-responsiveness-in-the-civil-service-and-recruitment-and

### Independent Agency Capture
- Assessment: This is an official DOJ OLC opinion concluding that the Foreign Service Grievance Board's structure violates the Appointments Clause due to insufficient oversight of inferior officers. This represents a real legal finding that an independent agency's decision-making authority lacks adequate political accountability safeguards—a direct match to the signal. However, severity is capped at 2 because this is an OLC opinion (legal analysis) rather than a confirmed structural breakdown or defiance of court order. The opinion identifies a constitutional weakness but does not demonstrate that safeguards have already been dismantled or that the agency has begun operating in violation of the ruling.
- [courtlistener.com] **[official record]** Constitutionality of the Foreign Service Grievance Board's Oversight Authority (2026-08-20) - https://www.courtlistener.com/opinion/10954524/constitutionality-of-the-foreign-service-grievance-boards-oversight/

### Emergency Powers Expansion
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 23
- Query feeds successful: 23
- Query feeds failed: 0
- Primary-source lookups: 21 signals, 15 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 2
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
