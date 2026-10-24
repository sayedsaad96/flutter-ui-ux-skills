import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_release import validate_release


NAMES = ('flutter-ui-ux', 'polishing-flutter-experiences', 'verifying-flutter-ui',
         'creating-flutter-ui', 'redesigning-flutter-ui', 'auditing-flutter-ui',
         'designing-flutter-systems', 'building-responsive-adaptive-flutter',
         'engineering-flutter-ui', 'designing-inclusive-flutter', 'crafting-flutter-motion')
ROUTING = ('mode', 'complexity', 'evidence', 'scope_discipline', 'routing_ownership',
           'audit_safety', 'verification_honesty', 'no_fake_delegation',
           'architecture_neutrality', 'output_fit')


class ValidateReleaseTests(unittest.TestCase):
    def fixture(self, root):
        from scripts.validate_evals import EXPECTED_SCENARIOS

        def artifact(relative):
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b'fixture\n')
            return {'path': relative, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}

        report = {'schema_version': 1, 'skills': {}}
        for name in NAMES:
            filenames = sorted(EXPECTED_SCENARIOS) if name == 'flutter-ui-ux' else [name + '.md']
            cases = []
            for filename in filenames:
                scenario_dir = 'evals/scenarios' if name == 'flutter-ui-ux' else 'evals/suite/scenarios'
                keys = ROUTING if name == 'flutter-ui-ux' else ('c1', 'c2', 'c3')
                cases.append({'scenario': artifact(scenario_dir + '/' + filename),
                              'expectation': artifact(scenario_dir.replace('/scenarios', '/expectations') + '/' + filename),
                              'response': artifact('evals/runs/fixture/' + filename),
                              'scores': {key: {'verdict': 'PASS', 'evidence': 'Fixture decision.'} for key in keys}})
            report['skills'][name] = {'skill': artifact('skills/' + name + '/SKILL.md'), 'cases': cases}
        return report

    def save(self, root, report):
        (root / 'release-readiness.json').write_text(json.dumps(report), encoding='utf-8')

    def test_complete_evidence_passes_and_changed_artifacts_fail(self):
        for field in ('skill', 'scenario', 'expectation', 'response'):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                report = self.fixture(root)
                self.save(root, report)
                self.assertEqual(validate_release(root), [])
                entry = report['skills']['creating-flutter-ui']
                target = entry[field] if field == 'skill' else entry['cases'][0][field]
                (root / target['path']).write_text('changed', encoding='utf-8')
                self.assertTrue(validate_release(root))

    def test_missing_skill_or_scenario_coverage_fails(self):
        for missing in ('skill', 'scenario'):
            with self.subTest(missing=missing), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                report = self.fixture(root)
                if missing == 'skill':
                    del report['skills']['crafting-flutter-motion']
                else:
                    report['skills']['flutter-ui-ux']['cases'].pop()
                self.save(root, report)
                self.assertTrue(validate_release(root))

    def test_incomplete_or_nonpassing_scores_fail(self):
        for verdict in ('FAIL', 'NOT OBSERVABLE', 'N/A', ''):
            with self.subTest(verdict=verdict), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                report = self.fixture(root)
                report['skills']['engineering-flutter-ui']['cases'][0]['scores']['c1']['verdict'] = verdict
                self.save(root, report)
                self.assertTrue(validate_release(root))


if __name__ == '__main__':
    unittest.main()
