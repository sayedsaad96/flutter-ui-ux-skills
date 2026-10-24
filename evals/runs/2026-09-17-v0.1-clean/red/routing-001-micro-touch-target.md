---
scenario: routing-001-micro-touch-target.md
scenario_sha256: ad1390f0d5c7da35e8fb8996b85bb0c65964391171e90cd0d88c9b7b22b9954f
phase: RED
target_model: pro
target_runtime: Antigravity
subagent_id: 34a7dc45-73a0-4546-92fa-c346058106e1
timestamp: 2026-09-17T00:29:14Z
skill_loaded: false
declared_evidence:
  - Existing Flutter source code is available.
  - No screenshots or runtime are available.
  - No specialist skills are guaranteed to be installed.
actually_accessible_evidence:
  - Canonical scenario text supplied in prompt; no repository files accessed.
tools_available:
  - none
---

## Exact Response

To increase the usable touch target of the Settings icon button from 36×36 to 44×44 without increasing the visual size of the icon or altering the surrounding screen layout, you can adjust the hit-test and padding properties directly on the widget.

Here are the standard and recommended ways to do this in Flutter depending on how your icon button is implemented:

---

### Option 1: If using `IconButton` (Recommended)

In Flutter's Material library, `IconButton` separates the visual icon size (`iconSize`) from the tappable area (`constraints` / `padding`). By setting the button's minimum constraints to 44×44 and keeping the visual icon size at 36 (or its current visual dimension), you expand the touch target without changing the icon's visual scale.

```dart
IconButton(
  iconSize: 24.0, // Or whatever the visual icon size currently is (< 36)
  padding: const EdgeInsets.all(4.0), // Adjust padding to expand bounds
  constraints: const BoxConstraints(
    minWidth: 44.0,
    minHeight: 44.0,
  ),
  icon: const Icon(Icons.settings),
  onPressed: () {
    // Handle settings navigation/action
  },
)
```

> **Note on Material Tap Targets:** By default, standard Flutter `IconButton` widgets use `MaterialTapTargetSize.padded` (which targets 48×48). If your button was constrained down to 36×36, ensuring `constraints: BoxConstraints(minWidth: 44, minHeight: 44)` will enforce your required 44×44 boundary.

---

### Option 2: If using `GestureDetector` or `InkWell`

If the button is a custom widget (e.g., an `InkWell` or `GestureDetector` wrapping an `Icon`), wrap the icon with padding or use a constrained container with transparent padding so the hit area expands to 44×44 while the icon remains visually centered:

```dart
InkWell(
  borderRadius: BorderRadius.circular(22.0), // Optional: rounds ripple to match the 44x44 target
  onTap: () {
    // Handle settings navigation/action
  },
  child: const SizedBox(
    width: 44.0,
    height: 44.0,
    child: Center(
      child: Icon(
        Icons.settings,
        size: 24.0, // Visual icon remains untouched
      ),
    ),
  ),
)
```

Or using `GestureDetector` with `HitTestBehavior.opaque` to ensure transparent padded areas intercept taps:

```dart
GestureDetector(
  behavior: HitTestBehavior.opaque,
  onTap: () {
    // Handle settings navigation/action
  },
  child: Container(
    width: 44.0,
    height: 44.0,
    alignment: Alignment.center,
    child: const Icon(
      Icons.settings,
      size: 24.0, // Visual size
    ),
  ),
)
```

---

### Key Takeaways
- **Keep Visual Size Unchanged:** Do not change the `Icon(size: ...)` or asset size.
- **Enforce Touch Area:** Set the wrapping box/constraints to `44.0` width and height.
- **No Surrounding Changes:** Because the visual icon remains centered within the 44×44 bounds, the visual layout balance remains preserved without needing to redesign the parent layout.
