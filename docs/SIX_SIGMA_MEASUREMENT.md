
# Six Sigma Measurement

## Critical rule

**No shared DPMO denominator is imported from Projects 1–4.**

Each source domain retains its own CTQs and opportunity model.

## Synthesis CTQ

Unit:
**one validated correlation record**

Opportunities per unit:
1. source binding present;
2. evidence binding present;
3. source authority preserved;
4. deterministic reason present;
5. deterministic route present.

Defect examples:
- missing source reference;
- unsupported evidence;
- authority overwrite;
- unexplained correlation;
- missing route.

The v0.1 fixture can compute a synthetic DPMO for the executed fixture. That number is explicitly not process capability, and no Sigma/Cpk claim is made.

## Cross-domain protection

`XDOM-01` tests that source-project DPMO denominators are not pooled.

Production capability would require a stable real process, sufficient observations, defined specifications and an appropriate statistical model.
