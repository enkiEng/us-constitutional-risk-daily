# Constitutional Risk Dashboard (0-100)

- Generated: 2026-08-10 13:48:19 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **9 / 100** (Baseline Institutional Noise)
- Previous day delta: **-2.0**
- Delta vs 7-day average: **-3.5**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.00 | 0.00 |
| Judicial Independence and Rule of Law | 15 | 0.32 | 1.19 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.65 | 2.11 |
| Civil Service and Agency Independence | 10 | 1.33 | 3.33 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 1.00 | 2.00 |
| Federalism and Legislative Oversight | 8 | 0.12 | 0.25 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Independent Agency Capture | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 3 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 3 | 0 |
| Security Sector Loyalty Tests | security_sector_neutrality | 2.00 (Yellow) | ai | 1 | 0 |
| Legislative Bypass by Executive | executive_constraints | 1.65 (Watch) | ai | 0 | 3 |
| Judge Intimidation Campaign | judiciary_rule_of_law | 0.95 (Watch) | ai | 0 | 1 |
| Legislative Oversight Obstruction | federalism_oversight | 0.25 (Green) | keyword | 0 | 0 |

## Evidence Samples

### Independent Agency Capture
- Assessment: A renewed attempt to remove a Federal Reserve Governor after a court blocked the first effort represents an action to weaken independence of a regulatory agency. However, the summary indicates a court has already blocked a prior attempt, suggesting legal safeguards are functioning. The renewal itself is a real action (not hypothetical), but severity remains 2 (contained, repeated stress) rather than 3 because the court has already intervened and there is no indication the removal succeeded or that the court order was defied.
- [eciks.org] Trump renews effort to remove Fed Governor Lisa Cook after court blocked first - eciks.org (2026-08-08) - https://news.google.com/rss/articles/CBMiYEFVX3lxTE4zRDFUM1pHYU0xXzh0NjhObDB3MFc0dnZXcmRCRURfNzBQdTA2eGtSeXFKNEUwSVZhcTMwcmxLMWVRVjRfN2g0b1hSc1Ewc2RIZ2lTN3l3VHdmeWI0OFNlMA?oc=5

### Civil Service Purge / Schedule F
- Assessment: OPM has issued a final rule modifying RIF regulations to prioritize performance over tenure and length of service. This is a real, published regulatory action that materially changes federal personnel protections by reducing seniority-based safeguards. While presented as merit-based efficiency, the shift from tenure-protective RIF procedures to performance-based retention creates a concrete mechanism for politicizing career civil service. This is a contained but credible stress signal—a structural change to established civil-service protections, not a mass purge event or emergency action.
- [federalregister.gov] **[official record]** Reduction in Force (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15665/reduction-in-force
- [federalregister.gov] **[official record]** Streamlining Probationary and Trial Period Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15654/streamlining-probationary-and-trial-period-appeals
- [federalregister.gov] **[official record]** Suitability Action Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15650/suitability-action-appeals

### Security Sector Loyalty Tests
- Assessment: This is a final OPM regulation that removes the Merit Systems Protection Board (MSPB)—an independent adjudicative body—from appeals of suitability actions and consolidates that authority within OPM itself. Suitability determinations affect federal employment eligibility and can be used to screen personnel. Removing independent oversight of such determinations and concentrating appeals authority within the executive personnel office constitutes a material shift in internal review mechanisms that could enable partisan loyalty filters in federal personnel decisions. This is a confirmed structural change to a coercive-state institution's internal accountability, though it remains procedural rather than involving overt purges or open defiance of courts. Severity 2: real, confirmed, official action affecting institutional independence in personnel matters.
- [federalregister.gov] **[official record]** Suitability Action Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15650/suitability-action-appeals

### Legislative Bypass by Executive
- [NewsBreak: Local News & Alerts] 7 Limits on Trump’s Presidential Power That Even the White House Cannot Ignore - NewsBreak: Local News & Alerts (2026-08-09) - https://news.google.com/rss/articles/CBMi5AFBVV95cUxPN05aTXhjTzVhQXd6ZFM0TzF1WTZTRm5UUS0yalhmZFJsNGNJcjJOV29hVjV5UmdxalEtS2RWblN4ZEhfSFRUa3FlTU93ZzdrVDgxVFNHdTBMeUlncVI1eW9pbVIxTjg5MUQwdmdfZjRPeGNjSVREZ2JFVl9ydUpNa2ZEY3ZHeWZvcUtsaFZaY2d3dWc1aXRwcWdzTVc0SmRudThsZ3duYkp0aHNVc1U4YW5nNHpzMm0zVy02WFQ3dzRhSWszOEhleWRhY3NWbEdfbzNvUUxNWDFOTmRwdWcxZmVzbWM?oc=5
- [Free Press Journal] US Appeals Court Blocks Trump’s $400 Million White House Ballroom Project Pending Congressional Approval - Free Press Journal (2026-08-08) - https://news.google.com/rss/articles/CBMi1wFBVV95cUxNLXdWUk8tdTNaRTdwRXJHQld6R1B6YlBtZTFvX3l4aWVKUWs3Q3lSNi1CS2tEZkZUd1FObnZfRktQV1RnOHRPSG5aUVg5dThVaU5ZZWdud3Q1RmtkZjRsdHk4YkxsWWRTSlA5SGs3cnhoRDJMRHpmNkExUmtGelkwYUZmVllOUS1JOU92cVByV2NoQzNHNTBPaVh6dzhuUVpRenZDZDhtNE5ra0RWcW9NZlRnby1IT05QLUZpZS1qeUN5YlBkNjdIRVFVODRaMDVHS2M5VlN5d9IB3AFBVV95cUxOSTNVdDF0WEV1WnhMSXlLRHRzUnZhSW5HU1FRU21vNHdzUElPOFhzVzV2a2lTbm96eThWVXY3eUJmYTk0bWlCNEQ4ZlFhTElBT0k2ZzhFNmRUUUFGVzl0T1FfazNhcks4X2UzX0ZNYUItNW94TEVBNTY4TFBLaEJTRGZNRVdMcXV3R3pRMXd4LXh1dTJvU3RWVlNhdldPQi1iUjhpUVduRGFPZmNsUHh3RGFva2pRanhoTlN2emtMRmtFT1BYRFZ0Y3pmeTJmamlVRGlsSE90eWFtOXp0?oc=5
- [Dainik Jagran MP CG] Trump Names Will Scharf as New White House Counsel - Dainik Jagran MP CG (2026-08-10) - https://news.google.com/rss/articles/CBMi0gFBVV95cUxQQnBybVdockMtMnNXeWxMODVpYm1LcFZmenBqNFRyeXJpdjJERUZ5bXdLSGM3Qmo1RHVqMjNRVkdSWHh1RXJDd1dvLWdaZHVDeWJ0T0lqV2k3cmI2N0M1UjBkdFM2YnlYVWN3SElLTTNDQks0eDM5aE1zTzE0REJjLWZISGxBUXBLcWNSemduTHFOUk14dHllQWc4cnpGTlhnX0dfaFFnOXB0NnZDVVB2b0dGRlpkQjlKenItTU9LUDFvd3FINFZldzBqdGdLbW9QcVE?oc=5

### Judge Intimidation Campaign
- [EL PAÍS English] Trump tightens his grip on the US justice system - EL PAÍS English (2026-08-10) - https://news.google.com/rss/articles/CBMimwFBVV95cUxOTFVpS09oOWo1bWNXQXhkdEZQVUdqak02RjVvaEZSN2lJa1cwWGJJTFp6eEZuZm5NTlROd255VE1XLTF0TVJKOEFsNGFoZTBKZU4wOGwwejNCVndZc1c4MDFNS0pKM0FiOGJ4Sm1QQnJibHFLQnR0MUxSOVVEX091RzhXdVhxdm92eXJLZ0k4Q2pXLXI2bV9VRlN2MNIBrwFBVV95cUxQdkJ3Z3g2cHdKTlBadVZzUFg1TEZGVnctbnpfdWxmOVZNLWdJbFhyZkdXRS1PdFVlZG5tempRbXgyRTZ5SWpVa1lxMGthcTVlajZscWVaY3ljckNNZE1MMHlZWE91VnNEN2lDQ2dFQUJhZHlCdDNkQzFWR1lQM3hOWVMxNGtmZmhHaTREQnlKYkl1ZkxQTUpPdFp5dW53cGlKeXhNa1RweE5Eb0lxSWNz?oc=5

## Data Quality

- Query feeds attempted: 22
- Query feeds successful: 22
- Query feeds failed: 0
- Primary-source lookups: 20 signals, 19 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 4
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
