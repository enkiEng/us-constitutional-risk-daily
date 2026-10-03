# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-03 14:02:39 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **9 / 100** (Baseline Institutional Noise)
- Previous day delta: **-2.0**
- Delta vs 7-day average: **+0.4**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.65 | 3.57 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.32 | 1.03 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.22 | 3.04 |
| Security Sector Neutrality | 8 | 0.50 | 1.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 11 | 11 |
| Election Administration Capture | elections_transfer | 1.65 (Watch) | ai | 0 | 1 |
| Press Restrictions or Retaliation | civil_liberties_information | 1.65 (Watch) | ai | 0 | 1 |
| Domestic Military Use in Political Conflict | security_sector_neutrality | 1.00 (Watch) | ai | 1 | 1 |
| Legislative Bypass by Executive | executive_constraints | 0.95 (Watch) | ai | 0 | 0 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: News report of directive to use taxpayer money for ads praising the Trump presidency. This is a credible report of an alleged action that matches the signal (appropriated public funds spent on communications promoting an officeholder). However, without official confirmation or documentary evidence of the specific directive, this is a press report of an alleged action rather than verified official record. The repeated nature across multiple outlets (items 0-6, 9) elevates this from isolated mention to credible stress signal, but without access to the actual expenditure records or directive document, severity is held at 2.
- [The New York Times] Trump Directed Use of Taxpayer Money for Ads Praising His Presidency - The New York Times (2026-10-02) - https://news.google.com/rss/articles/CBMibkFVX3lxTFBiejVxNFZGSTRKNlpwaTFSOUppTm9SOWJXVHJXblVVbkNTTklEQkZxLVQ0YlRDQUVHMWdsNkduUlcxWGpycmg3SFJLWDZQWDY2RDlld1AzN0NrOEVvVDNNOGxURFAzSFVTMFRCU1pR?oc=5
- [CNN] ‘God made Trump’ ad and at least 12 others are part of controversial taxpayer-funded ad campaign - CNN (2026-10-02) - https://news.google.com/rss/articles/CBMic0FVX3lxTE9IRWxQX0Jpa0U2X01ScDg5YlBLM0J1NGhDOE1lZjJqcTNaMnpIRmhQTllETThRNjNXV01KOTlFQXh0MzYweFpXSXRSbDBldndSM3pQRG90QXZGT3E3RG41MXBrSkFscnl2Tm5sdmQtUUk0c00?oc=5
- [ABC News - Breaking News, Latest News and Videos] Trump defends spending millions on taxpayer-funded promotional ads: 'For the country' - ABC News - Breaking News, Latest News and Videos (2026-10-01) - https://news.google.com/rss/articles/CBMisAFBVV95cUxQTTZ6c1ZheWdCTTN1d1hKaGR2U2xxb1hZSV9HWDFueUNpU1U3NlBBcW84V0ZENVBfMy0tV2syam5MTlJFMmdvMFZ3N0c5bEZUdXhCWGxCRGd2Uk9fOGFiRW5tU2k2cEp2X2dKdkpZTUN5V1VNdDUtQUMwekJJbnRSS2lpVC13emZ4eU1uaEdtN1N6RWJvRHZ4V3hMN01TWWtOQWZaT2pqRnhib0JmekozZNIBtgFBVV95cUxQZUZWR1E1ZDdHMkR3Y2gxV213QWVTMjBRbUNxNzVWMkd3ak01TDB1X213VTl3RXNMM3lHdU1PaFp2cHphWF85V1NCMUtlbVZuRy1EX2JWY0N1M09QcVQ5ZVl2eFRaTHhXSEJtYjJVX1Bheld5ekRyaFZVZmtKNFNTUzBIZU1CSGZCVTZ0Z21mU0xmRVRJMS0zNUJpTVBreS0tUUNsUm5hbEsxcUo5U0w4QS1TeTFSZw?oc=5

### Election Administration Capture
- [The Economic Times] Shivakumar, Vijayendra trade charges over 'deletion of voters' from electoral rolls - The Economic Times (2026-10-02) - https://news.google.com/rss/articles/CBMi9AFBVV95cUxOMURybUFMLWUtZUZXSFQ3djU5QUllS3dLeWU1RUxWSlFKOGxGdjdDbTRYbDAwUS1rbFVRTE1JemFYLWt3d3RDNWNqQzZsX2hzdUJDZ1ZrRnVZaW10cENLb2pwa0thWmtPT1o0S0VyeXBSdGgzRnZSLVlVbExmVWllNWpkNjNINk54Vl80WDR0Sm8yYnVIOHVoWmhOQ2Q3ZUxsS3ZVbWNXbEhBVUxHV2pMU28xR3hDNy1XRy1obzlBX1VhSnpuMmpZOHJZSG1jN1haVjhVdG10OURza1dhTzVoR0VDWFJmb2VOdWtETXBqM2VsUlN00gH0AUFVX3lxTE4xRHJtQUwtZS1lRldIVDd2NTlBSWVLd0t5ZTVFTFZKUUo4bEZ2N0NtNFhsMDBRLWtsVVFMTUl6YVgta3d3dEM1Y2pDNmxfaHN1QkNnVmtGdVlpbXRwQ0tvanBrS2Faa09PWjRLRXJ5cFJ0aDNGdlItWVVsTGZVaWU1amQ2M0g2TnhWXzRYNHRKbzJidUg4dWhaaE5DZDdlTGxLdlVtY1dsSEFVTEdXakxTbzFHeEM3LVdHLWhvOUFfVWFKem4yalk4cllIbWM3WFpWOFV0bXQ5RHNrV2FPNWhHRUNYUmZvZU51a0RNcGozZWxSU3Q?oc=5

### Press Restrictions or Retaliation
- [Civicus Monitor] CSOs, activists, lawyers, opposition, critics & media houses face severe retaliation - Civicus Monitor (2026-10-01) - https://news.google.com/rss/articles/CBMitgFBVV95cUxPYXdYT0hyRFJLRGRLVVJZMkpPeWk5SmllUjJHdHFGT0pFV2d0enpjX2dGeTNiTXljQzlmMWxJOFZhLVFoa2YyZnBlUHF6SUtydTVIeXdNSTI2SVZUOUwtRFUwcm9aMTJSOWpzSV9ZbE9sMHpDbEw1b19RX0dqVjdKdDJnX1BfbWloYzFyUGxyeXhrVG5RWWczV2J5SVFra0EtOVpqS0xZZlVCeDFqNzVDdTVybnRXZw?oc=5

### Domestic Military Use in Political Conflict
- Assessment: A civil complaint has been filed in federal court (D. Minnesota) naming multiple current and former federal officials. The complaint itself is an official record indicating that plaintiffs have asserted claims regarding potentially unlawful conduct by these defendants. However, without access to the complaint's substantive allegations, the severity cannot be determined beyond acknowledging that a legal action has been initiated. The filing is a real procedural event, but severity is limited to 1 because a complaint represents an allegation, not a proven occurrence, and the specific nature of the alleged conduct cannot be assessed from the docket summary alone.
- [courtlistener.com] **[official record]** Ganger v. Ross (2026-10-01) - https://www.courtlistener.com/docket/74901903/1/ganger-v-ross/

### Legislative Bypass by Executive
- [federalregister.gov] **[official record]** Rescissions Proposals Pursuant to the Congressional Budget and Impoundment Control Act of 1974 (2026-09-30) - https://www.federalregister.gov/documents/2026/09/30/2026-19965/rescissions-proposals-pursuant-to-the-congressional-budget-and-impoundment-control-act-of-1974

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 14 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 1
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
