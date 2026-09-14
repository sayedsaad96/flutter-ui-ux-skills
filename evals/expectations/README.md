# Expectations (Evaluator-Only)

Files in this directory are evaluator-only and must never be shown to the target agent before its response is captured.

Each file here matches a scenario in `evals/scenarios/` by filename and contains the required behavior, expected mode/complexity classification, and the criteria used to score a captured response against `evals/rubrics/flutter-ui-ux-routing-rubric.md`.

## Usage

1. Show the target agent only the matching file in `evals/scenarios/` — nothing from this directory.
2. Capture its exact, verbatim response before doing anything else.
3. Only after the response is captured, open the matching file here to score it.

Showing a target agent any file from this directory before its response is captured invalidates that run as behavioral evidence.
