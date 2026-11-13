# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-13 12:28:17 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **14 / 100** (Baseline Institutional Noise)
- Previous day delta: **-1.0**
- Delta vs 7-day average: **+0.4**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 2.00 | 11.00 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.42 | 1.35 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 0.52 | 1.29 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 3.00 (Orange) | ai | 1 | 4 |
| Press Restrictions or Retaliation | civil_liberties_information | 0.95 (Watch) | keyword | 0 | 0 |
| Emergency Powers Expansion | executive_constraints | 0.65 (Green) | keyword | 0 | 0 |
| Legislative Bypass by Executive | executive_constraints | 0.60 (Green) | ai | 0 | 2 |
| Public Funds for Political Promotion | civil_liberties_information | 0.60 (Green) | keyword | 0 | 0 |

## Evidence Samples

### Election Administration Capture
- Assessment: Trump directing the Department of Justice to sue to block Senate election results based on partisan outcome represents a direct attempt to use federal executive power to overturn or invalidate election administration and results. This is a verifiable action (Trump directing DOJ) to subordinate election administration to partisan control by invoking federal litigation authority over state electoral outcomes. This constitutes serious, confirmed action to capture election administration through executive branch pressure on the DOJ to intervene in state elections on behalf of a political party.
- [ABC News - Breaking News, Latest News and Videos] Trump told DOJ to sue to block Alaska Senate results if Republican narrowly loses - ABC News - Breaking News, Latest News and Videos (2026-11-12) - https://news.google.com/rss/articles/CBMipAFBVV95cUxQekhpNnRhMmk3WnMteVlLeVRYT2ZMUGRnRkJmSlJxUU9TUm1GN1ZEYWp5SFRqS20tSWVtQWpUMF9VaWd3U1FFRUd1TDRBMk9UTXhpMkhHTlE4NnQzZDEyRjUxQ3lkYlVkZHAxTS05MjJkbDA2VXFNQVBhcGdmUVJ3LTRHTjBScTBucno5Y0NhazNCeWdiLWpJMUlTRjF2Uk5zRzE2SNIBqgFBVV95cUxQUEZqTzdWbGhCLTVzd1J1VlI1cUxOOWFyLXZIbDI0TnA1YXlWQXgyMTFtaXRMdE9jbTIzTXdkUmpXMzJkejdKeHlXc2lHYWVJd2t3WFVVTmNwS05BT2wzTjhkeW0tZ3FpU0Z5aUxmOFFCMWNydkk1S3hPT09xT2w1WWdjdG5ybXRhWl9FZV84TG5kOWM0YkZwNVVYWU9keUFfZWF1ZVIwRUs3UQ?oc=5

### Press Restrictions or Retaliation
- No fresh evidence links in the current lookback window.
### Emergency Powers Expansion
- No fresh evidence links in the current lookback window.
### Legislative Bypass by Executive
- [Daily Excelsior] 2026 US Congress Midterm: Power, Policy and Global Impact - Daily Excelsior (2026-11-11) - https://news.google.com/rss/articles/CBMilAFBVV95cUxOMUhfd0dpNjdjeVpHUjRlV3RVRl9LM1BzQmU2QkFGUGRKNFMwWEc0enJTSEdxdHNNS0REaXZFN3hDNWRXbjRKSmhCU2VDRnlKa0xKSndZZHJEdXhmYXVkMlQ3ZjhKaFlqUzVwUHNQZ0NFQ29iTEswajlDRjBzdG9tcVJtU2lBWTdMN2dNMmNtS001Rjdj0gGUAUFVX3lxTE4xSF93R2k2N2N5WkdSNGVXdFVGX0szUHNCZTZCQUZQZEo0UzBYRzR6clNIR3F0c01LRERpdkU3eEM1ZFduNEpKaEJTZUNGeUprTEpKd1lkckR1eGZhdWQyVDdmOEpoWWpTNXBQc1BnQ0VDb2JMSzBqOUNGMHN0b21xUm1TaUFZN0w3Z00yY21LTTVGN2M?oc=5
- [TheNigeriaLawyer] “Internal Democracy Is Not A Slogan” — Court Voids Mark, Aregbesola’s ADC Leadership, Says INEC Monitoring Isn’t Election — Download Judgment - TheNigeriaLawyer (2026-11-11) - https://news.google.com/rss/articles/CBMi8wFBVV95cUxQUjRrMExFbDczQVVNVXVHVmRCcy04dGFCcE0yUEhCRGdPZ1NTMDFZQWxFMFNTRklDX1Jfb0EwZldUWFplUm5HOHJXRkd2dkVBbTRzTFRySldRMWdaeC13SlhvQmhYbEhEYnBrSVVUVHk3UWVNWUItYzEtSFR6TU4tbzFtVl9namNYUGdCUV83bXFqa2JKY2ZWUUYzVkY4SDNjR2M0OEs2WjR2YmRoZmtRUnZnNDdxcHdtcEtPem1ZZnpBV3ZacmNmeHF2NTJFQmdxbFhiOTAydlR1bGRLUk9hTFBjRFRuOUwyUkZGVjV5dDJMNzQ?oc=5

### Public Funds for Political Promotion
- No fresh evidence links in the current lookback window.
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
