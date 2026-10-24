---
name: crafting-flutter-motion
description: Use when designing or fixing Flutter animations, microinteractions, state or navigation transitions, motion personality, reduced-motion behavior, or animation interruption and lifecycle problems.
---

# Crafting Flutter Motion

Own what moves, why, when and how. Prioritize functional continuity, feedback and
navigation before expression or decoration. Motion personality comes from the
product: calm reading, precise transactions and playful learning need different
behavior, not one universal premium spring.

## Define the transition contract

Inspect the current interaction, state owner, navigation and accessible motion
evidence. Identify the trigger, start/end state, user benefit, duration/curve
rationale, interruption behavior and reduced-motion result. Consider
microinteractions, state changes, navigation, spatial continuity, list changes and
achievement feedback only when the task needs them.

| Need | Start with |
|---|---|
| Simple value/appearance change | An SDK implicit animation tied to state |
| Coordinated or interactive sequence | An explicitly owned controller |
| Navigation/spatial continuity | Existing route/shared-element conventions |
| List or content replacement | Stable identity and understandable state transition |
| Rich authored animation | Existing asset tooling; add a dependency only for a demonstrated gap |

Timing should fit the distance, interaction frequency and reading/attention cost.
Avoid continuous movement, entrance replay on rebuild, animation on every list
item or feedback that delays the next action. A screenshot does not verify
timing, smoothness or interruption behavior.

## Integrate with lifecycle and state

Create controllers at their owning state/lifecycle boundary, update them from
meaningful transitions and dispose them when that owner ends. Do not create
controllers or call forward on every build. Handle rapid reversals, repeated
input, cancellation and leaving the screen. Keep widget/item identity stable.
Ticker suppression does not replace disposal or correct state ownership.

Animation presents application state; it must not become a competing owner of
reading position, selection, form contents, requests or playback. Essential state
changes must not depend on decorative completion callbacks that can be skipped
when interrupted. Preserve existing audio and navigation boundaries.

Respect both app reduced-motion preferences and platform animation-disable
settings. When either requests less motion, reduce or remove spatial movement
and present the meaningful final state promptly. Keep feedback understandable
through text, color/shape or semantics; do not replace one disabled effect with
another distracting one.

Example: a reading bookmark can change selected appearance immediately with a
small state transition when appropriate. Rebuilding or scrolling must not replay
an entrance, move reading content or restart audio. Celebration after every scroll
adds interruption without useful feedback.

## Verify proportionally

Inspect repeated/reversed transitions, route exit, disposal, reduced-motion
changes and preservation of selection/scroll/playback when relevant. Use runtime
inspection and profile evidence to assess jank; minimize expensive effects before
introducing speculative optimization. Stop after the intended communication is
clear and regressions are addressed.

Deliver the transition intent, chosen mechanism, interruption/reduced-motion
behavior and actual checks. Mark absent runtime, frame/device and accessibility
evidence NOT VERIFIED; never claim smoothness from code alone. Visual systems
define broad character; this skill owns concrete motion behavior.
