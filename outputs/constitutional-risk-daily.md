# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-07 17:45:39 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **13 / 100** (Baseline Institutional Noise)
- Previous day delta: **-3.0**
- Delta vs 7-day average: **-0.8**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.95 | 5.22 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 1.10 | 3.57 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 0.00 | 0.00 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 1.00 | 2.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Oversight Obstruction | federalism_oversight | 2.00 (Yellow) | ai | 1 | 1 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 2 | 0 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 0 |
| Election Administration Capture | elections_transfer | 1.95 (Yellow) | keyword | 0 | 0 |
| Legislative Bypass by Executive | executive_constraints | 1.30 (Watch) | ai | 0 | 3 |

## Evidence Samples

### Legislative Oversight Obstruction
- Assessment: Leon Black's documented skip of a House deposition and filed lawsuit challenging congressional subpoenas constitute a real, credible action that creates an obstruction to legislative fact-finding. This is a verified occurrence of resistance to congressional oversight authority. However, severity remains at 2 rather than 3 because: (1) the obstruction is from a private individual rather than a government official systematically blocking accountability; (2) this is an isolated incident of one person's non-compliance, not a systematic campaign or structural barrier; (3) the subpoena power itself remains intact and enforceable through contempt and other mechanisms. The action demonstrates friction in the oversight process but not the systematic, institutionalized obstruction that would warrant higher severity.
- [The Well News] Billionaire Leon Black Skips Epstein Deposition and Sues House Committee Over Subpoenas - The Well News (2026-09-06) - https://news.google.com/rss/articles/CBMiwwFBVV95cUxPUVdhdGJiV1JTV0F5cjFoYkVodkNxQ2cxUURkQi00UTNlUzdhQ3c1eTlQQmpZY1J6eFZKV0JSU2UtdHI2dGlPNnNTNnR5a3pQcHBENWVEREl3VVk5VkthbmsxZWNfSk41UjNBTFRFeWlvNzJWSnZwZERhMndkMGRhUW5UZG9QZ2drRVBoU2h1cWxGWmhEd0FPTnkxeWM3UmpCZWUzUVZoVkJSRldWWTNxYk5FSGNxS0FneVczYXh1MzNMZDg?oc=5

### Emergency Powers Expansion
- Assessment: A continuation of a declared national emergency is an official action that invokes emergency authorities to maintain existing powers beyond the ordinary legislative process. The continuation document itself is the legal instrument that extends emergency authorities. However, this represents maintenance of an existing emergency declaration (originally issued in 2017), not a new expansion. The severity is 2 rather than higher because: (1) the underlying emergency was declared through ordinary constitutional channels and has been subject to congressional oversight mechanisms (National Emergencies Act requires periodic review); (2) continuation is routine procedural practice rather than novel expansion; (3) no evidence from the summary indicates the scope of emergency powers has been broadened or that ordinary legislative constraints have been newly bypassed. The action is real and matches the signal, but reflects existing rather than expanded emergency authorities.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Foreign Interference in or Undermining Public Confidence in United States Elections (2026-09-02) - https://www.federalregister.gov/documents/2026/09/02/2026-18046/continuation-of-the-national-emergency-with-respect-to-foreign-interference-in-or-undermining-public
- [federalregister.gov] **[official record]** Declaring a National Emergency To Secure the United States Bulk-Power System (2026-08-31) - https://www.federalregister.gov/documents/2026/08/31/2026-17843/declaring-a-national-emergency-to-secure-the-united-states-bulk-power-system

### Civil Service Purge / Schedule F
- Assessment: An official final rule by the MSPB, effective upon publication in the Federal Register, eliminates a longstanding procedural safeguard (the Douglas factors test) that previously constrained agency penalty selection in misconduct cases. This change immediately alters the legal landscape: agencies can now dismiss employees for misconduct without MSPB review of penalty proportionality under the prior multi-factor framework. The removal of this safeguard is itself an accomplished action, not a proposal. However, the severity is limited to 2 because the action is narrow in scope (affects one adjudicatory procedure), targeted at a specific category of decisions, and does not yet constitute a wholesale structural failure or a purge in progress. No mass dismissals have occurred under this rule; the change creates a new permissive legal condition for politicized removals but does not demonstrate that such a campaign has been launched.
- [federalregister.gov] **[official record]** Determining the Appropriate Penalty for Federal Employees Charged With Misconduct (2026-09-03) - https://www.federalregister.gov/documents/2026/09/03/2026-18061/determining-the-appropriate-penalty-for-federal-employees-charged-with-misconduct

### Election Administration Capture
- No fresh evidence links in the current lookback window.
### Legislative Bypass by Executive
- [SCOTUSblog] Trump administration again appeals mail-in ballot dispute to the Supreme Court - SCOTUSblog (2026-09-06) - https://news.google.com/rss/articles/CBMitAFBVV95cUxNWm5ORTlLX0V1T0gtYi1yRVZ6REhtbDU2WDFtODNjN1VjdWNkNVJfR1dMNjdkVHg4ME5KNnh1MV96SlA5Q0o0bURlNndvNk8tX2p0NkU2R0pabjR5U1dyS1hxS0o5eE92d1pFcmtKQTV2T3dJVkJyVEE4Y2w2Q1JtdDM2cVRybnQxQlpONmtZYmd3Q3FxX3RCSG91UGwyNWViZlUzMGcwdlpmeDAtN1VOSm10R1k?oc=5
- [Heraldo USA] Trump Urges Supreme Court to Limit Mail-In Voting in the U.S. - Heraldo USA (2026-09-06) - https://news.google.com/rss/articles/CBMiswFBVV95cUxQSVlabHBtcVNXbmt5c0JkYVRJbjBKMnktalY3RHNQSVV3V1R4Q0FIbXRCV3BNNlFLTzlPazQ1Rm56TFBkVlV3UXVkZDlRTklzZC1KajFFUTRlb1A5dXNOdEFuNjB2c29SOW16SGRLazFwd2Z1Sm4wT0tWTXc2X3FzcDdFdUlpdklJM0VYeXlPZHU1YmJvVDRKN2ZmU3NuWXJUNXNqNXVfRnJzQXRFSUFqWWF3TQ?oc=5
- [Real Clear Politics] Election Integrity Hysteria Betrays Weakness - Real Clear Politics (2026-09-07) - https://news.google.com/rss/articles/CBMitAFBVV95cUxPZXVzeFRRZWw4WEJheHY5U1laX1lUc2Y2TEQ4dExDT2c2eWF0QmRIcWk3Sk54VzhySE5qVE9iZk42TUJ5M0dpRDl5TEpjQTEyMzNFdjZnRnFNSTl2QVl3R2ZwWTNrUGpvbERnX20tcXgtWFpiZmM5ZjVKWWZ3NnVNUS12LW9Bd0tXQXd0aDZ6QmUyRUY1NGdpX3QxbGpSSXpLa0RmUVZDbHA4UlY2ZzJnaVdGeWvSAbQBQVVfeXFMT2V1c3hUUWVsOFhCYXh2OVNZWl9ZVHNmNkxEOHRMQ09nNnlhdEJkSHFpN0pOeFc4ckhOalRPYmZONk1CeTNHaUQ5eUxKY0ExMjMzRXY2Z0ZxTUk5dkFZd0dmcFkza1Bqb2xEZ19tLXF4LVhaYmZjOWY1SllmdzZ1TVEtdi1vQXdLV0F3dGg2ekJlMkVGNTRnaV90MWxqUkl6S2tEZlFWQ2xwOFJWNmcyZ2lXRnlr?oc=5

## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 24
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 15 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 3
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
