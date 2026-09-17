# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-17 17:06:56 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **13 / 100** (Baseline Institutional Noise)
- Previous day delta: **-1.0**
- Delta vs 7-day average: **-1.0**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.33 | 1.79 |
| Judicial Independence and Rule of Law | 15 | 0.33 | 1.22 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 1.00 | 2.50 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 1.00 | 2.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Oversight Obstruction | federalism_oversight | 2.00 (Yellow) | ai | 3 | 16 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 3 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 2 | 0 |
| Statistical Agency Integrity | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Election Administration Capture | elections_transfer | 1.30 (Watch) | ai | 0 | 2 |
| Judicial Review Foreclosure | judiciary_rule_of_law | 1.30 (Watch) | ai | 0 | 1 |
| Legislative Bypass by Executive | executive_constraints | 0.60 (Green) | ai | 0 | 1 |

## Evidence Samples

### Legislative Oversight Obstruction
- Assessment: House Oversight unanimously votes to hold Leon Black in contempt for subpoena non-compliance. Confirms the same real event of resistance to legislative oversight. Severity 2: repeated, credible report of a single contained action.
- [meidasnews.com] House Oversight Unanimously Votes to Hold Epstein Associate Leon Black in Contempt - meidasnews.com (2026-09-15) - https://news.google.com/rss/articles/CBMirwFBVV95cUxQN1VsTkhzNDY4OEpmMklZWlZ5RTRsd0MxN0FwSWprVVNDRXRSbkRZUVdzNTdfeFdxT0pkQ3ZPQlV1SEoxbFlHTHFHdDZITVNUX0VnY01ZaFlJYTc4SGY0X3pneXF2Tm9HOG5yVFhCdUQtRW5EUG1pcjJTUG9FQVRoYldRNTVEeURWM3Y3dWJLOFJNZnlaRDl4VV9pM0tIZHhKVHdXdFEzMW1kb2VoN0dV?oc=5
- [rawstory.com] House panel unanimously votes to hold billionaire in contempt over Epstein - rawstory.com (2026-09-15) - https://news.google.com/rss/articles/CBMiYkFVX3lxTE1GcHhEYU82REx3c1FhRVpJMGM2Sk1CQm0zTmJCZEY0RXQtQldjN2hxcmp0a18ycTZXU2ptM25iT1l2TzlxbFFhMFpLV1dxUkZTb0Q0TlAwMHNqSHZCQ25wMW5n0gF0QVVfeXFMTWNhT2pCOVpENUEtS1ZvY0xPQnAzdW8tbGhualZsYUxSekhLSFlaTGpLcEJyeGdmaDdXcjdUUlZBbWptbHBfTVB6THgzTDZuWU9obGJOOUsxNFdWcXYzZ2EtN21Jd0N0YmdzM0ctUVpuT0pDSWg?oc=5
- [Just The News] House Oversight votes to hold Leon Black in contempt of Congress for defying subpoenas - Just The News (2026-09-15) - https://news.google.com/rss/articles/CBMiuAFBVV95cUxNSWVDLWd1eWh4WUR5c2xhVEJjZGlwcHB5R1lZY3JSeS1KRlh5d2RvbnZXOHlhazN0TDhqMU1HUy1uZ2Zyd3NUMXZDazNkMXhoU3VqQVJ3d3NTdnJacFdUYUExOGRwSnkwejJrYkcxd2lRMDJCR1dQRUpSMWRwX0ZyU3N0T0dWaDg5T0xDQl8yVjlRelNfcUlCMlVRb1Y0cThXMGJVcUxTWGJnZDdCOVkxVmhDR2FNSXRq?oc=5

### Press Restrictions or Retaliation
- Assessment: ABC News reports that the Trump administration has targeted specific individuals including James Comey. This constitutes a real occurrence of state action that raises costs or legal risk (targeting by name creates reputational, investigative, or potential legal pressure). However, the report is limited to naming individuals targeted; without detail on the specific mechanism of retaliation (prosecution, removal from office, legal action, loss of license), the severity is contained at level 2 rather than escalated. A confirmed, orchestrated campaign with verifiable legal or official action would be severity 3+. This is credible press coverage of a real targeting action.
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-09-17) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

### Emergency Powers Expansion
- Assessment: This is an official record of continuation of a pre-existing national emergency declaration. The continuation itself is a routine renewal mechanism established under the National Emergencies Act (50 U.S.C. § 1601 et seq.), whereby the President may extend a declared emergency for successive one-year periods without new legislative authorization. While this document confirms the use of emergency authorities to maintain expanded executive powers outside ordinary legislative process—and therefore matches the signal—the action is procedurally lawful, statutorily authorized, and represents the normal operation of the emergency declaration system rather than an expansion or abuse of emergency powers. The severity is 2 (a real but contained and legally-authorized stress signal) because emergency declarations do represent a bypass of ordinary process, but this particular continuation is a standard recurring action, not a novel expansion or defiance of law.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Persons Who Commit, Threaten To Commit, or Support Terrorism (2026-09-16) - https://www.federalregister.gov/documents/2026/09/16/2026-19053/continuation-of-the-national-emergency-with-respect-to-persons-who-commit-threaten-to-commit-or
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Certain Terrorist Attacks (2026-09-10) - https://www.federalregister.gov/documents/2026/09/10/2026-18589/continuation-of-the-national-emergency-with-respect-to-certain-terrorist-attacks

### Statistical Agency Integrity
- Assessment: This is an OFFICIAL RECORD—a final rule issued by DOL that materially changes data availability protocols for confidential unemployment compensation information. The rule mandates disclosure of previously confidential UC data to Federal officials for oversight and audits. This is a real, accomplished action (a final rule) that alters the scope and handling of statistical/administrative data outside normal notice procedures, which constitutes a credible stress signal on statistical agency integrity. However, the framing as 'oversight and audits' by DOL's own OIG suggests internal administrative coordination rather than external political manipulation of methodology, definitions, or suppression. The action is real and confirmed, but contained in scope and justified as administrative oversight rather than politicized interference with the independence or objectivity of statistical production. Severity 2 reflects a confirmed, material change to data protocols that warrants monitoring, but without evidence of removal of statistical leadership, improper methodology changes, or withheld releases.
- [federalregister.gov] **[official record]** Federal-State Unemployment Compensation (UC) Program; Data Availability (2026-09-16) - https://www.federalregister.gov/documents/2026/09/16/2026-18978/federal-state-unemployment-compensation-uc-program-data-availability

### Election Administration Capture
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-09-17) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5
- [WBUR] Trump's war on mail-in ballots - WBUR (2026-09-16) - https://news.google.com/rss/articles/CBMif0FVX3lxTFA5UmE0cVNRTjZVVkxuYXM1MmZGaXM2RGF0WV9qR3BnczVTSTVnWVZoVHBONUk4b1I1N1lFZ09XUkNacUprOURLVzg4Z0NaV21MNzItdWpTdG5BUS01dElidEl1T3dqb0tsQkxHNHkzbmsyaDFCSHE1R21UbXlmbkE?oc=5

## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 24
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 19 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 3
- Evidence extraction: AI event extraction
- Confidence: **High**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
