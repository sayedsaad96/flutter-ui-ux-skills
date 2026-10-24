---
name: auditing-flutter-ui
description: Use when reviewing a Flutter interface or flow for UI/UX defects, accessibility problems, design drift, motion concerns or pre-release priorities with findings rather than implementation.
---

# Auditing Flutter UI

Deliver an evidence-based, prioritized assessment. AUDIT is read-only unless the
user explicitly asks for changes. A small obvious fix is still a change; include
its recommendation instead of applying it during a findings-only review.

## Set the assessment boundary

Identify the screens, user journeys, platforms, languages and states in scope.
Inspect accessible code, themes, screenshots and runtime. Distinguish supplied
logs/reports from behavior you reproduced. An excerpt is not a whole-app audit;
an inaccessible screenshot cannot substantiate visual findings. Record gaps
without converting missing evidence into either a pass or an invented defect.

Follow critical user actions and their pending/failure/recovery states before
reviewing decoration. Assess only relevant areas: hierarchy, navigation, visual
system coherence, responsive/adaptive behavior, inclusion, state completeness,
performance and motion. Compare product identity and useful structure rather
than imposing a fashionable aesthetic or a competing application architecture.

## Write actionable findings

For each finding provide **severity → problem → evidence → user impact →
recommended direction**. Cite an inspected file/line, visible element, supplied
excerpt or recorded interaction. State whether the finding is an observed fact,
a supported design judgment or an unverified risk. Combine symptoms of one
underlying problem; do not inflate the count with duplicate findings.

| Severity | User consequence |
|---|---|
| Critical | A core task can cause serious harm, data loss or an unrecoverable outcome |
| High | A core task fails or excludes users, or recovery is substantially impaired |
| Medium | A usable task has material friction or inconsistency |
| Low | Local craft/refinement with limited task impact |

Severity follows impact and reach, not how easy the fix is. Uncertain evidence
should qualify the finding, not become a categorical allegation.

Example: a form remains submittable while pending and logs show two requests.
Report repeat submission as evidenced UI behavior, recommend an in-flight guard
consistent with the existing state owner, and identify service idempotency as
unknown. Do not claim duplicate charges without evidence or change payment logic
under a UI audit.

## Return a usable verdict

Lead with a scoped executive verdict, then Critical/High/Medium/Low findings in
priority order and the next verification steps. Separate release blockers,
quality-impacting work and optional refinements. For each key gap, say what
evidence would resolve it. If nothing can be inspected, report the limited scope
and evidence handoff rather than a fabricated “no issues” result.

Keep Android-only observations separate from iOS, web and other targets. Mark
unperformed runtime, visual, screen-reader, contrast, large-text, keyboard,
performance and motion checks NOT VERIFIED when relevant. No numerical quality
score or static test result substitutes for that coverage.

When review and fixes are both authorized, state the diagnosis before the
redesign work and retain evidence for the subsequent before/after comparison.
