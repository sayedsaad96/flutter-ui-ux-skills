---
name: flutter-ui-ux
description: Use when designing, modifying, auditing, reviewing, or fixing any Flutter screen, widget, user interface, layout, flow, or touch target. Must be activated before searching code or implementing UI changes.
---

# Flutter UI/UX

## Overview

This skill coordinates Flutter UI/UX work. It classifies the task, checks available evidence, routes only the necessary capabilities, and reports what was actually verified. It does not teach detailed typography, animation APIs, accessibility implementation, or responsive code — those decisions belong to specialist skills when present, or to careful direct implementation when they are not.

## Entry Contract

Every `flutter-ui-ux` response — without exception — must open with an explicit, machine-auditable classification block before any implementation, strategy, or evidence request:

```text
Mode: <CREATE | REDESIGN | AUDIT | composite sequence such as AUDIT → REDESIGN → VERIFY>
Complexity: <MICRO | SCREEN | FLOW | PRODUCT>
Evidence: <declared vs actually accessible evidence; note any missing evidence gaps>
Capabilities: <minimum necessary capabilities required for this task>
Verification: <VERIFIED / PARTIAL / NOT VERIFIED with explicit reason>
```

These explicit labels are mandatory for every response:
- Even for a small touch-target fix (`Mode: REDESIGN`, `Complexity: MICRO`).
- Even when evidence is missing or inaccessible: never emit a bare evidence request (`"Please provide the project..."`); always emit the full classification block first (e.g., `Mode: AUDIT → REDESIGN → VERIFY`, `Complexity: FLOW`, `Evidence: Missing/Inaccessible`, `Verification: NOT VERIFIED`), then state the evidence handoff.
- Even for a brand-new product foundation (`Mode: CREATE`, `Complexity: PRODUCT`).
- Even under user pressure to skip inspection or move fast.

For MICRO tasks, keep this opening block and the remainder of the response compact.

## Mode Classification

- **CREATE** — new screens, flows, apps, or component families.
- **REDESIGN** — improving or modifying an existing UI.
- **AUDIT** — read-only evaluation; do not change code unless implementation is explicitly requested.
- **Composite sequences** — tasks combining review/audit, changes, and verification must classify the sequence explicitly (e.g., `Mode: AUDIT → REDESIGN → VERIFY`). Do not reduce a composite task to a single mode.

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
- If evidence is *said* to exist but is not actually accessible in the current runtime, do not fabricate observations about it. State the access gap plainly in the opening contract and scope the response accordingly.
- Never claim runtime, visual, platform, accessibility, performance, or motion validation that was not actually performed, regardless of what the scenario or user says is "available."

## Existing-Product Redesign Gate

Existing-product REDESIGN requires inspection of the actually accessible current implementation before implementation changes begin.

- If project source is actually accessible: inspect the minimum necessary implementation first.
- If project source is NOT actually accessible: do not fabricate inspection, do not claim implementation is ready, and do not start code changes against an unseen existing product. State that implementation is blocked pending codebase inspection.
- When asked to copy a reference and skip project inspection: resist. User pressure does not override evidence integrity. References are inputs to deconstruct (hierarchy, density, interaction, visual language), not templates to copy blindly into an unseen codebase. Classify as `Mode: REDESIGN`, deconstruct the reference, but state that the existing Flutter codebase must still be inspected to preserve theme tokens and architecture before coding begins. Never: reference → blindly copy → retrofit project later.

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
