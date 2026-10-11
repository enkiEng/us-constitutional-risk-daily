# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-11 12:42:36 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **11 / 100** (Baseline Institutional Noise)
- Previous day delta: **0.0**
- Delta vs 7-day average: **-1.0**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.24 | 1.31 |
| Judicial Independence and Rule of Law | 15 | 0.33 | 1.22 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 1.00 | 2.50 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Independent Agency Capture | civil_service_integrity | 2.00 (Yellow) | ai | 6 | 7 |
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 5 | 6 |
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 1 | 2 |
| Court Order Noncompliance | judiciary_rule_of_law | 1.30 (Watch) | keyword | 0 | 0 |
| Election Administration Capture | elections_transfer | 0.95 (Watch) | ai | 0 | 4 |

## Evidence Samples

### Independent Agency Capture
- Assessment: The establishment of a committee to investigate a Federal Reserve governor represents a concrete action aimed at removing an independent agency official. While not yet successful removal, this is a verifiable attempt to weaken the independence of the Fed through targeted investigation and intimidation of a sitting governor. The Fed's independence depends on insulation from executive pressure to remove officials for policy disagreements. A presidential committee investigating a Fed governor to facilitate her removal constitutes a stress on that independence safeguard, though it remains an investigative action rather than a completed removal or structural dismantling.
- [PBS] Trump establishes committee to investigate Federal Reserve's Lisa Cook in latest effort to fire her - PBS (2026-10-09) - https://news.google.com/rss/articles/CBMi1wFBVV95cUxObEdMclh5a2RrT0JKbE02ZVRKQ29FQkFwdkJNdVhFWWt0S2dBdG1PeE10b1A1TlpqbnBGeUxlUmhPMUNuY3BZdS1EeGlONFhhZ0VDcUdrNXhjN1hFSVBBcVp2N3pfYmdROWNwLTJTdTVSMVY2bUNnVUp4aEcxV3VWOXNESXFqcmF2Z0NxdEN0Q2tDM3lOeTJ5dHQyMERxQzJzZ2Z6aFpwbFNiSjBfRWN1TW5jOHFxSWpKVk96eU1GWUJ0Qk1icVNJZE42dU5aVlRqMC1FYTZRa9IB1wFBVV95cUxObEdMclh5a2RrT0JKbE02ZVRKQ29FQkFwdkJNdVhFWWt0S2dBdG1PeE10b1A1TlpqbnBGeUxlUmhPMUNuY3BZdS1EeGlONFhhZ0VDcUdrNXhjN1hFSVBBcVp2N3pfYmdROWNwLTJTdTVSMVY2bUNnVUp4aEcxV3VWOXNESXFqcmF2Z0NxdEN0Q2tDM3lOeTJ5dHQyMERxQzJzZ2Z6aFpwbFNiSjBfRWN1TW5jOHFxSWpKVk96eU1GWUJ0Qk1icVNJZE42dU5aVlRqMC1FYTZRaw?oc=5
- [Mother Jones] Trump Tries—Yet Again—to Fire Fed Governor Lisa Cook - Mother Jones (2026-10-09) - https://news.google.com/rss/articles/CBMinwFBVV95cUxNejR4ZEhYMXhoUXFhM2dNZ3otUlVFWFBEb1JVRDRERml4SjhrYnJlRllpWkdKa1Zucm15SzgxeXQyLTFJaXlHWnVNTmtIVXpQMmRzaE9LOFdidjlWcnFhMU84c1d5N1hwalFScnpCOVpqZE5pM2R6eUs2aEtCMGdsc1RRTEZfTUlEcnBiUDV0ZXk3dFB1dVd6bU5DMTBSRFE?oc=5
- [Detroit Free Press] Trump creates White House panel to investigate Fed Governor Lisa Cook - Detroit Free Press (2026-10-09) - https://news.google.com/rss/articles/CBMivgFBVV95cUxPR09xYUVFQVd2WEwtazlUUzViSElUNndqcTJDckZjalEtbHViT2NnTGdNM3EtMzRGWWV3Q0piY1p2Z016NjN2MDA2dUIxa25nT245NE00blA3NnRNRmdNRDYtSlF2YUpOeGVxV1dsSURLdXJid3lfNm9YYnl6YmN5SjdiN2RlY2l3eTV6UVpoZ0syTWgwRTRRdHBpalpWNGQ5VE1OTXpxZjhoekx6RktqeUMyZkZoSlRLenNrSlhn?oc=5

### Public Funds for Political Promotion
- Assessment: Multiple lawsuits filed against Trump administration alleging use of taxpayer funds for political advertising. The fact that lawsuits are being filed indicates plaintiffs have identified and are challenging alleged actual use of federal funds for partisan promotion. This is a credible, repeated stress signal of the activity described by the signal. Severity 2: confirmed instances of alleged improper spending are being litigated, indicating real occurrence rather than mere proposal or hypothetical.
- [Democracy Docket] Trump’s taxpayer-funded propaganda ads draw third lawsuit - Democracy Docket (2026-10-09) - https://news.google.com/rss/articles/CBMiowFBVV95cUxPT1c0Q251YnNPTmllNzE0ZWlvd3RLRXRPTWxiNDF2NGhiSUMyWEVxU1VCd0tLWHNjMktfUU1VcHZ5MEQxQlBjbnA5aFQxMktXTmViTldCbnFWWEszWGtjYVIyNnZNbmtpREZ2STVia2JhNFZkalY4NHIxUDA5UU9lUXA5ejh6eEFFblY3My1ubVBIX3NXcjVrM3FBUFQ2ZHdGSTFj?oc=5
- [Mother Jones] You’re Funding Trump’s New Ads - Mother Jones (2026-10-09) - https://news.google.com/rss/articles/CBMif0FVX3lxTFBNZkZ2d2tIYURUVjFIQVI1b01yTVY2RWx4QWVDVkN5bFAyVFd5X3VxQlY2NllXV0NROUpRTEpsdFlOTWxzS2JTRUctVkwxbHo4X2pHNjlEYU45TFREY3NaWUlzM1VDUnhqYmU3dHlHbkRYLVM3LUU0R3VIOFFqUzA?oc=5
- [Milwaukee Journal Sentinel] Wisconsin Dems sue administration over taxpayer-funded pro-Trump ads - Milwaukee Journal Sentinel (2026-10-09) - https://news.google.com/rss/articles/CBMi3wFBVV95cUxPN2dYNG96dGtTUlhaLWlGeFgtOEFJVlFJbmxFVHh5YmJGNGtBUk5OdkM4cmZ0eUNhOWtaaXVDTkktM3NGUHZfZUV1Znhobm5Od2dPSWk1Yi1vT2FzV3hjYWI5dHZiemt4TzZiT1pOTWU3MzJkUVBiTlBuSEZ5SUk0LWhMVmRFckd1UlJzdXNGS1Mzcm8tN09MUjBvbTUzQzNSNjFsWl9uR3BIOTY1QUtwd3pDeVpkRlFSVjUzVkdjRnRvWUI5TVBJN2g2X2VmNmhLWnJubGNlVVQ5TDFVWTI4?oc=5

### Legislative Bypass by Executive
- Assessment: Multiple credible sources report that the Supreme Court allowed Trump to implement parts of a mail-in voting executive order. This represents a shift of voting-rule authority from statutory/legislative control to unilateral executive action via EO. The Court's allowance (likely through stay or injunction ruling) enabled executive implementation without requiring legislative authorization. This is a real, confirmed action that transfers governance authority from statute to executive fiat, but is narrowly scoped to mail-voting procedures rather than a broader structural dismantling. Severity 2 reflects this as a real, credible stress signal of limited scope, not yet structural failure.
- [ABC News - Breaking News, Latest News and Videos] Supreme Court allows Trump to implement parts of his mail-in voting executive order - ABC News - Breaking News, Latest News and Videos (2026-10-09) - https://news.google.com/rss/articles/CBMigAFBVV95cUxQLUpWVmxZNkVNNGxlamhNRjkteVhjUVJNMXhDQ3Vyc3V3UkdTVEcyeUM0ZnEzTUlJQXRYMUZsNkZ5LTN5Q0VzWDFrVmVFSVlpOFBSaEpwa19qd0Q4SExzankxMEpIQjMxT2k5R0Z3emE0cDFCNng3V3lwVjBQUDg1NNIBhgFBVV95cUxOWGtmd1BpZ1U2QlJOeTZIcXhKMTVTOVFEZDJKcDJPS1NzX2NsOG1RT2w2TkpUMDkwTWY1QzlZcGt4LVlmNV9NZlFVUG04S0Y1U2hUSUdFSk5sUlFId1VsZzlnd1JvOGlWQnY2LThiN1J6cjZDSjdSWHd3elNWS3FpYWJqMXFnUQ?oc=5

### Court Order Noncompliance
- No fresh evidence links in the current lookback window.
### Election Administration Capture
- [American Civil Liberties Union] Federal Court Sides With Voters, Ruling DOJ Data Demands Violate Voter Privacy, States’ Election Authority - American Civil Liberties Union (2026-10-09) - https://news.google.com/rss/articles/CBMizwFBVV95cUxQajhYSXpOcUU3TmFmZWVhcDVycVdMdnpWem5ZTlV0cWZlWEt6WWdFUDR0ZTJfZjhEODU2MDhHa1NiYi1oTTdSRElJRHZnNnJuRzNET3ZFUTAzRHA3Yk9rb0YxWGVaY3A5dG9uUjJ4andrSmRfWk5xcDdxd3J5Sm5WTURITFFBOC1IVHptWVltTER3SXNYV3hvSlRXT0g3bDBtbWNTSGFnLVlwWS1CLUlaVFFLbnN4ZVlwb0RSVnhHcWJrUkNvOTBNS1VDSEhRVG8?oc=5
- [ABC News - Breaking News, Latest News and Videos] 'Going to be practical': Sen. Markwayne Mullin speaks out after being named Noem's replacement at DHS - ABC News - Breaking News, Latest News and Videos (2026-10-10) - https://news.google.com/rss/articles/CBMipgFBVV95cUxQRGFPSVpoVFZTUlFjaDZRakItV05kaVlGVlluM1pMRGRvTkpaS2RFNlY2ZElwbFFOUEwtQVhSTzVVZlRmSmVBb1JFZDBaaVRqR05kNnZydDNBcFVOak5ENzZvRmdaOFdLTk9sUk9Kc3hSdnB4a3VEcGl6NDJ0M2RNTG9mMjFSUkd0MlNUYnl2QTNjeDI3aWt1UHM3WVBXaGhTOVY0VXBR0gGrAUFVX3lxTE1JN1FWZ1RwMHQ4aEpyckdLR2RxTnhucVUwZ21uVWZscnBKU3MxZFBQX3RaTXlBZE45YnBXLUo0OW4tSWRWdDRRVnFtTHhxbVdzMTJuLTNYQXdQUlB2M0hobldMT05hN2xscnlXLXVjT2VaX2I5WXlzWWdiY0lWNHIzZ0dDMnBDTFN5bUx1bXpQRkduNzdjcF9nS2ZqbTZZMm5YQmRaOTlPVjdNYw?oc=5
- [LAist] Prop. 5: Revamp how California handles recall elections - LAist (2026-10-10) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQRktmTGtpb0pUOGpGT1g4OVBsVlBpcXU3Smh1M09oQVY4TU50Z2I2RTdpal9MVFA3NUhkanl5YWZscUFXMU93WFlTWjRBcEp2dmF6VjdsWkk1SEFxci1DYlZaTUhmeWhSd19lVHoxRU95cXNGMVRJNnREazBGWVc2YUNULW9FNzAxSERyYnBkdTQyOGplczFlYnc5SUJYRWxQanJCQWRieFd2M09M?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 15 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
