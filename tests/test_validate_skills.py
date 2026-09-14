import tempfile
import unittest
from pathlib import Path

from scripts.validate_skills import validate_repository


class ValidateSkillsTests(unittest.TestCase):
    def write_skill(self, root: Path, folder: str, body: str) -> None:
        skill_dir = root / "skills" / folder
        skill_dir.mkdir(parents=True, exist_ok=True)
        (skill_dir / "SKILL.md").write_text(body, encoding="utf-8")

    def test_valid_skill_returns_no_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_skill(
                root,
                "flutter-ui-ux",
                "---\n"
                "name: flutter-ui-ux\n"
                "description: Use when working on Flutter UI/UX tasks.\n"
                "---\n\n"
                "# Flutter UI/UX\n",
            )
            self.assertEqual(validate_repository(root), [])

    def test_folder_and_name_must_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_skill(
                root,
                "flutter-ui-ux",
                "---\n"
                "name: wrong-name\n"
                "description: Use when working on Flutter UI/UX tasks.\n"
                "---\n\n# Skill\n",
            )
            errors = validate_repository(root)
            self.assertTrue(any("must match folder" in error for error in errors))

    def test_description_must_start_with_use_when(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_skill(
                root,
                "flutter-ui-ux",
                "---\n"
                "name: flutter-ui-ux\n"
                "description: Routes Flutter design work.\n"
                "---\n\n# Skill\n",
            )
            errors = validate_repository(root)
            self.assertTrue(any("description must start with 'Use when'" in error for error in errors))

    def test_duplicate_skill_names_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for folder in ("first", "second"):
                self.write_skill(
                    root,
                    folder,
                    "---\n"
                    "name: duplicate\n"
                    "description: Use when testing duplicate names.\n"
                    "---\n\n# Skill\n",
                )
            errors = validate_repository(root)
            self.assertTrue(any("duplicate skill name" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
