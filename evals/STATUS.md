# Eval Release Status

## Release gate: CLEAN RERUN REQUIRED

The historical RED/GREEN/REFACTOR records currently in `evals/baselines/` and `evals/results/` were captured before target-agent scenario prompts (`evals/scenarios/`) were separated from evaluator-only expectations (`evals/expectations/`). Those original scenario files contained a `## Required behavior` section that the target agent could see before answering. That contaminates the evidence: a response that "correctly" classified mode/complexity or avoided a failure mode may simply have been reading the answer key rather than reasoning it out.

**Because of this, the historical records do not count as release-gating behavioral evidence.** They are preserved verbatim for transparency (see the historical notice prepended to each file), but no release claim may cite them as proof the orchestrator works.

## What "clean" means

### Clean RED
- Fresh agent context, `skills/flutter-ui-ux/SKILL.md` **not** loaded.
- The target agent is shown **only** the matching file in `evals/scenarios/` — nothing from `evals/expectations/`, `evals/rubrics/`, or this file.
- Capture the exact, verbatim response before doing anything else.

### Clean GREEN
- Same six unchanged scenario prompts from `evals/scenarios/`.
- `skills/flutter-ui-ux/SKILL.md` loaded via the runtime's normal skill mechanism.
- Capture the exact, verbatim response.

### REFACTOR
- Only modify `SKILL.md` wording in direct response to a real, observed failure from the clean RED or clean GREEN run.
- Do not broaden the skill for hypothetical failures.
- Re-run all six scenarios again after any change, in fresh contexts.

### Scoring
- Score each captured response against the matching file in `evals/expectations/` and against `evals/rubrics/flutter-ui-ux-routing-rubric.md`.
- Do not open the expectation file until after the response is captured.

### Evidence record (required for every run)
- Model/runtime used.
- Date.
- The exact target prompt shown (must match `evals/scenarios/*.md` verbatim).
- What evidence was **actually accessible** to the agent in that run (not just what the scenario says is "available").
- The exact, verbatim raw response.
- Rubric score per criterion.
- Any observed failure or rationalization, quoted verbatim.

### Release condition
`v0.1.0` may only be tagged once all applicable rubric criteria PASS in all six REFACTOR scenarios, scored from a clean rerun that satisfies the above. Until then, the release gate is **CLEAN RERUN REQUIRED**, not READY.
