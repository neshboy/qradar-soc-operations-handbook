# QRadar SOC Operations

**Offense Management, Rule Engineering, DSM Onboarding, and Platform Operations — Running QRadar Beyond the Query Language**

📄 **[Download the full PDF](./QRadar_SOC_Operations.pdf)** — 259 pages, ~101,400 words across 22 parts.

Part of the **NESHBOY SOC Professional Library**, a sibling title to [The Detection Engineering Handbook V2](https://github.com/neshboy/detection-engineering-handbook) (DEH) and alongside [The SOC Manager's Operating Handbook](https://github.com/neshboy/soc-manager-handbook), [SIGNAL TO ACTION: The Complete SOC Playbook Handbook](https://github.com/neshboy/soc-playbook-handbook), and the [SOC Case Studies Casebook](https://github.com/neshboy/soc-case-studies-casebook).

DEH Part 27 (QRadar AQL) covers QRadar at query-language-comparison depth — AQL syntax, the Ariel `events`/`flows` model, and just enough of the Custom Rules Engine (CRE) to prove one claim: that QRadar's correlation model forces a three-object decomposition (Building Block, Reference Set, Rule) that a single-language SIEM implementation doesn't need. It was never meant to teach anyone how to run a QRadar deployment. **This book is that book.** It covers the platform-operations ground DEH Part 27 explicitly defers: offense management and scoring (magnitude/credibility/relevance), the full Rule Wizard catalog beyond one canonical rule, Building Block governance at scale, the complete reference-data type taxonomy (Set/Map/Table/Sequence), DSM and log source onboarding, custom properties, Ariel search performance, flow-vs-event architecture, dashboards and executive reporting, noisy-offense tuning workflow, rule change management without a git-based pipeline, licensing/EPS/FPM capacity planning, asset model and multi-tenancy, and QRadar-specific troubleshooting. Every part states its DEH dependency in front matter and cross-references DEH Part 23 (Query Language Strategy) and Part 27 (QRadar AQL) by section rather than re-teaching either.

## Reading the book

- **[QRadar_SOC_Operations.pdf](./QRadar_SOC_Operations.pdf)** — the assembled, print-ready book. Start here.
- **[BOOK-INDEX.md](./BOOK-INDEX.md)** — the full part table with per-unit scope, plus a "Key structural decisions and provenance" section recording the scope boundary against DEH and why this book renamed two of DEH's six content tags.
- **[STYLE-GUIDE.md](./STYLE-GUIDE.md)** — the voice, formatting, object-notation, and figure-evidence-classification contract every part follows: six content tags (`[CONCEPT]`, `[ANALYST]`, `[RULE ENGINEER]`, `[PLATFORM ENGINEER]`, `[THREAT HUNTER]`, `[SOC MANAGEMENT]`), nine recurring callouts (Rule Autopsy, Hunter's Note, Platform Reality, Blind Spot, Noisy Offense Trap, Validation Test, SOC Management View, What Would Change My Mind, and the QRadar-specific PRODUCT VERSION NOTE), and — critically — §0 and §9, which state and operationalize this book's evidence constraint (see below).

## What's synthetic vs. real — read this before citing anything as current

**No real QRadar deployment exists in this book's author's lab.** DEH could stand up Sysmon, a domain controller, an SSH host — commodity lab infrastructure on demand. QRadar is a commercial SIEM with licensing and appliance/cloud costs well past what a solo author's lab supports for a full multi-node deployment. That constraint shapes every figure and every specific claim in this book:

- **Evidence is restricted to two classes: `OFFICIAL REFERENCE` and `CONCEPTUAL`.** `CONTROLLED LAB EXAMPLE` and `REAL LAB EXAMPLE` — a real captured console screenshot — are not used anywhere in this book, because that evidence does not exist for this project. Every diagram is either sourced and cited from IBM's own public documentation (`OFFICIAL REFERENCE`) or an honestly-labeled illustrative diagram this book drew itself (`CONCEPTUAL`, the default for anything not sourced from IBM). No synthetic console mockup is styled to look like a captured screenshot.
- **IBM's own public documentation was largely unfetchable during authoring.** The plan was for `OFFICIAL REFERENCE` figures and claims to trace directly to IBM's QRadar documentation. In practice, most of that documentation could not be retrieved while writing this book. As a result, this book's core technical facts — the CRE's Building Block/Reference Set/Rule decomposition, the Ariel `events`/`flows` model, the offense-scoring architecture — trace back to **The Detection Engineering Handbook V2, Part 27 (QRadar AQL)** rather than to independently fetched IBM sourcing. Part 27 is cited by section throughout rather than restated, per this book's own DEH-boundary rule, but readers should understand that DEH Part 27 — not a fresh pull from IBM's docs — is the actual evidentiary backbone underneath most of this book's platform-specific claims.
- **QRadar moves, and this book says so on every claim where it matters.** Console navigation, Rule Wizard wording, the DSM catalog, and QRadar's own packaging/delivery model have shifted across release cycles this book cannot track from outside a live deployment. Every part uses the **PRODUCT VERSION NOTE** convention (`STYLE-GUIDE.md` §11) to flag a version-sensitive claim explicitly rather than asserting a menu path as permanent fact.
- **Diagrams are original Mermaid flowcharts**, rendered to SVG and committed alongside their Markdown source (`STYLE-GUIDE.md` §10). None claims to be a reproduction of a specific IBM-published diagram unless captioned as such.

If a future edition gains real, authorized access to a QRadar instance, `CONTROLLED LAB EXAMPLE`/`REAL LAB EXAMPLE` evidence becomes usable and this section (and `STYLE-GUIDE.md` §0/§9) gets revised to say so — that has not happened yet, and this book does not pretend otherwise.

## How it was built

- `build/build_book.js` — parses `BOOK-INDEX.md`'s Part Table, assembles all 22 chapter files into one HTML document (stripping YAML front matter, resolving image paths, colorizing the six content tags), and prints it to PDF via headless Chrome. Appendices A1–A3 are listed in `BOOK-INDEX.md` as planned but not yet authored, so the build intentionally stops before the Appendix Table rather than emitting placeholder pages.
- `build/render_mermaid.py` — renders every embedded ` ```mermaid ` source block under `chapters/` to SVG and inserts the image reference immediately after the source block. Idempotent: it skips any fence that already has a rendered image tag following it, so re-running it after a partial pass never double-inserts.
- `build/add_watermark.py` — applies the diagonal `neshboy` watermark to every page.

## Rebuilding it yourself

```
cd build
npm install
node build_book.js
"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer ^
  --print-to-pdf="..\_build\QRadar_SOC_Operations.pdf" "..\_build\book.html"
python add_watermark.py
```

## Repository layout

- `chapters/` — the 22 parts, Markdown source of record.
- `appendices/` — reserved for A1–A3 (QRadar Terminology Addendum, Rule Wizard/Rule Test Quick Reference, Troubleshooting Decision Trees); planned in `BOOK-INDEX.md` but not yet authored.
- `assets/diagrams/` — rendered Mermaid SVGs, one per figure referenced in `chapters/`.
- `build/` — the build/render/watermark tooling above.
- `BOOK-INDEX.md`, `STYLE-GUIDE.md` — cross-cutting project documentation: the canonical part list/provenance and the voice/formatting/evidence contract every part follows.
