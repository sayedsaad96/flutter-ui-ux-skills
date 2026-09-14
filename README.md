# Flutter UI/UX Skills

AI can write Flutter UI quickly. The harder problem is making that UI intentional, product-specific, adaptive, accessible, maintainable, fast, state-complete, animated with purpose, and visually convincing.

**Flutter UI/UX Skills** is a behaviorally tested design-engineering skill system for AI coding agents. Its goal is to make Flutter interfaces feel **designed, not generated**.

## Current Release

`main` currently contains the **v0.1 release candidate**, not a tagged release. Only one skill exists: `flutter-ui-ux`, the Layer-1 orchestrator. The other ten planned skills (three workflow skills, seven specialists) do not exist yet — that is by design, not an oversight. See Roadmap.

**`v0.1.0` has not been tagged and must not be considered released until a clean behavioral eval rerun passes.** The repository's earlier RED/GREEN/REFACTOR eval records were captured while the target-agent scenario prompts still contained evaluator-only "Required behavior" sections, which contaminates them as evidence — the agent being tested could see the answer key. Those records are preserved for transparency in `evals/baselines/` and `evals/results/`, each marked with a historical, non-gating notice, but they cannot be cited as proof the orchestrator works. See `evals/STATUS.md` for the exact release gate and what a clean rerun requires.

## Why This Exists

AI-generated Flutter UI tends to converge on the same generic patterns regardless of product, audience, or brand. This project is a set of Agent Skills that push AI coding agents toward evidence-first, product-specific, honestly-verified UI/UX work instead.

## Core Modes

- **CREATE** — new screens, flows, apps, or component families.
- **REDESIGN** — improving an existing UI, grounded in inspection of what already exists.
- **AUDIT** — read-only evaluation with prioritized findings; does not change code unless asked.
- Composite sequences: `AUDIT → REDESIGN → VERIFY`, `CREATE → review/polish → VERIFY`.

## Architecture

The full design is a layered skill system: one orchestrator (`flutter-ui-ux`), three workflow skills, and seven specialists. This release candidate implements only the orchestrator. See `docs/superpowers/specs/2026-09-14-flutter-ui-ux-skill-system-design.md` for the complete approved design.

## Prompt / Expectation Isolation

`evals/scenarios/` contains only what a target agent is allowed to see: scenario title, user request, and available evidence. `evals/expectations/` contains the evaluator-only required behavior for each matching scenario and must never be shown to a target agent before its response is captured. This separation is enforced by `scripts/validate_evals.py` and its tests, and is required reading before running any eval — see `evals/expectations/README.md` and `evals/STATUS.md`.

## Install

```bash
npx skills add sayedsaad96/flutter-ui-ux-skills --skill flutter-ui-ux
```

This installs from `main`, i.e. the pre-release candidate — not a tagged version, since `v0.1.0` has not been tagged yet.

## Behavioral Evals

Every skill in this system is meant to be authored using RED → GREEN → REFACTOR: baseline agent behavior is captured before the skill exists, the skill is written from the observed failures, then pressure-tested. The current `evals/baselines/` and `evals/results/` records predate prompt/expectation isolation and are kept only as historical, non-gating evidence. A clean rerun using the isolated `evals/scenarios/` and `evals/expectations/` has not yet been performed — see `evals/STATUS.md` for the exact release gate.

## Designed, Not Generated

The system's differentiation is a positive quality model, not a list of banned styles: product specificity, visual intent, experience coherence, system coherence, platform/context fit, and craft. See the design spec for the full quality model, design-smell tests, and hard-failure criteria.

## Roadmap

**Phase 1 — Foundation:** `flutter-ui-ux` (this release candidate), `polishing-flutter-experiences`, `verifying-flutter-ui`.

**Phase 2 — Workflows:** `creating-flutter-ui`, `redesigning-flutter-ui`, `auditing-flutter-ui`.

**Phase 3 — Specialist Depth:** `designing-flutter-systems`, `building-responsive-adaptive-flutter`, `engineering-flutter-ui`, `designing-inclusive-flutter`, `crafting-flutter-motion`.

Each skill is completed and verified (RED → GREEN → REFACTOR, with clean prompt/expectation isolation) before work begins on the next. None of the Phase 1–3 skills beyond `flutter-ui-ux` currently exist in this repository.

## Contributing

See `CONTRIBUTING.md`.

## License

MIT — see `LICENSE`.
