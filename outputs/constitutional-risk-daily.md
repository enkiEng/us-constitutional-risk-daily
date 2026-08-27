# Constitutional Risk Dashboard (0-100)

- Generated: 2026-08-27 22:24:48 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **23 / 100** (Elevated Strain)
- Previous day delta: **+1.0**
- Delta vs 7-day average: **+12.7**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.65 | 3.57 |
| Judicial Independence and Rule of Law | 15 | 0.65 | 2.44 |
| Opposition Rights and Political Pluralism | 14 | 1.22 | 4.26 |
| Executive Constraints and Emergency Powers | 13 | 1.65 | 5.36 |
| Civil Service and Agency Independence | 10 | 2.00 | 5.00 |
| Civil Liberties and Information Environment | 10 | 1.00 | 2.50 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Independent Agency Capture | civil_service_integrity | 3.00 (Orange) | ai | 2 | 4 |
| Legislative Bypass by Executive | executive_constraints | 2.65 (Yellow) | ai | 0 | 3 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 3 |
| Opposition Ballot Exclusion | opposition_pluralism | 2.00 (Yellow) | ai | 1 | 2 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Election Administration Capture | elections_transfer | 1.65 (Watch) | ai | 0 | 4 |
| Politicized Prosecution of Opposition | opposition_pluralism | 1.65 (Watch) | ai | 0 | 1 |
| Targeted Jurisdiction Stripping | judiciary_rule_of_law | 1.65 (Watch) | keyword | 0 | 0 |

## Evidence Samples

### Independent Agency Capture
- Assessment: A Supreme Court ruling described as stripping federal agencies' independence and recharacterizing them as 'political arms of the president' constitutes a significant change to the legal status of independent agency safeguards. This appears to be a major judicial decision that materially weakens the structural independence of regulatory bodies. The framing indicates SCOTUS has altered doctrine concerning agency autonomy, which is a serious constitutional-stress event affecting the signal of independent agency capture. This is a confirmed high-severity judicial action altering agency independence protections.
- [Lexology] “Political arms of the president”: how SCOTUS is stripping US federal agencies’ independence - Lexology (2026-08-26) - https://news.google.com/rss/articles/CBMivwFBVV95cUxNdGVkbnlXUFkwZ0xiRjdmbEJPcmtKQVlmQnh5SDg0STZjMkZjZGNnMmg1R19zaFFFTFpOUHZ5MVdzUUNTVGl6SnJkTXFRVURUV0o3WW9HSlY0eHpEU0IwVTkyWDJ6Y3dQcEIzWXBobWtDREQtWmktTzAyeGotV3NTRG5NQ2FOa1lmZXNoS3d1TjNKVWhfS2N5Zm5yeHZWVVZvNV9HYk9TY09XTGN1ekpJWGwxLTdod19hdzZyam9GVQ?oc=5
- [courtlistener.com] **[official record]** Constitutionality of the Foreign Service Grievance Board's Oversight Authority (2026-08-20) - https://www.courtlistener.com/opinion/10954524/constitutionality-of-the-foreign-service-grievance-boards-oversight/

### Legislative Bypass by Executive
- [ColombiaOne.com] How Far Can De la Espriella Really Go in Dismantling Total Peace and the FARC Peace Accord? - ColombiaOne.com (2026-08-27) - https://news.google.com/rss/articles/CBMieEFVX3lxTE5TdnZHQ0NZUENnbG1FM2dWcnlxM3d2Z0theElBYmRlQ29taU15cEJUak11eFRuSnhhMGNHLUxHbV95WDJSZzhqak1TRi10TW94eHNTeUQyNG1remRNTmpYMFMxV1RUc1NaMGJyOGJ6Q0JjcFZvWnIycw?oc=5
- [NCHStats] Mail-In Voting Rules for the 2026 Midterms Remain Unclear After Two Major Court Rulings - NCHStats (2026-08-26) - https://news.google.com/rss/articles/CBMickFVX3lxTFByZW1WQ1puMUV1TVVtUFJ0cjdNejVQbjVrN25ybGpSZk51RTdSa2loTFQ1RnJBNy1sQURkR29FV2RQeGF0UXVMTzZrU2xPY1FnREs0RzFMZUotN1lJbzVJRTN6eElRVElwTTNMSF9zeWVJUQ?oc=5
- [news.meaww.com] Trump scores mail-ballot win, putting America's voting rules on the line - news.meaww.com (2026-08-26) - https://news.google.com/rss/articles/CBMimAFBVV95cUxNTl9TYlNEMFhoNk9sLWNDdGxReEhhNDdmUkZSMzMxX2FHeUNKRzJPX1AzdkRLX3ZpS3R0REZGZ1NsQ0VWXzVraWh2TkJZWlcyRG1UNEVxSUVrOWlVYlVvTlZPMFp6MUZQYkZlQ1luQnFBVVdPV3RUSmpjclVGOWRsV3hwQ0xOcFRxUDZJalhzUlEwVDFxaHpraw?oc=5

### Press Restrictions or Retaliation
- Assessment: Stars and Stripes journalists filed a lawsuit alleging retaliatory firings by the Pentagon, which is a credible, confirmed action alleging state retaliation against journalists. This is a real, documented stress signal—journalists have taken legal action claiming employment retaliation for their reporting work. While the allegations require adjudication and this is not yet a court-confirmed finding of wrongdoing, the lawsuit itself represents a verifiable state action (alleged retaliatory employment decisions) that raises legal risk and costs for independent reporting. This is a contained, serious signal (severity 2) rather than a structural constitutional failure.
- [cedarnews.net] Stars and Stripes Journalists Sue Pentagon Over Alleged Retaliatory Firings - cedarnews.net (2026-08-27) - https://news.google.com/rss/articles/CBMinwFBVV95cUxQMm80bVZFSi1TbkQ3UVlHczA3WTJmVHZWZTBabEYzcmJSWjA3SWptUl9FSmpHUmQydldEYmlQZ0x1Sl9MV0JKYmFVeFlCcW5sUGFQYjVFWjFpNWxIV29rcFd0amFfVWJCSlNuSFVwTGUtTk5hMGVlb0I3eVI4UWNHc0dxelFRS2lIMlFUZHRkVkdhWTFPdDRLd2xGUWFWQ1U?oc=5

### Opposition Ballot Exclusion
- Assessment: A court ruling preventing the Iowa Libertarian Party from replacing candidates on the ballot for governor and Congress nominees is a real, judicially-ordered exclusion of opposition candidates from the ballot. This represents a credible, confirmed action (a court order) that removes opposition candidates from meaningful ballot participation. The action is narrow in scope (one party, one state, specific offices) and is subject to appeal, limiting severity to 2 rather than 3+. However, it is verifiable evidence that systematic removal has occurred through judicial order.
- [The Des Moines Register] Judge says Iowa Libertarians can't replace governor, Congress nominees - The Des Moines Register (2026-08-27) - https://news.google.com/rss/articles/CBMi7AFBVV95cUxPNTd6T0NGWjh6TVNJNUlLaGJoeTJTN0VFWjFneDdPV0RSaUkzMTFVOUpTd0xidmx5ZHVQRFhkemN3RUZla2lfbk5DaHVEbDB0N3lUMGRBNVZJeUxJak95cmQ1US1OeDI3b0Rfd09vUTVJdGJvQndLdWxwY1BMOXZzdWZhZ0hla1R2UWxaa051OFNMUE1nMW1talhKdTl4UC1DYWw1WGZ5b0VLRE5DdmJzekg1NjgzZmZoWDliaTJCWUYxbldJd1doOS1vS3JzclR6ekN3alZZSldCaDl0T2k4Y3BKaUQ3YXRycGpRYw?oc=5

### Civil Service Purge / Schedule F
- Assessment: This is an official Federal Register document confirming that OPM has issued a final rule titled 'Improving Performance, Accountability and Responsiveness in the Civil Service' (published February 6, 2026, effective March 9, 2026). The August 25, 2026 entry is a technical correction to that rule. The original February rule directly addresses civil service structure and performance accountability, consistent with Schedule F concerns about reclassification of career positions. As an issued final rule effective before this correction, it represents a material structural change to civil service rules. The correction itself confirms the underlying rule exists and operates. Severity is 2 (repeated/credible stress signal, real but contained action) rather than higher because the document excerpt does not detail the specific reclassification powers granted, only that such a rule has been issued and corrected. The fact that a major civil service reform rule exists and is being administratively refined constitutes verifiable evidence of civil service policy change, though the full scope of at-will reclassification authority is not detailed in this excerpt.
- [federalregister.gov] **[official record]** Improving Performance, Accountability and Responsiveness in the Civil Service, and Recruitment and Relocation Incentive Waivers; Correcting Amendments (2026-08-25) - https://www.federalregister.gov/documents/2026/08/25/2026-17334/improving-performance-accountability-and-responsiveness-in-the-civil-service-and-recruitment-and

## Data Quality

- Query feeds attempted: 23
- Query feeds successful: 23
- Query feeds failed: 0
- Primary-source lookups: 21 signals, 22 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 2
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
