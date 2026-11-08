# Constitutional Risk Dashboard (0-100)

- Generated: 2026-11-08 12:25:11 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **17 / 100** (Elevated Strain)
- Previous day delta: **+9.0**
- Delta vs 7-day average: **+3.6**

## Interpretation
- Band meaning: Repeated norm-breaking attempts, but institutional checks mostly holding.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 2.00 | 11.00 |
| Judicial Independence and Rule of Law | 15 | 0.06 | 0.23 |
| Opposition Rights and Political Pluralism | 14 | 0.00 | 0.00 |
| Executive Constraints and Emergency Powers | 13 | 0.88 | 2.87 |
| Civil Service and Agency Independence | 10 | 0.00 | 0.00 |
| Civil Liberties and Information Environment | 10 | 1.33 | 3.33 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Election Administration Capture | elections_transfer | 3.00 (Orange) | ai | 1 | 4 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 3 |
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 1 |
| Legislative Bypass by Executive | executive_constraints | 1.65 (Watch) | ai | 0 | 4 |
| Emergency Powers Expansion | executive_constraints | 1.00 (Watch) | ai | 3 | 0 |
| Election Certification Interference | elections_transfer | 0.60 (Green) | keyword | 0 | 0 |
| Judicial Review Foreclosure | judiciary_rule_of_law | 0.25 (Green) | ai | 0 | 1 |

## Evidence Samples

### Election Administration Capture
- Assessment: Trump directing the Department of Justice to sue to block Senate election results based on partisan outcome represents a direct attempt to use federal executive power to overturn or invalidate election administration and results. This is a verifiable action (Trump directing DOJ) to subordinate election administration to partisan control by invoking federal litigation authority over state electoral outcomes. This constitutes serious, confirmed action to capture election administration through executive branch pressure on the DOJ to intervene in state elections on behalf of a political party.
- [ABC News - Breaking News, Latest News and Videos] Trump told DOJ to sue to block Alaska Senate results if Republican narrowly loses - ABC News - Breaking News, Latest News and Videos (2026-11-07) - https://news.google.com/rss/articles/CBMipAFBVV95cUxQekhpNnRhMmk3WnMteVlLeVRYT2ZMUGRnRkJmSlJxUU9TUm1GN1ZEYWp5SFRqS20tSWVtQWpUMF9VaWd3U1FFRUd1TDRBMk9UTXhpMkhHTlE4NnQzZDEyRjUxQ3lkYlVkZHAxTS05MjJkbDA2VXFNQVBhcGdmUVJ3LTRHTjBScTBucno5Y0NhazNCeWdiLWpJMUlTRjF2Uk5zRzE2SNIBqgFBVV95cUxQUEZqTzdWbGhCLTVzd1J1VlI1cUxOOWFyLXZIbDI0TnA1YXlWQXgyMTFtaXRMdE9jbTIzTXdkUmpXMzJkejdKeHlXc2lHYWVJd2t3WFVVTmNwS05BT2wzTjhkeW0tZ3FpU0Z5aUxmOFFCMWNydkk1S3hPT09xT2w1WWdjdG5ybXRhWl9FZV84TG5kOWM0YkZwNVVYWU9keUFfZWF1ZVIwRUs3UQ?oc=5

### Press Restrictions or Retaliation
- Assessment: ABC News reports that the Trump administration has targeted specific individuals including James Comey. This constitutes a real occurrence of state action that raises costs or legal risk (targeting by name creates reputational, investigative, or potential legal pressure). However, the report is limited to naming individuals targeted; without detail on the specific mechanism of retaliation (prosecution, removal from office, legal action, loss of license), the severity is contained at level 2 rather than escalated. A confirmed, orchestrated campaign with verifiable legal or official action would be severity 3+. This is credible press coverage of a real targeting action.
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-11-07) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

### Public Funds for Political Promotion
- Assessment: The item reports that a federal judge has issued an order directing the Trump administration to pull three taxpayer-funded advertisements featuring the president, characterizing them as 'purely partisan.' This represents a real, confirmed instance of public funds being spent on communications that promote the officeholder in a partisan manner—the core of this signal. The judge's order indicates that the ads violated the statutory bar on using appropriated funds for 'publicity or propaganda purposes' as interpreted by GAO. This is a contained, specific action with judicial confirmation rather than a structural constitutional failure or systematic pattern. Severity 2 reflects that this is a credible, confirmed stress signal of real but bounded significance—a judge had to intervene to stop the conduct, which demonstrates both that the violation occurred and that existing legal checks functioned to address it.
- [www.wonderwall.com] ‘Purely partisan’: Federal judge orders Trump admin to pull three taxpayer-funded ads featuring the president - www.wonderwall.com (2026-11-08) - https://news.google.com/rss/articles/CBMi0gFBVV95cUxPb21LbVZkbUhpdjBpV2xNUVFZRmZ3ZUhnTVkxcEJ1SFBZS1dCem1iUU94U0tHQzNQZl8tdVRMU3hIdjFQWXhoZUtxWmpnSEJULThzSUE0MGhqODNCN1pSYUVPaVVKZ3g4RE01LWVYbUk5cklFTVdobko1M1U5X0VZekxmOXpiY2RUVGVwNGxIck9vU3FKSWhJdUNCc0NtcmVVaGlHaXJIVE9uYmpPTW1UdGtVc1B3WTNVUUJjLWFsd3ctVHpKUUd1S1l6ZU9qWjBPdFE?oc=5

### Legislative Bypass by Executive
- [ABC News - Breaking News, Latest News and Videos] Appeals court blocks construction of White House ballroom - ABC News - Breaking News, Latest News and Videos (2026-11-07) - https://news.google.com/rss/articles/CBMinAFBVV95cUxNSW5aYzhFSU9YYUZ6dWtZZ3IxSXgxcXRkU3ZmX3dPeFdtOUpVRDFjMjNzTzB0SEptMnFxUkFtWmFXamYwenRTMTdoaVdYTU90OVlEd3V3blBqVVQtREx2NzJfT21ab012SE5kSVNjTzJGRkVfRklBcWt1WmhVX2RBdjA0V2JVdXlsVXU0NHNmTUtsdkh4ZjlpcUp1YzHSAaIBQVVfeXFMT1dUdHR5em8zNThqVVhUYXpLMDYzQ2pqZ1NtdTR2MXJxaDBHR1pZd0trbUc3TzJ1OEhweVRtRjRhNEotUXdtcC1RTTFZdXF5LXVPQzlmcUUyVW5JTWs2ZTBLRE1ZVDh3U3E5YVNPaHhxak1KZS1XU0JuYnpXaEhqb3RwMUZmc3ExYmN2NEhaMnBHMmRhSUMtY1RTTm1KU01VcVN3?oc=5
- [The Times of India] Democrats take back Congress after Republican wipeout: What lies ahead for Trump’s final two years? - The Times of India (2026-11-06) - https://news.google.com/rss/articles/CBMinwJBVV95cUxOMjFVWU9RYy1sYmFHNGszamxsMzhjdkx3VUNsMldCakY3dkF6Q280Tjh3ZzBPSEZXTjdiYzRneldWTHd1YklGS3F0R2tnSXZTaFBNMlZ1NmNsYWtNWDZDRzcwS1hzMDhfNV9zSjBxRHY5ZVNOUTlFUElCaFg3U0xrbzgydnM2VFFvWmRiQ280WENPenU3aTlISHNZMFZDTXhXRTBjMEprN01WVndDeUlFNlVTSWNVM1UxQkZTcTRDZlJQS1V2b3hfVzE2dWd3SFN6NzVub0FIMkhsWGlmYXNBY2hDN1JiY0l1cTJwN1FUbTJFOHdhZ0drUnpSVDcwYWdEOTZYaVg2N1l0QnNsaXJycjFnUURrX0Iya3kwdkN3TQ?oc=5
- [The Times of India] In foreign policy, why Donald Trump is not a ‘lame duck’ president - The Times of India (2026-11-07) - https://news.google.com/rss/articles/CBMi5AFBVV95cUxONlpBbmRoT2Qydll0ZEg0WVVSMzdYc2dCZ1pVcTNpX2JpUWhHN095WEpfbEhPTkE1N0xKenVVUjVGMG9JTF90WjFycF9oajNtTHhqblo3MFp5UzVGUzBOSzRGV2JzN2t3R0pSNnVXLVo5bUNjaF80dmgxSFJCeUlfNzNSRURqVW1HblBiLUJDMjctRnBPMUhrYVc2U1MwREQ4V01rNUFwSUViRWpBUVhxcW1ZTU1VblF0bEtvT0dUQmlSS0lCem9aX2xiUmFFTm9zZUlPQTNudE9PMnFGZVBfOTlvdlI?oc=5

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
