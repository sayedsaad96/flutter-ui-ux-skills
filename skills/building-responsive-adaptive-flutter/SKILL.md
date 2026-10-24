---
name: building-responsive-adaptive-flutter
description: Use when a Flutter interface must handle constrained panels, resizing, phones, tablets, foldables, web or desktop, including layout transitions, navigation adaptation and touch, pointer or keyboard input.
---

# Building Responsive and Adaptive Flutter

Own spatial and platform adaptation. Responsive layout fits content into available
space; adaptive behavior makes navigation and interaction useful in that space.
A wide window does not imply every nested panel is wide.

## Measure the actual region

Inspect the parent constraint chain and existing state/navigation ownership.
Use local `LayoutBuilder` constraints for a component or panel; use `MediaQuery`
for relevant window/environment data such as insets, display features and text
scaling. A breakpoint based on full-window width can overflow a split panel.
Handle unbounded constraints at their source instead of treating infinity as a
large desktop width or applying arbitrary fixed dimensions.

Derive transitions from minimum usable content widths, padding, density and
input needs. Choose a readable content maximum; do not stretch every phone
control to fill a desktop window. SDK examples can be starting points, not
universal breakpoints or evidence of fit.

| Available space/context | Adaptation to consider |
|---|---|
| Narrow content region | One pane, focused task, reachable compact navigation |
| Enough room for both panes | List/detail or supporting context without oversized content |
| Resizable window | Stable state and usable intermediate widths, not just endpoint screenshots |
| Fold/occlusion | Usable subregions and safe placement of content/actions |
| Keyboard, pointer or touch | Focus, shortcuts/activation, hover where useful, and touch ergonomics |

Device names or operating-system checks alone are not layout strategies. Keep
brand identity coherent while adapting interaction to actual platform conventions
and input capabilities. Consider safe areas, keyboards, text expansion and large
text alongside width; landscape is not automatically a two-pane layout.

## Preserve continuity

Keep selected items, forms, navigation state and asynchronous ownership outside
the presentation branch. Do not recreate a Cubit, reset a route or issue a fresh
request merely because constraints changed. Preserve scroll state deliberately
with stable widget identity and an appropriate controller/PageStorage strategy.
A controller alone is not proof an unmounted/reparented scrollable restores its
position. Avoid attaching one controller to conflicting simultaneous scrollables.
Dispose owned resources at the owning widget's lifecycle boundary.

Example: an account panel inside a wide workspace is only 420 logical pixels.
Show a focused list or detail there; expose both only when that panel has room.
Resize while an item is selected and the list is scrolled to verify continuity.

## Verify adaptation

Check representative narrow, wide and transition constraints, long/localized
content, large text, relevant insets, focus/keyboard interaction and state
preservation. Inspect fold behavior when display-feature evidence exists.
Use project widget/runtime tests where appropriate; do not claim phone, tablet,
foldable or desktop validation from code inspection alone.

Deliver the local constraints and transition rationale, changed interaction
patterns, state-preservation approach and actual results. Mark unavailable
runtime, device and input checks NOT VERIFIED.
