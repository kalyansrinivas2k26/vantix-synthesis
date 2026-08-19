
# OWASP-Aligned AI Security Mapping

This is a control mapping, not certification.

| Threat area | Control | Executed test |
|---|---|---|
| Prompt injection / policy override | AI cannot change deterministic class/route | `AI-01` |
| Source-fact manipulation | AI cannot change source severity | `AI-02` |
| Unsupported output/evidence | evidence refs must be known | `AI-03`, `PROV-02` |
| Excessive agency | AI route override is rejected | `AI-04` |
| Broken source binding | missing/unknown source is blocked | `SRC-01`–`SRC-04` |
| Stale/invalid evidence | evidence gate blocks it | `PROV-01`–`PROV-04` |
| False correlation | six negative-correlation tests | `COR-01`–`COR-06` |
| Human authority mismatch | decision contract validation | `AUTH-01`, `AUTH-02` |
| Cross-domain contamination | denominator/source-authority isolation | `XDOM-01`, `XDOM-02` |
| Dependency degradation | unavailable/malformed source handled safely | `XDOM-03`, `XDOM-04` |

Production IAM, provider security, penetration testing and production DLP remain unproven.
