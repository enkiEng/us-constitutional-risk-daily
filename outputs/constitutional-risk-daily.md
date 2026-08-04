# Constitutional Risk Dashboard (0-100)

- Generated: 2026-08-04 14:42:43 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **14 / 100** (Baseline Institutional Noise)
- Previous day delta: **+3.0**
- Delta vs 7-day average: **+3.9**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.65 | 2.27 |
| Executive Constraints and Emergency Powers | 13 | 0.00 | 0.00 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 1.00 | 2.00 |
| Federalism and Legislative Oversight | 8 | 1.00 | 2.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 4 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 3 | 0 |
| Security Sector Loyalty Tests | security_sector_neutrality | 2.00 (Yellow) | ai | 1 | 0 |
| Legislative Oversight Obstruction | federalism_oversight | 2.00 (Yellow) | ai | 1 | 0 |
| Opposition Ballot Exclusion | opposition_pluralism | 1.65 (Watch) | ai | 0 | 1 |

## Evidence Samples

### Election Administration Capture
- Assessment: This reports an allegation (via affidavit) that a Trump-appointed director of election security sparked a Georgia office raid. This represents a real action that has occurred—a raid of an election office—allegedly directed by a Trump administration official. While the severity is not extreme (no election was cancelled or overturned), this constitutes a credible signal of election administration being subject to partisan pressure from the executive. The involvement of a Trump administration official in directing action against a state election office suggests potential partisan capture or interference.
- [ABC News - Breaking News, Latest News and Videos] Trump director of election security sparked Georgia office raid, affidavit says - ABC News - Breaking News, Latest News and Videos (2026-08-03) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5

### Civil Service Purge / Schedule F
- Assessment: OPM has issued a final rule modifying RIF regulations to prioritize performance over tenure and length of service. This is a real, published regulatory action that materially changes federal personnel protections by reducing seniority-based safeguards. While presented as merit-based efficiency, the shift from tenure-protective RIF procedures to performance-based retention creates a concrete mechanism for politicizing career civil service. This is a contained but credible stress signal—a structural change to established civil-service protections, not a mass purge event or emergency action.
- [federalregister.gov] **[official record]** Reduction in Force (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15665/reduction-in-force
- [federalregister.gov] **[official record]** Streamlining Probationary and Trial Period Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15654/streamlining-probationary-and-trial-period-appeals
- [federalregister.gov] **[official record]** Suitability Action Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15650/suitability-action-appeals

### Security Sector Loyalty Tests
- Assessment: This is a final OPM regulation that removes the Merit Systems Protection Board (MSPB)—an independent adjudicative body—from appeals of suitability actions and consolidates that authority within OPM itself. Suitability determinations affect federal employment eligibility and can be used to screen personnel. Removing independent oversight of such determinations and concentrating appeals authority within the executive personnel office constitutes a material shift in internal review mechanisms that could enable partisan loyalty filters in federal personnel decisions. This is a confirmed structural change to a coercive-state institution's internal accountability, though it remains procedural rather than involving overt purges or open defiance of courts. Severity 2: real, confirmed, official action affecting institutional independence in personnel matters.
- [federalregister.gov] **[official record]** Suitability Action Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15650/suitability-action-appeals

### Legislative Oversight Obstruction
- Assessment: An official motion to quash third-party subpoenas filed by the Executive Office of the President represents a verifiable action to obstruct legislative fact-finding. The filing of a motion to quash subpoenas is a concrete legal action aimed at preventing disclosure of information to Congress or its agents. This constitutes a real occurrence of obstruction of legislative oversight, though the motion itself is a procedural challenge rather than an outright defiance of a court order or systematic campaign. The severity is 2 (repeated or credible stress signal—a real but contained action) rather than 3, because this is a single motion through the normal judicial process, not an open defiance or structural campaign to prevent oversight.
- [courtlistener.com] **[official record]** IN RE SUBPOENAS ON BORIS EPSHTEYN (2026-07-02) - https://www.courtlistener.com/docket/73690657/2/in-re-subpoenas-on-boris-epshteyn/

### Opposition Ballot Exclusion
- [The Hindu] Day before bypoll result, Congress suspends ex-Datia MLA Rajendra Bharti - The Hindu (2026-08-02) - https://news.google.com/rss/articles/CBMi3gFBVV95cUxQQWxIU2w4aWpEbmNXS1c1V29DaEJ6d2l4WEVEZHdPRF9GZTVKZ29GNTAtVmVwb1JjSF9pMjFYb2VXa2hPNHJ4YVVBdzNFaXpDT3A2Qzk5TjEwUEpRVUNldENGaGJZU1F2aWFxZzlYLTJhN1pnNlQxN2RhQk50VmhtQ0xTM3VnUmQtVVEzV2VjWjFuRndBSzJXTFhnd0pxTjBGTjlpOXl0WEdJZGlkUXhXR2xWZzhMMlNmMGVVNmh2Z2o1eXNEY2locnIxZzdDSnNlcmwwWFVyRnRrLUdjSEHSAeQBQVVfeXFMTzFnUVhpQzhGUW5uT1FDQllnSjdiRUwwdzhTb29sX2FDbEZ5dVc0aG9tdzdFWHZRenNIQU1FUzJRbjFicnpPcDIxYzBYaS1YMWV6cDZhMTg1b1E0MktGaTBBSTdybkdZZEFsdGZXSGdhajh5SUY2allsdTVNRmlGZVc2X0lxZ3hDM1JhMkNJRDhoZ1FvdnU1RGtlTUFtRy1fdi1OTW5KRFE4S0dVQ1dUdjNtMkhfTzRpcnQwZHVta2dMVjZ1S1dPMmYxSWszVFdrT0Exd2k0dEYydmpYRzFPYlF2b2ND?oc=5

## Data Quality

- Query feeds attempted: 22
- Query feeds successful: 22
- Query feeds failed: 0
- Primary-source lookups: 20 signals, 14 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 5
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
