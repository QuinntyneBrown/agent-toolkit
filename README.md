# Agent Toolkit

A version-controlled collection of reusable agent skills, shared references,
and helper scripts for use across projects.

## Skills

| Skill | Purpose |
|-------|---------|
| [Requirements engineer](skills/requirements-engineer/SKILL.md) | Create and maintain L1 and L2 requirements in `docs/specs/`, with acceptance criteria and test traceability. |
| [Software design document](skills/software-design-document/SKILL.md) | Turn L1/L2 requirements into feature design documents in `docs/detailed-designs/`, with C4, class, and sequence diagrams. |

Both skills were imported from the corresponding folders in `~/.claude/skills/`.
Their contents are preserved; the requirements skill's entrypoint was renamed
from `skill.md` to `SKILL.md` to match this repository's convention.

## Use in another project

Copy each desired skill's entire folder from `skills/` into the consuming
project's `.claude/skills/` directory, or into `~/.claude/skills/` for personal
use across projects. Keep the supporting files alongside `SKILL.md` so relative
resource paths continue to work.

The requirements skill produces the specifications used by the design skill.
The design skill includes its writing guide, diagram templates, worked example,
PlantUML rendering script, and evaluation scenarios.

Rendering diagrams requires Python 3 and a PlantUML installation. The renderer
looks for `PLANTUML_JAR`, then `plantuml` on `PATH`, then common JAR locations.
Using a JAR requires Java. Run it from the consuming project's root:

```sh
python .claude/skills/software-design-document/scripts/render_puml.py docs/detailed-designs
```

The files under `evals/` describe evaluation scenarios. The fixture projects
referenced by those scenarios were not bundled with the original skill.

## Repository guidance

Keep each skill in its own folder under `skills/`. Add shared references and
helper scripts only when needed. See [AGENTS.md](AGENTS.md) for repository rules;
project-specific rules belong in each consuming project's `AGENTS.md`.
