# Constitutional Risk Dashboard (0-100)

- Generated: 2026-08-08 13:15:05 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **13 / 100** (Baseline Institutional Noise)
- Previous day delta: **-2.0**
- Delta vs 7-day average: **+0.4**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.15 | 0.82 |
| Judicial Independence and Rule of Law | 15 | 0.65 | 2.44 |
| Opposition Rights and Political Pluralism | 14 | 0.08 | 0.29 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 1.33 | 3.33 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 1.00 | 2.00 |
| Federalism and Legislative Oversight | 8 | 0.47 | 0.95 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Independent Agency Capture | civil_service_integrity | 2.00 (Yellow) | ai | 10 | 14 |
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 3 | 8 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 3 | 0 |
| Security Sector Loyalty Tests | security_sector_neutrality | 2.00 (Yellow) | ai | 1 | 0 |
| Judge Intimidation Campaign | judiciary_rule_of_law | 1.65 (Watch) | ai | 0 | 1 |
| Legislative Oversight Obstruction | federalism_oversight | 0.95 (Watch) | keyword | 0 | 0 |
| Election Administration Capture | elections_transfer | 0.60 (Green) | keyword | 0 | 0 |
| Opposition Ballot Exclusion | opposition_pluralism | 0.25 (Green) | keyword | 0 | 0 |

## Evidence Samples

### Independent Agency Capture
- Assessment: Washington Post reports Trump 'renews effort' to fire Cook after a Supreme Court ruling blocked an earlier attempt. This indicates a sustained, recurring action following judicial rebuke. A president actively pursuing removal of an independent agency official after a court order against a prior removal attempt is concrete evidence of pressure on agency independence. Severity 2: repeated and credible stress signal.
- [The Washington Post] Trump renews effort to fire Fed governor Lisa Cook after Supreme Court ruling - The Washington Post (2026-08-08) - https://news.google.com/rss/articles/CBMiuAFBVV95cUxOMHV6QkY1anVqMi1FVnVua1ZldlVkbHJROERfUFItOF8tOG9KT3cxOEJadlJ5emhRZHRHaGtPWlNOUXZ0Rm5uLTdpNjlTR3k2TFFhQkw1c0UyTVNtd2FfVE9laXRNZHhkRk55NkVJTEZfeUdBSk5RT0drcTZpSFZBZU9ZZlRwcnFRdUlVTURIQVRobHlVeDVoLUtWeGUzTlNPSzlEcTRuRDRKSmVyeFlGRGRQa0RTLTZ2?oc=5
- [NBC Boston] Trump administration moves ahead with efforts to fire Federal Reserve governor Lisa Cook - NBC Boston (2026-08-07) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxPQWQ4clBPeTM1bXp3WjFMSGg2NndqZlZEdm4yUEN3WTZOTGdiNnhFU052d3FVT0x1VHVrQ2hUTEFud1NYblNFZFhqb1YySWRKaE9lQnRVNGl2X1l5aVEwM0REM08wdGZRNXUxbDFGOU1DQzg3THdlSHhaaGhVQ0NEYmpzenIxRFM3TGM4YVNkZy1MdXh2ellGQUJ1bl9tcUVuZVo3Skx3d0pjZ9IBsgFBVV95cUxNaVZOeGFhRzdZRTJad2daWkJnUFRYZEpEWnpxZDNLMXFDaHA0c2Q0MW1pN3Zjc2JPV1JWREpNYWpTeWh2NG9pS1dlX0hONm44elZkWjVPZnpDUEVNb1VhSm9LcU0xMWhjdFp6TXhhVTg1cUtWd1hEMnFjbWhhUGFhQ2N1V1o2VFB5MTVzQkt6ZlNQOV8zVHhlaXhZNzFIS2hMVTYtTmVWTjgwQ080ZWZoaEpB?oc=5
- [Yahoo] Trump Restarts Bid To Fire Fed Gov. Lisa Cook After SCOTUS Ruling - Yahoo (2026-08-07) - https://news.google.com/rss/articles/CBMikAFBVV95cUxPRHdtWkRwY3lvWjlCQU8zcjRXNGM1RmRiTEM3RW9pWTFqZHdXMHk4d0hGdUxfVWRHQVNWMTdRMjVfTjVaVFh6U1lwT2w2WGFMM3RGR1o1QXI1ZFVZMVVWMkhZZlZhVHJEYWdNNTVnZnc1czYyQTY0NWc1MWVTdS1XSzNwXzd4dEkxNzI1TUZZTGo?oc=5

### Legislative Bypass by Executive
- Assessment: Trump has signed a birthright citizenship order, which attempts to modify citizenship law unilaterally via executive action rather than through statutory amendment. This is a real action (not hypothetical) that shifts a governance matter from legislative to executive domain. However, the action is under legal challenge and its enforceability remains uncertain, preventing severity 3+ assignment. Severity 2 reflects a real but contested executive action in a material policy domain.
- [SCOTUSblog] Trump signs new birthright citizenship order, ballroom dispute likely headed to Supreme Court - SCOTUSblog (2026-08-07) - https://news.google.com/rss/articles/CBMixwFBVV95cUxOLXZrc0s4bkJMdjBJZVhlQk8yT05BVEZiWkYtYXlKV09Db29hTW55M0R2SnJfTEloODE5c0RYUWFnQURBRU5iNVRRMjMzNnFqZExQanhWbkFXcXRfNGZKNUdCdS1UemVPQmxLb1ZFV3lzRFJQbll1dmN4NVpBdDNoQ0toUjVkaTFlbGp4MGRuWm96NWR0TF9sYVNWU3E5dzNnMzdrRXI2NG9aalgxVnBzQjR3UzVWbDFPZDRLczU2eWFsUHN0anBF?oc=5
- [Reuters] Trump signs orders to limit US birthright citizenship, despite Supreme Court ruling - Reuters (2026-08-06) - https://news.google.com/rss/articles/CBMinAFBVV95cUxNQlBIVEJ3RmxwWHB3RElBYnBYVGdvRjZUUjYzbmJ6UW5wU0E3SlQtV1g3Uk5zQzFlelZMUWo5UExUelBUMnZQY0pibWx1OHBLN1FtTDBJY1Q3WUFXMmNScndrNUtleC1ucVEtdDdMUy1oR2RTeVpaN09heGUtLUk0UFNfT25Lb0swemZNVjQtbHRoLWh3anVQOTF2WGU?oc=5
- [Legal Service India] Learning Resources v. Trump: Supreme Court Limits Presidential Tariff Power Under IEEPA - Legal Service India (2026-08-08) - https://news.google.com/rss/articles/CBMipwFBVV95cUxQLWs0M1ZPbWlUUS00eEI5bGpxdDI5MTl6bDNvODZJdHpTdEdvazZpSVhnbHNOTGFqTjZQTk84Y0tqTGtDUi1ueW1LWGFMTEJCZlMyWHdYdXVmNUV0STdJcVNtbXRYbVNDZVhBNzdfQTgtdnVXUktLQUpVcEtUMmZsUHJpWXNzZExfcEV3VE9Fcy1kUTNPSXNjQnFTdHNIUUpnOVJNZXRHNA?oc=5

### Civil Service Purge / Schedule F
- Assessment: OPM has issued a final rule modifying RIF regulations to prioritize performance over tenure and length of service. This is a real, published regulatory action that materially changes federal personnel protections by reducing seniority-based safeguards. While presented as merit-based efficiency, the shift from tenure-protective RIF procedures to performance-based retention creates a concrete mechanism for politicizing career civil service. This is a contained but credible stress signal—a structural change to established civil-service protections, not a mass purge event or emergency action.
- [federalregister.gov] **[official record]** Reduction in Force (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15665/reduction-in-force
- [federalregister.gov] **[official record]** Streamlining Probationary and Trial Period Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15654/streamlining-probationary-and-trial-period-appeals
- [federalregister.gov] **[official record]** Suitability Action Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15650/suitability-action-appeals

### Security Sector Loyalty Tests
- Assessment: This is a final OPM regulation that removes the Merit Systems Protection Board (MSPB)—an independent adjudicative body—from appeals of suitability actions and consolidates that authority within OPM itself. Suitability determinations affect federal employment eligibility and can be used to screen personnel. Removing independent oversight of such determinations and concentrating appeals authority within the executive personnel office constitutes a material shift in internal review mechanisms that could enable partisan loyalty filters in federal personnel decisions. This is a confirmed structural change to a coercive-state institution's internal accountability, though it remains procedural rather than involving overt purges or open defiance of courts. Severity 2: real, confirmed, official action affecting institutional independence in personnel matters.
- [federalregister.gov] **[official record]** Suitability Action Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15650/suitability-action-appeals

### Judge Intimidation Campaign
- [The New York Times] The Trump Administration Has Been Sued More Than 750 Times. Track These Cases. - The New York Times (2026-08-06) - https://news.google.com/rss/articles/CBMihAFBVV95cUxQc1cyTkxZUThGOUZLcjJOb3l0T1YyTDZURFBjNVNscEI5TDlUOF9FVmRLMDdEYkZpMEtIRTl2b2NfOGVqRUlvVHBlaHJyTUVYWDhqUi10aEM3U3RpazVzamtMcHpWUkY5cTNYQjlpRmpTZTAyY2d5Rl9WVHlfbHR0NUVxT1c?oc=5

## Data Quality

- Query feeds attempted: 22
- Query feeds successful: 22
- Query feeds failed: 0
- Primary-source lookups: 20 signals, 19 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 4
- Evidence extraction: AI event extraction
- Confidence: **High**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
