# Contributing

This project requires behavioral evidence for any skill or skill-wording change, not just review-by-reading.

## Requirements for any new skill or behavior-changing edit

1. **RED baseline first.** Run the target scenarios in a fresh agent context without the skill (or without the change) loaded, and record the exact responses before writing or editing any skill wording.
2. **Unchanged scenario inputs between RED and GREEN.** Do not edit a scenario after seeing how an agent responds to it, and do not edit it merely to force a failure or a pass.
3. **Exact responses preserved in eval records.** Baseline, GREEN, and REFACTOR files must contain verbatim agent responses, not paraphrases or summaries.
4. **Static validation passing.** `python -m unittest tests.test_validate_skills -v` and `python scripts/validate_skills.py .` must both pass before a skill is merged.
5. **One skill completed and deployed before starting the next.** Do not begin authoring a second skill while an existing one is mid RED/GREEN/REFACTOR cycle.
6. **No vague quality claims.** Do not describe a change as "improves quality" or similar without an eval that demonstrates the specific behavior change (a failing scenario that now passes, or a new failure pattern caught).

## Pull requests

CI (`.github/workflows/validate.yml`) runs the validator tests, the skill metadata validator, and a placeholder-marker scan on every push and pull request. All three must pass.
