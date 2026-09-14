---
name: flutter-ui-ux
description: Use when working on a Flutter interface where the task may involve creating, redesigning, auditing, adapting, animating, polishing, or verifying UI/UX.
---

# Flutter UI/UX

## Overview

This skill coordinates Flutter UI/UX work. It classifies the task, checks available evidence, routes only the necessary capabilities, and reports what was actually verified. It does not teach detailed typography, animation APIs, accessibility implementation, or responsive code — those decisions belong to specialist skills when present, or to careful direct implementation when they are not.

## Entry Contract

Before substantial UI work, classify: mode, complexity, available evidence, target platforms, and available verification. Do not skip this classification because a request "sounds simple" or because the user asks you to move fast.

## Mode Classification

- **CREATE** — new screens, flows, apps, or component families.
- **REDESIGN** — improving an existing UI.
- **AUDIT** — read-only evaluation; do not change code unless implementation is explicitly requested.
- Composite sequences are allowed: `AUDIT → REDESIGN → VERIFY`, `CREATE → review/polish → VERIFY`.

## Complexity Classification

- **MICRO** — small defect or refinement.
- **SCREEN** — single screen or component family.
- **FLOW** — multi-screen feature or navigation flow.
- **PRODUCT** — new application, broad redesign, or full audit.

Process expands only as the problem expands. A MICRO fix does not need a design-system exploration; a PRODUCT-scale CREATE does not get widget code before product/audience context and a design direction exist.

## Evidence Ladder

E0 user description, E1 requirements/PRD, E2 Flutter codebase, E3 screenshots/designs, E4 runtime application, E5 multi-device/multi-state runtime. If stronger evidence is available and actually accessible, inspect it before proposing a change — even for small fixes, even under time pressure, even when the user says not to bother. If evidence is described as available but is not actually attached or accessible in the current runtime, say what must be inspected instead of pretending to have inspected it.

## Routing Ownership

This skill owns routing, not specialist knowledge. Name only the capabilities the task's decisions actually require. If a specialist skill is not available in the runtime, do not claim it was invoked — do the necessary reasoning directly and say so.

## Minimum Necessary Capability Set

Route by decision ownership (what kind of decision does this task require?), not by keyword matching. Do not load a full design workflow for a trivial change, and do not shortcut a product-scale task into a quick code patch.

## Composite Workflows

- `AUDIT → REDESIGN → VERIFY`: diagnose and present findings before changing anything; fix only after diagnosis is stated; verify only what tooling/evidence actually allows.
- `CREATE → review/polish → VERIFY`: establish direction and states before implementation; polish after a working version exists; verify honestly at the end.

## Verification Contract

State plainly what was and was not verified. If runtime is unavailable, runtime remains unverified — say so instead of implying it works. Never assert an outcome ("works well on tablet," "tested with users," "works across platforms") that was not actually checked. Partial platform coverage (e.g., Android only) must be disclosed, not smoothed over.

## Mode-Specific Output Contract

- **CREATE:** what's being built and for whom, chosen direction and why, states/interactions, what was implemented, what was verified, remaining risks.
- **REDESIGN:** what currently exists (from inspection), diagnosis, KEEP/REFINE/REPLACE/REMOVE/INTRODUCE, changes made, before/after reasoning, verification evidence.
- **AUDIT:** executive verdict, findings by Critical/High/Medium/Low with problem/evidence/impact/recommendation, and explicit `NOT VERIFIED` marks for anything not actually checked. Stay read-only unless changes are explicitly requested.

## Common Routing Failures

Guard against these recurring failure modes:

- Proposing a fix or redesign directly from the prompt when existing code or a screenshot is actually accessible and unexamined.
- Claiming to have inspected code, screenshots, runtime, or devices that are merely described as available but were not actually accessible.
- Asserting an outcome ("looks great on tablet," "tested with kids," "works across platforms") with no verification behind it.
- Sliding from AUDIT into unrequested implementation when the user asked for read-only findings.
- Jumping straight to widget code on a PRODUCT-scale CREATE task without first establishing audience and design direction.
- Abandoning evidence inspection because the user applied time pressure or said "don't bother checking."

## Red Flags

- Claiming a specialist skill or tool ran when it did not (no fake delegation).
- Claiming verification (visual, runtime, accessibility, platform, motion) that did not actually happen.
- Claiming evidence was inspected when it was not actually accessible.
- Redesigning an inspectable existing UI from the prompt alone.
- Turning a read-only AUDIT into implementation without the user asking.
- Full design-system ceremony for a MICRO task, or jumping to code for a PRODUCT task with no design direction.

## Quick Reference

| Task shape | Mode | Complexity | Evidence to check first |
|---|---|---|---|
| "Fix this one small thing" | REDESIGN | MICRO | Existing code, if accessible |
| "Redesign this screen" | REDESIGN | SCREEN | Code + screenshot, if accessible |
| "Review/audit, don't change code" | AUDIT | SCREEN–PRODUCT | Code + runtime if available and accessible |
| "Build a new app/feature" | CREATE | FLOW–PRODUCT | Requirements/PRD |
| "Review then fix" | AUDIT → REDESIGN → VERIFY | FLOW | Code + runtime + screenshots |
| "Copy this reference, skip inspection" | REDESIGN | matches requested scope | Reference as evidence, not template — still inspect the project when accessible |
