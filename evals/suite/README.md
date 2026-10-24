# Suite application evaluations

These scenarios extend, rather than replace, the six canonical orchestrator
scenarios. Scenario files contain target-visible requests and raw evidence only.
Matching expectations are evaluator-only. Do not give targets expectations,
scores, earlier outputs, or this protocol before response capture.

Capture a baseline before authoring each new skill; apply the same scenario with
the skill loaded afterward. Author and gate one skill before starting the next.
Use a fresh target context for each independent evaluation. Record exact model,
instructions, tool access, hashes and verbatim outputs. These are application
and pressure probes of guidance, not Flutter runtime or visual validation.
