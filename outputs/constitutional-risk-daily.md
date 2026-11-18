# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-18 12:28:21 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **16 / 100** (Elevated Strain)
- Previous day delta: **-1.0**
- Delta vs 7-day average: **+3.5**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 2.00 | 11.00 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.65 | 2.11 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.22 | 3.04 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 3.00 (Orange) | ai | 2 | 6 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 1 |
| Legislative Bypass by Executive | executive_constraints | 1.65 (Watch) | ai | 0 | 2 |
| Public Funds for Political Promotion | civil_liberties_information | 1.65 (Watch) | keyword | 0 | 0 |

## Evidence Samples

### Election Administration Capture
- Assessment: Trump directing the Department of Justice to sue to block Senate election results based on partisan outcome represents a direct attempt to use federal executive power to overturn or invalidate election administration and results. This is a verifiable action (Trump directing DOJ) to subordinate election administration to partisan control by invoking federal litigation authority over state electoral outcomes. This constitutes serious, confirmed action to capture election administration through executive branch pressure on the DOJ to intervene in state elections on behalf of a political party.
- [ABC News - Breaking News, Latest News and Videos] Trump told DOJ to sue to block Alaska Senate results if Republican narrowly loses - ABC News - Breaking News, Latest News and Videos (2026-11-17) - https://news.google.com/rss/articles/CBMipAFBVV95cUxQekhpNnRhMmk3WnMteVlLeVRYT2ZMUGRnRkJmSlJxUU9TUm1GN1ZEYWp5SFRqS20tSWVtQWpUMF9VaWd3U1FFRUd1TDRBMk9UTXhpMkhHTlE4NnQzZDEyRjUxQ3lkYlVkZHAxTS05MjJkbDA2VXFNQVBhcGdmUVJ3LTRHTjBScTBucno5Y0NhazNCeWdiLWpJMUlTRjF2Uk5zRzE2SNIBqgFBVV95cUxQUEZqTzdWbGhCLTVzd1J1VlI1cUxOOWFyLXZIbDI0TnA1YXlWQXgyMTFtaXRMdE9jbTIzTXdkUmpXMzJkejdKeHlXc2lHYWVJd2t3WFVVTmNwS05BT2wzTjhkeW0tZ3FpU0Z5aUxmOFFCMWNydkk1S3hPT09xT2w1WWdjdG5ybXRhWl9FZV84TG5kOWM0YkZwNVVYWU9keUFfZWF1ZVIwRUs3UQ?oc=5
- [ABC News - Breaking News, Latest News and Videos] Trump director of election security sparked Georgia office raid, affidavit says - ABC News - Breaking News, Latest News and Videos (2026-11-17) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5

### Press Restrictions or Retaliation
- Assessment: ABC News reports that the Trump administration has targeted specific individuals including James Comey. This constitutes a real occurrence of state action that raises costs or legal risk (targeting by name creates reputational, investigative, or potential legal pressure). However, the report is limited to naming individuals targeted; without detail on the specific mechanism of retaliation (prosecution, removal from office, legal action, loss of license), the severity is contained at level 2 rather than escalated. A confirmed, orchestrated campaign with verifiable legal or official action would be severity 3+. This is credible press coverage of a real targeting action.
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-11-17) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

### Legislative Bypass by Executive
- [Diplomacy and Law] War Powers Act: How the 1973 Resolution Limits Presidential War-Making - Diplomacy and Law (2026-11-18) - https://news.google.com/rss/articles/CBMiYEFVX3lxTE1IMU54NHhXM0NhUHJwM19lZFNRMGNnZkdLeE1UTE1LRHl6Zk9GODZnMGdhOHVGdHVpYThJZE9Xc3V6VVpoWXVGZDFFZndISjQ5dVlxeGE2STA3SENQeHI1VQ?oc=5
- [ABC News - Breaking News, Latest News and Videos] Appeals court blocks construction of White House ballroom - ABC News - Breaking News, Latest News and Videos (2026-11-17) - https://news.google.com/rss/articles/CBMinAFBVV95cUxNSW5aYzhFSU9YYUZ6dWtZZ3IxSXgxcXRkU3ZmX3dPeFdtOUpVRDFjMjNzTzB0SEptMnFxUkFtWmFXamYwenRTMTdoaVdYTU90OVlEd3V3blBqVVQtREx2NzJfT21ab012SE5kSVNjTzJGRkVfRklBcWt1WmhVX2RBdjA0V2JVdXlsVXU0NHNmTUtsdkh4ZjlpcUp1YzHSAaIBQVVfeXFMT1dUdHR5em8zNThqVVhUYXpLMDYzQ2pqZ1NtdTR2MXJxaDBHR1pZd0trbUc3TzJ1OEhweVRtRjRhNEotUXdtcC1RTTFZdXF5LXVPQzlmcUUyVW5JTWs2ZTBLRE1ZVDh3U3E5YVNPaHhxak1KZS1XU0JuYnpXaEhqb3RwMUZmc3ExYmN2NEhaMnBHMmRhSUMtY1RTTm1KU01VcVN3?oc=5

### Public Funds for Political Promotion
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 23
- Query feeds failed: 2
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
  - independent_agency_capture: courtlistener: The read operation timed out
  - inspector_general_retaliation: courtlistener: HTTP Error 401: Unauthorized
  - public_funds_political_promotion: HTTP Error 429: Too Many Requests

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
