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
| Python 3 and, optionally, Playwright with Chromium | Run the mock and design-system checkers (standard library only). Screenshot the mocks at three widths in both themes with the Python `playwright` package or the Playwright CLI (`npx playwright`). |
| Application runtimes and capture tools | Record demos locally. Browser capture prefers Playwright and Chromium; terminal/native apps need compatible capture and WebM encoding tools. Narration also needs ffmpeg and Python with `edge-tts`. |
| Node.js, ffmpeg, a Chromium-based browser, and Python with `edge-tts` | Build narrated videos. The audio generator and video builder run on Node, synthesize narration with `edge-tts`, screenshot slides in headless Chrome or Edge, and encode MP4 files with ffmpeg (libx264 and libass). |

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

The first command registers the marketplace; the second installs all seven skills
as one `agent-toolkit` plugin. Terminal commands use user scope by default. Choose
user scope if Claude's interactive installer prompts for a scope. Start a new
session in the consuming project afterward. Neither a manual clone nor Python is
needed for plugin installation, but the helpers still need the runtime tools
listed above. These GitHub commands require the manifests to be on the repository's
default branch.

In Codex, type `$` and select a skill from Agent Toolkit. Plugin entries may show
the `agent-toolkit:` namespace. In Claude Code, use:

```text
/agent-toolkit:writing-agent-instructions Describe your new project here.
/agent-toolkit:writing-requirements Define requirements for a library lending system.
/agent-toolkit:writing-design-documents Create detailed designs from docs/specs/.
/agent-toolkit:writing-html-mocks Create HTML mocks for every screen and state.
/agent-toolkit:extracting-design-systems Extract the design system from docs/mocks/.
/agent-toolkit:recording-demo-videos Create a demo video for each executable application.
/agent-toolkit:creating-narrated-videos Create a narrated video that explains the loan workflow.
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
        ├── writing-agent-instructions/
        │   ├── SKILL.md
        │   ├── assets/
        │   └── scripts/
        ├── writing-requirements/
        │   ├── SKILL.md
        │   └── agents/openai.yaml
        ├── recording-demo-videos/
        │   ├── SKILL.md
        │   ├── agents/openai.yaml
        │   ├── references/
        │   └── evals/
        ├── writing-design-documents/
        │   ├── SKILL.md
        │   ├── agents/openai.yaml
        │   ├── references/
        │   ├── scripts/
        │   └── evals/
        ├── writing-html-mocks/
        │   ├── SKILL.md
        │   ├── agents/openai.yaml
        │   ├── assets/
        │   ├── references/
        │   ├── scripts/
        │   └── evals/
        ├── extracting-design-systems/
        │   ├── SKILL.md
        │   ├── agents/openai.yaml
        │   ├── assets/
        │   ├── references/
        │   ├── scripts/
        │   └── evals/
        └── creating-narrated-videos/
            ├── SKILL.md
            └── agents/openai.yaml
```

Skills will be available on the next Codex turn. If discovery does not refresh,
restart Codex. In the CLI or IDE, use `/skills` or type `$` to select a skill.

### Standalone Claude Code skills

The same complete folders can be copied into `<project>/.claude/skills/` or
`~/.claude/skills/`. Use `/writing-agent-instructions`, `/writing-requirements`,
`/writing-design-documents`, `/writing-html-mocks`, `/extracting-design-systems`,
`/recording-demo-videos`, and `/creating-narrated-videos` there. Codex-specific `agents/openai.yaml` metadata
does not replace `SKILL.md`.

## Create agent instruction files

The [writing agent instructions skill](../skills/writing-agent-instructions/SKILL.md)
uses a project description to generate guidance before implementation begins.
Its templates prescribe .NET CLI conventions or Angular/.NET web conventions.
It does not infer guidance from an existing codebase.

Open Codex in the new project directory and invoke:

```text
$writing-agent-instructions This is a new library lending web application with an Angular frontend and a .NET API.
```

The skill writes `AGENTS.md` and pointer files for Claude, Gemini, and Copilot.
The guidance stays in `AGENTS.md` so the files do not duplicate project rules.

The generator can also be run directly with Python, without installing the Primer
.NET tool. From the toolkit checkout, use an existing target directory:

```sh
python skills/writing-agent-instructions/scripts/render.py --path /path/to/new-project --archetype cli --prompt "A .NET command-line tool that validates CSV files."
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
$writing-requirements Define the requirements for a library lending system with a catalog, member accounts, loans, and returns.
```

Review the L1 capabilities and L2 behaviors, including their acceptance criteria.
The skill writes `docs/specs/L1.md` and `docs/specs/L2.md`, preserving existing
requirement IDs when updating a specification.

Once both levels are present, invoke:

```text
$writing-design-documents Create detailed feature designs from docs/specs/, including rendered diagrams.
```

The design skill organizes the output by subsystem and feature. Each feature
contains a `README.md` with Overview, Description, Requirements, and Diagrams
sections, plus PlantUML sources and PNG images in a `diagrams/` directory.

Review the designs against the source requirements. Acceptance tests are written
during development, using the L2 traceability convention in the requirements skill.

## Create HTML mocks and extract a design system

Open the consuming repository and invoke:

```text
$writing-html-mocks Create HTML mocks for every page, dialog and notification of this product in every state.
```

The [writing HTML mocks skill](../skills/writing-html-mocks/SKILL.md) reads
`docs/specs/`, `docs/detailed-designs/`, routes, and existing templates when they
exist (none are required), enumerates every page, dialog, and notification plus
the screens every product needs (sign in, password reset, 404, 403, errors,
offline, settings), and writes one static HTML file per screen per state to
`docs/mocks/pages/`, `docs/mocks/dialogs/`, and `docs/mocks/notifications/`.
Every mock shares `docs/mocks/assets/tokens.css` and `ui.css`, works at 360, 768,
and 1280 px, switches between light and dark themes, is keyboard accessible, and
uses real copy. `manifest.json` lists the screens and states; the bundled checker
regenerates the gallery and coverage matrix and fails on missing states, orphan
files, unlabelled controls, placeholder text, or broken links:

```sh
python .agents/skills/writing-html-mocks/scripts/check_mocks.py docs/mocks --write
python .agents/skills/writing-html-mocks/scripts/screenshot_mocks.py docs/mocks
```

Screenshots land in `docs/mocks/.cache/` (never committed) and need the Python
`playwright` package or the Playwright CLI with Chromium. For a plugin
installation, ask the skill to run its helpers; the client manages the path.

Once the mocks are approved, invoke:

```text
$extracting-design-systems Extract the design system from docs/mocks into docs/design-system.
```

The [extracting design systems skill](../skills/extracting-design-systems/SKILL.md)
stops if `docs/mocks/` is missing. Otherwise it harvests every colour, size,
spacing, radius, shadow, and duration the mocks use, normalises them into
`docs/design-system/tokens/tokens.css` (primitive, semantic, and component tiers
with light and dark themes, reduced-motion, high-contrast, and forced-colours
overrides), exports a DTCG `tokens.json`, and writes the component CSS, twelve
foundation pages (colour, typography, spacing, layout with gutters and margins,
elevation, shape, motion, iconography, theming, responsive, accessibility,
content), one HTML page per component with anatomy, variants, sizes, every state
in both themes, responsive rules, theming, WCAG 2.2 AA accessibility notes,
content rules, do/don't, tokens, code, and source mocks, plus pattern pages. Its
checkers verify contrast for every declared token pair in both themes and the
structure of every page:

```sh
python .agents/skills/extracting-design-systems/scripts/check_contrast.py docs/design-system/tokens/tokens.css
python .agents/skills/extracting-design-systems/scripts/check_design_system.py docs/design-system
```

## Create application demo videos

Open the consuming repository and invoke:

```text
$recording-demo-videos Understand this repository and create a narrated, captioned demo video for each executable application in docs/demo/.
```

The [recording demo videos skill](../skills/recording-demo-videos/SKILL.md) reads source, tests, startup
scripts, and any existing specifications or detailed designs. It discovers web
apps, CLIs, APIs, workers, and native apps, then records real local workflows with
assertions. Missing `docs/specs/` or `docs/detailed-designs/` does not block it.
Name particular applications in the request to narrow the recording scope.

Prepare the application's normal local runtimes and dependencies. The agent
checks capture capabilities and uses isolated demo data. For browser apps it
prefers the repository's Playwright installation and Chromium. Noninteractive
CLI output may be streamed live into a recorded browser display; interactive
terminal and native apps need compatible terminal or desktop capture. A full
FFmpeg installation is required to mux the narration and inspect media; do not
assume Playwright's encoder includes ffprobe or MP4 support.

Every demo is voice-narrated. The skill writes the narration as short paragraphs
per chapter, synthesizes them with the free `edge-tts` package using the same
voices as the narrated video skill (`en-US-AndrewMultilingualNeural` for the
narrator and `en-US-AvaMultilingualNeural` for a second speaker; `EDGE_VOICE`
and `EDGE_VOICE_2` override them), holds each caption for at least its clip's
length, and muxes the assembled Opus track into the WebM after capture. If
`edge-tts`, internet access, or ffmpeg is unavailable, the silent recording
stays in staging and the skill reports the remaining commands instead of
delivering it.

Default output is narrated, captioned 1280 × 720 WebM footage, usually two to
five minutes per app, plus a poster, the narration text, and chapters in
`docs/demo/README.md`. That README records the actual setup and rerun commands,
demonstrated workflows, voices, substitutions, and blockers. Recording scripts live in the project's existing test or script
structure, separately from ordinary acceptance runs. There is no universal rerun
command across frameworks.

The skill fixes recording and setup problems. Product repairs require expanded
user scope. If an app cannot run or be captured, it reports the precise blocker
and completes independent apps. Existing successful videos survive failed reruns.

## Create narrated videos

Open the consuming repository and invoke:

```text
$creating-narrated-videos Create a narrated video that explains how the loan workflow is implemented in this repository.
```

The [creating narrated videos skill](../skills/creating-narrated-videos/SKILL.md) produces an explainer
rather than a screen recording. It writes three text files into
`docs/videos/NN-kebab-topic/`: a `script.md` transcript, a `slides.html` deck
whose slides are cued to verbatim phrases in the script, and a `README.md`
outline with objectives, a run sheet, and references. Every path, identifier,
and quote is checked against the repository. If the repository already has a
videos folder or video tooling, the skill follows that convention instead.

Narration is synthesized paragraph by paragraph with the free `edge-tts` Python
package, which needs internet access but no API key, and the measured clip
durations become a timing manifest. The video builder resolves each slide cue
against that manifest, screenshots the deck at 1920 × 1080 in headless Chrome or
Edge, and uses ffmpeg to encode an MP4 with burned-in captions. Install the
package with `python -m pip install edge-tts` using the interpreter named by
`PYTHON`; `EDGE_PATH` and `FFMPEG_PATH` point the builder at a browser or
ffmpeg that is not on `PATH`. Behind a TLS-intercepting proxy, append the proxy
certificate to Python's `certifi` bundle so `edge-tts` can connect.

The skill expects an audio generator and a video builder under `tools/` in the
consuming repository and describes both so they can be created when missing.
When Node, Python, `edge-tts`, a browser, ffmpeg, or internet access is
unavailable, it still delivers the text files, runs the validation it can, and
lists the remaining commands rather than fabricating media.

## Configure diagram rendering

Install PlantUML using its [local installation guide](https://plantuml.com/starting).
Class and component diagrams use Graphviz; depending on the platform and PlantUML
distribution, a separate Graphviz installation may be needed. See
[PlantUML's Graphviz guidance](https://plantuml.com/graphviz-dot).

The bundled renderer searches in this order:

1. A JAR file identified by `PLANTUML_JAR`.
2. The `plantuml` command on `PATH`.
3. The common JAR locations listed in
   [render_puml.py](../skills/writing-design-documents/scripts/render_puml.py).

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
python .agents/skills/writing-design-documents/scripts/render_puml.py docs/detailed-designs
```

Use `python3` if that is the Python 3 executable on the system. For a personal
installation, replace the script path with the installed copy under
`~/.codex/skills/writing-design-documents/scripts/` (or the chosen installation
destination). For example, with the default personal installation in PowerShell:

```powershell
python "$env:USERPROFILE/.codex/skills/writing-design-documents/scripts/render_puml.py" docs/detailed-designs
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
| `edge-tts` fails with a certificate error | A TLS-intercepting proxy is in use. Append its CA certificate to the file printed by `python -c "import certifi; print(certifi.where())"` and retry. |
| The video builder cannot find a browser | Install Chrome, Edge, or Chromium, or set `EDGE_PATH` (or `CHROME_PATH`) to the executable. |
| A slide cue is not found or not unique | Copy the `data-cue` text verbatim from `script.md`, keep it unique in the script, and keep slides in narration order. |
| The agent-file generator reports a missing template | Restore the skill's `assets/` directory. Regeneration from source requires a Primer checkout, as described in the skill. |
| The agent-file generator reports `Not a directory` | Create the target project directory before running the command. |
| Design-system skill refuses to run | It extracts from `docs/mocks/`; run `writing-html-mocks` first. |
| Mock checker reports missing states | Add the state file or declare it under `not_applicable` with a reason in `manifest.json`; never remove required states. |
| Contrast check fails | Adjust the primitive colour the failing semantic token aliases, keep the token names, and rerun; aim for margin above 4.5:1 and 3:1. |
| Mock screenshots cannot run | Install the Python `playwright` package or run `npx playwright install chromium`; otherwise review the HTML directly and report the remaining command. |
| Agent guidance is truncated | Shorten the description, regenerate, and review the end of `AGENTS.md` for missing guidance. |
| Design generation stops at the requirements gate | Provide both L1 and L2 requirements under `docs/specs/`, with L2 entries tracing to their parent L1. |
| `PlantUML not found` | Check `PLANTUML_JAR`, the `plantuml` command on `PATH`, or a supported JAR location. |
| Java cannot be started | Confirm `java -version` works in the same terminal used for rendering. |
| A diagram has a syntax or layout error | Inspect the generated image and `.puml` source. Run PlantUML directly on that source to see its diagnostic output. |
| A PNG is missing or appears outdated | Confirm the source path passed to the renderer, render again, and inspect the corresponding PNG. |

For discovery behavior, see the
[official Codex skills documentation](https://learn.chatgpt.com/docs/build-skills).
For issues that remain unresolved, follow the [support guide](../SUPPORT.md).
