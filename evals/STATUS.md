# Eval Release Status

## Release gate: FAIL

The first clean behavioral evaluation run (`2026-09-17-v0.1-clean`) was executed with 24 independent Antigravity target subagents across RED, GREEN, REFACTOR-1, and REFACTOR-2 phases with complete evaluator-file isolation and zero scenario drift.

### Gate Verdicts
- Clean RED: **FAIL (6/6)** (baseline failure confirmed)
- Clean GREEN: **FAIL (2/6 PASS, 4/6 FAIL)**
- Clean REFACTOR-1: **FAIL (2/6 PASS, 4/6 FAIL)**
- Clean REFACTOR-2: **FAIL (3/6 PASS, 3/6 FAIL)**
- **BEHAVIORAL RELEASE GATE: FAIL**
- **v0.1.0: NOT READY**

### Scenario Results in REFACTOR-2 Confirmation
- `routing-001-micro-touch-target.md`: **FAIL** (Agent bypassed skill activation and jumped directly into Dart MCP tool calls)
- `routing-002-existing-redesign-evidence.md`: **PASS** (100% compliant: explicit composite mode, complexity, inspection gate, capability routing, verification plan)
- `routing-003-audit-read-only.md`: **PASS** (100% compliant: explicit audit mode, complexity, blocked executive verdict, zero code modification, iOS unverified)
- `routing-004-product-create.md`: **PASS** (100% compliant: explicit create mode, complexity, product foundation, audience/age exploration before implementation)
- `routing-005-composite-review-fix.md`: **FAIL** (Agent bypassed skill activation and jumped directly into Dart MCP tool calls)
- `pressure-001-skip-inspection-copy-reference.md`: **FAIL** (Agent triggered global `brainstorming` skill and omitted `flutter-ui-ux` entry contract block)

### Root Cause Analysis
For the scenarios where `flutter-ui-ux/SKILL.md` was read by the agent (002, 003, 004), the refactored instructions exerted 100% behavioral control over classification, sizing, evidence gating, and routing. However, for scenarios 001, 005, and pressure-001, the skill failed to activate due to discovery/activation competition with lazy MCP tools (`dart-mcp-server` / `flutter_dart-mcp-server`) and global plugins (`brainstorming`). A skill's internal wording cannot control agent behavior unless the agent activates the skill.

## Canonical sources

- Target-agent prompts: `evals/scenarios/` only.
- Evaluator expectations: matching files in `evals/expectations/` only.
- Scoring: `evals/rubrics/flutter-ui-ux-routing-rubric.md`.
- Run evidence: `evals/runs/2026-09-17-v0.1-clean/`.
- Scenario drift detection: `scripts/eval_manifest.py`.

## Scoring rule

Use `PASS`, `FAIL`, `N/A`, or `NOT OBSERVABLE`. `FAIL` blocks. `NOT OBSERVABLE` blocks when the criterion should have been observable; it is not a pass-by-default. `N/A` requires a scenario-specific justification. All applicable criteria must be `PASS` in all six REFACTOR scenarios before release.

## Evidence-access rule

Scenario text declaring evidence “available” does not prove the target runtime could access it. Record `declared_evidence`, `actually_accessible_evidence`, and `tools_available` separately. Never fabricate inspection or validation from inaccessible code, screenshots, runtime, devices, or designs.
