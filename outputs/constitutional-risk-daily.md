# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-07 12:25:57 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **8 / 100** (Baseline Institutional Noise)
- Previous day delta: **0.0**
- Delta vs 7-day average: **-6.1**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.56 | 3.09 |
| Judicial Independence and Rule of Law | 15 | 0.15 | 0.56 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 0.43 | 1.08 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 1 | 5 |
| Election Administration Capture | elections_transfer | 1.30 (Watch) | ai | 0 | 6 |
| Public Funds for Political Promotion | civil_liberties_information | 1.30 (Watch) | ai | 0 | 1 |
| Emergency Powers Expansion | executive_constraints | 1.00 (Watch) | ai | 3 | 0 |
| Election Certification Interference | elections_transfer | 0.95 (Watch) | keyword | 0 | 0 |
| Judicial Review Foreclosure | judiciary_rule_of_law | 0.60 (Green) | ai | 0 | 1 |

## Evidence Samples

### Legislative Bypass by Executive
- Assessment: Multiple credible sources report that the Supreme Court allowed Trump to implement parts of a mail-in voting executive order. This represents a shift of voting-rule authority from statutory/legislative control to unilateral executive action via EO. The Court's allowance (likely through stay or injunction ruling) enabled executive implementation without requiring legislative authorization. This is a real, confirmed action that transfers governance authority from statute to executive fiat, but is narrowly scoped to mail-voting procedures rather than a broader structural dismantling. Severity 2 reflects this as a real, credible stress signal of limited scope, not yet structural failure.
- [ABC News - Breaking News, Latest News and Videos] Supreme Court allows Trump to implement parts of his mail-in voting executive order - ABC News - Breaking News, Latest News and Videos (2026-11-06) - https://news.google.com/rss/articles/CBMigAFBVV95cUxQLUpWVmxZNkVNNGxlamhNRjkteVhjUVJNMXhDQ3Vyc3V3UkdTVEcyeUM0ZnEzTUlJQXRYMUZsNkZ5LTN5Q0VzWDFrVmVFSVlpOFBSaEpwa19qd0Q4SExzankxMEpIQjMxT2k5R0Z3emE0cDFCNng3V3lwVjBQUDg1NNIBhgFBVV95cUxOWGtmd1BpZ1U2QlJOeTZIcXhKMTVTOVFEZDJKcDJPS1NzX2NsOG1RT2w2TkpUMDkwTWY1QzlZcGt4LVlmNV9NZlFVUG04S0Y1U2hUSUdFSk5sUlFId1VsZzlnd1JvOGlWQnY2LThiN1J6cjZDSjdSWHd3elNWS3FpYWJqMXFnUQ?oc=5

### Election Administration Capture
- [The Texas Tribune] State-appointed managers in Texas takeover school districts brace for imminent removal - The Texas Tribune (2026-11-06) - https://news.google.com/rss/articles/CBMilwFBVV95cUxPbWo3aTBQVUFXRkVCcjhpLVZmamF4VkN5b05jTFBXQXhralRTdDI4cnFvUDBNMGM3WkFBbWpTclFjR2JYZURZdHB2UWpsOVo1Zm5xSDU1aDVnaGd4RTB1YWVkLVV2LXVpT0g1ZGJUeGVkNkpGeFRkMDYyZHFOYlR0aDJudWJxcDlBVG9WenRxeVNSWmJxb0tV?oc=5
- [ABC News - Breaking News, Latest News and Videos] FBI seizes 2020 ballots in Georgia in apparently unprecedented action, alarming local officials - ABC News - Breaking News, Latest News and Videos (2026-11-06) - https://news.google.com/rss/articles/CBMiqwFBVV95cUxNVE1NWTlMSlBNNkU3NzBTUmV6UEtIYV9EdUtfdFJ1dWdyendCdUk2Rk94ZW81Zkw0QWFEMml6aGdwcFg4TWZOMV9xelBCU1VJMXhpcHZlTHcyQlZjX3V0dUR2NWNtRGJvZVdNeW9Lbk1aM2hHVy1zNFotWG1HSFVGeksxWkoxOHVDQ1hTTUxFN0d1S2ZzbUZjVWpRMXB1S1VNRjQ0dHpMOWFWX0U?oc=5
- [13WHAM-TV] 'Deportations will continue': DHS shares reminder as Democrats set to take over Congress - 13WHAM-TV (2026-11-05) - https://news.google.com/rss/articles/CBMiwANBVV95cUxPbTdSeDYtb0ZON2NqRzBMdmJrSXZ6X216QzhtbXNWYmFNbEhRMHRndW5UOEZEdDVMeC1fVGtBaTNnTXQ5RW51WUllbzVtSVEtOHBUUnlqYnNrOFRyZkFvRHU0bTRGNjRieEE4c0xlYnBlQzdPbnFZdV92UWZmdWdwcllPNVg1MlRac1BLdkN5akxBUUxqMmJ5TENFczJmLUU2U1JnaV9TQWtOUzJSTXpXTnlpcHB5M1VmUF9Oamp3RzJuTjdtbXRETWJ5TjFWakc3MV9wUmUwNlJzUWZBWkgydDVoN3VkQTNBeDFQMURKUEdvU1k4aDZJZlRVUi1sMEhkNWNtcWk2SUdfY0ZmRjNGd3dNQ2ZjeUFGSk95NXdfWEpSTUdCaURHZ001d19od1ZVYlJxUVJIb0xnMkdxYjR4UE5PenVlRGphMmIxYzlXRFh4NmhoSzd0VFlaYzNlLUNiUmlqaDdkWEt0TmxDRWxTYi1icGd3THdtMHMtTUJlUnp5ZUtXdzZSUGh4ODVyTFRaejlTaHpPMVpkaGlWTVZIZWhaNzVNS0FZWVVkTWIzdXl6SWNwazJnQXJOclJYZDNS?oc=5

### Public Funds for Political Promotion
- [GLAAD] Trump Accountability Tracker - GLAAD (2026-11-05) - https://news.google.com/rss/articles/CBMiW0FVX3lxTE1DclMwQURIODFrXzE3cXFrS0IzOUFvdkFOVmRuX01SaFBMNk5rWHQ2TzlKN190V0xmR29YTnFuLV9KREZtTGdzQWYtUktvRHpkSllfbGkweEtsNUk?oc=5

### Emergency Powers Expansion
- Assessment: This is a continuation of an existing declared national emergency under the National Emergencies Act (NEA). Continuation of a previously declared emergency is a routine executive action that renews authorities already granted by Congress through the NEA framework. While the NEA does permit emergency powers to bypass ordinary rulemaking, continuation documents are ministerial renewals of standing authorizations, not new expansions. The underlying emergency was declared in an earlier year; this 2026 continuation represents ongoing use of existing delegated authority rather than a novel expansion. Severity is low because continuation is the ordinary operation of a congressionally-authorized framework, not a structural bypass of legislative process.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to the Threat From Securities Investments That Finance Certain Companies of the People's Republic of China (2026-11-05) - https://www.federalregister.gov/documents/2026/11/05/2026-22688/continuation-of-the-national-emergency-with-respect-to-the-threat-from-securities-investments-that
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to the Proliferation of Weapons of Mass Destruction (2026-11-05) - https://www.federalregister.gov/documents/2026/11/05/2026-22686/continuation-of-the-national-emergency-with-respect-to-the-proliferation-of-weapons-of-mass
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Iran (2026-11-05) - https://www.federalregister.gov/documents/2026/11/05/2026-22685/continuation-of-the-national-emergency-with-respect-to-iran

### Election Certification Interference
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 10 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 3
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
