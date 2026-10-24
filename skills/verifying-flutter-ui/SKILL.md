---
name: verifying-flutter-ui
description: Use when checking a Flutter UI change, assessing interface release readiness, reviewing verification evidence, or reporting which layouts, states, interactions, and platforms were actually validated.
---

# Verifying Flutter UI

Readiness is a claim supported by evidence for a stated scope. Green analysis or
unit tests do not establish rendered quality, accessible interactions or platform
coverage. A supplied log is reported evidence; distinguish it from checks you ran.

## Build the evidence ledger

For the changed screen/flow, record the target platforms, constraints, languages,
states and critical actions. Inspect accessible code and artifacts before choosing
checks. For each relevant check record **scope → method → observed result →
limitation**. Missing tooling reduces confidence, not the quality standard.

| Layer | Evidence that can support it |
|---|---|
| Static correctness | Project analysis and relevant widget/unit checks, with their results |
| Runtime behavior | Running the actual flow, including navigation, pending/error/retry and state preservation |
| Visual quality | Inspected renders with hierarchy, clipping, alignment, contrast and content stress |
| Responsive/adaptive | Named local constraints, resizing transitions, input modes and fold/keyboard insets |
| Inclusion | Large text, RTL/LTR, keyboard/focus, semantics and assistive-technology checks appropriate to the change |
| Performance/motion | Profile evidence on relevant hardware, interrupted/repeated transitions and reduced motion |

Choose the smallest set of checks that resolves the actual risk. A target-size
fix needs geometry, hit behavior and unchanged icon size; it does not require a
whole-product design audit. A cross-platform checkout needs more than a loaded
Android screenshot. Reuse project test commands; inspect their scope and results
rather than treating their names as proof. Do not update goldens just to bless a
regression, or report an unexecuted command as successful.

## Gate and confidence

Separate **blocking**, **quality-impacting**, and **optional** issues. Broken
actions, lost input, unreadable content, serious overflow, inaccessible critical
controls, missing critical states and severe motion/performance jank block the
affected experience. Fix and repeat the relevant check; unknown reproduction is
not proof a reported defect is resolved.

Evaluate relevant product specificity, visual intent, experience/system coherence,
platform fit and craft using PASS / PASS WITH CONCERNS / FAIL / NOT VERIFIED.
Do not turn these judgments into invented numerical quality scores.

Example: analysis and eight total-formatting tests pass, but a log reports an
invoice-row overflow at text scaling 2.0. Record the two checks as supplied
results; the overflow remains unresolved until checked. Phone runtime, tablet,
iOS, screen reader, error states and profiling remain NOT VERIFIED if absent.
The correct release claim is narrower than “fully tested.”

## Report

Lead with the verdict for the requested scope. Give verified checks and evidence,
blockers with next actions, then unverified coverage and its practical limit.
Name platforms individually when coverage differs. Use VERIFIED only for the
checks actually performed; use PARTIAL or NOT VERIFIED for incomplete scope.
An inaccessible screenshot, source file or device cannot count as inspected.
Finish once evidence supports the scoped verdict; do not keep polishing beyond
the requested gate.
