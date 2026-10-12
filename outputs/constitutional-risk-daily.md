# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-12 13:03:00 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **9 / 100** (Baseline Institutional Noise)
- Previous day delta: **-2.0**
- Delta vs 7-day average: **-2.4**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.15 | 0.82 |
| Judicial Independence and Rule of Law | 15 | 0.24 | 0.89 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.65 | 2.11 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 1.00 | 2.50 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 7 | 7 |
| Independent Agency Capture | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 1 |
| Legislative Bypass by Executive | executive_constraints | 1.65 (Watch) | keyword | 0 | 0 |
| Court Order Noncompliance | judiciary_rule_of_law | 0.95 (Watch) | keyword | 0 | 0 |
| Election Administration Capture | elections_transfer | 0.60 (Green) | ai | 0 | 3 |

## Evidence Samples

### Public Funds for Political Promotion
- Assessment: A US federal judge has issued an order halting taxpayer-funded TV ads. This represents a court-confirmed instance of the administration attempting to use public funds for political promotion (the signal event), with judicial intervention ordering cessation. The event occurred (the ads existed and were funded by taxpayers), matches the signal (partisan promotion via appropriated funds), but severity is 2 rather than higher because: (1) the court has intervened and ordered a halt, indicating the constitutional check is functioning; (2) this is a single contained action now enjoined, not a pattern or structural failure; (3) no official has openly defied the order. The signal event itself (public funds for political promotion) did occur prior to the judicial order.
- [CNBC] Judge orders Trump administration to immediately stop taxpayer-funded TV ads - CNBC (2026-10-12) - https://news.google.com/rss/articles/CBMib0FVX3lxTE9CZmZ4U3JfSk9QT0JlZ1dvbXBsaTl4bl93M1JRQ2laTnhLVURlanhGVFdNb1h4Z0tsLW1hdVZZX0ZWN0hseGhiTERjYi1feGZTLUVrNEZ4Mk1CZmZWTWkyNUVmeHJiQUR2Yi13TDlCTdIBdEFVX3lxTE1HQlRwMGhPd3NzZW1qOTRDUXd1ZU5vNU5vcTVqSXZZbHFNcnpKSVBNaVA3VDdXczJzTTBQYUZBYUwzT19wV3o3cUhHbVRQZ29tRC1pTGxBaE9uLTQzeHI5dWVYaEFYTTFtVmt1Yk9mZDBHRThx?oc=5
- [Reuters] US judge orders halt to taxpayer-funded ads featuring Trump - Reuters (2026-10-11) - https://news.google.com/rss/articles/CBMiowFBVV95cUxOVURYbEJsVDMteXRVRGdGQWo2RnduSDB3ZklKSERDM3pvY0Q4U0FrdDZxWmJNUTNqLVpQNzVFZWRWcGVfd2ZDYXRDcFRTb0Ftd2NlQUR5dm1QVDl3dXBlcG10TUtWc18ycXFMY0U0UUZoaGQ3SkRKUkRIMWRsSXEwUGZaZ2R5bHRkZDNyR3lkSWVPa29zZGF5VDVja3laUlMyblIw?oc=5
- [DW.com] US judge orders halt to taxpayer-funded promo ads of Trump - DW.com (2026-10-12) - https://news.google.com/rss/articles/CBMilgFBVV95cUxNeW0wMXZ2aXpwelZieHotV3haUjNZeU1SOE41WjBaSktmNks4cnVOaVB4Yy1nVXJ2WWVDTUttSHpQRDJVQld2NlNqX0lVNnBKZUpRd283REJNaG1QdUh4c1NWZmpBZlNlQTdSbnJydzN5eVFFeWprWmE5ZS1jQk9WWloxUzktclZISGJjQkpveVMyS1lWd0HSAZYBQVVfeXFMT2FNODdZZzdCaHB5SHRmQlVJVjZYYkxFQUhvTXI5V3l4MmhBZTkzSnpyNmdvZVVXT1BCRjlINFNBVzZ6OWlBeVdFbTRUVFZHbzhHMGY3dG95UEpCcFJ4S2Q3M2FXbThEbEN2RUp0U3JvdGNZVk43ZkdGU293eGxOU3p6QWwwZUJ5cHZMMEtEUVZpdnlwMHpR?oc=5

### Independent Agency Capture
- Assessment: Foreign news outlet (Indonesian) reporting the same U.S. event as item [0]: Trump's establishment of a committee to investigate Fed Governor Lisa Cook. This is the same verifiable action reported from a non-U.S. source. The underlying event matches the independent agency capture signal—an executive action designed to pressure removal of an independent regulator. Severity remains 2 as this is investigatory pressure rather than structural removal of safeguards or accomplished removal.
- [SuaraGarut.ID] Trump Forms Committee to Investigate Fed Governor Lisa Cook - SuaraGarut.ID (2026-10-10) - https://news.google.com/rss/articles/CBMickFVX3lxTE8xY0ctMWVVT3Jya2FfVWJrb3gtVnBJdloxNklZNTFmb1Z3VW1oX0ZJWmpBdm94YUxKNk1MdFFtN1ZLT2V3UWxrWkNUZkRxT1I3RzVXSjVDWGwtV0NMT0NLRWwySVNoSkxheVFKTjAzWmNOUQ?oc=5

### Legislative Bypass by Executive
- No fresh evidence links in the current lookback window.
### Court Order Noncompliance
- No fresh evidence links in the current lookback window.
### Election Administration Capture
- [California Association of Realtors (CAR)] Ballot Measures - California Association of Realtors (CAR) (2026-10-11) - https://news.google.com/rss/articles/CBMidkFVX3lxTE1CZG9ubEJFZHJ1MmM2YUlLTVowNFM2RmVvVHhpRkZvem1ITmstRk9TZW14bms0S1BTNi0tajlxVzNIUC01a3BQQ0NOaTBsN0RrUTdETUtIcUVhVmpUMFJ0dDVENE1RaWJmZHNPa2ZPMnVSeEJTdFE?oc=5
- [www.indiagazette.com] "Around 40 lakh votes removed in Hyderabad in name of SIR": Telangana Minister slams BJP's Ramchander Rao - www.indiagazette.com (2026-10-11) - https://news.google.com/rss/articles/CBMi3AFBVV95cUxOQWVtMjV3VGdLUk5FQ1I5UFkydTd2RHdVN1hxRGwwRF9Ka2tTbTh6ckt0R0RDSVdPTVJBbDNVTGQ2b3YzTGtmMGhYYlNxNWF4UHNyS3lDN0tkeFBYUjcwNE9rc0xVbDdNcGd6Zml5QVIxSlRKaDlvT09ZVC02UnNjcEExd3I3UlM3OGUxMHhldEtxWXpQQ05Wd1BDZzVRMEpHSWdTdzU1a1FMNkdtRWsweXJ1VGxKZXdEX0p2Tkp4NHN6aDRwNm1SUEJwMnQ4azFNMl83aTNtamxWV0RL?oc=5
- [Big News Network.com] Scuffle breaks out among Congress workers at Ajay Rai's office in Lucknow - Big News Network.com (2026-10-11) - https://news.google.com/rss/articles/CBMiuAFBVV95cUxPNWxwSms4VnFGYnVjbS16STNJc3JkMDFQVlRwSXpsWTZvTlI2dmZDVDQ1UHYxZ0dmUGpDbmZMUzNncEpUSTh4MnY2SHFMazA4cVpNV2plbXNTSmZwOG9nZ2ZSencwYUs0WmlQMXNxYUtabm9UTC1xLVNXam1VRXpyUVdyUWJ2N1h4SWZvWnVDc24ybUVTdUNjcUNGc3BodXBRNlpueGUzYkRIVFFlblJPSF9SV3dTcWxH?oc=5

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 15 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 0
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
