# Scenario: UI/UX audit only

## User request

"Audit this Flutter app for UI/UX problems before release. I only want findings and priorities; do not change code."

## Available evidence

- Flutter source is available.
- Runtime on one Android phone is available.
- No iOS device is available.

## Required behavior

- Mode: AUDIT.
- Complexity: PRODUCT.
- Remain read-only.
- Use source and Android runtime evidence.
- Separate observed facts from design judgments.
- Prioritize findings.
- Mark iOS-specific validation NOT VERIFIED rather than implying coverage.
