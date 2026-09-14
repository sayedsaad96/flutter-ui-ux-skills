# Behavioral Evals

Run each scenario in a fresh agent context.

## RED
Run scenarios before `skills/flutter-ui-ux/SKILL.md` exists or is loaded. Record the agent's exact answer and score every rubric criterion.

## GREEN
After the first skill draft exists, run the same scenarios in fresh contexts with the skill loaded. Do not edit scenarios between RED and GREEN.

## REFACTOR
If GREEN reveals loopholes or inconsistent behavior, tighten only the guidance required by observed failures. Re-run all scenarios in fresh contexts.

## Recording
For every run record:
- model/runtime
- date
- scenario filename
- exact response
- rubric score
- observed rationalizations/failures

Never rewrite a baseline after seeing the skill-guided result.
