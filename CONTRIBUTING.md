# Contributing

This project requires behavioral-evaluation integrity for any skill or skill-wording change.

## Mandatory eval rules

1. Target agents receive only the matching file from `evals/scenarios/`.
2. Never show `evals/expectations/`, `evals/rubrics/`, `evals/STATUS.md`, prior outputs, or evaluator notes before response capture.
3. RED happens before behavior-changing skill wording, in a fresh context with the skill absent.
4. Scenario prompts remain unchanged between RED, GREEN, and REFACTOR; verify this with `scripts/eval_manifest.py`.
5. Raw responses remain verbatim.
6. Evidence described as available is not automatically evidence actually inspected. Record declared evidence separately from actually accessible evidence and tools available.
7. Do not fabricate failures, passes, runtime access, device access, or tool use.
8. `NOT OBSERVABLE` is not a pass; follow the rubric release-gate rules.
9. No vague “improves quality” claim without clean behavioral evidence.
10. Complete and cleanly gate one skill before authoring the next.

## Local verification

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/validate_skills.py .
python scripts/validate_evals.py .
python scripts/eval_manifest.py .
```

## Pull requests

CI runs the same static tests and validators plus the placeholder scan. Static CI validates infrastructure only; it does not perform or imply behavioral RED/GREEN/REFACTOR evaluations.
