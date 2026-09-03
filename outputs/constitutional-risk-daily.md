# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-03 16:31:32 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **10 / 100** (Baseline Institutional Noise)
- Previous day delta: **+1.0**
- Delta vs 7-day average: **-1.6**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.00 | 0.00 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.08 | 0.29 |
| Executive Constraints and Emergency Powers | 13 | 1.22 | 3.95 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 0.65 | 1.62 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 1.00 | 2.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Oversight Obstruction | federalism_oversight | 2.00 (Yellow) | ai | 6 | 6 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 2 | 0 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Legislative Bypass by Executive | executive_constraints | 1.65 (Watch) | ai | 0 | 1 |
| Political Speech Criminalization or Surveillance | civil_liberties_information | 1.30 (Watch) | keyword | 0 | 0 |
| Independent Agency Capture | civil_service_integrity | 0.55 (Green) | keyword | 0 | 0 |
| Opposition Ballot Exclusion | opposition_pluralism | 0.25 (Green) | keyword | 0 | 0 |

## Evidence Samples

### Legislative Oversight Obstruction
- Assessment: A private citizen has ignored a congressional subpoena and filed suit to block legislative fact-finding. This is a specific, credible, real occurrence of an individual obstructing legislative oversight through litigation and non-compliance. However, this is an individual defiance rather than a systematic governmental barrier to oversight, and the legislative process retains enforcement mechanisms (contempt, etc.). Severity 2 reflects a real but localized obstruction action, not a systemic failure of the oversight apparatus itself.
- [The Washington Post] Billionaire Leon Black ignores Epstein investigation subpoena, sues congressional committee - The Washington Post (2026-09-03) - https://news.google.com/rss/articles/CBMivgFBVV95cUxPOE9iTUtZQW5ZTDY1c0djTXhWcVJvVDFPVU9LSEthYUpqblBzX0ZTaTMzRXc2LUpCUmczWklKLWItcHpYT3MwNksxVG5vR1Q0TFNRMkUxU3E0SmprbDdiMmRCbzUxMmNiRW9TeHhsTUZmc0pLZlZNN1FLdTNsbTB3OEI1TWNsX2xVWTRNNUZ6R29XcUlwa214djExNHFjeVlyaW9weGRsaWhuOTktQV9xQUtsckpGOFJ3cXVqODVn?oc=5
- [Fortune] Billionaire Leon Black is suing Congress for ‘fishing’ into his alleged ties to Epstein - Fortune (2026-09-03) - https://news.google.com/rss/articles/CBMiggFBVV95cUxNM05CU2VxRFo4bTRkMHFOT0t3TERtT3FtV1o2dkV6TTdUV1ZxeElyNEdTNUhLUWlzLWVIYzVZM0dLeEpiOUdsanRHaGxubGV4UDl2eTI4bWVicFpjMElmbGNPS3pLZFVXZE9UOWI2N0VlSTA1SnJNbmxYcEcxZFVpRTRB?oc=5
- [qz.com] Leon Black sues House Oversight Committee, skips Epstein deposition - qz.com (2026-09-03) - https://news.google.com/rss/articles/CBMiigFBVV95cUxQY3RBSVE3QXZhUXVRUFo1MkE5NExqZDYzYTBFX0lNbGtBR0syQ1JMaDlvaWJuamsyZE1rTlpfcnpKUkEzbUhGMFBQYlFDdjhPMnA4NzhnZTBzTy05d2pHSERyZkJ3bUlUMURXYlhGMTA0Z0poQkFXQ1BRQWp3aTRiMGRNOUpZZXRCamc?oc=5

### Emergency Powers Expansion
- Assessment: A continuation of a declared national emergency is an official action that invokes emergency authorities to maintain existing powers beyond the ordinary legislative process. The continuation document itself is the legal instrument that extends emergency authorities. However, this represents maintenance of an existing emergency declaration (originally issued in 2017), not a new expansion. The severity is 2 rather than higher because: (1) the underlying emergency was declared through ordinary constitutional channels and has been subject to congressional oversight mechanisms (National Emergencies Act requires periodic review); (2) continuation is routine procedural practice rather than novel expansion; (3) no evidence from the summary indicates the scope of emergency powers has been broadened or that ordinary legislative constraints have been newly bypassed. The action is real and matches the signal, but reflects existing rather than expanded emergency authorities.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Foreign Interference in or Undermining Public Confidence in United States Elections (2026-09-02) - https://www.federalregister.gov/documents/2026/09/02/2026-18046/continuation-of-the-national-emergency-with-respect-to-foreign-interference-in-or-undermining-public
- [federalregister.gov] **[official record]** Declaring a National Emergency To Secure the United States Bulk-Power System (2026-08-31) - https://www.federalregister.gov/documents/2026/08/31/2026-17843/declaring-a-national-emergency-to-secure-the-united-states-bulk-power-system

### Civil Service Purge / Schedule F
- Assessment: An official final rule by the MSPB, effective upon publication in the Federal Register, eliminates a longstanding procedural safeguard (the Douglas factors test) that previously constrained agency penalty selection in misconduct cases. This change immediately alters the legal landscape: agencies can now dismiss employees for misconduct without MSPB review of penalty proportionality under the prior multi-factor framework. The removal of this safeguard is itself an accomplished action, not a proposal. However, the severity is limited to 2 because the action is narrow in scope (affects one adjudicatory procedure), targeted at a specific category of decisions, and does not yet constitute a wholesale structural failure or a purge in progress. No mass dismissals have occurred under this rule; the change creates a new permissive legal condition for politicized removals but does not demonstrate that such a campaign has been launched.
- [federalregister.gov] **[official record]** Determining the Appropriate Penalty for Federal Employees Charged With Misconduct (2026-09-03) - https://www.federalregister.gov/documents/2026/09/03/2026-18061/determining-the-appropriate-penalty-for-federal-employees-charged-with-misconduct

### Legislative Bypass by Executive
- [Center for American Progress] Despite President Trump’s Claims of Foreign Election Interference, He Has No Legal Authority To Declare a National Emergency and Unilaterally Nationalize Elections - Center for American Progress (2026-09-02) - https://news.google.com/rss/articles/CBMiqwJBVV95cUxOQWxINGlBRldZWEZuM2tmNHFiVEhvcUloOGZoRklyV19OSFZ2elpCV0ZGWFV6QzZzekpfbjlDWW5qaC1pN0JVeW5TT0dodXVfMm1qV0ZUVEZjSEN5V3lyaEwzdTIxRGhzeTdYczMzbWtCMm1MdVYzYW8yLUJjOW5uaGZ1MXZoRFVEY19acWF4RGpGVDJUcF9jeGgxTjMxZXJUWHNRNHlnRlRkTXZwTXNQMFZhSlQ2QmpqZmI1QmNhdTlsNVZIazRTbnlwbVZ5YjREeUxQVW9qeWxraGo4R212QmZGQ1JlQV8zTmZMUHFnRk8yZXRQdXZhY3c2dnVYZVBNd3Z3Y2NnVmZwNDhPam9fWEhaeHBONWY5NTNkUEZST3VOa1pHS2I0c2xEVQ?oc=5

### Political Speech Criminalization or Surveillance
- No fresh evidence links in the current lookback window.
## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 24
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 12 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 3
- Evidence extraction: AI event extraction
- Confidence: **Medium**
- Fetch errors:
  - independent_agency_capture: courtlistener: The read operation timed out
  - inspector_general_retaliation: courtlistener: The read operation timed out

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
