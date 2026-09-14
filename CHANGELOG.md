# Changelog

## [Unreleased]

`v0.1.0` has not been released or tagged. The clean behavioral release gate remains CLEAN RERUN REQUIRED; see `evals/STATUS.md`.

### Added
- `flutter-ui-ux` orchestrator with CREATE / REDESIGN / AUDIT, MICRO / SCREEN / FLOW / PRODUCT sizing, and E0–E5 evidence levels.
- Prompt/expectation isolation: canonical target prompts in `evals/scenarios/`, evaluator-only expectations in `evals/expectations/`.
- Static eval-isolation validation, exact six-scenario enforcement, and tests.
- SHA-256 scenario fingerprinting for RED/GREEN/REFACTOR drift detection.
- Canonical `evals/runs/` structure for future immutable clean-run evidence.
- PASS / FAIL / N/A / NOT OBSERVABLE rubric vocabulary with explicit release-gate semantics.
- Evidence-access clarification distinguishing declared evidence from actually accessible evidence.
- Historical RED/GREEN/REFACTOR records preserved as non-gating evidence.

### Changed
- Project version is `0.1.0rc1` until the clean behavioral gate passes.
- Release documentation no longer claims the current candidate is behaviorally verified.
