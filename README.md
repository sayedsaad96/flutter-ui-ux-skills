# Flutter UI/UX Skills

Eleven Agent Skills that help an AI coding assistant create, redesign, audit and
refine Flutter interfaces. Install them in your Flutter project, then ask your
assistant to use a skill in chat. The package contains Markdown instructions;
you do not add it as a Dart dependency in `pubspec.yaml`.

[الدليل بالعربية](README.ar.md) · [Skills](#choose-a-skill) · [Troubleshooting](#troubleshooting)

## Current version

**0.2.0rc1 — release candidate.** The full suite is on the
[`fix/flutter-ui-ux-activation-reliability` branch](https://github.com/sayedsaad96/flutter-ui-ux-skills/tree/fix/flutter-ui-ux-activation-reliability).
The commands below select that branch explicitly; the default branch may still
contain the earlier orchestrator-only candidate. No stable release is claimed.

## 1. Prepare your tools

You need:

- **Node.js 22.20.0 or newer**, including npm/npx. The instructions pin the tested
  [skills CLI](https://github.com/vercel-labs/skills) version, `1.7.4`.
- **Git**, available in your terminal, for repository installation/fallback.
- An AI coding assistant that supports Agent Skills. The walkthrough uses Codex;
  other CLI agent identifiers are listed below.
- Your Flutter project and its Flutter SDK for implementation and app checks.

Check the tools in a terminal:

```bash
node --version
npm --version
git --version
flutter doctor
```

Install missing tools from [Node.js](https://nodejs.org/en/download),
[Git](https://git-scm.com/downloads) or the [Flutter setup guide](https://docs.flutter.dev/get-started/install).
Resolve Flutter setup issues for the platform you intend to test.

## 2. Install inside your Flutter project

Open a terminal in the **root of the app you want to work on**, where
`pubspec.yaml` is located. Run:

```bash
npx skills@1.7.4 add "sayedsaad96/flutter-ui-ux-skills#fix/flutter-ui-ux-activation-reliability" --skill "*" --agent codex --copy --yes
```

The first run may ask npm to download the CLI; accept that prompt. This command:

- Selects the branch containing all eleven skills.
- Installs only this suite, in the current project.
- Targets Codex and copies the files, avoiding symlink setup.
- Keeps the installation project-local because no global flag is used.

For Codex, expect eleven folders under `.agents/skills/`, each containing a
`SKILL.md` file. The CLI may also create/update `skills-lock.json`; keep that file
with the project if you want to record the installed sources.

To use another assistant, replace `--agent codex` with its CLI identifier:

| Assistant | Identifier |
|---|---|
| Codex | `codex` |
| Claude Code | `claude-code` |
| Cursor | `cursor` |
| Antigravity | `antigravity` |

See the CLI's [supported agents](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)
for current paths and identifiers. Behavioral checks for this candidate were run
in Codex. Other runtimes require their own validation; explicit skill selection
is especially useful where automatic discovery competes with other skills.

To install only the orchestrator instead of the full suite, use:

```bash
npx skills@1.7.4 add "sayedsaad96/flutter-ui-ux-skills#fix/flutter-ui-ux-activation-reliability" --skill flutter-ui-ux --agent codex --copy --yes
```

The orchestrator works alone and falls back to direct reasoning when a specialist
is unavailable. Installing all eleven provides the full set of guidance.

## 3. Confirm the installation

From the same Flutter project, run:

```bash
npx skills@1.7.4 list --agent codex
```

For a full installation, check that the eleven names in the table below appear.
Then open your assistant on that Flutter project and start a new chat/session so
it can discover the newly installed skills.

## 4. Use a skill in the assistant's chat

Paste these prompts **in the AI chat, not in the terminal**. In Codex, `$` selects
a named skill. In another assistant, use its skill picker or explicitly ask it to
read the installed skill's `SKILL.md` before the task.

Start with the orchestrator for most Flutter UI work:

```text
$flutter-ui-ux Review lib/features/checkout and then fix the important UI issues.
Preserve the existing state management and navigation. Inspect the current code
before changing it. Report what you changed and what you actually verified.
```

Replace the example path with a real file or feature in your app. Give the
assistant access to that project. Attach screenshots or make a runtime available
when you want visual or interaction verification.

More examples:

```text
$creating-flutter-ui Create an expense-entry screen for this app. Use the current
theme, support Arabic and English, and include loading, validation and error states.
```

```text
$auditing-flutter-ui Audit the onboarding flow. Give prioritized findings with
evidence and recommendations only; do not change code.
```

```text
$designing-inclusive-flutter Fix large-text overflow and mixed Arabic/English
content in the invoice row. Preserve the stored data and existing callbacks.
```

```text
$crafting-flutter-motion Improve bookmark feedback in the reader. Preserve
reading position and audio state, and respect reduced-motion settings.
```

```text
$verifying-flutter-ui Check the changed screens before release. Separate static,
runtime, visual, accessibility and platform checks, and identify unverified coverage.
```

The orchestrator classifies the task, states the evidence it can access, selects
only the needed capabilities and reports verification honestly. A missing
screenshot, source file or runtime should produce a stated limitation, not a
claim that it was inspected. Audit-only requests stay read-only.

## Choose a skill

| Skill | Use it for |
|---|---|
| [flutter-ui-ux](skills/flutter-ui-ux/SKILL.md) | Routing and coordinating Flutter UI work |
| [creating-flutter-ui](skills/creating-flutter-ui/SKILL.md) | New screens, components and flows |
| [redesigning-flutter-ui](skills/redesigning-flutter-ui/SKILL.md) | Improving an existing interface from evidence |
| [auditing-flutter-ui](skills/auditing-flutter-ui/SKILL.md) | Read-only findings and priorities |
| [designing-flutter-systems](skills/designing-flutter-systems/SKILL.md) | Visual direction, themes, tokens and component language |
| [building-responsive-adaptive-flutter](skills/building-responsive-adaptive-flutter/SKILL.md) | Local layout constraints, resizing, navigation and input adaptation |
| [engineering-flutter-ui](skills/engineering-flutter-ui/SKILL.md) | Widget composition, state rendering and UI performance |
| [designing-inclusive-flutter](skills/designing-inclusive-flutter/SKILL.md) | Accessibility, localization, RTL, large text and focus |
| [crafting-flutter-motion](skills/crafting-flutter-motion/SKILL.md) | Purposeful transitions, lifecycle and reduced motion |
| [polishing-flutter-experiences](skills/polishing-flutter-experiences/SKILL.md) | Hierarchy, alignment, spacing, density and perceived craft |
| [verifying-flutter-ui](skills/verifying-flutter-ui/SKILL.md) | Quality gates, evidence and scoped readiness verdicts |

Skills are self-contained. They preserve the project's existing architecture and
derive visual decisions from its product rather than imposing one style.

## Update or remove

To refresh the full suite from this candidate branch, rerun the full installation
command in the same project. Review any local edits to installed copies first;
reinstallation can replace them.

To remove only the orchestrator:

```bash
npx skills@1.7.4 remove flutter-ui-ux --agent codex --yes
```

To choose several installed skills for removal, run `npx skills@1.7.4 remove`
interactively and select only this suite's names. Avoid `--all` if the project
contains skills from other packages.

## Local/offline source option

Clone the candidate if you prefer installing from a local checkout:

```bash
git clone --branch fix/flutter-ui-ux-activation-reliability --single-branch https://github.com/sayedsaad96/flutter-ui-ux-skills.git
```

Return to the destination Flutter project's root, then run the following with
the actual absolute path to the checkout's `skills` directory:

```bash
npx skills@1.7.4 add "/absolute/path/to/flutter-ui-ux-skills/skills" --skill "*" --agent codex --copy --yes
```

On Windows, an absolute path can look like `C:/Projects/flutter-ui-ux-skills/skills`.
Keep it quoted if it contains spaces. Installing from a local source still needs
the CLI available or cached; it does not by itself provide offline dependencies.

## Troubleshooting

| Problem | What to check |
|---|---|
| `npx` is not recognized | Install a supported Node.js version and reopen the terminal. |
| Fewer than eleven skills | Use the full command with the quoted `#fix/...` branch and `--skill "*"`; the default branch may be older. |
| Skills are missing in the assistant | Run the list command in the intended Flutter project, confirm the target agent, and start a new chat/session. |
| The assistant skips the guidance | Invoke `$flutter-ui-ux` or the specific installed skill explicitly. |
| GitHub/network installation fails | Check Git/network access or use the local checkout option. |
| Link permissions fail on Windows | Keep `--copy` in the command. |
| An audit starts modifying files | State that you want findings only and use `auditing-flutter-ui`. |
| Visual/device verification is unavailable | Provide the app, screenshots or runtime; require unverified checks to be named. |

## Validation and limits

The candidate passed 24 Python regression tests, six explicit orchestrator
scenarios and ten workflow/specialist application probes. Four targeted Codex
discovery probes and an isolated eleven-skill installation were also checked.
Some pre-authoring controls already passed; no improvement is claimed for those
cases. See [release status](evals/STATUS.md) and the
[readiness report](docs/RELEASE_READINESS.md) for scope and evidence.

These guidance probes do not certify a real Flutter app on devices, screen
readers or performance traces. Verify the app you change. No universal automatic
discovery or cross-agent reliability is claimed.

Maintainers can run these checks with Python 3.10+ and its standard library:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/validate_skills.py .
python scripts/validate_evals.py .
python scripts/eval_manifest.py .
python scripts/validate_release.py .
```

Normal skill users do not need Python. Read [CONTRIBUTING.md](CONTRIBUTING.md), the
[approved design](docs/superpowers/specs/2026-09-14-flutter-ui-ux-skill-system-design.md)
and [evaluation protocol](evals/README.md) before changing the suite.

MIT — see [LICENSE](LICENSE).
