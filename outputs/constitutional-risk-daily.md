# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-09 12:43:29 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **13 / 100** (Baseline Institutional Noise)
- Previous day delta: **-3.0**
- Delta vs 7-day average: **+1.3**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.65 | 3.57 |
| Judicial Independence and Rule of Law | 15 | 1.00 | 3.75 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.65 | 2.11 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.00 | 2.50 |
| Security Sector Neutrality | 8 | 0.33 | 0.65 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 22 | 44 |
| Court Order Noncompliance | judiciary_rule_of_law | 2.00 (Yellow) | ai | 1 | 2 |
| Election Administration Capture | elections_transfer | 1.65 (Watch) | ai | 0 | 2 |
| Legislative Bypass by Executive | executive_constraints | 1.65 (Watch) | keyword | 0 | 0 |
| Domestic Military Use in Political Conflict | security_sector_neutrality | 0.65 (Green) | ai | 0 | 2 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: DNC has filed a lawsuit alleging that taxpayer-funded ads promoting Trump constitute illegal propaganda under the 1950s appropriations law barring federal funds for publicity or propaganda. The lawsuit is a credible, verified action alleging the underlying signal event (use of public funds for partisan promotion). However, severity is 2, not higher, because: (1) the lawsuit is a legal challenge to an alleged violation, not confirmation by government or court that the violation occurred; (2) the lawsuit itself is the remedy mechanism, suggesting checks remain functional; (3) no court has yet ruled on the merits; (4) the suit alleges the conduct but does not confirm it has been judicially established.
- [PBS] DNC files lawsuit alleging Trump's taxpayer-funded ads are illegal propaganda - PBS (2026-10-07) - https://news.google.com/rss/articles/CBMitAFBVV95cUxOcmFTNnZQbDJuczJ6RnN0UHRXaDBZSHJ0UUhfYm54andsLVJWN3MtYTFHMERYZml4M3ZMNWQwLUZUVTRhSk1Ranh5eVpBYTBZYmJpOVlfOXd3S2FadjdhWTc3N0VpcEJ0LUxwWjZ3VjhlbUg5S2tZamVWV2xsY2NZTzRmVzRDenppWUpYTmFGQld6VDUwVk1WazBZVk5PUzZzQlJ6R2dEa3FXX183N29EMVgzMG7SAboBQVVfeXFMTUdZRVpqQ1l6dXN4ODF4ME42dEM2MEhZckJyU0VMd0xiWENEVFlyeXVvQ2hwV2NlaVZDX3VDLW5rdHNCN3FLOUEwdi10TGhfQzRxTnZsY1RHTlRuWk1NT095cm14cW5fWEJsZlVOcnpBeFFkWEhFYVVJSnhUeU5MT3BGRzROdU5uQjk1ZW1QTUdlWE1tOXhxN3UxdS0wc1JaeGxNTXhPOFljd1VJcE5vdWdWazZlNlVEVk1B?oc=5
- [Common Cause] Coalition Challenges Unlawful Use of Public Money for Trump Political Ads - Common Cause (2026-10-08) - https://news.google.com/rss/articles/CBMirAFBVV95cUxOT25xa2Rnck1FV0xOSE1iRndGaHJ6U04wTnJTQnJTbGZjWi1Jc25tNHRoTjIxSDh6UENfS2ZZSVN6V3h6cExtWXBJbUNKd0FSakNPT2FPLWhyUVBRYlctR0N5eWJqLUpaaVJUWXA3OWpYdU40RV9IOUhORng0TjE3VEV3UVgwZl9FVmdVWjNWSlhEQlhVTUVUV01ZZ1d5UUxRLXdJUlNmT2lIbXBx?oc=5
- [NBC News] DNC sues administration over taxpayer-funded pro-Trump TV ads - NBC News (2026-10-07) - https://news.google.com/rss/articles/CBMirwFBVV95cUxQZkR6VTgxLWFFRUZOUGdWb1dqM0ZQYmRPb2drUHhHTW0wLVBHWWp4N1BRY1pXYjZtWUZURHk1dzhDVHUtanhjakc3RkxrWGhDcFpmaFduRVhmeEZJWWxVRVhlbTBrRS1Lb0RwbWg5ZHctM09KM0ZGQkpLTVYxOVpJcTgzTElxeGdyMkF1NHZ1bW5XbFhocTRtWVgzMjZkM0N2b2FwMV9UWmp0aWFkWlpZ?oc=5

### Court Order Noncompliance
- Assessment: Civil rights groups are alleging that ICE has defied a court detention order from San Francisco. This is a credible mention of alleged executive noncompliance with a judicial order, reported by a legitimate news outlet. The allegation itself indicates a real potential stress event (an agency allegedly flouting court authority), though the use of 'allegedly' and the fact that this is framed as groups seeking enforcement (rather than confirmed defiance) places it at severity 2—a credible but contested signal requiring verification through enforcement proceedings.
- [Davis Vanguard] Civil Rights Groups Seek Federal Court Enforcement as ICE Allegedly Defies San Francisco Detention Order - Davis Vanguard (2026-10-08) - https://news.google.com/rss/articles/CBMia0FVX3lxTE9rYVBfRWJuYnk2OTdEOW1EOVRfTkR0Y21QSkEyYXY5UW1uVmJaYnlvSG8xS2V3a0V0S1h6N3lXYmJSNHdRQkd2X21HaG5RUDBxeWpSY3oyZ2dLckhxUkFhdDlMUG1WV2l6Szhr?oc=5

### Election Administration Capture
- [ABC News - Breaking News, Latest News and Videos] 'Going to be practical': Sen. Markwayne Mullin speaks out after being named Noem's replacement at DHS - ABC News - Breaking News, Latest News and Videos (2026-10-09) - https://news.google.com/rss/articles/CBMipgFBVV95cUxQRGFPSVpoVFZTUlFjaDZRakItV05kaVlGVlluM1pMRGRvTkpaS2RFNlY2ZElwbFFOUEwtQVhSTzVVZlRmSmVBb1JFZDBaaVRqR05kNnZydDNBcFVOak5ENzZvRmdaOFdLTk9sUk9Kc3hSdnB4a3VEcGl6NDJ0M2RNTG9mMjFSUkd0MlNUYnl2QTNjeDI3aWt1UHM3WVBXaGhTOVY0VXBR0gGrAUFVX3lxTE1JN1FWZ1RwMHQ4aEpyckdLR2RxTnhucVUwZ21uVWZscnBKU3MxZFBQX3RaTXlBZE45YnBXLUo0OW4tSWRWdDRRVnFtTHhxbVdzMTJuLTNYQXdQUlB2M0hobldMT05hN2xscnlXLXVjT2VaX2I5WXlzWWdiY0lWNHIzZ0dDMnBDTFN5bUx1bXpQRkduNzdjcF9nS2ZqbTZZMm5YQmRaOTlPVjdNYw?oc=5
- [The New Republic] Election Denier’s Lawyer Reveals Trump’s Chilling Midterm Plan - The New Republic (2026-10-08) - https://news.google.com/rss/articles/CBMioAFBVV95cUxORHV2c0txUUJleEk3ekhWTXFSWlpWOW9peXpiVGdaTng5TlNkLW9fb0hvY1NELVJGTkRJS3RSZEdaZUo5S3VEN3BOb20tNWpaelI0ODB1SzduUktqczVxWVhRRVB5TklYNk5tcFRtVVVTVlFhZnEyUnVBZTd5UkJmNDRxcU9LLVhGMEg0YXQ0TE5CaGJPOEwtOGFqYnZPQWVI?oc=5

### Legislative Bypass by Executive
- No fresh evidence links in the current lookback window.
### Domestic Military Use in Political Conflict
- [courtlistener.com] **[official record]** The City of Johnston v. REV Group LLC (2026-09-18) - https://www.courtlistener.com/docket/74915726/1/the-city-of-johnston-v-rev-group-llc/
- [myRepublica] US activists deploy poll volunteers over Trump intimidation fears - myRepublica (2026-10-09) - https://news.google.com/rss/articles/CBMiwgFBVV95cUxNcnNDLUptTVl2alROWlZ3U083LTRoTUc1Zy1iZVFfUFVkM3BKRW81NXZaQklVeG03RF9lNVcwWldrY2xHQjBFT19ZbXZQZFUtN0NXQzBnS0NSSV9zWlcxc3E5RlZCMU5iRmZienJIa0FYWHVqVHNUSWp3Y2lIOVpONWdmNmJYOXEyTGlZaFh2VUlxY2RNeVZGOGd0YkFiNWlqNE1hTS0yZnN1UW5RMUFNLU9ELXVpb2ZQOTZpVTFzLTRSUQ?oc=5
- [The Times of India] Pak army chief Munir bypasses PM Sharif, moves to deploy more military assets to Saudi Arabia - The Times of India (2026-10-08) - https://news.google.com/rss/articles/CBMi_gFBVV95cUxQT2ltbjlzSU90bTcyRW5qOWtqblJIdWVNTFQzZFMwRWlxdGFrSHc1d1BHbUszYUNYeDFFTU5LWldNcWsxbDRZaHFYSU1TT1ZoQnBEMkdrVmg2UUxiU0huTVh3a0VSeFNMMUh3M1B2b1o5ZUFXSlJ3NGZKUlNNaWRDOEp2T2pCc19CS1JkYmhrUmhEYjdRUkRkVTRKdkZvZXprdERRV09iTUFwdDdZUksxSjNxSk45R3NRM0pPNGRrRnY4TkxPT1FiQ08xUzdFYzVJRXBWejlzYnhGSGhJYkNGVEg4WjRhWVlwbjhXVEFGRkJMMV9YdzNORDVfY2xZd9IBgwJBVV95cUxQU1NfZ1NfSXUtX0NzM2NIQUh2bndiS0wyODk2TkRzSFVLZnd2b19RMHFHU1pfeUI3eGxDM0V3bUdza1p4WF9kc19kZVR6LUVOMzdEU3piV0xQT1ZxRjY4NXRMMzVFb3RERXpCQmhidHdBUGJDN296cFhNT2l2elFZZUpOeGNKM3E5NmJ0R1lZeHFCNV9BVlh2QmNvUDRGMEh3ei1FWG51bU5tQWc1Vk5VOEpxYzVEVEhYWHVJMDl3Vko0LTd2OF9SMGt4bGVjMFFpazhBUHNYRDg1WWtNa2ZOVi1nUk1EQzJNQ2trVkpCd05pMDF6dnR3dzdQeWphZ1A4ME53?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 15 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **High**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
