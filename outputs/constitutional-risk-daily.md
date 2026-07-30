# Constitutional Risk Dashboard (0-100)

- Generated: 2026-07-30 14:36:00 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **9 / 100** (Baseline Institutional Noise)
- Previous day delta: **0.0**
- Delta vs 7-day average: **-0.7**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.65 | 3.57 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 1.00 | 3.50 |
| Executive Constraints and Emergency Powers | 13 | 0.65 | 2.11 |
| Civil Service and Agency Independence | 10 | 0.08 | 0.21 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Opposition Ballot Exclusion | opposition_pluralism | 2.00 (Yellow) | ai | 1 | 2 |
| Election Administration Capture | elections_transfer | 1.65 (Watch) | keyword | 0 | 0 |
| Legislative Bypass by Executive | executive_constraints | 1.65 (Watch) | keyword | 0 | 0 |
| Independent Agency Capture | civil_service_integrity | 0.25 (Green) | ai | 0 | 2 |
| Martial Law or Military Governance Language | executive_constraints | 0.25 (Green) | ai | 0 | 1 |

## Evidence Samples

### Opposition Ballot Exclusion
- Assessment: A Libertarian gubernatorial candidate was removed from the ballot in Iowa and is planning to appeal. This is a confirmed real occurrence of ballot exclusion of an opposition candidate. The fact that an appeal is being filed confirms the removal happened. However, without evidence of systematic, statewide, or coordinated removal of multiple opposition candidates, and given that legal challenge mechanisms appear available, this represents an isolated or contained action rather than structural failure. Severity 2: real but not yet confirmed as part of a systematic campaign.
- [Iowa Capital Dispatch] Iowa Libertarian gubernatorial candidate plans to file appeal in ballot removal case - Iowa Capital Dispatch (2026-07-29) - https://news.google.com/rss/articles/CBMixwFBVV95cUxPcmpTZGx4MkpaUW1Xb0FHX21iTS1rVk9PN1FDMlV5MzVNNlZOdmxKdGt5dFdwdnZfa195TzYyZERTdGRmaFgtdzIzUS1hT0NCZHdfTHlZSGNvR0tRTEFMWm5ielIwR1JNNjliSW5jZ2Y5WVdfZURCY1JBTkRoUjZzVHdMUEYzVnZpNF92Skk4aXhiNTFXTFRDcndlU2FfRUJ0UUZGSDdlMDUxc3QwUlNsQWI2akNGTGxyYmFHU3pEQXFRNFhHU2RF?oc=5

### Election Administration Capture
- No fresh evidence links in the current lookback window.
### Legislative Bypass by Executive
- No fresh evidence links in the current lookback window.
### Independent Agency Capture
- [The Regulatory Review] The Fate of Independent Adjudication and the Civil Service? - The Regulatory Review (2026-07-30) - https://news.google.com/rss/articles/CBMivAFBVV95cUxORGRPQWVFZXBvQmVHMHB0Z2I0XzF4RUdqZDl5Z1F1cndiQXRfQ1RrU0R1RDU1SUFyX2RCc05YX3k3YnZaa1dFc3ZVY1I2YkdzQTJZNm9hY0xJY1Y2N3YxcTQxSi02UzcwVk9UTUlKNlpCN2JxaXQzaUlrZkU4c1Etam8xUzYwb0g0dk1CTnhYWFhUNlZsS1BJN3RBNjdtdTFTRVF0R3p2TFdldWJETW9WYnFPRGxoYXRxV05sSg?oc=5
- [Gulf Today] AI has no future without credible regulation for sure - Gulf Today (2026-07-28) - https://news.google.com/rss/articles/CBMingFBVV95cUxNV0lBYVR0bFNvTjBFSGxiQ2dWMjJpN2ZOY0RxQ1dNLXRrTUh5X0oyVmNJOE05V2ZfTlU3MFhmd1QwWVdHSHhtUHRfUkZFdVYxT2U4VGZoSC1QVlhqMko4R2R4c2JZRWJjUi1ya3pRVVRsbGxrT0RoZDJScWRNbEt0a3JycjJBaW80RndSZHAzNUdvQUpFa0RQLXpFNVN1UQ?oc=5

### Martial Law or Military Governance Language
- [Судово-юридична газета] A woman waited three years for her husband: the court declared the soldier who disappeared near Bakhmut dead - Судово-юридична газета (2026-07-29) - https://news.google.com/rss/articles/CBMi2AFBVV95cUxPR0R3bzVmNTZpLVNiSUNPNFRfakhKY2thLUo2c1NGZW9mTEl6aXEzZXR1c2h2XzlKbF8yNjROLVFFQnJzS2VJOUtudm1ib1ZkRDkyOFp4QU9kQUFBS3lENEVab0tfcDRpZDdfazVaQU0yS3B6Qi1xaEdJT3NLdUJleGYzT0NwRzlpbEpfR3JuNmlZelFIaWpwRXBYTFFmaFhfVk1yMHJ0b0ZuYURUSG1nNUV0TF8tMERBVWFBVXJJTFlfUVpBSDRMeWpSRzN0Q0toaDJFT3hGbXU?oc=5

## Data Quality

- Query feeds attempted: 22
- Query feeds successful: 22
- Query feeds failed: 0
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
