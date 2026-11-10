# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-10 12:27:29 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **13 / 100** (Baseline Institutional Noise)
- Previous day delta: **-2.0**
- Delta vs 7-day average: **+0.3**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 1.30 | 7.15 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.88 | 2.87 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.22 | 3.04 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 2.30 (Yellow) | ai | 1 | 8 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 2 |
| Legislative Bypass by Executive | executive_constraints | 1.65 (Watch) | ai | 0 | 2 |
| Public Funds for Political Promotion | civil_liberties_information | 1.65 (Watch) | ai | 0 | 2 |
| Emergency Powers Expansion | executive_constraints | 1.00 (Watch) | ai | 3 | 0 |

## Evidence Samples

### Election Administration Capture
- Assessment: This reports an allegation (via affidavit) that a Trump-appointed director of election security sparked a Georgia office raid. This represents a real action that has occurred—a raid of an election office—allegedly directed by a Trump administration official. While the severity is not extreme (no election was cancelled or overturned), this constitutes a credible signal of election administration being subject to partisan pressure from the executive. The involvement of a Trump administration official in directing action against a state election office suggests potential partisan capture or interference.
- [ABC News - Breaking News, Latest News and Videos] Trump director of election security sparked Georgia office raid, affidavit says - ABC News - Breaking News, Latest News and Videos (2026-11-09) - https://news.google.com/rss/articles/CBMiqgFBVV95cUxQWFNyVlNGblFCd3ZfSEo5RGl2Z1htZGh0eGhxRkJBeGFGU2JKUG5haW5VYlM5RDBXTEV0Y2R0WVdzQTh3MU5lcFgyXzJ4aXJjcm1xcjE2Vzh0T3NzWVl6ck96eDF2MW1lREd1TFZ5Rl9MT2JVcFdyelFwOUJhbGMwWWg3VGZzSi1OYlRrQXUzaVk1YUJWelJjXzJfVmV1dFExRm1hYzNteDFwZ9IBrwFBVV95cUxNU0ljTjFlZmY5cExkci1ETmZKU2d5bm5lZ2NFVTBNUjM2RmdGVHhlNi1EMDFQYzl2Y2FtbXpGY3JDSlZmejZYWGpfenBlaHdQSFJqNENPNWhCWFVJTk0wUW15V3FwTjlFLWpUR3BacEF6U2theFBDdHUwNDZac0NzN3JyR1pEcG9pWU5WTVh6MmxDVHpzT2JJQ0FLNlR3Q25nWjhYcHdKT05mSk5xaDEw?oc=5

### Press Restrictions or Retaliation
- Assessment: ABC News reports that the Trump administration has targeted specific individuals including James Comey. This constitutes a real occurrence of state action that raises costs or legal risk (targeting by name creates reputational, investigative, or potential legal pressure). However, the report is limited to naming individuals targeted; without detail on the specific mechanism of retaliation (prosecution, removal from office, legal action, loss of license), the severity is contained at level 2 rather than escalated. A confirmed, orchestrated campaign with verifiable legal or official action would be severity 3+. This is credible press coverage of a real targeting action.
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-11-09) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

### Legislative Bypass by Executive
- [Diplomacy and Law] Pete Hegseth Impeachment: The International Law Issues Behind Massie’s Eight Charges - Diplomacy and Law (2026-11-09) - https://news.google.com/rss/articles/CBMibkFVX3lxTFBsbm1ocnBFUG5nSnhCMTAwLUVseFJfdWNfaDZGTlZZNEYtS3gtc1RoaE10dGpRREYxaF9MYjNjaHZfaEthRnlNUk5raGltem5JdXM5c0ROdk02aHJvWE9yX0d0c0hfWUh5bzFGTjFR?oc=5
- [PM News Nigeria] ADC: An Opposition At War With Itself - PM News Nigeria (2026-11-09) - https://news.google.com/rss/articles/CBMif0FVX3lxTE82UTl0VnphNjNXMWg1OTRJTEVTQnNQdmJNNkdqcDJOUkh3Z0RsLWdhaVo3VUt3SnBFQ3F0Qk5nYVFtX0FhblVMY3BJMWNnWURLWlhtdnE4U0lzVlBxUkpKaEgtQlVISlp4LS1CVDVkbWpmUFdyQUhkVXBCV2s0dDg?oc=5

### Public Funds for Political Promotion
- [News24] Chris Bowen’s ‘Orwellian’ net zero propaganda exposed in department talking points - News24 (2026-11-09) - https://news.google.com/rss/articles/CBMi0AJBVV95cUxOeVkyNHVlUW9iMi1EQ3pidVhTaDFGTWdMYTFfRW9JUmV5Y0xmR2ViTDJPNXNnX2pGVll6WjZuWjFZbURJQ014S25FMDRLdjRfMnpwRll1aHpvLTVDUWp6WUhQUkZWb1VKbWxJY3BMN2k2LUxLbXIyek5zblh3VjctQ08tNmw4bDRvRFFybEF4anBFVmc2ZENIMjdMemw0cnpMZ0VYZjR4bzIwT25aWVViQ3dmc004SXJjWnM0QUNQRVgtTThvWmRweGFYMF9OSHlra0Y3QUlWQUR0MWFzcmpnLVEtR3piNXJGVkx4YlRjcmFYcGpzTlZac09xYkNlTUVyZE55QnptSmFNN0lyOXJfUGRITmdxQ1hCdVYxdjh2UVVlb3pkMFJOdG9lZXlmN2ozeWRoTGxndEJYelhJOTlMMHdiR004MndXaEM0WDFzeGTSAdYCQVVfeXFMTTlPamprcTFweWZ2OU5LQVN3Y0NnWEY2dV95UmFsc1lQMEZyd2xIbk5XVkR1V2lJYlFydmVSTTVlR3U1VzVKZzdVRTNwQ3V3Wi0wYXFwYlJkd25IZ251M0Y4NERpWHFjbi1HM2p3TlpXVXZIVDdoRzcyN3JnMWJJR3o3cmRWY0RiSmh5cGY3amVQT25KdDFQYlRVQmZPRG5LaDdIU1ZBQkF4TnJmNEhXVHBuTjFQTVNFM0RnYWFPYmdlV2I3NUMxMmpIaDc4Y3paRUlHNUJGWWE1WWVWclc5RVczeTR4S0hPa3FXejJuU29nQW16aVBLZ3ZWT0xzQWNuZEJTdWZDd094WEFMR1dWeWJkcFpYSUJsRVNrYlh2eUhVVU5TTGMwLVdwcHNkcG83dmNZbzByc1hpQUxfeGxXN0pYVzdueDJ1U2JnVjlwbXA4cExkV0h3?oc=5
- [Gazeta Express] Judge orders Trump to pull taxpayer-funded ads promoting the president - Gazeta Express (2026-11-09) - https://news.google.com/rss/articles/CBMipwFBVV95cUxNS201alFiSnZ0eUVJSWltRHUwZnQ2N19Ob1Q1MUxDMVlEMDdiSUhqWWIweTlRQjAtWk5NaTFfSWZ6OGRjS1R2ZTlXTG5LTno1QWtaV3k3dHFTekw5elhaV3l2VUpnbHlBNGtaaTRjeTdHYmpwVU50VklINWhZZXlIbDR5b3pwdTh3SGFNY28wTXF4TTNRWGVON0R4ZGQwNllnb3JJMExPTQ?oc=5

### Emergency Powers Expansion
- Assessment: This is a continuation of an existing declared national emergency under the National Emergencies Act (NEA). Continuation of a previously declared emergency is a routine executive action that renews authorities already granted by Congress through the NEA framework. While the NEA does permit emergency powers to bypass ordinary rulemaking, continuation documents are ministerial renewals of standing authorizations, not new expansions. The underlying emergency was declared in an earlier year; this 2026 continuation represents ongoing use of existing delegated authority rather than a novel expansion. Severity is low because continuation is the ordinary operation of a congressionally-authorized framework, not a structural bypass of legislative process.
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to the Threat From Securities Investments That Finance Certain Companies of the People's Republic of China (2026-11-05) - https://www.federalregister.gov/documents/2026/11/05/2026-22688/continuation-of-the-national-emergency-with-respect-to-the-threat-from-securities-investments-that
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to the Proliferation of Weapons of Mass Destruction (2026-11-05) - https://www.federalregister.gov/documents/2026/11/05/2026-22686/continuation-of-the-national-emergency-with-respect-to-the-proliferation-of-weapons-of-mass
- [federalregister.gov] **[official record]** Continuation of the National Emergency With Respect to Iran (2026-11-05) - https://www.federalregister.gov/documents/2026/11/05/2026-22685/continuation-of-the-national-emergency-with-respect-to-iran

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 10 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 3
- Evidence extraction: AI event extraction
- Confidence: **Medium**
- Fetch errors:
  - election_certification_interference: courtlistener: HTTP Error 401: Unauthorized
  - election_delay_or_cancellation: courtlistener: HTTP Error 401: Unauthorized
  - alternate_elector_scheme: courtlistener: HTTP Error 401: Unauthorized
  - politicized_prosecution_opposition: courtlistener: HTTP Error 401: Unauthorized
  - opposition_ballot_exclusion: courtlistener: HTTP Error 401: Unauthorized
  - court_order_noncompliance: courtlistener: HTTP Error 401: Unauthorized
  - judicial_review_foreclosure: courtlistener: HTTP Error 401: Unauthorized
  - independent_agency_capture: courtlistener: HTTP Error 401: Unauthorized
  - inspector_general_retaliation: courtlistener: HTTP Error 401: Unauthorized
  - military_domestic_political_use: courtlistener: HTTP Error 401: Unauthorized

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
