---
name: polishing-flutter-experiences
description: Use when an implemented Flutter screen or flow needs refinement of hierarchy, spacing, alignment, density, feedback, or product character without a broad redesign.
---

# Polishing Flutter Experiences

Improve perceived craft by clarifying the user's task. Polish follows a working
experience; broken actions, missing critical states and inaccessible controls
take priority over decorative refinement.

## Evidence and scope

Inspect the supplied implementation, theme and any accessible visuals. A code
excerpt supports code observations, not claims about rendered alignment or
contrast. State missing evidence and preserve navigation, data ownership and
working interactions. For an existing screen, do not invent observations about
an inaccessible screenshot or replace its identity from a reference alone.

Choose the few refinements that most improve comprehension or use:

| Symptom | Decision to examine |
|---|---|
| Everything attracts attention | Primary task, information hierarchy, restrained emphasis |
| Dense or oversized lists | Grouping, row rhythm, scanning and useful whitespace |
| Visually uneven controls | Optical alignment as well as measured bounds |
| Generic or overdecorated surfaces | Product purpose, meaningful grouping and brand language |
| Unclear action result | Pending, success, error and disabled feedback |

Use existing tokens and text styles first. A token change should solve a visible
or evidenced problem; do not normalize every gap just because a number differs.
Cards communicate grouping; gradients, shadows and large hero sections need a
product reason. Ask whether the same composition would still fit after swapping
the logo. Product specificity is more useful than a universal premium style.

## Bounded refinement loop

1. State the observed issue, intended improvement and smallest affected area.
2. Refine hierarchy, rhythm, alignment or feedback while preserving behavior.
3. Inspect the changed result when possible, including long/localized content,
   large text, relevant loading/error/empty states and narrow/wide constraints.
4. Stop when the stated issue is resolved and regressions are absent. If an
   unresolved blocker needs a broader redesign, report it rather than repeating
   an indefinite polish loop. Separate optional enhancements from blockers.

Example: on an account overview, make the balance the primary figure through an
existing heading style, keep transaction amounts easy to scan, and reduce visual
competition between row surfaces and the Transfer action. Compare the same
content before/after; do not add glowing cards to establish quality.

Motion observations can identify distraction or weak feedback; motion behavior
belongs to `crafting-flutter-motion` when available. Do not claim that skill ran
unless it did. Final evidence assessment belongs to `verifying-flutter-ui` when
available; otherwise assess it directly.

## Completion

Report the refinements and their user benefit, preserved behavior, and the
stopping condition. Name visual, runtime, accessibility, responsive and motion
checks actually performed. Mark unavailable checks NOT VERIFIED, including
accessibility when no relevant check was possible. A code-only refinement does
not establish rendered quality or release readiness.
