# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-26 14:08:17 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **24 / 100** (Elevated Strain)
- Previous day delta: **+2.0**
- Delta vs 7-day average: **+7.1**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 2.00 | 11.00 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.20 | 0.70 |
| Executive Constraints and Emergency Powers | 13 | 0.00 | 0.00 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 1.65 | 4.12 |
| Security Sector Neutrality | 8 | 0.82 | 1.65 |
| Federalism and Legislative Oversight | 8 | 2.00 | 4.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 3.00 (Orange) | ai | 3 | 6 |
| Legislative Oversight Obstruction | federalism_oversight | 3.00 (Orange) | ai | 1 | 1 |
| Public Funds for Political Promotion | civil_liberties_information | 2.65 (Yellow) | ai | 1 | 1 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 3 | 0 |
| Election Certification Interference | elections_transfer | 1.65 (Watch) | ai | 0 | 0 |
| Domestic Military Use in Political Conflict | security_sector_neutrality | 1.65 (Watch) | keyword | 0 | 0 |
| Opposition Ballot Exclusion | opposition_pluralism | 0.60 (Green) | ai | 0 | 2 |
| Press Restrictions or Retaliation | civil_liberties_information | 0.25 (Green) | ai | 0 | 4 |
| Inspector General Retaliation | civil_service_integrity | 0.25 (Green) | ai | 0 | 0 |

## Evidence Samples

### Election Administration Capture
- Assessment: Report indicates DOJ has filed a lawsuit seeking to block Alaska Senate election results contingent on a Republican loss. This represents a direct federal intervention to prevent certification of election results based on outcome, which constitutes partisan control of election administration and a serious assertion of federal power to override state election administration. A lawsuit filed is a concrete action (not a proposal), and blocking results based on party affiliation is a high-severity manifestation of election administration capture.
- [NPR] Blanche defends DOJ lawsuit blocking Alaska Senate results if Republican loses - NPR (2026-10-25) - https://news.google.com/rss/articles/CBMiwAFBVV95cUxPeTFtSVNpVEV6RTJSb3VhQ1I1WEsyYXBaaWxXV0hBZkZ0R0RkN2Nrdm9lRnM2WWhVd19xTWVMVzcyLUM2SExta29EWVI5Q2JJaWJKSmxSNmhHYmwtVUtPUngxUGhfWld0eW9BaTlQRFZjWHptbE9ocWdjQVBUdTl2Nm5wYTVDdnN4Q21DY254dGFxZ2lGQXNfY21PVG4wVjJwZi1rLWszQkFuMEpnN1A4NnZ0RVYtcTlvWlpHeFVlSXg?oc=5
- [NewsOne] Trump Sues Alaska To Stop A Senate Election If His Guy Loses - NewsOne (2026-10-24) - https://news.google.com/rss/articles/CBMib0FVX3lxTE5OdzctYm0wcGo3RFFYYzctSHE2empYT2x4MHpTQmFNNGV2bEFsaHBhTllpb2UyRjNQZ2NtX0JVMVdxOTBvekJXbWFjamtBdDJBcFMtUDUyVllONFBfLWk3TFVYZ3U4V3AtMVdnZWxGcw?oc=5
- [WKBW] Justice Department orders California counties to set aside ballots from suspected noncitizens - WKBW (2026-10-25) - https://news.google.com/rss/articles/CBMi0wFBVV95cUxPQ041anJMbnpmY1Z5V0hTMHU1ZHppX2VDT2JYS2g0eXpQV3hFR0I2em5tZzBOZjVZOWgzTVJpemZaNEU1WXFSdlpBNEVlbnhWX01KNEhHbHVWNFhPa1hMS1B4dkpuSk03UFo2bEc3dDBOSWd2dUwybXVCeXhhMmp5bDg2d2pmS0x0cW05YzIyVG9CZUUwRFA4QWJ3YnNfa2ZELVFWWm1XUDlYbVNHZW9yOVZlUGt0TUtFTm1yQlJzRFFRUE5rTFBXeGl0eHRCWlF0ck9Z?oc=5

### Legislative Oversight Obstruction
- Assessment: DOJ assertion that a House-issued subpoena no longer obligates testimony constitutes a direct obstruction of legislative fact-finding. The DOJ has taken an affirmative position that removes the binding effect of a lawful legislative subpoena without a court order or statutory authority. This is a confirmed high-severity action blocking executive accountability to Congress in an ongoing investigation. The systematic claim (that the subpoena 'no longer obligates') represents an official position that strips the House Oversight Committee of its core fact-finding power in this matter.
- [ABC News - Breaking News, Latest News and Videos] DOJ says House Oversight's subpoena 'no longer obligates' Bondi testimony in Epstein matter - ABC News - Breaking News, Latest News and Videos (2026-10-24) - https://news.google.com/rss/articles/CBMirwFBVV95cUxORTJiZlVKWkpFTkRRTnUtaVl2MkptSGRSZ1ROV1pyV3dLNFdyRGV6RDRybUJXMzgySjJkYUhsbGdHNGw1Mmw4VExNY1JaMENkSWtFeE5qM3pOUk9seW42eHhCYTQ0ZUcxLTM5TXdTQVdwOHVsVlFmUUpTQ0J0TGEwYVFLaHN5d3pHTGlVaTBhc1BHdFZvdzN5MzVrenZ3VldUcnhmSXZKRTlDWEUtQ1Q00gG0AUFVX3lxTE5ad3ZZQm5USXplejJSZkdVTnNHcUJ2U3ZLTlhnUTR1RTU5WVFjYVRoM181UW9sV1RJdnMtUWNiVXJ6WjQ2T3dyZ1FmaWxmWnh6cHdMTmFSaWgtZzVjNHlhN05BR09IX2p0Mk9FTEVVYU5yTFVkbFdNU3hpanhGaFpXU2ZZeEdKRzZscGRVVnJ5SlM4UHF5c0lBQ2FkN1pvdkd0UjBIN3JkN0ZIUjdNeDN1bVE0Yg?oc=5

### Public Funds for Political Promotion
- Assessment: News report confirming that an administration aired TV advertisements promoting the officeholder using taxpayer funds. This constitutes spending of appropriated public money on communications that promote the officeholder rather than serve a public-information purpose, which directly matches the signal definition. The report itself treats this as a real occurrence (not hypothetical, opinion, or allegation), though the severity is moderate because this appears to be a discrete action that has been detected and is now subject to public scrutiny and potential legal challenge. No court order has been defied, no structural constitutional breakdown has occurred, but the alleged violation of the 1950s appropriations prohibition on 'publicity or propaganda purposes' is material.
- [ABC News - Breaking News, Latest News and Videos] Administration's pro-Trump TV ad is taxpayer-funded - ABC News - Breaking News, Latest News and Videos (2026-10-26) - https://news.google.com/rss/articles/CBMiqAFBVV95cUxNNEc3UWRPWjdaWkt2Wk9vcklvTkd3LUU0eEFHNnBTNGE1M01jZ1ZsczFwN0o1VjVmMk9rU3kxOUx5M1N2V1MtLVRqNjFfUXJYV0FQeFJSV3pBSEJ1Y2NFV29FMzFGLUxmVGVRa2tVVnhwM3hRYVhzSnFRM2YzUklyR3BjQm4xOUltenU0V2lRSHB2SzJlVmpMLV9lMHdGT2dJU3FBZG5FVVnSAa4BQVVfeXFMT2lPdUJtQ0JKMEs1aVhMMUFfOXFWRmxwZlBsSk9LYjFHX3pMamdNOUV6c1BNZnQwdGtVUzRTMS1IVzJoWjl4c3Z1elZtdWotY2MwazN5UzhQNGk1TGtnSGJhMzI3WUNlY3BlemEzWGlNMkpGNnFjNXZiZU1vQVZ3SFRPYklhZjN1ek4wWUN3ZUt4YUxMcDJpTmhGMjhaVkg4Wm0tMm9CbERyWnVENjNB?oc=5

### Civil Service Purge / Schedule F
- Assessment: Final rule issued by OPM expanding the scope and legitimate uses of administrative leave, including explicitly for 'workforce realignment initiatives.' This is an accomplished regulatory action (not a proposal) that creates new legal authority for executive discretion in removing or repositioning civil servants. Administrative leave can facilitate workforce removal without competitive process protections. Severity 2 because this is a real, confirmed action that materially expands tools available for politicized personnel actions, but it is a procedural/regulatory change rather than a demonstrated mass removal or targeted purge yet executed.
- [federalregister.gov] **[official record]** Administrative Leave for Workforce Realignment and Other Purposes (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21320/administrative-leave-for-workforce-realignment-and-other-purposes
- [federalregister.gov] **[official record]** Elimination of Time-in-Grade (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21319/elimination-of-time-in-grade
- [federalregister.gov] **[official record]** Managing Senior Professional Performance (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21316/managing-senior-professional-performance

### Election Certification Interference
- [courtlistener.com] **[official record]** United States v. State of Alaska (2026-10-23) - https://www.courtlistener.com/docket/75009254/5/united-states-v-state-of-alaska/

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 29 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 3
- Evidence extraction: AI event extraction
- Confidence: **Medium**
- Fetch errors:
  - military_domestic_political_use: courtlistener: The read operation timed out

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
