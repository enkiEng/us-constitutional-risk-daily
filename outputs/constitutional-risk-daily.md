# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-27 12:30:05 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **12 / 100** (Baseline Institutional Noise)
- Previous day delta: **+4.0**
- Delta vs 7-day average: **+2.5**

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
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.33 | 3.33 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 7 | 7 |
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 6 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 5 |
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 1 | 3 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: News report confirming that an administration aired TV advertisements promoting the officeholder using taxpayer funds. This constitutes spending of appropriated public money on communications that promote the officeholder rather than serve a public-information purpose, which directly matches the signal definition. The report itself treats this as a real occurrence (not hypothetical, opinion, or allegation), though the severity is moderate because this appears to be a discrete action that has been detected and is now subject to public scrutiny and potential legal challenge. No court order has been defied, no structural constitutional breakdown has occurred, but the alleged violation of the 1950s appropriations prohibition on 'publicity or propaganda purposes' is material.
- [ABC News - Breaking News, Latest News and Videos] Administration's pro-Trump TV ad is taxpayer-funded - ABC News - Breaking News, Latest News and Videos (2026-11-27) - https://news.google.com/rss/articles/CBMiqAFBVV95cUxNNEc3UWRPWjdaWkt2Wk9vcklvTkd3LUU0eEFHNnBTNGE1M01jZ1ZsczFwN0o1VjVmMk9rU3kxOUx5M1N2V1MtLVRqNjFfUXJYV0FQeFJSV3pBSEJ1Y2NFV29FMzFGLUxmVGVRa2tVVnhwM3hRYVhzSnFRM2YzUklyR3BjQm4xOUltenU0V2lRSHB2SzJlVmpMLV9lMHdGT2dJU3FBZG5FVVnSAa4BQVVfeXFMT2lPdUJtQ0JKMEs1aVhMMUFfOXFWRmxwZlBsSk9LYjFHX3pMamdNOUV6c1BNZnQwdGtVUzRTMS1IVzJoWjl4c3Z1elZtdWotY2MwazN5UzhQNGk1TGtnSGJhMzI3WUNlY3BlemEzWGlNMkpGNnFjNXZiZU1vQVZ3SFRPYklhZjN1ek4wWUN3ZUt4YUxMcDJpTmhGMjhaVkg4Wm0tMm9CbERyWnVENjNB?oc=5
- [Newsweek] Democrats Lose Bid to Block Taxpayer-Funded Pro-Trump Ads - Newsweek (2026-11-26) - https://news.google.com/rss/articles/CBMilgFBVV95cUxPWHQzLXFjaDhHVkE4dzQ4YzNhU3dqYjRncXJQSXNqY0lMN3VocnM3cTVFSHJWR1BaMzA1UFpvNjE5QkZJOHhvSW9mNklaeF9uNFUyaDZPQURrMm9YRGN1UnltYkVpVmtHODQ0U2tzd2h0UG95TXBGS1VnYlIyY2t1NExfNUt0YnhER1NIa3VQaFBteXdWNmc?oc=5
- [NOTUS] Another Federal Judge Declines to Block Trump’s Taxpayer-Funded Ads After DNC Lawsuit - NOTUS (2026-11-26) - https://news.google.com/rss/articles/CBMimgFBVV95cUxNS1ZiRVJ0VWhUbGlILVNRZzZKMy0wd3RZUkZBNTBrTnhSTUJjYW1RUjVNLVhhUEtNYndndkhPYng5Wm9hbW5RTm5kMEluS1hQNzJhQnRWSTJOOHQteUpoNHpzWjJUdkdqRlRqRTBXQ1d1d2w2YXFSYV9iTy1CSkFYaFNGRTBKNHoyUlRHZ0N2anFmRVlsT0RLZDd3?oc=5

### Election Administration Capture
- Assessment: This reports an allegation (via affidavit) that a Trump-appointed director of election security sparked a Georgia office raid. This represents a real action that has occurred—a raid of an election office—allegedly directed by a Trump administration official. While the severity is not extreme (no election was cancelled or overturned), this constitutes a credible signal of election administration being subject to partisan pressure from the executive. The involvement of a Trump administration official in directing action against a state election office suggests potential partisan capture or interference.
- [ABC News - Breaking News, Latest News and Videos] Trump director of election security sparked Georgia office raid, affidavit says - ABC News - Breaking News, Latest News and Videos (2026-11-26) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5

### Press Restrictions or Retaliation
- Assessment: ABC News reports that the Trump administration has targeted specific individuals including James Comey. This constitutes a real occurrence of state action that raises costs or legal risk (targeting by name creates reputational, investigative, or potential legal pressure). However, the report is limited to naming individuals targeted; without detail on the specific mechanism of retaliation (prosecution, removal from office, legal action, loss of license), the severity is contained at level 2 rather than escalated. A confirmed, orchestrated campaign with verifiable legal or official action would be severity 3+. This is credible press coverage of a real targeting action.
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-11-26) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

### Legislative Bypass by Executive
- Assessment: Multiple credible sources report that the Supreme Court allowed Trump to implement parts of a mail-in voting executive order. This represents a shift of voting-rule authority from statutory/legislative control to unilateral executive action via EO. The Court's allowance (likely through stay or injunction ruling) enabled executive implementation without requiring legislative authorization. This is a real, confirmed action that transfers governance authority from statute to executive fiat, but is narrowly scoped to mail-voting procedures rather than a broader structural dismantling. Severity 2 reflects this as a real, credible stress signal of limited scope, not yet structural failure.
- [ABC News - Breaking News, Latest News and Videos] Supreme Court allows Trump to implement parts of his mail-in voting executive order - ABC News - Breaking News, Latest News and Videos (2026-11-25) - https://news.google.com/rss/articles/CBMigAFBVV95cUxQLUpWVmxZNkVNNGxlamhNRjkteVhjUVJNMXhDQ3Vyc3V3UkdTVEcyeUM0ZnEzTUlJQXRYMUZsNkZ5LTN5Q0VzWDFrVmVFSVlpOFBSaEpwa19qd0Q4SExzankxMEpIQjMxT2k5R0Z3emE0cDFCNng3V3lwVjBQUDg1NNIBhgFBVV95cUxOWGtmd1BpZ1U2QlJOeTZIcXhKMTVTOVFEZDJKcDJPS1NzX2NsOG1RT2w2TkpUMDkwTWY1QzlZcGt4LVlmNV9NZlFVUG04S0Y1U2hUSUdFSk5sUlFId1VsZzlnd1JvOGlWQnY2LThiN1J6cjZDSjdSWHd3elNWS3FpYWJqMXFnUQ?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 24
- Query feeds failed: 1
- Primary-source lookups: 22 signals, 7 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **High**
- Fetch errors:
  - election_certification_interference: courtlistener: HTTP Error 401: Unauthorized
  - election_delay_or_cancellation: courtlistener: HTTP Error 401: Unauthorized
  - alternate_elector_scheme: courtlistener: HTTP Error 401: Unauthorized
  - politicized_prosecution_opposition: courtlistener: HTTP Error 401: Unauthorized
  - opposition_ballot_exclusion: HTTP Error 429: Too Many Requests
  - opposition_ballot_exclusion: courtlistener: HTTP Error 401: Unauthorized
  - court_order_noncompliance: courtlistener: HTTP Error 401: Unauthorized
  - judicial_review_foreclosure: courtlistener: HTTP Error 401: Unauthorized
  - independent_agency_capture: courtlistener: HTTP Error 401: Unauthorized
  - inspector_general_retaliation: courtlistener: HTTP Error 401: Unauthorized

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
