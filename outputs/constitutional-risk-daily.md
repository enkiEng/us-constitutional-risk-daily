# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-17 12:36:07 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **10 / 100** (Baseline Institutional Noise)
- Previous day delta: **-1.0**
- Delta vs 7-day average: **+1.2**

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
| Executive Constraints and Emergency Powers | 13 | 0.00 | 0.00 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 1.65 | 4.12 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.65 (Yellow) | ai | 5 | 6 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 2 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 3 | 0 |
| Election Administration Capture | elections_transfer | 1.65 (Watch) | ai | 0 | 7 |
| Independent Agency Capture | civil_service_integrity | 0.25 (Green) | ai | 0 | 3 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: A judge has issued an injunction blocking taxpayer-funded Trump ads. This confirms that public funds were being spent on campaign-style ads promoting the officeholder—precisely the signal defined—and that a judicial remedy was sought and partially granted. The injunction itself is a real legal action that altered the status quo by preventing ad expenditure until after the midterms. This is credible, confirmed stress: an actual attempt to use appropriated funds for partisan promotion, caught and enjoined by a court.
- [The Hill] Judge extends block on taxpayer-funded Trump ads until after midterms - The Hill (2026-10-15) - https://news.google.com/rss/articles/CBMiqAFBVV95cUxNMV9xOEc4MjhHNHVMR3JlQzdCd1BBaElxbkNYM2t4SGI0VWxrN0VndjlVeGRJU1dBNFF1ekh3X0ZuWkxqQmU2VngzTTBMZVAxRWN1TUFLRWlHWTAxVGFzR3ZGMkJOajlXXzJiYkM1a0J4bW9jWWJnaE9LbHB5cjYzaHYyUUItZ0lZRVo4ekw3bzNob295SzJZQzNsWHM1dFpiMVNVSnFsUnDSAagBQVVfeXFMTTFfcThHODI4RzR1TEdyZUM3QndQQWhJcW5DWDNreEhiNFVsazdFZ3Y5VXhkSVNXQTRRdXpId19GblpMakJlNlZ4M00wTGVQMUVjdU1BS0VpR1kwMVRhc0d2RjJCTmo5V18yYmJDNWtCeG1vY1liZ2hPS2xweXI2M2h2MlFCLWdJWUVaOHpMN28zaG9veUsyWUMzbFhzNXRaYjFTVUpxbFJw?oc=5
- [Baptist News Global] Trump loses lawsuit over partisan ads paid for with public funds - Baptist News Global (2026-10-16) - https://news.google.com/rss/articles/CBMingFBVV95cUxQRlp0cGdBRS1uZE8yZklOdGlQQ0tZdk5RdFVaVG1DQTJCdXJRMHhZaFMwb0hGaGwwQVVpNVdoS1JmYXJpQVlmbEFLU0oybV9BR3pvTlgwT1hMOWp5ZHJjRmg4dm54ck5hcEZ5N0lZcTU0Vm1DX0FBRnQ5NVBIS3dFa2U4cWlLS1EwMFJucmFTUmdhWjlNLVRrQ2NoR0VNdw?oc=5
- [Winston-Salem Journal] Trump does not plan to reimburse government for taxpayer-funded ads - Winston-Salem Journal (2026-10-15) - https://news.google.com/rss/articles/CBMirwFBVV95cUxNVFBlY2hTTVhyblB0VEt2MXhNNnNEdjQzbmdNT2drbV9qV0NyVEJqaU96aGEydlZyZGx0dW93b3BNX3ZyOHFjaHRNdVYtaXQwOFZnRHNuMXlzZThKZlhWdDFiaVg0SGpiSm16R2xvYmVzSkZsVXhFUGRrZ3M5cjhnQWpONG8yX0pxQ0FRRHFVUmcySTBGQUFabkNpQVI2NFVkdENMNzZEZjlOTFZQelBF?oc=5

### Press Restrictions or Retaliation
- Assessment: ABC News reports that the Trump administration has targeted specific individuals including James Comey. This constitutes a real occurrence of state action that raises costs or legal risk (targeting by name creates reputational, investigative, or potential legal pressure). However, the report is limited to naming individuals targeted; without detail on the specific mechanism of retaliation (prosecution, removal from office, legal action, loss of license), the severity is contained at level 2 rather than escalated. A confirmed, orchestrated campaign with verifiable legal or official action would be severity 3+. This is credible press coverage of a real targeting action.
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-10-15) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

### Civil Service Purge / Schedule F
- Assessment: Final rule issued by OPM expanding the scope and legitimate uses of administrative leave, including explicitly for 'workforce realignment initiatives.' This is an accomplished regulatory action (not a proposal) that creates new legal authority for executive discretion in removing or repositioning civil servants. Administrative leave can facilitate workforce removal without competitive process protections. Severity 2 because this is a real, confirmed action that materially expands tools available for politicized personnel actions, but it is a procedural/regulatory change rather than a demonstrated mass removal or targeted purge yet executed.
- [federalregister.gov] **[official record]** Administrative Leave for Workforce Realignment and Other Purposes (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21320/administrative-leave-for-workforce-realignment-and-other-purposes
- [federalregister.gov] **[official record]** Elimination of Time-in-Grade (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21319/elimination-of-time-in-grade
- [federalregister.gov] **[official record]** Managing Senior Professional Performance (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21316/managing-senior-professional-performance

### Election Administration Capture
- [Politico] Playbook - Politico (2026-10-16) - https://news.google.com/rss/articles/CBMiSEFVX3lxTFAyQkZwUjVOOEFSSFFicG1RMFhQTVo2TWdmZDN2Zjd2aWtJM0lpMklrQkVPR3dVRDByTkFORmJHZU9qSXlEdTNxbw?oc=5
- [Longview News-Journal] Here’s how Abbott, Hinojosa want to reshape Texas education - Longview News-Journal (2026-10-17) - https://news.google.com/rss/articles/CBMimgFBVV95cUxPUHZpMUN6cVZNeG8tMGVzbzYwWnZoc2JUb3JyZEtvbVp0LXc2elVfbGl6TlVJTWtNTUpZQmJ6MTBjdFNydkFvamhzdDRNMFZPTTZHcE5iNjJnNUpIUzVfRlZvS1dqODMtckF0TjZJbk5hQWRTUFU2dUdsbjQzZFNhWkxhSUVwMTRrRmF5c2tCYlhCTEJSZmdpX3Bn?oc=5
- [Hawaii Public Radio] Voting explainer: 2026 Honolulu charter amendment ballot questions - Hawaii Public Radio (2026-10-16) - https://news.google.com/rss/articles/CBMivgFBVV95cUxPZnNCWU51YVZmdXVJb3dzQVJkdEVQUVZORmtsc0RXb1VkUmJyVWx0dzVxNkEydU14QW1ZS0pQVG9pbXNsLXV5Sm44Mk1OQWUtaVMxMUhVcVhUUWJlbXBnUXJiOUl2SHh1TXZxUWM1eHJDTFdTQ3FJWVl4U1hhWXFMQmVMOUlTU2FTUXBRbWhpMDBHYXVEd1N5Q3E2Y3JLeDB6a0NkUm93TTFoenZOMjQ4cThQV3BoWFJKdTdIVExn?oc=5

### Independent Agency Capture
- [Consumer Finance Monitor] Podcast Release: The Supreme Court Opinions in Trump v. Slaughter and Trump v. Cook: What Do They Mean for the Future of the Administrative State? - Consumer Finance Monitor (2026-10-15) - https://news.google.com/rss/articles/CBMinAJBVV95cUxNLUJxT01sUmRISUl2NEttTDlZalhSbXFOa0RueENrTmh3NFlHeXlzMy1ZOWt1U01MMm8tQ28yazY0UVotRmhVQk5pYW9vTzRVT05HaFRubFUyREpRYnl0VzJPU2xfeUE5R09PaUxKNW5kSU8yZFltNXdwS2hJa3RZQldtUW1VYnJaNXh0bHRyUU8wRks4Vml2ZE1qd0lvVXY3QU5JamFtUHBWMHNNYTgxUU80VGttYTdNLVNqdXRXbEJmRTk2YS02amY3T29CT09VUEM1YldoWk9oSnl5WUVfZzlvamJmMDdyYzZjUmh3MTVyUjNsbDRJUDZnNHhoWnpCLVNwUXZMOGh3SVRFQThGQ1VNTmtJTnRiREcwXw?oc=5
- [The Daily Economy] Cook Case Tests the Limits of Fed Independence - The Daily Economy (2026-10-16) - https://news.google.com/rss/articles/CBMiiwFBVV95cUxPSDNkQXYtVktHT2IwVkpGQXBwbHJzdVNmOEcxN3VpVTcyYm1ydlRZQjNiTmM4Q19jMl9aYTVPS0dYOXU2MTF1M2ZMdXRDQ0w0OFFrbW5MNnFyejJkS3pfMHNtcjNQZEVOVmI4bmJZWDFvMjY0UWlPZzJiQWtqcW1oX1NOS0RnbHBuOG1z?oc=5
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-10-15) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 15 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 3
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
