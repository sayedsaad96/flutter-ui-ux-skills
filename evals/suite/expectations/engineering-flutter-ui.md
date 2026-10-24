# Evaluator expectations: engineering-flutter-ui

## Required behavior

- Identify network side effects in build and ignored Cubit state without creating a competing async owner.
- Render existing states, use lazy bounded scrolling and preserve cancellation/order/selection behavior.
- Focused composition and existing dependencies first; do not invent measured performance or rewrite architecture.

Any applicable failure blocks this application probe. Score observable decisions, not exact wording. NOT OBSERVABLE is not a pass. No runtime validation is implied by a passing prose application probe.

