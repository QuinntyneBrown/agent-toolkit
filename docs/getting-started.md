# Getting started

Install the skills in a consuming project, establish agent guidance for a new
project, and turn requirements into detailed designs. The examples below use
Claude Code.

## Prerequisites

| Tool | When it is needed |
| --- | --- |
| Git | Clone the toolkit and retrieve updates. |
| Claude Code | Load and run the installed skills. |
| Python 3 | Run the agent-file generator and diagram renderer; both use the Python standard library. |
| PlantUML and Java | Render the design skill's diagrams using a local PlantUML installation. |

Requirements authoring does not need the diagram tools. For Java setup, see the
[PlantUML installation guide](https://plantuml.com/starting).

## Install the skills

Clone the toolkit if it is not already available locally:

```sh
git clone https://github.com/QuinntyneBrown/agent-toolkit.git
cd agent-toolkit
```

Choose an installation scope. These locations follow the
[Claude Code skills documentation](https://code.claude.com/docs/en/skills#where-skills-live).

| Scope | Destination | Availability |
| --- | --- | --- |
| Project | `<project>/.claude/skills/` | The consuming project. |
| Personal | `~/.claude/skills/` | Projects used by the current user. |

Copy entire skill folders so references and scripts remain available. The
commands below are for a new project installation. Replace the example project
path with an existing project directory. If a selected skill is already installed, follow
[Updating skills](#updating-skills) before copying.

### Windows PowerShell

Run from the toolkit checkout:

```powershell
$toolkitProject = (Resolve-Path -LiteralPath 'C:\projects\my-app').Path
$toolkitDestination = Join-Path $toolkitProject '.claude\skills'
New-Item -ItemType Directory -Path $toolkitDestination -Force | Out-Null
Copy-Item -LiteralPath 'skills\agent-instruction-files' -Destination $toolkitDestination -Recurse
Copy-Item -LiteralPath 'skills\requirements-engineer' -Destination $toolkitDestination -Recurse
Copy-Item -LiteralPath 'skills\software-design-document' -Destination $toolkitDestination -Recurse
```

For a personal installation, set `$toolkitDestination` to
`Join-Path $env:USERPROFILE '.claude\skills'` instead.

### macOS and Linux

Run from the toolkit checkout:

```sh
toolkit_project='/path/to/my-app'
toolkit_destination="$toolkit_project/.claude/skills"
mkdir -p "$toolkit_destination"
cp -R skills/agent-instruction-files "$toolkit_destination/"
cp -R skills/requirements-engineer "$toolkit_destination/"
cp -R skills/software-design-document "$toolkit_destination/"
```

For a personal installation, set `toolkit_destination="$HOME/.claude/skills"`
instead.

The installed project structure is:

```text
my-app/
└── .claude/
    └── skills/
        ├── agent-instruction-files/
        │   ├── SKILL.md
        │   ├── assets/
        │   └── scripts/
        ├── requirements-engineer/
        │   └── SKILL.md
        └── software-design-document/
            ├── SKILL.md
            ├── references/
            ├── scripts/
            └── evals/
```

## Create agent instruction files

The [agent instruction files skill](../skills/agent-instruction-files/SKILL.md)
uses a project description to generate guidance before implementation begins.
Its templates prescribe .NET CLI conventions or Angular/.NET web conventions.
It does not infer guidance from an existing codebase.

Open Claude Code in the new project directory and invoke:

```text
/agent-instruction-files This is a new library lending web application with an Angular frontend and a .NET API.
```

The skill writes `AGENTS.md` and pointer files for Claude, Gemini, and Copilot.
The guidance stays in `AGENTS.md` so the files do not duplicate project rules.

The generator can also be run directly with Python, without installing the Primer
.NET tool. From the toolkit checkout, use an existing target directory:

```sh
python skills/agent-instruction-files/scripts/render.py --path /path/to/new-project --archetype cli --prompt "A .NET command-line tool that validates CSV files."
```

Replace the target path for the local system. Use `--archetype web` for the web
template, `--prompt-file` for a description stored in a UTF-8 file, and `--dry-run`
to report planned paths without writing. Repeat `--agent` to select pointer files;
the default includes all supported agents.

Existing output files are updated when their content differs. Preserve intentional
manual changes before rerunning. Review generated guidance, including the Purpose
section if the description contains Markdown fences. The renderer limits output
to 150 lines and reports when a long description causes truncation.

## Create requirements and designs

Start Claude Code from the consuming project's root. Invoke:

```text
/requirements-engineer Define the requirements for a library lending system with a catalog, member accounts, loans, and returns.
```

Review the L1 capabilities and L2 behaviors, including their acceptance criteria.
The skill writes `docs/specs/L1.md` and `docs/specs/L2.md`, preserving existing
requirement IDs when updating a specification.

Once both levels are present, invoke:

```text
/software-design-document Create detailed feature designs from docs/specs/, including rendered diagrams.
```

The design skill organizes the output by subsystem and feature. Each feature
contains a `README.md` with Overview, Description, Requirements, and Diagrams
sections, plus PlantUML sources and PNG images in a `diagrams/` directory.

Review the designs against the source requirements. Acceptance tests are written
during development, using the L2 traceability convention in the requirements skill.

## Configure diagram rendering

Install PlantUML using its [local installation guide](https://plantuml.com/starting).
Class and component diagrams use Graphviz; depending on the platform and PlantUML
distribution, a separate Graphviz installation may be needed. See
[PlantUML's Graphviz guidance](https://plantuml.com/graphviz-dot).

The bundled renderer searches in this order:

1. A JAR file identified by `PLANTUML_JAR`.
2. The `plantuml` command on `PATH`.
3. The common JAR locations listed in
   [render_puml.py](../skills/software-design-document/scripts/render_puml.py).

For a JAR installation, set its path for the current terminal session:

```powershell
# PowerShell: use the actual path to the installed JAR.
$env:PLANTUML_JAR = 'C:\tools\plantuml.jar'
```

```sh
# macOS or Linux: use the actual path to the installed JAR.
export PLANTUML_JAR='/path/to/plantuml.jar'
```

Run the renderer from the consuming project's root:

```sh
python .claude/skills/software-design-document/scripts/render_puml.py docs/detailed-designs
```

Use `python3` if that is the Python 3 executable on the system. For a personal
installation, replace the script path with the installed copy under
`~/.claude/skills/software-design-document/scripts/`.

Inspect the output images and confirm that every design's relative image links
resolve. The reference templates use PlantUML's bundled C4 library, so they do
not require downloading C4 includes during rendering.

## Updating skills

Record the toolkit revision used for an installation with `git rev-parse HEAD`.
Retrieve updates with `git pull --ff-only` from the toolkit checkout, then review
the [changelog](../CHANGELOG.md) and the changes to each installed skill.

Before replacing an installed folder, preserve any local customizations in
version control or a backup outside the active skills directory. Copy the complete
updated folder and reapply intentional local changes. Check for files removed
upstream; copying over an existing folder does not remove obsolete files.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| A skill is unavailable | Confirm the installed path ends in `<skill-name>/SKILL.md`. Restart Claude Code if the top-level skills directory was created after the session started. |
| A reference or script is missing | Copy the entire skill directory, including `references/` and `scripts/`. |
| The agent-file generator reports a missing template | Restore the skill's `assets/` directory. Regeneration from source requires a Primer checkout, as described in the skill. |
| The agent-file generator reports `Not a directory` | Create the target project directory before running the command. |
| Agent guidance is truncated | Shorten the description, regenerate, and review the end of `AGENTS.md` for missing guidance. |
| Design generation stops at the requirements gate | Provide both L1 and L2 requirements under `docs/specs/`, with L2 entries tracing to their parent L1. |
| `PlantUML not found` | Check `PLANTUML_JAR`, the `plantuml` command on `PATH`, or a supported JAR location. |
| Java cannot be started | Confirm `java -version` works in the same terminal used for rendering. |
| A diagram has a syntax or layout error | Inspect the generated image and `.puml` source. Run PlantUML directly on that source to see its diagnostic output. |
| A PNG is missing or appears outdated | Confirm the source path passed to the renderer, render again, and inspect the corresponding PNG. |

For discovery behavior, see the
[Claude Code documentation](https://code.claude.com/docs/en/skills#live-change-detection).
For issues that remain unresolved, follow the [support guide](../SUPPORT.md).
