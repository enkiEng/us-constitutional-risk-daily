# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-13 12:48:15 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **9 / 100** (Baseline Institutional Noise)
- Previous day delta: **0.0**
- Delta vs 7-day average: **-2.3**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.06 | 0.34 |
| Judicial Independence and Rule of Law | 15 | 0.15 | 0.56 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.43 | 1.41 |
| Civil Service and Agency Independence | 10 | 0.65 | 1.62 |
| Civil Liberties and Information Environment | 10 | 2.00 | 5.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 3.00 (Orange) | ai | 15 | 15 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 1 |
| Independent Agency Capture | civil_service_integrity | 1.65 (Watch) | ai | 0 | 1 |
| Legislative Bypass by Executive | executive_constraints | 1.30 (Watch) | ai | 0 | 1 |
| Court Order Noncompliance | judiciary_rule_of_law | 0.60 (Green) | ai | 0 | 0 |
| Election Administration Capture | elections_transfer | 0.25 (Green) | ai | 0 | 4 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: NBC News reports that a federal judge has ordered pro-Trump TV ads funded by taxpayers to be taken off the air immediately. This is a confirmed court order in response to the unlawful spending. The fact that a judge found the conduct serious enough to issue an immediate injunction elevates this from isolated misconduct to a serious, confirmed high-severity action with judicial review.
- [NBC News] Federal judge orders pro-Trump TV ads funded by taxpayers off air immediately - NBC News (2026-10-12) - https://news.google.com/rss/articles/CBMiywFBVV95cUxON1pBMERGUjZ4cG5DX0EyQlZWVG1KMGx5NWFCcHUtRnJac28wMmx4ME9kdmpRN1dqRDQxTTRSU1UzOEhNRHRnMUNkVEdSdDNRaTRUSkhSVDRWaHhDUnFTNmY5elA0Zm5UMXlZZHF2aGZGRUNuSmJLTlpSV2hwNDBuaTVOQWRublJOSU9EaVhrZGVVU2l0Wk5mYjhTOUVDSkVxckRWT3VVNG5iM1dFZC1xbzkxXzVGS3AzY2Vsc3o2TzJmZFpIQjJlaTRNMA?oc=5
- [CBS News] Judge orders Trump administration to cancel taxpayer-funded TV ads - CBS News (2026-10-12) - https://news.google.com/rss/articles/CBMieEFVX3lxTE5pLUtqbzlUWHRveXYwMmY5clRlVzVGVWc3SThfWEEzb2xvZm9tSFhHR0pHcFo3c2U5UXdjMnp0aTg2NTAyc3FHSlhIR0dxSlFEOUdwVmlsek9GTEVmYlhaT01kQjVJWmVWLU10U1FvWFdaYmc5N3pYSA?oc=5
- [The Daily Beast] Judge Immediately Pulls the Plug on Trump’s Bonkers Propaganda Blitz - The Daily Beast (2026-10-12) - https://news.google.com/rss/articles/CBMingFBVV95cUxOUjZDUHZnWDBYbGhhcVdEY0hKaGJVdXNreUY3RXhDaTRZZ0o0LVZjOFNBbVpUQ3JXSGxjZDgwN1hqTFJpeEZ5VmtUbnkyZExJYUpvdktUME5LVklseGdxT0RIYW1YaTBXRXJXSDEwLWVjY3hlZ1A3U0JVWWt5MTdsbjRnN21FQXdBektRdkJJdTdMSHoxeEttTklEUjV6dw?oc=5

### Press Restrictions or Retaliation
- Assessment: ABC News reports that the Trump administration has targeted specific individuals including James Comey. This constitutes a real occurrence of state action that raises costs or legal risk (targeting by name creates reputational, investigative, or potential legal pressure). However, the report is limited to naming individuals targeted; without detail on the specific mechanism of retaliation (prosecution, removal from office, legal action, loss of license), the severity is contained at level 2 rather than escalated. A confirmed, orchestrated campaign with verifiable legal or official action would be severity 3+. This is credible press coverage of a real targeting action.
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-10-12) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

### Independent Agency Capture
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-10-12) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

### Legislative Bypass by Executive
- [Britannica] Donald Trump | Birthday, Age, Education, Biography, Impeachments, & Military Parade - Britannica (2026-10-12) - https://news.google.com/rss/articles/CBMiXkFVX3lxTE4zTlNFQlJBYmZmZE9MbUdKWElnLXE0c2pWcVFIenNYSjQwbURvQm5kUmRFQVM1NVlCT24zZktQZHliMEV4ZnZ1QzM0VEpZWS1pWWxON0ZUa3N0RUpmemc?oc=5

### Court Order Noncompliance
- [courtlistener.com] **[official record]** Allina Health System v. Minnesota Department of Human Services Commissioner John Connolly (2026-10-11) - https://www.courtlistener.com/docket/74943556/9/allina-health-system-v-minnesota-department-of-human-services-commissioner/

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 15 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **High**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
