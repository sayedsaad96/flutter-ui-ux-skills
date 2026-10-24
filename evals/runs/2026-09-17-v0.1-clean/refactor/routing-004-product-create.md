---
scenario: routing-004-product-create.md
scenario_sha256: e83f4e679bf6f096acbfc5bacc6c7b37c50b64974800eca310fc6381b3ebe6b2
phase: REFACTOR
target_model: pro
target_runtime: Antigravity
subagent_id: 3f6ac2b4-ee37-4023-85f4-c7728f9d758c
timestamp: 2026-09-17T00:59:17Z
skill_loaded: true
skill_path: skills/flutter-ui-ux
skill_loading_method: Antigravity workspace skill discovery via .agents/skills.json
declared_evidence:
  - Product requirements only.
  - No existing code, screenshots, Figma, or runtime.
actually_accessible_evidence:
  - Canonical scenario text supplied in prompt.
tools_available:
  - view_file
---

## Exact Response

Here is a comprehensive UI/UX foundation plan for the cross-platform Flutter children's learning app, tailored to your requirements:

### 1. Design System: "Playful but Structured"
*   **Colors:** Use a soft, neutral or pastel background (e.g., cream, soft mint, or pale sky blue) to avoid chaos and cognitive overload. Use vibrant, saturated accent colors (bright orange, sunny yellow, vivid teal) specifically for interactive elements (buttons, draggable items) and progress indicators.
*   **Typography:** Choose friendly, rounded, and highly legible typefaces.
    *   *English:* **Nunito** or **Quicksand**.
    *   *Arabic:* **Cairo** or **Tajawal**.
*   **Shapes & Depth:** Use large corner radii (e.g., `BorderRadius.circular(24)` or fully stadium-shaped buttons). Soft, diffuse drop shadows can provide tactile depth to interactive cards, making them look "pressable" to children.

### 2. Localization & RTL (Arabic & English)
*   **Architecture:** Use `flutter_localizations` alongside the `intl` package. Define string catalogs for both `en` and `ar`.
*   **Layout Logic:** Flutter handles RTL mirroring automatically, but the UI must be built using directional properties.
    *   *Crucial:* Always use `EdgeInsetsDirectional` (e.g., `.start`, `.end`) instead of standard `EdgeInsets.only(left, right)`.
    *   *Icons:* Use `Icon(..., textDirection: TextDirection.rtl)` or `auto_mirrored` icons where directional context matters (like navigation arrows).
    *   *Alignment:* Use `AlignmentDirectional` (e.g., `AlignmentDirectional.centerStart`) rather than `Alignment.centerLeft`.

### 3. Responsive & Adaptive Layouts (Mobile, Tablet, Web)
*   **Breakpoints:** Establish clear breakpoints using `LayoutBuilder`. For a learning app:
    *   *Mobile (Portrait):* Stacked cards, vertical scrolling, full-width buttons.
    *   *Tablet (Landscape) / Web:* Split-screen layouts (e.g., navigation/characters on the side, main learning canvas in the center), leveraging `Row`, `Expanded`, and `Flexible`.
    *   *Constraint limits:* Use `ConstrainedBox` with `maxWidth` on web to ensure the UI doesn't stretch infinitely on large monitors, maintaining the "card-like" bounded feel.
*   **Touch Targets:** Ensure all buttons have a minimum touch target of `64x64` logical pixels (larger than the standard 48x48) to accommodate children's developing motor skills.

### 4. Animation & "Alive" Feedback
*   **Implicit Animations:** For simple state changes (e.g., a card enlarging slightly when selected), use Flutter's built-in implicit animators like `AnimatedContainer`, `AnimatedScale`, and `AnimatedOpacity`. Keep durations short (200-300ms) with bouncy curves (e.g., `Curves.easeOutBack`).
*   **Progress Indicators:** Use `TweenAnimationBuilder` to animate progress bars filling up smoothly, rather than jumping instantly to the new value. Combine this with particle effects when a level is completed.
*   **Character & Celebration (Lottie/Rive):** Integrate the `lottie` or `rive` packages for complex, high-performance vector animations (e.g., a mascot character that cheers when the child gets a correct answer, or looks confused on an incorrect one).
*   **Haptics & Audio:** Accompany visual feedback with auditory chimes and `HapticFeedback.lightImpact()` (on mobile/tablet) to reinforce positive actions and provide a multi-sensory learning experience.
