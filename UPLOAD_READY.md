
# Upload Ready

**Current state: LOCALLY GREEN / READY FOR ADVERSARIAL REVIEW**

The package is complete enough to be reviewed by another LLM today.

Before GitHub freeze:
1. another LLM may adversarially review this ZIP;
2. correct only evidence-backed defects;
3. after Projects 1–4 are live and Green, insert their final commit SHAs in `source-manifest.json`;
4. regenerate checksums;
5. upload Synthesis;
6. require the exact GitHub Actions run to pass;
7. freeze.

Final source commit binding is intentionally metadata-only and should not require workflow redesign.
