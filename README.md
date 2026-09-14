# Flutter UI/UX Skills

AI can write Flutter UI quickly. The harder problem is making that UI intentional, product-specific, adaptive, accessible, maintainable, fast, state-complete, animated with purpose, and visually convincing.

**Flutter UI/UX Skills** is a design-engineering skill system for AI coding agents. Its goal is to make Flutter interfaces feel **designed, not generated**.

## Current Status

`main` contains the **v0.1 release candidate** with one skill: `flutter-ui-ux`, the Layer-1 orchestrator. It classifies Flutter UI/UX requests (CREATE / REDESIGN / AUDIT), sizes them (MICRO / SCREEN / FLOW / PRODUCT), checks available evidence before guessing, routes only the capabilities a task actually needs, and reports verification honestly.

The repository does **not** have a `v0.1.0` tag yet. A clean RED → GREEN → REFACTOR rerun is required before release because the first eval records were produced before target prompts and evaluator expectations were strictly separated. See `evals/STATUS.md`.

The remaining ten planned skills do **not** exist yet by design; see Roadmap.

## Why This Exists

AI-generated Flutter UI tends to converge on the same generic patterns regardless of product, audience, or brand. This project pushes AI coding agents toward evidence-first, product-specific, honestly-verified UI/UX work instead.

## Core Modes

- **CREATE** — new screens, flows, apps, or component families.
- **REDESIGN** — improving an existing UI, grounded in inspection of what already exists when it is actually accessible.
- **AUDIT** — read-only evaluation with prioritized findings; does not change code unless asked.
- Composite sequences: `AUDIT → REDESIGN → VERIFY`, `CREATE → review/polish → VERIFY`.

## Architecture

The full design is a layered skill system: one orchestrator (`flutter-ui-ux`), three workflow skills, and seven specialists. The v0.1 candidate implements only the orchestrator. See `docs/superpowers/specs/2026-09-14-flutter-ui-ux-skill-system-design.md` for the complete approved design.

## Install Pre-release From `main`

```bash
npx skills add sayedsaad96/flutter-ui-ux-skills --skill flutter-ui-ux
```

Treat this as a pre-release install until `v0.1.0` is tagged.

## Behavioral Evals

Every skill is intended to follow RED → GREEN → REFACTOR.

The eval harness now strictly separates:
- target-agent prompts in `evals/scenarios/`;
- evaluator-only expectations in `evals/expectations/`;
- scoring rules in `evals/rubrics/`.

The original 2026-09-14 RED/GREEN/REFACTOR records are retained for transparency but are **historical and non-gating** because the scenario files still contained evaluator-only `Required behavior` sections at the time. See `evals/STATUS.md` for the clean rerun gate.

## Designed, Not Generated

The system's differentiation is a positive quality model, not a list of banned styles: product specificity, visual intent, experience coherence, system coherence, platform/context fit, and craft. See the design spec for the full quality model, design-smell tests, motion quality, and hard-failure criteria.

## Roadmap

**Phase 1 — Foundation:** `flutter-ui-ux` (v0.1 candidate), `polishing-flutter-experiences`, `verifying-flutter-ui`.

**Phase 2 — Workflows:** `creating-flutter-ui`, `redesigning-flutter-ui`, `auditing-flutter-ui`.

**Phase 3 — Specialist Depth:** `designing-flutter-systems`, `building-responsive-adaptive-flutter`, `engineering-flutter-ui`, `designing-inclusive-flutter`, `crafting-flutter-motion`.

Each skill is completed and verified before work begins on the next.

## Contributing

See `CONTRIBUTING.md`.

## License

MIT — see `LICENSE`.
