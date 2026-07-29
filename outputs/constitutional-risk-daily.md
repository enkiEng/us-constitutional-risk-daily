# Constitutional Risk Dashboard (0-100)

- Generated: 2026-07-29 14:33:36 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **9 / 100** (Baseline Institutional Noise)
- Previous day delta: **+5.0**
- Delta vs 7-day average: **-1.5**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.00 | 5.50 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.00 | 3.25 |
| Civil Service and Agency Independence | 10 | 0.20 | 0.50 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 1 | 4 |
| Election Administration Capture | elections_transfer | 2.00 (Yellow) | ai | 1 | 1 |
| Independent Agency Capture | civil_service_integrity | 0.60 (Green) | ai | 0 | 6 |
| Martial Law or Military Governance Language | executive_constraints | 0.60 (Green) | keyword | 0 | 0 |

## Evidence Samples

### Legislative Bypass by Executive
- Assessment: Corroborating report of the same executive petition to revive mail-in voting restrictions. Describes the same administration action as item [0]. The framing of 'revive' suggests a prior order was blocked, which is consistent with item [2]. This is a real, documented attempt at executive action on electoral policy that bypasses legislative process.
- [The Maine Wire] Trump Administration Asks Supreme Court to Revive Mail-In Voting Order Ahead of Midterms - The Maine Wire (2026-07-28) - https://news.google.com/rss/articles/CBMixAFBVV95cUxQdG4xQnZZOHF6UmZ0YUVJWnhLa1JaM1prZUxjS21KNVNhMllLakprUy1hbVRWRnFpeGpleGZqYzI1SU1iR0I1amR1cWpmNkVWWGVzVnQ3V2dLMms0czJGSTdSNUVZc2pBbXRvWGtLUzNlUFh5US0wQXlIMlVocXlJSUlfNmxZLU1qdjZLa2h2azdwUzJoNFN4dWJjaElNa2NhSVpUSV9DMzhoMDVFVk1sc0VoNW5PVHdtNGIxZ1BwZUI2eG9y?oc=5

### Election Administration Capture
- Assessment: A state legislature voting to shorten early voting and expand voter purges represents a real action that moves election administration toward partisan control by restricting voter access and participation mechanisms. This is a credible, documented legislative action. However, without evidence that the measure represents systematic capture of the entire election administration apparatus or defiance of courts, and given that legislative changes to voting rules, while potentially contentious, remain within formal legal processes, this constitutes a real but contained signal rather than a systemic failure. Severity 2 reflects that this is a confirmed action with partisan electoral implications, but not yet a structural breakdown of election administration neutrality.
- [WRAL] NC Senate votes to shorten early voting, purge more voters - WRAL (2026-07-28) - https://news.google.com/rss/articles/CBMixgFBVV95cUxPbF84WFJQUHdLSU9fNFJrR2FoN2NBYUdDOGZQNDYxNnhIMGlBTUZlSGxpeGVaRlNRVWo4RlBpN3M3TGkzakFpZVdSeVFOak1HM1V3bXNQU0JpdUxoVDFpYnFiZDU2QlBTa0tDeENNZ0RKQ3hzaUJna2dremlLOFNhQm1MTUoyUXVvMkVpbDJMSmppTXRtdnVRNmQ3UW1kbmJGSDVnWnJ2b202TTEyVUU0NnU1Rng5QV9TUnBMX1FhVEhwU1Y0UXc?oc=5

### Independent Agency Capture
- [The Regulatory Review] Preserving the Adjudicative Capacity of Non-Article III Tribunals - The Regulatory Review (2026-07-28) - https://news.google.com/rss/articles/CBMiuAFBVV95cUxPNzZwZHkzQ1dtT3Vici1KUy0xUS1NOHoyRFRsNXpGZnpZeUNabGZsekpCbDJheG5tcXctVDRIVHhjak9iMFlVSDl6ZkRJazJIZHU0THpzMGU5SEppS045NXl1Tno1ZWczMWtUcEhTaFhiWFFXNDdfX29OOEFhQkVCblRyeWx6V2FuUmtJWUNDRUM3cWJCc2Q3YTBHNE5YU2dfOFR3b3RZTUlNeFpVbzM2d3BRZGhMcFBN?oc=5
- [The New York Review of Books] An Unconstrained Supreme Court | David Cole - The New York Review of Books (2026-07-28) - https://news.google.com/rss/articles/CBMijAFBVV95cUxOWmpXMjN1MVBQMHhfOUhTQjdCQXUwMXVxSmZaVFJ6anp1aXFLOU9UTi1VUkhpQnNNRGQ2UlBBMGNJTGc2OXB5Rm5Zd0luRC15dThQZ1NGWHNNMi1wbkQxN2ZVajdYWkJyUjBPa3Y5WnpVSHYtVnBNaWVSR2pKTUl6RE12MldjSUdhNTJsOA?oc=5
- [Marin Independent Journal] Guest editorial: The Fed’s independence is unfinished business - Marin Independent Journal (2026-07-27) - https://news.google.com/rss/articles/CBMinAFBVV95cUxPT3AzUGFvU21YeEpHQzNtYUlDN1JPblhVUkRlRlp5QjYtbjg5TldJMU9CLW9kaFFlODdVNVZmM0tLVmQ3bEVUdndnWWQ1OWJWazduQWZaVmtFXzRNa3RsdTFVSUJQWWZnQjNwcnhXTGRPOGMyUTRubmF4TG1LTEVya09RUS1NMi1zRkdUM3B2SThmWk43RG90NUNwNnbSAaIBQVVfeXFMTUpWYmxHOGg1cUpvTndTM2VncnQwa3Z5b3VWb2ZldXI1bFJDZDhnYXhTemNmNUxjai1aUFl5Z01JNkh2MnBRN3VGaFFIRHZqbWlzYkxMMFU1RGloYktpeU5IMENtTUIzWnVvNEdOUWVFcDY0Z3N0MlB0YUhrV1ZGYnlSUmh4b3dadDlIbGlESGtsV21yVFhTS0xwSDNsa3l0X3pB?oc=5

### Martial Law or Military Governance Language
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 22
- Query feeds successful: 22
- Query feeds failed: 0
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
