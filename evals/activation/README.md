# Non-Gating Activation Probes

This test suite evaluates **skill activation reliability** for `flutter-ui-ux`.
It is completely decoupled from the release-gating behavioral evaluation suite in `evals/scenarios/`.

## Purpose

To verify whether the agent planner discovers and activates (reads) `flutter-ui-ux` when given UI/UX tasks across various shapes and sizes, and correctly avoids activating it for unrelated non-UI Flutter tasks.

## Activation Criteria

- **Positive Probes (UI/UX tasks):**
  - **PASS:** `flutter-ui-ux` is discovered and read (`view_file` on `skills/flutter-ui-ux/SKILL.md`) before UI implementation decisions or specialist tool execution.
  - **FAIL:** The runtime planner immediately invokes specialist implementation tools or competing generic workflow skills without ever reading `flutter-ui-ux`.
- **Negative Probes (Non-UI tasks):**
  - **PASS:** `flutter-ui-ux` is NOT read or activated.
  - **FAIL:** `flutter-ui-ux` is spuriously read for unrelated non-UI tasks (backend logic, database migrations, Gradle builds, networking).
