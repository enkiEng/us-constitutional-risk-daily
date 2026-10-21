# Constitutional Risk Dashboard (0-100)

- Generated: 2026-10-21 12:42:17 UTC
- Methodology: **v2** (extraction: AI event extraction)
- Score: **13 / 100** (Baseline Institutional Noise)
- Previous day delta: **-1.0**
- Delta vs 7-day average: **+3.0**

## Interpretation
- Band meaning: Normal democratic conflict and routine legal contestation.
- Signal scale: 0=green, 1=watch, 2=yellow, 3=orange, 4=red.
- Formula: domain severity = max(mean signal severity, max signal severity - 1); domain points = domain weight * (domain severity / 4); total score = sum of domain points, then raised to any active trip-wire floor.

## Domain Breakdown

| Domain | Weight | Severity (0-4) | Points |
|---|---:|---:|---:|
| Elections and Transfer of Power | 22 | 0.65 | 3.57 |
| Judicial Independence and Rule of Law | 15 | 0.00 | 0.00 |
| Opposition Rights and Political Pluralism | 14 | 1.00 | 3.50 |
| Executive Constraints and Emergency Powers | 13 | 0.00 | 0.00 |
| Civil Service and Agency Independence | 10 | 1.00 | 2.50 |
| Civil Liberties and Information Environment | 10 | 1.33 | 3.33 |
| Security Sector Neutrality | 8 | 0.00 | 0.00 |
| Federalism and Legislative Oversight | 8 | 0.00 | 0.00 |

## Highest-Risk Signals Today

| Signal | Domain | Severity | Source | Confirmed | Coverage |
|---|---|---:|---|---:|---:|
| Opposition Ballot Exclusion | opposition_pluralism | 2.00 (Yellow) | ai | 2 | 5 |
| Public Funds for Political Promotion | civil_liberties_information | 2.00 (Yellow) | ai | 2 | 4 |
| Press Restrictions or Retaliation | civil_liberties_information | 2.00 (Yellow) | ai | 1 | 2 |
| Inspector General Retaliation | civil_service_integrity | 2.00 (Yellow) | ai | 1 | 1 |
| Civil Service Purge / Schedule F | civil_service_integrity | 2.00 (Yellow) | ai | 3 | 0 |
| Election Administration Capture | elections_transfer | 1.65 (Watch) | ai | 0 | 3 |

## Evidence Samples

### Opposition Ballot Exclusion
- Assessment: Corroborating report of the same ballot-exclusion event: North Miami Mayor Alix Desulme was disqualified from the ballot during early voting. Confirms that an opposition candidate (sitting mayor seeking reelection) was removed from meaningful electoral participation. Severity remains 2: the event is real and credible, but the disqualification appears grounded in stated compliance reasons rather than demonstrating systematic removal as policy or constitutional defiance. Single incident in one municipality, not evidence of structural pattern.
- [Miami Herald] As early voting begins, North Miami mayor is disqualified from ballot. Here’s why - Miami Herald (2026-10-19) - https://news.google.com/rss/articles/CBMimAFBVV95cUxNNVZnSDZoMEpjenU1aWNwQ3pDaHZBcE4yVF9XQ2l3SzZwS2ZxRjRmQ1VNdEgtU29GbzRETml3TVZWSWlZRUhRMHNfaHg5bElSWHFsT05veXFfdFdSMXhUbzVVQ1dPYTRqS29rQ1JEby15eGFoYjNyMldST0hJWHFVLTNFZjQtQl9QUi1MUmRpZlZQeFZBV1lhQtIBmAFBVV95cUxOQ2FTam5BRFhoUzROOU9yWkZmbmdfSzNmenB0NUY3aVJPSGdCa2dnbnVUUTNHWXgyNlUwbEFucUpiYkU3Q3NDLUZaSlI3NHRIRHU0XzZSU1ZTT2JLSmdFajlhazZTNmk2NXdkRDdHaVN4Q1Mtc2lDSGtHbk5VX3QwUXlldDdEUjd6RHNxVXBYbDRiWGFybkx3Rg?oc=5
- [Caribbean National Weekly] North Miami Mayor Alix Desulme disqualified from reelection bid over cashier’s checks - Caribbean National Weekly (2026-10-20) - https://news.google.com/rss/articles/CBMiygFBVV95cUxNYlBRalpTU0pMQ0JnV0pEeFJJNVNXbzJOZzJGQWVIeFlhQUZfWFhtT3VxSzhuMlNSSnZCTHYxX2tRMzl0djFSNlo3U2ZQQlV1ZVFEci1fOEowYUhKb3g3dkF3ZmNpWXlGdzBLQTNJQkRsR0s4UHBDSjE4bDZhRkplVnVlcXY0bVBnbkJZcEJKck92c1Bra2ZraWZkc2VDbk1ZTE9xbWhzNkhMVjlrY0RDeXBzM0dJc0NadHJ4S2xzOTI3LTkzdHlxTTNn?oc=5

### Public Funds for Political Promotion
- Assessment: News report alleges that taxpayer funds were spent on pro-Trump TV advertising. This directly matches the signal definition: public money spent on communications promoting an officeholder in campaign-style format. The item identifies a real action (ad production and air time) funded by public money, not merely a proposal or concern. However, without access to official documentation or GAO finding, confidence is moderate rather than high. Severity 2 reflects a credible, repeated-pattern allegation of actual misappropriation affecting a discrete campaign cycle, not a structural failure or ongoing regime.
- [ABC7 Bay Area] Administration's pro-Trump TV ad is taxpayer-funded - ABC7 Bay Area (2026-10-20) - https://news.google.com/rss/articles/CBMi-BRBVV95cUxPZy1OcjhHUXR4TDFzNGZkRm14Vno2STM1U1FkQURyY1ZWWmFnYXFNeGJNTVEwYW8wOW8zVDYzX19yZEVPa0UtVUs3cDhhYk1MX19hMC1RQlhCWEh6Y1NlY18tOGFYaGk4T0J2alhFSDJGNHdGRU5ZLTBHNFZzcEpiODdCaG9iMVhLek52YTFXU0d1T2t6a2R3VzBzTUxZZlJud1RCSTVyTDhPN0tkWUVCTFFFQ21LYkx5WXZsZkVKQ3h6SlJQQmd5NVAwV3g0aGNqSlU4SFVTODNxWmcycUJNYmROVjBkM0hvR0xVampDX3ZQUmZyMWJ1YkhjVXlobkZ5dGVmWW1FcGpGTzdNazhtQVhZYWl1X0lvM0RkTFhja3Bnc21EZE52cTlwclpPcEExQjlyeGZ5TExacmJuWXo2VnVTQm94ajNWNl9hdXdIVHgzR0QxTjFERk9OWThmYWZWd0dCc0lvY2phaDZCbFF1RWY3SERSQTRtSXVmVGNYbTE0TkdKd0k0NENFbmk2VTJEUlRMR0JRc3pac2pxSFg0VG1KVnAyS0JEZG13dFcwN3hld2F4VGxRX1JVRFZvQUVqckJ4VjNNaFVrUERHVzcyWXpTZGo1bXBUUFdadS1IQ3pSZkFka1pDeTg0VVpPRWJtSHdQd0pqa2QwRmFfT1JuV0cwd2RuRFhqcHJ3RkVuc3Z4NWtkWjRuRXBRWWtpbExFS2ZkeE5oX0xUOEVDT0pSeWhic0lRaUVtZlI0U2lEandERzBxWkwxSFphSVR4WGR6d1pzamRfVENBdklyajJqbUJQdWRsMHc5ekVMMW8zY20wMkNBUEJ5UlVXVXFFaUd0VkJKakZqNVBtdEFtdUoySVp3Zkh6X1lwMG1rRHZwXzJpT0o5aTZNYUhveTNkOVktN053U3RxZUZMTjB4V0RVbHUyZDEwTVZsWTMtTXBRSnh0QTlYU2lnTU13WE83R2ZnbVB0ZnNCLUQwQ1lmV1Zid01GWUxiZlNlbVNUSEtWNWFHVko5dVZIYWJadUJVNGQ2YTJWa3daSlMyUFctV0NCeXRCWjdCcjJ4aDNjOU1uTWlkbHNiWWdHZXMtUHdDV1YwT0pteC1EYUtoTXRaVnV2RGVsSzRNdWJLZnd4UFV3dEZjeWQyc3dudFhkZ3JWdUlLNDA1YVBsaGl5ZE5aLW9lWHNULWtoTlFSV2k2U2NGMF9pR1Z2eloyR2NVazFXdy13dzlPZ081OUxpODZOX1o4WHVoMnc2N0FFUnl3MVVJaVVWUWhQaVpmUkhVLUFIVVdnRXNIRWJKY1lhZ2JZOU5VdmxHWFF5VHhFMWl6MGZSVFJiWkNRRTZESThkSDNYMU5RelBCM3kxRG1kVXhaVlZHUDU3WklCTVV5U05vRDdjZDhyUzBFSGZNZ1h2STYtelREcEZyY2VHS0lTcUdKNFhFeHBPakZPRG0xVV9CTk1CY2tVNUNZUWloRUNFU2xaRWFSSXpUczBTMTFWclR6ZFVJUS1iSnNOYy0waVBmcXBra25rS1pJc0EwZllFN0o5dTctYlIwUHEtcVRQTWxlLVdlSTFLU0dxY2FkSGRTaThjc2ZqWEpFaU5SMGlmREo4T1F3dXdaSFc1Y2REemZ1bTNnR1JrT0E0bjNZbXhfa2hzeEFsR3NSQU9jX0lEWlNtVDhJMUFudktVVXdCZE1RTS11Sng0cE8xQU9ZaEktWjhhMVRoSnY0VnZCOHBGSUd0anRqVl80SnQxR0xndmxiWF9SVDBwVkVqT0l6T0t2VjF0dnJTODZyaEQ4c1JtXzZsak9XWENvdVFwbklfS0c0Zk9rdG1jRkxTZnVjemUzMktrdW5McGJkbzMtZGJWLTREamU2NXY3ZnBtWkNSYWFKUE9xcmFsc01aUjhUckx2cnNNcUdVblJaOFpSQUpaaTJreW9CbG9GX2VoaUNTX29vU1FOcHBwUjZROHlLYkRuUXVYMGt5QXZmRGpnVF9HbnlRZjN0RzltLUd2QWdSZU56ZnVrOERaSTNDdnRidFdRZEpQblAxZ0Y5cXZxcmRPc2dGUjBMM25Yc0FLVjkwOGhjTlJEcktIZV9VaTdtMm1jRDdPajJrUXhmYXdjRzRMUkFlR3NQVU9ZNFZfQUpscER6RmJRdmt5ZC1EVVFxVzVrS3hNZEIyT2g3cEtLbGVfODR4V3ZTbHNPSzFJUnV1UUxPbjIxSjRFNlFkaGthYzY3SmI5V2VWNDNTbTY0VXVXOWhlMXhIX3BGY0VLSlRhZFFHWTlrc3JRdDA4QVJSZlNwX0tyVC1ncTZlZC11SHBTQktnTkZrVW5OUzJTal9VVHlaazRFNkRGRHo2Y2pwckowQmE5Vm5tY1Nvd1RCM0lBV3hsbGRhLWFoLVcxVjhLVWFjODRLbGdxQjZ3NzdWQWVhVzhRV3NianB5OEticUloMXh4eEQ2aElTT1M5bE5wa2RvRmRhQzV2alRzN0Vnc2d6ME5Cc0tWX1NSTVNyUHpGMWo2Z3ZYTkdmUTEzc2xqbm9rNFM2UFNUNUlfWXVaSnJLWG9TNl9MN2N3SWcyc2VkaFNiU3VRSEdueFR1YUlNMWUxWVBEM1kzQ0F5cFZjOW8yQVQweXJNTGRCNm5FOVFsQ0tLYUlYZWtnYjA4NEh0dFdUQ3lWd0tBdkRpZ3IwNFdrbVV5QkM0VXZ0dmpIZlNySEJMNWcwOE1sd3E4TmZXVWd4eGlkaHAzMXVfYU84Q2QybnF3endxOHdTVWxKQzJoYzdHQkZPaUhUdGEyM1MwU0drV3R1TE5OTmxtaDBQQUdvZzUxVmtaYk9vTm02cFFKRUxRcjJiVm10bng2R3NXQmQ1N1BSV2lCVC1GS3FhalpHTGdscEJqeUZ3RDZ5NUk3Q0RZS1JSbm9WVzNkUC1JWmdhRjg0aW1zanZ1MHVvclpVSWFkeldYd2toTU9yenRuYjVQWkl4U0NFMzlMZVh1ZEtLZGtDQTczd3FGS3QwSGxhRXVxQXA4bGpIbjllZzkyelRFcnBCa2NRN2ZfcjVtai1xQUdCa3JYOXAyeTdyeF9QRjMtalM2Q1RLREVsMFpxVXo1eDZrOGFTemszTnJkOWxvVkRnLUM0TlZHUVpVc2hjalN1S2xSd1V2WHRIMmJJcEF4b0lfb1BUVnFnRWVHZWpaNXVJU3M0VmplbW92ZDVmb3NqX2x1WHpPTmR6LVAtRWtab1k3Rld3b3V3c2dZdlFTM3ZsdHI4Nk5aTFZDTTROSGluNVR5Z0FtZGNfR1JjZ1pBVGJ6SGVmdnJhc0lVWFZRd2ZDcmswZmpCWGFqR3had0FBbmZtbVFBMTg2Z1RhZC1YTEtQWDBIalVMSHZqdXowaEYzRnFQRmxVaHpNSnZ0WE9XWVowUUdicnIwcnFnT2ZSWlByc3NvVWIydlpMMi1CV084NjdfRVhidDU0d3lOQzNDMTZZTkIwTE9FLXBnd0xNcmtaSlFQNWhGYjFsdl8tcXhCNGdKaWN6YzhtUllPdTFXV204d3VmQmZxV1VqYjNIS1pSMEpGRjhneEJiajkxYVdybEREUldpM2Fx?oc=5
- [The Independent] Trump used taxpayer funds to make campaign-style ads — and now his super PAC is running them - The Independent (2026-10-20) - https://news.google.com/rss/articles/CBMiswFBVV95cUxOZ2tDYlVsX1dSRXZsMXB6ekduT0oxanp3TDlvWUJiZk5wejNJSENWOFJQeWpwMFFLX3JvUFBfMEpycjlYN0hPcWV2Y3A4U3FaTl9CZDg3a0JQR3ltYThpcU1uM2UwY3lBZlhlcHY2NC1LNVJpeEFCbE5hUE84bnlseWprVUdnbTlhb283MzdKWHRpY1VubVloalBYSHlrdm1vdE5OMlVfckhmQm1mLW5JeHZ2RQ?oc=5

### Press Restrictions or Retaliation
- Assessment: ABC News reports that the Trump administration has targeted specific individuals including James Comey. This constitutes a real occurrence of state action that raises costs or legal risk (targeting by name creates reputational, investigative, or potential legal pressure). However, the report is limited to naming individuals targeted; without detail on the specific mechanism of retaliation (prosecution, removal from office, legal action, loss of license), the severity is contained at level 2 rather than escalated. A confirmed, orchestrated campaign with verifiable legal or official action would be severity 3+. This is credible press coverage of a real targeting action.
- [ABC News - Breaking News, Latest News and Videos] Here's a list of the individuals, including James Comey, targeted by the Trump administration - ABC News - Breaking News, Latest News and Videos (2026-10-19) - https://news.google.com/rss/articles/CBMirAFBVV95cUxQeDV4U3lXWlRPTHY5M1ljNzBTUEdlZEx2R2c5N1VSQ0NSLXAxbUp5bW1PREhFV2YtX3VaX0JnTWQteGJHazFYWE9vdXp2ZDVrTkdmREhLVWpkVXUtN0tQQUZfdVNFYUFKWmxWdEZ4a3NfelpMS2lNWjc2V3hpcWdoeldIOHFTRkNRU2hmdV9yNmFVd0NBNmt6U0JiZVU0NUJEeHpkLXo4QThUaWlk0gGyAUFVX3lxTE9nUFNSZ0VyeGtKYkluY181dEdkR3lvdlZNck83dWlhbXAyMzA4aTI3Um8tY01RdkVGWkVDLVhuTUg2b2dDXy1jbFpHMjBnLWZBYm0yV3lLeG9ZSWRUOG56U24xd05NTlBEM2JhMktaaFR4a0VacURFckVIOTFqT2dlNGdKa2Z5ZC1MN2FNUFdIdWNvTWxabG9lMVlmY1owNjF6NlM5VGU3NDRMT29zdUJCcXc?oc=5

### Inspector General Retaliation
- Assessment: The headline and summary indicate an allegation by VA employees that Trump's IG nominee is 'watering down' oversight. This constitutes credible reporting of a real action or pattern (reduction of IG investigative scope/rigor) by an executive appointee toward watchdog functions. However, without detailed reporting, this appears to be one newsroom account of employee allegations rather than multiple independent confirmations of a systematic removal of safeguards. Scored as severity 2: a real but isolated or contained signal of IG function impairment, not yet a confirmed structural failure. The action alleged (reducing oversight intensity) has reportedly occurred, but the scope and persistence require closer monitoring.
- [GovExec.com] Trump’s IG pick at the VA is ‘watering down’ oversight, some employees allege - GovExec.com (2026-10-20) - https://news.google.com/rss/articles/CBMi0gFBVV95cUxQY1JHWDlFcEZ6SF84WXdYRkxaa3h3X3Biek1WbXZpZkNsNzk2eGk2S0pWUFZ1cHkxRUI3cXctNjZqSmZrdktMSml3X254VWhhS0ZZT1RFTTExZ1M4YUVrY3Rnb1I2QWw0UU9ROUFuOVQ1ZWt1SWRFRHBRa3pnbWFRVnRNNlpIZW5zUkpzWHdRZ0xPdDdlY2dDMUV6eFJhVkZQam9tSmRkZ2dFb0steks4SzItRVVWVTFSZXpQQW5UMlRHZEZRNW9tUUVud3ppNVRpYmc?oc=5

### Civil Service Purge / Schedule F
- Assessment: Final rule issued by OPM expanding the scope and legitimate uses of administrative leave, including explicitly for 'workforce realignment initiatives.' This is an accomplished regulatory action (not a proposal) that creates new legal authority for executive discretion in removing or repositioning civil servants. Administrative leave can facilitate workforce removal without competitive process protections. Severity 2 because this is a real, confirmed action that materially expands tools available for politicized personnel actions, but it is a procedural/regulatory change rather than a demonstrated mass removal or targeted purge yet executed.
- [federalregister.gov] **[official record]** Administrative Leave for Workforce Realignment and Other Purposes (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21320/administrative-leave-for-workforce-realignment-and-other-purposes
- [federalregister.gov] **[official record]** Elimination of Time-in-Grade (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21319/elimination-of-time-in-grade
- [federalregister.gov] **[official record]** Managing Senior Professional Performance (2026-10-19) - https://www.federalregister.gov/documents/2026/10/19/2026-21316/managing-senior-professional-performance

## Data Quality

- Query feeds attempted: 25
- Query feeds successful: 25
- Query feeds failed: 0
- Primary-source lookups: 22 signals, 22 official documents (Federal Register, CourtListener)
- Primary-source confirmations: 3
- Evidence extraction: AI event extraction
- Confidence: **Medium**

Use this score as an early-warning indicator. Confirm high-severity changes with primary legal documents, court orders, and official records.
