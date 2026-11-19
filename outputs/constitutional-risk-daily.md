# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-19 12:28:23 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **13 / 100** (Baseline Institutional Noise)
- Previous day delta: **-3.0**
- Delta vs 7-day average: **+0.6**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.65 | 9.07 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.43 | 1.41 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 0.98 | 2.46 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 2.65 (Yellow) | ai | 0 | 4 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.65 (Watch) | ai | 0 | 1 |
| Legislative Bypass by Executive | executive_constraints | 1.30 (Watch) | ai | 0 | 2 |
| Public Funds for Political Promotion | civil_liberties_information | 1.30 (Watch) | keyword | 0 | 0 |

## Evidence Samples

### Election Administration Capture
- [The Texan] Report Card: The State of the Takeovers - The Texan (2026-11-17) - https://news.google.com/rss/articles/CBMizwFBVV95cUxQV0ZSUkoxQ2Z5Q1FpNVg1ZUYtanppaDRlbWJfNUFhdW1fTHdIYmlhNnRYUVRMVmVpY05JNWE0SlNuQ0hRMUJhZ1VxSmRvbEN3cUZoTUNlZy1pblNERlFHUnhnN056Xzd4VHFUZlo1NUJvdzk2M3ZNalc0aHZSMXRDNWxhaHlwSjl5RUJNSlBqLUhicVdqdld0Z2FsRG4teVh5XzFJR3RyTl90ajg5Zk4wbS1fMDBfNGZmYUVtenQxa0lwZDFxUmFxcVk2Y3VUbU0?oc=5
- [Newsweek] How the Midterms Hurt MAGA’s Grip on Swing-State Elections - Newsweek (2026-11-17) - https://news.google.com/rss/articles/CBMihgFBVV95cUxPSXlXVUtjV1NkREh5WEl1djFpX0dlY0N4Tk9Ic0V0Z29fRENzVVVndFhEYTR4cHRKbnRPM1JueHBVX0ItbDJzRzlablV1QWt2U29KMXJVZ1NwUzV4ektyTHhqOEVhVW90b2JYX0VheUZ6MkpXM2NSLVVqb3RoMkdBcTdlUERLdw?oc=5
- [The New Republic] Google’s Attempt to Force Schools to Use Its AI Tools Is Backfiring - The New Republic (2026-11-18) - https://news.google.com/rss/articles/CBMiX0FVX3lxTE0xSkpzYkpQeC1iNDJjbDNpdlRfYTh0SjFBdjVabWNwSElpWEdkMWpGVGVZQ1BiRXBHaHI5NXFYR0tRdTRYRFRNRVVWZkRQelRXTDZ6NUo3QXl2UW04UkV3?oc=5

### Press Restrictions or Retaliation
- [Journalism Pakistan] Is Asia using the law to silence independent journalism? - Journalism Pakistan (2026-11-18) - https://news.google.com/rss/articles/CBMilAFBVV95cUxQM0FZT2MtNElycU9wXy0yQTFld25tSmc4ekt6U2E5LS0yMFE3LVBZVUtELWhXRHZzam43VDBSQXdaX3piRGVHeGpDZ1pMZGwycGlIanRwazVjOVhObmZZcGdoYWlfTFR6U29WZk1TdjVWbHlJZWUwb3JLNDBsU2QweUdLTG5PR3JVQ2lkRHUyOE9pU2ZT?oc=5

### Legislative Bypass by Executive
- [The Dispatch] Impeachment Is Fine, but Have We Tried Laws? - The Dispatch (2026-11-19) - https://news.google.com/rss/articles/CBMihAFBVV95cUxNcURRNk0zMzQxNlhlNTRSUll6aEpoMmpxWGdoemRpRElNYWQtbjJOWnBQV0FZWjFibE50SGNhWnJsNHpGQ3hxTVpsa3g4RmlDS3Z2TjNlVzR0cjdUOXduWGxxeF8tbXNjV1hvUHU4eHNiQmt2Q0xEVG5CUHJmQ2xqOFFRTmk?oc=5
- [Diplomacy and Law] War Powers Act: How the 1973 Resolution Limits Presidential War-Making - Diplomacy and Law (2026-11-18) - https://news.google.com/rss/articles/CBMiYEFVX3lxTE1IMU54NHhXM0NhUHJwM19lZFNRMGNnZkdLeE1UTE1LRHl6Zk9GODZnMGdhOHVGdHVpYThJZE9Xc3V6VVpoWXVGZDFFZndISjQ5dVlxeGE2STA3SENQeHI1VQ?oc=5

### Public Funds for Political Promotion
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 24
- Query feeds failed: 1
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
