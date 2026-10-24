# Contributing

Keep decision ownership clear and preserve evidence integrity. The approved
suite has one orchestrator, three workflows and seven specialists. Skills may be
installed individually; do not require undeclared tools or another skill merely
to make a leaf capability usable.

## Behavioral changes

1. Keep canonical orchestrator prompts in `evals/scenarios/`. Suite application
   prompts live in `evals/suite/scenarios/`; matching expectations are evaluator-only.
2. Targets must not see expectations, rubrics, previous responses, scores or
   release status before response capture. Use fresh contexts and document tool
   isolation accurately; instructions are not a technical sandbox.
3. Capture a no-skill control before authoring or changing behavior. When it
   fails, preserve the failure and show how guidance addresses it. When it
   already passes, record PASS; do not manufacture a RED result or claim a gain.
   Reusable reference guidance may still serve the approved suite.
4. Reuse the exact scenario across control/application runs. Record hashes,
   model/runtime, evidence access, skill loading and exact responses. Score only
   after capture. Keep raw responses verbatim, including incidental save notes.
5. Gate one skill before authoring the next. Re-run all affected scenarios after
   behavior changes; all six canonical cases apply to orchestrator changes.
6. Record declared evidence separately from actually accessible evidence. Do not
   infer code, visual, device, screen-reader or profiling access from prompt text.
7. Test discovery separately from loaded-skill behavior. Neither a CLI listing nor
   a forced invocation proves reliable automatic activation.

Historical baseline/result directories and the September run are preserved;
new evidence belongs under `evals/runs/<run-id>/`.

## Local gates

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/validate_skills.py .
python scripts/validate_evals.py .
python scripts/eval_manifest.py .
python scripts/validate_release.py .
```

Python 3.10+ is sufficient; no third-party Python packages are required. If the
host's temporary directory is restricted, point TEMP/TMP at a writable test
directory. The skill metadata validator checks this repository's flat frontmatter
conventions and simple inline local-file links; it is not a general YAML parser
or a complete Markdown/link checker.

`scenario-manifest.json` pins the six original prompts. Git attributes preserve
their original CRLF fingerprint bytes on Windows and Unix. Captured run artifacts
are byte-preserved. Release source fingerprints normalize CRLF to LF so a checkout
line-ending change alone does not invalidate the same skill text. Response and
scenario fingerprints remain byte-exact.

After a new evaluation, review its scores and update `release-readiness.json` to
reference the current skill text and exact captured artifacts. Never refresh
hashes merely to hide drift. Every applicable release criterion must PASS; a
NOT OBSERVABLE result needs more evidence, not an automatic pass. Canonical
rubric N/A judgments may be retained with reasons, but the current release report
contains only applicable PASS criteria.

## Publishing

Check all local gates, inspect the actual CLI discovery/install in an isolated
destination, and review the candidate's limitations. CI validates infrastructure
and recorded evidence integrity; it does not run models or Flutter devices.
Tagging, pushing and publishing are separate maintainer actions. A remote install
does not include unpushed local files.
