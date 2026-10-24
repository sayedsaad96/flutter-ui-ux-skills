---
name: designing-flutter-systems
description: Use when defining or evolving Flutter visual direction, theme tokens, typography, semantic colors, spacing, component language, or resolving design-system drift.
---

# Designing Flutter Systems

Own visual language and reusable design decisions. Derive identity from the
product and its users; a coherent system can be quiet, dense, expressive or
playful. No universal premium palette, font, radius or card style fits every app.

## Discover before defining

For an existing app, inventory ThemeData, ColorScheme, text styles, extensions,
local tokens and repeated components. Inspect representative consumers and
available visuals. Classify decisions as **KEEP / NORMALIZE / EXTEND / DEPRECATE**
with reasons. Preserve brand assets, approved reading fonts, semantic roles and
working components unless the task demonstrates a reason to change them.

For a new app, establish audience, domain, emotional goal, content density and
platform context, then choose a direction. Start with the minimum useful tokens
and one representative screen; extract components after patterns prove useful.
Do not build a speculative token/component catalog before content exists.

## Give tokens meaning

| System concern | Decision to make |
|---|---|
| Color | Role of content, surface, action, selection, status and error across themes |
| Typography | Reading vs interface roles, hierarchy, language coverage, scaling and fallback |
| Spacing | A deliberate rhythm with useful exceptions, not arbitrary normalization |
| Shape/elevation | Grouping and interaction hierarchy rather than universal card decoration |
| Components/icons | Proven anatomy, semantic states, variants and consistent visual weight |
| Motion personality | Product character; timing/behavior implementation belongs to motion work |

Use the existing Flutter theme as the first integration point. Add a custom token
only when a meaningful role cannot be expressed by the existing system. Avoid
parallel hardcoded colors, per-screen text scales or unnecessary theme wrappers.
Read the installed SDK and project conventions before choosing APIs.

Treat contrast, large text, Arabic/English coverage and light/dark states as
constraints. Do not assume a supplied brand color is readable on every surface.
A direction can be proposed without measurements; measured contrast and rendered
type quality cannot be claimed until checked.

## Migrate with a bounded blast radius

Map each drifted value to an existing role before adding a new one. Inspect
callers of shared tokens/components and migrate incrementally. Preserve state
APIs and interaction behavior; a theme cleanup is not an app architecture change.
Keep compatibility while callers migrate, and remove an old token only after its
remaining usages are addressed. A dependency must solve a real gap beyond the
SDK or installed packages.

Example: two new settings screens introduce a second action color and unrelated
spacing. Normalize them to the existing semantic roles and row pattern, retain
the established reading typography elsewhere, and inspect affected theme states.
Do not rebrand the whole app to match the new screens.

## Deliver

State the product-derived direction, token/component decisions, affected
consumers and migration order. Identify what stays and why. Report inspected
evidence separately from proposed values; visual, accessibility, platform and
runtime results remain NOT VERIFIED without actual checks. Spatial adaptation
and component engineering remain separate decision owners when needed.
