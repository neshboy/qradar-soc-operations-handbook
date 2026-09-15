# QRadar SOC Operations — STYLE-GUIDE.md

**Status:** Adopted before any part is drafted.
**Series:** NESHBOY SOC Professional Library — sibling title to *The Detection Engineering Handbook* (DEH), `C:\Users\User\projects\detection-engineering-handbook\release-v2\`.
**Applies to:** every part, appendix, figure, and callout in this book.
**Audience:** every writer and reviewer working on this book.

## 0. Why this document exists, and the constraint that shapes all of it

This book sits one layer inside a single platform from where DEH Part 27 (QRadar AQL) leaves off. Part 27 teaches AQL syntax and introduces the Custom Rules Engine (CRE) only far enough to prove one point: that QRadar's correlation model forces a different detection design than KQL or SPL. This book is the rest of running QRadar — offense scoring, rule/Building Block/Reference Set authoring at real scale, log source and DSM onboarding, Ariel performance, dashboards, tuning workflow, and platform troubleshooting. It does not re-teach AQL syntax (DEH Part 27 §1 owns that) and does not re-argue Sigma-first-vs-native authoring (DEH Part 23 §5 owns that). Every part below states its DEH dependency in front matter and links to the specific section it builds on rather than restating it.

**The constraint that governs every figure and every specific claim in this book: no real QRadar deployment exists in the author's lab.** DEH could stand up Sysmon, a domain controller, an SSH host — commodity lab infrastructure. QRadar is a commercial SIEM platform with licensing, appliance sizing, and (for a full multi-node deployment) hardware or cloud spend well past what a solo author's lab supports on demand. That means this book's evidence base is structurally different from DEH's, and §10 below exists specifically to keep that honest rather than papered over with invented screenshots. Two consequences follow immediately:

1. **This book's figures are almost exclusively `OFFICIAL REFERENCE` or `CONCEPTUAL`** (see §10). `CONTROLLED LAB EXAMPLE` and `REAL LAB EXAMPLE` are not banned outright — if a later edition gains access to a real instance (IBM has, at various points, offered a limited-EPS trial/Community Edition VM; verify current availability before relying on this), those classes become available and should be used. Until then, a figure claiming captured evidence this book does not have is a worse defect than an honestly-labeled diagram.
2. **QRadar is a fast-moving vendor product**, and its console navigation, Rule Wizard wording, packaging (on-prem vs. cloud/SaaS delivery), and even ownership/branding have shifted across release cycles and business decisions outside this book's control. §12 formalizes how this book flags that risk on every claim where it matters, rather than asserting a specific menu path as permanent fact.

Everything else in this guide inherits DEH's core conventions where QRadar gives no reason to deviate, and deviates explicitly, with a stated reason, where it does. Where this guide is silent, DEH's `STYLE-GUIDE.md` governs.

---

## 1. Voice and Tone

Adopt DEH `STYLE-GUIDE.md` §1 in full — the core rule, the banned-filler table, and the worked GOOD/BAD examples all transfer unchanged; nothing about writing for a SOC audience is different because the platform is QRadar instead of a query language. Retarget the examples, not the rules:

- Write like a QRadar admin explaining a tuning decision to the analyst who'll be paged when the next flood of offenses hits — not like an IBM datasheet.
- **Prefer the concrete number.** "A `BB:` library that's grown past 400 unreviewed Building Blocks over three years" beats "a large and unwieldy rule base."
- **Name the object, not the category.** "The Reference Set `RS-Allowlisted-LSASS-Tools` has no TTL configured" beats "reference data can accumulate."
- **Commit to a claim, and flag version uncertainty explicitly rather than hedging generically** — that's what §12's PRODUCT VERSION NOTE convention exists for. "This menu path is current as of QRadar 7.5.x; earlier and later releases have moved it — verify in your own console" is the honest form of uncertainty this book uses. "This may vary" alone is banned filler exactly as it is in DEH.

One addition specific to this book: **do not describe a QRadar UI action ("click Admin, then Network Hierarchy, then...") with the false confidence of a captured screenshot behind it.** Either the claim is stable release-to-release and stated plainly, or it's a specific navigation detail and gets a PRODUCT VERSION NOTE. There is no third option where an unverified navigation claim is stated as bare fact.

---

## 2. Heading Level Conventions

Identical to DEH `STYLE-GUIDE.md` §2 — H1 for the part title only, H2 for numbered major sections, H3 for named subsections (a specific rule type, a specific troubleshooting scenario), H4 rare. Every part opens with an unnumbered `## Why this part exists` before `## 1.` starts, exactly as DEH requires. Section titles are sentence case; part titles are title case with an em dash (`# Part 8 — Ariel Search Performance and Tuning`).

One QRadar-specific heading pattern: when a named QRadar object gets a dedicated walkthrough, format the heading as the object's own name, not a paraphrase — `### BB:LSASS-Access-Candidate — anatomy of a Building Block`, not `### A building block example`. This mirrors DEH §2's Event ID heading rule (`### 4624 — An account was successfully logged on`) for the same reason: a reader jumping in via the index needs the heading to be the greppable token, not a description of it.

---

## 3. Code Block Conventions

Adopt DEH `STYLE-GUIDE.md` §3's table and rules in full, plus the following QRadar-specific additions DEH's own table leaves implicit:

| Content | Fence tag | Notes |
|---|---|---|
| AQL (Ariel Query Language) | `` ```sql `` | Matches DEH Part 27's own precedent exactly — no renderer has a distinct AQL lexer, so AQL borrows SQL's generic highlighting. **Every AQL fence must carry the same disambiguating comment DEH Part 27 uses on first appearance in a part:** a one-line comment stating this is AQL, not standard SQL, and naming the specific non-SQL behavior relevant to that block (no general-purpose `JOIN`, `LAST n HOURS` shorthand, etc.). Do not invent an `aql` fence tag. |
| QRadar REST API calls | `` ```bash `` (for `curl`) or `` ```json `` (for request/response bodies) | Never mix a `curl` invocation and its JSON response in one fence — split them so each carries the correct tag. |
| DSM extension XML (regex-based log source extensions) | `` ```xml `` | Only if the excerpt is valid, complete XML; a truncated or annotated excerpt uses `` ```text ``, same rule as DEH §3's raw-log-excerpt row. |
| Rule Wizard condition text (a Rule Test's literal on-screen wording) | Inline code, never a fenced block | A Rule Test is UI-composed, not authored as a file — quote its wording with backticks inside prose, e.g. `` `when at least 3 events are seen with the same source IP and username in 5 minutes` ``, exactly as DEH Part 27 §2.1 already does. Fencing it as if it were a query language misrepresents how it's actually built. |
| Reference Set / Reference Table contents (illustrative) | `` ```text `` | Never `json`, even though the REST API returns reference data as JSON — a body-text illustration of *values in a set* is not an API payload; reserve `json` for actual API request/response examples. |

DEH §3's framing requirement — every real query preceded by a platform/version sentence and followed by its main limitation or a pointer to the callout that names it — applies unchanged, and is the mechanical enforcement point for §12's PRODUCT VERSION NOTE convention: if a code block or UI-navigation claim is version-sensitive, that framing sentence is where the version note belongs or is linked from.

---

## 4. QRadar Object-Naming and Notation

DEH locked down Windows Event ID and MITRE ID notation because V1 drifted on both. This book has an equivalent drift risk around QRadar's own object vocabulary, which is why this section exists as a first-class addition rather than folded into prose:

- **Offense** is capitalized as a formal term when referring to the QRadar object (`the Offense's magnitude`, `a new Offense`) and lowercase in ordinary descriptive use (`three offenses fired overnight`) — the same convention DEH `TERMINOLOGY.md` §"Capitalization" already uses for its own glossary terms, applied to this book's platform-specific vocabulary.
- **QID**: always the bare acronym, never expanded to a full phrase mid-sentence after first use. First use in a part: "QID (QRadar's internal event-taxonomy identifier)," per DEH Part 27 §1.2's own introduction. Subsequent uses: bare `QID`.
- **Building Block names** are always written with the `BB:` prefix exactly as configured, in inline code: `` `BB:LSASS-Access-Candidate` ``. Never invent a Building Block name without the prefix — a name without it reads as a generic concept, not the object.
- **Reference Set / Reference Map / Reference Map of Sets / Reference Map of Maps / Reference Table names** are always written with the `RS-` prefix (or the equivalent prefix your example has established for a Map/Map of Sets/Map of Maps/Table) in inline code: `` `RS-Allowlisted-LSASS-Tools` ``. State the reference-data *type* (Set vs. Map vs. Map of Sets vs. Map of Maps vs. Table) at first mention in a part — they are not interchangeable, and Part 10 covers exactly where each type is the right choice.
- **Rule names** are always written with the `R:` prefix in inline code: `` `R: Suspicious LSASS Access — Unapproved Process` ``. This matches DEH Part 27 §3.3's own naming convention exactly — do not diverge from it.
- **Log Source Type / DSM names** are quoted exactly as QRadar's own `LOGSOURCETYPENAME()` would render them, in inline code with quotation marks preserved where QRadar's own UI uses them: `` `'Microsoft Windows Security Event Log'` ``.
- **Never abbreviate "Custom Rules Engine" to an unexplained acronym on first use per part.** Spell it out once ("the Custom Rules Engine, universally abbreviated CRE" — DEH Part 27 §2's own phrasing is the model), bare `CRE` after.

---

## 5. MITRE ATT&CK ID Formatting

Adopt DEH `STYLE-GUIDE.md` §5 verbatim — this book makes MITRE claims about the same techniques DEH's domain parts already map, and a second, slightly different formatting rule for the same ID space is exactly the kind of drift both books exist to prevent. Short form: `T1003.001 (OS Credential Dumping: LSASS Memory)` on first reference per section, bare `T1003.001` after; a standalone `**MITRE:**` line always spells out every ID in full regardless of prior mentions; never invent or guess a mapping.

---

## 6. Callout Boxes — Nine Templates

This book keeps DEH's base callout *mechanism* unchanged — a blockquote opened with a bold label, 1–5 sentences, never nested, never a heading — and adapts the *set* to an operations audience. Five of DEH's eight carry over with a renamed lens; three are dropped or merged because their DEH framing is specific to cross-language detection authoring, which is not this book's job; one is new. Nine total.

| DEH callout | This book's callout | What changed and why |
|---|---|---|
| Detection Autopsy | **Rule Autopsy** | Same four-part structure (**The rule / Why it shipped / How it failed / The fix**), retargeted from a naive detection-logic pattern to a naive QRadar *configuration* pattern — a Rule, Building Block, DSM mapping, or Reference Set policy that shipped broken. DEH dissects logic; this book dissects platform configuration decisions logic alone doesn't capture (a missing TTL, a `BB:` referenced by name after a rename, a DSM extension nobody re-tested after an agent upgrade). |
| Hunter's Note | **Hunter's Note** | Unchanged. AQL/Ariel ad hoc search pivots and offense-to-event drill-down tips, extending DEH Part 27 §5's hunting pattern into full platform practice (saved searches, pivoting from a fired Offense rather than starting cold). |
| Engineering Reality | **Platform Reality** | Renamed to match the [PLATFORM ENGINEER] tag (§8). Same purpose — documented/expected behavior vs. what production actually does — retargeted from telemetry-pipeline plumbing to QRadar's own platform behavior: licensing overage handling, autoupdate side effects, App Framework resource contention, Ariel search-resource sharing across concurrent analysts. |
| Blind Spot | **Blind Spot** | Unchanged. A specific, named gap in what QRadar's architecture can see or do — e.g., the CRE's lack of an arbitrary multi-event join, named generically in DEH Part 27 §2.3 and given full operational treatment here (Part 11). |
| False Positive Trap | **Noisy Offense Trap** | Renamed because this book's unit of noise is the Offense, and the fix is as often a tuning-workflow or Reference Set maintenance gap as it is a single rule's logic — broader than DEH's per-detection FP framing. Names a specific configuration or operational gap that floods the queue, and the fix (with the same DEH `TERMINOLOGY.md` Tuning-vs-Suppression distinction carried forward — see Part 15). |
| Detection Test | **Validation Test** | Deliberately *not* called "Rule Test" — QRadar's own Rule Wizard already uses "Rule Test" as a specific technical term for one condition inside a Rule (DEH Part 27 §2.1). Reusing it for this callout would collide with a real platform term throughout a book about that platform. Same **Setup / Action / Expected result** structure as DEH's Detection Test. |
| SOC Management View | **SOC Management View** | Unchanged. |
| What Would Change My Mind | **What Would Change My Mind** | Unchanged. |
| *(none — new)* | **PRODUCT VERSION NOTE** | New. See §12 for the full convention; the callout form is: |

```
> **PRODUCT VERSION NOTE**
> The specific claim, and the QRadar version(s) it's confirmed against or believed current for, in one clause.
> What has changed, or plausibly could change, across releases — the menu path, the wording, the default,
> the availability of the feature at all. What the reader should check in their own console before trusting
> this claim as current.
```

Worked example:

```
> **PRODUCT VERSION NOTE**
> The Rule Wizard's exact Rule Test category wording ("when at least X events are seen with the same
> property in Y minutes") is stable in spirit across recent QRadar releases but has shifted in exact phrasing
> and menu grouping before — DEH Part 27 §2.1 flags the same risk for the Rule Test catalog generally. Verify
> the current wording and category list against your own deployment's Rule Wizard before treating this
> section's phrasing as a literal transcript.
```

**Density guidance:** identical to DEH §6.9 — a section stacking every callout type is over-boxed. A typical operational walkthrough (e.g., a rule type, a troubleshooting scenario) carries one Rule Autopsy or one Validation Test, zero-to-one Blind Spot, zero-to-one Noisy Offense Trap, and a PRODUCT VERSION NOTE wherever a navigation or wording claim needs one — which, in this book, is often, precisely because the subject matter is a console rather than a query language.

---

## 7. Content-Level Tags — Six Tags

DEH's six content tags exist to let one section serve every reader depth without five separate books. This book keeps that model and keeps the tag *count* at six, but renames two to match a platform-operations audience rather than a cross-language detection-authoring one, and narrows one's scope accordingly. Format is unchanged: `**[TAG]**`, bold, brackets, all caps, start of the paragraph or subsection it governs, never doubled on one paragraph.

| This book's tag | DEH equivalent | Use for | Do not use for |
|---|---|---|---|
| `[CONCEPT]` | `[CONCEPT]` (unchanged) | Foundational "what and why" for a QRadar architecture piece — what an Offense is, what Ariel is, what the CRE evaluates and when — before any role-specific content in the section makes sense. | A specific Rule Test, threshold value, or console path — that's a lower tag even if conceptually simple. |
| `[ANALYST]` | `[ANALYST]` (unchanged) | Triage-facing: what a fired Offense's magnitude/credibility/relevance actually tells you, what to pull first, escalation and closing-reason criteria. | Tuning the rule that produced the Offense — that's `[RULE ENGINEER]`. |
| `[RULE ENGINEER]` | `[DETECTION ENGINEER]` (renamed) | The QRadar Custom Rules Engine authoring surface specifically: Rule Wizard mechanics, Building Block design, Reference Set/Map/Table choice, custom property definition, thresholds, chaining logic, Response configuration. This book's "detection engineer" role operates *inside* one platform's console, not across six query languages — DEH owns that comparison; this tag owns going deep on the one platform DEH's Part 27 only had room to touch. | Cross-platform analytic design, field-mapping translation loss, or query-language syntax — that's DEH Parts 23–29. Pipeline/infrastructure concerns that sit below the CRE — that's `[PLATFORM ENGINEER]`. |
| `[PLATFORM ENGINEER]` | `[ENGINEERING]` (renamed) | QRadar's own infrastructure: Console/Event Processor/Event Collector/Flow Processor/Data Node/App Host topology, DSM and log source onboarding mechanics, licensing/EPS/FPM capacity, Ariel search performance and retention buckets, HA/DR, autoupdate, the App Framework's own resource footprint. | Rule logic itself, even when the rule is the thing consuming the resource being discussed — describe the resource constraint here, and cross-reference the rule-authoring content under `[RULE ENGINEER]`. |
| `[THREAT HUNTER]` | `[THREAT HUNTER]` (unchanged) | Hypothesis-driven AQL/Ariel exploration and offense-to-event pivoting, extending DEH Part 27 §5's pattern into full operational hunting practice within QRadar specifically. | A named, deployed Rule/Building Block — tag the finished object `[RULE ENGINEER]` and keep the hunting narrative that led to it `[THREAT HUNTER]`, same discipline DEH requires. |
| `[SOC MANAGEMENT]` | `[SOC MANAGEMENT]` (unchanged) | Staffing, licensing cost, MSSP-vs-in-house tradeoffs, and the review-cost consequence of QRadar's own object model (the three-object review burden DEH Part 27's own closing SOC MANAGEMENT paragraph already names) — framed for whoever budgets a QRadar practice. | Any paragraph that starts specifying a Rule Test, a threshold, or a console path — split it. |

**Why two renames and not six:** `[CONCEPT]`, `[ANALYST]`, `[THREAT HUNTER]`, and `[SOC MANAGEMENT]` describe a reader's *relationship to the work* (understanding, triaging, hunting, budgeting), which doesn't change when the subject narrows from six platforms to one. `[DETECTION ENGINEER]` and `[ENGINEERING]` described DEH's *cross-platform analytic/pipeline* split, which doesn't map cleanly onto a single-platform operations book — this book's rule author and this book's platform administrator are different people with different consoles-within-the-console, and `[RULE ENGINEER]` / `[PLATFORM ENGINEER]` name that split directly instead of inheriting a distinction built for a different comparison.

---

## 8. Table Conventions

Adopt DEH `STYLE-GUIDE.md` §8 unchanged: lead-in sentence stating what decision the table supports, short noun-phrase headers in title case, left-aligned text columns, fragment cells (not full sentences), em dash for "not applicable," never a blank cell. Additions specific to this book:

- Any table listing Rule Test categories, DSM names, or console menu paths gets a **Version** column (or a table-level PRODUCT VERSION NOTE immediately below it) if the content is anything more specific than "this concept exists" — a bare feature name is usually stable; the exact wording, grouping, or menu location is the part that drifts.
- `BB:`/`RS-`/`R:`-prefixed object names inside a table cell use inline code, same as in prose, per §4.

---

## 9. Figures, Diagrams, and Screenshots: Evidence Classification

This is the section that operationalizes §0's honesty constraint. The four-class taxonomy is unchanged from DEH `STYLE-GUIDE.md` §9.1 — kept identical for cross-series consistency, since a reader moving between NESHBOY titles should not have to learn a second evidence-tagging scheme:

| Tag | Meaning | Status in this book |
|---|---|---|
| `CONTROLLED LAB EXAMPLE` | Captured from a lab the author built specifically to generate this evidence. | **Not currently available.** No such lab exists for this book. Do not use this tag unless a real QRadar instance was actually stood up and used to produce the specific artifact — a reviewer encountering this tag should treat it as a claim to verify, not accept on sight, precisely because it should be rare here. |
| `REAL LAB EXAMPLE` | Captured from a real, pre-existing environment (a customer engagement, an employer's own deployment), scrubbed of secrets/PII. | **Not currently available**, same reasoning. If a future contributor has legitimate, authorized access to a real QRadar deployment and captures evidence from it, this tag becomes usable — with the scrubbing and authorization discipline DEH §9.1 already requires, non-negotiably. |
| `OFFICIAL REFERENCE` | Sourced from IBM's own public QRadar documentation, reproduced or closely adapted with attribution. | **The primary evidence class for anything claiming to show real platform behavior.** Every use cites the exact IBM doc URL and, wherever the source states one, the QRadar version the doc covers, in `REFERENCES.md`. If IBM's own source doesn't specify a version, say so in the caption rather than inventing one. |
| `CONCEPTUAL` | An illustrative diagram with no claim of being captured from a real system. | **The primary evidence class for this book's own architecture and workflow diagrams** — deployment topology, offense-scoring data flow, rule/Building Block/Reference Set relationship diagrams, tuning-workflow flowcharts. This is the default for anything this book draws itself rather than sources from IBM. |

**Rules specific to this book, beyond DEH §9.1's baseline:**

1. **No synthetic console mockup may be styled to look like a captured screenshot.** DEH §9.1 permits a clearly-labeled `SYNTH-UI-` synthetic mockup when a real capture is genuinely infeasible, logged in `VISUAL-INVENTORY.md` with a reason. This book goes one step further: any illustrative "what the Offense list looks like" or "what the Rule Wizard looks like" figure must be visually distinguishable from a real screenshot at a glance — a labeled wireframe or boxed-field diagram, not a pixel-accurate recreation of QRadar's actual console chrome. The risk this book is specifically guarding against is a reader mistaking an invented mockup for a real captured UI, given that real captures are the exception here rather than the norm DEH could rely on for other platforms. A `SYNTH-UI-`-prefixed file that looks photorealistic is a build defect in this book even if correctly captioned.
2. **Every figure defaults to `CONCEPTUAL` unless it earns `OFFICIAL REFERENCE`.** There is no "we'll upgrade the tag later" allowance for `CONTROLLED LAB EXAMPLE`/`REAL LAB EXAMPLE` placeholders the way DEH's pending-placeholder mechanism (§9.3, unchanged here) allows for figures on a path to being captured — because this book has no lab-access roadmap to point that placeholder at. If lab access is ever secured, treat it as a scope change to this guide (§0/§9 both get revised), not a quiet swap-in.
3. **The pending-placeholder format is unchanged from DEH §9.3** for the rare case a `CONCEPTUAL` diagram is referenced before it's rendered — the target evidence class in that placeholder should almost always read `CONCEPTUAL` or `OFFICIAL REFERENCE` for this book, and a reviewer should challenge a pending placeholder that targets `CONTROLLED LAB EXAMPLE`/`REAL LAB EXAMPLE` by asking where the lab access is actually coming from.

Caption format is unchanged from DEH §9.2. Worked example adapted to this book:

```
**Figure 3.1 — Offense magnitude as a function of severity, relevance, and credibility.** *CONCEPTUAL.*
Illustrates the three inputs QRadar's own documentation names as magnitude's components and how they
combine into one queue-ranking score; not a reproduction of any single IBM diagram, and not a claim about
the exact internal weighting formula, which this book states as unpublished/version-variable rather than
guessed at (see §12). Compare Figure 3.2 for the OFFICIAL REFERENCE figure sourced directly from IBM's own
offense-management documentation.
```

---

## 10. Diagram Rendering Requirement

Unchanged from DEH `STYLE-GUIDE.md` §10: every `mermaid` block is rendered to a static image (SVG preferred) and committed alongside the source; the Mermaid source stays in the file as editable truth; a unit is not review-complete with an unrendered `mermaid` fence and no paired figure reference.

---

## 11. The PRODUCT VERSION NOTE Convention, in Depth

QRadar is not a stable, slow-moving reference implementation the way a Windows Event ID or a MITRE technique ID is — its console, Rule Wizard wording, DSM catalog, and even its packaging and delivery model (on-prem vs. cloud-hosted, and which business unit sells and supports which piece) change across release cycles in ways this book's author cannot track in real time from outside an active deployment. DEH Part 27 already models this instinct ad hoc — "the exact wording and available test categories in the Rule Wizard have shifted across QRadar releases," "whether a given QRadar version lets you anchor a Rule Test directly to a saved AQL search... is a version-dependent capability." This book makes that instinct a named, checkable convention rather than leaving it to each author's judgment about when to hedge.

**A PRODUCT VERSION NOTE (callout form in §6, or an inline flag where a full callout is too heavy for a single clause) is required wherever a claim names:**

- A specific console menu path or click sequence.
- The exact wording of a Rule Wizard category, a dashboard item name, or any other literal UI string.
- Whether a specific feature exists at all in "QRadar" without a version qualifier (a feature present in a recent release may not exist in an older deployment a reader is actually running, and vice versa).
- Anything about QRadar's commercial packaging, delivery model, or vendor-side support/ownership — this space has changed more than once in ways this book does not have current visibility into at time of writing, and asserting a specific current state here is exactly the kind of claim that ages fastest and least gracefully.

**A PRODUCT VERSION NOTE is not required for:** the existence of the CRE, the Ariel `events`/`flows` split, the general concept of a DSM parsing raw logs into a QID, or the three-input structure of magnitude (severity/relevance/credibility) — these are architectural concepts stable across the platform's history, not UI specifics. The test, matching DEH's own filler-word test in spirit: **would a reader on a materially different QRadar release than the one this book had in mind, checking their own console, find this claim simply wrong, or only differently worded?** "Simply wrong" needs a version note. "Differently worded, same idea" does not.

**What a PRODUCT VERSION NOTE must not do:** hedge everything into mush. A note that fires on every sentence trains the reader to skip all of them — reserve it for the specific claims above, state the claim plainly first, and let the note do the version-risk work rather than diluting the claim itself with "may vary" language banned under §1.

---

## 12. Relationship to the Detection Engineering Handbook

This book is a sibling title, not a rewrite. Concretely:

- **Do not redefine any term already in DEH `TERMINOLOGY.md`.** Alert, Case, Incident, Disposition, Tuning, Suppression, Coverage, and every other DEH glossary term keep their DEH definitions unchanged here — including DEH Part 27 §6's own finding that a QRadar Offense is a hybrid of DEH's Alert and Case concepts, which this book's offense-management parts inherit rather than re-derive. New, genuinely QRadar-specific vocabulary this book needs (Magnitude, Credibility, Relevance, QID, DSM, CRE, Building Block, Reference Set/Map/Table, Domain, Tenant, EPS/FPM) belongs in this book's own appendix glossary, cross-referencing DEH `TERMINOLOGY.md` rather than duplicating any entry that already exists there.
- **Do not re-teach AQL syntax.** DEH Part 27 §1 is the canonical syntax reference; every part in this book that shows an AQL query links back to it rather than re-explaining `SELECT`/`FROM`/`WHERE`/`GROUP BY`/`LAST n HOURS` from scratch.
- **Do not re-argue Sigma-first vs. native authoring.** DEH Part 23 owns that tradeoff generically and DEH Part 27 §2–§4 owns it for QRadar specifically (the three-object decomposition of a canonical detection). This book's rule-authoring parts (Section D) build past that single worked example into the full Rule Wizard catalog, Building Block governance at scale, and the full reference-data type taxonomy — genuinely new material, not a restatement.
- **Carry DEH's detection IDs forward by reference, never by redefinition.** Where this book discusses DET-27-01 or DET-27-02 as a worked example of a rule-authoring pattern, it cites the ID and links to DEH Part 27 — it does not restate the analytic's boundary (the allowlist, the `GrantedAccess` intent) as if this book owned that decision.

---

## 13. Review Checklist

1. **Voice:** DEH §1's filler test applied; no unqualified navigation/UI claim stated as bare permanent fact (§1, §12).
2. **Headings:** correct nesting, `## Why this part exists` present, no heading used as a bold-line substitute (§2).
3. **Code blocks:** every fence tagged per §3's table, AQL fences carry the disambiguating comment, framing sentences present for every real query or console-navigation claim.
4. **Object notation:** `BB:`/`RS-`/`R:` prefixes used correctly and consistently, QID/DSM/CRE terms expanded on first use per part (§4).
5. **MITRE IDs:** DEH §5 rules followed exactly, no invented mapping.
6. **Callouts:** correct label from the nine in §6, correct structure, density not excessive, "Rule Test"/"Validation Test" naming collision avoided.
7. **Tags:** every `##`/`###` subsection carries at least one of the six tags in §7, no paragraph carries two, `[RULE ENGINEER]` vs. `[PLATFORM ENGINEER]` boundary respected.
8. **Tables:** DEH §8 conventions followed; Version column or note present where a table lists UI-specific detail.
9. **Figures:** every figure has a §9 evidence-class caption; **any figure tagged `CONTROLLED LAB EXAMPLE` or `REAL LAB EXAMPLE` is challenged and its actual lab-access basis verified before acceptance**, since these should be rare-to-nonexistent in this book; no synthetic mockup is photorealistic enough to be mistaken for a capture; every Mermaid block has a paired rendered image.
10. **PRODUCT VERSION NOTE coverage:** every menu path, literal UI string, and packaging/ownership claim identified in §11's required list carries a note; no note-fatigue from over-application.
11. **DEH boundary check:** no AQL syntax re-taught from scratch, no Sigma-vs-native argument re-litigated, no DEH `TERMINOLOGY.md` term redefined, every DEH-sourced detection ID cited rather than restated.

Any deviation a reviewer approves is recorded as a documented change to this file, not silent drift — the same discipline DEH's own closing line requires of its guide.
