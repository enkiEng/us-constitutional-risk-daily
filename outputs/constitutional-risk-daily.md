# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-05 12:28:45 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **12 / 100** (Baseline Institutional Noise)
- Previous day delta: **-3.0**
- Delta vs 7-day average: **-4.5**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 0.33 | 1.22 |
| Opposition Rights and Political Pluralism | 14 | 0.08 | 0.29 |
| Executive Constraints and Emergency Powers | 13 | 0.75 | 2.44 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.00 | 2.50 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.10 | 0.20 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 2 | 16 |
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 3 |
| Emergency Powers Expansion | executive_constraints | 1.65 (Watch) | ai | 3 | 1 |
| Election Certification Interference | elections_transfer | 1.65 (Watch) | keyword | 0 | 0 |
| Judicial Review Foreclosure | judiciary_rule_of_law | 1.30 (Watch) | keyword | 0 | 0 |
| Legislative Bypass by Executive | executive_constraints | 0.60 (Green) | ai | 0 | 24 |
| Opposition Ballot Exclusion | opposition_pluralism | 0.25 (Green) | keyword | 0 | 0 |
| Legislative Oversight Obstruction | federalism_oversight | 0.20 (Green) | ai | 0 | 1 |

## Evidence Samples

### Election Administration Capture
- Assessment: This reports an allegation (via affidavit) that a Trump-appointed director of election security sparked a Georgia office raid. This represents a real action that has occurred—a raid of an election office—allegedly directed by a Trump administration official. While the severity is not extreme (no election was cancelled or overturned), this constitutes a credible signal of election administration being subject to partisan pressure from the executive. The involvement of a Trump administration official in directing action against a state election office suggests potential partisan capture or interference.
- [ABC News - Breaking News, Latest News and Videos] Trump director of election security sparked Georgia office raid, affidavit says - ABC News - Breaking News, Latest News and Videos (2026-11-03) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5
- [NewsNation] Texas GOP pushes to limit Hinojosa’s power before takeover - NewsNation (2026-11-05) - https://news.google.com/rss/articles/CBMie0FVX3lxTFBGMVoyVnk3QmY0cUYzeEVMRWxhM0JIRXFwSnJaNW9FaU14MDA0d3BtakVCNHhsdFdxVENPemVfYk5ndmQwSnA2bW9IQWVNaklfNW1SVE5maHJCRk1BSzFQUjB2bU9FU2xHa2RYQnJvT1lpMnBDUHk1ZGlnSdIBgAFBVV95cUxQV0N4U3BLcFMwc2FyM0gyaGx5Y0NIMWFmVFB2NTcxekNZcGFoNVJMTlJQbGlQYWlOb08tSlhwWnc3eFFGaVFkS0daRGZRVk9RWXNPdnp3Rm00cF9qRVQwOFRmNFpwLUkyVWtGdWJIUG9sNDVIaWVwUkpDa2dvWkE1OA?oc=5

### Public Funds for Political Promotion
- Assessment: The headline reports that federal agencies used an internal list to send a pro-Trump email blast before an election. This is a credible report of an alleged use of federal communications infrastructure and resources for partisan/candidate promotion, which directly matches the signal definition. However, without access to the full article or official documentation, the confirmation status and scale of the action cannot be fully verified. The timing (before election) and partisan nature ('pro-Trump') align with the signal's definition. Severity is 2 (repeated or credible stress signal) rather than higher because the report is from a news outlet rather than an official record and details are limited.
- [Truthout] Federal Agencies Use Internal List to Send Pro-Trump Email Blast Before Election - Truthout (2026-11-03) - https://news.google.com/rss/articles/CBMisAFBVV95cUxNVC1KdWtfWTJzX2VLd0p5alkxZ1daSkJTUXNrWlBDdTlmd1NGNmR3UTdGWEdHNXJYWEVWcGpuWUlHZWFBSHFwMUpBcmVRZ1ppWDBaS2lPbUVsT3lDbXdSdTY1THUzUVpkbGNIMnN1RGFsSEl2eEFRclp1b0lCZXJoYlRTT2xNd2pZcmpoOTZuMGlTUTh1UHNsRWRPNWpfbUpRSDhjNDJ5bUJQUkw0bzdCNw?oc=5

### Emergency Powers Expansion
- Assessment: This is a continuation of an existing declared national emergency under the National Emergencies Act (NEA). Continuation of a previously declared emergency is a routine executive action that renews authorities already granted by Congress through the NEA framework. While the NEA does permit emergency powers to bypass ordinary rulemaking, continuation documents are ministerial renewals of standing authorizations, not new expansions. The underlying emergency was declared in an earlier year; this 2026 continuation represents ongoing use of existing delegated authority rather than a novel expansion. Severity is low because continuation is the ordinary operation of a congressionally-authorized framework, not a structural bypass of legislative process.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to the Threat From Securities Investments That Finance Certain Companies of the People's Republic of China (2026-11-05) - https://www.federalregister.gov/documents/2026/11/05/2026-22688/continuation-of-the-national-emergency-with-respect-to-the-threat-from-securities-investments-that
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to the Proliferation of Weapons of Mass Destruction (2026-11-05) - https://www.federalregister.gov/documents/2026/11/05/2026-22686/continuation-of-the-national-emergency-with-respect-to-the-proliferation-of-weapons-of-mass
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Iran (2026-11-05) - https://www.federalregister.gov/documents/2026/11/05/2026-22685/continuation-of-the-national-emergency-with-respect-to-iran

### Election Certification Interference
- No fresh evidence links in the current lookback window.
### Judicial Review Foreclosure
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 12 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 3
- Evidence extraction: AI event extraction
- Confidence: **High**
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
