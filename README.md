# Agent Toolkit

**Reusable agent skills for project guidance, requirements, and technical design.**

Agent Toolkit packages engineering workflows as version-controlled instructions,
references, and helper scripts. Use the skills across projects to establish coding
conventions, define system behavior, and produce design documents with diagrams
that trace back to testable requirements.

[Getting started](docs/getting-started.md) ·
[Available skills](#available-skills) ·
[Contributing](CONTRIBUTING.md) ·
[Support](SUPPORT.md) ·
[Changelog](CHANGELOG.md)

## Overview

- **Project guidance.** Generate `AGENTS.md` and agent-specific pointer files from
  a description of a new project using the bundled web or CLI conventions.
- **Traceable requirements.** Capture high-level capabilities (L1) and detailed
  behaviors (L2), with Given/When/Then acceptance criteria.
- **Consistent design documents.** Organize designs by subsystem and feature,
  with a shared writing style and explicit links to source requirements.
- **Diagrams alongside the design.** Author C4, class, and sequence diagrams in
  PlantUML and render PNG images for inline viewing on GitHub.
- **Portable skill folders.** Keep each skill's instructions and supporting
  resources together so they can be copied into a consuming project.

## Available skills

| Skill | Use it to | Output in the consuming project |
| --- | --- | --- |
| [Agent instruction files](skills/agent-instruction-files/SKILL.md) | Establish guidance for a new .NET CLI or Angular/.NET web project from its description. | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md` |
| [Requirements engineer](skills/requirements-engineer/SKILL.md) | Create and maintain L1/L2 requirements, acceptance criteria, and test traceability. | `docs/specs/L1.md` and `docs/specs/L2.md` |
| [Software design document](skills/software-design-document/SKILL.md) | Develop feature designs from existing requirements, including components and rendered diagrams. | `docs/detailed-designs/{subsystem}/{feature}/` |

The design skill requires existing L1 and L2 requirements under `docs/specs/`.
The requirements skill establishes the acceptance criteria used during development.

```mermaid
flowchart LR
    L1["L1: High-level requirements"] --> L2["L2: Detailed requirements"]
    L2 --> Design["Feature designs and diagrams"]
    L2 --> Tests["Acceptance tests during development"]
```

## Quick start

### Install in Codex

Run these commands in a terminal with Git and a Codex CLI that supports `plugin`:

```sh
codex plugin marketplace add QuinntyneBrown/agent-toolkit
codex plugin add agent-toolkit@agent-toolkit
```

### Install in Claude Code

Run these commands in a terminal with Git and Claude Code:

```sh
claude plugin marketplace add QuinntyneBrown/agent-toolkit
claude plugin install agent-toolkit@agent-toolkit
```

Or run the equivalent commands inside Claude Code:

```text
/plugin marketplace add QuinntyneBrown/agent-toolkit
/plugin install agent-toolkit@agent-toolkit
```

For either client, the first command registers the marketplace and the second
installs one plugin containing all three skills. Terminal commands default to
user scope; choose user scope if Claude's interactive installer asks. Start a
new session in your consuming project after installation. GitHub installation
requires the marketplace files to be published on this repository's default branch.

See the [installation guide](docs/getting-started.md#install-the-skills) for
updates, local checkout testing, and switching from manually copied skills.

### Use the skills

1. Open Codex in the consuming project. For a new project, establish its agent guidance:

   ```text
   $agent-instruction-files This is a new library lending web application with an Angular frontend and a .NET API.
   ```

2. Define the requirements:

   ```text
   $requirements-engineer Define the requirements for a library lending system with a catalog, member accounts, loans, and returns.
   ```

3. Once the L1/L2 requirements are ready, invoke the design skill:

   ```text
   $software-design-document Create detailed feature designs from docs/specs/, including rendered diagrams.
   ```

Codex supports explicit skill mentions and automatic selection from descriptions.
See the [official skills documentation](https://learn.chatgpt.com/docs/build-skills).
In Codex, type `$` and select the skill from the Agent Toolkit plugin; plugin
entries may display the `agent-toolkit:` namespace. In Claude Code, invoke the
plugin skills with their namespace:

```text
/agent-toolkit:agent-instruction-files Describe your new project here.
/agent-toolkit:requirements-engineer Define requirements for a library lending system.
/agent-toolkit:software-design-document Create detailed designs from docs/specs/.
```

### Alternative: install standalone skills

To copy the skills into your personal Codex skills directory using Python 3.10
or later:

```sh
git clone https://github.com/QuinntyneBrown/agent-toolkit.git
cd agent-toolkit
python scripts/install_skills.py
```

The installer uses `$CODEX_HOME/skills` when set, otherwise `~/.codex/skills`.
It includes all supporting files and refuses to overwrite differing copies.
Choose either plugin installation or standalone copies to avoid duplicate skills.
Python is not required to install the plugin.

Agent-file generation requires Python 3. Diagram rendering additionally requires
PlantUML and Java when using a PlantUML JAR.
See [diagram setup](docs/getting-started.md#configure-diagram-rendering) for
configuration and platform dependencies.

## Documentation

| Document | What it covers |
| --- | --- |
| [Getting started](docs/getting-started.md) | Installation, usage, diagram rendering, updates, and troubleshooting. |
| [Contributing](CONTRIBUTING.md) | Skill structure, validation, and pull request expectations. |
| [Code of conduct](CODE_OF_CONDUCT.md) | Community standards and how to raise a concern. |
| [Security](SECURITY.md) | Reporting vulnerabilities in the toolkit. |
| [Support](SUPPORT.md) | Usage questions, bug reports, and feature requests. |
| [Changelog](CHANGELOG.md) | Notable changes to skills and documentation. |

## Repository layout

```text
agent-toolkit/
├── .agents/plugins/marketplace.json
├── .codex-plugin/plugin.json
├── .claude-plugin/
│   ├── marketplace.json
│   └── plugin.json
├── skills/
│   ├── agent-instruction-files/
│   │   ├── SKILL.md
│   │   ├── assets/
│   │   └── scripts/
│   ├── requirements-engineer/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   └── software-design-document/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/
│       ├── scripts/
│       └── evals/
├── docs/
│   └── getting-started.md
├── scripts/
│   └── install_skills.py
├── AGENTS.md
└── README.md
```

[AGENTS.md](AGENTS.md) is the source of repository guidance. Project-specific
rules belong in the consuming project's `AGENTS.md`. Shared `references/` and
`scripts/` directories at the repository root are added only when needed.

## Contributing and support

Contributions that improve skill behavior, documentation, and reusable tooling
are welcome. Read the [contribution guide](CONTRIBUTING.md) and
[code of conduct](CODE_OF_CONDUCT.md) before opening a pull request.

For questions and bugs, follow the [support guide](SUPPORT.md). Report security
concerns through the process in [SECURITY.md](SECURITY.md).
