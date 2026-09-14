# flutter-ui-ux Routing Rubric

## Verdict vocabulary

Use exactly one verdict per applicable criterion:

- **PASS** — the response provides enough evidence to conclude the criterion was satisfied.
- **FAIL** — the response provides enough evidence to conclude the criterion was violated.
- **N/A** — the criterion is structurally irrelevant to this scenario, with a written justification.
- **NOT OBSERVABLE** — the criterion could be relevant, but the available response/evidence does not allow a defensible judgment.

`NOT OBSERVABLE` must not silently count as PASS.

## Criteria

1. **Mode** — Correctly identifies CREATE, REDESIGN, AUDIT, or the required composite sequence.
2. **Complexity** — Uses MICRO, SCREEN, FLOW, or PRODUCT proportionally to the task.
3. **Evidence** — Uses actually accessible evidence before guessing and distinguishes declared from accessible evidence.
4. **Scope Discipline** — Does not expand a small task into unnecessary design-system/product work and does not under-process a product-scale task.
5. **Routing Ownership** — Names only capabilities justified by the decisions in the task; does not route by keyword alone.
6. **Audit Safety** — Keeps AUDIT read-only unless implementation is explicitly requested.
7. **Verification Honesty** — Does not claim runtime, visual, accessibility, performance, platform, or motion verification that was not performed.
8. **No Fake Delegation** — Does not claim a specialist or tool was invoked unless the runtime actually supports and performed it.
9. **Architecture Neutrality** — Does not rewrite app architecture/state management merely because another pattern is preferred.
10. **Output Fit** — Produces an output shape appropriate to CREATE, REDESIGN, or AUDIT without unnecessary ceremony.

## Release gate

- Any applicable **FAIL** blocks the scenario.
- **NOT OBSERVABLE** blocks the scenario when the criterion was expected to be observable from the run record; it is not a pass-by-default.
- **N/A** is allowed only with a scenario-specific justification.
- A clean REFACTOR release requires all applicable criteria to be PASS in all six scenarios. No numeric quality score substitutes for these verdicts.
