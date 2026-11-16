# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-16 12:37:17 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **7 / 100** (Baseline Institutional Noise)
- Previous day delta: **-3.0**
- Delta vs 7-day average: **-4.4**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.95 | 5.22 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.00 | 0.00 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 0.65 | 1.62 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 1.95 (Yellow) | ai | 0 | 4 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.65 (Watch) | ai | 0 | 2 |

## Evidence Samples

### Election Administration Capture
- [The Atlanta Journal-Constitution] After a Democratic sweep, Georgia’s election board faces a reckoning - The Atlanta Journal-Constitution (2026-11-16) - https://news.google.com/rss/articles/CBMiekFVX3lxTFBRMnBoQmMxUUhJM2Q0b2Z6dDJsMi1xWWE4MTZtUzJ4bGFhbTZTaHVhbVdLamJlQzNHMlNiNjlVQmt4VWpXaU1WOEMxT1AzYUZCd0hXeXo4S1RBZ3NqRjMyd3dDT2VoY01pd0xtZXBTYWxjRUw1a2t3Zmx3?oc=5
- [San Antonio Report] 7 ways blue San Antonio is gearing up for a Democratic takeover in Texas - San Antonio Report (2026-11-15) - https://news.google.com/rss/articles/CBMimAFBVV95cUxNNkNrcEljMEltX1NjczVoLW1mSVZ0Y1ZnQldCa1V4UVotTm5HSnNhTTlZRzFkanhtY1pQWWlFR1VRdkZabFNQZFhXZTRjem9NcUl2clJDN0tEQ2dGS25qLVU2SGdEMVkwdDNHbDlNVGhEZ0dCSEtSTGtsLUZMd0FaRzhwZy1LUmFoUDRuVUYxdTJJQ3FKNlNXdQ?oc=5
- [Britannica] Trinamool Congress - Britannica (2026-11-16) - https://news.google.com/rss/articles/CBMiYEFVX3lxTFAyY0d3dDhTMU9aVG1Gemt6TGV0NGVrWkNBSDZROVFjSUkzLTZiTTJicTdEUzZMMzFlRnFnLWRmbEtrOXdvdmkxSHhpeW1yLWRCTUh6bDlsTFZpMVhCMXZGVQ?oc=5

### Press Restrictions or Retaliation
- [Journalism Pakistan] The price of reporting: Prison, violence and intimidation - Journalism Pakistan (2026-11-15) - https://news.google.com/rss/articles/CBMilAFBVV95cUxNVnU3ZDlLd29Vc01YM2pqejM5SkpSbjIxb3dNSzlMbS1makxWeGVnU1RYbXp1S19NRzBwY2FmeTNfckdmaFF0ODRtdzl1dldxSThuWkF2dGQtLUpSREdFaGZrSVhOSFNUaUQwV1FSUDBtZnVrRnE2c3NCRE1fdkZCaXdFSkZBS21JbFhOQzlGOExmcEE3?oc=5
- [Ratopati] Government Must Prioritize Reconstruction Over Political Retribution - Ratopati (2026-11-16) - https://news.google.com/rss/articles/CBMi1wFBVV95cUxPNU5wRTQ5MThDTlRhVUQ3TGxmMHVOTWNKLTNqNV9WNkotcFBFSXJyaWVkM21VLVB2V04yTVhOVmhlbjZmQzFNanpIWU5Uc2FlREtBX0NFMGwzZ1E2RkFlallxTmd5WlBYWDBNdUxWeW1vM0c2bVVhdUF4OWVtaVcxOUJTMUhnSHRTMXVsd3pRcE1ib3JnMElnRU0ycjNBVWxNVGRBd1cwRmZXR3VWcUowM0FSTjFIREpYY1FFMjFRTDdkQ2hqUE44NURKZlRPWGJpZnJvdzhnOA?oc=5

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
