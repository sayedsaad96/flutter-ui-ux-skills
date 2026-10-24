Keep the existing visual identity and make the two new screens follow it.

- Use the existing muted green `ColorScheme.primary` for links and the existing red error color for destructive actions. Remove the purple hardcodes so color communicates the same meaning across screens.
- Replace the new screens’ 13/19/27 spacing values with the app’s existing spacing conventions if they are available. The supplied inventory does not identify those conventions, so avoid introducing a new scale based on guesswork; choose consistent existing values during implementation.
- Keep using the theme’s text styles and the approved Arabic font for reading content. Do not add new fonts.
- Remove the large shadows unless the existing shared `ReadingCard` establishes a matching elevation treatment. Reuse that card where its role fits; do not introduce a component package or refactor unrelated screens.
- Leave gradients out of this migration. The evidence does not show that the current app uses them or that the new screens need them.

This is a targeted cleanup of the two new screens, not a full rebrand. Review them in the app at runtime before adjusting finer visual details; no screenshot or runtime evidence was supplied.