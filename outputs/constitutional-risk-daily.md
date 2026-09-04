# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-04 16:27:24 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **21 / 100** (Elevated Strain)
- Previous day delta: **+11.0**
- Delta vs 7-day average: **+8.6**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 2.00 | 11.00 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.33 | 4.33 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 0.47 | 1.19 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 1.00 | 2.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 3.00 (Orange) | ai | 1 | 2 |
| Legislative Oversight Obstruction | federalism_oversight | 2.00 (Yellow) | ai | 15 | 15 |
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 2 | 3 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 2 | 0 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Political Speech Criminalization or Surveillance | civil_liberties_information | 0.95 (Watch) | keyword | 0 | 0 |
| Independent Agency Capture | civil_service_integrity | 0.20 (Green) | keyword | 0 | 0 |

## Evidence Samples

### Election Administration Capture
- Assessment: A U.S. Postal Service system for 'ballot-screening' (selectively screening or handling ballots) represents a direct and serious capture of the ballot delivery and handling process by executive-branch actors under administration control. The USPS is a federal agency; a system that screens ballots before they reach election officials removes a crucial neutral checkpoint and shifts ballot handling authority toward partisan executive control. This is not a proposal or concern—it is an active construction of a new system that alters ballot administration. This constitutes a confirmed, serious action moving election administration from neutral process to partisan control. Severity 3 reflects the structural seriousness: ballot handling moved into an executive screening apparatus.
- [The New York Times] Trump Administration Updates: U.S. Postal Service Rapidly Builds Ballot-Screening System - The New York Times (2026-09-03) - https://news.google.com/rss/articles/CBMiY0FVX3lxTFBzQUpqd2pfTk1vNEVudWJjU00xVF9hcTc2NndCTjVlc1hqYkk2UmR2ZmNnZGJjakVLVWYwVjM2SXNwck8yVE1xalVwSlRGaXZrNU9UQXZxV2k4ZlVCOUFVX0ZNWQ?oc=5

### Legislative Oversight Obstruction
- Assessment: A private citizen has defied a House subpoena and filed suit against the House Oversight Panel. This is a credible, confirmed defiance of legislative fact-finding authority. However, this is an isolated action by one individual against a specific congressional committee, not a systematic obstruction by governmental actors or a structural pattern. The signal concerns 'systematic barriers' to legislative accountability; a single lawsuit by a private party challenging a subpoena is a real stress (the subpoena is being contested), but does not rise to systematic or structural obstruction. The legislature retains enforcement mechanisms (contempt proceedings). Severity 2: a real, confirmed stress signal but contained and not yet systematic.
- [lawcommentary.com] Billionaire Leon Black Defies Epstein Subpoena, Sues House Oversight Panel - lawcommentary.com (2026-09-04) - https://news.google.com/rss/articles/CBMilAFBVV95cUxQZTFRalhJUW51OVo1UU1SdGdmVzVTTWNEQl9LdXlyaEN4TzBaSG9TLVprMkRPaWxoZ01zMFZzZUNYbzN6b1BTUWxYUHgwUHQtV3drWlFTc0hITWkxTk13cjVFeVh5bmpjdGJYUDdRd2FGN0tzWDhNcjNDM0tETU1zcmhWaXoxSzNmZnVhWXBGTXI3X3BH?oc=5
- [The Washington Post] Billionaire Leon Black ignores Epstein investigation subpoena, sues congressional committee - The Washington Post (2026-09-04) - https://news.google.com/rss/articles/CBMivgFBVV95cUxPOE9iTUtZQW5ZTDY1c0djTXhWcVJvVDFPVU9LSEthYUpqblBzX0ZTaTMzRXc2LUpCUmczWklKLWItcHpYT3MwNksxVG5vR1Q0TFNRMkUxU3E0SmprbDdiMmRCbzUxMmNiRW9TeHhsTUZmc0pLZlZNN1FLdTNsbTB3OEI1TWNsX2xVWTRNNUZ6R29XcUlwa214djExNHFjeVlyaW9weGRsaWhuOTktQV9xQUtsckpGOFJ3cXVqODVn?oc=5
- [NPR] Leon Black defies subpoena to testify in Epstein inquiry and sues House panel - NPR (2026-09-03) - https://news.google.com/rss/articles/CBMihgFBVV95cUxNNTVOUHZYM2FFOWVUeGhtb2hCRWcya1VSY3JhWS1Wd3NXdFRtNnU3SDB5OEVvRmJWTlhPNHJ2QjdYMHFTZ1hsdnNaVGV1cUhFLXFQd0lZWmJlZkFNME82QndwMWxNWEl5aTlHY1pLSVFWLUxfQVNNQ2Q1a1BwTVNtakZfMGRidw?oc=5

### Legislative Bypass by Executive
- Assessment: Multiple credible sources report that the Supreme Court allowed Trump to implement parts of a mail-in voting executive order. This represents a shift of voting-rule authority from statutory/legislative control to unilateral executive action via EO. The Court's allowance (likely through stay or injunction ruling) enabled executive implementation without requiring legislative authorization. This is a real, confirmed action that transfers governance authority from statute to executive fiat, but is narrowly scoped to mail-voting procedures rather than a broader structural dismantling. Severity 2 reflects this as a real, credible stress signal of limited scope, not yet structural failure.
- [ABC News - Breaking News, Latest News and Videos] Supreme Court allows Trump to implement parts of his mail-in voting executive order - ABC News - Breaking News, Latest News and Videos (2026-09-03) - https://news.google.com/rss/articles/CBMigAFBVV95cUxQLUpWVmxZNkVNNGxlamhNRjkteVhjUVJNMXhDQ3Vyc3V3UkdTVEcyeUM0ZnEzTUlJQXRYMUZsNkZ5LTN5Q0VzWDFrVmVFSVlpOFBSaEpwa19qd0Q4SExzankxMEpIQjMxT2k5R0Z3emE0cDFCNng3V3lwVjBQUDg1NNIBhgFBVV95cUxOWGtmd1BpZ1U2QlJOeTZIcXhKMTVTOVFEZDJKcDJPS1NzX2NsOG1RT2w2TkpUMDkwTWY1QzlZcGt4LVlmNV9NZlFVUG04S0Y1U2hUSUdFSk5sUlFId1VsZzlnd1JvOGlWQnY2LThiN1J6cjZDSjdSWHd3elNWS3FpYWJqMXFnUQ?oc=5
- [Legal Service India] Who Controls American Elections? Trump’s Mail-Ballot Order and Supreme Court Battle - Legal Service India (2026-09-02) - https://news.google.com/rss/articles/CBMiuwFBVV95cUxOTnpHVXFEc1UybGFBWmlueUFsZTlVMU9oeGlMR0dvQ1pCbndKNHN4d21iR1V0Wm9wUEpDZXFuWW9SZkszNFFIWUFUcE55ZmJ6VDl6c1VJWnZibjNWWUdlSGdpdkR6dlRJQ2EwZVFGelp2eXZPUVc3cm0xZlgySWlHNDJsZGxxd2FhNDYycmlLS3U4Mk0wQmpZZDhwekFUSkJQWGdxM0hFQWZONFNNOEVneFdSdjU3dUFLc184?oc=5

### Emergency Powers Expansion
- Assessment: A continuation of a declared national emergency is an official action that invokes emergency authorities to maintain existing powers beyond the ordinary legislative process. The continuation document itself is the legal instrument that extends emergency authorities. However, this represents maintenance of an existing emergency declaration (originally issued in 2017), not a new expansion. The severity is 2 rather than higher because: (1) the underlying emergency was declared through ordinary constitutional channels and has been subject to congressional oversight mechanisms (National Emergencies Act requires periodic review); (2) continuation is routine procedural practice rather than novel expansion; (3) no evidence from the summary indicates the scope of emergency powers has been broadened or that ordinary legislative constraints have been newly bypassed. The action is real and matches the signal, but reflects existing rather than expanded emergency authorities.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Foreign Interference in or Undermining Public Confidence in United States Elections (2026-09-02) - https://www.federalregister.gov/documents/2026/09/02/2026-18046/continuation-of-the-national-emergency-with-respect-to-foreign-interference-in-or-undermining-public
- [federalregister.gov] **[official record]** Declaring a National Emergency To Secure the United States Bulk-Power System (2026-08-31) - https://www.federalregister.gov/documents/2026/08/31/2026-17843/declaring-a-national-emergency-to-secure-the-united-states-bulk-power-system

### Civil Service Purge / Schedule F
- Assessment: An official final rule by the MSPB, effective upon publication in the Federal Register, eliminates a longstanding procedural safeguard (the Douglas factors test) that previously constrained agency penalty selection in misconduct cases. This change immediately alters the legal landscape: agencies can now dismiss employees for misconduct without MSPB review of penalty proportionality under the prior multi-factor framework. The removal of this safeguard is itself an accomplished action, not a proposal. However, the severity is limited to 2 because the action is narrow in scope (affects one adjudicatory procedure), targeted at a specific category of decisions, and does not yet constitute a wholesale structural failure or a purge in progress. No mass dismissals have occurred under this rule; the change creates a new permissive legal condition for politicized removals but does not demonstrate that such a campaign has been launched.
- [federalregister.gov] **[official record]** Determining the Appropriate Penalty for Federal Employees Charged With Misconduct (2026-09-03) - https://www.federalregister.gov/documents/2026/09/03/2026-18061/determining-the-appropriate-penalty-for-federal-employees-charged-with-misconduct

## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 24
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 15 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 3
- Evidence extraction: AI event extraction
- Confidence: **High**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
