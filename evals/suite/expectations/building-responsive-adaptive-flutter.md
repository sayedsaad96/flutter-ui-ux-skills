# Evaluator expectations: building-responsive-adaptive-flutter

## Required behavior

- Use local bounded LayoutBuilder constraints rather than window width for the panel and choose content-driven transitions.
- Distinguish resizing/reflow from navigation/input adaptation; preserve selected state/scroll across layout changes.
- Address fold/display occlusion and keyboard/pointer/touch, avoid OS-only decisions, do not claim device verification.

Any applicable failure blocks this application probe. Score observable decisions, not exact wording. NOT OBSERVABLE is not a pass. No runtime validation is implied by a passing prose application probe.

