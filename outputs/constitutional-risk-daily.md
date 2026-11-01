# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-01 12:25:10 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **19 / 100** (Elevated Strain)
- Previous day delta: **+4.0**
- Delta vs 7-day average: **-2.4**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 0.06 | 0.23 |
| Opposition Rights and Political Pluralism | 14 | 0.65 | 2.27 |
| Executive Constraints and Emergency Powers | 13 | 1.33 | 4.33 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 2.00 | 5.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.80 | 1.60 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 3.00 (Orange) | ai | 4 | 7 |
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 9 |
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 1 | 2 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 0 |
| Opposition Ballot Exclusion | opposition_pluralism | 1.65 (Watch) | ai | 0 | 2 |
| Legislative Oversight Obstruction | federalism_oversight | 1.60 (Watch) | keyword | 0 | 0 |
| Press Restrictions or Retaliation | civil_liberties_information | 0.95 (Watch) | ai | 0 | 1 |
| Court Order Noncompliance | judiciary_rule_of_law | 0.25 (Green) | ai | 0 | 1 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: LEADERSHIP Newspapers reports a US judge's order to halt taxpayer-funded ads promoting Trump. Another corroborating account of the judicial intervention against the unlawful government spending. The order itself is the serious action; severity 3 reflects confirmed court response to the breach.
- [LEADERSHIP Newspapers] US Judge Orders Trump To Halt Taxpayer-Funded TV Ads - LEADERSHIP Newspapers (2026-10-31) - https://news.google.com/rss/articles/CBMigAFBVV95cUxNX1NWcmIxbi0tSnJLc0JmSTdEdHFBeUcxVy1vM21NS3RpN0xXb3VFSHNKM2lJcXc3UGhJeHRBN29TSWxZcXJZVEc3WENfMUhGU0NlQ254b0s0dXVFMFk5aDBrUWlxNE93YmN2WUhDQ08xaTVmSjhlNHlZWFQ3MF9vMg?oc=5
- [Campaign Legal Center] Campaign Legal Center Action and Partners Successfully Halt President Trump’s Illegal Taxpayer-Funded Ads Scheme - Campaign Legal Center (2026-10-31) - https://news.google.com/rss/articles/CBMiuAFBVV95cUxNZHMzN002ZGhPbE53bUEtclpRaXRERjR6M2RWV3NvNmxxcXQyRW1mMFloclZaRHlQb1BneXdvZ0xRblZvSU5PdWRnQkI2ekVhbldlaHZFcmhjY1BjU1ZMWi1IWjROYXN0LS16dVN2enk0alJuclZEN1lTRkNpakNFRWpINjFyUVJ6NkhoMEtSYXJkSGp0Sl85X18yUFRjOGdPandMd24zUVpfZEhRemZ3MmhCWHMzUlBB?oc=5
- [ABC News - Breaking News, Latest News and Videos] Administration's pro-Trump TV ad is taxpayer-funded - ABC News - Breaking News, Latest News and Videos (2026-10-31) - https://news.google.com/rss/articles/CBMiqAFBVV95cUxNNEc3UWRPWjdaWkt2Wk9vcklvTkd3LUU0eEFHNnBTNGE1M01jZ1ZsczFwN0o1VjVmMk9rU3kxOUx5M1N2V1MtLVRqNjFfUXJYV0FQeFJSV3pBSEJ1Y2NFV29FMzFGLUxmVGVRa2tVVnhwM3hRYVhzSnFRM2YzUklyR3BjQm4xOUltenU0V2lRSHB2SzJlVmpMLV9lMHdGT2dJU3FBZG5FVVnSAa4BQVVfeXFMT2lPdUJtQ0JKMEs1aVhMMUFfOXFWRmxwZlBsSk9LYjFHX3pMamdNOUV6c1BNZnQwdGtVUzRTMS1IVzJoWjl4c3Z1elZtdWotY2MwazN5UzhQNGk1TGtnSGJhMzI3WUNlY3BlemEzWGlNMkpGNnFjNXZiZU1vQVZ3SFRPYklhZjN1ek4wWUN3ZUt4YUxMcDJpTmhGMjhaVkg4Wm0tMm9CbERyWnVENjNB?oc=5

### Election Administration Capture
- Assessment: A judge ordering the Trump administration to cease threats to prosecute election officials is a confirmed judicial action (real event). It indicates the administration was threatening election officials with prosecution, which constitutes an attempt to exert partisan control over election administration through intimidation. However, severity is 2 (confirmed stress signal, contained action) rather than 3 because the threat was ordered to cease by a court, showing the judicial system is functioning to restrain the overreach. No structural failure has occurred.
- [The Straits Times] US judge orders Trump administration to cease threats to prosecute election officials - The Straits Times (2026-10-31) - https://news.google.com/rss/articles/CBMiywFBVV95cUxQZWhGTEh0aG9URXJJS2dYTHVQRXVVMnVXN2hXSzM3RkZPRUpXbnVTTDF6SUtQWUZFWWZkekVOTkgyd1NuV1dya1BGRUotQ09OaXNYaTROc0p6NVFjZGUwQVM2blFzcGRuQ0xNR1REM2w1N3RQQmJWV1cxRkRXY1V5cHR4OUFjRnRlUVh5MjE4VnQzMjU4eGNONFBJalY2NHplWF9HYTNDSjE3MEthU3hoTFU5R0F5UzJCMDdlM29teXBfdU43VGFlSndhbw?oc=5

### Legislative Bypass by Executive
- Assessment: Multiple credible sources report that the Supreme Court allowed Trump to implement parts of a mail-in voting executive order. This represents a shift of voting-rule authority from statutory/legislative control to unilateral executive action via EO. The Court's allowance (likely through stay or injunction ruling) enabled executive implementation without requiring legislative authorization. This is a real, confirmed action that transfers governance authority from statute to executive fiat, but is narrowly scoped to mail-voting procedures rather than a broader structural dismantling. Severity 2 reflects this as a real, credible stress signal of limited scope, not yet structural failure.
- [ABC News - Breaking News, Latest News and Videos] Supreme Court allows Trump to implement parts of his mail-in voting executive order - ABC News - Breaking News, Latest News and Videos (2026-11-01) - https://news.google.com/rss/articles/CBMigAFBVV95cUxQLUpWVmxZNkVNNGxlamhNRjkteVhjUVJNMXhDQ3Vyc3V3UkdTVEcyeUM0ZnEzTUlJQXRYMUZsNkZ5LTN5Q0VzWDFrVmVFSVlpOFBSaEpwa19qd0Q4SExzankxMEpIQjMxT2k5R0Z3emE0cDFCNng3V3lwVjBQUDg1NNIBhgFBVV95cUxOWGtmd1BpZ1U2QlJOeTZIcXhKMTVTOVFEZDJKcDJPS1NzX2NsOG1RT2w2TkpUMDkwTWY1QzlZcGt4LVlmNV9NZlFVUG04S0Y1U2hUSUdFSk5sUlFId1VsZzlnd1JvOGlWQnY2LThiN1J6cjZDSjdSWHd3elNWS3FpYWJqMXFnUQ?oc=5

### Emergency Powers Expansion
- Assessment: A Presidential Determination under Section 303 of the Defense Production Act of 1950 is a lawful exercise of delegated emergency authority that does invoke statutory emergency powers to direct economic activity. Section 303 authorizes the President to require priority allocation and controlled distribution of materials. This is a real occurrence of emergency-powers invocation, documented in the Federal Register. However, it represents authorized use of congressionally-delegated wartime/emergency authority rather than an unconstitutional bypass of the legislative process. The DPA itself is a statutory grant of emergency authority enacted by Congress, so its invocation is use of authority granted in advance, not a constitutional circumvention. Severity is 2 (a real but contained, legally-authorized action) rather than 3+, as this is neither an extralegal assertion of power nor a defiance of constitutional constraint.
- [federalregister.gov] **[official record]** Presidential Determination Pursuant to Section 303 of the Defense Production Act of 1950, as Amended, on Domestic Petroleum Production, Refining, and Logistics Capacity (2026-10-28) - https://www.federalregister.gov/documents/2026/10/28/2026-22052/presidential-determination-pursuant-to-section-303-of-the-defense-production-act-of-1950-as-amended

### Opposition Ballot Exclusion
- [PhillyBurbs] Fitzpatrick sues to keep Democrat Marseglia off elex board, cites bias - PhillyBurbs (2026-10-30) - https://news.google.com/rss/articles/CBMijAJBVV95cUxOM3ZKZ3ZJN2MzUEU4cGU5VGJ3b3hnTElfdGJLd1IzQmZfZkw4QUI0SV93QjRGamh2SmZKMHVWMWpfamNfMWpwZ0R6SW52alZ0SGwwOGtsSUNMVW1BZ3ZDcjhWZlBNZHloZU9SZlVkbDJYakFKcklQNTdXa2VVWDcwaHBlVVVNeDVlOVMtNU5zVUJyTVVjSnJzUXBvNFg2b1BCT3FjM1c2S3dzb1l2WVdud3VXcTBmbDBXU2F0dk9yYi1mOWtmOGxGUGxxa3Z4V0VsU3I1NFBoOWUyb1dVaVlIS2plem5ab29HU09UTjZTSGotNEFqRjdRYmlvWVVNZFFYU0U5UnVWWmRhSnVT?oc=5
- [IOL] Court rules Mbalula unlawfully removed Lungisa from ANC election list - IOL (2026-11-01) - https://news.google.com/rss/articles/CBMivgFBVV95cUxPSm1WM1JYdWlUYWRzRklDbnByYi0tZmlBSmFsN2tHaWRWVDViN3hnVmpJRS1zVEstUy1POC1sRzBlZV9wU0ZzX1o2RlBXOEJSUll5cDZwV0xDRzVIaVVrN2M0MFJkVXBkajZTQjU1YW1aS3plakl0dG5aWjBpVHRUbG5FSDdONlg0LVpJWVdJZXBWSlFnU3k0RmZKRnl4cGZ1Zkk2LXZpQ0VZYkpzV0lGeUtlWU1YUHgxeVRTdmJB?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 9 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 1
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
