# Contributing

This project requires behavioral evidence for any skill or skill-wording change, not just review-by-reading.

## Eval integrity (mandatory)

1. **Target agents receive only `evals/scenarios/`.** Never show a target agent anything from `evals/expectations/`, `evals/rubrics/`, `evals/STATUS.md`, or this file before its response is captured.
2. **Expectations and the rubric must not be shown before the response is captured.** Score only after the exact response is recorded.
3. **RED must happen before any behavior-changing skill wording is written.** Capture baseline failures first, in a fresh context, with the skill not loaded.
4. **Scenario prompts remain unchanged between RED and GREEN.** Do not edit a scenario after seeing how an agent responds to it, and never edit it merely to force a failure or a pass.
5. **Raw responses remain verbatim.** Baseline, GREEN, and REFACTOR records must contain the exact captured text, not paraphrases or summaries.
6. **Evidence described as available is not automatically evidence actually inspected.** A scenario saying "code is available" does not mean the agent opened it. Record what evidence was *actually accessible* in the run, separately from what the scenario merely describes.
7. **Actual runtime/tool access must be recorded.** If a run had no real tool access to inspect code/screenshots/runtime, say so in the evidence record rather than assuming the scenario's description was acted on.
8. **Do not fabricate failures or passes.** Every verdict must trace to the actual captured raw response.
9. **No vague "improves quality" claim without clean behavioral evidence.** A change must cite a specific scenario/criterion that moved from FAIL to PASS (or vice versa) under a clean rerun.
10. **One skill completed and verified before authoring the next.** Do not begin a second skill's RED/GREEN/REFACTOR cycle while `flutter-ui-ux` (or any skill) is mid-cycle or its release gate is not READY.

## Local verification commands

Run all three before proposing any change:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/validate_skills.py .
python scripts/validate_evals.py .
```

## Pull requests

CI (`.github/workflows/validate.yml`) runs the same three checks plus a placeholder-marker scan on every push and pull request. All must pass. See `evals/STATUS.md` for the current release gate status before claiming any eval-based readiness in a PR description.
