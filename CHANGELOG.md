# Changelog

## [Unreleased] — 0.2.0rc1

This is a locally prepared complete-suite candidate, not a published/tagged
release. See `evals/STATUS.md` and `docs/RELEASE_READINESS.md`.

### Added

- All ten planned workflow/specialist skills, completing the eleven-skill design.
- Ten isolated control/application scenario pairs, evaluator-only expectations
  and verbatim response captures.
- Four targeted Codex discovery probes with separate action logs.
- Release evidence validation covering every skill and all sixteen application
  cases, including criterion scores and SHA-256 drift checks.
- Pinned canonical scenario fingerprints and cross-platform evidence attributes.
- Regression coverage for empty/incomplete skill trees, invalid names, duplicate
  frontmatter keys, missing local references and invalid release evidence.

### Changed

- Orchestrator routing now identifies current and later PRODUCT CREATE concerns
  and names each suite decision owner.
- Installation and contribution guidance distinguish local preparation, remote
  availability, explicit invocation, automatic discovery and app validation.
- Stale release claims and implementation-plan status are reconciled with the
  preserved historical evidence.

### Historical 0.1 candidate

The orchestrator-only 0.1.0rc1 was never released/tagged. Its first clean
Antigravity run ended at 3/6 passing due to activation failures; older contaminated
records remain non-gating history. New explicit-use confirmation passes all six
scenarios in Codex and does not claim to fix the earlier runtime's activation.
