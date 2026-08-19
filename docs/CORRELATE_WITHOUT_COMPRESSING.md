# Correlate Without Compressing

**Preserve domain truth while surfacing cross-domain relationships.**

> A reusable VANTIX design principle for cross-domain correlation without destroying source-domain meaning.

## Purpose

VANTIX Synthesis correlates normalized source outputs from Projects 1–4 while preserving the authority, measurement boundaries, and unresolved conflicts of each source domain. This principle documents behavior already implemented by Synthesis; it does not introduce a new architecture.

## Canonical relationship classes

Synthesis uses exactly six relationship classes:

1. `duplicate` — distinct records represent the same evidence event.
2. `repeated` — the same source/domain control condition recurs for the same entity/outcome without being the same evidence event.
3. `related` — different source projects reference the same entity/outcome without meeting a stronger deterministic class.
4. `compounding` — three or more source projects contribute unresolved or negative signals to the same entity/outcome.
5. `contradictory` — authoritative signals assert different values for the same claim key.
6. `unresolved` — available evidence is insufficient for a stronger class.

The detailed deterministic rules and precedence remain canonical in [Correlation Taxonomy](CORRELATION_TAXONOMY.md).

## 1. Preserve source authority

Synthesis cannot overwrite originating-project facts, severity, status, approval state, closure state, or other authoritative source fields. Correlation creates a relationship record around source facts; it does not replace them.

## 2. Do not average unlike measures

Synthesis does not pool DPMO denominators, average Sigma measures, or create a universal enterprise score merely because signals can be correlated. Cross-domain aggregation is valid only when a genuinely shared measurement model exists and is explicitly defined. The current Portfolio Preview does not make that claim.

## 3. Contradiction is information

Conflicting authoritative evidence remains visible. Synthesis must not average, suppress, or silently resolve contradictory source facts. Contradiction is itself a governed correlation outcome requiring downstream review.

## 4. AI explains; deterministic logic classifies

Deterministic logic owns the correlation class and governed route. AI may explain or critique the deterministic result, but it cannot redefine correlation truth, alter source authority, suppress contradiction, or authorize consequential action.

## 5. Correlation is not causation

A `related` or `compounding` classification identifies a governed cross-domain relationship. It does not by itself establish that one signal caused another. Causal language requires separate evidence sufficient to support that conclusion.

## Evidence boundary

This principle is demonstrated here within the **Portfolio Preview / synthetic evidence** boundary. It does not claim live production integration, production model execution, authenticated production human identity, real customer action, production ROI, independent certification, or production penetration testing.
