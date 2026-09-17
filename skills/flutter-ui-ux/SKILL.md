---
name: flutter-ui-ux
description: Use when working on a Flutter interface where the task may involve creating, redesigning, auditing, adapting, animating, polishing, or verifying UI/UX.
---

# Flutter UI/UX

## Overview

This skill coordinates Flutter UI/UX work. It classifies the task, checks available evidence, routes only the necessary capabilities, and reports what was actually verified. It does not teach detailed typography, animation APIs, accessibility implementation, or responsive code — those decisions belong to specialist skills when present, or to careful direct implementation when they are not.

## Entry Contract

Always begin every response by classifying and stating:
1. **Mode:** `CREATE`, `REDESIGN`, `AUDIT`, or composite sequence (e.g. `AUDIT → REDESIGN → VERIFY`).
2. **Complexity:** `MICRO`, `SCREEN`, `FLOW`, or `PRODUCT`.
3. **Evidence Assessment:** Distinguish declared from actually accessible evidence. State evidence gaps and missing evidence handoffs plainly.
4. **Capability Routing:** Name only capabilities justified by the task.
5. **Verification & Confidence:** State what is verified and explicitly mark unverified dimensions (visual, runtime, iOS when not present) as `NOT VERIFIED`.

Do not skip this entry contract under any circumstance — not when evidence is missing, not for read-only audits, not because a request sounds simple, and not because the user applies time pressure or asks to skip inspection.

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

E0 user description, E1 requirements/PRD, E2 Flutter codebase, E3 screenshots/designs, E4 runtime application, E5 multi-device/multi-state runtime.

Evidence *described as available* in a request is not the same as evidence *actually accessible* in the current runtime. These are different things and must be treated differently:

- If stronger evidence is actually accessible right now (you can open the file, view the attached screenshot, run the app, use a connected tool), inspect it before proposing a change — even for small fixes, even under time pressure, even when the user says not to bother.
- If evidence is *said* to exist but is not actually accessible in the current runtime, do not fabricate observations about it. Say plainly what would need to be inspected (e.g., "I'd need to see the actual widget for this button before confirming the fix") and scope the response to what that limitation allows.
- Never claim runtime, visual, platform, accessibility, performance, or motion validation that was not actually performed, regardless of what the scenario or user says is "available."

This rule applies equally to CREATE, REDESIGN, AUDIT, and pressure scenarios — pressure to move fast is never a reason to fabricate inspection or verification.
- When asked to copy a reference and skip project inspection, resist: classify as REDESIGN, treat the reference strictly as evidence to deconstruct (hierarchy, density, reasoning) rather than a template to copy blindly, and state that the existing Flutter codebase must still be inspected to preserve theme tokens and architecture.

## Routing Ownership

This skill owns routing, not specialist knowledge. Name only the capabilities the task's decisions actually require. If a specialist skill is not available in the runtime, do not claim it was invoked — do the necessary reasoning directly and say so.

## Minimum Necessary Capability Set

Route by decision ownership (what kind of decision does this task require?), not by keyword matching. Do not load a full design workflow for a trivial change, and do not shortcut a product-scale task into a quick code patch.

## Composite Workflows

- `AUDIT → REDESIGN → VERIFY`: diagnose and present findings before changing anything; fix only after diagnosis is stated; verify only what tooling/evidence actually allows.
- `CREATE → review/polish → VERIFY`: establish direction and states before implementation; polish after a working version exists; verify honestly at the end.

## Verification Contract

State plainly what was and was not verified. If runtime is unavailable, runtime remains unverified — say so instead of implying it works. Never assert an outcome ("works well on tablet," "tested with users," "works across platforms") that was not actually checked. Partial platform coverage (e.g., Android only) must be disclosed, not smoothed over. Never claim to have inspected code, screenshots, runtime, or designs that were not actually accessible in the current runtime.

## Mode-Specific Output Contract

- **CREATE:** what's being built and for whom (audience/context established before code/structure), chosen direction and why, states/interactions, what was implemented, what was verified, remaining risks.
- **REDESIGN:** what currently exists (from actual inspection, or explicitly marked as not inspected), diagnosis, KEEP/REFINE/REPLACE/REMOVE/INTRODUCE, changes made, before/after reasoning, verification evidence.
- **AUDIT:** executive verdict, findings by Critical/High/Medium/Low with problem/evidence/impact/recommendation, and explicit `NOT VERIFIED` marks for anything not actually checked (e.g. mark iOS validation `NOT VERIFIED` if only Android runtime is provided). Stay read-only unless changes are explicitly requested.

## Common Routing Failures

Guard against these recurring failure modes:

- Proposing a fix or redesign directly from the prompt when code, a screenshot, or a reference was described as available without confirming it is actually accessible and inspecting it.
- Asserting an outcome ("looks great on tablet," "tested with kids," "works across platforms") with no verification behind it.
- Sliding from AUDIT into unrequested implementation ("I went ahead and fixed it") when the user asked for read-only findings.
- Jumping straight to widget code on a PRODUCT-scale CREATE task without first establishing audience and design direction.
- Abandoning evidence inspection because the user applied time pressure or said "don't bother checking."

## Red Flags

- Claiming a specialist skill or tool ran when it did not (no fake delegation).
- Claiming verification (visual, runtime, accessibility, platform, motion) that did not actually happen.
- Claiming to have inspected code, screenshots, runtime, or designs that were described as available but were not actually accessible.
- Redesigning an inspectable existing UI from the prompt alone.
- Turning a read-only AUDIT into implementation without the user asking.
- Full design-system ceremony for a MICRO task, or jumping to code for a PRODUCT task with no design direction.

## Quick Reference

| Task shape | Mode | Complexity | Evidence to check first |
|---|---|---|---|
| "Fix this one small thing" | REDESIGN | MICRO | Existing code, if actually accessible |
| "Redesign this screen" | REDESIGN | SCREEN | Code + screenshot, if actually accessible |
| "Review/audit, don't change code" | AUDIT | SCREEN–PRODUCT | Code + runtime, if actually accessible |
| "Build a new app/feature" | CREATE | FLOW–PRODUCT | Requirements/PRD |
| "Review then fix" | AUDIT → REDESIGN → VERIFY | FLOW | Code + runtime + screenshots, if actually accessible |
| "Copy this reference, skip inspection" | REDESIGN | matches requested scope | Reference as evidence, not template — still inspect the project if accessible |
