# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-08 12:46:00 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **16 / 100** (Elevated Strain)
- Previous day delta: **+6.0**
- Delta vs 7-day average: **+4.9**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 1.00 | 3.75 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.00 | 2.50 |
| Security Sector Neutrality | 8 | 0.50 | 1.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 15 | 29 |
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 1 | 4 |
| Court Order Noncompliance | judiciary_rule_of_law | 2.00 (Yellow) | ai | 2 | 2 |
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 2 |
| Domestic Military Use in Political Conflict | security_sector_neutrality | 1.00 (Watch) | ai | 1 | 0 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: DNC has filed a lawsuit alleging that taxpayer-funded ads promoting Trump constitute illegal propaganda under the 1950s appropriations law barring federal funds for publicity or propaganda. The lawsuit is a credible, verified action alleging the underlying signal event (use of public funds for partisan promotion). However, severity is 2, not higher, because: (1) the lawsuit is a legal challenge to an alleged violation, not confirmation by government or court that the violation occurred; (2) the lawsuit itself is the remedy mechanism, suggesting checks remain functional; (3) no court has yet ruled on the merits; (4) the suit alleges the conduct but does not confirm it has been judicially established.
- [PBS] DNC files lawsuit alleging Trump's taxpayer-funded ads are illegal propaganda - PBS (2026-10-07) - https://news.google.com/rss/articles/CBMitAFBVV95cUxOcmFTNnZQbDJuczJ6RnN0UHRXaDBZSHJ0UUhfYm54andsLVJWN3MtYTFHMERYZml4M3ZMNWQwLUZUVTRhSk1Ranh5eVpBYTBZYmJpOVlfOXd3S2FadjdhWTc3N0VpcEJ0LUxwWjZ3VjhlbUg5S2tZamVWV2xsY2NZTzRmVzRDenppWUpYTmFGQld6VDUwVk1WazBZVk5PUzZzQlJ6R2dEa3FXX183N29EMVgzMG7SAboBQVVfeXFMTUdZRVpqQ1l6dXN4ODF4ME42dEM2MEhZckJyU0VMd0xiWENEVFlyeXVvQ2hwV2NlaVZDX3VDLW5rdHNCN3FLOUEwdi10TGhfQzRxTnZsY1RHTlRuWk1NT095cm14cW5fWEJsZlVOcnpBeFFkWEhFYVVJSnhUeU5MT3BGRzROdU5uQjk1ZW1QTUdlWE1tOXhxN3UxdS0wc1JaeGxNTXhPOFljd1VJcE5vdWdWazZlNlVEVk1B?oc=5
- [NBC News] DNC sues administration over taxpayer-funded pro-Trump TV ads - NBC News (2026-10-07) - https://news.google.com/rss/articles/CBMirwFBVV95cUxQZkR6VTgxLWFFRUZOUGdWb1dqM0ZQYmRPb2drUHhHTW0wLVBHWWp4N1BRY1pXYjZtWUZURHk1dzhDVHUtanhjakc3RkxrWGhDcFpmaFduRVhmeEZJWWxVRVhlbTBrRS1Lb0RwbWg5ZHctM09KM0ZGQkpLTVYxOVpJcTgzTElxeGdyMkF1NHZ1bW5XbFhocTRtWVgzMjZkM0N2b2FwMV9UWmp0aWFkWlpZ?oc=5
- [Democracy Docket] Trump hit with second lawsuit over taxpayer-funded political propaganda ads - Democracy Docket (2026-10-08) - https://news.google.com/rss/articles/CBMivAFBVV95cUxNd0JYcE5xRDByVTVGbTZ4YjJTYUliQlZySVVnUVdQRWZ5dmkzRjV2TXNHNDhlMDdFaEhYWlMwSVZZV0tPcWRzTGxGWXJqU3lkSlVpbWxleF9Ob2hDU1dyQ0Flbzd5ZGhrZUlnMkx6VFFCUGwzVXpZMVJVM0dLWGJGTC12UXEwSC0tSFd1VU9WTXhBc1ZyRmNrRzRTRkZMREJ0ZUJnSUpyRnR3MHZsUG84eXFsVXhSMUgwc3d2cg?oc=5

### Legislative Bypass by Executive
- Assessment: Multiple credible sources report that the Supreme Court allowed Trump to implement parts of a mail-in voting executive order. This represents a shift of voting-rule authority from statutory/legislative control to unilateral executive action via EO. The Court's allowance (likely through stay or injunction ruling) enabled executive implementation without requiring legislative authorization. This is a real, confirmed action that transfers governance authority from statute to executive fiat, but is narrowly scoped to mail-voting procedures rather than a broader structural dismantling. Severity 2 reflects this as a real, credible stress signal of limited scope, not yet structural failure.
- [ABC News - Breaking News, Latest News and Videos] Supreme Court allows Trump to implement parts of his mail-in voting executive order - ABC News - Breaking News, Latest News and Videos (2026-10-06) - https://news.google.com/rss/articles/CBMigAFBVV95cUxQLUpWVmxZNkVNNGxlamhNRjkteVhjUVJNMXhDQ3Vyc3V3UkdTVEcyeUM0ZnEzTUlJQXRYMUZsNkZ5LTN5Q0VzWDFrVmVFSVlpOFBSaEpwa19qd0Q4SExzankxMEpIQjMxT2k5R0Z3emE0cDFCNng3V3lwVjBQUDg1NNIBhgFBVV95cUxOWGtmd1BpZ1U2QlJOeTZIcXhKMTVTOVFEZDJKcDJPS1NzX2NsOG1RT2w2TkpUMDkwTWY1QzlZcGt4LVlmNV9NZlFVUG04S0Y1U2hUSUdFSk5sUlFId1VsZzlnd1JvOGlWQnY2LThiN1J6cjZDSjdSWHd3elNWS3FpYWJqMXFnUQ?oc=5

### Court Order Noncompliance
- Assessment: Civil rights groups are alleging that ICE has defied a court detention order from San Francisco. This is a credible mention of alleged executive noncompliance with a judicial order, reported by a legitimate news outlet. The allegation itself indicates a real potential stress event (an agency allegedly flouting court authority), though the use of 'allegedly' and the fact that this is framed as groups seeking enforcement (rather than confirmed defiance) places it at severity 2—a credible but contested signal requiring verification through enforcement proceedings.
- [Davis Vanguard] Civil Rights Groups Seek Federal Court Enforcement as ICE Allegedly Defies San Francisco Detention Order - Davis Vanguard (2026-10-08) - https://news.google.com/rss/articles/CBMia0FVX3lxTE9rYVBfRWJuYnk2OTdEOW1EOVRfTkR0Y21QSkEyYXY5UW1uVmJaYnlvSG8xS2V3a0V0S1h6N3lXYmJSNHdRQkd2X21HaG5RUDBxeWpSY3oyZ2dLckhxUkFhdDlMUG1WV2l6Szhr?oc=5
- [GovExec.com] Union demands federal prison leaders be held in contempt after agency ‘openly defies’ court order - GovExec.com (2026-10-07) - https://news.google.com/rss/articles/CBMizwFBVV95cUxQODV1SUZKT0h5Zk5VU3VsTzFkdDFia0FrOWxZS05qc3hkNGZMeF8tZ0dLUXNJVk5kS0dLR25Vbzl1blhzYkJuaTdNWFNaVV9xUkd0ZXljWHlac1AxWjd1a01lOEtDUlJ0THNlVHVRSXNxbTd5TXJMcXhqWmNKMjVPdm56b3J0Y0tnT3ZrNmFIRXFTbjh4czFvOTBZeXlRMTNMYUxueGl3dVFPaUl1LTZFUDFnQi1QVHlodGdfRTZ5a1J4WGE2alhuUFNFeXpHUDA?oc=5

### Election Administration Capture
- Assessment: Florida election officials removed a sitting U.S. president's personal information from voter files. This is a credible, confirmed action by election administration that demonstrates differential treatment based on partisan identity (removal of one officeholder's data). However, severity remains at 2 rather than 3 because the action appears reactive to a disputed legal citation rather than a systematic structural capture; it is a single documented instance of partisan-inflected administrative discretion rather than an ongoing campaign or structural takeover of election administration.
- [WLRN] Florida removes Trump’s personal information from voter files, after president wrongly cites new law - WLRN (2026-10-06) - https://news.google.com/rss/articles/CBMi5AFBVV95cUxPdmdIZHhGaG1IcWJWYW9IMHh2MjB0UmFJcWc3c2czTjNxNUwtcGJjYmJRYy1mdzJTRTNTMDJYeVFYMS1JZmlYWDJFdm9NX2VQNEJENnZFMGt3RnFtNUpnSTI0TTlMN3lKY084OGZ1dnFqUnlpQ25Ld1lSVEZHVS1JTkNMcldraTI5QW44Q0ZxekZWNFBzMWEwOG1MNXNWNUx1bHNiNVoxS3A5TGMtNnI1REM1LTBhZE5tVFFKOWhIWDZiemlOVmRZR0RKUUpJRmxzT0VMd2FhcnFnRUNzaHRiYzl6WUc?oc=5

### Domestic Military Use in Political Conflict
- Assessment: A civil complaint has been filed in federal court (D. Minnesota) naming multiple current and former federal officials. The complaint itself is an official record indicating that plaintiffs have asserted claims regarding potentially unlawful conduct by these defendants. However, without access to the complaint's substantive allegations, the severity cannot be determined beyond acknowledging that a legal action has been initiated. The filing is a real procedural event, but severity is limited to 1 because a complaint represents an allegation, not a proven occurrence, and the specific nature of the alleged conduct cannot be assessed from the docket summary alone.
- [courtlistener.com] **[official record]** Ganger v. Ross (2026-10-01) - https://www.courtlistener.com/docket/74901903/1/ganger-v-ross/

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 16 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 1
- Evidence extraction: AI event extraction
- Confidence: **High**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
