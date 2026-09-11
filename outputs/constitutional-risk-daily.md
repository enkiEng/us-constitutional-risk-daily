# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-11 16:35:00 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **12 / 100** (Baseline Institutional Noise)
- Previous day delta: **+3.0**
- Delta vs 7-day average: **-1.0**

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
| Executive Constraints and Emergency Powers | 13 | 1.10 | 3.57 |
| Civil Service and Agency Independence | 10 | 0.65 | 1.62 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.65 | 1.30 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 3 | 4 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 0 |
| Civil Service Purge / Schedule F | civil_service_integrity | 1.65 (Watch) | ai | 0 | 0 |
| Legislative Bypass by Executive | executive_constraints | 1.30 (Watch) | ai | 0 | 2 |
| Legislative Oversight Obstruction | federalism_oversight | 1.30 (Watch) | keyword | 0 | 0 |

## Evidence Samples

### Election Administration Capture
- Assessment: This reports an allegation (via affidavit) that a Trump-appointed director of election security sparked a Georgia office raid. This represents a real action that has occurred—a raid of an election office—allegedly directed by a Trump administration official. While the severity is not extreme (no election was cancelled or overturned), this constitutes a credible signal of election administration being subject to partisan pressure from the executive. The involvement of a Trump administration official in directing action against a state election office suggests potential partisan capture or interference.
- [ABC News - Breaking News, Latest News and Videos] Trump director of election security sparked Georgia office raid, affidavit says - ABC News - Breaking News, Latest News and Videos (2026-09-11) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5
- [Mother Jones] A MAGA activist flooded Georgia with voter challenges. Now he works for the State Election Board. - Mother Jones (2026-09-09) - https://news.google.com/rss/articles/CBMi6AFBVV95cUxPY3B6V1ZMWWpwWUZMNmo5NkN5bzZOQ3plRGE2d1lxcUNKbktiTGVmWDRjc3p0dkMzQkJMNmtFR3ZySGxBX3VodEZEanh5OEh1WVlXSjlLU2VzSUhKVGIxSU41VzFhZktyaDdXcjBWUmFZcDVUdXc3MlJtTWZmcWFMSUhtb0RPTWs5NTVyTm9UN1VZZDh1cF9US2RmMG1lbjk0WDRPaW43d2d6UVFobmRmaHVBNmxDcmFvUU5aTDYyaVpaOVloZHoxdDFhMlJKZVl6SDd1Q2N0SGtqRUM2Z0xjVzVBeFF5aF91?oc=5
- [rawstory.com] MAGA activist who targeted thousands of voters lands state election job: report - rawstory.com (2026-09-09) - https://news.google.com/rss/articles/CBMiUEFVX3lxTE9yRXlLSDdBX0kwekNjS3dKOHRfQi1WN1VWQ2hoMEJYOFlDaXJzRi1WQVl4b1d1Sk53YTlBdU5tNFlWZ3ZySEEwMlo2bVV3MUNQ0gFjQVVfeXFMTzNhYlBLX2N5UDlfN3I2TW9IV2Q5SFJpdF9ET0ZDRGZycndfYVk3LXpXaUJMcS00bDlVNDV3OFJ2Q2I5MHFoblZjRzlsQVFMS2dVTmNFUkh2dVRKU2xtcFgwbGJF?oc=5

### Emergency Powers Expansion
- Assessment: A presidential continuation of a national emergency declaration is a real, documented action that invokes emergency authorities to maintain powers that bypass ordinary legislative process. This is an official Federal Register record of an executive action. However, this represents a routine renewal of a long-standing emergency declaration (post-9/11 terrorist emergency), not a novel expansion or structural breach. The National Emergencies Act (50 U.S.C. § 1601 et seq.) permits such continuations and requires congressional notification. While emergency powers do bypass ordinary process, this is within the statutory framework and constitutes a contained, recurring action rather than a new seizure of authority or defiance of legislative/judicial check. Severity is 2: a credible, real stress signal (emergency authority maintained) that is repetitive and authorized by statute, but not a serious novel violation or structural failure.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Certain Terrorist Attacks (2026-09-10) - https://www.federalregister.gov/documents/2026/09/10/2026-18589/continuation-of-the-national-emergency-with-respect-to-certain-terrorist-attacks

### Civil Service Purge / Schedule F
- [federalregister.gov] **[official record]** Driving Efficiency in Farm Loan Delivery (2026-09-04) - https://www.federalregister.gov/documents/2026/09/04/2026-18164/driving-efficiency-in-farm-loan-delivery

### Legislative Bypass by Executive
- [Missouri Independent] US Supreme Court again blocks use of Missouri’s gerrymandered congressional map - Missouri Independent (2026-09-10) - https://news.google.com/rss/articles/CBMivwFBVV95cUxQcUFjblBrcWs3ejQ3VURLQlUydGNveG9BUkhRRzVsTWR6UURVX2RLb1hwZTZJVDRNWkwxTy1aVUhtUFVjLXlIVzBRWVZWWEtPTEp4UDBfaTdlY1RhbDNCWjg0LXBORVU2OXdnU09xZjVkNHozdUo3Sl9fdlFSZkFxenVBTHRWS1NkNGpiWWhFU2ZOQ2NQSWhTc21faFFITVhkbEJuRFpnWU9va25GY0d0NGlsdEFsajR4ZVFRblcwWQ?oc=5
- [LawFold.com] California Oregon DEI Grant Lawsuit 2026: Full Guide - LawFold.com (2026-09-10) - https://news.google.com/rss/articles/CBMibkFVX3lxTFA1T2Ywa3dDYjNvdE9oTDJMUGMzOTdiUnhhRzZacklnN0lXSlZKMHo0eTFrUXI1MWhuZGhFWUFPdUlyR2w4Z09xVVdGZ0NXWm84RjRKR2xqNHRGYnVWbEVsNE1FTEo3Z3lYNG5pZXdn?oc=5

### Legislative Oversight Obstruction
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 24
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 11 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 1
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
