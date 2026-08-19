
# Correlation Taxonomy

## Duplicate

Two distinct records represent the same evidence event.

Reference rule: matching non-null evidence fingerprint.

## Repeated

The same source/domain control condition occurs again for the same entity/outcome without being the same evidence event.

Reference rule: same project + entity + outcome + control; distinct evidence fingerprints.

## Related

Different source projects reference the same entity/outcome but do not meet duplicate, contradiction or compounding rules.

## Compounding

Three or more source projects contribute unresolved or negative signals to the same entity/outcome.

Compounding is not a sum of risk scores. It is a deterministic relationship classification.

## Contradictory

Authoritative signals assert different values for the same claim key.

Contradiction must remain visible; AI cannot choose which source “wins.”

## Unresolved

Evidence is insufficient for a stronger class.

`unresolved` is a valid governed outcome, not a failure to be hidden.

## Precedence

For overlapping candidate facts, the engine's safe precedence is:

**contradictory → compounding → duplicate → repeated → related → unresolved**

A candidate can be re-evaluated only when new evidence is supplied.
