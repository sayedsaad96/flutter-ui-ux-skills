---
name: engineering-flutter-ui
description: Use when implementing or refactoring Flutter widgets, rendering UI states, integrating theme and existing state management, or fixing presentation-layer rebuild, scrolling and performance problems.
---

# Engineering Flutter UI

Own maintainable presentation code. Respect the app's existing state, navigation,
domain and data boundaries; a UI improvement is not permission to replace them.

## Inspect ownership first

Read the affected widgets, their parent constraints, state owner, callbacks,
theme, dependencies and relevant tests. Identify who starts requests, owns
controllers, preserves input and renders errors. Reuse the existing owner before
introducing another async/state mechanism. Verify APIs against the installed SDK
and packages rather than assuming a preferred version or architecture.

Keep build methods a description of current UI. Start requests and subscriptions
at the existing event/lifecycle boundary, not on each rebuild. Preserve existing
cancellation, request ordering, authorization and persistence behavior. Do not
implement business rules or network effects in a widget to simplify its code.

## Compose for actual states

| Concern | Implementation decision |
|---|---|
| Widget boundaries | Extract a coherent responsibility or proven repeated component |
| State rendering | Explicit relevant initial/loading/data/empty/error/offline/partial/pending UI |
| Styling | Theme/token roles and existing component conventions |
| Ownership | Caller-owned resources stay with their caller; locally owned resources are disposed |
| Interaction | Stable callbacks, disabled/pending behavior, retry and input preservation |

Do not hide loading or errors behind an empty collection, replace a form on
transient failure, or recreate state owners during a layout change. Keep API
contracts stable while refactoring. Use stable item identity when ordering or
selection can change; do not reuse index identity for stateful reordered items.

## Avoid predictable expensive work

Use lazy list/grid/sliver construction for large data and give the scrollable
finite constraints through its parent layout. Nesting a shrink-wrapped large list
inside a `SingleChildScrollView` can defeat lazy behavior; it is not a general
fix for unbounded constraints. Compose a single scroll surface or a properly
bounded region instead. Decode images for their actual display needs and inspect
unnecessary rebuild scope, intrinsic layout, clipping, blur and offscreen effects.
Use profiling to establish a bottleneck before adding caches, repaint boundaries
or other speculative optimizations.

Example: a screen creates a network future in build while its existing state
owner already exposes search states. Remove the duplicate future, render those
states, and build results lazily within bounded layout. Preserve the existing
owner's request ordering rather than replacing it with another package.

## Verify and hand off

Run relevant project analysis/tests and inspect runtime behavior when available.
Choose checks that exercise the changed contract: repeated rebuilds, error/retry,
large result sets, selection, disposal or resizing as appropriate. Do not invent
performance measurements or call code-only reasoning runtime validation.

Report what changed, the ownership preserved, actual checks and limitations.
Separate maintainability improvements from behavior changes. New abstractions
and dependencies need a present user beyond saving a few lines. Detailed visual,
adaptive, inclusive and motion decisions remain their respective owners.
