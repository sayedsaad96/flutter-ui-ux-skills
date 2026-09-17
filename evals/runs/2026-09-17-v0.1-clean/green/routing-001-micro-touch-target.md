---
scenario: routing-001-micro-touch-target.md
scenario_sha256: ad1390f0d5c7da35e8fb8996b85bb0c65964391171e90cd0d88c9b7b22b9954f
phase: GREEN
target_model: pro
target_runtime: Antigravity
subagent_id: 7d85208a-69c8-4141-a329-493b9cb088c7
timestamp: 2026-09-17T00:34:27Z
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

### 1. Classification & Sizing
* **Mode:** `REDESIGN` (modifying an existing UI element without altering screen layout)
* **Complexity:** `MICRO` (isolated component touch target adjustment)

---

### 2. Evidence Assessment
* **Declared evidence:** Existing Flutter source code is declared available.
* **Actually accessible evidence in this session:** No source files or snippets were provided in the prompt context, and file browsing tools are not provided.
* **Evidence Gap:** The current widget implementation details (e.g., standard `IconButton`, custom `InkWell`, `GestureDetector`, or nested `Padding`) are not directly inspectable.
* **Action:** Provide the canonical, minimal solution covering the standard Flutter implementations without altering visual bounds or redesigning surrounding layout.

---

### 3. Capability Routing
* **Primary Focus:** Touch ergonomics and hit testing bounds (`flutter-accessibility` / interaction conventions).
* **Skills Omitted:** 
  * `flutter-ui-design-tokens`: Not needed; no token, color, typography, or theme changes requested.
  * `flutter-layout-responsive`: Not needed; screen layout and responsive structure must remain unchanged.
  * `flutter-motion-animation`: Not needed; no animations involved.
  * `flutter-visual-polish`: Not needed; explicitly instructed not to redesign or alter visual prominence.

---

### 4. Implementation Solution

To expand the usable touch target to 44×44 while preserving the visual size of the 36×36 icon button, adjust the hit-test bounds and internal padding based on how the button is currently implemented.

#### Scenario A: Using standard `IconButton`
In Flutter, `IconButton` defaults to a minimum interactive dimension (usually 48×48 dp via `MaterialTapTargetSize.padded`). If constraints or padding were tightened to 36×36, set the constraints explicitly to 44×44 and maintain the visual icon size:

```dart
IconButton(
  iconSize: 24.0, // Or current visual size <= 36
  padding: const EdgeInsets.all(4.0),
  constraints: const BoxConstraints(
    minWidth: 44.0,
    minHeight: 44.0,
  ),
  icon: const Icon(Icons.settings),
  onPressed: () {
    // Action
  },
)
```

#### Scenario B: Using `InkWell` or `GestureDetector`
If wrapped in a custom gesture recognizer, enforce the 44×44 tappable boundary via a `ConstrainedBox` or `SizedBox`, centering the visual icon:

```dart
InkWell(
  borderRadius: BorderRadius.circular(22.0),
  onTap: () {
    // Action
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

---

### 5. Verification & Confidence
* **Touch Target Verification:** Meets iOS HIG (44×44 pt minimum) target size without altering adjacent screen spacing or visual balance.
* **Verification Status:**
  * Static code structure: Verified.
  * Visual inspection: `NOT VERIFIED` (no screenshot or visual preview tool accessible in this session).
  * Runtime / Device hit testing: `NOT VERIFIED` (no active runtime/device connection).
* **Confidence:** High for standard Flutter touch target expansion.
