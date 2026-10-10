# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-10 12:40:51 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **11 / 100** (Baseline Institutional Noise)
- Previous day delta: **-2.0**
- Delta vs 7-day average: **-0.7**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.33 | 1.79 |
| Judicial Independence and Rule of Law | 15 | 0.65 | 2.44 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.43 | 1.41 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 1.00 | 2.50 |
| Security Sector Neutrality | 8 | 0.15 | 0.30 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 15 | 16 |
| Independent Agency Capture | civil_service_integrity | 2.00 (Yellow) | ai | 5 | 7 |
| Court Order Noncompliance | judiciary_rule_of_law | 1.65 (Watch) | keyword | 0 | 0 |
| Election Administration Capture | elections_transfer | 1.30 (Watch) | ai | 0 | 5 |
| Legislative Bypass by Executive | executive_constraints | 1.30 (Watch) | ai | 0 | 2 |
| Domestic Military Use in Political Conflict | security_sector_neutrality | 0.30 (Green) | ai | 0 | 2 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: Multiple lawsuits filed against Trump administration alleging use of taxpayer funds for political advertising. The fact that lawsuits are being filed indicates plaintiffs have identified and are challenging alleged actual use of federal funds for partisan promotion. This is a credible, repeated stress signal of the activity described by the signal. Severity 2: confirmed instances of alleged improper spending are being litigated, indicating real occurrence rather than mere proposal or hypothetical.
- [Democracy Docket] Trump’s taxpayer-funded propaganda ads draw third lawsuit - Democracy Docket (2026-10-09) - https://news.google.com/rss/articles/CBMiowFBVV95cUxPT1c0Q251YnNPTmllNzE0ZWlvd3RLRXRPTWxiNDF2NGhiSUMyWEVxU1VCd0tLWHNjMktfUU1VcHZ5MEQxQlBjbnA5aFQxMktXTmViTldCbnFWWEszWGtjYVIyNnZNbmtpREZ2STVia2JhNFZkalY4NHIxUDA5UU9lUXA5ejh6eEFFblY3My1ubVBIX3NXcjVrM3FBUFQ2ZHdGSTFj?oc=5
- [Mother Jones] You’re Funding Trump’s New Ads - Mother Jones (2026-10-09) - https://news.google.com/rss/articles/CBMif0FVX3lxTFBNZkZ2d2tIYURUVjFIQVI1b01yTVY2RWx4QWVDVkN5bFAyVFd5X3VxQlY2NllXV0NROUpRTEpsdFlOTWxzS2JTRUctVkwxbHo4X2pHNjlEYU45TFREY3NaWUlzM1VDUnhqYmU3dHlHbkRYLVM3LUU0R3VIOFFqUzA?oc=5
- [Milwaukee Journal Sentinel] Wisconsin Dems sue administration over taxpayer-funded pro-Trump ads - Milwaukee Journal Sentinel (2026-10-09) - https://news.google.com/rss/articles/CBMi3wFBVV95cUxPN2dYNG96dGtTUlhaLWlGeFgtOEFJVlFJbmxFVHh5YmJGNGtBUk5OdkM4cmZ0eUNhOWtaaXVDTkktM3NGUHZfZUV1Znhobm5Od2dPSWk1Yi1vT2FzV3hjYWI5dHZiemt4TzZiT1pOTWU3MzJkUVBiTlBuSEZ5SUk0LWhMVmRFckd1UlJzdXNGS1Mzcm8tN09MUjBvbTUzQzNSNjFsWl9uR3BIOTY1QUtwd3pDeVpkRlFSVjUzVkdjRnRvWUI5TVBJN2g2X2VmNmhLWnJubGNlVVQ5TDFVWTI4?oc=5

### Independent Agency Capture
- Assessment: Credible press report (PBS) documents establishment of a committee to investigate a sitting Federal Reserve governor, framed as part of effort to remove her from office. This represents a concrete action to pressure an independent agency official through investigation rather than through ordinary legal channels. Severity is 2 rather than 3 because the action is an investigation/committee, not yet a formal removal or defiance of law; it is a stress signal on Fed independence but not a completed breach of structural safeguards.
- [PBS] Trump establishes committee to investigate Federal Reserve's Lisa Cook in latest effort to fire her - PBS (2026-10-09) - https://news.google.com/rss/articles/CBMi0gFBVV95cUxPczlSNXliYm9yYnRRbzN4MEdfLXR4bFZLdHZzS3dTUUw2dG1wX0NKR240UkpBRWN3el95NHlsNnpEQ3NzUVZyX25jbWxmeW1XZk00Wi1ORFd4TFVvYnhVOUhUQ0NXajhtZ1BzZnZINm1MUGMxRWpuMEZWTnJwTF8wcEpIaGxnSjU3cGlhVkcyZWZnYnEzV1BZSTlpQ1lJS1NHcXRsYllCUG5kXzJCUmpvWTlYamJ0SndDbmhQV2Z2TURxRzJ2aFl4WE5FR2RrbU5nVGfSAdcBQVVfeXFMTmxHTHJYeWtka09CSmxNNmVUSkNvRUJBcHZCTXVYRVlrdEtnQXRtT3hNdG9QNU5aam5wRnlMZVJoTzFDbmNwWXUtRHhpTjRYYWdFQ3FHazV4YzdYRUlQQXFadjd6X2JnUTljcC0yU3U1UjFWNm1DZ1VKeGhHMVd1VjlzRElxanJhdmdDcXRDdENrQzN5TnkyeXR0MjBEcUMyc2dmemhacGxTYkowX0VjdU1uYzhxcUlqSlZPenlNRllCdEJNYnFTSWRONnVOWlZUajAtRWE2UWs?oc=5
- [Mother Jones] Trump Tries—Yet Again—to Fire Fed Governor Lisa Cook - Mother Jones (2026-10-09) - https://news.google.com/rss/articles/CBMinwFBVV95cUxNejR4ZEhYMXhoUXFhM2dNZ3otUlVFWFBEb1JVRDRERml4SjhrYnJlRllpWkdKa1Zucm15SzgxeXQyLTFJaXlHWnVNTmtIVXpQMmRzaE9LOFdidjlWcnFhMU84c1d5N1hwalFScnpCOVpqZE5pM2R6eUs2aEtCMGdsc1RRTEZfTUlEcnBiUDV0ZXk3dFB1dVd6bU5DMTBSRFE?oc=5
- [Realtor.com] Trump Launches New Investigation into Fed Gov. Lisa Cook Over Mortgage Fraud Allegations - Realtor.com (2026-10-09) - https://news.google.com/rss/articles/CBMisgFBVV95cUxPaVNERHh1NWM3MldPWlVtZWdFV0dQYVExel9fUmpVWFdtLWFaVHFZZ2pXZGNBYzZnM1BDY0NzZHROYnVNMk9lancydGo0S0tSYS05R190ajZtQlJmbDVORng2YWN3SkxFUFI5NG5uWEI0NEd1d1dXTFpBVkstM1ZHdVN2c2dpN3BVVWJnZnlmSUhXVmtxZkV5WlpvT0xncnpULUF3S1pTTW5IVXhCYnFTRnZB?oc=5

### Court Order Noncompliance
- No fresh evidence links in the current lookback window.
### Election Administration Capture
- [American Civil Liberties Union] Federal Court Sides Voters, Ruling DOJ Data Demands Violate Voter Privacy, States’ Election Authority - American Civil Liberties Union (2026-10-09) - https://news.google.com/rss/articles/CBMizwFBVV95cUxQajhYSXpOcUU3TmFmZWVhcDVycVdMdnpWem5ZTlV0cWZlWEt6WWdFUDR0ZTJfZjhEODU2MDhHa1NiYi1oTTdSRElJRHZnNnJuRzNET3ZFUTAzRHA3Yk9rb0YxWGVaY3A5dG9uUjJ4andrSmRfWk5xcDdxd3J5Sm5WTURITFFBOC1IVHptWVltTER3SXNYV3hvSlRXT0g3bDBtbWNTSGFnLVlwWS1CLUlaVFFLbnN4ZVlwb0RSVnhHcWJrUkNvOTBNS1VDSEhRVG8?oc=5
- [LAist] Prop. 5: Revamp how California handles recall elections - LAist (2026-10-10) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQRktmTGtpb0pUOGpGT1g4OVBsVlBpcXU3Smh1M09oQVY4TU50Z2I2RTdpal9MVFA3NUhkanl5YWZscUFXMU93WFlTWjRBcEp2dmF6VjdsWkk1SEFxci1DYlZaTUhmeWhSd19lVHoxRU95cXNGMVRJNnREazBGWVc2YUNULW9FNzAxSERyYnBkdTQyOGplczFlYnc5SUJYRWxQanJCQWRieFd2M09M?oc=5
- [Austin American-Statesman] Austin ISD candidates raise at least $86K one month from Election Day - Austin American-Statesman (2026-10-09) - https://news.google.com/rss/articles/CBMirgFBVV95cUxQQTcyUVBYQTNhT0JjSF84UzVfOS1PczRhWm1RMXZ0Sy1IUGY0QmpZR3MwLW90bHlFckpDajRPUm40TVpJLVBlNzJlQUd3UzhJSVk5dUJtQ2VEQWs1VHFRT20ta0dDXzJrZUNtV2Yyb203WlJiY1psYmZRU3ZtbmtTTU9pZkVhNDYyS2ZVdzdQU1Y0SUx4clhScWZxeWhpaHNFc295ZGwzaEZYZ2hvOEE?oc=5

### Legislative Bypass by Executive
- [Naples Daily News] President Trump’s reckless pattern of disastrous judgments | Opinion - Naples Daily News (2026-10-10) - https://news.google.com/rss/articles/CBMiygFBVV95cUxNZy1BcHRIRENhUDBSanBkZk12REY2VHdseTN1SWg5UW9RRlk4dl9Rb3R5cVNNZjRkWnpLOTVuSnJnMW5zSi1zaHl0TUNHdjZmWU15cjVyb0JpRkhYeFBHS0o0WGZmY1hncElWLS16dWxCLXJuSDlEWTUwQ2xReW1rQ2ZVYjFuWXJKaWRaUFFWX0t6SHBYTURPeWk2N3k3RTJHNWR0bnduYUxSTHJIZ0FndFZIMFdWN3FIdTd6LW9zeWZEQmpaamQ5Njdn?oc=5
- [The Regulatory Review] The Future of Administrative Enforcement - The Regulatory Review (2026-10-10) - https://news.google.com/rss/articles/CBMikwFBVV95cUxNZi1DM1pxb0stYVEwczBlRkVwWlI5a1lidWRrSUhwN1FCZW43TENfQXU3UFBFR2R0NlBTWXV6akVNbDc3NUlNUEQzdHVIWk9rV1BPanZjeS1GQVRQOExGWS0xdjBxY3BmSm13SGZLdTBFejh4VUQ2a1RIcTVFMUpKamVsRGJTZVQ5TEEza2o3NlczWHM?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 15 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **High**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
