# Clean Run Artifacts

New clean behavioral evidence belongs under `evals/runs/<run-id>/`. Do not place new evidence in the historical `evals/baselines/` or `evals/results/` directories, and do not copy contaminated historical records into this structure.

## Structure

```text
evals/runs/<run-id>/
├── manifest.json
├── red/
│   ├── routing-001-micro-touch-target.md
│   └── ...
├── green/
│   └── ...
└── refactor/
    └── ...
```

`manifest.json` must include the scenario fingerprint manifest and run metadata. Each phase response file should be human-reviewable Markdown with YAML frontmatter or an equivalent explicit metadata block.

## Required per-response fields

```yaml
scenario: routing-001-micro-touch-target.md
scenario_sha256: <sha256 from the RED manifest>
model: <actual model identifier>
runtime: <actual evaluation runtime>
date: YYYY-MM-DD
skill_loaded: true|false
declared_evidence: []
actually_accessible_evidence: []
tools_available: []
exact_response: |
  <verbatim response>
scores:
  mode: PASS|FAIL|N/A|NOT OBSERVABLE
  complexity: PASS|FAIL|N/A|NOT OBSERVABLE
  evidence: PASS|FAIL|N/A|NOT OBSERVABLE
  scope_discipline: PASS|FAIL|N/A|NOT OBSERVABLE
  routing_ownership: PASS|FAIL|N/A|NOT OBSERVABLE
  audit_safety: PASS|FAIL|N/A|NOT OBSERVABLE
  verification_honesty: PASS|FAIL|N/A|NOT OBSERVABLE
  no_fake_delegation: PASS|FAIL|N/A|NOT OBSERVABLE
  architecture_neutrality: PASS|FAIL|N/A|NOT OBSERVABLE
  output_fit: PASS|FAIL|N/A|NOT OBSERVABLE
observed_failures: []
```

The actual response must remain verbatim. `NOT OBSERVABLE` is not a passing verdict; see the rubric and `evals/STATUS.md`.
