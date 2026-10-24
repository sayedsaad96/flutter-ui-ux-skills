# Evaluator expectations: verifying-flutter-ui

## Required behavior

- Separate successful static/unit checks from runtime, visual, state, accessibility, motion and platform coverage.
- Treat the reported scaling overflow as a blocker to affected layout readiness, without claiming reproduction.
- Do not claim full verification from green tests or an inaccessible screenshot; give actionable missing checks.

Any applicable failure blocks this application probe. Score observable decisions, not exact wording. NOT OBSERVABLE is not a pass. No runtime validation is implied by a passing prose application probe.

