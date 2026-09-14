from __future__ import annotations

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[A-Za-z0-9-]+$")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}, [f"{path}: missing opening YAML frontmatter delimiter"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, [f"{path}: missing closing YAML frontmatter delimiter"]

    data: dict[str, str] = {}
    for raw in lines[1:end]:
        if not raw.strip():
            continue
        if ":" not in raw:
            errors.append(f"{path}: invalid frontmatter line: {raw}")
            continue
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, errors


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    skills_root = root / "skills"
    if not skills_root.exists():
        return [f"{skills_root}: skills directory does not exist"]

    seen_names: dict[str, Path] = {}
    for skill_file in sorted(skills_root.glob("*/SKILL.md")):
        folder = skill_file.parent.name
        data, parse_errors = parse_frontmatter(skill_file)
        errors.extend(parse_errors)
        if parse_errors:
            continue

        name = data.get("name", "")
        description = data.get("description", "")

        if not name:
            errors.append(f"{skill_file}: missing name")
        elif not NAME_RE.fullmatch(name):
            errors.append(f"{skill_file}: name must contain only letters, numbers, and hyphens")
        elif name != folder:
            errors.append(f"{skill_file}: name '{name}' must match folder '{folder}'")

        if not description:
            errors.append(f"{skill_file}: missing description")
        elif not description.startswith("Use when"):
            errors.append(f"{skill_file}: description must start with 'Use when'")

        if name:
            if name in seen_names:
                errors.append(
                    f"{skill_file}: duplicate skill name '{name}' also used by {seen_names[name]}"
                )
            else:
                seen_names[name] = skill_file

        all_lines = skill_file.read_text(encoding="utf-8").splitlines()
        end = all_lines.index("---", 1)
        frontmatter_size = sum(len(line) + 1 for line in all_lines[1:end])
        if frontmatter_size > 1024:
            errors.append(f"{skill_file}: frontmatter exceeds 1024 characters")

    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    errors = validate_repository(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Skill validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
