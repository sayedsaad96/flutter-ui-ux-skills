# flutter-ui-ux Routing Rubric

Score each criterion as PASS or FAIL. `NOT APPLICABLE` is allowed only where the scenario explicitly makes a criterion irrelevant.

## Criteria

1. **Mode** — Correctly identifies CREATE, REDESIGN, AUDIT, or the required composite sequence.
2. **Complexity** — Uses MICRO, SCREEN, FLOW, or PRODUCT proportionally to the task.
3. **Evidence** — Uses the strongest evidence explicitly available in the scenario before guessing.
4. **Scope Discipline** — Does not expand a small task into unnecessary design-system/product work and does not under-process a product-scale task.
5. **Routing Ownership** — Names only capabilities justified by the decisions in the task; does not route by keyword alone.
6. **Audit Safety** — Keeps AUDIT read-only unless implementation is explicitly requested.
7. **Verification Honesty** — Does not claim runtime, visual, accessibility, performance, platform, or motion verification that the scenario does not provide.
8. **No Fake Delegation** — Does not claim a specialist or tool was invoked unless the runtime actually supports and performed it.
9. **Architecture Neutrality** — Does not rewrite app architecture/state management merely because another pattern is preferred.
10. **Output Fit** — Produces an output shape appropriate to CREATE, REDESIGN, or AUDIT without unnecessary ceremony.

## Release Gate

A scenario passes only if all applicable criteria pass.
The skill release passes only when all six scenarios pass in the REFACTOR run.
