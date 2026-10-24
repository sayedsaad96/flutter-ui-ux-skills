---
name: designing-inclusive-flutter
description: Use when Flutter UI needs accessibility, Arabic/English or other localization, RTL/LTR and mixed-direction content, large text, semantic controls, keyboard/focus access, contrast or reduced-motion support.
---

# Designing Inclusive Flutter

Treat language, text size, assistive technology and input method as design
constraints. Own inclusive behavior; preserve canonical business/user content.

## Inspect the real barriers

Read affected controls, layout constraints, localization, directionality, semantic
structure and focus behavior. Use available renders/runtime, but distinguish
code risks from measured contrast or observed screen-reader behavior. Do not
claim compliance from source inspection or a supplied palette alone.

| Concern | Implementation direction |
|---|---|
| Actions | Prefer semantic SDK controls, localized accessible names and usable hit areas |
| Text scaling | Preserve system scaling; permit wrapping, growth and scrolling |
| RTL/LTR | Directional padding/alignment and meaningful navigation/icon mirroring |
| Mixed content | Isolate direction-sensitive identifiers at the display boundary |
| Keyboard/focus | Reachable actions, visible focus, logical traversal and stable restoration |
| Status/contrast | Text/semantics alongside color; measured foreground/background combinations |
| Motion | Essential information without motion and respect for reduced-motion preferences |

An icon glyph's size is not its hit target. Follow project/target-platform
ergonomic requirements without making the glyph huge. Avoid overlapping hit
regions, duplicate semantics and focusable decoration. Announce important
pending/error/result changes appropriately without continuously interrupting
assistive-technology users. Keep focus on a useful destination after dialogs,
navigation, validation and list changes.

## Localize layout and content together

Use the app's localization and locale-aware formatting for messages, plurals,
dates, times and numbers. Allow translation expansion and language-appropriate
font coverage. Direction is a property of the UI context, not a reason to reverse
strings manually or force the whole application LTR.

In mixed Arabic/English rows, keep the name in the surrounding reading direction
and give a Latin identifier its own appropriate directional text boundary. Use
explicit text direction or tested presentation-layer bidi isolation where needed.
Do not alter the stored name/identifier, insert controls into canonical data or
assume amounts should always use one numeral system. Verify displayed punctuation,
copying and semantic reading order as well as alignment.

Example: an invoice row needs directional start padding, a growing/wrapping
content region, a separately rendered invoice ID and a localized semantic delete
button. Disabling text scaling or forcing the entire row LTR hides the layout
problem and changes the reading experience.

## Validate the affected experience

Exercise Arabic/English or relevant locales, both directions, representative
large text and long content, narrow/wide constraints, keyboard activation and
screen-reader names/order. Measure contrast against actual surfaces and states;
test selected, disabled, error and focus indicators without relying only on color.
Use relevant Flutter accessibility guidelines/tests where supported by the project.

Report the barriers addressed, data/behavior preserved and checks actually
performed. Mark unavailable contrast measurements, runtime, assistive-technology,
keyboard, large-text and RTL checks NOT VERIFIED. Layout inclusion requirements
may inform adaptation; animation implementation remains motion's responsibility.
