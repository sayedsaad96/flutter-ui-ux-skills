import tempfile
import unittest
from pathlib import Path

from scripts.validate_evals import validate_evals


SCENARIO_NAMES = [
    "routing-001-micro-touch-target.md",
    "routing-002-existing-redesign-evidence.md",
    "routing-003-audit-read-only.md",
    "routing-004-product-create.md",
    "routing-005-composite-review-fix.md",
    "pressure-001-skip-inspection-copy-reference.md",
]


class ValidateEvalsTests(unittest.TestCase):
    def write(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def populate_valid_suite(self, root: Path) -> None:
        for name in SCENARIO_NAMES:
            self.write(
                root / "evals" / "scenarios" / name,
                "# Scenario\n\n## User request\n\nDo X.\n\n## Available evidence\n\n- None.\n",
            )
            self.write(
                root / "evals" / "expectations" / name,
                "# Expectation\n\n## Required behavior\n\n- Mode: X.\n",
            )

    def test_valid_scenario_expectation_pair_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.populate_valid_suite(root)
            self.assertEqual(validate_evals(root), [])

    def test_required_behavior_leaking_into_scenario_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.populate_valid_suite(root)
            path = root / "evals" / "scenarios" / SCENARIO_NAMES[0]
            path.write_text(path.read_text() + "\n## Required behavior\n\n- Leak.\n", encoding="utf-8")
            self.assertTrue(any("evaluator-only marker" in e for e in validate_evals(root)))

    def test_scenario_without_matching_expectation_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.populate_valid_suite(root)
            (root / "evals" / "expectations" / SCENARIO_NAMES[0]).unlink()
            self.assertTrue(any("missing expectation file" in e for e in validate_evals(root)))

    def test_expectation_without_matching_scenario_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.populate_valid_suite(root)
            (root / "evals" / "scenarios" / SCENARIO_NAMES[0]).unlink()
            self.assertTrue(any("no matching scenario" in e for e in validate_evals(root)))

    def test_deprecated_prompts_directory_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.populate_valid_suite(root)
            (root / "evals" / "prompts").mkdir(parents=True)
            self.assertTrue(any("deprecated competing prompt" in e for e in validate_evals(root)))

    def test_missing_required_scenario_section_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.populate_valid_suite(root)
            path = root / "evals" / "scenarios" / SCENARIO_NAMES[0]
            path.write_text("# Scenario\n\n## User request\n\nDo X.\n", encoding="utf-8")
            self.assertTrue(any("missing required section" in e for e in validate_evals(root)))

    def test_expectation_missing_required_behavior_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.populate_valid_suite(root)
            path = root / "evals" / "expectations" / SCENARIO_NAMES[0]
            path.write_text("# Expectation\n", encoding="utf-8")
            self.assertTrue(any("missing '## Required behavior'" in e for e in validate_evals(root)))

    def test_unexpected_scenario_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.populate_valid_suite(root)
            self.write(root / "evals" / "scenarios" / "unexpected.md", "## User request\n## Available evidence\n")
            self.assertTrue(any("unexpected scenarios" in e for e in validate_evals(root)))


if __name__ == "__main__":
    unittest.main()
