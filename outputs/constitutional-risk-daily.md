# Constitutional Risk Dashboard (0-100)

- Generated: 2026-08-06 14:38:14 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **13 / 100** (Baseline Institutional Noise)
- Previous day delta: **+1.0**
- Delta vs 7-day average: **+1.6**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.33 | 1.79 |
| Judicial Independence and Rule of Law | 15 | 1.00 | 3.75 |
| Opposition Rights and Political Pluralism | 14 | 0.32 | 1.11 |
| Executive Constraints and Emergency Powers | 13 | 0.00 | 0.00 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 1.00 | 2.00 |
| Federalism and Legislative Oversight | 8 | 0.82 | 1.65 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Judge Intimidation Campaign | judiciary_rule_of_law | 2.00 (Yellow) | ai | 1 | 2 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 3 | 0 |
| Security Sector Loyalty Tests | security_sector_neutrality | 2.00 (Yellow) | ai | 1 | 0 |
| Legislative Oversight Obstruction | federalism_oversight | 1.65 (Watch) | keyword | 0 | 0 |
| Election Administration Capture | elections_transfer | 1.30 (Watch) | ai | 0 | 3 |
| Opposition Ballot Exclusion | opposition_pluralism | 0.95 (Watch) | keyword | 0 | 0 |

## Evidence Samples

### Judge Intimidation Campaign
- Assessment: Article reports that a federal judge (John McConnell) received death threats following a ruling against Trump regarding a funding freeze case. Death threats constitute a form of intimidation directed at a judge for an adverse ruling. However, severity is 2 (repeated/credible but contained signal) rather than 3, as the threats appear to originate from unidentified private actors rather than from an official sustained campaign or official pressure. No evidence is presented that the threats constitute an organized or sustained official intimidation campaign, which would be required for severity 3+.
- [The Sunday Guardian] Who is Judge John McConnell? Federal Judge Who Received Death Threats After Blocking Trump’s Funding Freeze Case — Daughter, Wife, Net Worth and Ruling Against Trump - The Sunday Guardian (2026-08-05) - https://news.google.com/rss/articles/CBMiqwJBVV95cUxObUlzeUZoTzVsRTVJb0gzTkVmTm5vcDBFVDBLdm43LTYtN1pUU01YY3dWeHRtZURIcFF0SHo4dHpOUFlEd3ZGLUEtTE56OHF1MENQUzdXd1l6R0E0c2Uzc1pjQnZRbWFPWG5zVjVza2dFMzY2azdDSjhTZG1jRjN6NXRUWGROM3FiR214cW41NlFWQmFaX0RzMXZfSC1CX0E3Q1ZQSDZsX0I0QXlXSi1NcnZRS2tZMk1VUXpYZjZ1VU1BalBMZjN3MWZtYlJhZ0duei1yVW9LN01vOXpXdEJBVDB4bzk2S3VSRG5vWi13QXUweWhDTHpPRC1KZDN3Q0p1cHpXWTZVa0k2NFNDRmNOb0hhSE1YdDlqaVFpcGZKTTJmWHlFRGRQTGhhb9IBsAJBVV95cUxOZWZRLS1ZZUZ1RGRvdmsyaXk2M3ZjS2FsUXNzRGRDbTJFeDViRlJya0dKV3dZekgxTFNxVHpLQVg2dEs5cGdMT1pjQUdSODIzbkhYZldSUXN4emVXSGpQblBlREFsWDZDMG54SFR3aU5uejBMdzBoSUV0b0ZQcThmYWFCdGtUMzN4SkZOQXVKMlBMV1RsMFJoTDNIZE4tYldTbkVyNV90MzBCT2kxYy1mZ1pDQWlQdkxhNzJpSVJvS19fNnd2bFFmOEROQW1fRUlBNXpPS2FsdVp5a1JkckpvX3NmZHktS09pT1VZalVKZnpXREUtYUkzUXcyaElUclB1UDF5ckdHNUpGQXJoMEpLTTZkUWtIWmNlTG9DU0g3VEpmUlIxQWxnT01RdERVT3lj?oc=5

### Civil Service Purge / Schedule F
- Assessment: OPM has issued a final rule modifying RIF regulations to prioritize performance over tenure and length of service. This is a real, published regulatory action that materially changes federal personnel protections by reducing seniority-based safeguards. While presented as merit-based efficiency, the shift from tenure-protective RIF procedures to performance-based retention creates a concrete mechanism for politicizing career civil service. This is a contained but credible stress signal—a structural change to established civil-service protections, not a mass purge event or emergency action.
- [federalregister.gov] **[official record]** Reduction in Force (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15665/reduction-in-force
- [federalregister.gov] **[official record]** Streamlining Probationary and Trial Period Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15654/streamlining-probationary-and-trial-period-appeals
- [federalregister.gov] **[official record]** Suitability Action Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15650/suitability-action-appeals

### Security Sector Loyalty Tests
- Assessment: This is a final OPM regulation that removes the Merit Systems Protection Board (MSPB)—an independent adjudicative body—from appeals of suitability actions and consolidates that authority within OPM itself. Suitability determinations affect federal employment eligibility and can be used to screen personnel. Removing independent oversight of such determinations and concentrating appeals authority within the executive personnel office constitutes a material shift in internal review mechanisms that could enable partisan loyalty filters in federal personnel decisions. This is a confirmed structural change to a coercive-state institution's internal accountability, though it remains procedural rather than involving overt purges or open defiance of courts. Severity 2: real, confirmed, official action affecting institutional independence in personnel matters.
- [federalregister.gov] **[official record]** Suitability Action Appeals (2026-08-03) - https://www.federalregister.gov/documents/2026/08/03/2026-15650/suitability-action-appeals

### Legislative Oversight Obstruction
- No fresh evidence links in the current lookback window.
### Election Administration Capture
- [carolinajournal.com] Stein criticizes appointment, election law changes - carolinajournal.com (2026-08-04) - https://news.google.com/rss/articles/CBMihwFBVV95cUxPVkdQdFV2dUZUbkhLd2U4eEtWdm1KYmFETWJQNW9iMFBBWDI4dmJMb2pFNG93UWJJV3l6U3JrdGhwZC1iLWduVjdFcVY3eW55UFdwMnBTVkNDdFlZRmNpaWp1QzZqcHZUcV92c0Y2NmZjUEo2dFZfVlVteE5BVXN4bDExb3EzWXM?oc=5
- [PBS] Live Results: Kansas midterm primaries - PBS (2026-08-04) - https://news.google.com/rss/articles/CBMigAFBVV95cUxPVjY5ZXBYOGdvQ3NkLTVHUXFjdm5CbUprWTJwMHFtM3QwRGZ5ZXBsajhyM2t4VmhkeGlfYVZzQVVOTUcwTW5vWDRwNmtzZHc2ZUV1WWo2bUl3WmN5QnBDODlkbnVNRm5vcUpUSVExNFNGRld0a2pnYXV0Uk81NjF2RdIBhgFBVV95cUxNWjA2WHMwYnZreHZxZUVNQThGWEdSb3BnOEIxWXNuTV9qU0c4NW5pSE1TMGNTd3VOVmh3eVRqVjZva3Bxem83YWQ5c0JYS2MwQkhxbGl0dFBudlJ6dDFTX0IxdXB1bDdOZF8zSVA2REZjWDB4MERwX1p1WENXRnFUR0d4WWJVUQ?oc=5
- [Zeteo | Substack] Here Are 19 - Yes, 19! - Ways Trump and Republicans Are Plotting to Rig and Steal the Midterm Elections - Zeteo | Substack (2026-08-04) - https://news.google.com/rss/articles/CBMiY0FVX3lxTE9ZdDdMQW5GM21ra3hOcllwUm1uVlNOSUtrSmhya2JTMU13d2c5TF9SdGdPMVJ2ZUUtZXU2cThWSExYQldNSGtlZWF6bnJxSzlaU21Dc3VyZUhubmJ6dDFWTFRfcw?oc=5

## Data Quality

- Query feeds attempted: 22
- Query feeds successful: 22
- Query feeds failed: 0
- Primary-source lookups: 20 signals, 17 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 4
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
