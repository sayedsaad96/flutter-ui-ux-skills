import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.eval_manifest import scenario_manifest, validate_manifest


EXPECTED_NAMES = {
    "routing-001-micro-touch-target.md",
    "routing-002-existing-redesign-evidence.md",
    "routing-003-audit-read-only.md",
    "routing-004-product-create.md",
    "routing-005-composite-review-fix.md",
    "pressure-001-skip-inspection-copy-reference.md",
}


class EvalManifestTests(unittest.TestCase):
    def write_scenario(self, root: Path, name: str, data: str | bytes) -> None:
        path = root / "evals" / "scenarios" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(data, str):
            data = data.encode("utf-8")
        path.write_bytes(data)

    def write_expected_suite(self, root: Path) -> None:
        for name in EXPECTED_NAMES:
            self.write_scenario(root, name, b"content\n")

    def test_sha256_is_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_scenario(root, "example.md", b"content\n")
            first = scenario_manifest(root)
            second = scenario_manifest(root)
            self.assertEqual(first, second)
            expected = hashlib.sha256(b"content\n").hexdigest()
            self.assertEqual(first["scenarios"]["example.md"]["sha256"], expected)

    def test_lf_and_crlf_produce_different_hashes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_scenario(root, "example.md", b"content\n")
            lf_hash = scenario_manifest(root)["scenarios"]["example.md"]["sha256"]
            self.write_scenario(root, "example.md", b"content\r\n")
            crlf_hash = scenario_manifest(root)["scenarios"]["example.md"]["sha256"]
            self.assertNotEqual(lf_hash, crlf_hash)
            self.assertEqual(lf_hash, hashlib.sha256(b"content\n").hexdigest())
            self.assertEqual(crlf_hash, hashlib.sha256(b"content\r\n").hexdigest())

    def test_modified_scenario_changes_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_scenario(root, "example.md", b"before\n")
            first = scenario_manifest(root)
            self.write_scenario(root, "example.md", b"after\n")
            second = scenario_manifest(root)
            self.assertNotEqual(first, second)

    def test_unchanged_manifest_validates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_expected_suite(root)
            manifest_path = root / "manifest.json"
            manifest_path.write_text(json.dumps(scenario_manifest(root)), encoding="utf-8")
            self.assertEqual(validate_manifest(root, manifest_path), [])

    def test_manifest_validation_detects_drift(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_expected_suite(root)
            manifest_path = root / "manifest.json"
            manifest_path.write_text(json.dumps(scenario_manifest(root)), encoding="utf-8")
            self.write_scenario(root, next(iter(EXPECTED_NAMES)), "after\n")
            self.assertTrue(validate_manifest(root, manifest_path))


if __name__ == "__main__":
    unittest.main()
