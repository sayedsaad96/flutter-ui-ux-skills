from __future__ import annotations

import sys
from pathlib import Path

EXPECTED_SCENARIOS = {
    "routing-001-micro-touch-target.md",
    "routing-002-existing-redesign-evidence.md",
    "routing-003-audit-read-only.md",
    "routing-004-product-create.md",
    "routing-005-composite-review-fix.md",
    "pressure-001-skip-inspection-copy-reference.md",
}
REQUIRED_SCENARIO_MARKERS = ["## User request", "## Available evidence"]
FORBIDDEN_SCENARIO_MARKERS = [
    "## Required behavior",
    "**Verdict:**",
    "Failed criteria:",
    "## Release Gate",
]
REQUIRED_EXPECTATION_MARKER = "## Required behavior"


def validate_evals(root: Path) -> list[str]:
    errors: list[str] = []
    scenarios_dir = root / "evals" / "scenarios"
    expectations_dir = root / "evals" / "expectations"
    prompts_dir = root / "evals" / "prompts"

    if prompts_dir.exists():
        errors.append(f"{prompts_dir}: deprecated competing prompt source must not exist")
    if not scenarios_dir.exists():
        return errors + [f"{scenarios_dir}: scenarios directory does not exist"]
    if not expectations_dir.exists():
        return errors + [f"{expectations_dir}: expectations directory does not exist"]

    scenario_files = sorted(scenarios_dir.glob("*.md"))
    scenario_names = {p.name for p in scenario_files}
    if scenario_names != EXPECTED_SCENARIOS:
        missing = sorted(EXPECTED_SCENARIOS - scenario_names)
        unexpected = sorted(scenario_names - EXPECTED_SCENARIOS)
        if missing:
            errors.append(f"{scenarios_dir}: missing canonical scenarios: {', '.join(missing)}")
        if unexpected:
            errors.append(f"{scenarios_dir}: unexpected scenarios: {', '.join(unexpected)}")

    for scenario in scenario_files:
        text = scenario.read_text(encoding="utf-8")
        for marker in REQUIRED_SCENARIO_MARKERS:
            if marker not in text:
                errors.append(f"{scenario}: missing required section '{marker}'")
        for marker in FORBIDDEN_SCENARIO_MARKERS:
            if marker in text:
                errors.append(f"{scenario}: contains evaluator-only marker '{marker}'")

    expectation_files = sorted(
        p for p in expectations_dir.glob("*.md") if p.name != "README.md"
    )
    expectation_names = {p.name for p in expectation_files}
    for name in sorted(scenario_names - expectation_names):
        errors.append(f"{expectations_dir / name}: missing expectation file for scenario '{name}'")
    for name in sorted(expectation_names - scenario_names):
        errors.append(f"{scenarios_dir / name}: expectation file '{name}' has no matching scenario")
    for expectation in expectation_files:
        if REQUIRED_EXPECTATION_MARKER not in expectation.read_text(encoding="utf-8"):
            errors.append(f"{expectation}: missing '{REQUIRED_EXPECTATION_MARKER}' section")

    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    errors = validate_evals(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Eval isolation validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
