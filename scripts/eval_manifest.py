from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

SCENARIOS_DIR = Path("evals/scenarios")
MANIFEST_SCHEMA_VERSION = 1
EXPECTED_SCENARIOS = {
    "routing-001-micro-touch-target.md",
    "routing-002-existing-redesign-evidence.md",
    "routing-003-audit-read-only.md",
    "routing-004-product-create.md",
    "routing-005-composite-review-fix.md",
    "pressure-001-skip-inspection-copy-reference.md",
}


def scenario_manifest(root: Path) -> dict:
    directory = root / SCENARIOS_DIR
    scenarios = {}
    for path in sorted(directory.glob("*.md")):
        scenarios[path.name] = {"sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    return {"schema_version": MANIFEST_SCHEMA_VERSION, "scenarios": scenarios}


def validate_manifest(root: Path, manifest_path: Path) -> list[str]:
    try:
        expected = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{manifest_path}: invalid manifest: {exc}"]
    actual = scenario_manifest(root)
    errors = []
    if set(actual["scenarios"]) != EXPECTED_SCENARIOS:
        errors.append("canonical scenario set differs from the six v0.1 scenarios")
    if expected != actual:
        errors.append(f"{manifest_path}: scenario hashes or manifest schema differ")
    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    manifest_path = Path(sys.argv[2]) if len(sys.argv) > 2 else root / "scenario-manifest.json"
    manifest = scenario_manifest(root)
    if manifest_path.exists():
        errors = validate_manifest(root, manifest_path)
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print(f"Scenario manifest valid: {manifest_path}")
        return 0
    if set(manifest["scenarios"]) != EXPECTED_SCENARIOS:
        print("ERROR: canonical scenario set differs from the six v0.1 scenarios")
        return 1
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
