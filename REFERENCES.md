# References

External sources cited inline in `chapters/`, added during a citation-enrichment pass (2026-09-16) after a census found this book carrying zero real external citations. Every entry below was independently fetched and read before being cited — see `README.md`'s "What's synthetic vs. real" section for why IBM's own live `ibm.com/docs` pages could not be used as sources (they return a generic JavaScript shell to automated fetches, not real page content) and why this book's core platform-architecture facts trace to *The Detection Engineering Handbook V2*, Part 27, instead. The entries here are the exceptions: claims independently verifiable through a standards body or IBM's own public GitHub presence, which — unlike `ibm.com/docs` — loads correctly for automated fetches.

This is a new convention for this book specifically, since it had no prior citation of any kind; it follows the NESHBOY SOC Professional Library's existing practice (see the sibling *Detection Engineering Handbook*'s own `REFERENCES.md`) of citing a real source once in full here and naming it briefly inline at the point of use, rather than a numbered `[1]`/`[2]` scheme.

## External / Third-Party Sources

### IETF (Internet Engineering Task Force)

- **Cisco Systems, "Cisco Systems NetFlow Services Export Version 9," RFC 3954, IETF, 2004.** https://www.rfc-editor.org/rfc/rfc3954 — Cisco's own template-based flow-export format, cited to support the claim that NetFlow v9 is a real, specific, vendor-authored export format distinct from IPFIX and sFlow. Cited in: Part 7 (§2.1).
- **IETF, "Specification of the IP Flow Information Export (IPFIX) Protocol for the Exchange of Flow Information," RFC 7011, 2013.** https://www.rfc-editor.org/rfc/rfc7011 — the IETF standards-track protocol NetFlow v9 fed into; cited to support the claim that IPFIX (unlike NetFlow) is a formal IETF standard with generally richer field detail available to an exporter. Cited in: Part 7 (§2.1).
- **InMon Corporation, "InMon Corporation's sFlow: A Method for Monitoring Traffic in Switched and Routed Networks," RFC 3176, IETF, 2001.** https://www.rfc-editor.org/rfc/rfc3176 — the sampling-based flow-export alternative named alongside NetFlow and IPFIX. Cited in: Part 7 (§2.1).

### IBM (official public GitHub organization, `github.com/IBM`)

- **IBM, "qradar-mcp," GitHub, 2026.** https://github.com/IBM/qradar-mcp — IBM's own public Model Context Protocol server for QRadar; its documentation independently confirms the `SEC`/`QRadarCSRF` REST API authentication header pair (or an authorized service token passed as `SEC`) and the submit-search/poll-status/retrieve-results lifecycle for Ariel searches used in this book's illustrative REST API example. Used to corroborate that the illustrative example's *shape* matches a real, current IBM-maintained integration, not to override this book's own PRODUCT VERSION NOTE hedge on exact header/endpoint permanence. Cited in: Part 19 (§5).
- **IBM, "qradar-misp-ioc-importer," GitHub, 2023.** https://github.com/IBM/qradar-misp-ioc-importer — IBM's own public app that polls a MISP threat-intelligence instance and writes matching indicators into a named QRadar Reference Set on a configurable interval. Cited as a real, IBM-built example of the generic "denylist fed by an external threat-intel feed into a Reference Set" pattern this book describes. Cited in: Part 10 (§2).

## Verified but not used

Sources fetched and confirmed real during this pass but not cited in the end, either because the underlying claim was already adequately hedged with a PRODUCT VERSION NOTE or honest "not independently verified" language, or because no fetchable primary source could be found:

- **MITRE ATT&CK** (`attack.mitre.org`) — techniques T1003.001, T1078, T1059, T1110.003, and T1110.004, referenced by bare ID throughout `chapters/`, were each independently re-verified against their live `attack.mitre.org` pages during this pass and confirmed accurate. No inline URL citation was added for these, consistent with this library's existing convention (see the sibling *Detection Engineering Handbook*'s own `REFERENCES.md`, which does not carry a bibliography entry for routine ATT&CK technique-ID notation either — a bare `T1003.001 (OS Credential Dumping: LSASS Memory)` is treated as standard notation across this series, the same way a Windows Event ID is, not as an uncited claim).
- **LEEF (Log Event Extended Format) specification** — IBM's own LEEF specification document could not be independently verified through a live fetch; every candidate IBM URL tried (`ibm.com/docs`, `ibm.com/support`) returned either a 404 or a generic documentation-shell page with no substantive content. Part 4/Part 5's description of LEEF is left uncited rather than backed by a guessed or reconstructed URL.
- **CEF (Common Event Format) specification** — the original ArcSight/Micro Focus/OpenText CEF specification document could not be independently verified through a live fetch (the vendor's community/documentation pages returned empty or redirect-only content to automated fetch, and general web search did not surface a working direct link during this pass). Part 4/Part 5's description of CEF as originating at ArcSight is left uncited for the same reason.

## Internal — Project Governing Documents

Unchanged from this book's pre-existing internal cross-referencing convention — see `STYLE-GUIDE.md` and `BOOK-INDEX.md`, and each part's own "Cross-references" closing section, for citations to DEH parts, this book's own sibling parts, and this book's `STYLE-GUIDE.md`/`BOOK-INDEX.md` sections. Those are not duplicated here, consistent with how the sibling *Detection Engineering Handbook*'s `REFERENCES.md` separates external sources from internal cross-references.
