# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-17 12:28:36 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **17 / 100** (Elevated Strain)
- Previous day delta: **+10.0**
- Delta vs 7-day average: **+5.1**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 2.00 | 11.00 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.10 | 2.75 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 3.00 (Orange) | ai | 2 | 7 |
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 2 | 3 |
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 1 | 3 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.30 (Watch) | ai | 0 | 2 |

## Evidence Samples

### Election Administration Capture
- Assessment: Trump directing the Department of Justice to sue to block Senate election results based on partisan outcome represents a direct attempt to use federal executive power to overturn or invalidate election administration and results. This is a verifiable action (Trump directing DOJ) to subordinate election administration to partisan control by invoking federal litigation authority over state electoral outcomes. This constitutes serious, confirmed action to capture election administration through executive branch pressure on the DOJ to intervene in state elections on behalf of a political party.
- [ABC News - Breaking News, Latest News and Videos] Trump told DOJ to sue to block Alaska Senate results if Republican narrowly loses - ABC News - Breaking News, Latest News and Videos (2026-11-16) - https://news.google.com/rss/articles/CBMipAFBVV95cUxQekhpNnRhMmk3WnMteVlLeVRYT2ZMUGRnRkJmSlJxUU9TUm1GN1ZEYWp5SFRqS20tSWVtQWpUMF9VaWd3U1FFRUd1TDRBMk9UTXhpMkhHTlE4NnQzZDEyRjUxQ3lkYlVkZHAxTS05MjJkbDA2VXFNQVBhcGdmUVJ3LTRHTjBScTBucno5Y0NhazNCeWdiLWpJMUlTRjF2Uk5zRzE2SNIBqgFBVV95cUxQUEZqTzdWbGhCLTVzd1J1VlI1cUxOOWFyLXZIbDI0TnA1YXlWQXgyMTFtaXRMdE9jbTIzTXdkUmpXMzJkejdKeHlXc2lHYWVJd2t3WFVVTmNwS05BT2wzTjhkeW0tZ3FpU0Z5aUxmOFFCMWNydkk1S3hPT09xT2w1WWdjdG5ybXRhWl9FZV84TG5kOWM0YkZwNVVYWU9keUFfZWF1ZVIwRUs3UQ?oc=5
- [ABC News - Breaking News, Latest News and Videos] Trump director of election security sparked Georgia office raid, affidavit says - ABC News - Breaking News, Latest News and Videos (2026-11-16) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5

### Public Funds for Political Promotion
- Assessment: News report confirming that an administration aired TV advertisements promoting the officeholder using taxpayer funds. This constitutes spending of appropriated public money on communications that promote the officeholder rather than serve a public-information purpose, which directly matches the signal definition. The report itself treats this as a real occurrence (not hypothetical, opinion, or allegation), though the severity is moderate because this appears to be a discrete action that has been detected and is now subject to public scrutiny and potential legal challenge. No court order has been defied, no structural constitutional breakdown has occurred, but the alleged violation of the 1950s appropriations prohibition on 'publicity or propaganda purposes' is material.
- [ABC News - Breaking News, Latest News and Videos] Administration's pro-Trump TV ad is taxpayer-funded - ABC News - Breaking News, Latest News and Videos (2026-11-16) - https://news.google.com/rss/articles/CBMiqAFBVV95cUxNNEc3UWRPWjdaWkt2Wk9vcklvTkd3LUU0eEFHNnBTNGE1M01jZ1ZsczFwN0o1VjVmMk9rU3kxOUx5M1N2V1MtLVRqNjFfUXJYV0FQeFJSV3pBSEJ1Y2NFV29FMzFGLUxmVGVRa2tVVnhwM3hRYVhzSnFRM2YzUklyR3BjQm4xOUltenU0V2lRSHB2SzJlVmpMLV9lMHdGT2dJU3FBZG5FVVnSAa4BQVVfeXFMT2lPdUJtQ0JKMEs1aVhMMUFfOXFWRmxwZlBsSk9LYjFHX3pMamdNOUV6c1BNZnQwdGtVUzRTMS1IVzJoWjl4c3Z1elZtdWotY2MwazN5UzhQNGk1TGtnSGJhMzI3WUNlY3BlemEzWGlNMkpGNnFjNXZiZU1vQVZ3SFRPYklhZjN1ek4wWUN3ZUt4YUxMcDJpTmhGMjhaVkg4Wm0tMm9CbERyWnVENjNB?oc=5
- [ABC13 Houston] Trump defends spending millions on taxpayer-funded promotional ads: 'For the country' - ABC13 Houston (2026-11-16) - https://news.google.com/rss/articles/CBMihApBVV95cUxPWGRtcXUwS2thOG1zOVhVRnVVTThWWmxUWXBlUjNqdTNobGlyZjBvM2NZd2xSRWE5ZlVlMlVfd3VnTlk3dVZwajVLTFlMRjI2SjlNSHpSWTdldzJYUXhiZmhULTYxYW9NeTVod2U5RTdiSHRieGhUbEdoczFmdUM3RWNjOWF3eTNCUEVLcnJUdVZ3b0FsQUgxTTRoWWI1LWszWXlPTDhRdGdLY013Um9pQV9uQVV6RVpaajhGMjJhVTIxS0Z4RTdhUEFYOU5aNDhtcnpOYnhFZG9FWFNnc0V5UmZRelFZQUhEZGx3ZXp4T1NyeEhhVVNLQ1MzZnB5MUFCNkpYVlRrTFU5c2dRTkhtRXpOdi1JN1MzaUZRV1paRENWTnBLMGhDell4WDlkcFI3SG85VmlsNkdLSVRRUkRlb21ydkZiQlR5eFU1Y3hrZ1FrcTdaQVpDcDZXSloyelF1SzFKT1FDYllHYlRQOEtaMjYzdnlIOF9saHpkdEFySG5ySTFKQnR1MWRmdXRRakVocmdGX25BX2E5MFBwQ0cwQ2VFcTBLSjJ2SU9ZX0FINTZYRWNXNUoxdG5Od3hhX1lkRGVBZGJZSHM5RE8yXzF3MkRnamlGbkctaVhQWEVTY2RqeDllSkgxWVBRTzdvZ0c5MlAxbUhFMzJ6ckxXeTA3c3FfeHhoVUl5ZnBXamhhUnIySEtpaGRqZElPbnJST2h0UmxFRFFSN2MycU1XeUdkUWFtZGF4ZXV5SkVrWmVhbDBiSV9Tc0F2S0JqMzNlSnJSUlJOWVBtd0lTaWZtN182RDJhcGkxem5pZWJ3SGl3SWdZRXJFYnFiVWhEemVoZW9QX3ZFZ01NUUtvSW5VNkkwWGNvQWQzMVhpTjF5YU51Y2N2bjhDb01paDJQU2tqeC13RDUxLVRWN3A4RVU3bjc3cThfVkhfaV81SUxyWml2emJmaTV0UnBKS3pXLV94WDNlWk5vM0ZxNGd2RGZDY1V1dlBwUzJTcTdoNV9Mdzl4c0N1QnQ5NDg2U0NrZllidW5aeE5NS0tYaUZhSDRDam91VFVFZXJYTUFiN2VoM2Q3OXNOaTBHYjk2aEloTzJXWW5iZVIwNFRaS01aZW5JczZNY2ZjVnpjNGJEa2x6S0tIWVZqN0ctUmJqX2tuT2JYTjlDQjJ1c0xPT2FOQnVDY3lvQ2JQcEhDMmVMc05xeGhWSkl3aFhsOUNHQ0tBcERLMkxmVzBOWlVYLXVuR2tJeHdFTzFHYV9McTltNlpPbXlRWkhTTjdjMGVFejZpYW1TYmU5Z2syZXpvTWNzcmlYT1oxeDB0eV9HNHJyWFJQa1IyRnlGWHRyeFhTLWRKbHdkaTRTS19NbC1QQnVsVi1BNk50Q3RaMVp0X3ZqQXhVbmdrMDBTa2dNd1EwUXB0Y2hrMFo0UG8yWEVHNlBNLUJ5b1NfdUZUTDZ1VWhwbGhQMzJDeXhEcW8xd3JqMWc3d2ZmZVl6UG5KYzdjdXp0bWt6VFp2TlZvaXR1UUc4Q0JvcWx6eVp1SVp0VHZpOHI0Y0VUQ1FYY2pKZXhPeXRzb1p5WVNkTXpaOG4tOENKY2NLYjVwTTNWcDFjNVRmQ3R3X1d5MW14b1NrRmQ4YWllYmgwOTFTZnVzdkFCN0t4dzR1UTVQaGp3SG1TLVltdjBsb2VBYlZjRkZka3RjSFNVdEZvNjQ2N053aF8?oc=5

### Legislative Bypass by Executive
- Assessment: Multiple credible sources report that the Supreme Court allowed Trump to implement parts of a mail-in voting executive order. This represents a shift of voting-rule authority from statutory/legislative control to unilateral executive action via EO. The Court's allowance (likely through stay or injunction ruling) enabled executive implementation without requiring legislative authorization. This is a real, confirmed action that transfers governance authority from statute to executive fiat, but is narrowly scoped to mail-voting procedures rather than a broader structural dismantling. Severity 2 reflects this as a real, credible stress signal of limited scope, not yet structural failure.
- [ABC News - Breaking News, Latest News and Videos] Supreme Court allows Trump to implement parts of his mail-in voting executive order - ABC News - Breaking News, Latest News and Videos (2026-11-16) - https://news.google.com/rss/articles/CBMigAFBVV95cUxQLUpWVmxZNkVNNGxlamhNRjkteVhjUVJNMXhDQ3Vyc3V3UkdTVEcyeUM0ZnEzTUlJQXRYMUZsNkZ5LTN5Q0VzWDFrVmVFSVlpOFBSaEpwa19qd0Q4SExzankxMEpIQjMxT2k5R0Z3emE0cDFCNng3V3lwVjBQUDg1NNIBhgFBVV95cUxOWGtmd1BpZ1U2QlJOeTZIcXhKMTVTOVFEZDJKcDJPS1NzX2NsOG1RT2w2TkpUMDkwTWY1QzlZcGt4LVlmNV9NZlFVUG04S0Y1U2hUSUdFSk5sUlFId1VsZzlnd1JvOGlWQnY2LThiN1J6cjZDSjdSWHd3elNWS3FpYWJqMXFnUQ?oc=5

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
