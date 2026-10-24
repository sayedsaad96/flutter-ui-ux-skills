# Evaluator expectations: designing-inclusive-flutter

## Required behavior

- Use directional layout while isolating only directionally sensitive identifiers; do not force whole-row LTR or reorder underlying text.
- Preserve text scaling, adapt height/wrapping, provide labeled reachable action/focus/keyboard and usable hit targets.
- Contrast and assistive-tech checks remain unverified without measurements/runtime; preserve data and localization behavior.

Any applicable failure blocks this application probe. Score observable decisions, not exact wording. NOT OBSERVABLE is not a pass. No runtime validation is implied by a passing prose application probe.

