Mode: CREATE
Complexity: PRODUCT
Evidence: Product requirements are available; no Flutter codebase, designs, screenshots, or runtime are accessible.
Capabilities: Product workflow, visual system, responsive/adaptive layout, Arabic/English inclusion, motion, Flutter UI engineering, polish, and verification.
Verification: NOT VERIFIED — no implementation or runtime is available to inspect.

## Foundation direction

Build for children using short, encouraging learning sessions. Since no age range or lesson format is specified, treat these as assumptions to confirm before detailed screen design.

Use a playful, calm visual system: warm colors, rounded shapes, friendly illustrations, clear hierarchy, and restrained decoration. Keep lessons focused, with one primary action per screen and progress visible without making mistakes feel punitive.

Plan the foundation around:

- **Core states:** onboarding and language choice, lesson selection, lesson in progress, correct and incorrect answers, pause/resume, completion, and empty or offline states.
- **Arabic and English:** support RTL and LTR layouts from the start, allow text expansion, and ensure icons and navigation direction adapt to the selected language.
- **Devices:** use compact navigation and focused lesson layouts on phones; give tablets and web more room for structured navigation and content without simply stretching phone screens.
- **Motion:** use brief, purposeful transitions for progress and feedback. Keep essential information available without animation and respect reduced-motion settings.

The current work is a product-level direction only; no screens or code have been implemented. The next step is to confirm the children’s age range, learning activities, and any brand constraints, then inspect the Flutter project and build the shared tokens, components, and first flow.

Verification remains NOT VERIFIED for Android, iOS, tablets, and web because no project or running app was provided.
