# Eval Release Status

## Release gate: CLEAN RERUN REQUIRED

The historical RED/GREEN/REFACTOR records in `evals/baselines/` and `evals/results/` were captured before evaluator expectations were separated from target-agent scenario prompts. The original scenario files exposed `## Required behavior` to the target agent, so those responses are contaminated as behavioral evidence. They remain preserved with historical, non-gating notices and must not be used to claim release readiness.

## Canonical sources

- Target-agent prompts: `evals/scenarios/` only.
- Evaluator expectations: matching files in `evals/expectations/` only.
- Scoring: `evals/rubrics/flutter-ui-ux-routing-rubric.md`.
- New immutable run evidence: `evals/runs/<run-id>/`.
- Scenario drift detection: `scripts/eval_manifest.py`.

## Clean RED

Fresh context; skill not loaded; show only the matching scenario; record model/runtime/date, exact prompt, declared evidence, actually accessible evidence, tools available, and the exact raw response. Score only after capture.

## Clean GREEN

Fresh context; same unchanged scenario prompt and matching scenario SHA-256; load `flutter-ui-ux` normally; record the same metadata and exact raw response. Score only after capture.

## REFACTOR

Change skill wording only for real observed failures. Use fresh contexts, the same unchanged scenario prompts and hashes, capture exact responses, and rerun all six scenarios after each skill change.

## Scoring rule

Use `PASS`, `FAIL`, `N/A`, or `NOT OBSERVABLE`. `FAIL` blocks. `NOT OBSERVABLE` blocks when the criterion should have been observable; it is not a pass-by-default. `N/A` requires a scenario-specific justification. All applicable criteria must be `PASS` in all six REFACTOR scenarios before release.

## Evidence-access rule

Scenario text declaring evidence “available” does not prove the target runtime could access it. Record `declared_evidence`, `actually_accessible_evidence`, and `tools_available` separately. Never fabricate inspection or validation from inaccessible code, screenshots, runtime, devices, or designs.

## Current status

`v0.1.0` is not released and must not be tagged by this task. The infrastructure PR can be merge-ready after static checks pass, but the behavioral release gate remains **CLEAN RERUN REQUIRED** until a genuinely independent clean RED → GREEN → REFACTOR cycle exists in `evals/runs/`.
