---
scenario: routing-004-product-create.md
scenario_sha256: e83f4e679bf6f096acbfc5bacc6c7b37c50b64974800eca310fc6381b3ebe6b2
phase: GREEN
target_model: pro
target_runtime: Antigravity
subagent_id: 12bd1457-90d6-4f73-9584-cf15555e61a3
timestamp: 2026-09-17T00:34:27Z
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

Here is the proposed UI/UX foundation strategy for the new cross-platform Flutter learning app for children:

1. **Responsive & Adaptive Design (Mobile, Tablet, Web)**
   - Use `LayoutBuilder` and breakpoints to adapt the UI for different screen sizes. Mobile devices will have simplified, vertical-scrolling layouts, while tablets and web will utilize multi-column grids or side navigation to make use of the extra screen real estate.
   - Use responsive typography and scaling padding to maintain readability and touch targets.

2. **Playful & Structured UI/UX**
   - **Color Palette & Shapes**: Soft, inviting background colors paired with vibrant, high-contrast primary colors for actionable items. Utilize rounded corners (`BorderRadius.circular`) and bubbly shapes.
   - **Cognitive Load**: Keep screens uncluttered to avoid chaos. Focus on one primary action or learning objective per screen to maintain a structured flow.

3. **Localization (Arabic & English) & Bi-directional Support**
   - Implement `flutter_localizations` and the `intl` package.
   - Ensure full RTL (Right-to-Left) support for Arabic. Flutter automatically handles mirroring for most standard widgets, but custom icons and directional animations will need explicit `Directionality` handling.

4. **Animations for Feedback & Progress**
   - Use implicit animations (like `AnimatedContainer`, `AnimatedOpacity`) for state changes.
   - Use packages like `flutter_animate` for playful entrance animations or `Rive` / `Lottie` for complex, interactive character animations.
   - Reward progress with micro-interactions (e.g., a bouncing star or confetti effect when completing a task).

Please let me know if you would like me to begin implementing the project structure, localization setup, or a specific UI prototype based on these principles.
