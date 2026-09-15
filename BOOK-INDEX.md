# QRadar SOC Operations

**BOOK-INDEX.md — canonical part list and appendix list.**
**Series:** NESHBOY SOC Professional Library — sibling title to *The Detection Engineering Handbook* (DEH), `C:\Users\User\projects\detection-engineering-handbook\release-v2\`.
**Status:** Architecture draft, pre-authoring. No chapter files exist yet — this index is the plan they get written against.

## What this book is

DEH Part 27 (`chapters\part27-qradar-aql.md`) covers QRadar at a query-language-comparison depth: AQL syntax, the Ariel `events`/`flows` model, and just enough of the Custom Rules Engine (CRE) to prove one specific claim — that QRadar's correlation model forces a three-object decomposition (Building Block, Reference Set, Rule) where a KQL or SPL implementation of the same analytic is one deployed artifact. That is ~5,800 words with room for one worked example. It was never meant to teach anyone how to run a QRadar deployment.

**This book is that book.** It covers the platform-operations experience DEH Part 27 explicitly defers: offense management and scoring, the full Rule Wizard catalog beyond one canonical rule, Building Block governance at scale, the complete reference-data type taxonomy, DSM and log source onboarding, custom properties, Ariel search performance, flow-vs-event architecture, dashboards, noisy-offense tuning workflow, rule change management without a git-based pipeline, licensing/capacity planning, and QRadar-specific troubleshooting. Every part states its DEH dependency in front matter and cross-references DEH Part 23 (Query Language Strategy) and Part 27 (QRadar AQL) by section rather than re-teaching either.

**The honesty constraint that shapes this whole book:** no real QRadar deployment exists in the author's lab. `STYLE-GUIDE.md` §0 and §9 cover this in full; the short version is that this book's figures are almost exclusively `OFFICIAL REFERENCE` (sourced and cited from IBM's own public documentation) or `CONCEPTUAL` (this book's own architecture/workflow diagrams, honestly labeled as illustrative). `CONTROLLED LAB EXAMPLE` and `REAL LAB EXAMPLE` — a real captured console screenshot — are not used, because that evidence does not exist yet for this project. Where DEH could build a Sysmon lab or an SSH host on demand, a multi-node QRadar deployment is commercial infrastructure outside a solo author's easy reach; this book states that plainly rather than fabricating a console capture to look otherwise.

**The other constraint: QRadar moves.** Console navigation, Rule Wizard wording, the DSM catalog, and QRadar's own packaging and delivery model have all shifted across release cycles in ways this book cannot track from outside a live deployment. Every part uses the **PRODUCT VERSION NOTE** convention (`STYLE-GUIDE.md` §11) to flag a version-sensitive claim explicitly rather than asserting a menu path as permanent fact.

## Multi-level content model

Six content tags, adapted from DEH's six for a platform-operations audience (full rationale in `STYLE-GUIDE.md` §7):

- `[CONCEPT]` — foundational QRadar architecture, unchanged in spirit from DEH.
- `[ANALYST]` — Offense triage: reading magnitude/credibility/relevance, escalation, disposition.
- `[RULE ENGINEER]` — the CRE authoring surface itself: Rule Wizard, Building Blocks, reference data, custom properties, thresholds. *(Renamed from DEH's `[DETECTION ENGINEER]` — this tag operates inside one platform's console, not across six query languages.)*
- `[PLATFORM ENGINEER]` — QRadar's own infrastructure: deployment topology, DSM/log source onboarding, licensing/capacity, Ariel performance, HA/DR, the App Framework. *(Renamed from DEH's `[ENGINEERING]`.)*
- `[THREAT HUNTER]` — AQL/Ariel ad hoc search and offense-to-event pivoting, extending DEH Part 27 §5.
- `[SOC MANAGEMENT]` — staffing, licensing cost, MSSP-vs-in-house, and the review-cost consequence of QRadar's own multi-object model.

Nine recurring callouts (`STYLE-GUIDE.md` §6): **Rule Autopsy**, **Hunter's Note**, **Platform Reality**, **Blind Spot**, **Noisy Offense Trap**, **Validation Test**, **SOC Management View**, **What Would Change My Mind**, and the new **PRODUCT VERSION NOTE**.

## Production model

Every part carries mandatory YAML front matter, extending DEH's model with one field this book's version-drift risk specifically requires:

- `author`, `reviewer` (different person/agent, technical-adversarial), `status` (draft → reviewed → tested → released), `last_validated`, `depends_on` (part IDs, and DEH part/section IDs where relevant — e.g. `deh_depends_on: ["part23", "part27#2.2"]`).
- **`qradar_version_scope`** — the QRadar version range a part's specific UI/wording claims target (e.g., `"stated generically; version-sensitive claims individually flagged per STYLE-GUIDE §11"`), forcing every part to declare its own version-currency posture rather than leaving it implicit.

Nothing ships to `released` without a reviewer sign-off, and — specific to this book — without confirming no figure claims `CONTROLLED LAB EXAMPLE`/`REAL LAB EXAMPLE` evidence that doesn't actually exist (`STYLE-GUIDE.md` §9, review item 9).

---

## Part Table

*File path pattern:* `C:\Users\User\projects\qradar-soc-operations-handbook\chapters\partNN-slug.md` (planned; not yet authored).

### Section A — Platform Orientation and the Honesty Constraint

| Part | Title | File Path | Scope | Recurring Features |
|---|---|---|---|---|
| 1 | Why This Book Exists, and What "Operations" Means Here | `chapters\part01-why-this-book-exists.md` | Scope boundary against DEH Part 23/27; states the no-lab evidence constraint and the PRODUCT VERSION NOTE convention up front, not as buried fine print; who this book is for (QRadar admins, rule authors, Tier-1/2 analysts, SOC managers evaluating or running a QRadar practice) and who it isn't (a reader wanting AQL syntax — sent to DEH Part 27 §1). | SOC Management View, What Would Change My Mind |
| 2 | QRadar Deployment Architecture: Console, Processors, Collectors, and Data Nodes | `chapters\part02-qradar-deployment-architecture.md` | All-in-One vs. distributed deployment; Console, Event Processor, Event Collector, Flow Processor, Data Node, and App Host roles; how event and flow data physically moves through the deployment before it reaches Ariel or the CRE. First required PRODUCT VERSION NOTE: on-prem vs. cloud/SaaS packaging and delivery-model changes over recent release cycles. | Platform Reality, PRODUCT VERSION NOTE |

### Section B — The Offense Model

| Part | Title | File Path | Scope | Recurring Features |
|---|---|---|---|---|
| 3 | Offenses, Magnitude, Credibility, and Relevance | `chapters\part03-offenses-magnitude-credibility-relevance.md` | Full scoring model — what severity, relevance, and credibility each measure and how they combine into magnitude (stated as architecture, with any specific numeric weighting flagged as unpublished/version-variable per PRODUCT VERSION NOTE rather than guessed at); offense indexing and entity binding; offense lifecycle (active, dormant, closed) and retention/cleanup; offense forwarding. Cross-references DEH Part 27 §6's finding that an Offense is a hybrid of DEH `TERMINOLOGY.md`'s Alert and Case concepts — inherited, not re-derived. | Blind Spot, PRODUCT VERSION NOTE |

### Section C — Getting Data In

| Part | Title | File Path | Scope | Recurring Features |
|---|---|---|---|---|
| 4 | DSMs, QID Mapping, and Log Source Onboarding | `chapters\part04-dsms-qid-mapping-log-source-onboarding.md` | Full onboarding lifecycle: protocol configuration, auto-discovery, parsing order, the DSM's role in assigning a QID and extracting fields. Directly operationalizes the failure mode DEH Part 27 §3.1 names once ("an unmapped or partially-mapped event lands under a generic QID with no custom properties, and the query fails silently") into a repeatable onboarding checklist. | Rule Autopsy, Platform Reality |
| 5 | The Universal DSM, DSM Editor, and Custom Log Source Extensions | `chapters\part05-universal-dsm-dsm-editor-extensions.md` | Handling sources with no native DSM: Universal DSM, DSM Editor regex-based field extraction, LEEF/CEF as vendor-side escape hatches, and the maintenance cost of a hand-built extension surviving a source's own format changes. | Platform Reality, Noisy Offense Trap |
| 6 | Custom Properties: Extraction, Calculated Properties, and Governance | `chapters\part06-custom-properties.md` | Event vs. flow custom properties; regex-extracted vs. calculated properties; the Ariel search-performance cost of a poorly written extraction property (cross-references Part 12); naming/governance so a custom property referenced by name in AQL or a Rule Test doesn't silently drift out of sync with the DSM that populates it. | Rule Autopsy, Platform Reality |
| 7 | Flow Data Architecture: QFlow, Flow Sources, and Flow-vs-Event Design | `chapters\part07-flow-data-architecture.md` | Flow collection architecture and QFlow processing; superflows; asymmetric-routing and packet-capture-location pitfalls; the design decision of whether an analytic belongs on `events`, `flows`, or both — a decision DEH Part 27 §1.1 introduces the two tables for but does not itself make. | Blind Spot, Platform Reality |

### Section D — Building the Correlation Layer

| Part | Title | File Path | Scope | Recurring Features |
|---|---|---|---|---|
| 8 | The Rule Wizard Catalog: Rule Types Beyond the Canonical Example | `chapters\part08-rule-wizard-catalog.md` | Event, Flow, Common, Offense, User, Anomaly, Threshold, and Behavioral rule types; Response actions beyond "create an Offense" (email, script, Reference Set update, SNMP); response limiters. Builds outward from the single Event-rule example DEH Part 27 §2.1/§3.3 walks through. | Rule Autopsy, PRODUCT VERSION NOTE |
| 9 | Building Blocks: Design Patterns and Governance at Scale | `chapters\part09-building-blocks-governance.md` | `BB:` library organization and naming; avoiding sprawl/drift once a library holds hundreds of Building Blocks; change control inside a console-native workflow, without DEH Part 22's git/CI model available for free — what a disciplined team substitutes instead. | SOC Management View, Rule Autopsy |
| 10 | Reference Data Collections: Sets, Maps, Map of Sets, Map of Maps, and Sequences | `chapters\part10-reference-data-collections.md` | The full typed reference-data taxonomy beyond the single Reference Set DEH Part 27 §2.2 introduces; when each type (Set, Map, Map of Sets, Map of Maps, Sequence) is the right structural fit; TTL/expiry management; populating via Rule Response, the REST API, or a bulk Reference Data import, and the drift risk of each population path getting out of sync with the others. | Blind Spot, Noisy Offense Trap |
| 11 | Thresholds, Anomaly and Behavioral Rules, and the Limits of Native Aggregation | `chapters\part11-thresholds-anomaly-behavioral-rules.md` | QRadar's native threshold/aggregation Rule Test generalized beyond DEH Part 27 §4's single worked example (DET-27-02); Anomaly and Behavioral rule types built on saved-search baselines; closes the loop on DEH Part 27 §2.3's Blind Spot — exactly which correlation shapes these native mechanisms cover, and which still force the Reference Set decomposition pattern. | Blind Spot, What Would Change My Mind |

### Section E — Operating the Search and Reporting Layer

| Part | Title | File Path | Scope | Recurring Features |
|---|---|---|---|---|
| 12 | Ariel Search Performance and Tuning | `chapters\part12-ariel-search-performance-tuning.md` | Index management and quick-filter properties, search-scope narrowing, saved vs. scheduled searches, retention buckets, and search-resource contention across concurrent analysts sharing one Ariel deployment. Expands DEH Part 27 §1.3's one-paragraph EPS/search-cost flag into a full tuning discipline. | Platform Reality, Validation Test |
| 13 | Dashboards, Pulse, and Executive Reporting | `chapters\part13-dashboards-pulse-reporting.md` | Default vs. custom dashboard items, AQL-backed dashboard widgets, scheduled reports, and honest metrics reporting — cross-references DEH `TERMINOLOGY.md`'s Coverage entry to avoid the same bare-"coverage" ambiguity DEH warns against, applied to an offense-count dashboard that can look like progress without being detection coverage. | SOC Management View, PRODUCT VERSION NOTE |

### Section F — Running the Queue

| Part | Title | File Path | Scope | Recurring Features |
|---|---|---|---|---|
| 14 | Analyst Triage Workflow for Offenses | `chapters\part14-analyst-triage-workflow.md` | Day-to-day queue handling: disposition, escalation, note-taking, closing-reason codes, using magnitude/credibility/relevance to prioritize a queue rather than treating every Offense as equally urgent. Direct continuation of DEH Part 27 §6's analyst-triage capsule and DEH `TERMINOLOGY.md`'s Disposition/Triage/Case/Incident entries. | Rule Autopsy, Validation Test |
| 15 | Noisy-Offense Triage and the Tuning Workflow | `chapters\part15-noisy-offense-tuning-workflow.md` | Systematic diagnosis of a flooding Rule/Building Block/Reference Set combination; the Tuning-vs-Suppression distinction from DEH `TERMINOLOGY.md` applied to a console-native environment; a repeatable tuning-intake process (request → diagnosis → change → re-validation) built for a platform with no CI gate. | Noisy Offense Trap, SOC Management View |
| 16 | Rule Change Management Without a Detection-as-Code Pipeline | `chapters\part16-rule-change-management.md` | The honest gap: QRadar's console-native workflow doesn't hand you DEH Part 22's git/PR/CI model for free. What a disciplined team builds instead — change tickets, rule revision history as a rollback mechanism, a staging tenant where licensing allows one, manual regression testing against known-positive events before and after a change. | Validation Test, SOC Management View |

### Section G — Keeping the Platform Healthy

| Part | Title | File Path | Scope | Recurring Features |
|---|---|---|---|---|
| 17 | Licensing, EPS/FPM Management, and Capacity Planning | `chapters\part17-licensing-eps-fpm-capacity-planning.md` | License tiers, burst/overage handling, growth forecasting, and the real cost of onboarding one new noisy log source — deep dive beyond DEH Part 27 §1.3's single-paragraph flag. | Platform Reality, SOC Management View |
| 18 | QRadar-Specific Troubleshooting: Log Sources, DSMs, and Offense Flooding | `chapters\part18-troubleshooting.md` | A diagnostic playbook per named failure mode: a log source that stops parsing, a DSM/QID mismatch after a vendor agent upgrade, and an offense-flooding incident — each walked as symptom → likely cause set → verification step → fix, cross-referencing Parts 4 (DSM/QID), 10 (Reference Set drift), and 15 (tuning workflow) as the parts that prevent recurrence. | Rule Autopsy, Blind Spot |
| 19 | Apps, Extensions, and the App Framework | `chapters\part19-apps-extensions-app-framework.md` | App Host architecture and resource footprint; the App Exchange ecosystem; common apps (Use Case Manager, Pulse, UBA) at a survey level; governance risk of installing a third-party app against a production deployment. | Platform Reality, PRODUCT VERSION NOTE |

### Section H — Program, Identity, and Scale

| Part | Title | File Path | Scope | Recurring Features |
|---|---|---|---|---|
| 20 | Asset Model, Network Hierarchy, and Vulnerability Data | `chapters\part20-asset-model-network-hierarchy-vulnerability-data.md` | How Relevance (Part 3) actually gets weighted in practice: the asset database, Network Hierarchy configuration, and vulnerability-feed (VIS) integration; the staleness problem of an asset model nobody re-validates after infrastructure changes. | Blind Spot, Platform Reality |
| 21 | Multi-Tenancy, RBAC, and MSSP Operations | `chapters\part21-multi-tenancy-rbac-mssp.md` | Domains, tenants, and security profiles, and how each interacts with Rules, Offenses, and Reference Sets in a shared deployment — the MSSP-specific version of the review-cost problem DEH Part 27's closing paragraph names for a single-tenant shop. | SOC Management View, PRODUCT VERSION NOTE |
| 22 | Staffing and Running a QRadar Practice | `chapters\part22-staffing-and-running-a-qradar-practice.md` | Capstone. Headcount model for Rule/Building Block/Reference Set review, cross-referencing DEH Part 27's own closing SOC MANAGEMENT paragraph on the three-object review burden; MSSP-vs-in-house tradeoffs; honest total-cost-of-ownership framing (license tier, App Framework add-ons, staffing) for a budget conversation. | SOC Management View, What Would Change My Mind |

**Total: 22 parts.**

---

## Appendix Table

*File path pattern:* `C:\Users\User\projects\qradar-soc-operations-handbook\appendices\aN-slug.md` (planned; not yet authored).

| Appendix | Title | File Path | Contents |
|---|---|---|---|
| A1 | QRadar Terminology Addendum | `appendices\a1-qradar-terminology-addendum.md` | Platform-specific glossary (Offense, Magnitude/Credibility/Relevance/Severity, QID, DSM, Ariel, CRE, Building Block, Reference Set/Map/Table/Sequence, Domain, Tenant, EPS/FPM) — extends, never redefines, DEH `TERMINOLOGY.md`. |
| A2 | Rule Wizard and Rule Test Quick Reference | `appendices\a2-rule-wizard-rule-test-quick-reference.md` | Rule Test catalog by category, cross-referenced to DEH Part 27 §2.1 and this book's Part 8; every entry carries a PRODUCT VERSION NOTE by default given the source category's own documented drift. |
| A3 | Troubleshooting Decision Trees | `appendices\a3-troubleshooting-decision-trees.md` | Flowchart companions to Part 18's three named failure modes (log source not parsing, DSM/QID mismatch, offense flooding), rendered per `STYLE-GUIDE.md` §10. |

**Total: 3 appendix bundles.**

---

## Key structural decisions and provenance

1. **22 parts, not fewer.** The task scope named eleven distinct operational subject areas (offense scoring, rule/Building Block authoring, reference sets, DSM/onboarding, custom properties, Ariel performance, flow-vs-event architecture, dashboards, noisy-offense tuning, rule testing/change management, troubleshooting) that each need real depth to avoid the exact "breadth-only, thin depth" trap DEH's own architecture notes name as a defect risk. Foundational (Parts 1–2), scale/program (Parts 20–22), and platform-health (Parts 17–19) parts were added around that core to make the result a coherent book rather than a topic list.
2. **Two of DEH's six tags renamed, four kept as-is** (`STYLE-GUIDE.md` §7). The four kept tags describe a reader's relationship to the work (understanding, triaging, hunting, budgeting), which doesn't change when scope narrows from six platforms to one. The two renamed tags described DEH's cross-platform analytic/pipeline split specifically, which doesn't map onto a single-platform book the same way — `[RULE ENGINEER]` and `[PLATFORM ENGINEER]` name the split this book actually has (CRE authoring surface vs. platform infrastructure) instead of inheriting a distinction built for a different comparison.
3. **Evidence-class honesty stated in three places, not one** — this file's opening section, `STYLE-GUIDE.md` §0, and `STYLE-GUIDE.md` §9 — deliberately redundant, because DEH's own stated V1 defect #1 (89 unrendered diagrams, 71 uncaptured screenshots) is exactly the failure mode of a promise not being checked anywhere structural. This book has no lab-access roadmap to point a pending placeholder at, so the placeholder mechanism DEH uses for "not captured yet" is not a safe default here — the default is an honestly-labeled `CONCEPTUAL` diagram instead.
4. **PRODUCT VERSION NOTE promoted to a named, checkable convention** rather than left as the ad hoc hedging DEH Part 27 already does in prose ("the exact wording... has shifted across QRadar releases"). A single-platform operations book makes far more concrete UI/navigation/wording claims than a six-language comparison chapter does, so the version-drift risk is proportionally larger here — formalizing it as a callout with a stated trigger list (`STYLE-GUIDE.md` §11) is the mechanical fix, matching how DEH itself turned "separation of duties" from a policy statement into a blocking front-matter field.
5. **DSM/onboarding split into three parts (4–6)** rather than one, mirroring DEH's own decision (documented in DEH `BOOK-INDEX.md` decision 3) to split a wide topic rather than produce one shallow survey — QID mapping, the Universal DSM/extension escape hatch, and custom-property governance are three distinct failure surfaces DEH Part 27 §3.1 gestures at in one paragraph and this book treats as three separate operational disciplines.
6. **Rule change management (Part 16) named as an explicit gap against DEH Part 22**, not glossed over — DEH's detection-as-code model assumes a git-based pipeline that QRadar's console-native workflow does not hand a team for free. Naming that gap directly, and building the compensating practice a real team needs instead, is more useful to this book's reader than implying QRadar supports the same workflow DEH Part 22 describes for other platforms.
