# Constitutional Risk Dashboard (0-100)

- Generated: 2026-09-02 16:40:09 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **9 / 100** (Baseline Institutional Noise)
- Previous day delta: **-2.0**
- Delta vs 7-day average: **-5.1**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.00 | 0.00 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.20 | 0.70 |
| Executive Constraints and Emergency Powers | 13 | 1.33 | 4.33 |
| Civil Service and Agency Independence | 10 | 0.65 | 1.62 |
| Civil Liberties and Information Environment | 10 | 0.82 | 2.06 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Legislative Bypass by Executive | executive_constraints | 2.00 (Yellow) | ai | 1 | 1 |
| Emergency Powers Expansion | executive_constraints | 2.00 (Yellow) | ai | 2 | 0 |
| Civil Service Purge / Schedule F | civil_service_integrity | 1.65 (Watch) | keyword | 0 | 0 |
| Political Speech Criminalization or Surveillance | civil_liberties_information | 1.65 (Watch) | keyword | 0 | 0 |
| Independent Agency Capture | civil_service_integrity | 0.90 (Watch) | ai | 0 | 2 |
| Opposition Ballot Exclusion | opposition_pluralism | 0.60 (Green) | ai | 0 | 1 |

## Evidence Samples

### Legislative Bypass by Executive
- Assessment: This item references Trump issuing a mail-ballot order and subsequent Supreme Court litigation. This indicates an executive order on voting administration (mail ballots) bypassing legislative process, with the order being challenged before the Supreme Court. This constitutes a plausible instance of major governance action shifted to unilateral executive authority regarding electoral administration. However, severity is capped at 2 because: (1) the item is from a secondary source summarizing the dispute rather than the order itself, (2) the outcome is still in litigation with no confirmation the action succeeded or persists, and (3) a single order challenged in court is a stressed signal but not yet a confirmed structural failure.
- [Legal Service India] Who Controls American Elections? Trump’s Mail-Ballot Order and Supreme Court Battle - Legal Service India (2026-09-01) - https://news.google.com/rss/articles/CBMiuwFBVV95cUxOTnpHVXFEc1UybGFBWmlueUFsZTlVMU9oeGlMR0dvQ1pCbndKNHN4d21iR1V0Wm9wUEpDZXFuWW9SZkszNFFIWUFUcE55ZmJ6VDl6c1VJWnZibjNWWUdlSGdpdkR6dlRJQ2EwZVFGelp2eXZPUVc3cm0xZlgySWlHNDJsZGxxd2FhNDYycmlLS3U4Mk0wQmpZZDhwekFUSkJQWGdxM0hFQWZONFNNOEVneFdSdjU3dUFLc184?oc=5

### Emergency Powers Expansion
- Assessment: A continuation of a declared national emergency is an official action that invokes emergency authorities to maintain existing powers beyond the ordinary legislative process. The continuation document itself is the legal instrument that extends emergency authorities. However, this represents maintenance of an existing emergency declaration (originally issued in 2017), not a new expansion. The severity is 2 rather than higher because: (1) the underlying emergency was declared through ordinary constitutional channels and has been subject to congressional oversight mechanisms (National Emergencies Act requires periodic review); (2) continuation is routine procedural practice rather than novel expansion; (3) no evidence from the summary indicates the scope of emergency powers has been broadened or that ordinary legislative constraints have been newly bypassed. The action is real and matches the signal, but reflects existing rather than expanded emergency authorities.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Foreign Interference in or Undermining Public Confidence in United States Elections (2026-09-02) - https://www.federalregister.gov/documents/2026/09/02/2026-18046/continuation-of-the-national-emergency-with-respect-to-foreign-interference-in-or-undermining-public
- [federalregister.gov] **[official record]** Declaring a National Emergency To Secure the United States Bulk-Power System (2026-08-31) - https://www.federalregister.gov/documents/2026/08/31/2026-17843/declaring-a-national-emergency-to-secure-the-united-states-bulk-power-system

### Civil Service Purge / Schedule F
- No fresh evidence links in the current lookback window.
### Political Speech Criminalization or Surveillance
- No fresh evidence links in the current lookback window.
### Independent Agency Capture
- [www.iconnectblog.com] The Unitary Executive Theory after Slaughter: A Comparative Hispanic Perspective - www.iconnectblog.com (2026-09-01) - https://news.google.com/rss/articles/CBMirgFBVV95cUxOd1RiVThoUVhsWXdDR1luSWZOWExYWENJYjdHWWR0THpDVEFKanFadFJoUEVmTXpJYmR1N2dyN1VwSEtEZFhWTno2OVMzVGdNaXBIOFdEZi1zeFdKZkN0YW9nMHZGVjFJMjNmZkk0Z3llNDRfWHpDckdtbXY1QW9BR1huUGZCU25HM2pheVU5NlpLanpnbEtTRzJTN1Z1UEhQM0lOdWdGMnRNSzJmUEE?oc=5
- [abcnews.com] Here's a list of the individuals, including James Comey, targeted by the Trump administration - abcnews.com (2026-09-01) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

## Data Quality

- Query feeds attempted: 24
- Query feeds successful: 24
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 18 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 2
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
