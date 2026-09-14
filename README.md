# Flutter UI/UX Skills

AI can write Flutter UI quickly. The harder problem is making that UI intentional, product-specific, adaptive, accessible, maintainable, fast, state-complete, animated with purpose, and visually convincing.

**Flutter UI/UX Skills** is a behaviorally tested design-engineering skill system for AI coding agents. Its goal is to make Flutter interfaces feel **designed, not generated**.

## Current Release

v0.1 ships exactly one skill: `flutter-ui-ux`, the Layer-1 orchestrator. It classifies Flutter UI/UX requests (CREATE / REDESIGN / AUDIT), sizes them (MICRO / SCREEN / FLOW / PRODUCT), checks available evidence before guessing, routes only the capabilities a task actually needs, and reports verification honestly. The remaining ten planned skills (three workflow skills, seven specialists) do **not** exist yet in this release — see Roadmap.

## Why This Exists

AI-generated Flutter UI tends to converge on the same generic patterns regardless of product, audience, or brand. This project is a set of Agent Skills that push AI coding agents toward evidence-first, product-specific, honestly-verified UI/UX work instead.

## Core Modes

- **CREATE** — new screens, flows, apps, or component families.
- **REDESIGN** — improving an existing UI, grounded in inspection of what already exists.
- **AUDIT** — read-only evaluation with prioritized findings; does not change code unless asked.
- Composite sequences: `AUDIT → REDESIGN → VERIFY`, `CREATE → review/polish → VERIFY`.

## Architecture

The full design is a layered skill system: one orchestrator (`flutter-ui-ux`), three workflow skills, and seven specialists. v0.1 implements only the orchestrator. See `docs/superpowers/specs/2026-09-14-flutter-ui-ux-skill-system-design.md` for the complete approved design.

## Install

```bash
npx skills add sayedsaad96/flutter-ui-ux-skills --skill flutter-ui-ux
```

## Behavioral Evals

Every skill in this system is authored using RED → GREEN → REFACTOR: baseline agent behavior is captured before the skill exists, the skill is written from the observed failures, then pressure-tested. See `evals/` for the six scenarios, the routing rubric, the RED baseline (all six scenarios failed without the skill), and the GREEN/REFACTOR results (all six pass with the skill loaded).

## Designed, Not Generated

The system's differentiation is a positive quality model, not a list of banned styles: product specificity, visual intent, experience coherence, system coherence, platform/context fit, and craft. See the design spec for the full quality model, design-smell tests, and hard-failure criteria.

## Roadmap

**Phase 1 — Foundation:** `flutter-ui-ux` (shipped in v0.1), `polishing-flutter-experiences`, `verifying-flutter-ui`.

**Phase 2 — Workflows:** `creating-flutter-ui`, `redesigning-flutter-ui`, `auditing-flutter-ui`.

**Phase 3 — Specialist Depth:** `designing-flutter-systems`, `building-responsive-adaptive-flutter`, `engineering-flutter-ui`, `designing-inclusive-flutter`, `crafting-flutter-motion`.

Each skill is completed and verified (RED → GREEN → REFACTOR) before work begins on the next.

## Contributing

See `CONTRIBUTING.md`.

## License

MIT — see `LICENSE`.
