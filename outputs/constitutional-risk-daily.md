# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-09 16:44:28 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **11 / 100** (Baseline Institutional Noise)
- Previous day delta: **0.0**
- Delta vs 7-day average: **-3.9**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.31 | 1.72 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.33 | 4.33 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 1.00 | 2.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 2 | 5 |
| Legislative Oversight Obstruction | federalism_oversight | 2.00 (Yellow) | ai | 1 | 1 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 1 | 1 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Election Administration Capture | elections_transfer | 1.25 (Watch) | ai | 0 | 3 |

## Evidence Samples

### Legislative Bypass by Executive
- Assessment: A mail-order ballot order has been issued by the executive branch. This is a real action that appears to operate in a domain normally governed by statute (election administration, which is primarily a legislative domain under the Elections Clause). The item identifies an executive action that constrains a voting method without clear statutory authority. This is a credible stress signal of legislative bypass, though confined to this specific order and without indication of defiance of a court order or systematic removal of safeguards. Severity 2 reflects a real, confirmed action that is contained and not yet at the level of structural constitutional failure.
- [inkl] Trump's Mail-Order Ballot Order is an Assault on Federalism and Separation of Powers - inkl (2026-09-08) - https://news.google.com/rss/articles/CBMirgFBVV95cUxNb3Zwd1VuVFR3aXN3Y3kwS2hBa0phNnJzMmh4a3FmaFhsR1RQd09sYzh4M0JVLWxrUG5UeExJNWdPejYzdURmZEM4aGtpakVxLWdZY2lRYWtwMFNTOGxYcFRRcldZcmJlTzREYmFIQnNSaVo5c2lCZXpnN1A3MWU2YVd3MGhOTkFXbDRQNEc3OGEzdlZzMGUzLXo0Z2FaTG42ekRKS3kxeVVkaEdqWHc?oc=5
- [RadarOnline] EXCLUSIVE: Trump Accused of 'Unconstitutional' Election Power Grab as Members of Congress Beg Supreme Court to Block New Mail-Ballot Crackdown - RadarOnline (2026-09-08) - https://news.google.com/rss/articles/CBMisgFBVV95cUxPbDZtN1pOTmZRQnJOb1k5dzVXQnViSGZwZ1FEUXFpdWFVQThfbzlEcmwyeDRPUkJjamRCRWhzdVV3bXQ0S2dxNjdpbldUZm0yb1VkNmIwYVB1TWtlSk05WFRwbERMbXZmWWpiTzVJd3ZhSlJwWEZyNVZUX3FndjNtTFBGcmFGd0Z2RDBOazNJUTc4VmJmU3ZWYWJwMzRlT2V1a3k5MEVBNGJLV1pKV3NRNFZB?oc=5

### Legislative Oversight Obstruction
- Assessment: Leon Black's documented skip of a House deposition and filed lawsuit challenging congressional subpoenas constitute a real, credible action that creates an obstruction to legislative fact-finding. This is a verified occurrence of resistance to congressional oversight authority. However, severity remains at 2 rather than 3 because: (1) the obstruction is from a private individual rather than a government official systematically blocking accountability; (2) this is an isolated incident of one person's non-compliance, not a systematic campaign or structural barrier; (3) the subpoena power itself remains intact and enforceable through contempt and other mechanisms. The action demonstrates friction in the oversight process but not the systematic, institutionalized obstruction that would warrant higher severity.
- [The Well News] Billionaire Leon Black Skips Epstein Deposition and Sues House Committee Over Subpoenas - The Well News (2026-09-08) - https://news.google.com/rss/articles/CBMiwwFBVV95cUxPUVdhdGJiV1JTV0F5cjFoYkVodkNxQ2cxUURkQi00UTNlUzdhQ3c1eTlQQmpZY1J6eFZKV0JSU2UtdHI2dGlPNnNTNnR5a3pQcHBENWVEREl3VVk5VkthbmsxZWNfSk41UjNBTFRFeWlvNzJWSnZwZERhMndkMGRhUW5UZG9QZ2drRVBoU2h1cWxGWmhEd0FPTnkxeWM3UmpCZWUzUVZoVkJSRldWWTNxYk5FSGNxS0FneVczYXh1MzNMZDg?oc=5

### Emergency Powers Expansion
- Assessment: A continuation of a declared national emergency is an official action that invokes emergency authorities to maintain existing powers beyond the ordinary legislative process. The continuation document itself is the legal instrument that extends emergency authorities. However, this represents maintenance of an existing emergency declaration (originally issued in 2017), not a new expansion. The severity is 2 rather than higher because: (1) the underlying emergency was declared through ordinary constitutional channels and has been subject to congressional oversight mechanisms (National Emergencies Act requires periodic review); (2) continuation is routine procedural practice rather than novel expansion; (3) no evidence from the summary indicates the scope of emergency powers has been broadened or that ordinary legislative constraints have been newly bypassed. The action is real and matches the signal, but reflects existing rather than expanded emergency authorities.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Foreign Interference in or Undermining Public Confidence in United States Elections (2026-09-02) - https://www.federalregister.gov/documents/2026/09/02/2026-18046/continuation-of-the-national-emergency-with-respect-to-foreign-interference-in-or-undermining-public

### Civil Service Purge / Schedule F
- Assessment: An official final rule by the MSPB, effective upon publication in the Federal Register, eliminates a longstanding procedural safeguard (the Douglas factors test) that previously constrained agency penalty selection in misconduct cases. This change immediately alters the legal landscape: agencies can now dismiss employees for misconduct without MSPB review of penalty proportionality under the prior multi-factor framework. The removal of this safeguard is itself an accomplished action, not a proposal. However, the severity is limited to 2 because the action is narrow in scope (affects one adjudicatory procedure), targeted at a specific category of decisions, and does not yet constitute a wholesale structural failure or a purge in progress. No mass dismissals have occurred under this rule; the change creates a new permissive legal condition for politicized removals but does not demonstrate that such a campaign has been launched.
- [federalregister.gov] **[official record]** Determining the Appropriate Penalty for Federal Employees Charged With Misconduct (2026-09-03) - https://www.federalregister.gov/documents/2026/09/03/2026-18061/determining-the-appropriate-penalty-for-federal-employees-charged-with-misconduct

### Election Administration Capture
- [Newsday] 2026's elections could test how heavy trading on prediction markets affects races and results - Newsday (2026-09-08) - https://news.google.com/rss/articles/CBMimAFBVV95cUxNNUp5aUkxSm1HS3VPSUNBU3pPTDZMV1hDNFJiY3d5blR5Ny0zYldrM3kxX1VDR2J4M0FvRUdCdnZDMUJCVENEcHN5RkdBM0doQ3JXMl85YTgwdHB3TW1ndjhSYXZDeGhFVFBPWm9GVWxjYkZiTThxajFOaS10SWlCTTlVMkprcmVHLTUyZTdnVzJ0elJRUXNLSg?oc=5
- [Daily Kos] Old Home Page - Daily Kos (2026-09-09) - https://news.google.com/rss/articles/CBMiTEFVX3lxTFAya2puRGpPa0cwbmtmQk5FWElERklFbWJhSXVSWkdxMW00MjVTNVdZMXAyS0VlVVRsVmRIeUxnUHBhUlEzX0xGSFA0Rk0?oc=5
- [Britannica] Trinamool Congress - Britannica (2026-09-08) - https://news.google.com/rss/articles/CBMiYEFVX3lxTFAyY0d3dDhTMU9aVG1Gemt6TGV0NGVrWkNBSDZROVFjSUkzLTZiTTJicTdEUzZMMzFlRnFnLWRmbEtrOXdvdmkxSHhpeW1yLWRCTUh6bDlsTFZpMVhCMXZGVQ?oc=5

## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 24
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 10 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 2
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
