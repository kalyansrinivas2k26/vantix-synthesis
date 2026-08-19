
# VANTIX Synthesis v0.1 — Independent Adversarial Review Prompt

Review the attached:

`VANTIX_Project_5_SYNTHESIS_PORTFOLIO_PREVIEW_v0.1.zip`

Your job is to try to prove that the package is not ready for GitHub.

Do not redesign Projects 1–4. Do not propose a universal risk score. Reopen Synthesis architecture only for a concrete evidence-backed defect.

## 1. Core architecture question

Verify that Synthesis consumes normalized source outputs and does not duplicate or replace the internal decision logic of:

- Project 1 — Flow Integrity;
- Project 2 — Agile Delivery;
- Project 3 — Control Value;
- Project 4 — Attestor.

Verify `source-manifest.json` keeps source-project facts authoritative.

## 2. Correlation taxonomy

The only canonical classes are:

- duplicate
- repeated
- related
- compounding
- contradictory
- unresolved

Run the exact-node test harness and confirm the synthetic reference fixture produces all six.

Check the deterministic classifier directly.

Try to produce:
- false duplicate;
- false repeated;
- false related;
- false compounding;
- suppressed contradiction;
- unresolved incorrectly forced into a stronger class.

## 3. No universal score / no pooled DPMO

Search the entire package.

Confirm:
- no universal enterprise risk score exists;
- source severities are not averaged or overwritten;
- domain DPMO denominators are not pooled;
- Synthesis has its own CTQ/opportunity model only.

Challenge Six Sigma 9/10 in the scorecard.

## 4. Source contracts and provenance

Inspect:
- `contracts/v1.0.0/`
- `source-manifest.json`
- `fixtures/source-signals.synthetic.json`
- `docs/EVIDENCE_MODEL.md`

Try:
- missing source project;
- unknown source;
- missing evidence;
- missing provenance;
- stale evidence;
- schema mismatch;
- malformed input;
- unavailable source.

Confirm fail-closed or degraded-unresolved handling.

## 5. AI authority

Inspect:
- `prompts/`
- nodes 09–11 in the main workflow;
- `docs/DECISION_RIGHTS.md`.

Verify AI cannot:
- change correlation class;
- change source severity/status;
- invent evidence;
- change deterministic route;
- suppress contradiction;
- authorize escalation;
- create a universal score.

Inject an AI → executive-route or AI → human-decision bypass edge and confirm graph validation fails.

## 6. Human authority

Check:
- preparation of decision contract;
- synthetic human fixture;
- deterministic validation;
- explicit `authenticatedIdentity=false`.

Do not allow labelled demo identity to become authenticated identity evidence.

## 7. Exact-node tests

Run:

`node tests/offline_exact_node_tests.js workflows/VANTIX-Synthesis-Cross-Project-Governed-Correlation-v0.1-public.json workflows/VANTIX-Synthesis-Adversarial-Regression-v0.1-public.json /tmp/synthesis.json`

Expected:
- 8/8 PASS;
- adversarial summary 24/24 PASS;
- evidence class `OFFLINE_EXACT_NODE_CODE_EXECUTION`;
- `n8nRuntimeExecution=false`;
- workflow hashes match the shipped JSON.

Modify one expectation and prove the harness exits non-zero.

## 8. Repository controls

Run:
- `python validation/validate_repository.py`
- `python scripts/validate_graph.py`
- `python scripts/checksums.py --check`

Then attack:

1. broken Markdown file link;
2. broken same-file anchor;
3. broken cross-file anchor;
4. fake API key in JS;
5. fake secret in HTML;
6. required file removed;
7. stale duplicate handoff/prompt added;
8. score dimension changed;
9. printed Total row changed;
10. main workflow changed without evidence regeneration;
11. adversarial workflow changed without evidence regeneration;
12. direct AI → executive route edge;
13. source-manifest project removed;
14. final commit status falsely changed from pending;
15. checksummed file tampered;
16. unsupported maturity wording inserted.

Report whether each relevant control fails.

## 9. Evidence honesty

Do not allow:
- offline exact-node execution → n8n runtime evidence;
- synthetic fixtures → live Projects 1–4 integration;
- synthetic human decision → authenticated human;
- synthetic DPMO → production capability;
- source repository URL → proof of final live commit;
- internal score → certification.

## 10. Score

Independently recalculate:

- Business 11/12
- Differentiation 8/8
- Architecture 12/12
- Bounded agency 10/10
- Security 10/12
- Six Sigma 9/10
- PMP 8/8
- Agile 6/6
- Testing 11/12
- Documentation 6/6
- Executive/demo 3/4

Proposed total: **94/100**.

Do not accept it automatically.

## Required response

1. Verdict:
   - `PASS — READY TO BIND FINAL SOURCE COMMITS AND UPLOAD`
   - `PASS WITH REQUIRED CORRECTIONS`
   - `BLOCKED`
2. Findings table: Severity | File | Finding | Evidence | Exact correction
3. Independent 100-point score
4. Architecture verdict
5. Correlation-taxonomy verdict
6. Source-authority verdict
7. AI/human-authority verdict
8. Six Sigma verdict
9. 8/8 exact-node verdict
10. 24/24 adversarial verdict
11. CI/negative-test verdict
12. Exact blockers before GitHub
13. Exact blockers before freeze
14. Questions only if they can materially change evidence/score/merge
15. Final challenge: strongest evidence-backed reason not to upload

Do not manufacture defects merely to extend the review cycle.
