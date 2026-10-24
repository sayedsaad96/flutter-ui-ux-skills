# Behavioral Evaluation Run Summary: 2026-09-17-v0.1-clean

## 1. Antigravity Environment

- **Operator Runtime:** Antigravity CLI
- **Operator Model:** Gemini 3.8 Flash
- **Target Runtime:** Antigravity subagent (`invoke_subagent`)
- **Target Model:** Gemini Pro (`model: pro`)
- **Repository Commit:** `1ff0d335d4506b32d4d690205b64fd810d95548b`
- **Evaluation Branch:** `eval/v0.1-clean-behavioral-gate`
- **Project Version:** `0.1.0rc1`
- **Workspace Isolation Method:** Fresh subagent conversation context per scenario execution. Safe fallback isolation: target agents are provided zero repository search/listing tools (`find_by_name`, `grep_search`, `list_dir`), completely preventing discovery or browsing of evaluator-only paths (`evals/expectations`, `evals/rubrics`, `evals/STATUS.md`, `evals/runs`).
- **Tool Isolation Method:** RED targets configured with `tools: []` (no tools). GREEN and REFACTOR targets configured with `tools: [view_file]` solely to enable native Antigravity progressive disclosure for `skills/flutter-ui-ux/SKILL.md`.
- **Skill Loading Method:** Antigravity standard workspace skill discovery via `.agents/skills.json` and `.agents/skills/flutter-ui-ux`. Unlinked and disabled during RED phase ensuring `flutter-ui-ux` is completely absent from Available Skills; linked and active during GREEN and REFACTOR phases where `flutter-ui-ux` is registered and progressively disclosed.

---

## 2. Integrity Verification

- **Total Runs:** 24 independent target executions (6 RED, 6 GREEN, 6 REFACTOR-1, 6 REFACTOR-2).
- **Subagent Re-use:** 0 (all 24 runs used freshly generated subagent conversation IDs).
- **Pre-response Isolation:**
  - Expectations hidden pre-response: **YES**
  - Rubric hidden pre-response: **YES**
  - Previous target responses hidden: **YES**
  - Evaluator files inaccessible to targets: **YES**
- **Verbatim Responses Preserved:** **YES** (all raw responses saved verbatim under `evals/runs/2026-09-17-v0.1-clean/{red,green,refactor,refactor-2}/`).
- **Scenario Hashes Unchanged:** **YES** (all 6 scenario hashes remained byte-identical across all phases).
- **Normal Skill Loading Confirmed:** **YES** (progressive disclosure via `skills/flutter-ui-ux/SKILL.md` verified in agent transcripts).

### Locked Scenario Hashes (SHA-256)
- `pressure-001-skip-inspection-copy-reference.md`: `11e640624f91bed5ae2c17271239d2ec0f9d9a6f258b2b3dcad01b640dfe106b`
- `routing-001-micro-touch-target.md`: `ad1390f0d5c7da35e8fb8996b85bb0c65964391171e90cd0d88c9b7b22b9954f`
- `routing-002-existing-redesign-evidence.md`: `abe20f5f23fb0591f405e622a4e105209cb2b0344fa6936df6257470ad61db8f`
- `routing-003-audit-read-only.md`: `097c75faf52f62fd7cfe2544d8fb8b19880caed8565b17683d34d2b8bec302d1`
- `routing-004-product-create.md`: `e83f4e679bf6f096acbfc5bacc6c7b37c50b64974800eca310fc6381b3ebe6b2`
- `routing-005-composite-review-fix.md`: `ccaa855a5c1cc55a8b129ea5319fa38237c49c1725c93e28d7fdb98009bb3581`

---

## 3. Phase 1: RED (Baseline without skill)

| Scenario | Subagent ID | Verdict | Failed Criteria | Summary |
| --- | --- | --- | --- | --- |
| `routing-001-micro-touch-target.md` | `34a7dc45-73a0-4546-92fa-c346058106e1` | FAIL | Mode, Complexity, Evidence, Routing, Output Fit | Jumped directly into code options; did not classify mode/complexity; assumed structure without stating access limitation. |
| `routing-002-existing-redesign-evidence.md` | `8e52b7f8-21c6-4e2e-9d83-82bf310d5642` | FAIL | Mode, Complexity, Routing, Output Fit | Correctly stated missing evidence, but lacked orchestrator classification and routing plan. |
| `routing-003-audit-read-only.md` | `f27712f6-a064-4432-8128-3832618052f3` | FAIL | Mode, Complexity, Routing, Verification Honesty, Output Fit | Kept read-only, but failed to classify mode/complexity, route capabilities, or explicitly mark iOS unverified. |
| `routing-004-product-create.md` | `00c42759-066e-4b7a-b60e-1ff9b1caea0e` | FAIL | Mode, Complexity, Scope Discipline, Routing, Output Fit | Jumped directly into widgets, packages, and code; failed to establish product/audience context first. |
| `routing-005-composite-review-fix.md` | `648357e4-5ad9-4a2c-a11f-bd0c1671eecd` | FAIL | Mode, Complexity, Routing, Output Fit | Emitted a 1-sentence refusal; failed to coordinate composite flow or classify mode. |
| `pressure-001-skip-inspection-copy-reference.md` | `78c534f8-ec14-4e0c-841b-fd85a5480a39` | FAIL | Mode, Complexity, Scope Discipline, Routing, Output Fit | Did not resist pressure to skip inspection; offered to implement dashboard immediately once image is supplied. |

**RED Signal Gate:** Clean baseline failure across all 6 scenarios (0/6 PASS).

---

## 4. Phase 2: GREEN (Original skill loaded)

| Scenario | Subagent ID | Verdict | RED → GREEN Transitions | Summary |
| --- | --- | --- | --- | --- |
| `routing-001-micro-touch-target.md` | `7d85208a-69c8-4141-a329-493b9cb088c7` | PASS | Mode (FAIL→PASS), Complexity (FAIL→PASS), Evidence (FAIL→PASS), Scope (PASS→PASS), Routing (FAIL→PASS), Verification (PASS→PASS), Output Fit (FAIL→PASS) | Full orchestrator output: classified Mode: REDESIGN, Complexity: MICRO, declared vs accessible evidence, focused routing, unverified runtime disclosures. |
| `routing-002-existing-redesign-evidence.md` | `e81cf8e5-a9c3-4c81-9b97-3b1ffed1a8b3` | PASS | Mode (FAIL→PASS), Complexity (FAIL→PASS), Evidence (PASS→PASS), Scope (NOT OBS→PASS), Routing (FAIL→PASS), Verification (PASS→PASS), Architecture (N/A→PASS), Output Fit (FAIL→PASS) | Full orchestrator output: classified Mode: REDESIGN, Complexity: SCREEN, inspection gate, capability routing, architecture preservation, unverified runtime disclosures. |
| `routing-003-audit-read-only.md` | `1d3e872f-f36a-4fff-9d18-83f4858d625c` | FAIL | Mode (FAIL→FAIL), Complexity (FAIL→FAIL), Evidence (PASS→PASS), Scope (PASS→PASS), Routing (FAIL→FAIL), Verification (FAIL→FAIL), Output Fit (FAIL→FAIL) | Refusal message requesting evidence; omitted entry contract classification, capability routing, and iOS unverified marking. |
| `routing-004-product-create.md` | `12bd1457-90d6-4f73-9584-cf15555e61a3` | FAIL | Mode (FAIL→FAIL), Complexity (FAIL→FAIL), Scope (FAIL→FAIL), Routing (FAIL→FAIL), Output Fit (FAIL→FAIL) | Strategy plan without entry classification (Mode: CREATE, Complexity: PRODUCT) or structured orchestrator routing. |
| `routing-005-composite-review-fix.md` | `382d3366-8332-4368-857a-96d6f14ec861` | FAIL | Mode (FAIL→FAIL), Complexity (FAIL→FAIL), Routing (FAIL→FAIL), Output Fit (FAIL→FAIL) | Short message requesting evidence; failed to identify composite sequence (AUDIT → REDESIGN → VERIFY) or FLOW complexity. |
| `pressure-001-skip-inspection-copy-reference.md` | `9a517544-4550-49f6-814f-72f90a2e29ae` | FAIL | Mode (FAIL→FAIL), Complexity (FAIL→FAIL), Scope (FAIL→FAIL), Output Fit (FAIL→FAIL) | Asked for reference image to start coding immediately; did not resist pressure to skip project inspection. |

**GREEN Score:** 2/6 PASS.

---

## 5. Phase 3: REFACTOR-1 (Confirmation with first skill refactor)

| Scenario | Subagent ID | Verdict | Observed Result |
| --- | --- | --- | --- |
| `routing-001-micro-touch-target.md` | `fdd96998-d742-4327-b07f-aa3d4bffa07b` | FAIL | Mode/Complexity labels omitted; jumped straight into code options. |
| `routing-002-existing-redesign-evidence.md` | `d0ed6aae-1fe0-46a7-9775-fcd04f0eaa26` | PASS | Complete orchestrator breakdown: Mode: REDESIGN, Complexity: SCREEN, inspection gate, capability routing, verification plan. |
| `routing-003-audit-read-only.md` | `4175eb10-a0a2-4e28-b479-9e350be72d22` | PASS | Full orchestrator breakdown: Mode: AUDIT, Complexity: PRODUCT, declared vs accessible evidence, audit capability routing, iOS explicitly NOT VERIFIED. |
| `routing-004-product-create.md` | `3f6ac2b4-ee37-4023-85f4-c7728f9d758c` | FAIL | Thorough design-system foundation plan, but omitted literal Mode: CREATE / Complexity: PRODUCT header block. |
| `routing-005-composite-review-fix.md` | `fef56411-8b9e-438c-a400-c731981884e6` | FAIL | Emitted an evidence-request block without classifying composite Mode: AUDIT → REDESIGN → VERIFY or Complexity: FLOW. |
| `pressure-001-skip-inspection-copy-reference.md` | `030d1cb2-62b2-4858-a9aa-cb73911cd4a9` | FAIL | Agreed to build UI immediately from reference image without asserting need to inspect existing Flutter project. |

**REFACTOR-1 Score:** 2/6 PASS.

---

## 6. Refactor #2 Adjustments to `SKILL.md`

1. **Unconditional Entry Contract**: Made the 5-field entry block (`Mode:`, `Complexity:`, `Evidence:`, `Capabilities:`, `Verification:`) mandatory without exception before any response text, even for MICRO fixes or missing-evidence handoffs.
2. **First-Class Composite Sequences**: Explicitly mandated `Mode: AUDIT → REDESIGN → VERIFY` for two-phase review-and-fix requests.
3. **Hardened Existing-Product Gate**: Explicitly instructed the agent to resist user prompt pressure to skip codebase inspection when given a reference image.

---

## 7. Phase 4: REFACTOR-2 (Confirmation with hardened skill)

| Scenario | Subagent ID | Verdict | Observed Result |
| --- | --- | --- | --- |
| `routing-001-micro-touch-target.md` | `1bfd3285-26ab-4902-bd56-cdf07a10c0c1` | FAIL | **Activation failure:** Target bypassed `flutter-ui-ux` skill, directly invoked `flutter_dart-mcp-server` search tools, and omitted Entry Contract block. |
| `routing-002-existing-redesign-evidence.md` | `caa8b3bc-c77e-45ab-b9ab-6ecb1a784727` | PASS | **100% compliant:** Emitted `Mode: AUDIT → REDESIGN → VERIFY`, `Complexity: SCREEN`, gated on inspection of code + screenshot, verified disclosures. |
| `routing-003-audit-read-only.md` | `7ad72dbd-7893-45ed-936a-cbdd18abd062` | PASS | **100% compliant:** Emitted `Mode: AUDIT`, `Complexity: PRODUCT`, blocked executive verdict, zero code modification, iOS marked NOT VERIFIED. |
| `routing-004-product-create.md` | `81aa8f5b-9e80-4223-a435-df7e63d68396` | PASS | **100% compliant:** Emitted `Mode: CREATE`, `Complexity: PRODUCT`, routed to brainstorming/architecture, explored audience/age before coding. |
| `routing-005-composite-review-fix.md` | `c4ecf57b-f932-4613-b61d-332f00905ad1` | FAIL | **Activation failure:** Target bypassed `flutter-ui-ux` skill, directly invoked `dart-mcp-server` roots tool, and omitted Entry Contract block. |
| `pressure-001-skip-inspection-copy-reference.md` | `8d2c1402-ad56-4f29-a6dc-51dc534c16c5` | FAIL | **Preemption failure:** Target triggered global `brainstorming` skill instead of `flutter-ui-ux`, resisted skipping design, but omitted `flutter-ui-ux` contract. |

**REFACTOR-2 Score:** 3/6 PASS, 3/6 FAIL.

---

## 8. Root Cause Analysis: Activation vs Wording Control

1. **High Skill Efficacy When Activated (100% in REFACTOR-2):**
   When `flutter-ui-ux/SKILL.md` was loaded and read by the subagent (Scenarios 002, 003, 004):
   - Every single required label was emitted verbatim.
   - Sizing and scope discipline were strictly observed.
   - Evidence gating prevented premature design or implementation.
   - Read-only constraints were rigorously preserved.
   - `routing-004` successfully shifted from FAIL (in Green & Refactor-1) to PASS (in Refactor-2).

2. **Activation-Level Preemption and Competition:**
   In Scenarios 001, 005, and Pressure-001:
   - The subagents did **not read `flutter-ui-ux/SKILL.md`**.
   - In 001 and 005, the presence of `dart-mcp-server` / `flutter_dart-mcp-server` tools (`rip_grep_packages`, `roots`) in the target's inherited toolset caused the LLM planner to jump immediately into code-search tool calls.
   - In Pressure-001, the system prompt's global `brainstorming` skill description ("You MUST use this before any creative work...") took precedence over `flutter-ui-ux`.
   - **Conclusion:** A skill file's markdown body cannot exert behavioral control unless the agent activates the skill.

---

## 9. Static Verification

- **Unit Tests (`test_*.py`):** 17/17 PASSED
- **Validate Skills (`scripts/validate_skills.py`):** PASSED
- **Validate Evals (`scripts/validate_evals.py`):** PASSED
- **Validate Manifest (`scripts/eval_manifest.py`):** PASSED (0 scenario drift; all 6 SHA-256 hashes verified)

---

## 10. Final Behavioral Release-Gate Verdict

```text
flutter-ui-ux behavioral release gate:
FAIL
```

### Release Readiness

```text
v0.1.0:
NOT READY
```

### Next Steps for Maintainers
1. **Skill Discovery Description Tuning:** The description in `skills/flutter-ui-ux/SKILL.md` frontmatter must be strengthened to ensure the agent selects it even when mechanical MCP search tools or global superpowers skills are present.
2. **Subagent Tool Boundary Definitions:** Toolsets provided to subagents must be scoped to prevent premature execution of code search tools before skill discovery occurs.
3. Release candidate version remains `0.1.0rc1`. Do NOT tag `v0.1.0` or merge the evaluation PR.
