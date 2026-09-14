# Flutter UI/UX Skill System — Design Specification

**Date:** 2026-09-14  
**Status:** Approved by user; implementation planning authorized  
**Working repository name:** `flutter-ui-ux-skills`  
**Primary positioning:** A design-engineering skill system for Flutter agents that produces product-specific, adaptive, production-ready interfaces that feel **designed, not generated**.

---

## 1. Product Vision

The project is an open-source, GitHub-hosted suite of Agent Skills for designing, redesigning, auditing, implementing, polishing, animating, and verifying Flutter UI/UX.

The system is intended for AI coding agents working on Flutter applications across Android, iOS, tablets, foldables, web, and desktop. It must improve the quality of agent-produced interfaces without imposing a single visual style or forcing a specific application architecture.

The defining product promise is:

> **Make Flutter interfaces feel intentionally designed for their product, not assembled from generic AI patterns.**

The system must help agents produce interfaces that are visually distinctive, context-aware, responsive, adaptive, inclusive, maintainable, performant, state-complete, platform-appropriate, and visually verified whenever evidence and tooling allow.

---

## 2. Goals

The skill system must:

1. Support three primary modes: **CREATE**, **REDESIGN**, and **AUDIT**.
2. Infer the correct mode automatically from user intent and project state.
3. Understand available evidence before making design decisions.
4. Derive visual language from the product rather than imposing a house style.
5. Prevent generic AI-generated UI patterns through explicit quality checks.
6. Preserve existing application architecture unless change is justified by the task.
7. Support Flutter across mobile, tablet, foldable, web, and desktop targets.
8. Treat responsive and adaptive behavior as different concerns.
9. Treat accessibility, localization, RTL, dynamic text, and input modes as design constraints.
10. Treat UI performance as part of user experience.
11. Treat loading, empty, error, offline, partial, permission, and other relevant states as first-class UX.
12. Treat animation and motion as a purposeful UX system rather than decorative polish.
13. Use visual/runtime evidence when available and never claim verification that was not performed.
14. Scale process depth to task complexity.
15. Remain tool-agnostic and runtime-adaptive.
16. Be suitable for public distribution through GitHub and skills ecosystems such as skills.sh.
17. Be testable with repeatable behavioral evals, not just reviewed as prose.

---

## 3. Non-Goals

The system will not:

- Force Clean Architecture, BLoC, Cubit, Riverpod, Provider, MVVM, or any other app-wide architecture.
- Impose a universal “premium” visual style.
- Add animations merely to make an app appear lively.
- Add dependencies when Flutter SDK or existing project dependencies already solve the problem cleanly.
- Rebuild working architecture or components because the skill prefers another implementation.
- Treat every UI task as a full design-system project.
- Require Figma, emulator access, screenshots, or a specific agent runtime.
- Pretend to have performed runtime, visual, platform, accessibility, or performance validation when those checks were not actually possible.
- Generate multiple design concepts when the decision is small and the exploration would add ceremony without value.

---

## 4. Core Design Principles

### 4.1 Context-Driven Design Intelligence

The skill system has no fixed visual style. The visual language must be derived from:

`product → audience → domain → brand → emotional goal → usage context → content density → platform expectations`

A fintech app, children’s learning app, Quran app, productivity tool, and B2B dashboard must not converge on the same generic visual DNA merely because the same agent or skill suite created them.

Core rule:

> **Never impose a house style on the product. Derive the visual language from the product.**

### 4.2 Evidence-First Product Understanding

When available, stronger evidence must be inspected before guessing.

Evidence sources may include:

- User intent and requirements
- PRD or product documentation
- Existing Flutter codebase
- Existing theme/design system
- Screenshots
- Figma or other design files
- Runtime UI
- Multi-device or multi-state runtime evidence

Core rule:

> **Never redesign an existing Flutter experience from the prompt alone when the implementation can be inspected.**

### 4.3 Adaptive Design Gate

The amount of design reasoning must scale with task size.

- **Micro refinement:** inspect → establish intent → implement → verify
- **Single screen:** inspect → diagnose → choose direction → define hierarchy/components → implement → verify
- **Feature flow:** understand → UX flow → design direction → states → responsive/adaptive strategy → implementation → verify
- **Product-scale work:** understand → design foundations → system → information architecture → key experience language → incremental implementation → continuous verification

Core rule:

> **Never code the visual solution before understanding the design problem, but never create more design ceremony than the task requires.**

### 4.4 Architecture-Aware, Architecture-Neutral

The system respects the architecture already used by the application.

It must preserve working boundaries, state management, navigation, domain layers, and project conventions unless the current task directly exposes a problem that must be addressed.

At the UI boundary it enforces:

- Focused widgets
- Clear responsibilities
- Reusable abstractions only after repetition is proven
- Theme/token-driven styling
- No business logic buried in presentation widgets
- Explicit state rendering
- Maintainable composition
- Testable UI behavior
- Minimal duplication
- Isolated platform-specific behavior

Core rule:

> **Respect the application architecture. Enforce quality at the UI boundary.**

### 4.5 Living Design System

A design system should emerge from product needs and become stricter as patterns prove themselves.

For existing projects:

`DISCOVER → EVALUATE → KEEP / NORMALIZE / EXTEND / DEPRECATE`

For new projects:

`visual direction → minimum viable tokens → initial screens → proven patterns → reusable components`

Core rule:

> **Build systems from proven patterns, not speculative abstractions.**

### 4.6 Inclusive by Construction

Accessibility, localization, RTL/LTR, dynamic text, contrast, input methods, focus, keyboard, reduced motion, and bidirectional content are product constraints, not post-production fixes.

Core rule:

> **Accessibility, RTL, and localization are design constraints—not post-production fixes.**

### 4.7 Performance by Construction

Performance is part of perceived quality.

The system should avoid unnecessary rebuilds, excessive blur, needless clipping, oversized image decoding, expensive decorative effects, poor list composition, layout workarounds, and animation choices that create jank.

Core rule:

> **Premium UI must look premium and feel fast, stable, and responsive.**

### 4.8 Adaptive Design Divergence

The amount of concept exploration scales with the design decision.

- Small refinement: one clear design intent
- Component redesign: compare likely patterns internally
- Important screen: explore 2–3 genuinely different directions
- Major feature/product: explore differences in hierarchy, navigation, density, interaction, rhythm, typography character, surface treatment, and motion personality

Core rule:

> **Do not confuse variation with exploration.**

### 4.9 Brand-Consistent, Platform-Adapted

The product identity remains coherent across platforms while interaction patterns adapt to platform conventions and device capabilities.

Core rule:

> **Adapt interaction patterns before adapting decoration.**

### 4.10 Dependency-Aware Minimalism

Dependencies are reused or added only when they materially improve reliability, accessibility, quality, or maintainability.

Decision order:

`existing dependency → Flutter SDK → justified new dependency`

Core rule:

> **A dependency must earn its place.**

### 4.11 State-Complete UX

A screen is a set of relevant states, not a single screenshot.

The system must identify only the states that can realistically occur, such as:

- Initial
- Loading
- Loaded
- Empty
- Error
- Offline
- Partial data
- Refreshing
- Disabled
- Permission denied
- First-use
- Edge cases

Core rule:

> **Design the state machine, not just the screenshot.**

### 4.12 Reference Deconstruction, Never Blind Imitation

References are analyzed for underlying design reasoning—hierarchy, density, navigation, typography, spacing, interaction, motion, and emotional character—rather than copied at the surface level.

Core rules:

> **Borrow reasoning, not appearance.**  
> **References are evidence, not templates.**

### 4.13 Tool-Agnostic, Visual-First When Valuable

The system uses the strongest evidence and tools available without depending on a specific runtime, Figma, emulator, or visual tool.

Core rule:

> **Use the strongest available evidence. Never confuse unavailable tooling with unavailable quality standards.**

### 4.14 Mode-Specific Adaptive Output

CREATE, REDESIGN, and AUDIT produce different output shapes. Output depth scales to task complexity.

The system must separate:

- Observed facts
- Design judgments
- Implemented changes
- Unverified assumptions

---

## 5. System Architecture

The approved architecture is a **Layered Skill System**.

### Layer 1 — Orchestrator

- `flutter-ui-ux`

### Layer 2 — Workflow Skills

- `creating-flutter-ui`
- `redesigning-flutter-ui`
- `auditing-flutter-ui`

### Layer 3 — Specialist Skills

- `designing-flutter-systems`
- `building-responsive-adaptive-flutter`
- `engineering-flutter-ui`
- `designing-inclusive-flutter`
- `crafting-flutter-motion`
- `polishing-flutter-experiences`
- `verifying-flutter-ui`

**Total planned skills: 11.**

Architectural rule:

> **A specialist owns one class of decisions. If two skills own the same decision, the boundary is wrong.**

---

## 6. Skill Responsibilities

### 6.1 `flutter-ui-ux`

The orchestrator is the routing and coordination brain, not a design encyclopedia.

Responsibilities:

- Detect CREATE / REDESIGN / AUDIT intent
- Determine task size
- Assess available evidence
- Detect target platforms
- Inspect existing architecture when available
- Determine available tooling and verification depth
- Select workflow and specialist skills
- Enforce system-wide principles
- Require truthful completion reporting

### 6.2 `creating-flutter-ui`

Use for new screens, new feature flows, new applications, and new component families.

Owns the CREATE workflow:

`understand → structure → explore when justified → choose direction → define states/interactions → coordinate specialist concerns → implement → verify`

### 6.3 `redesigning-flutter-ui`

Use for improving an existing UI.

Owns:

`OBSERVE → DIAGNOSE → KEEP / REFINE / REPLACE / REMOVE / INTRODUCE → REDESIGN → INTEGRATE → VERIFY`

Core rule:

> **Never redesign what you have not inspected when inspection is possible.**

### 6.4 `auditing-flutter-ui`

Read-only by default.

Owns:

- Evidence inspection
- Finding UI/UX defects
- Separating fact from judgment
- Assessing user impact
- Prioritizing Critical / High / Medium / Low
- Recommending direction

It must not silently turn an audit into implementation.

### 6.5 `designing-flutter-systems`

Owns visual system decisions:

- Visual direction
- Design tokens
- Color semantics
- Typography
- Spacing rhythm
- Shape language
- Elevation
- Component language
- Icon strategy
- Motion personality definition
- Design-system drift detection

### 6.6 `building-responsive-adaptive-flutter`

Owns spatial and platform adaptation:

- Phone
- Tablet
- Foldable
- Web
- Desktop
- Breakpoints
- Layout transitions
- Navigation adaptation
- Density changes
- Master-detail layouts
- Window resizing
- Pointer vs touch concerns
- Platform interaction expectations

Core rule:

> **Responsive is not the same as adaptive.**

### 6.7 `engineering-flutter-ui`

Owns clean Flutter implementation:

- Widget composition
- Component boundaries
- Theme usage
- State rendering
- Maintainable UI code
- Dependency decisions
- Performance-aware implementation
- Avoiding giant widgets
- Avoiding speculative abstractions

### 6.8 `designing-inclusive-flutter`

Owns inclusive design concerns:

- Accessibility
- RTL/LTR
- Localization
- Text scaling
- Contrast
- Semantics
- Focus
- Keyboard
- Touch targets
- Reduced motion requirements
- Bidirectional content
- Dynamic content resilience

### 6.9 `crafting-flutter-motion`

Owns motion and animation intent, hierarchy, behavior, and motion-system decisions.

It answers:

- What should move?
- Why should it move?
- When should it move?
- How should it move?
- How much motion is appropriate?

It covers:

1. Microinteractions
2. State transitions
3. Navigation motion
4. Spatial transitions
5. Feedback and achievement motion
6. Brand/expressive motion

Motion priority hierarchy:

`functional → feedback → navigational → expressive → decorative`

Core rules:

> **Motion must communicate change, causality, hierarchy, feedback, or personality.**  
> **There is no universal premium animation style. Motion personality must come from the product.**  
> **A beautiful animation that drops frames is a UX defect.**

Motion must adapt to product context. Examples:

- Fintech: restrained, precise, short
- Children’s learning: expressive, rewarding, playful
- Quran/reading: calm, gentle, low-distraction
- Productivity: fast, functional, nearly invisible
- Social/gaming: richer expressive feedback where justified

The skill must distinguish when to use:

- Implicit animations
- Explicit animations
- Shared-element/spatial continuity
- Animated list/state transitions
- Custom motion
- External animation tooling such as Rive/Lottie only when justified

It must apply Dependency-Aware Minimalism and Performance by Construction.

### 6.10 `polishing-flutter-experiences`

Owns refinement and perceived craft:

- Visual hierarchy
- Composition
- Optical alignment
- Spacing refinement
- Content density
- Motion-related craft observations; motion behavior decisions remain owned by `crafting-flutter-motion`
- Microinteraction refinement
- Feedback quality
- Product personality
- Anti-AI design smell correction

### 6.11 `verifying-flutter-ui`

Owns the quality gate:

`static correctness → runtime behavior → visual inspection → responsive/adaptive → state coverage → accessibility sanity → performance sanity → motion inspection → anti-AI quality → verification confidence`

Core rule:

> **Never claim validation that was not performed.**

---

## 7. Orchestration Protocol

The orchestrator follows:

`user request → classify → size → assess evidence → select workflow → select required specialists only → execute → verify → report confidence`

### 7.1 Mode Detection

Primary modes:

- CREATE
- REDESIGN
- AUDIT

Intent outranks keywords.

Composite workflows are allowed, including:

- `AUDIT → REDESIGN → VERIFY`
- `CREATE → AUDIT RESULT → POLISH → VERIFY`

### 7.2 Task Complexity

- **Level 1 — MICRO:** small defect or refinement
- **Level 2 — SCREEN:** single screen or component family
- **Level 3 — FLOW:** multi-screen feature or navigation flow
- **Level 4 — PRODUCT:** new application, broad redesign, or full audit

The process expands only as the problem expands.

### 7.3 Evidence Ladder

- **E0:** user description only
- **E1:** requirements / PRD
- **E2:** Flutter codebase
- **E3:** screenshots / visual designs
- **E4:** runtime application
- **E5:** multi-device / multi-state runtime

If higher evidence is available, use it before guessing.

### 7.4 Orchestration Rules

1. The orchestrator owns routing.
2. Workflow and specialist skills remain leaf capabilities where possible.
3. Use the minimum necessary skill set.
4. Route by decision ownership, not keyword matching.
5. CREATE and REDESIGN should end in verification by default.
6. AUDIT may remain read-only unless the user explicitly requests changes.
7. No fake delegation when the runtime cannot actually invoke other skills.
8. No indefinite polish loop.
9. Failures are classified as:
   - Blocking
   - Quality-impacting
   - Optional enhancement

---

## 8. Designed, Not Generated Quality Model

The primary differentiation of the project is a positive quality model, not merely a list of banned styles.

### 8.1 Six Quality Dimensions

1. **Product Specificity** — Does this UI belong to this product?
2. **Visual Intent** — Can major visual decisions be explained?
3. **Experience Coherence** — Do hierarchy, states, navigation, and interactions work together?
4. **System Coherence** — Do typography, spacing, components, and motion speak one language?
5. **Platform & Context Fit** — Does the experience fit device, input, language, and platform?
6. **Craft** — Does the implementation feel refined rather than assembled?

Core principle:

> **Distinctive because it is product-specific, not distinctive because it is decorative.**

Signature line:

> **Do not ask whether the interface looks good. Ask whether it looks inevitable for this product.**

### 8.2 Quality Verdicts

No fake numerical precision.

Each relevant dimension uses:

- `PASS`
- `PASS WITH CONCERNS`
- `FAIL`
- `NOT VERIFIED`

### 8.3 Design Smell Tests

The quality model includes:

- Logo-Swap Test
- Template-Smell Test
- Card-Abuse Test
- Generic-Hero Test
- Product-Specificity Test
- Decoration-Without-Purpose Test
- Pattern-Repetition Test
- Hierarchy-Clarity Test
- Reference-Distance Test
- State-Completeness Test
- Platform-Fit Test
- Responsive-Integrity Test
- Content-Stress Test

### 8.4 Motion Smell Tests

Motion quality includes:

- Purpose Test
- Competition Test
- Repetition Test
- Duration Test
- Continuity Test
- Personality Test
- Distraction Test
- Performance Test

### 8.5 Hard Failures vs Quality Smells

Hard failures block completion when relevant:

- Overflow
- Unreachable critical action
- Broken RTL
- Unreadable contrast
- Broken text scaling
- Missing critical state
- Target-platform interaction failure
- Severe motion/performance jank that harms use

Quality smells trigger refinement but do not automatically block completion:

- Too many cards
- Generic composition
- Weak personality
- Over-decoration
- Repetitive components
- Poor visual rhythm
- Excessive or purposeless animation

---

## 9. Visual and Motion Quality Loop

The implementation loop is:

`DESIGN → MOTION INTENT → IMPLEMENT → RUN → VISUAL INSPECTION → MOTION INSPECTION → INTERACTION INSPECTION → RESPONSIVE/ADAPTIVE INSPECTION → ACCESSIBILITY SANITY → PERFORMANCE SANITY → POLISH → VERIFY AGAIN`

If tooling is unavailable, perform the strongest available checks and mark unavailable checks as unverified.

Evidence confidence can be described in levels:

- Level 1 — code inspection
- Level 2 — static visual evidence
- Level 3 — runtime visual evidence
- Level 4 — multi-size / multi-state runtime evidence
- Level 5 — device/platform validation

---

## 10. Mode-Specific Output Contracts

### CREATE

Adaptive output should cover:

- What is being built and for whom
- Chosen design direction and why
- UX hierarchy, states, and interactions
- What was implemented
- What was verified
- Remaining risks/unverified areas

### REDESIGN

Adaptive output should cover:

- What currently exists
- Diagnosis
- KEEP / REFINE / REPLACE / REMOVE / INTRODUCE
- Changes made
- Before/after reasoning
- Verification evidence

### AUDIT

Read-only by default.

Output should prioritize:

- Executive verdict
- Critical / High / Medium / Low findings
- For each finding: problem, evidence, user impact, rationale, recommended direction
- Design-system drift
- Responsive/adaptive issues
- Accessibility issues
- Performance UX issues
- Motion issues
- Anti-AI findings
- Platform concerns
- Final priority order

---

## 11. Repository Architecture

Proposed repository:

```text
flutter-ui-ux-skills/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
│
├── skills/
│   ├── flutter-ui-ux/
│   ├── creating-flutter-ui/
│   ├── redesigning-flutter-ui/
│   ├── auditing-flutter-ui/
│   ├── designing-flutter-systems/
│   ├── building-responsive-adaptive-flutter/
│   ├── engineering-flutter-ui/
│   ├── designing-inclusive-flutter/
│   ├── crafting-flutter-motion/
│   ├── polishing-flutter-experiences/
│   └── verifying-flutter-ui/
│
├── shared/
│   └── references/
│       ├── designed-not-generated.md
│       ├── visual-quality.md
│       ├── design-smells.md
│       ├── motion-quality.md
│       ├── platform-conventions.md
│       ├── flutter-layout-patterns.md
│       ├── typography.md
│       ├── accessibility.md
│       ├── rtl-localization.md
│       ├── performance-ui.md
│       ├── design-tokens.md
│       └── responsive-adaptive.md
│
├── evals/
│   ├── scenarios/
│   ├── baselines/
│   ├── expectations/
│   └── README.md
│
├── scripts/
│   ├── validate-skills.*
│   └── check-links.*
│
└── .github/
    ├── workflows/
    ├── ISSUE_TEMPLATE/
    └── pull_request_template.md
```

Each skill follows the Agent Skill structure with `SKILL.md` as the required entry point and separate supporting/reference files only when useful.

---

## 12. Skill Authoring and Evaluation Strategy

Every skill is authored using RED → GREEN → REFACTOR.

### RED

Run realistic scenarios without the skill and record failure behavior and rationalizations.

### GREEN

Write the minimum skill guidance that corrects observed failures.

### REFACTOR

Find new loopholes, tighten language, and re-run scenarios until behavior is stable.

No batch creation of untested skills.

### Eval Categories

1. Recognition evals
2. Routing evals
3. Application evals
4. Pressure evals
5. Regression evals

The suite must test both:

- **Under-processing:** agent skips necessary design reasoning
- **Over-processing:** agent invokes a full design workflow for trivial changes

Motion evals should specifically test whether agents:

- Add animation without purpose
- Over-animate common interactions
- Use the same motion pattern everywhere
- Ignore reduced-motion needs
- Introduce avoidable jank
- Use motion appropriately to explain state or spatial change

---

## 13. CI and Repository Quality Gates

Repository checks should eventually validate:

- Valid `SKILL.md`
- Valid YAML frontmatter
- Unique skill names
- Discovery-oriented descriptions
- Existing referenced files
- No broken internal links
- No circular skill ownership
- Reasonable skill file size
- Eval coverage for behavioral changes

Not all behavioral evals need to be automated in the first release, but the repository structure must support progressive automation.

---

## 14. Versioning and Release Strategy

Use semantic versioning for the suite.

- `0.x` — architecture and behavior still evolving
- `1.0.0` — skill boundaries and orchestration considered stable

### Phased Delivery

**Phase 1 — Foundation**

1. `flutter-ui-ux`
2. `polishing-flutter-experiences`
3. `verifying-flutter-ui`

Purpose: prove the core “Designed, Not Generated” value proposition.

**Phase 2 — Workflows**

4. `creating-flutter-ui`
5. `redesigning-flutter-ui`
6. `auditing-flutter-ui`

**Phase 3 — Specialist Depth**

7. `designing-flutter-systems`
8. `building-responsive-adaptive-flutter`
9. `engineering-flutter-ui`
10. `designing-inclusive-flutter`
11. `crafting-flutter-motion`

Each skill is completed and verified before work begins on the next.

---

## 15. Public Positioning

Recommended core positioning:

> **A design-engineering skill system for Flutter agents that produces product-specific, adaptive, production-ready interfaces that feel designed—not generated.**

Recommended README opening concept:

> AI can write Flutter UI quickly. The harder problem is making that UI intentional, product-specific, adaptive, accessible, maintainable, fast, state-complete, and visually convincing. This project teaches agents how.

Primary product verbs:

- CREATE
- REDESIGN
- AUDIT
- ADAPT
- ANIMATE
- POLISH
- VERIFY

---

## 16. Acceptance Criteria for the System Design

The design is considered internally consistent when:

1. Every skill has a distinct decision domain.
2. The orchestrator owns routing and does not duplicate specialist knowledge.
3. CREATE, REDESIGN, and AUDIT have different workflow semantics.
4. Motion has a dedicated owner and is not reduced to decoration.
5. Responsive and adaptive concerns are explicitly separated.
6. Inclusive design, performance, state completeness, and verification are first-class concerns.
7. The system does not force a visual style, app architecture, dependency stack, or design tool.
8. “Designed, Not Generated” is expressed through repeatable quality tests rather than taste alone.
9. Verification is evidence-based and can report `NOT VERIFIED` honestly.
10. The authoring process requires behavioral evals before a skill is considered complete.
11. The repository can grow incrementally without changing the architectural model.
12. There are no unresolved design decisions required before implementation planning.

---

## 17. Final Design Decision

The approved product is a **hybrid, layered, evidence-first Flutter UI/UX skill system** with one orchestrator, three workflow skills, seven specialist skills, an explicit motion specialist, on-demand shared references, behavioral evals, and evidence-based verification.

Its defining philosophy is:

> **Understand the product before styling it.**  
> **Design the experience before coding the appearance.**  
> **Adapt to the platform without losing the brand.**  
> **Animate with purpose.**  
> **Build systems from proven patterns.**  
> **Verify what users actually experience.**  
> **Make it feel designed, not generated.**
