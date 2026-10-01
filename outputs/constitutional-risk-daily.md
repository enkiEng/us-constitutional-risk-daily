# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-01 12:44:38 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **7 / 100** (Baseline Institutional Noise)
- Previous day delta: **-1.0**
- Delta vs 7-day average: **-3.3**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.25 | 1.38 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.65 | 2.11 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.22 | 3.04 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 17 | 34 |
| Legislative Bypass by Executive | executive_constraints | 1.65 (Watch) | ai | 0 | 2 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.65 (Watch) | ai | 0 | 1 |
| Election Administration Capture | elections_transfer | 1.00 (Watch) | ai | 1 | 3 |
| Martial Law or Military Governance Language | executive_constraints | 0.25 (Green) | keyword | 0 | 0 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: CREW, a watchdog organization, alleges that taxpayer-funded Trump ads paid for by DHS/CBP funds ($20M identified in other sources) violate federal law against partisan publicity. Multiple corroborating reports confirm ads are running and funded from identified appropriations. This represents a credible, repeated allegation of misappropriation of public funds for partisan promotion—a violation of the 1950s bar on propaganda spending. However, no official enforcement action, admission, or court determination has yet occurred.
- [Citizens for Responsibility and Ethics in Washington] Trump’s taxpayer-funded propaganda ads violate multiple federal laws - Citizens for Responsibility and Ethics in Washington (2026-09-30) - https://news.google.com/rss/articles/CBMizAFBVV95cUxQajc3NEpJSlFJNktnWXhQaGozc2FNVUlVUENlSWNzekhwREo5aGJ6UTZ4ZUd1Z3RyZ01uVnctNmtCOE9mSUpPXzZJc2hXV0pPUUItOXlCSmFYRE12ZGZFa1JKR3c0YTJjNTdGSHBNb2VIS3FoX0JLYWsyaV9ULVdoSjlJbW1vc0NFUE1xUW5nZXBrZ3lpbFRmYkc4QnhGdnU1NVoyVXdsc0tjb2hSZVpUMXBybFUxNE9scE41RmRCbTcwZ0l6OGpPTDVJLWU?oc=5
- [PBS] Homeland Security spending $20M in taxpayer funds for pro-Trump ads - PBS (2026-09-29) - https://news.google.com/rss/articles/CBMipwFBVV95cUxNZDlpTmFNd1IwREdDeVNFcnVFSThEZ2xOazdOakxwdUVqczByekptNFFmeDRCelhmejhDRnF3TGZ5c3ZqWDNkSDA2TUZIZmsxUkJZTEY2OTV4Ukd5ZHVpMkNRVHY5aWhVcm13WkJZanFXZTg0cFEzZGp1V2M1SHdmbmhfZmJVUUVPdEgzUUdleVdJcFhTb0h0SkZRQ2NrREY1bXBFdGJNRdIBrAFBVV95cUxOU2hjZ3JITUlGaDB4TXZLSUVWNnp4TWdmdHp1emdFcC1YRTA1dGdxR2NCNHJKQlYyZ0RjZ1BrNWFjWFJrM1FSUGdrQmsyc3RsVUhNemI0OTZVeUIyd0s3dXFkQWIyRHRxUFpwWk9MTURrTExkN0kzNU04SFV4UUs3cGdJVFZSSGZlN0VNVDFwYUhvS0xOZUZQSF8zNTMza3VHcFdvTUZUWHdxZTR2?oc=5
- [CBC] Why pro-Trump ads — paid for with public money — are airing on U.S. TV - CBC (2026-09-30) - https://news.google.com/rss/articles/CBMiekFVX3lxTE5TazN5aE5nRzFPdktFQ2M1TFVHdzBqMV80Wkp4RjVaNE1oYmo3Y2J1WF9sWi1tTHB2cVBITE5mdVQ0WWdXX1k0cGx2eGY4bmV5TFBGaDdtQTYxNlVSbWlIZThlUmdkRF9fc3pkRW5JSEx2bFlPUm90VFp3?oc=5

### Legislative Bypass by Executive
- [federalregister.gov] **[official record]** Rescissions Proposals Pursuant to the Congressional Budget and Impoundment Control Act of 1974 (2026-09-30) - https://www.federalregister.gov/documents/2026/09/30/2026-19965/rescissions-proposals-pursuant-to-the-congressional-budget-and-impoundment-control-act-of-1974
- [National Affairs] The Unfinished Work of Federal Permitting Reform - National Affairs (2026-10-01) - https://news.google.com/rss/articles/CBMimAFBVV95cUxOa0o4OXVkQkxHdXJ6VkxqLUNNTVhfQ0JFT3lYSDFLc2YycTlRUFV3VWp3TFhMMTgwSGZQaTdlU2RMNFBVZlV2Q05odjlFN3QwU0ZHVFh5QXE0OEJKRWh0dnR4ZGxFVk5KblVTWXI2UzJrRWlSeF9DWXAxX3lRNDRPMVBHdVlsdVZuemZZSjcyWGF0dUV1YnB3Xw?oc=5
- [Pakistan Observer] Trump’s America: Democracy under pressure? - Pakistan Observer (2026-09-30) - https://news.google.com/rss/articles/CBMickFVX3lxTE5EMF9aSzd6WDZOSlduSnVVdlZjaVpKeTNFaFpTMmJUaTh0MUUwVm1WVlRfUUo0ZTJZSXZKZmhIWlBLcDZmSE5pMFBKTzVRLVBwaXpNZ1pwOGM1dDNlSXlvNURCVVZVbVdUN0I4Z09sY2pFUQ?oc=5

### Press Restrictions or Retaliation
- [Borkena] A Question of Conscience, Human Rights and Ethiopia’s Future - Borkena (2026-09-30) - https://news.google.com/rss/articles/CBMihgFBVV95cUxNTEpFMmdlbnFJdTB0aU83bkd4djhDd0F3bU5sRWxmeTVmR0diYzFjbVFKVzlTbHR1SE1XQW84TWV5ck9PSGNaVmg3UGRXRVlaUFVRQS1LVzQ4VmVIRFE4V2pnbjQ4WUkyMjdoTk5Pc2c0Q2N1N2R6S3pIc1kzR3d1blgwRlhhUQ?oc=5

### Election Administration Capture
- Assessment: The item reports that some North Carolina county election officials promoted conspiracy theories about the 2020 election outcome and January 6. This is a real occurrence—officials in administrative positions making partisan statements and promoting false narratives about elections. However, this is isolated conduct by unnamed officials at the county level and does not demonstrate systematic partisan capture of election administration authority or removal of neutral process safeguards. The severity is 1 (isolated or weak signal) rather than higher because: (1) it describes individual speech/promotion of conspiracy theories rather than structural changes to election administration authority; (2) it is geographically limited (some NC counties); (3) there is no indication these officials used their positions to alter election procedures or outcomes; (4) it does not show they have captured the administration in a way that prevents neutral process from functioning.
- [The Asheville Citizen Times] Some NC county election officials promoted conspiracies about 2020 outcome, Jan. 6 - The Asheville Citizen Times (2026-09-30) - https://news.google.com/rss/articles/CBMi3gFBVV95cUxOR3V1XzVWLWtERDNOMlRjTm5NR0UtbHl1d1BPeF92Mnl5TDRydzh5LTVBYVlnUUt3S1NyYXFKZWRNYXdNTDVIMkZQWkFJQzgyaHRUbU93clAtTldBQzlzS3lQeGpDaUN5NjVLbHI0ZjRDekxreW9rallTNm9HY3pSRXdJSlZvUUUyZEQxOXZZVGhzeVlCOWJ6ajZiS2FXRWY4VUN2THhPa1hkLTQtSWw1amZjZ2dQQTJzdDJOaFVoQXhjazY5MkVXemVEeW5tdWFDM0lFV0ZjanVyRFRBbVE?oc=5

### Martial Law or Military Governance Language
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 12 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **High**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
