# Getting started

Install the skills in a consuming project, establish agent guidance for a new
project, and turn requirements into detailed designs. The examples below use
Codex.

## Prerequisites

| Tool | When it is needed |
| --- | --- |
| Git | Retrieve the plugin marketplace or clone the toolkit. |
| Codex CLI or Claude Code with plugin support | Install the plugin and load its skills. If `plugin` is unavailable, update the client. |
| Python 3.10 or later | Run the local installer; it uses the Python standard library. Python 3 is also needed for the agent-file generator and diagram renderer. |
| PlantUML and Java | Render the design skill's diagrams using a local PlantUML installation. |
| Application runtimes and capture tools | Record demos locally. Browser capture prefers Playwright and Chromium; terminal/native apps need compatible capture and WebM encoding tools. |

Requirements authoring does not need the diagram tools. For Java setup, see the
[PlantUML installation guide](https://plantuml.com/starting).

## Install the skills

### Codex plugin (recommended)

Run in a terminal:

```sh
codex plugin marketplace add QuinntyneBrown/agent-toolkit
codex plugin add agent-toolkit@agent-toolkit
```

### Claude Code plugin

Run in a terminal:

```sh
claude plugin marketplace add QuinntyneBrown/agent-toolkit
claude plugin install agent-toolkit@agent-toolkit
```

Inside Claude Code, the equivalent commands are:

```text
/plugin marketplace add QuinntyneBrown/agent-toolkit
/plugin install agent-toolkit@agent-toolkit
```

The first command registers the marketplace; the second installs all four skills
as one `agent-toolkit` plugin. Terminal commands use user scope by default. Choose
user scope if Claude's interactive installer prompts for a scope. Start a new
session in the consuming project afterward. Neither a manual clone nor Python is
needed for plugin installation, but the helpers still need the runtime tools
listed above. These GitHub commands require the manifests to be on the repository's
default branch.

In Codex, type `$` and select a skill from Agent Toolkit. Plugin entries may show
the `agent-toolkit:` namespace. In Claude Code, use:

```text
/agent-toolkit:agent-instruction-files Describe your new project here.
/agent-toolkit:requirements-engineer Define requirements for a library lending system.
/agent-toolkit:software-design-document Create detailed designs from docs/specs/.
/agent-toolkit:demo-video Create a demo video for each executable application.
```

Both plugins use the same `skills/` tree, including all templates, references,
and helper scripts. Repository guidance such as the root `CLAUDE.md` governs
contributors; it is not installed as context for a consuming project.

See the official [Codex plugin packaging guide](https://developers.openai.com/plugins/build/plugins)
and [Claude Code marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces).

### Test a local checkout

Before publishing the manifests, use an absolute path to the toolkit checkout in
place of `QuinntyneBrown/agent-toolkit` in the marketplace-add command, then run
the same plugin-install command. The marketplace and plugin names remain
`agent-toolkit`. This checks local packaging; it does not test GitHub retrieval.
Use a separate test configuration when developing so a local source does not
replace your GitHub marketplace registration.

### Switch from standalone skills

Use either the plugin or standalone copies of these skills in each client to
avoid duplicate entries. Before switching, back up any customized copies outside
the client's active skills directories, then move the corresponding standalone skill
folders out of those directories. Install the plugin and start a new session.
The plugin installer does not migrate customizations from standalone copies.

### Standalone installation (alternative)

Clone the toolkit if it is not already available locally:

```sh
git clone https://github.com/QuinntyneBrown/agent-toolkit.git
cd agent-toolkit
```

### Personal standalone installation

Run this from the toolkit checkout in PowerShell, macOS, or Linux:

```sh
python scripts/install_skills.py
```

Use `python3` if that is the Python 3 executable on the system. The installer
copies all complete skill folders into `$CODEX_HOME/skills`, or `~/.codex/skills`
when `CODEX_HOME` is unset. This is the destination used by Codex's bundled
skill-installer. This alternative does not use a marketplace or require Python
packages. The installed folders work independently of this checkout.

The installer verifies every copied file. Rerunning it skips identical skills;
if any existing skill differs, it stops before copying any skills. It never
overwrites customizations. See [Updating skills](#updating-skills) for replacements.

Codex also supports the `.agents/skills` discovery locations described in the
[official skills documentation](https://learn.chatgpt.com/docs/build-skills).
Use `--dest` to choose an alternative scope:

| Scope | Destination | Availability |
| --- | --- | --- |
| Personal (installer default) | `$CODEX_HOME/skills/`, otherwise `~/.codex/skills/` | Projects used by the current user. |
| Personal (alternative) | `~/.agents/skills/` | Projects used by the current user. |
| Project | `<project>/.agents/skills/` | The consuming project. |

Choose one location to avoid duplicate entries in skill selectors. The project
examples below install all skills into an existing consuming project.

### Windows PowerShell

Run from the toolkit checkout:

```powershell
$toolkitProject = (Resolve-Path -LiteralPath 'C:\projects\my-app').Path
$toolkitDestination = Join-Path $toolkitProject '.agents\skills'
python scripts/install_skills.py --dest $toolkitDestination
```

For the alternative personal location, pass
`--dest (Join-Path $env:USERPROFILE '.agents\skills')` instead.

### macOS and Linux

Run from the toolkit checkout:

```sh
toolkit_project='/path/to/my-app'
python3 scripts/install_skills.py --dest "$toolkit_project/.agents/skills"
```

For the alternative personal location, pass `--dest "$HOME/.agents/skills"` instead.

The installed project structure is:

```text
my-app/
└── .agents/
    └── skills/
        ├── agent-instruction-files/
        │   ├── SKILL.md
        │   ├── assets/
        │   └── scripts/
        ├── requirements-engineer/
        │   ├── SKILL.md
        │   └── agents/openai.yaml
        ├── demo-video/
        │   ├── SKILL.md
        │   ├── agents/openai.yaml
        │   ├── references/
        │   └── evals/
        └── software-design-document/
            ├── SKILL.md
            ├── agents/openai.yaml
            ├── references/
            ├── scripts/
            └── evals/
```

Skills will be available on the next Codex turn. If discovery does not refresh,
restart Codex. In the CLI or IDE, use `/skills` or type `$` to select a skill.

### Standalone Claude Code skills

The same complete folders can be copied into `<project>/.claude/skills/` or
`~/.claude/skills/`. Use `/agent-instruction-files`, `/requirements-engineer`,
`/software-design-document`, and `/demo-video` there. Codex-specific
`agents/openai.yaml` metadata does not replace `SKILL.md`.

## Create agent instruction files

The [agent instruction files skill](../skills/agent-instruction-files/SKILL.md)
uses a project description to generate guidance before implementation begins.
Its templates prescribe .NET CLI conventions or Angular/.NET web conventions.
It does not infer guidance from an existing codebase.

Open Codex in the new project directory and invoke:

```text
$agent-instruction-files This is a new library lending web application with an Angular frontend and a .NET API.
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

Start Codex from the consuming project's root. Invoke:

```text
$requirements-engineer Define the requirements for a library lending system with a catalog, member accounts, loans, and returns.
```

Review the L1 capabilities and L2 behaviors, including their acceptance criteria.
The skill writes `docs/specs/L1.md` and `docs/specs/L2.md`, preserving existing
requirement IDs when updating a specification.

Once both levels are present, invoke:

```text
$software-design-document Create detailed feature designs from docs/specs/, including rendered diagrams.
```

The design skill organizes the output by subsystem and feature. Each feature
contains a `README.md` with Overview, Description, Requirements, and Diagrams
sections, plus PlantUML sources and PNG images in a `diagrams/` directory.

Review the designs against the source requirements. Acceptance tests are written
during development, using the L2 traceability convention in the requirements skill.

## Create application demo videos

Open the consuming repository and invoke:

```text
$demo-video Understand this repository and create a captioned demo video for each executable application in docs/demo/.
```

The [demo video skill](../skills/demo-video/SKILL.md) reads source, tests, startup
scripts, and any existing specifications or detailed designs. It discovers web
apps, CLIs, APIs, workers, and native apps, then records real local workflows with
assertions. Missing `docs/specs/` or `docs/detailed-designs/` does not block it.
Name particular applications in the request to narrow the recording scope.

Prepare the application's normal local runtimes and dependencies. The agent
checks capture capabilities and uses isolated demo data. For browser apps it
prefers the repository's Playwright installation and Chromium. Noninteractive
CLI output may be streamed live into a recorded browser display; interactive
terminal and native apps need compatible terminal or desktop capture. A full
FFmpeg installation is only needed when the selected capture/conversion method
requires it; do not assume Playwright's encoder includes ffprobe or MP4 support.

Default output is silent, captioned 1280 × 720 WebM footage, usually two to five
minutes per app, plus a poster and chapters in `docs/demo/README.md`. That README
records the actual setup and rerun commands, demonstrated workflows, substitutions,
and blockers. Recording scripts live in the project's existing test or script
structure, separately from ordinary acceptance runs. There is no universal rerun
command across frameworks.

The skill fixes recording and setup problems. Product repairs require expanded
user scope. If an app cannot run or be captured, it reports the precise blocker
and completes independent apps. Existing successful videos survive failed reruns.

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

For a plugin installation, ask the design skill to render the diagrams using its
bundled helper; the client manages its installation path. The direct commands
below apply to standalone installations.

```sh
python .agents/skills/software-design-document/scripts/render_puml.py docs/detailed-designs
```

Use `python3` if that is the Python 3 executable on the system. For a personal
installation, replace the script path with the installed copy under
`~/.codex/skills/software-design-document/scripts/` (or the chosen installation
destination). For example, with the default personal installation in PowerShell:

```powershell
python "$env:USERPROFILE/.codex/skills/software-design-document/scripts/render_puml.py" docs/detailed-designs
```

Inspect the output images and confirm that every design's relative image links
resolve. The reference templates use PlantUML's bundled C4 library, so they do
not require downloading C4 includes during rendering.

## Updating skills

### Plugin installations

Review the [changelog](../CHANGELOG.md) before updating. Refresh the Codex
marketplace, then reinstall the plugin to refresh its cached bundle:

```sh
codex plugin marketplace upgrade agent-toolkit
codex plugin remove agent-toolkit@agent-toolkit
codex plugin add agent-toolkit@agent-toolkit
```

For Claude Code:

```sh
claude plugin marketplace update agent-toolkit
claude plugin update agent-toolkit@agent-toolkit
```

Start a new session afterward. Treat plugin caches as managed files; keep any
customizations separately rather than editing a cached installation. Authors
must bump the version in both plugin manifests together when publishing changes
so clients recognize a new release. Refreshing a marketplace alone is not the
same as updating an installed plugin.

### Standalone installations

Record the toolkit revision used for an installation with `git rev-parse HEAD`.
Retrieve updates with `git pull --ff-only` from the toolkit checkout, then review
the [changelog](../CHANGELOG.md) and the changes to each installed skill.

Before replacing an installed folder, move it to a backup outside the active
skills directory. Run the installer again with the same destination, then reapply
intentional local changes. Moving the old folder out first prevents obsolete
files from surviving an update. Identical installed skills are left in place.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| `plugin` command is unavailable | Update the client to a version with plugin support, or use standalone installation. |
| Marketplace cannot be found on GitHub | Confirm the repository is accessible and the client's marketplace manifest is published on the default branch. |
| Plugin installed but skills are unavailable | Confirm `agent-toolkit@agent-toolkit` is installed and enabled with the client's `plugin list` command, then start a new session. In Claude use `/agent-toolkit:<skill-name>`. |
| Skills appear twice | Check for standalone copies as well as the plugin; follow the migration steps above. |
| A skill is unavailable | Confirm the installed path ends in `<skill-name>/SKILL.md`, check `/skills`, and restart Codex if discovery has not refreshed. Check for disabled entries under `skills.config` in the Codex configuration. |
| The installer reports a differing destination | Move the existing skill to a backup outside the active skills directory, then rerun with the same destination. |
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
[official Codex skills documentation](https://learn.chatgpt.com/docs/build-skills).
For issues that remain unresolved, follow the [support guide](../SUPPORT.md).
