
# VANTIX Portfolio — Projects 1–4 Status and Assurance Summary

## Current status

The first four VANTIX portfolio projects have undergone repeated technical, evidence, documentation, security and repository-integrity reviews and are at the GitHub upload / final live-CI stage.

| Project | Purpose | Current local state | Final live gate |
|---|---|---|---|
| Project 1 — Flow Integrity / Salesforce Governance Sentinel | Detects measurable Salesforce governance defects and routes them through governed AI critique and human-controlled remediation | Local validation PASS; checksum PASS; one authentic workflow-success image remains an optional/non-blocking evidence item if not already in repository history | final GitHub Actions Green on exact merged commit |
| Project 2 — Agile Delivery & Admin Workload Sentinel | Prevents weak, duplicate, unsupported or unapproved Salesforce work entering delivery backlog | Validation PASS; graph invariants PASS; 9/9 exact-node offline tests PASS; scorecard reconciles to 94/100 | final GitHub Actions Green; historical Gemini-key rotation remains an evidence/security action outside repository code |
| Project 3 — Control Value / Customer Commitment Assurance | Prevents customer commitments being closed without evidence of the promised outcome | Repository identity restored; infrastructure reconciled; validation PASS; graph PASS; 5/5 exact-node tests PASS; final SHA ledger regenerated after last documentation changes | controlled merge + final GitHub Actions Green |
| Project 4 — Attestor | Extends governed outcome assurance across Commitment Assurance, Service Recovery and Customer Momentum | Repository validation PASS; graph PASS; SHA ledger PASS; 5/5 exact-node replay PASS; owner-run adversarial suite 18/18 PASS | final GitHub Actions Green on exact merged commit |

## What was corrected

The repeated review rounds were valuable because they exposed failure modes that are common in real portfolio and enterprise-control work, not only coding defects.

### 1. Evidence claims were tightened

We removed or prevented unsupported wording such as:
- unsupported production-maturity wording without production evidence;
- third-party/audit wording without a genuine external reviewer;
- authenticated identity where only labelled identity fields were demonstrated;
- live AI where a synthetic replay or preview was used;
- CI Green where only local validation had run;
- market-exclusivity claims without dated competitive evidence.

This made the portfolio more credible because every important statement now has an evidence class and explicit limitation.

### 2. Repository integrity became executable

Projects evolved from documentation-heavy validation to executable controls:
- SHA-256 ledgers;
- generic Markdown file and anchor checks;
- broad secret scanning across JSON, JavaScript, HTML, Markdown and configuration-like files;
- workflow/evidence hash binding;
- scorecard arithmetic validation;
- required-file enforcement;
- graph-invariant checks;
- negative tests proving validators fail when attacked.

This means repository quality is no longer based only on a checklist saying a control exists; the control itself is testable.

### 3. AI authority was separated from deterministic authority

Across the portfolio:
- deterministic logic owns facts, calculations, eligibility and policy-critical routing;
- AI is limited to explanation, drafting, critique or bounded interpretation;
- AI output is validated before it can move forward;
- consequential approval remains human-controlled;
- AI cannot silently convert incomplete evidence into a final business fact.

This is a central design choice that differentiates the portfolio from simple “LLM in a workflow” demos.

### 4. Six Sigma measurement was made domain-specific

The projects no longer imply that one DPMO or Sigma denominator can be copied across unrelated domains.

Each project defines its own:
- CTQs;
- defect opportunities;
- observation boundary;
- measurement limitations.

Where production process history does not exist, the documentation explicitly refuses to claim process capability or Cpk.

### 5. Identity and lineage were corrected

Project 3 exposed an important portfolio-governance issue: Control Value had temporarily been overwritten by Attestor-facing material.

That was corrected by:
- restoring Control Value as Project 3;
- preserving Attestor-transition history rather than erasing it;
- reconciling genuine Control Value infrastructure instead of deleting it;
- keeping Attestor as Project 4.

This gives the portfolio an auditable evolution path rather than four repositories with overlapping or contradictory identities.

### 6. Version drift and stale canonicals were removed

Review rounds caught:
- stale README release wording;
- duplicate handoff/review prompts;
- score changes not reflected everywhere;
- changed files after checksum generation;
- old workflow names surviving in CI.

The final packages enforce one canonical handoff, one canonical review prompt, one active score and one active release identity.

## How the issues were identified

The corrections were found through several independent mechanisms:

1. **Direct file inspection** — checking actual repository/package contents instead of relying on prior summaries.
2. **Cross-file reconciliation** — comparing README, scorecard, handoff, release notes, workflow files and evidence inventories for contradictions.
3. **Exact-node-code execution** — extracting JavaScript directly from n8n workflow JSON and running it against controlled fixtures.
4. **Negative testing** — deliberately breaking links, hashes, scores, workflow edges, evidence records and security patterns to prove the validators fail.
5. **Live-repository reconciliation** — comparing remediation ZIPs with the real repository tree to find unaccounted infrastructure.
6. **Independent LLM adversarial review** — using a second reviewer to attack evidence claims and packaging assumptions, then reproducing valid findings locally before accepting them.

## What makes the portfolio unique

The differentiation is not that individual technologies are unique. Salesforce, n8n, AI, Agile, PMP and Six Sigma all exist elsewhere.

The portfolio is differentiated by their **governed composition**:

**Salesforce/CRM evidence → deterministic controls → bounded AI → independent validation → human authority → measurable outcome → audit evidence**

Across the four projects, the focus moves through a coherent operating chain:

**Flow Integrity → Delivery Integrity → Commitment Integrity → Customer Outcome Assurance**

That creates a portfolio story about how enterprise operations can use AI without giving the model uncontrolled authority over facts, policy or customer-impacting decisions.

## What makes it robust

The portfolio is robust because:
- positive paths are not the only evidence;
- failure modes are deliberately exercised;
- deterministic controls are separated from probabilistic AI;
- source evidence is retained;
- human authority is explicit;
- checksums and CI protect file integrity;
- scores are machine-reconciled;
- security claims distinguish tested controls from production guarantees;
- limitations are published rather than hidden;
- cross-project history and lineage are documented;
- each repository can be reproduced and challenged by another reviewer.

## Public-positioning statement

> The VANTIX portfolio is a five-layer enterprise AI operations programme demonstrating how Salesforce/CRM governance, Agile delivery, customer commitment assurance and customer-outcome controls can be connected through deterministic evidence gates, bounded AI and human decision authority. The projects are intentionally evidence-first: each publishes its control boundaries, failure-mode tests, limitations and reproducibility checks rather than presenting synthetic portfolio demonstrations as production deployments.
