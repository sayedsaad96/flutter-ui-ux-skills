---
scenario: routing-001-micro-touch-target.md
scenario_sha256: ad1390f0d5c7da35e8fb8996b85bb0c65964391171e90cd0d88c9b7b22b9954f
phase: REFACTOR
target_model: pro
target_runtime: Antigravity
subagent_id: fdd96998-d742-4327-b07f-aa3d4bffa07b
timestamp: 2026-09-17T00:59:16Z
skill_loaded: true
skill_path: skills/flutter-ui-ux
skill_loading_method: Antigravity workspace skill discovery via .agents/skills.json
declared_evidence:
  - Existing Flutter source code is available.
  - No screenshots or runtime are available.
  - No specialist skills are guaranteed to be installed.
actually_accessible_evidence:
  - Canonical scenario text supplied in prompt; no source files accessed.
tools_available:
  - view_file
---

## Exact Response

To increase the usable touch target to 44x44 without making the icon visually huge, you can explicitly set the constraints of an `IconButton` or wrap the icon in a `SizedBox` with a gesture detector.

**Option 1: Using IconButton**
If you are using an `IconButton`, you can set the `constraints` property to enforce a 44x44 minimum touch area while keeping the `iconSize` small.

```dart
IconButton(
  icon: const Icon(Icons.settings),
  iconSize: 24, // Keeps the icon visually small
  constraints: const BoxConstraints(
    minWidth: 44,
    minHeight: 44,
  ),
  padding: EdgeInsets.zero, // Adjust or remove depending on desired padding
  onPressed: () {
    // Your settings action
  },
)
```

**Option 2: Using GestureDetector**
If you are using a standard `Icon` widget, wrap it in a `SizedBox` of 44x44 and use a `GestureDetector` with `HitTestBehavior.opaque` to ensure the entire empty area around the icon is tappable.

```dart
GestureDetector(
  behavior: HitTestBehavior.opaque, // Ensures the entire 44x44 area captures taps
  onTap: () {
    // Your settings action
  },
  child: const SizedBox(
    width: 44,
    height: 44,
    child: Center(
      child: Icon(
        Icons.settings,
        size: 24, // Keeps the icon visually small
      ),
    ),
  ),
)
```
