# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-14 12:25:18 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **10 / 100** (Baseline Institutional Noise)
- Previous day delta: **-4.0**
- Delta vs 7-day average: **-3.2**

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
| Executive Constraints and Emergency Powers | 13 | 0.18 | 0.60 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 0.28 | 0.71 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 2.65 (Yellow) | ai | 0 | 6 |
| Press Restrictions or Retaliation | civil_liberties_information | 0.60 (Green) | ai | 0 | 3 |
| Emergency Powers Expansion | executive_constraints | 0.30 (Green) | ai | 0 | 1 |
| Legislative Bypass by Executive | executive_constraints | 0.25 (Green) | ai | 0 | 1 |
| Public Funds for Political Promotion | civil_liberties_information | 0.25 (Green) | ai | 0 | 1 |

## Evidence Samples

### Election Administration Capture
- [Time Magazine] How Texas’ Blue Takeover Could Soon Begin Impacting Texans’ Lives - Time Magazine (2026-11-13) - https://news.google.com/rss/articles/CBMikAFBVV95cUxOYThZS05mY3BlV0FoN25TUEtCYU5JLTFsbjJBYW5GVUJHT2pzTjJnaEdFSE5aSHBqSW5XTWlWVF83dmp2dFBqSHlUOGd1a0VsTFN4Y2JURnRBN0Ita09xUGFnSElIbC1KVHY0M2gtd1NtLXRXMmJsdjQ3TzVqZkgzazM0Z2pNUFVxVEN0eUwzQy0?oc=5
- [AP News] 2026 U.S. House Election Results - AP News (2026-11-13) - https://news.google.com/rss/articles/CBMibEFVX3lxTFBUM0VmeFZ2SjF1RGJlVENLazFvbHZxWjRIYUlNMFlKal9sRW1ySS1UQWo4djh3cWpLcXJLWWFuWXBmdkllMTd2aVRhWF9YZFM5ZGRmN3pxZW5nWERXMjREbTVDeGF2RXRfM3ZTUw?oc=5
- [Hawaii News Now] Testifiers call for elections chief’s ouster as commission meets after court order - Hawaii News Now (2026-11-13) - https://news.google.com/rss/articles/CBMivwFBVV95cUxOTEY4am5GUXZjUXJtX282TlBBOWF0V01qZS1kZzJWMkdYbnlPUG9EenpEREdtLU84czlvYk9HcktBX09ncVNRSU1rcDhZR2NpRExNenBiRVB6YVhNOURFUkxMbEdZLTB6OWpqai0yWDhWWlFpR3RBWEY2Ymtsakdpd3gycHl3TDQ4bGJpQjJlaHNWTlNxRUlIZ05OTDVNdUJEekpmZlZoVnNtUWRteDRyMndfZTRqMGpMVHY3OG5BVQ?oc=5

### Press Restrictions or Retaliation
- [Afghanistan International] US Must Free Afghan Journalist Facing Deportation, Says CPJ - Afghanistan International (2026-11-14) - https://news.google.com/rss/articles/CBMiT0FVX3lxTFBGQ3hkQ0FlaUtScTZJaFNIWjBqT3A5THZ3Yjc0Q1BWWFpZTlA1Q3g0VDg3WkRtMTJ0aEp1TVRKdXBuR2tzeE8xalp0WEdOajQ?oc=5
- [The New Republic] MAGA Propagandist Paid by Russian Government Shows Up at Mar-a-Lago - The New Republic (2026-11-13) - https://news.google.com/rss/articles/CBMiTkFVX3lxTE8xbTZfVUxGSkREWEpuaFFIcXIyaHhqM1FGRkllWk1fTmJOWTd0RjVNUzFEcGJ0QjlaR1hYVXg5V2hIQWY3YllJNXI0N0gtUQ?oc=5
- [Nepalnews.com] Opposition closes ranks as questions mount over PM Balen government’s performance - Nepalnews.com (2026-11-13) - https://news.google.com/rss/articles/CBMiXEFVX3lxTE5UUlVSTFVsOUdkQmF5VWJMbmtUcnJGUTQzVUwwekNEc2pKYVR5TmdXamd4cDRTWndfaE1JVU1QcGtncUtVY29DV3B4VjNweVhBQzUwVnExVk1hNjVu?oc=5

### Emergency Powers Expansion
- [The Federalist] How Stephen Miller Can Bypass A Democratic Congress For The Next Two Years - The Federalist (2026-11-13) - https://news.google.com/rss/articles/CBMikwFBVV95cUxQMzNIOWk2czFqVmtyVEpROFpFODJHZkVKX282WGk4OVdmTUhnZUoteG1yNkRtcFl2aGF5ZlM2TjhPT3k4dWcwaG91N1dhWlJsUVNuenBHdmpZaU9yVTFWNUNCcDVLV1QyNk9QQVF5WEpaSTF2NXJ2TVpybVpsekU0UWJqWDdRYVJKZ1piYmIwbWplY1E?oc=5

### Legislative Bypass by Executive
- [SCOTUSblog] The major Trump cases that might come back to SCOTUS - SCOTUSblog (2026-11-13) - https://news.google.com/rss/articles/CBMilgFBVV95cUxNclo1WEt4alpQNG9ocVZiS0VTVWdneG5hTXpmYS1CRUlWR3RraTdlWnJCaGxSYy1KcmhBWDNnNl9aYk0yQ1Y2M01MWWVPZldWb01JQVJBU0lSSU81RE1sdzZaXy1SSUc3OXNORUVNUU1QSUwwdkZmdlZzWlN5c09YWVlLVEI1X0JnTUYzY3ZLNG9kYzJIdmc?oc=5

### Public Funds for Political Promotion
- [Mises Institute] Three Free-Market Ways to Limit Immigration - Mises Institute (2026-11-14) - https://news.google.com/rss/articles/CBMieEFVX3lxTE5BN19fMm9UbUdkVVBDQWdHbFlPeUFFTzFxaEFDZFhXTHFybzV2XzUtMlZLREVFYnZPcS1ENGJKeWhJWmhabzdwMFZGQ0xiWDV3NEpqOFBWLWRCWml5cTdCcjl6dDlBUmlaTEMtY18yUnJheHM3eVBpVA?oc=5

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
