
# Evidence Model

Each synthesis signal carries:
- source identity;
- source record/run IDs;
- entity/outcome keys;
- source status/severity;
- evidence references;
- evidence fingerprint when available;
- provenance class;
- authoritative-field declaration.

## Evidence rule

Synthesis may cite evidence. It may not replace source evidence with AI text.

## Source-authority rule

If Project 2 says a work item is not approved, Synthesis cannot call it approved.

If Project 3 says a commitment outcome is not verified, Synthesis cannot convert that into verified closure.

If Project 4 reports contradictory customer evidence, Synthesis must preserve that contradiction.

## Commit binding

Final GitHub commit SHAs live in `source-manifest.json`.

They are intentionally reference metadata so final upload changes in Projects 1–4 do not require rebuilding the Synthesis architecture.
