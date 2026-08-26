# Constitutional Risk Dashboard (0-100)

- Generated: 2026-08-26 13:26:05 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **22 / 100** (Elevated Strain)
- Previous day delta: **+12.0**
- Delta vs 7-day average: **+13.6**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 1.00 | 3.75 |
| Opposition Rights and Political Pluralism | 14 | 1.00 | 3.50 |
| Executive Constraints and Emergency Powers | 13 | 2.00 | 6.50 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Bypass by Executive | executive_constraints | 3.00 (Orange) | ai | 5 | 7 |
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 4 |
| Politicized Prosecution of Opposition | opposition_pluralism | 2.00 (Yellow) | ai | 2 | 2 |
| Targeted Jurisdiction Stripping | judiciary_rule_of_law | 2.00 (Yellow) | ai | 1 | 1 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 1 |
| Independent Agency Capture | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 1 |
| Emergency Powers Expansion | executive_constraints | 0.25 (Green) | keyword | 0 | 0 |

## Evidence Samples

### Legislative Bypass by Executive
- Assessment: Supreme Court has allowed the Trump administration to proceed with an executive order restricting mail-in voting without statutory authorization or legislative action. This represents a significant shift of electoral governance authority from statute to unilateral executive action, with direct constitutional implications for voting access. The Court's allowance means the order can take effect, constituting a real occurrence rather than a proposal. Severity 3 reflects confirmation of a serious action affecting fundamental constitutional rights (voting), though not yet a complete structural failure.
- [SCOTUSblog] Supreme Court allows Trump administration to move forward with order imposing restrictions on mail-in voting - SCOTUSblog (2026-08-24) - https://news.google.com/rss/articles/CBMizAFBVV95cUxQblFuM0lVVnk1ek05cENEdmp2YTdxclBnejRzM2J4RmgwNHp0Wm9KaFhWOTh5SVhncHZ0d19MQ1VLUWpmTk5KWHVoRnpjYlB1bVlJdkRORW8yaThCSm5Fc1o2MENqdnBxTkVESm9mOUdsVnU5LU83YzhJbjBXN0c3SlA3ZGdiZV8wS0EyaVppSWVLWmNnVHYwUkJoTnF5Q2FiWDREeHdVLVN0WVNpMjhmNkNkODZCSloxWl91WTZoUUp5YnFXWjhib0ZkbHc?oc=5
- [CBS News] Supreme Court allows Trump to implement key parts of order restricting mail voting ahead of midterms - CBS News (2026-08-24) - https://news.google.com/rss/articles/CBMiggFBVV95cUxQLVZTaUM5SDFJZUJEQTd6V2hOLWVNMlg5U1BkWFFWUGVQNmN1aWpMblE4TUhMSl9CeVNmSmZZX0VLRzJXYjd4ZDRYQkp4TWNVVkJSVXQwRlhkZFp1WnV0bkRkZGtNeXJieGVieEN0T3dEWW85WWNUQVVQVVFWbHJ1QzVn?oc=5
- [ABC News - Breaking News, Latest News and Videos] Supreme Court allows Trump to implement parts of his mail-in voting executive order - ABC News - Breaking News, Latest News and Videos (2026-08-24) - https://news.google.com/rss/articles/CBMigAFBVV95cUxQLUpWVmxZNkVNNGxlamhNRjkteVhjUVJNMXhDQ3Vyc3V3UkdTVEcyeUM0ZnEzTUlJQXRYMUZsNkZ5LTN5Q0VzWDFrVmVFSVlpOFBSaEpwa19qd0Q4SExzankxMEpIQjMxT2k5R0Z3emE0cDFCNng3V3lwVjBQUDg1NNIBhgFBVV95cUxOWGtmd1BpZ1U2QlJOeTZIcXhKMTVTOVFEZDJKcDJPS1NzX2NsOG1RT2w2TkpUMDkwTWY1QzlZcGt4LVlmNV9NZlFVUG04S0Y1U2hUSUdFSk5sUlFId1VsZzlnd1JvOGlWQnY2LThiN1J6cjZDSjdSWHd3elNWS3FpYWJqMXFnUQ?oc=5

### Election Administration Capture
- Assessment: A state canvassing board split along party lines, with Republican members voting to certify a ballot measure while Democratic members opposed, indicates partisan division in an election administration body responsible for ballot certification. This demonstrates partisanship in what should be a neutral administrative process, though it represents a contained instance of partisan voting on a specific measure rather than systematic structural capture. The severity is 2: credible, repeated stress signal of partisan behavior within election administration, but not yet a comprehensive loss of institutional neutrality.
- [facebook.com] The Board of State Canvassers' Republican members voted to send the "Americans for Citizen Voting" measure to the Nov. 4 ballot while the Democrats voted against certification. 📷 Photo by Ken Wiedemann, Getty Images - facebook.com (2026-08-25) - https://news.google.com/rss/articles/CBMi3wFBVV95cUxONndUS21ROTdMQVZhbWJwTVF0dTBjMFNtYjhvU01iM1JXbkZhS0pHdHd6V1Z6UWxhM1hIOEhmUmt4UnBSakl5aXRNTk93X192VlZsdXQwOFdvN1pMckdhY1VWbFRBOC1mRGtMWEpEUDl1V0FoZ05IU0FwcGhfS1RLeW9FWmtSdlJFR3p5cUY2ZzdEQk0tUmxJd0dvOGlvaktEUjBsZWtfejhKX1VIYlJBU19WWjlYWWtBQ3F6MC0wdGFuRkF1RmlCVTdCS09ma1ZwSFBOR1RWWHIzb2VCT1d3?oc=5

### Politicized Prosecution of Opposition
- Assessment: News report identifies that individuals including James Comey have been targeted by the Trump administration. This describes a real occurrence of selective enforcement targeting opposition/prior administration officials. However, without access to the full article details and specific charges/actions taken, severity is conservatively set at 2 (a credible stress signal of real action) rather than higher. The targeting of opposition figures by criminal enforcement represents material evidence of politicized prosecution signal, though the specific scope and legal basis require verification.
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-08-26) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk?oc=5
- [KTLA] Watchdog files bar complaint against Jeanine Pirro over bid to indict 6 Democratic lawmakers - KTLA (2026-08-25) - https://news.google.com/rss/articles/CBMi1gFBVV95cUxQMHM4WDhQWWgxU0h5ekZtbjdmMzZsSTM0UjFWTGR2WDB0Q0FWaDFEVFIySUN2U1N6Z3lUbzJxUUh6TXdoWWdYSHpuQmhDSG1HZ3Boa2pWQVdYdHNfbHI5OTlHcHRWRXROdzFDR19PVDZsc1NvSU9xcjRaYmt2Q1ZFMFVQWUQwZlltclByeGFsdG1hcl9SaWljWXFmSTRlcDNCYzM2aHlZQUJBdmxoVkx1WnQzcXc3Q2N0bUVLT2E1MGhZdTdiZ0txUTlZd05aUExTX1JmQUtB0gHbAUFVX3lxTE5GT1hRNXJ1bUFRVndrOVhQZ3pvZHlGVU9JanJORmg3am91Q2lTRmt2SFNuX0xIQmIwdkFiVjF3M201YURZVXl0UWJzd2pXRFBLT1ZqSlh4aHJlNXlkeTF3OUt3bkZBYmdBQjZYWHJDTzdIZlVBcERSYWhIbkdFVk1fUEg3M1IyYTFpRnVnMFFfSjJVQ09QcVk0YU1sM2pxUjl6MWVuSXppQjE1VVk4VlI3dzhFOTRrU1Y5YVpOQlhmUkZneWFPOHFoVFdwdi1EQlJWQm1vNFdNSHFFTQ?oc=5

### Targeted Jurisdiction Stripping
- Assessment: A Fifth Circuit decision holding that IRS penalty suits are beyond court review constitutes a real judicial action that strips federal courts of jurisdiction over a specific class of constitutional/statutory disputes. This is a verifiable court ruling (not a proposal or hypothetical) that removes judicial review authority from a particular category of cases. However, this appears to be a single appellate ruling rather than a systemic campaign to strip jurisdiction, and the severity is calibrated as a contained, credible stress signal (severity 2) rather than a structural failure. The decision has immediate legal effect—parties cannot now obtain court review of these penalties without a further appellate or legislative step—making it a real occurrence, not a proposal.
- [Law360] 5th Circ. Says IRS Penalty Suit Beyond Court Review - Law360 (2026-08-24) - https://news.google.com/rss/articles/CBMiugFBVV95cUxOd0tKT0FxQk5RajJCOEIzVENTb1l2RExUUDFTZTlvZ3lDSEE0LTYyRVoyTUUyTDh2ZEJkT2VQRXljT1pOV0dkQmEzMFZLdnFnalVRR3AyUXBFMGpFY0JaU09PTF8zeTgtWU1tUUhfZkwwbGJCUkV5d04yZmwyRV9RbWN3NGNxajV0ZXowM1FrTWtJTzJ1RURQQkNqOWlPa2cyaEVicUFOQ1BZUkVad1I5RGFyak4xblViNGfSAXNBVV95cUxNOEpjYzdTUmcybnc1dUI4RDdOT0xWNWVISm5sQXBmdXVRUmNCM2VpeGEwVTlSRFl5bFdMTkZoXzBSazlxeUh6U2t3a1hpOXJuZGdvc2ZqV3pfcmxqcEZIUFZGNVNoRmNaaW9hYXZhOFZnS1Fj?oc=5

### Civil Service Purge / Schedule F
- Assessment: This is an official Federal Register document confirming that OPM has issued a final rule titled 'Improving Performance, Accountability and Responsiveness in the Civil Service' (published February 6, 2026, effective March 9, 2026). The August 25, 2026 entry is a technical correction to that rule. The original February rule directly addresses civil service structure and performance accountability, consistent with Schedule F concerns about reclassification of career positions. As an issued final rule effective before this correction, it represents a material structural change to civil service rules. The correction itself confirms the underlying rule exists and operates. Severity is 2 (repeated/credible stress signal, real but contained action) rather than higher because the document excerpt does not detail the specific reclassification powers granted, only that such a rule has been issued and corrected. The fact that a major civil service reform rule exists and is being administratively refined constitutes verifiable evidence of civil service policy change, though the full scope of at-will reclassification authority is not detailed in this excerpt.
- [federalregister.gov] **[official record]** Improving Performance, Accountability and Responsiveness in the Civil Service, and Recruitment and Relocation Incentive Waivers; Correcting Amendments (2026-08-25) - https://www.federalregister.gov/documents/2026/08/25/2026-17334/improving-performance-accountability-and-responsiveness-in-the-civil-service-and-recruitment-and

## Data Quality

- Query feeds attempted: 23
- Query feeds successful: 23
- Query feeds failed: 0
- Primary-source lookups: 21 signals, 18 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 2
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
