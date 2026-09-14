# Changelog

## [Unreleased]

The repository does not yet have a valid clean behavioral release gate. `v0.1.0` has not been tagged. See `evals/STATUS.md` for what a clean rerun requires before tagging.

### Added
- `flutter-ui-ux` orchestrator skill with CREATE / REDESIGN / AUDIT classification, MICRO / SCREEN / FLOW / PRODUCT task sizing, and the E0–E5 evidence ladder.
- Minimum-necessary capability routing, composite workflow handling (`AUDIT → REDESIGN → VERIFY`, `CREATE → review/polish → VERIFY`).
- Verification honesty and no-fake-delegation rules.
- Behavioral eval harness: six scenarios, routing rubric, static validator (`scripts/validate_skills.py`) with tests.
- **Prompt/expectation separation:** `evals/scenarios/` now contains only target-agent-visible content; `evals/expectations/` holds evaluator-only required-behavior content per scenario, enforced by `scripts/validate_evals.py` and its tests.
- **Evidence-access clarification** in `skills/flutter-ui-ux/SKILL.md`: evidence described as "available" in a request is distinguished from evidence actually accessible in the current runtime; the skill must never fabricate observations from evidence it could not actually access.
- Historical RED/GREEN/REFACTOR eval records (`evals/baselines/`, `evals/results/`) marked non-gating via a prepended notice, since the original scenario prompts leaked evaluator expectations before this separation existed. Raw responses preserved verbatim for transparency.
- `evals/STATUS.md` documenting the exact clean-rerun requirements and release gate.
- CI now runs the eval-isolation validator in addition to the skill validator and test suite.

### Changed
- README no longer claims the historical eval records prove behavioral verification; release readiness is now explicitly gated on a clean rerun.
