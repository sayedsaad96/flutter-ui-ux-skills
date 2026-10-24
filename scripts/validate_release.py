from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

if __package__:
    from .validate_evals import EXPECTED_SCENARIOS
else:
    from validate_evals import EXPECTED_SCENARIOS

EXPECTED_SKILLS = set(('flutter-ui-ux polishing-flutter-experiences verifying-flutter-ui '
                      'creating-flutter-ui redesigning-flutter-ui auditing-flutter-ui '
                      'designing-flutter-systems building-responsive-adaptive-flutter '
                      'engineering-flutter-ui designing-inclusive-flutter crafting-flutter-motion').split())
ROUTING_CRITERIA = set(('mode complexity evidence scope_discipline routing_ownership '
                        'audit_safety verification_honesty no_fake_delegation '
                        'architecture_neutrality output_fit').split())


def check_artifact(root: Path, record: dict, normalize: bool = False) -> list[str]:
    if not isinstance(record, dict) or not isinstance(record.get('path'), str):
        return ['missing artifact path']
    path = (root / record['path']).resolve()
    if not path.is_relative_to(root.resolve()):
        return [f'{path}: artifact must stay inside repository']
    try:
        data = path.read_bytes()
    except OSError as exc:
        return [f'{path}: cannot read artifact: {exc}']
    if normalize:
        data = data.replace(b'\r\n', b'\n')
    if not data or hashlib.sha256(data).hexdigest() != record.get('sha256'):
        return [f'{path}: empty artifact or SHA-256 drift; capture and review evidence again']
    return []


def check_scores(name: str, scores: dict, criteria: set[str]) -> list[str]:
    if not isinstance(scores, dict) or set(scores) != criteria:
        return [f'{name}: incomplete criterion scores']
    errors = []
    for criterion, score in scores.items():
        if not isinstance(score, dict) or score.get('verdict') != 'PASS' or not score.get('evidence'):
            errors.append(f'{name}/{criterion}: applicable release criteria require PASS and evidence')
    return errors


def check_case_artifacts(root: Path, case: dict) -> list[str]:
    errors = []
    for key in ('scenario', 'expectation', 'response'):
        errors.extend(check_artifact(root, case.get(key)))
    scenario, expectation = case.get('scenario'), case.get('expectation')
    if isinstance(scenario, dict) and isinstance(scenario.get('path'), str) and isinstance(expectation, dict):
        if expectation.get('path') != scenario['path'].replace('/scenarios/', '/expectations/'):
            errors.append('expectation must match its scenario path')
    return errors


def check_cases(root: Path, name: str, cases: list) -> list[str]:
    canonical = name == 'flutter-ui-ux'
    directory = 'evals/scenarios/' if canonical else 'evals/suite/scenarios/'
    expected = {directory + filename for filename in EXPECTED_SCENARIOS} if canonical else {directory + name + '.md'}
    if not isinstance(cases, list) or not all(isinstance(case, dict) for case in cases):
        return [f'{name}: cases must be a list of records']
    actual = [case['scenario'].get('path') for case in cases
              if isinstance(case.get('scenario'), dict) and isinstance(case['scenario'].get('path'), str)]
    errors = []
    if len(actual) != len(expected) or set(actual) != expected:
        errors.append(f'{name}: incomplete or duplicate application scenario coverage')
    criteria = ROUTING_CRITERIA if canonical else {'c1', 'c2', 'c3'}
    for case in cases:
        errors.extend(check_case_artifacts(root, case))
        errors.extend(check_scores(name, case.get('scores'), criteria))
    return errors


def check_skill(root: Path, name: str, record: dict) -> list[str]:
    if not isinstance(record, dict):
        return [f'{name}: invalid skill evidence record']
    errors = []
    skill = record.get('skill')
    if not isinstance(skill, dict) or skill.get('path') != f'skills/{name}/SKILL.md':
        errors.append(f'{name}: evidence must identify its canonical SKILL.md')
    errors.extend(check_artifact(root, skill, normalize=True))
    errors.extend(check_cases(root, name, record.get('cases')))
    return errors


def validate_release(root: Path) -> list[str]:
    report_path = root / 'release-readiness.json'
    try:
        report = json.loads(report_path.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as exc:
        return [f'{report_path}: invalid release evidence: {exc}']
    if not isinstance(report, dict) or report.get('schema_version') != 1 or not isinstance(report.get('skills'), dict):
        return [f'{report_path}: invalid release evidence schema']
    records = report['skills']
    errors = []
    actual_skills = {path.parent.name for path in (root / 'skills').glob('*/SKILL.md')}
    if set(records) != EXPECTED_SKILLS or actual_skills != EXPECTED_SKILLS:
        errors.append('release requires all eleven approved skills and their evidence records')
    for name in sorted(EXPECTED_SKILLS & set(records)):
        errors.extend(check_skill(root, name, records[name]))
    return errors


def main() -> int:
    errors = validate_release(Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd())
    for error in errors:
        print(f'ERROR: {error}')
    if errors:
        return 1
    print('Release evidence validation passed: 11 skills, 16 application cases')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
