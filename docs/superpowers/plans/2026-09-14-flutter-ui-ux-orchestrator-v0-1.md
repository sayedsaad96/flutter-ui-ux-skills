# Flutter UI/UX Orchestrator v0.1 Implementation Plan

> Historical v0.1 scope. On 2026-10-24 the user explicitly requested completion
> of all eleven skills. The original scope constraints below describe that earlier
> plan; the current execution record is `2026-10-24-release-readiness.md`.

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the public `flutter-ui-ux-skills` repository foundation and ship the first verified skill, `flutter-ui-ux`, as a tested orchestrator that classifies Flutter UI/UX work, scopes it, uses available evidence, routes only the necessary capabilities, and reports verification honestly.

**Architecture:** This plan implements only the repository foundation plus the Layer-1 orchestrator. The orchestrator owns routing and coordination; it does not duplicate specialist design knowledge. Skill authoring follows RED → GREEN → REFACTOR: baseline agent behavior is captured before `skills/flutter-ui-ux/SKILL.md` exists, then the minimal skill is written from observed failures, pressure-tested, hardened, statically validated, documented, and released before any second skill is authored.

**Tech Stack:** Markdown Agent Skills, YAML frontmatter, Python 3 standard library for repository validation, `unittest` for validator tests, Git/GitHub, GitHub Actions, skills.sh-compatible repository layout.

**Spec:** `docs/superpowers/specs/2026-09-14-flutter-ui-ux-skill-system-design.md`

## Global Constraints

- The planned system contains 11 skills, but this plan creates only `flutter-ui-ux`.
- Do not create `polishing-flutter-experiences`, `verifying-flutter-ui`, or any other future skill in this plan.
- The orchestrator owns routing; it must not become a Flutter design encyclopedia.
- Primary modes are `CREATE`, `REDESIGN`, and `AUDIT`; intent outranks keywords.
- Complexity levels are `MICRO`, `SCREEN`, `FLOW`, and `PRODUCT`.
- Evidence levels are `E0` user description, `E1` requirements/PRD, `E2` Flutter codebase, `E3` screenshots/designs, `E4` runtime application, and `E5` multi-device/multi-state runtime.
- Use the minimum necessary capability set; do not invoke a full design workflow for a trivial change.
- Stronger available evidence must be inspected before guessing.
- AUDIT is read-only by default.
- CREATE and REDESIGN require verification by default, but the orchestrator must never claim checks that were not performed.
- No fake delegation: if a specialist skill is unavailable in the runtime, do not claim it was invoked.
- The visual philosophy is context-driven and evidence-first; the orchestrator must not impose a universal premium style.
- Do not force application-wide architecture, state management, dependency stacks, or design tools.
- Accessibility, RTL/localization, performance, state completeness, responsive/adaptive behavior, and motion are first-class concerns when relevant, but their detailed implementation belongs to specialist skills.
- No second skill is authored until `flutter-ui-ux` completes RED → GREEN → REFACTOR and the deployment checklist.

---

### Task 1: Bootstrap the Repository and Preserve the Approved Design (this commit)

- [x] **Step 1: Create the repository and directories** (done via GitHub API — create_repository)
- [x] **Step 2: Copy the approved spec and this plan into the repository** (this commit)
- [x] **Step 3: Add minimal repository metadata** (.gitignore, LICENSE, pyproject.toml committed)
- [x] **Step 4: Verify the repository is intentionally skill-empty** (no skills/ directory created yet)
- [x] **Step 5: Commit the foundation**

---

### Task 2: Define the Orchestrator Eval Contract Before Writing the Skill

Complete: six canonical prompts, isolated expectations and the routing rubric exist.

### Task 3: Run RED Baselines Without the Skill

Complete historically: the September clean run captured six failing controls.
Earlier contaminated records remain explicitly non-gating history.

### Task 4: Write the Minimal `flutter-ui-ux` Skill From Observed Failures

Complete: the orchestrator exists; the October confirmation corrected a PRODUCT
CREATE routing gap and added decision-owner routing for the full suite.

### Task 5: Run GREEN and REFACTOR Behavioral Evals

Complete for explicit use: the September final gate failed 3/6 on activation;
October explicit confirmation passes all six. Separate Codex discovery probes
pass three UI positives and one non-UI negative; Antigravity remains unverified.

### Task 6: Build a Static Skill Validator With TDD

Complete: metadata/reference validation and evidence integrity checks have
regression coverage. The current local suite contains 24 passing tests.

### Task 7: Add CI for Static Repository Gates

Complete: Windows/Ubuntu CI runs static tests, metadata/isolation/fingerprint
checks, the complete-suite release evidence gate and the placeholder scan.
Remote CI has not run for the unpushed candidate.

### Task 8: Publish v0.1 Documentation Without Overstating Capability

Complete locally: README, contributing guidance, changelog and release-readiness
report describe the complete 0.2.0rc1 candidate and its measured limitations.

### Task 9: Final Verification, Tagging, and Publication Gate

Local verification complete. Tagging, push and publication remain separate
maintainer actions; no v0.1.0 or v0.2.0 tag/release was created in this work.

---

## Plan Self-Review Checklist

- Every approved orchestrator requirement maps to an eval criterion or skill section.
- The RED baseline is committed before the skill file is created.
- No second skill is created in this plan.
- The orchestrator routes motion as a concern but does not duplicate `crafting-flutter-motion` expertise.
- AUDIT remains read-only by default.
- MICRO tasks are explicitly protected from over-processing.
- Product-scale tasks are explicitly protected from under-processing.
- Verification honesty and no-fake-delegation are release-gated.
- The repository can be installed from GitHub after publication.
