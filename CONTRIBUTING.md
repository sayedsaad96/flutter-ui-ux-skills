# Contributing

This project requires behavioral evidence for any skill or skill-wording change, not just review-by-reading.

## Eval integrity

1. **Prompts and expectations must be isolated.** Target agents may receive only files from `evals/scenarios/`. Never provide `evals/expectations/` or the rubric until after the target response is captured.
2. **RED baseline first.** Run the target scenarios in a fresh agent context without the skill (or without the change) loaded and record exact responses before writing behavior-changing skill wording.
3. **Unchanged scenario inputs between RED and GREEN.** Do not edit a scenario after seeing how an agent responds to it merely to force a failure or pass.
4. **Access is not implied by description.** If a scenario says code/screenshots/runtime are available, record whether they were actually attached or tool-accessible. Agents must not receive credit for fictional inspection.
5. **Exact responses preserved.** Baseline, GREEN, and REFACTOR records must contain verbatim agent responses.
6. **One skill completed and deployed before starting the next.** Do not begin authoring another skill while the current one is mid RED/GREEN/REFACTOR cycle.
7. **No vague quality claims.** Do not claim behavior improvement without clean eval evidence.

## Static validation

Run:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/validate_skills.py .
python scripts/validate_evals.py .
```

All commands must pass before merge.

## Pull requests

CI (`.github/workflows/validate.yml`) runs skill validation, eval-isolation validation, tests, and placeholder checks on every push and pull request.
