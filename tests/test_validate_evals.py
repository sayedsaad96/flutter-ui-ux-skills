import tempfile
import unittest
from pathlib import Path

from scripts.validate_evals import validate_evals


class ValidateEvalsTests(unittest.TestCase):
    def write(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_valid_scenario_expectation_pair_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(
                root / "evals" / "scenarios" / "example.md",
                "# Scenario: Example\n\n"
                "## User request\n\n\"Do X.\"\n\n"
                "## Available evidence\n\n- Code is available.\n",
            )
            self.write(
                root / "evals" / "expectations" / "example.md",
                "# Expectation: Example\n\n## Required behavior\n\n- Mode: X.\n",
            )
            self.assertEqual(validate_evals(root), [])

    def test_required_behavior_leaking_into_scenario_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(
                root / "evals" / "scenarios" / "example.md",
                "# Scenario: Example\n\n"
                "## User request\n\n\"Do X.\"\n\n"
                "## Available evidence\n\n- Code is available.\n\n"
                "## Required behavior\n\n- Mode: X.\n",
            )
            self.write(
                root / "evals" / "expectations" / "example.md",
                "# Expectation: Example\n\n## Required behavior\n\n- Mode: X.\n",
            )
            errors = validate_evals(root)
            self.assertTrue(any("evaluator-only marker" in e for e in errors))

    def test_scenario_without_matching_expectation_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(
                root / "evals" / "scenarios" / "example.md",
                "# Scenario: Example\n\n"
                "## User request\n\n\"Do X.\"\n\n"
                "## Available evidence\n\n- Code is available.\n",
            )
            (root / "evals" / "expectations").mkdir(parents=True, exist_ok=True)
            errors = validate_evals(root)
            self.assertTrue(any("missing expectation file" in e for e in errors))

    def test_expectation_without_matching_scenario_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "evals" / "scenarios").mkdir(parents=True, exist_ok=True)
            self.write(
                root / "evals" / "expectations" / "orphan.md",
                "# Expectation: Orphan\n\n## Required behavior\n\n- Mode: X.\n",
            )
            errors = validate_evals(root)
            self.assertTrue(any("no matching scenario" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
