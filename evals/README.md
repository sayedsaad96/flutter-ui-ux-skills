# Behavioral Evals

This directory defines the behavioral-evaluation protocol for the `flutter-ui-ux` orchestrator. Static CI validates the infrastructure; it does not pretend to run agent behavior evaluations.

## Directory ownership

- `evals/scenarios/` — the only canonical target-agent prompt source. Each file contains only material shown to the target agent: scenario title, user request, and declared available evidence.
- `evals/expectations/` — evaluator-only expectations paired by filename with scenarios. Never show these files to a target agent before its response is captured.
- `evals/rubrics/` — scoring criteria and verdict vocabulary.
- `evals/runs/` — immutable evidence from individual clean evaluation cycles. New RED/GREEN/REFACTOR evidence belongs here.
- `evals/baselines/` and `evals/results/` — historical legacy evidence only. They are preserved for transparency and must not be used as the preferred format or release-gating evidence for new runs.
- `evals/STATUS.md` — the current release-gate status and clean-rerun requirements.

There is no second prompt source. Deprecated `evals/prompts/` must not exist.

## Critical isolation rule

Never show the target agent files from `evals/expectations/`, `evals/rubrics/`, `evals/STATUS.md`, previous run outputs, or evaluator notes before its response is captured. The target agent receives only the matching file from `evals/scenarios/` (plus the normal skill/runtime context for that phase).

## Evidence accounting

Evidence described as “available” in a scenario is not necessarily evidence actually accessible to the target runtime. Every run must separately record:

- `declared_evidence`
- `actually_accessible_evidence`
- `tools_available`

The agent receives credit for inspecting evidence only when the run can show that evidence was actually accessible and the response supports that inspection. Never infer access merely from scenario wording.

## RED → GREEN → REFACTOR

### RED

- Use a fresh context.
- Do not load `skills/flutter-ui-ux/SKILL.md`.
- Show only the unchanged matching scenario.
- Capture the exact response verbatim.
- Score only after the response has been captured.

### GREEN

- Use a fresh context.
- Load `skills/flutter-ui-ux/SKILL.md` through the normal runtime mechanism.
- Show the same exact scenario prompt used for RED.
- Capture the exact response verbatim.
- Score only after the response has been captured.

### REFACTOR

- Change skill wording only in response to a real observed failure.
- Use a fresh context and the same exact scenario prompt.
- Capture the exact response verbatim.
- Re-run all six scenarios after any skill change.

Scenario content must not change between RED, GREEN, and REFACTOR. Use `scripts/eval_manifest.py` to fingerprint the six canonical scenario files and detect drift.

## Run evidence

Each clean cycle uses `evals/runs/<run-id>/` with a manifest and phase response files. Record the model/runtime, date, exact scenario and SHA-256, skill-loaded state, declared evidence, actually accessible evidence, tools available, exact response, per-criterion verdicts, and observed failures/rationalizations. Do not fabricate runtime/device/tool access or synthetic agent responses.

## Static checks

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/validate_skills.py .
python scripts/validate_evals.py .
python scripts/eval_manifest.py .
```
