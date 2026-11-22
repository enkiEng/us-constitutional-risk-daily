# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-22 12:26:47 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **9 / 100** (Baseline Institutional Noise)
- Previous day delta: **+2.0**
- Delta vs 7-day average: **-2.3**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.60 | 3.30 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.00 | 2.50 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 2 | 4 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 2 |
| Election Administration Capture | elections_transfer | 1.60 (Watch) | ai | 0 | 2 |
| Public Funds for Political Promotion | civil_liberties_information | 0.25 (Green) | keyword | 0 | 0 |

## Evidence Samples

### Legislative Bypass by Executive
- Assessment: This reports that Trump has restricted congressional access to federal contractors via executive action. If a completed executive order exists that formally restricts Congress's ability to access or obtain information from federal contractors, this constitutes a real action that shifts authority from legislative oversight (a statutory or constitutional power of Congress) to executive discretion. This is a credible signal of legislative bypass. However, without full verification of the order's scope and enforceability, and given the report is from a secondary source, severity is marked conservatively at 2 (confirmed but contained action) rather than 3. The action appears to have been issued, not merely proposed.
- [Limapagi] Trump Restricts Congressional Access to Federal Contractors - Limapagi (2026-11-22) - https://news.google.com/rss/articles/CBMidkFVX3lxTE9BS1N4ajh2alhYNUk4WEV2eWtyZk9YRTU2WTJLV3h6OHVhbHhZdkpXTm5FZEZySkRzTGUteXVDM3hCeGtrS3lxV192WW9IOF9WZ3BMNVZtdnNVN3ExYlRZUGpXd09rQkFrc0NUWTVrVVhpVEN1Unc?oc=5
- [NewsBreak: Local News & Alerts] Andy Kim Warns Trump Is Moving to Block Congressional Oversight — Says ICE and GEO Group “Owe Us Answers” as New Executive Order Threatens Contractor Access to Congress - NewsBreak: Local News & Alerts (2026-11-22) - https://news.google.com/rss/articles/CBMiywJBVV95cUxONUlKWUJpY2w0b3NIazdMVWxVM3Q3VC03ZGV5VWk3TmF3UndMNlAzYlJoU3Nnb0pucHlUV3BpSFA3LWc0ck9CZ3RkNDFqMWtXM3Jmd05hb29VaENZeUxNcEY1VmJPMFh1MmoycGVuR0lpQ3U2eEZnSHBzTkk4THBxaDl6TnJ4UFFURWllb0x6c3hnWmh3aE1SbWthejZ3NkQweDJ5elNxRGg0aV9CREZrMmhhRDRHOHhiX002bFVKY2FRbUwzd1dNa2xPZWlwSVp5UDJ3RlFUaVFiRThBOXJudl9HX2lRbEwzQUk3ZG56djQ1Z3JGMUQwUE9yWDRnS3FLTlhuRTNUVEpRUGo2Q3FnamVBYk5MSmF6MXZQaHEzTlM1emFpTkNoVTh4SnVaR0VicTFxbnFQYVdUWlVJSUo0RTFVNDV1Uzh2bC1R?oc=5

### Press Restrictions or Retaliation
- Assessment: ABC News reports that the Trump administration has targeted specific individuals including James Comey. This constitutes a real occurrence of state action that raises costs or legal risk (targeting by name creates reputational, investigative, or potential legal pressure). However, the report is limited to naming individuals targeted; without detail on the specific mechanism of retaliation (prosecution, removal from office, legal action, loss of license), the severity is contained at level 2 rather than escalated. A confirmed, orchestrated campaign with verifiable legal or official action would be severity 3+. This is credible press coverage of a real targeting action.
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-11-21) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

### Election Administration Capture
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-11-21) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5
- [The New Republic] “Rude”: Trump Snaps at Woman Reporter Who Dared to Ask Question - The New Republic (2026-11-20) - https://news.google.com/rss/articles/CBMikgFBVV95cUxNeDkxdGdrRFA2dXFrZFRTWUY5S3dxdURQZnFCMTg3Zld6OWdLR2M0Ri1rNm9rVFFLOTJ0T3JaWU1lUHNKMTNjOHJGbWxMTzYyTkY0YVpfMDlPbl9fNE9FVTZUM0x0a2ZRdkVJNlZvVHZtSWFHcHN4TmR4cWUySi1KejQ2TXVfU1l1a2dYcG54a1FiUQ?oc=5

### Public Funds for Political Promotion
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 7 official documents (Federal Register, CourtListener)
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
