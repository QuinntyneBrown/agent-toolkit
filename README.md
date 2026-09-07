# Agent Toolkit

**Reusable agent skills for software requirements and technical design.**

Agent Toolkit packages engineering workflows as version-controlled instructions,
references, and helper scripts. Use the skills across projects to define system
behavior, write testable requirements, and produce design documents with diagrams
that trace back to those requirements.

[Getting started](docs/getting-started.md) ·
[Available skills](#available-skills) ·
[Contributing](CONTRIBUTING.md) ·
[Support](SUPPORT.md) ·
[Changelog](CHANGELOG.md)

## Overview

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

1. Clone the repository:

   ```sh
   git clone https://github.com/QuinntyneBrown/agent-toolkit.git
   cd agent-toolkit
   ```

2. Copy the desired folders from `skills/` into your project's `.claude/skills/`
   directory, including all supporting files. See the
   [installation guide](docs/getting-started.md#install-the-skills) for PowerShell,
   macOS, Linux, and personal installation instructions.

3. Open Claude Code in that project and invoke the requirements skill:

   ```text
   /requirements-engineer Define the requirements for a library lending system with a catalog, member accounts, loans, and returns.
   ```

4. Once the L1/L2 requirements are ready, invoke the design skill:

   ```text
   /software-design-document Create detailed feature designs from docs/specs/, including rendered diagrams.
   ```

Claude Code supports project and personal skill directories and invocation by
skill name. See the [Claude Code skills documentation](https://code.claude.com/docs/en/skills).

Diagram rendering requires Python 3, PlantUML, and Java when using a PlantUML JAR.
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
├── skills/
│   ├── requirements-engineer/
│   │   └── SKILL.md
│   └── software-design-document/
│       ├── SKILL.md
│       ├── references/
│       ├── scripts/
│       └── evals/
├── docs/
│   └── getting-started.md
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
