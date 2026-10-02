# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-02 12:43:48 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **11 / 100** (Baseline Institutional Noise)
- Previous day delta: **+4.0**
- Delta vs 7-day average: **+2.2**

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
| Executive Constraints and Emergency Powers | 13 | 0.43 | 1.41 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.33 | 3.33 |
| Security Sector Neutrality | 8 | 0.50 | 1.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 16 | 18 |
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 4 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 3 |
| Legislative Bypass by Executive | executive_constraints | 1.30 (Watch) | ai | 0 | 1 |
| Domestic Military Use in Political Conflict | security_sector_neutrality | 1.00 (Watch) | ai | 1 | 1 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: ABC News reports Trump defending spending millions on taxpayer-funded promotional ads. The headline indicates an actual occurrence of taxpayer-funded promotional spending, not a hypothetical. Trump's defense of the action confirms the event happened. However, without detailed documentation of the specific appropriation source, amount, or official justification, this is a credible but partially sourced report rather than a confirmed official record. Severity 2: repeated/credible stress signal, a real but contained action.
- [ABC News - Breaking News, Latest News and Videos] Trump defends spending millions on taxpayer-funded promotional ads: 'For the country' - ABC News - Breaking News, Latest News and Videos (2026-10-01) - https://news.google.com/rss/articles/CBMisAFBVV95cUxQTTZ6c1ZheWdCTTN1d1hKaGR2U2xxb1hZSV9HWDFueUNpU1U3NlBBcW84V0ZENVBfMy0tV2syam5MTlJFMmdvMFZ3N0c5bEZUdXhCWGxCRGd2Uk9fOGFiRW5tU2k2cEp2X2dKdkpZTUN5V1VNdDUtQUMwekJJbnRSS2lpVC13emZ4eU1uaEdtN1N6RWJvRHZ4V3hMN01TWWtOQWZaT2pqRnhib0JmekozZNIBtgFBVV95cUxQZUZWR1E1ZDdHMkR3Y2gxV213QWVTMjBRbUNxNzVWMkd3ak01TDB1X213VTl3RXNMM3lHdU1PaFp2cHphWF85V1NCMUtlbVZuRy1EX2JWY0N1M09QcVQ5ZVl2eFRaTHhXSEJtYjJVX1Bheld5ekRyaFZVZmtKNFNTUzBIZU1CSGZCVTZ0Z21mU0xmRVRJMS0zNUJpTVBreS0tUUNsUm5hbEsxcUo5U0w4QS1TeTFSZw?oc=5
- [The Fiscal Times] Dems Call for Probe Into Federally Funded Pro-Trump Ads — and Penalties for Airing Them - The Fiscal Times (2026-10-01) - https://news.google.com/rss/articles/CBMitAFBVV95cUxQX0x0S3ZPejJTS0RmOG1hd1lpcmFPUHI3SXUtTTZiLTZKWGNYUzI1Q2hyZThsUlRSSWNsb0Jtb3A3cHNzekNhVGp0X2pHRnpFSWVpRGl6V1FLVVZHS2dhcXRzMDhJekJ4N0hyT244SWhSbUZGR1hXZVlrRkNPcnlhblJCY3daUHVoWHhrX245RnJzaXV2N3JUR1BFM2oySG44azAxZEFBTzV1Rlc5NFVyc2JrbFY?oc=5
- [Common Cause] What Republicans Are Saying About Trump’s Taxpayer Funded Propaganda - Common Cause (2026-10-01) - https://news.google.com/rss/articles/CBMiqAFBVV95cUxQMTVmV1N6Y2dyX0Z5TWtzdkphOVdIanA5eXpxNXVTOG9LWGFHelN2NEt5ZUMwUWZxNDdfZUh3UUFVWF9jNmdISzdINFRBMFNFZWw4b2VQa0xROG1RSGZlcno1dWd3RzhNWUllNzBXdVlPSjFBY3Q1M1E4Y3k1eHJYcVd1Tzc4b09mNTlHOHlRM3JXNlprcFJtRE5LZUhvVWdlQ2V4OFZ5OWU?oc=5

### Election Administration Capture
- Assessment: This reports an allegation (via affidavit) that a Trump-appointed director of election security sparked a Georgia office raid. This represents a real action that has occurred—a raid of an election office—allegedly directed by a Trump administration official. While the severity is not extreme (no election was cancelled or overturned), this constitutes a credible signal of election administration being subject to partisan pressure from the executive. The involvement of a Trump administration official in directing action against a state election office suggests potential partisan capture or interference.
- [ABC News - Breaking News, Latest News and Videos] Trump director of election security sparked Georgia office raid, affidavit says - ABC News - Breaking News, Latest News and Videos (2026-10-01) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5

### Press Restrictions or Retaliation
- Assessment: ABC News reports that the Trump administration has targeted specific individuals including James Comey. This constitutes a real occurrence of state action that raises costs or legal risk (targeting by name creates reputational, investigative, or potential legal pressure). However, the report is limited to naming individuals targeted; without detail on the specific mechanism of retaliation (prosecution, removal from office, legal action, loss of license), the severity is contained at level 2 rather than escalated. A confirmed, orchestrated campaign with verifiable legal or official action would be severity 3+. This is credible press coverage of a real targeting action.
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-10-02) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

### Legislative Bypass by Executive
- [federalregister.gov] **[official record]** Rescissions Proposals Pursuant to the Congressional Budget and Impoundment Control Act of 1974 (2026-09-30) - https://www.federalregister.gov/documents/2026/09/30/2026-19965/rescissions-proposals-pursuant-to-the-congressional-budget-and-impoundment-control-act-of-1974
- [National Affairs] The Unfinished Work of Federal Permitting Reform - National Affairs (2026-10-01) - https://news.google.com/rss/articles/CBMimAFBVV95cUxOa0o4OXVkQkxHdXJ6VkxqLUNNTVhfQ0JFT3lYSDFLc2YycTlRUFV3VWp3TFhMMTgwSGZQaTdlU2RMNFBVZlV2Q05odjlFN3QwU0ZHVFh5QXE0OEJKRWh0dnR4ZGxFVk5KblVTWXI2UzJrRWlSeF9DWXAxX3lRNDRPMVBHdVlsdVZuemZZSjcyWGF0dUV1YnB3Xw?oc=5

### Domestic Military Use in Political Conflict
- Assessment: A civil complaint has been filed in federal court (D. Minnesota) naming multiple current and former federal officials. The complaint itself is an official record indicating that plaintiffs have asserted claims regarding potentially unlawful conduct by these defendants. However, without access to the complaint's substantive allegations, the severity cannot be determined beyond acknowledging that a legal action has been initiated. The filing is a real procedural event, but severity is limited to 1 because a complaint represents an allegation, not a proven occurrence, and the specific nature of the alleged conduct cannot be assessed from the docket summary alone.
- [courtlistener.com] **[official record]** Ganger v. Ross (2026-10-01) - https://www.courtlistener.com/docket/74901903/1/ganger-v-ross/

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 17 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 1
- Evidence extraction: AI event extraction
- Confidence: **High**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
