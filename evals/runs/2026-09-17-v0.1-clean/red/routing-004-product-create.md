---
scenario: routing-004-product-create.md
scenario_sha256: e83f4e679bf6f096acbfc5bacc6c7b37c50b64974800eca310fc6381b3ebe6b2
phase: RED
target_model: pro
target_runtime: Antigravity
subagent_id: 00c42759-066e-4b7a-b60e-1ff9b1caea0e
timestamp: 2026-09-17T00:29:30Z
skill_loaded: false
declared_evidence:
  - Product requirements only.
  - No existing code, screenshots, Figma, or runtime.
actually_accessible_evidence:
  - Canonical scenario text supplied in prompt.
tools_available:
  - none
---

## Exact Response

Here is a proposed UI/UX foundation for the Flutter learning app for children based on your requirements:

### 1. Theming & Visual Design (Playful but structured)
- **Colors**: Use a vibrant but limited primary palette (e.g., Soft Blue, Cheerful Yellow, Mint Green) with plenty of whitespace (or cream/off-white backgrounds) to avoid visual chaos. 
- **Typography**: Choose friendly, highly legible, rounded fonts that support both English and Arabic well (e.g., *Nunito* for English and *Cairo* or *Tajawal* for Arabic). 
- **Shapes**: Use heavily rounded corners for buttons and cards (e.g., `BorderRadius.circular(16)`) to give a soft, safe, and toy-like feel.

### 2. Localization & RTL/LTR Support
- **Setup**: Use `flutter_localizations` and the `intl` package.
- **Directionality**: Since Arabic is Right-to-Left (RTL) and English is Left-to-Right (LTR), rely on directional margins/padding (`EdgeInsets.directional`) instead of absolute (`EdgeInsets.only(left: ...)`). Flutter’s standard widgets (like `Row`, `ListView`) will automatically mirror themselves.
- **Toggle**: Implement a locale switcher in the state management layer that dynamically updates the `MaterialApp`'s locale, forcing the UI to re-render in the correct direction instantly.

### 3. Responsive Layouts (Mobile, Tablet, Web)
- **Base constraints**: Wrap main screens in a `Center` or `Align` with a `ConstrainedBox` (e.g., max width of 800px) on the web and tablet so the UI doesn't stretch awkwardly.
- **Adaptive Grid**: Use `SliverGrid` or `Wrap` for content (like learning modules) that adjusts the number of columns based on `MediaQuery.sizeOf(context).width` or using `LayoutBuilder`.
- **Navigation**: Use a bottom navigation bar for mobile, but dynamically switch to a `NavigationRail` or a side drawer on tablets and web for better space utilization.

### 4. Animation & Feedback (Feeling alive)
- **Micro-interactions**: Use `AnimatedContainer`, `AnimatedScale`, or `InkWell` (with customized splash colors) for buttons to give immediate tactile feedback when tapped.
- **Progress & Success**: Integrate **Rive** or **Lottie** for complex, delightful animations (e.g., a character jumping when a level is completed, or confetti explosions).
- **Transitions**: Use the `animations` package (e.g., `SharedAxisTransition`, `FadeThroughTransition`) to make navigating between screens feel fluid and spatial rather than jarring.

### Recommended Package Stack
- `flutter_localizations` & `intl` (Localization)
- `rive` or `lottie` (Complex animations)
- `animations` (Pre-built beautiful transitions)
- `flutter_animate` (For chaining simple UI entry/exit animations easily)
- `go_router` (For responsive navigation and deep-linking on web)
- `provider` or `riverpod` (For state management)
