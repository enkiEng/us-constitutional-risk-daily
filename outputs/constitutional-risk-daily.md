# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-29 12:45:21 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **7 / 100** (Baseline Institutional Noise)
- Previous day delta: **+1.0**
- Delta vs 7-day average: **-5.0**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.15 | 0.82 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.08 | 0.29 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 0.15 | 0.38 |
| Civil Liberties and Information Environment | 10 | 1.00 | 2.50 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.12 | 0.25 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 12 | 39 |
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 1 | 3 |
| Martial Law or Military Governance Language | executive_constraints | 0.95 (Watch) | ai | 0 | 3 |
| Election Administration Capture | elections_transfer | 0.60 (Green) | ai | 0 | 1 |
| Statistical Agency Integrity | civil_service_integrity | 0.60 (Green) | ai | 0 | 0 |
| Opposition Ballot Exclusion | opposition_pluralism | 0.25 (Green) | ai | 0 | 3 |
| Legislative Oversight Obstruction | federalism_oversight | 0.25 (Green) | keyword | 0 | 0 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: Multiple credible news sources (NYT, NBC, CNN, Reuters, Fortune, etc.) confirm that the White House released taxpayer-funded advertisements featuring Trump's messaging describing a 'final battle.' The ads are described as government-funded and characterized as campaign-style messaging. This represents a real occurrence of public funds being spent on communications that promote the officeholder. However, severity is capped at 2 because: (1) this is a repeated but still-recent action under active scrutiny, not yet adjudicated as definitively violating the statutory prohibition; (2) no official document (court ruling, GAO decision, OLC opinion) has yet issued an instrument that changes legal positions; (3) the event is confirmed but the appropriation source and legal standing remain contested/unclear in the press reporting. If GAO or a court were to issue a binding determination, severity would rise.
- [The New York Times] Trump’s 2024 ‘Final Battle’ Ad Returns, Funded by Public Money - The New York Times (2026-09-27) - https://news.google.com/rss/articles/CBMihwFBVV95cUxQOXlqZWszQVhSYThHc0xrc1FNTGh4dmh6ZkllWmNWdUVkdk9xZjdRTDg3cnFyckQyYnpLMEh4NjVKMGlhN3pxZUpKQWNuRF9Cd1A3ZzRPUlJtQ3ptREZGWjNWblczSE8xVHQyU09Edm0tYUptYW9JSTVjWnVWOTdicDlCUEZrV2M?oc=5
- [NBC News] White House releases new taxpayer-funded ad describing ‘final battle’ - NBC News (2026-09-28) - https://news.google.com/rss/articles/CBMizAFBVV95cUxOVHQxTkktREdFVVhkVHppbzBoaUlPcWJwVGN2eENtNEtzLUlIM3FzM1l4SE8zM2R0elR4bWoxVzVtSDRrcDNnTGpuOHA2eHpyVUplRUFvZTMzLVkyeUxRdVFJZDlMMFRVVG5HN1lDdWpWWnFVTHNXam54YU5ONUFEb1d3UGxoQ19Yc21KMFhEMVlGUlZEbVN4WnoxVHlINjhtVzZVa2VHUXBHY1hTWFNjWFl3VTl6RkFWZGxNbHpOYlo1eFRYLUp2Rmd6MGo?oc=5
- [Poynter] Trump’s taxpayer-funded ads look like campaign spots. Are they legal? - Poynter (2026-09-29) - https://news.google.com/rss/articles/CBMihgFBVV95cUxOR2Z1RUZRNXVKMXJ5T2IxbzJoWjV6NFc4S2JIRW5na0pYQmpmWmJvYkRYelhjRWdta1VwbjEwUG5MOEl0dkF1N2dscTM3eURMNWtsQkZYVVlvODNmYmZEczRHZUw0bVA2cXlISXZfMFZ6MDVlaXRPaXd4cHhzMmw4Y1ZoT24zQQ?oc=5

### Legislative Bypass by Executive
- Assessment: Trump is seeking to cancel $810M in congressionally approved domestic programs. This represents an attempt to bypass legislative appropriations through executive action. However, a 'seek' or proposal to cancel is not yet an accomplished action that shifts governance from statute to unilateral executive action—it requires either successful execution or an official directive that removes the funds without further congressional action. The framing as a seek/proposal places this at the boundary between proposal and action. Without confirmation of actual execution or an official impoundment/rescission order, this is a credible but not yet fully materialized stress signal. Scored conservatively as severity 2 (repeated or credible stress signal of a real but contained action) rather than 3, pending evidence of actual implementation.
- [The Well News] Trump Seeks to Cancel $810M Congress Approved for Domestic Programs - The Well News (2026-09-28) - https://news.google.com/rss/articles/CBMirwFBVV95cUxON0JQSmZZaGJrWmlEaGdENUhhRnJoSEVSVDJBSTVRMHR5ZTZGa3otVXk0NXJhZlFlTmg4ZjdXUTNRWjdJQVRXOU52dXMxMkNRN3ZJeUdldWZleG5YVFhQcU5aS0dpdW9QN2p1S2YwaU5EbmdBaGFYWDFKM2U3S3BGd29hQXl4dmlQV2ZaUFZyclM0cE5DQWVFYUw5dkxXemJINnl4TUZ0YXNQdzZrMERB?oc=5

### Martial Law or Military Governance Language
- [10News.com] California Supreme Court orders Riverside County sheriff to return 650,000 seized ballots - 10News.com (2026-09-27) - https://news.google.com/rss/articles/CBMiuAFBVV95cUxQRll5ZncxNGd1MHFFelZUUFdmVzQtR245WDZ2Y2hpMjJwOXpDRjF0dEctcGtMU1o4eE4xbXE1Z1phWTNZQ0NibXA1ODlfczEwTFRiTk5EOVhuNWlUb0ktd3VOS3dKMjR2LU5zaHpJSF9ZSXpIWl9NSjRHb2xCVW9wQ21BTmtvWEh0dTRJYm12TmR4emtVeWhVNi02Umk3QTBtN3NraXV1cUhrMFdTUV8tcTZ4cnpSOFo3?oc=5
- [sud.ua] Two vacant seats in the High Council of Justice under the advocacy quota and four years without a Congress: the court will check whether the National Bar Association lawfully postponed its holding - sud.ua (2026-09-27) - https://news.google.com/rss/articles/CBMiggJBVV95cUxOaTJIM3BraEIwT3FRazYyU2lHVS04bEplOHItLXJlbHpzX1RlM19vZ182NXpQZXcwUENtcmdzUGtxSGxMMHpVbVVQMlRxd2FkejlqdklrbFRfUFhpVjVTVjhyOVNnZThfd3FjaEt6cUlHak5ZcmRMZlRSRnBiU1Z1QmN2X0lpZGktMll1anJZamJGdmk2cVlBeGp4aUo3R3c3c1hoNTU3TUhfZjZLT1ZsQnpZTWF4cWd3Sk9oQnVwcWh5ZVdWUUhhckNCcDBQXzMweG5JYXBmbVhqWklkRDg5ajctVjdpa2lhU3BlM0hzWDZLOXkxRVJzSUEtTUdpYVFnN2c?oc=5
- [India Today] Delhi Women Safety in Spotlight as Supreme Court Flags Law Enforcement Failures - India Today - India Today (2026-09-28) - https://news.google.com/rss/articles/CBMi2AFBVV95cUxNRzhNTkdxYk9QQU9ZQmJ1UWdHaTBSRFRlY2hnVEprenJvenNMbl9KSmNydV95LWRYTjBlR2RLQUNzdVpDWFd4TVE2djZvcEtrMklzSWpjVElkVTNvb2xHVEt4Y0VwSzhjMWxPWXdPT2djM1JHdFhaZk9XUkc1QmNCcm9wZVBoT1RqRmFsSmo0dlMyU0djdjQxZkdqb2FoZnVUNmxxZXdQZUFtMlRDeTd2cnQzWHVCaWFObFlUUEhNQmgxbm5TQkJtWXM3WG5JMWlaU0Q0UW5tZljSAd4BQVVfeXFMTTU4V0dkZWh4QWtWTGZZWHY4OGdyUjg0NVdvNVhMbGF0LVRiV0RmUkpna3BrbVhfNC1JamdxdlI5LUU1NlpQeC1RXzhHbWFCSHV3TjlBbjhPRVJIUDEwSFNJVVhGc3NCVGxzOXVKZWlEem9BdG5tb2VGWkxCeThrZjF4SmxiaGFhWnBuU2Z5c2x0RzNEdWFqQjdGWUcyb3Z2VlZxZU53UDkxOVhhQjBFaHFXMUJ1MXBWWVB4VnlxMGlPSi1kUExDNG5Eb0pPTHRSUnZodEhiVGoyZjBPUXhR?oc=5

### Election Administration Capture
- [streamlinefeed.co.ke] Hegseth Orders Cyber Agencies to Defend Midterms - streamlinefeed.co.ke (2026-09-29) - https://news.google.com/rss/articles/CBMikAFBVV95cUxOa3o4eFJIWW1lY3NvdTJNenk5OVRaLWM1aEJlZDFGdGszYjZmQ2NpcncxUy1kXzktX050cUlHSm95VC1qaE1KQlctUE5NZ0JHSzZENXRSTEJOSnVFRjNvTGRsVThzQmFSdVBPUzd2azZMMHd0M1BHMjRsQl9YeDluV2V6SHUwMWpxQmlHRVRMMjY?oc=5

### Statistical Agency Integrity
- [federalregister.gov] **[official record]** Notice of Adjustment of Disaster Grant Amounts (2026-09-29) - https://www.federalregister.gov/documents/2026/09/29/2026-19898/notice-of-adjustment-of-disaster-grant-amounts
- [federalregister.gov] **[official record]** Notice of Adjustment of Minimum Project Worksheet Amount (2026-09-29) - https://www.federalregister.gov/documents/2026/09/29/2026-19859/notice-of-adjustment-of-minimum-project-worksheet-amount
- [federalregister.gov] **[official record]** Notice of Adjustment of Countywide Per Capita Impact Indicator (2026-09-29) - https://www.federalregister.gov/documents/2026/09/29/2026-19858/notice-of-adjustment-of-countywide-per-capita-impact-indicator

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 12 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **High**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
