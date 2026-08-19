
# Architecture

## Layer 1 — Source contracts

Synthesis accepts normalized signals from Projects 1–4 through `contracts/v1.0.0/source-signal.schema.json`.

Only shared correlation fields cross the boundary. Source projects retain authority for their own domain facts.

## Layer 2 — Evidence and provenance gate

Every source signal requires:
- source project;
- source domain;
- source record ID;
- schema version;
- observed timestamp;
- entity and outcome keys;
- evidence references;
- provenance;
- authoritative-field declaration.

## Layer 3 — Deterministic correlation engine

The engine classifies candidate relationships into exactly:
- duplicate;
- repeated;
- related;
- compounding;
- contradictory;
- unresolved.

This layer follows the [Correlate Without Compressing](CORRELATE_WITHOUT_COMPRESSING.md) principle: cross-domain relationships are surfaced without collapsing source-domain authority or unlike measurements.

## Layer 4 — Bounded AI

AI-style explanation is downstream of deterministic classification.

It cannot:
- add evidence;
- alter class or route;
- change source facts;
- suppress contradiction;
- create a universal score.

## Layer 5 — Human authority

The workflow creates a human-decision contract for consequential routes. The current Portfolio Preview uses a labelled synthetic decision fixture.

## Layer 6 — Measurement

Synthesis measures defects in the synthesis process itself. It does not pool the CTQ opportunity denominators of Projects 1–4.

## Layer 7 — Audit output

The final record contains:
- source projects/domains;
- correlation classes;
- evidence references;
- deterministic reasons/routes;
- AI validation state;
- human-decision validation state;
- measurement boundary;
- audit events.
