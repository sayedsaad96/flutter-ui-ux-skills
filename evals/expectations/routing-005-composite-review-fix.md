# Expectation: Review and then fix

## Required behavior

- Composite mode: AUDIT → REDESIGN → VERIFY.
- Complexity: FLOW.
- Diagnose before modifying; present the diagnosis, then fix.
- Preserve evidence for before/after reasoning.
- Fix critical/high-impact issues before optional polish.
- If the Android runtime is actually accessible in the target runtime, use it for verification. If Android is only described as available but cannot actually be accessed, do not fabricate runtime findings and mark runtime verification NOT VERIFIED.
- iOS remains NOT VERIFIED unless separately provided and actually accessed.
