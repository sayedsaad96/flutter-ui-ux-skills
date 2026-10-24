---
name: redesigning-flutter-ui
description: Use when improving an existing Flutter screen, component or flow, including reference-led redesigns, UI fixes, and review-then-fix requests.
---

# Redesigning Flutter UI

Improve an existing experience from evidence of what it does today. Own the
redesign sequence, preserving working product behavior and app boundaries.

## Observe and diagnose

Inspect the accessible source, theme, navigation, state ownership and relevant
screens/runtime before proposing changes. A supplied excerpt is real evidence
for that excerpt; do not describe it as a review of the entire project. Mark
inaccessible references and runtime plainly. If no existing source is accessible,
provide a diagnosis scope/handoff rather than code against an invented app.

Separate observed problems from design judgments and assumptions. Tie each
proposed change to a user task, reading order, interaction, state, layout or
access need. A request for a modern/premium appearance is not evidence that
navigation, state management, fonts or the shared theme must be replaced.

## Choose a proportional intervention

| Disposition | Decision |
|---|---|
| KEEP | Working interactions, domain rules, proven tokens and components |
| REFINE | Hierarchy, spacing, labels, ergonomics or feedback that need adjustment |
| REPLACE | A pattern demonstrably unable to serve the current task |
| REMOVE | Redundant content, competing actions or decoration without purpose |
| INTRODUCE | A missing state, affordance or component required by the task |

Use only relevant dispositions; a micro fix can express them in one sentence.
State diagnosis before implementation in a review-then-fix request, then proceed
within the already-authorized scope. A read-only review belongs to
`auditing-flutter-ui`; do not silently turn it into changes.

Deconstruct references into hierarchy, density, content grouping and interaction
reasoning. Inspect available references and adapt what serves this product.
Under time pressure, reduce inspection to the affected widget and its boundaries;
do not substitute a reference for understanding an inspectable current app.

## Redesign and integrate

Implement the smallest coherent improvement using the existing theme,
callbacks, routes and state conventions. Preserve parent-owned loading/error
states and domain request ordering. Changing a shared token affects consumers;
inspect those consumers before a global change. Avoid a competing state owner
or app-wide migration for a row-level defect.

Example: refine an order list using existing text styles, directional padding
and a clearer status/action hierarchy while preserving its selection callback
and lazy list. Do not replace the app router to make the row look different.

## Verify and report

Compare the same content and states before/after when evidence allows. Check
changed hit areas, long/localized text, RTL, large text, constrained layouts and
critical actions proportionally. Name the checks actually performed and their
limits; static reasoning does not prove visual, runtime or accessibility quality.

Report current evidence, diagnosis, chosen dispositions, changes (or a clearly
labeled proposal), preserved behavior and verification. For an Android-only flow,
keep iOS explicitly NOT VERIFIED. Stop after the scoped problem is resolved and
relevant checks pass; separate broader suggestions from the delivered change.
