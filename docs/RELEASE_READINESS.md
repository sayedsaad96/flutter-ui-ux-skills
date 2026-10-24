# Release readiness — 0.2.0rc1

**Date:** 2026-10-24  
**Verdict:** complete eleven-skill local release candidate, ready for maintainer
review and publishing steps within the tested scope. No tag, push or public
release was performed as part of this preparation.

## Delivered

The approved design is implemented: one orchestrator, three workflow skills and
seven specialists. Every skill is self-contained; optional coordination uses
decision ownership rather than loading the entire suite. The public instructions
preserve existing app boundaries, evidence honesty and product-specific design.
Version metadata is `0.2.0rc1`; the earlier `0.1.0rc1` was never published here.

## Verification evidence

| Check | Result | Evidence |
|---|---|---|
| Local Python regression suite | 24 tests PASS | `tests/`; includes negative evidence-drift and missing-coverage cases |
| Skill metadata/files/references | PASS, 11 skills | `scripts/validate_skills.py` |
| Canonical prompt isolation and fingerprints | PASS, unchanged six scenarios | `scripts/validate_evals.py`, `scenario-manifest.json` |
| Explicit orchestrator behavior | 6/6 PASS | `evals/runs/2026-10-24-confirmation/` |
| Workflow/specialist application | 10/10 PASS | `evals/runs/2026-10-24-suite/` |
| Targeted Codex discovery | 3 UI positives + 1 unrelated negative PASS | `evals/runs/2026-10-24-discovery/` |
| Current release evidence integrity | PASS, 11 skills and 16 application cases | `release-readiness.json`, `scripts/validate_release.py` |
| CLI discovery | 11 skills found | `skills` CLI 1.7.4, local source, Windows/Node 24.15.0 |
| Isolated project installation | 11/11 copies match source bytes | `evals/runs/2026-10-24-install/summary.json` |

The installation destination was an ignored temporary project under
`.eval-tmp/install-smoke`, using `--agent codex --copy --yes` without global scope.
The installer listed the source and installed all eleven skills successfully.
`--list` and `--json` cannot be combined in CLI 1.7.4; the corrected listing ran
with `--list` alone. Package download needed network access; installation from
the local source then ran with the cached CLI. No user-wide skill installation
was changed by this smoke test.

Source fingerprints in the release report normalize CRLF to LF. The install
summary uses raw byte hashes and compares the installed copy to the actual
source bytes. Those two hash forms may differ for the same skill text.

## What the results establish

The guidance responds appropriately to the recorded task shapes when loaded in
fresh `gpt-6-luna` Codex contexts. The canonical prompts were unchanged across
confirmation phases. The ten new skill probes use the same prompt for a
pre-authoring control and a skill-loaded application. Seven controls already
passed; those are reference-usability checks, not demonstrated behavioral gains.
All scores and observed control gaps are inspectable alongside exact responses.

Targets were not given evaluator expectations or previous outputs. Read access
was restricted by instruction, not by a technical per-agent tool sandbox. Normal
system instructions and the skill catalog remained inherited. Discovery action
logs are target-reported rather than independently captured event traces.

## Limits and remaining publication actions

- No actual Flutter app patch was compiled or run in these application probes.
  Device, rendered UI, screen-reader and performance results are not established.
  Consumers must validate their own apps with the verification skill.
- One application case per new skill and four discovery probes are limited
  coverage. They do not establish exhaustive pressure, cross-model or cross-agent
  reliability. Six other activation probes were not run in this cycle.
- The earlier Antigravity run remains a historical activation failure. Explicit
  invocation is the supported fallback; these Codex results do not fix or certify
  that separate runtime.
- Checks ran locally on Windows. CI is configured for Windows and Ubuntu, but
  no remote CI success is claimed before the candidate is pushed.
- The full-suite remote install remains NOT VERIFIED because this candidate has
  not been pushed/tagged. The README distinguishes local and post-publication use.

Before publishing, rerun the documented gates from a clean checkout, review the
candidate, push the intended branch, inspect CI, and create the chosen release
tag. A stable version/tag should be chosen as a separate maintainer decision.
None of those external actions is implied by a local readiness verdict.

## Recheck

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/validate_skills.py .
python scripts/validate_evals.py .
python scripts/eval_manifest.py .
python scripts/validate_release.py .
```

These checks reject missing skills, incomplete scenario/criterion coverage,
nonpassing scores and changed skill/scenario/expectation/response artifacts.
They validate recorded evidence integrity; human review remains responsible for
the correctness of a behavioral score. See [CONTRIBUTING](../CONTRIBUTING.md).
