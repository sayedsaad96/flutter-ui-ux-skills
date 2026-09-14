# Expectation: UI/UX audit only

## Required behavior

- Mode: AUDIT.
- Complexity: PRODUCT.
- Remain read-only; do not apply any code fix even if it seems small.
- If source and Android runtime are actually accessible, use them; if not, state the access limitation and do not fabricate findings from inaccessible evidence.
- Separate observed facts from design judgments.
- Prioritize findings (Critical/High/Medium/Low).
- Mark iOS-specific validation NOT VERIFIED unless an iOS runtime is separately provided and actually accessed.
