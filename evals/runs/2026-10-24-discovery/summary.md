# Targeted Codex discovery probes

Three positive probes cover the earlier failure shapes: a small touch target,
review-and-fix, and reference pressure. One negative probe requests a pure Dart
Haversine utility. All four use fresh `gpt-6-luna` contexts, no explicit skill
name in the request, the inherited Codex skill catalog and instruction-scoped
file/tool access. Date: 2026-10-24.

The three positive target action logs report reading the installed
`flutter-ui-ux` skill before app-code/search tools; their answers show its
classification/evidence contract. The negative log reports no skill reads.
These four probes PASS their activation criteria. Six other catalog probes were
not run in this cycle.

Action logs are target-reported, not an independently captured tool-event trace.
The negative log's first file write was malformed; it and the missing answer
capture were repaired after response capture without rerunning the task or
reading more skills. The negative Dart code was not compiled; it is an activation
probe, not a utility correctness evaluation.

This does not resolve Antigravity activation or guarantee automatic discovery in
other configurations. Use explicit invocation when predictable selection matters.
