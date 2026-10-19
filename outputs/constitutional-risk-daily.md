# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-19 12:43:45 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **7 / 100** (Baseline Institutional Noise)
- Previous day delta: **-1.0**
- Delta vs 7-day average: **-1.2**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.24 | 1.31 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.00 | 0.00 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 1.32 | 3.29 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 1 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 3 | 0 |
| Public Funds for Political Promotion | civil_liberties_information | 1.95 (Yellow) | keyword | 0 | 0 |
| Election Administration Capture | elections_transfer | 0.95 (Watch) | ai | 0 | 2 |

## Evidence Samples

### Press Restrictions or Retaliation
- Assessment: ABC News reports that the Trump administration has targeted specific individuals including James Comey. This constitutes a real occurrence of state action that raises costs or legal risk (targeting by name creates reputational, investigative, or potential legal pressure). However, the report is limited to naming individuals targeted; without detail on the specific mechanism of retaliation (prosecution, removal from office, legal action, loss of license), the severity is contained at level 2 rather than escalated. A confirmed, orchestrated campaign with verifiable legal or official action would be severity 3+. This is credible press coverage of a real targeting action.
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-10-18) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

### Civil Service Purge / Schedule F
- Assessment: Final rule issued by OPM expanding the scope and legitimate uses of administrative leave, including explicitly for 'workforce realignment initiatives.' This is an accomplished regulatory action (not a proposal) that creates new legal authority for executive discretion in removing or repositioning civil servants. Administrative leave can facilitate workforce removal without competitive process protections. Severity 2 because this is a real, confirmed action that materially expands tools available for politicized personnel actions, but it is a procedural/regulatory change rather than a demonstrated mass removal or targeted purge yet executed.
- [federalregister.gov] **[official record]** Administrative Leave for Workforce Realignment and Other Purposes (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21320/administrative-leave-for-workforce-realignment-and-other-purposes
- [federalregister.gov] **[official record]** Elimination of Time-in-Grade (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21319/elimination-of-time-in-grade
- [federalregister.gov] **[official record]** Managing Senior Professional Performance (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21316/managing-senior-professional-performance

### Public Funds for Political Promotion
- No fresh evidence links in the current lookback window.
### Election Administration Capture
- [ABC News - Breaking News, Latest News and Videos] 'Going to be practical': Sen. Markwayne Mullin speaks out after being named Noem's replacement at DHS - ABC News - Breaking News, Latest News and Videos (2026-10-19) - https://news.google.com/rss/articles/CBMipgFBVV95cUxQRGFPSVpoVFZTUlFjaDZRakItV05kaVlGVlluM1pMRGRvTkpaS2RFNlY2ZElwbFFOUEwtQVhSTzVVZlRmSmVBb1JFZDBaaVRqR05kNnZydDNBcFVOak5ENzZvRmdaOFdLTk9sUk9Kc3hSdnB4a3VEcGl6NDJ0M2RNTG9mMjFSUkd0MlNUYnl2QTNjeDI3aWt1UHM3WVBXaGhTOVY0VXBR0gGrAUFVX3lxTE1JN1FWZ1RwMHQ4aEpyckdLR2RxTnhucVUwZ21uVWZscnBKU3MxZFBQX3RaTXlBZE45YnBXLUo0OW4tSWRWdDRRVnFtTHhxbVdzMTJuLTNYQXdQUlB2M0hobldMT05hN2xscnlXLXVjT2VaX2I5WXlzWWdiY0lWNHIzZ0dDMnBDTFN5bUx1bXpQRkduNzdjcF9nS2ZqbTZZMm5YQmRaOTlPVjdNYw?oc=5
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-10-18) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 16 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 3
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
