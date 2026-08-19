# Negative-Test Evidence

All attacks below were executed against disposable copies of the final local package. A control passes only when the attack produces a non-zero exit.

| Attack | Enforced by | Result |
|---|---|---|
| broken Markdown link | repo | **PASS — rejected (exit 1)** |
| broken same-file anchor | repo | **PASS — rejected (exit 1)** |
| broken cross-file anchor | repo | **PASS — rejected (exit 1)** |
| fake API secret in JS | repo | **PASS — rejected (exit 1)** |
| fake secret in HTML | repo | **PASS — rejected (exit 1)** |
| required file removed | repo | **PASS — rejected (exit 1)** |
| stale duplicate handoff | repo | **PASS — rejected (exit 1)** |
| score dimension tampered | repo | **PASS — rejected (exit 1)** |
| score printed total tampered | repo | **PASS — rejected (exit 1)** |
| main workflow hash drift | repo | **PASS — rejected (exit 1)** |
| adversarial workflow hash drift | repo | **PASS — rejected (exit 1)** |
| AI direct executive-route bypass | graph | **PASS — rejected (exit 1)** |
| source manifest project removed | repo | **PASS — rejected (exit 1)** |
| frozen source commit binding tampered | repo | **PASS — rejected (exit 1)** |
| checksum tamper | checksum | **PASS — rejected (exit 1)** |
| unsupported maturity wording | repo | **PASS — rejected (exit 1)** |
| offline expectation broken | offline | **PASS — rejected (exit 1)** |

**Result: 17/17 package attacks correctly rejected.**

These tests validate repository and control behavior. They are not production penetration-test evidence.
