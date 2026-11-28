# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-28 12:27:07 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **9 / 100** (Baseline Institutional Noise)
- Previous day delta: **-3.0**
- Delta vs 7-day average: **-0.8**

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
| Executive Constraints and Emergency Powers | 13 | 0.65 | 2.11 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.33 | 3.33 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 3 | 5 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 1 |
| Legislative Bypass by Executive | executive_constraints | 1.65 (Watch) | ai | 0 | 4 |
| Election Administration Capture | elections_transfer | 1.65 (Watch) | ai | 0 | 2 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: News report indicates Democrats lost a court bid to block taxpayer-funded pro-Trump ads. This reports a real occurrence—the ads themselves are airing using public funds. The event (taxpayer funds spent on pro-Trump communications) has occurred and matches the signal. Severity is 2 (confirmed but contained action) rather than 3 because judicial relief was sought and partially declined, suggesting oversight mechanisms are functioning even if unsuccessful here. No structural constitutional failure is evident.
- [Newsweek] Democrats Lose Bid to Block Taxpayer-Funded Pro-Trump Ads - Newsweek (2026-11-26) - https://news.google.com/rss/articles/CBMilgFBVV95cUxPWHQzLXFjaDhHVkE4dzQ4YzNhU3dqYjRncXJQSXNqY0lMN3VocnM3cTVFSHJWR1BaMzA1UFpvNjE5QkZJOHhvSW9mNklaeF9uNFUyaDZPQURrMm9YRGN1UnltYkVpVmtHODQ0U2tzd2h0UG95TXBGS1VnYlIyY2t1NExfNUt0YnhER1NIa3VQaFBteXdWNmc?oc=5
- [Dosya Haber] Federal Judge Rejects Long-Term Ban on Taxpayer-Funded Trump Ads - Dosya Haber (2026-11-26) - https://news.google.com/rss/articles/CBMiqwFBVV95cUxOaTBEUFliZ3ZGRE9lNm9Xam04bjhMUUFsSWNuRmVxZTJWMDhaOVpGbWxXN2Z5bTc0YTNQa1hkQnNHTEIwRjczbUlhdWJmMTJJMDVFbnVkYkR5cHV0WDZlSV9wNGQ3Mm9UOXlSQkktWWtJYUNMU3NCbElVY2JuVU5HbFQ1azBuR0ZyamVoNVNUWVZ3R0tieUpSOWdFZThuOFplVUdsei16enJyRG8?oc=5
- [Crave Online] Donald Trump Scores Legal Win From Biden-Appointed Judge in Taxpayer-Funded Ad Battle - Crave Online (2026-11-27) - https://news.google.com/rss/articles/CBMilAFBVV95cUxNM3pWWnB2dE9iU2pBeFcwZlFxM0s0LUtLbW9nazBtTzVEWDhDbm1jVUpyREhMbU9DamhYRE9pUnU1by1DXzVnV1pWT09XUi02Y2t4ampWcm5fLWM5N21CbUxOZ19TNERiZWE2Wlk4aXVkakNHYjl5RDhFTWlkTTFlV2d6RXZ4V1dLRFQ0a0s1UmJwSGFF?oc=5

### Press Restrictions or Retaliation
- Assessment: ABC News reports that the Trump administration has targeted specific individuals including James Comey. This constitutes a real occurrence of state action that raises costs or legal risk (targeting by name creates reputational, investigative, or potential legal pressure). However, the report is limited to naming individuals targeted; without detail on the specific mechanism of retaliation (prosecution, removal from office, legal action, loss of license), the severity is contained at level 2 rather than escalated. A confirmed, orchestrated campaign with verifiable legal or official action would be severity 3+. This is credible press coverage of a real targeting action.
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-11-26) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

### Legislative Bypass by Executive
- [ABC News - Breaking News, Latest News and Videos] Democrats take the House. Here’s what they plan to investigate and their legislative agenda - ABC News - Breaking News, Latest News and Videos (2026-11-28) - https://news.google.com/rss/articles/CBMiqAFBVV95cUxQcnFYZUlFZG0yREt2N1BuWkxsbWlkaTlNcVpzUUhGcnQtbVVURWFFSnhxT2EwWVlBeHhDLTBXb0tqNXk1bXZhcUpWdDIzZ0tsRWQwMENmN01pV2JDUENGZXZBWFhERmRqdzhUeldFam5IMW9Ta0R5NmR0UUV2elFDcEFHOHBLNlhHUVFMR1c0RGNFTEh0ZVpZTmVZOHRuLThITV8waG8yMW3SAa4BQVVfeXFMTTUwZl80MTBuZEl0Tmo1dHBYbkc4X2pTQ05fUWI5VEtkVEcxWnYxS3RBSXdnQzROZE4wR3BtYVdUOWhqbVhWRW9iLWNqWGtRZTFhQVJoMi12bllqSnNWVld4SHctWk1ydnpTdGpWc1c0QjRMM1FranFhekpjTm11TmlNUVI1ZWtpNXl2V2ozS1VIY0RVNHdZUEpYVDhkVHNERVdUMlFEb0pGUEdtV0hR?oc=5
- [Britannica] Donald Trump | Birthday, Age, Education, Biography, Impeachments, & Military Parade - Britannica (2026-11-28) - https://news.google.com/rss/articles/CBMiXkFVX3lxTE4zTlNFQlJBYmZmZE9MbUdKWElnLXE0c2pWcVFIenNYSjQwbURvQm5kUmRFQVM1NVlCT24zZktQZHliMEV4ZnZ1QzM0VEpZWS1pWWxON0ZUa3N0RUpmemc?oc=5
- [ABC News - Breaking News, Latest News and Videos] Appeals court blocks construction of White House ballroom - ABC News - Breaking News, Latest News and Videos (2026-11-27) - https://news.google.com/rss/articles/CBMinAFBVV95cUxNSW5aYzhFSU9YYUZ6dWtZZ3IxSXgxcXRkU3ZmX3dPeFdtOUpVRDFjMjNzTzB0SEptMnFxUkFtWmFXamYwenRTMTdoaVdYTU90OVlEd3V3blBqVVQtREx2NzJfT21ab012SE5kSVNjTzJGRkVfRklBcWt1WmhVX2RBdjA0V2JVdXlsVXU0NHNmTUtsdkh4ZjlpcUp1YzHSAaIBQVVfeXFMT1dUdHR5em8zNThqVVhUYXpLMDYzQ2pqZ1NtdTR2MXJxaDBHR1pZd0trbUc3TzJ1OEhweVRtRjRhNEotUXdtcC1RTTFZdXF5LXVPQzlmcUUyVW5JTWs2ZTBLRE1ZVDh3U3E5YVNPaHhxak1KZS1XU0JuYnpXaEhqb3RwMUZmc3ExYmN2NEhaMnBHMmRhSUMtY1RTTm1KU01VcVN3?oc=5

### Election Administration Capture
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-11-26) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5
- [ABC News - Breaking News, Latest News and Videos] 'Going to be practical': Sen. Markwayne Mullin speaks out after being named Noem's replacement at DHS - ABC News - Breaking News, Latest News and Videos (2026-11-27) - https://news.google.com/rss/articles/CBMipgFBVV95cUxQRGFPSVpoVFZTUlFjaDZRakItV05kaVlGVlluM1pMRGRvTkpaS2RFNlY2ZElwbFFOUEwtQVhSTzVVZlRmSmVBb1JFZDBaaVRqR05kNnZydDNBcFVOak5ENzZvRmdaOFdLTk9sUk9Kc3hSdnB4a3VEcGl6NDJ0M2RNTG9mMjFSUkd0MlNUYnl2QTNjeDI3aWt1UHM3WVBXaGhTOVY0VXBR0gGrAUFVX3lxTE1JN1FWZ1RwMHQ4aEpyckdLR2RxTnhucVUwZ21uVWZscnBKU3MxZFBQX3RaTXlBZE45YnBXLUo0OW4tSWRWdDRRVnFtTHhxbVdzMTJuLTNYQXdQUlB2M0hobldMT05hN2xscnlXLXVjT2VaX2I5WXlzWWdiY0lWNHIzZ0dDMnBDTFN5bUx1bXpQRkduNzdjcF9nS2ZqbTZZMm5YQmRaOTlPVjdNYw?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 6 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **Medium**
- Fetch errors:
  - election_certification_interference: courtlistener: HTTP Error 401: Unauthorized
  - election_delay_or_cancellation: courtlistener: HTTP Error 401: Unauthorized
  - alternate_elector_scheme: courtlistener: HTTP Error 401: Unauthorized
  - politicized_prosecution_opposition: courtlistener: HTTP Error 401: Unauthorized
  - opposition_ballot_exclusion: courtlistener: HTTP Error 401: Unauthorized
  - court_order_noncompliance: courtlistener: HTTP Error 401: Unauthorized
  - judicial_review_foreclosure: courtlistener: HTTP Error 401: Unauthorized
  - independent_agency_capture: courtlistener: HTTP Error 401: Unauthorized
  - inspector_general_retaliation: courtlistener: HTTP Error 401: Unauthorized
  - military_domestic_political_use: courtlistener: HTTP Error 401: Unauthorized

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
