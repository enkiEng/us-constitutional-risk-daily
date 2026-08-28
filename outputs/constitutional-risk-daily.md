# Constitutional Risk Dashboard (0-100)

- Generated: 2026-08-28 22:27:02 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **18 / 100** (Elevated Strain)
- Previous day delta: **-5.0**
- Delta vs 7-day average: **+5.5**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.33 | 1.79 |
| Judicial Independence and Rule of Law | 15 | 0.43 | 1.62 |
| Opposition Rights and Political Pluralism | 14 | 1.10 | 3.85 |
| Executive Constraints and Emergency Powers | 13 | 1.30 | 4.22 |
| Civil Service and Agency Independence | 10 | 1.65 | 4.12 |
| Civil Liberties and Information Environment | 10 | 0.82 | 2.06 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Independent Agency Capture | civil_service_integrity | 2.65 (Yellow) | ai | 0 | 2 |
| Legislative Bypass by Executive | executive_constraints | 2.30 (Yellow) | ai | 1 | 4 |
| Opposition Ballot Exclusion | opposition_pluralism | 2.00 (Yellow) | ai | 1 | 2 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.65 (Watch) | ai | 0 | 4 |
| Election Administration Capture | elections_transfer | 1.30 (Watch) | ai | 0 | 1 |
| Politicized Prosecution of Opposition | opposition_pluralism | 1.30 (Watch) | keyword | 0 | 0 |
| Targeted Jurisdiction Stripping | judiciary_rule_of_law | 1.30 (Watch) | keyword | 0 | 0 |

## Evidence Samples

### Independent Agency Capture
- [Briefs Finance] Fed Governor's Attorney Points to Trump's Home Claims in Removal Battle - Briefs Finance (2026-08-27) - https://news.google.com/rss/articles/CBMikgFBVV95cUxNV2tSZF9fc1BDcThrUGZoSGJnMXhqN1FpaXFoZnVHeDVjcmQ5R285UE1rNzRCeUhudlhvZHowdnFOWG1HZjVkb2dOMl9NemV4MmdYdlhKc1RLdEVva0twSFlYNDY1eXNfQkNlZy1qTzZuSWV1NlVYdTFESDg3a0RpR2Z1Ny1CN2R3MUx5YW90Y0FDUQ?oc=5
- [Newsmax] Lawyer for Fed's Cook Says There Are No Grounds for Dismissal - Newsmax (2026-08-26) - https://news.google.com/rss/articles/CBMiuAFBVV95cUxPRk90OWxIWFVoVkt6UmN2aXNWUUl6bEpoU1hwdko5RkJKQ3VnNEVxSkZ1MGEtTnJKYjlxV2FuVlpENld5S3BUcENzcXlYMWIteEZpdXFxVDlRTFg0cmh3S2FsaTg2MjRaLU05UFBhYml4bzhCTEtWcmZwMmlwZHltMXVidzFZZG5zbHlJMzRFVkltb0FLZjNQekUzazVnbEhNajlPQXlzMGJRSkM1SFQtNThNS3RsZWdw?oc=5

### Legislative Bypass by Executive
- Assessment: Item reports that a Trump executive order on birthright citizenship has been challenged in court and a judge has questioned its constitutionality, but the order remains in effect pending judicial resolution. This represents a real action: the executive has unilaterally altered birthright citizenship policy via order rather than legislation. However, the order is under active judicial review and has not been definitively upheld or struck down. The action is real and represents a shift of governance from statute to executive action, but the outcome remains contested. Severity is 2 because this is a confirmed action that has occurred and is in effect, though constitutionality is being litigated and the ultimate legal status is unsettled.
- [Law Commentary] Trump’s New Birthright Citizenship Order Stays in Place as Judge Questions Constitutionality - Law Commentary (2026-08-28) - https://news.google.com/rss/articles/CBMiygFBVV95cUxPT1M3a2diZTN2TEQ2dVNuTWJJbUs2aFMzNkhrc3RmclBUT3Q2bnlrSnlWSTNTX3lHMlNOU3BhZkFYMDE3VUNiUW03QmRDSF9EWkxNX0tfZ01qekhoYXFFSFdNLTNhR0ZxUnVNS0hKYnlieFJiVVlLMkc2c3JpQXdZMGY0SmlXbnJpSE0xUXpkME5TSUhpODRxV1VFdWRLR20zcWFiQ3dlbjFIUFNwZW0xTnpmMlRzS015V0ZpZG5Fdml2MUNKY1lyVjFB?oc=5

### Opposition Ballot Exclusion
- Assessment: A court ruling preventing the Iowa Libertarian Party from replacing candidates on the ballot for governor and Congress nominees is a real, judicially-ordered exclusion of opposition candidates from the ballot. This represents a credible, confirmed action (a court order) that removes opposition candidates from meaningful ballot participation. The action is narrow in scope (one party, one state, specific offices) and is subject to appeal, limiting severity to 2 rather than 3+. However, it is verifiable evidence that systematic removal has occurred through judicial order.
- [The Des Moines Register] Judge says Iowa Libertarians can't replace governor, Congress nominees - The Des Moines Register (2026-08-27) - https://news.google.com/rss/articles/CBMi7AFBVV95cUxPNTd6T0NGWjh6TVNJNUlLaGJoeTJTN0VFWjFneDdPV0RSaUkzMTFVOUpTd0xidmx5ZHVQRFhkemN3RUZla2lfbk5DaHVEbDB0N3lUMGRBNVZJeUxJak95cmQ1US1OeDI3b0Rfd09vUTVJdGJvQndLdWxwY1BMOXZzdWZhZ0hla1R2UWxaa051OFNMUE1nMW1talhKdTl4UC1DYWw1WGZ5b0VLRE5DdmJzekg1NjgzZmZoWDliaTJCWUYxbldJd1doOS1vS3JzclR6ekN3alZZSldCaDl0T2k4Y3BKaUQ3YXRycGpRYw?oc=5

### Civil Service Purge / Schedule F
- Assessment: This is an official Federal Register document confirming that OPM has issued a final rule titled 'Improving Performance, Accountability and Responsiveness in the Civil Service' (published February 6, 2026, effective March 9, 2026). The August 25, 2026 entry is a technical correction to that rule. The original February rule directly addresses civil service structure and performance accountability, consistent with Schedule F concerns about reclassification of career positions. As an issued final rule effective before this correction, it represents a material structural change to civil service rules. The correction itself confirms the underlying rule exists and operates. Severity is 2 (repeated/credible stress signal, real but contained action) rather than higher because the document excerpt does not detail the specific reclassification powers granted, only that such a rule has been issued and corrected. The fact that a major civil service reform rule exists and is being administratively refined constitutes verifiable evidence of civil service policy change, though the full scope of at-will reclassification authority is not detailed in this excerpt.
- [federalregister.gov] **[official record]** Improving Performance, Accountability and Responsiveness in the Civil Service, and Recruitment and Relocation Incentive Waivers; Correcting Amendments (2026-08-25) - https://www.federalregister.gov/documents/2026/08/25/2026-17334/improving-performance-accountability-and-responsiveness-in-the-civil-service-and-recruitment-and

### Press Restrictions or Retaliation
- [Civicus Monitor] Indonesia: Authorities target and vilify activists, block film screenings, crackdown on protests while impunity for violations continues - Civicus Monitor (2026-08-28) - https://news.google.com/rss/articles/CBMi_wFBVV95cUxPdC1ISmttRE1feE9pNTFtZlZRNXBmcm1UVVdRcExkRTNVNGROVDIyR0lOc0F6VHZSY1NwSTE3cVBRd1FYUjQ0OGxVUnRpcDVMYlVlRmRoZWs1MzhKQWFXTTYwUC1fQTg2NFRPdXRkVEJSX2ZBdnBCVG1iNVRCY2p2d3VIb1dkYkMxM0RSZERaaHZRc1RJM3oxNFpNQjZkM21LcW1NYjR4dmxQNUNCYmV1YmV4R2dmak5vUnRnUll6b3VFaEQ5MGdibW14VDd5c2VUbTV0aEh6bUFEcnJJaUxuRUFLT0J5akhIS2txZHJiX09KcE9VSHVDakpGa2szMGM?oc=5
- [Committee to Protect Journalists] The cost of truth: Inside Iran’s mounting media crackdown - Committee to Protect Journalists (2026-08-27) - https://news.google.com/rss/articles/CBMihwFBVV95cUxNMmN2X1ZFRmVIU2d0VUsza3VsbEctSXprZ0NiODVrQTg3UmxHV2FFaS0yMDNxRk16YmJQTDVpLUlJd1FxejJwbFdZWmxCYW1QUnJxUV85bHEzNU1hUkRpblRnZktEUy1NWmR2ZDJfUm1IQ0lITkk5NTJiN3FEYU5nS2ZxOVBrYWPSAYwBQVVfeXFMTUNsZGhFeGp5YmJFZTRCZzhWbHdrZFhTVjZVVjA3dW1iUmxrY3poX04zQ2xUOFJqS1FHUTJmY0F2bkJDeEU4Nk5aNndHMXh0bXE2UVM4NWR1QzhFRlNtR3g4N1d4eGVwc2JaeGtCaERzVXpGWlFsMzgtSTcySmd5R2lUajVnX0QxZjJQSjY?oc=5
- [Journalism Pakistan] The JournalismPakistan Global Media Brief | Edition 35 | August 28, 2026 - Journalism Pakistan (2026-08-28) - https://news.google.com/rss/articles/CBMipAFBVV95cUxONFZlaGQxbjhHYU1ZS3gwQmRNZEJNYzE4aXdCZjdwamdyU2hDQzdyQjhzOFl5U280RU9XeUw2UVpMNGVOMjhZbElWZmI1YXpiV0ZFTzM4YURCTGc3NDR6MUtIUlhtRDRlcGFmR3Npd21XdmZiOWVkRFh0d1NPX2VYTmxwTHV6dG4zeldXaTVPazUtcm9KUjA1eWE0Yk5NM1pkSEpjZQ?oc=5

## Data Quality

- Query feeds attempted: 23
- Query feeds successful: 23
- Query feeds failed: 0
- Primary-source lookups: 21 signals, 18 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 1
- Evidence extraction: AI event extraction
- Confidence: **Medium**
- Fetch errors:
  - independent_agency_capture: courtlistener: The read operation timed out

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
