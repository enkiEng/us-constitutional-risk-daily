# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-12 15:36:30 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **15 / 100** (Elevated Strain)
- Previous day delta: **+3.0**
- Delta vs 7-day average: **+2.8**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 1.00 | 3.75 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.33 | 4.33 |
| Civil Service and Agency Independence | 10 | 0.33 | 0.81 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.47 | 0.95 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 2 | 3 |
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 2 | 3 |
| Judicial Review Foreclosure | judiciary_rule_of_law | 2.00 (Yellow) | ai | 1 | 0 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 0 |
| Civil Service Purge / Schedule F | civil_service_integrity | 1.30 (Watch) | keyword | 0 | 0 |
| Legislative Oversight Obstruction | federalism_oversight | 0.95 (Watch) | ai | 0 | 1 |

## Evidence Samples

### Election Administration Capture
- Assessment: This item reports a real, verifiable action: a specific individual with a documented record of partisan voter-challenge activity has been hired into an election administration position (Georgia State Election Board). This is a concrete instance of partisan personnel placement in election administration, matching the signal of election administration moving toward partisan control. The placement is confirmed and has occurred, but it is a single personnel decision rather than a structural, systemic capture or an official policy dismantling neutral process. Severity 2 reflects that this is a real, credible stress signal (personnel capture) but not yet a high-severity structural breach.
- [Mother Jones] A MAGA activist flooded Georgia with voter challenges. Now he works for the State Election Board. - Mother Jones (2026-09-12) - https://news.google.com/rss/articles/CBMi6AFBVV95cUxPY3B6V1ZMWWpwWUZMNmo5NkN5bzZOQ3plRGE2d1lxcUNKbktiTGVmWDRjc3p0dkMzQkJMNmtFR3ZySGxBX3VodEZEanh5OEh1WVlXSjlLU2VzSUhKVGIxSU41VzFhZktyaDdXcjBWUmFZcDVUdXc3MlJtTWZmcWFMSUhtb0RPTWs5NTVyTm9UN1VZZDh1cF9US2RmMG1lbjk0WDRPaW43d2d6UVFobmRmaHVBNmxDcmFvUU5aTDYyaVpaOVloZHoxdDFhMlJKZVl6SDd1Q2N0SGtqRUM2Z0xjVzVBeFF5aF91?oc=5
- [ABC News - Breaking News, Latest News and Videos] Trump director of election security sparked Georgia office raid, affidavit says - ABC News - Breaking News, Latest News and Videos (2026-09-11) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5

### Legislative Bypass by Executive
- Assessment: An appeals court has blocked executive rules on mail ballots, confirming that an executive order on this subject was issued. This represents a real attempt to shift election administration (normally a statutory/state matter) to unilateral executive action. The court block indicates the action occurred and was challenged, confirming the bypass attempt. Severity 2 because the action was issued but was judicially blocked, preventing implementation—a contained stress signal rather than successful structural override.
- [lawcommentary.com] Appeals Court Blocks Trump Mail-Ballot Rules as Supreme Court Weighs Presidential Power Over Elections - lawcommentary.com (2026-09-12) - https://news.google.com/rss/articles/CBMingFBVV95cUxNakVYTWxBb0hHNF9JUTFaMUtxdVRYMTNYRW1GYUdaNEhJenhBaWJWLXU5WTh2VEwxS2V0c1FaZTZONUY4RUwxQkJjZEdTdkFESFkteFVseTVUdkZnZnF6TDRaS2JaZjZNcFZMYlFObDN1V0NlaDVFVGtaUnp1MTVNYWZHeW1VSFlXT0I5NjllMUpiWmFac0Iwd2RPQktodw?oc=5
- [inkl] First Circuit Refuses to Stay District Court Injunction Against Trump's Executive Order on Mail-In Voting - inkl (2026-09-10) - https://news.google.com/rss/articles/CBMiygFBVV95cUxPbkE5Q3NKTFN0MVNGQ1R3NlhPdFVPOTJwaFRzRVJDZEEtR2gwcGgtYWdLdC1vT0xYMS1PVkpuaW13d0NwU0FoMUpYWmNpREIyZW5UdmNlX2J5aDU1a3BwaF94aF80S3ZldlBKdnhqQk4zckZwbjZLY0Mzc0RpVFhyRUVYWkpaOHQ5dnFEVllDallDU0FxSVdWZndpMFNLOUVjUEF1Y2NaYkZ4TDlRT2JtZHFDZThyd2h5MUhWb3ZJeDdmX195ZHllaHRn?oc=5

### Judicial Review Foreclosure
- Assessment: An emergency motion to stay an injunction pending appeal is a threshold procedural action that, if granted, would foreclose judicial review of the underlying merits by suspending the injunction without addressing legality. The filing of such a motion by government defendants (LaRose and Norman) and its docketing by the court represents a real procedural event seeking to remove active judicial oversight of government action. This is credible evidence of judicial-review foreclosure via emergency-docket mechanism—a contained stress signal of moderate severity. However, the record shows only that the motion was filed and entered, not whether it was granted; a granted stay would elevate severity. As filed, this constitutes a confirmed action that manifests the signal's mechanism (threshold grounds used to bypass merits review), though the outcome remains pending.
- [courtlistener.com] **[official record]** Red Wine & Blue v. Frank LaRose (2026-09-09) - https://www.courtlistener.com/docket/74762684/5/red-wine-blue-v-frank-larose/

### Emergency Powers Expansion
- Assessment: A presidential continuation of a national emergency declaration is a real, documented action that invokes emergency authorities to maintain powers that bypass ordinary legislative process. This is an official Federal Register record of an executive action. However, this represents a routine renewal of a long-standing emergency declaration (post-9/11 terrorist emergency), not a novel expansion or structural breach. The National Emergencies Act (50 U.S.C. § 1601 et seq.) permits such continuations and requires congressional notification. While emergency powers do bypass ordinary process, this is within the statutory framework and constitutes a contained, recurring action rather than a new seizure of authority or defiance of legislative/judicial check. Severity is 2: a credible, real stress signal (emergency authority maintained) that is repetitive and authorized by statute, but not a serious novel violation or structural failure.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Certain Terrorist Attacks (2026-09-10) - https://www.federalregister.gov/documents/2026/09/10/2026-18589/continuation-of-the-national-emergency-with-respect-to-certain-terrorist-attacks

### Civil Service Purge / Schedule F
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 24
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 16 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 2
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
