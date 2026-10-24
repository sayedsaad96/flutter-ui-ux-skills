import tempfile
import unittest
from pathlib import Path

from scripts.validate_skills import validate_repository


class ValidateSkillsTests(unittest.TestCase):
    def write_skill(self, root: Path, folder: str, body: str) -> None:
        skill_dir = root / "skills" / folder
        skill_dir.mkdir(parents=True, exist_ok=True)
        (skill_dir / "SKILL.md").write_text(body, encoding="utf-8")

    def test_empty_or_incomplete_skill_tree_fails(self):
        for folder in ("skills", "skills/orphan"):
            with self.subTest(folder=folder), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / folder).mkdir(parents=True)
                self.assertTrue(validate_repository(root))

    def test_invalid_public_names_fail(self):
        for name in ("Uppercase", "-leading", "trailing-", "two--hyphens", "x" * 65):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.write_skill(root, name, f"---\nname: {name}\ndescription: Use when testing.\n---\n# Skill\n")
                self.assertTrue(validate_repository(root))

    def test_duplicate_frontmatter_key_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_skill(root, "example", "---\nname: wrong\nname: example\ndescription: Use when testing.\n---\n# Skill\n")
            self.assertTrue(validate_repository(root))

    def test_missing_local_reference_fails_then_resolves(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_skill(root, "example", "---\nname: example\ndescription: Use when testing.\n---\n# Skill\nRead [guide](references/guide.md).\n")
            self.assertTrue(validate_repository(root))
            reference = root / "skills/example/references/guide.md"
            reference.parent.mkdir()
            reference.write_text("# Guide\n", encoding="utf-8")
            self.assertEqual(validate_repository(root), [])

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
