# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-26 12:37:16 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **14 / 100** (Baseline Institutional Noise)
- Previous day delta: **-3.0**
- Delta vs 7-day average: **-1.9**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.65 | 3.57 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.43 | 1.52 |
| Executive Constraints and Emergency Powers | 13 | 1.53 | 4.98 |
| Civil Service and Agency Independence | 10 | 0.65 | 1.62 |
| Civil Liberties and Information Environment | 10 | 0.47 | 1.19 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.65 | 1.30 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Martial Law or Military Governance Language | executive_constraints | 2.00 (Yellow) | ai | 1 | 5 |
| Election Administration Capture | elections_transfer | 1.65 (Watch) | ai | 0 | 6 |
| Statistical Agency Integrity | civil_service_integrity | 1.65 (Watch) | ai | 0 | 2 |
| Legislative Bypass by Executive | executive_constraints | 1.65 (Watch) | ai | 0 | 1 |
| Opposition Ballot Exclusion | opposition_pluralism | 1.30 (Watch) | ai | 0 | 5 |
| Legislative Oversight Obstruction | federalism_oversight | 1.30 (Watch) | keyword | 0 | 0 |
| Press Restrictions or Retaliation | civil_liberties_information | 0.95 (Watch) | ai | 0 | 3 |
| Emergency Powers Expansion | executive_constraints | 0.95 (Watch) | ai | 0 | 2 |

## Evidence Samples

### Martial Law or Military Governance Language
- Assessment: A county sheriff seized a large quantity of ballots, which constitutes an attempt to interfere with election administration through law-enforcement action. Although a court ordered return of the ballots (indicating judicial checks are functioning), the underlying seizure event—a military/law-enforcement actor taking unilateral control of electoral materials—is a real occurrence that matches the signal of military or law-enforcement management of a political dispute. The fact that a court intervened prevents escalation to severity 3+, but the seizure itself is a credible stress signal (severity 2) of attempted law-enforcement takeover of electoral processes. This represents a contained but serious action by a law-enforcement official overstepping democratic norms.
- [ABC7 Los Angeles] California Supreme Court orders Riverside County Sheriff Chad Bianco to return 650,000 seized ballots - ABC7 Los Angeles (2026-09-24) - https://news.google.com/rss/articles/CBMiyAFBVV95cUxPRGdZaTFSWjZGazROWnJFUjYxVVpaTnFaSW9nRzRybVZaMmU5VzZRSFppajFCeG5QMWJSZHhjWXdHbkpjUzU2ZUVZY2FlUkpuWXBjTkI5RGx5dUlKc0s0MDI4RGxEcjZrbUdUTHNjSWN1bzRHSHBlVGwwaEVyZkhfa0N2NVVVNVREWFhPMzhwOE9xZUZtN2k1U1VBWTNBVzk3M2ZHRHBOMmpqak1tcXdvYVpxSkNtVFBSRDVNWjVzYVdhOURFUkE2RtIBzgFBVV95cUxNVzdZZ2Mya2tfZVByMnlLaWFLQjl2d0tkckkwdGFlLW9oQ3ZZQXllYzN6V1NwbFFYcms4TjZyb2ZUd2FsOF9FT3lHal9nVGtiUWRUSDk3RUV0aTc3UXhiaUNXUXNtd1hlQm1MT0J3WmlMWXc0LW8xaTBKejNtMGJMSmNFWnVXUVk3QlJqWXY4ZjJJaU5LcGFPc2JseHhXZXZpTW9ia3ZEdnVid1RBRFB1ZFJWYktzcnNWQ0JXWENxWWFyR0dCcUF5NUtpamV0dw?oc=5

### Election Administration Capture
- [The Texas Tribune] Texas Democrat who championed A-F trigger law says he’s trying to fix schools - The Texas Tribune (2026-09-26) - https://news.google.com/rss/articles/CBMinwFBVV95cUxQaTE3SEV2WUxkUDlLcTRYZjhqWHNET1BVTUh3VFVUcGtzRkdsSi1lSmRNRklmUXRZMXByZGlMQ1B6V2FIamdtaUtXM0ZfMVN3S0s2aVVfSVowTGluQ1M1b255bW1sLU5wZjlObFhLY0dlem9mbVloTHJScFZZdkgtWWtxNXdZNmMzQy1HaVJhZzBYUzVjcGdOZjVQSTc5RmM?oc=5
- [Roll Call] Schumer, Jeffries sue to block federal agents at polls in November - Roll Call (2026-09-24) - https://news.google.com/rss/articles/CBMinwFBVV95cUxPOGN4MFVZRldkWjExRlJJSVg0ekpyaTRodG9udXVzVzhCQVhSZU1zTDJvOTNyMnNLUXBhRG1WR0tOUWdJUC05cEJ4SFdNMWI5am41VUFaSmRGX1E4TERGWGhneWtNcHJWSHdjamFjRG52SDgxYlRrZ3A5aS1xVm9ldHRvN0M5MzF0OW45Z01rWFdYUEw5RkFFRXRHX3p5NkU?oc=5
- [The Indian Express] Rupture in Election Commission: How dissent has played out in the poll panel in the past - The Indian Express (2026-09-26) - https://news.google.com/rss/articles/CBMiuwFBVV95cUxQTUZTVHRsaFpaSC1RUE81VTI2TlBQRHJBbWJ5WjMxTDFzdU5ZN3A3TnR5Mnl1TE9Oa1l3SnVrNUM3bDJ4X1dIMHV3cnpwWkFyVU9nSzlxbHRmMkt4RnBGQ0M1VzZNRUxMMzZ1U0lJNUloV1cwUUgwOWRnMkE3ZXZHVzRuTDBSc1piQl9MMDYyOFVKblE0anZVQWNZbUl4OGpIeWpjU3dCbVNpWEZnbDFzd3hOWncyUndmNUdJ0gG7AUFVX3lxTFBNRlNUdGxoWlpILVFQTzVVMjZOUFBEckFtYnlaMzFMMXN1Tlk3cDdOdHkyeXVMT05rWXdKdWs1QzdsMnhfV0gwdXdyenBaQXJVT2dLOXFsdGYyS3hGcEZDQzVXNk1FTEwzNnVTSUk1SWhXVzBRSDA5ZGcyQTdldkdXNG5MMFJzWmJCX0wwNjI4VUpuUTRqdlVBY1ltSXg4akh5amNTd0JtU2lYRmdsMXN3eE5adzJSd2Y1R0k?oc=5

### Statistical Agency Integrity
- [federalregister.gov] **[official record]** Agency Information Collection Activities; Proposed Collection; Comment Request; Extension: Investment Company Act Form N-17f-1, Certificate of Accounting of Securities and Similar Investments of a Management Investment Company in the Custody of Members of National Securities Exchanges (2026-09-28) - https://www.federalregister.gov/documents/2026/09/28/2026-19787/agency-information-collection-activities-proposed-collection-comment-request-extension-investment
- [federalregister.gov] **[official record]** Airworthiness Directives; Airbus Helicopters (2026-09-28) - https://www.federalregister.gov/documents/2026/09/28/2026-19758/airworthiness-directives-airbus-helicopters
- [federalregister.gov] **[official record]** Agency Information Collection Activities; Extension of Collection; Comment Request; Generic Clearance for the Collection of Qualitative Feedback on Agency Service Delivery (2026-09-28) - https://www.federalregister.gov/documents/2026/09/28/2026-19750/agency-information-collection-activities-extension-of-collection-comment-request-generic-clearance

### Legislative Bypass by Executive
- [The Colgate Maroon-News] Constitution Day Debate 2026: Reconsidering the Unitary Executive - The Colgate Maroon-News (2026-09-24) - https://news.google.com/rss/articles/CBMigwFBVV95cUxOdlk1NkZMYjZWSG1XcW1NSUVHWGYwOS12MnNmZkszVW5QUDJZNlRMa3JiS2pMMGlyUFZnY3dUYmhVMXdzZjAtMTNoY3BwbEJIYmU3ZXk2Unltdkp0czBtRFFIVlduNl8zZzN4amQzLWhiQXp6c0hpYU9renRrNTE4b0l6VQ?oc=5

### Opposition Ballot Exclusion
- [Al Jazeera] Arab parties denounce ban from Israel’s October election - Al Jazeera (2026-09-24) - https://news.google.com/rss/articles/CBMipgFBVV95cUxPdnVQQkNrZk1PUDlwOEZaWElnTVNHUUotMEZRelpQVjhOQ0tnakl1SnVnNzhrM0ktajdtQU51b19KdzN1Tl9LVGFzcUREUjN2VTJzbHFrY0pXbF9pMm1Uc2NZOF9iTVBJMTRQOTFVX0NaS2FwTVU0amJxUDJTWVhGOEtNODNLbmZJSVpEWlhXekJkeDZaaDVRd283aDNSdk4zZWJBbEpR0gGrAUFVX3lxTE5ad1p6czlmemFOLUtMT05XZnpvTldZN2JVam03N3R3Ynpxa1V4UExtNmlldktiUzZzQWVnUjcxLVlFcFdpTWVNWExaTlJIeDdKdndsczM4M1A2LVZYeVc5dW5yWXBSaVpBVnY0YmQtNVBVdXVRUy1jbEVvRldIY3FLbGp2N01HYTdGZGtCUzlDMkRDUVRpV1Ryem4wWERwUV9tUHlZRTBwWjctMA?oc=5
- [Jewish Telegraphic Agency] Israel’s election committee disqualifies Arab parties but not far-right Jewish ones - Jewish Telegraphic Agency (2026-09-24) - https://news.google.com/rss/articles/CBMivAFBVV95cUxPTm9neDVhZW5TY3VmeHBwZFNMa1dScXNLUjhMdHFES3dzQ3FIMWdKWUM5Z2NhRHItVVphRHNXa1pVQUJBREppNlp3MHg5c3ROTGE5OWVnRWs4UEJ2Wi1zX0duUmhKZXdKT3pfRDNpTmFxd1lLOFJCQ0R3Q2x2ME0zcUN6bkhhRVJpcWl2amM5SHhSMnRFRFl0b0J3WWxqRlBUeUg2emRpVF9YUklzZU5KTmRYZEE4STlMRk80VA?oc=5
- [news24.com] ‘Dirty tricks’: ActionSA accuses DA of removing election posters in Cape Town - news24.com (2026-09-25) - https://news.google.com/rss/articles/CBMixwFBVV95cUxPdkpicFZoVFF3ZkF0VTVkYlJpWmtjU19WVm9JS2NyQmhfbldfZ2dESFlpQW54MkE3aFZXOHpqZjJZNHI4SXZ1UURkVjI2SlZlSlJ0TXNLdWQ2Xy1pWjVJTGNtck9FNi1rcm9IU0tUeV8zT2JSY2RiUTVLM0RCd0lyOTVaR0tyOWNkRGFaNmRGQk1sNkI3bHpGbnZvb3FqcXZFVm1oN1ltMmw1bDhON0xjMmhrX0U4cHlFdWtOa1k2SGFJS01id2R3?oc=5

## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 24
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 12 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **High**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
