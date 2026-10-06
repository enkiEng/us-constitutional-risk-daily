# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-06 12:43:20 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **9 / 100** (Baseline Institutional Noise)
- Previous day delta: **-3.0**
- Delta vs 7-day average: **-0.2**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.65 | 3.57 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.65 | 2.11 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.00 | 2.50 |
| Security Sector Neutrality | 8 | 0.50 | 1.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 11 | 31 |
| Legislative Bypass by Executive | executive_constraints | 1.65 (Watch) | ai | 0 | 3 |
| Election Administration Capture | elections_transfer | 1.65 (Watch) | ai | 0 | 2 |
| Domestic Military Use in Political Conflict | security_sector_neutrality | 1.00 (Watch) | ai | 1 | 0 |
| Press Restrictions or Retaliation | civil_liberties_information | 0.60 (Green) | ai | 0 | 1 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: Multiple credible sources report that taxpayer-funded ads promoting Trump were created and broadcast, then reversed after public backlash. The underlying fact—that public funds were used for partisan promotional ads—constitutes a real occurrence of the signal. Trump's subsequent promise to reimburse is a remedial statement, not a denial that the spending happened. This is a confirmed but limited incident (severity 2), not a structural failure, and was halted upon exposure.
- [The Guardian] Trump says Super Pac will pay for taxpayer-funded ads that sparked outcry - The Guardian (2026-10-06) - https://news.google.com/rss/articles/CBMidkFVX3lxTE0xcjJuOU12TDVrVFJfeGlxR3lhLXp5RmQyb0ViejZzc3Y5b1BtMlVKUndZMFdmeVhFLVRhNUhYNlpKaVlLbExzbnZ2V0tJN25lLXNTb1laT0thbllVLXB4bXptSV9rQzFROFR5YThlQ1hxa3JLTGc?oc=5
- [Spectrum News] Trump says his super PAC will pay for taxpayer-funded ads that sparked backlash for glo­ri­fying him - Spectrum News (2026-10-06) - https://news.google.com/rss/articles/CBMi7wFBVV95cUxNNzQxUExtdEFkYnRKOVNiY2lQMDRfZGV6a0pNLU0yWVliUE5OTWNrX2R6TE5DZzNvMldidFN0VmVfRzVzQzZlcU1XR3VHZV9LVVBicWNRMWZMbXRXS1RialQ4NlhMUUdoRVlpZm41QkVnYjFKaGdmRFQ2ajhHMUFwZzhKS05iX2FQbVZPUml2cHhvN1AwVVFsS3FSdWdwbWNsOHk3by1OemxFcmg5am1tRS0zNUptRDhPVHlkM1lZemJIZUh6ZTlZbmlkTlJjb01ZQWxFdGw1UjNpQVloRDdCVGFIWXpkenNZa2pPQzlycw?oc=5
- [DW.com] Trump says taxpayers will no longer fund ads touting administration - DW.com (2026-10-06) - https://news.google.com/rss/articles/CBMiogFBVV95cUxNY0ZmSE1PeU1HVE03Mk1vR2k5ZjZ5S0VRZFM3RDBUcFpPX0M2ZGtZaXpIaGR2eXRiMGRidXBwUTN6V2ppVm5vaV9hODRmUklGYWpEMS1zOE42MkR0all1bGNTSGltdUFNcGhJZGlmWWVGb0hycllLeF8zaVAzMjRJVEN5cjlXQmRydE55aDFQUnhPQVZSSFhxMjF5VlVVVWNLRVHSAaIBQVVfeXFMTk5qMTBhOEhDWGt5NW1mVTZsQ1hSZWtubm9Qc3hPRUpLa05qQ0ZjN1JPRnlvX05iRTZ0NW5uZENZSF9uWUlBeG9hTlJjMnpLSkRGbWh1Ulo1R29CSThTOWZNT0dFOE93VnJLOEpsaHAzcmFmOXBMSkZaOEZ5dkZHcjVwZGlUQ2FfaF9fVkRYMEc1QUJBVTFHbFNDaHVZSnc1dUFR?oc=5

### Legislative Bypass by Executive
- [federalregister.gov] **[official record]** Rescissions Proposals Pursuant to the Congressional Budget and Impoundment Control Act of 1974 (2026-09-30) - https://www.federalregister.gov/documents/2026/09/30/2026-19965/rescissions-proposals-pursuant-to-the-congressional-budget-and-impoundment-control-act-of-1974
- [National Affairs] The Unfinished Work of Federal Permitting Reform - National Affairs (2026-10-06) - https://news.google.com/rss/articles/CBMimAFBVV95cUxOa0o4OXVkQkxHdXJ6VkxqLUNNTVhfQ0JFT3lYSDFLc2YycTlRUFV3VWp3TFhMMTgwSGZQaTdlU2RMNFBVZlV2Q05odjlFN3QwU0ZHVFh5QXE0OEJKRWh0dnR4ZGxFVk5KblVTWXI2UzJrRWlSeF9DWXAxX3lRNDRPMVBHdVlsdVZuemZZSjcyWGF0dUV1YnB3Xw?oc=5
- [The New York Times] Congress Is Supposed to Be More Powerful Than the Supreme Court. Why Isn’t It? - The New York Times (2026-10-05) - https://news.google.com/rss/articles/CBMie0FVX3lxTE05LVE4Z1M4cDRTcFdPbWdRM3FoblR0UFMtejB6SjRGbUd4czNmQTlvcGpfa0l3dDk5VnhZRDJoOE1GTXliRlFoWnA3NWMwOFlNZjV2ZHB2cEw4cTNUU3o2dWVSb1V5VWswSDZ1TmhPREtBSTMtaWV1VkJOdw?oc=5

### Election Administration Capture
- [The Washington Post] An election chief lost. Then he padlocked the ballots and called the FBI. - The Washington Post (2026-10-04) - https://news.google.com/rss/articles/CBMisgFBVV95cUxNZmd6T0E5dUtlRXdDSV9pQVgwVkZfUk5LZG5GTFh3MTBlUzhBY1F6dDNIejZkZ1FZY0ZKYWJzM04yT2s2S2lWZmo3N0lkaXNYeUZ3eWsyMHFvX0sxS0NJanRjZndCYnkxWVljWXhjNU9SR1UwY19ZNmNRNEllRWNldkZRY2NSOFZ4WDdaRU4xa29ZNzVWNHBIZGpIWS1wd2xoYzE5NTlyeVVGQS1yVkVPdWJn?oc=5
- [Devdiscourse] Telangana: Owaisi alleges bid to delete 122 Muslim voters in Goshamahal; demands ECI action over fraudulent 'Form 7' filings - Devdiscourse (2026-10-06) - https://news.google.com/rss/articles/CBMiigJBVV95cUxPVS1CeWJadGtZSFBGZXRzNGxkVU5hLXp1TldJQXNsWXVPRU9oa056Y3RpRFdELVl4Rk83Q2hpZW83MXB5OFNnalRFMGRWeXVZZGZwOUhqWTRBa1NVSUNzeVZGQnZ3VHM0SXdhc0hOXzh1TWItbDBBd3FvWmZaSGYySXFrVTNZLWdFeDZJUFR5OVZZR1hHbmNQek1nU21DQTFBS1lTV3NkTjh0Y2hhN21lRmZKTGUtNGstazlIa2lnelBfWndncWZ6VHZya0M3T3VBX1FKZ0lnREpTRW5kbm41VURoRlpoVmFjajZhaC14SGZWWWs1ZGlKeVhFNUdzdkZNRVdTajk3QjNjUdIBigJBVV95cUxPVS1CeWJadGtZSFBGZXRzNGxkVU5hLXp1TldJQXNsWXVPRU9oa056Y3RpRFdELVl4Rk83Q2hpZW83MXB5OFNnalRFMGRWeXVZZGZwOUhqWTRBa1NVSUNzeVZGQnZ3VHM0SXdhc0hOXzh1TWItbDBBd3FvWmZaSGYySXFrVTNZLWdFeDZJUFR5OVZZR1hHbmNQek1nU21DQTFBS1lTV3NkTjh0Y2hhN21lRmZKTGUtNGstazlIa2lnelBfWndncWZ6VHZya0M3T3VBX1FKZ0lnREpTRW5kbm41VURoRlpoVmFjajZhaC14SGZWWWs1ZGlKeVhFNUdzdkZNRVdTajk3QjNjUQ?oc=5

### Domestic Military Use in Political Conflict
- Assessment: A civil complaint has been filed in federal court (D. Minnesota) naming multiple current and former federal officials. The complaint itself is an official record indicating that plaintiffs have asserted claims regarding potentially unlawful conduct by these defendants. However, without access to the complaint's substantive allegations, the severity cannot be determined beyond acknowledging that a legal action has been initiated. The filing is a real procedural event, but severity is limited to 1 because a complaint represents an allegation, not a proven occurrence, and the specific nature of the alleged conduct cannot be assessed from the docket summary alone.
- [courtlistener.com] **[official record]** Ganger v. Ross (2026-10-01) - https://www.courtlistener.com/docket/74901903/1/ganger-v-ross/

### Press Restrictions or Retaliation
- [Journalism Pakistan] Arrests and censorship tighten grip on global press - Journalism Pakistan (2026-10-04) - https://news.google.com/rss/articles/CBMijwFBVV95cUxNaVVISjFFTnN0Y2xkWWFtTExaU1dEOFJPc2o2QTlSQmlCYkpfYWtsa1lTUnMtMm5mbWR4RnVVZEZBZXgwZnBzdWlCakNlSmdkT2hhdTJmMlZLNmNvN21hb3pxRk85Z0dpSk1xOW5RNi11UW9DTFJvZVY2NlJGbDBiVTNMQmtaekctVVNrdVQxMA?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 16 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 1
- Evidence extraction: AI event extraction
- Confidence: **High**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
