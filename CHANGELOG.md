# Changelog

Notable changes to Agent Toolkit are recorded here. Pending changes are listed
under **Unreleased** until a release is published.

## Unreleased

### Added

- Agent instruction files skill from Primer, including the web and CLI templates
  and Python generator for `AGENTS.md` and agent-specific pointer files.
- Requirements engineer skill for L1/L2 specifications, Given/When/Then acceptance
  criteria, and acceptance test traceability.
- Software design document skill for feature designs with requirement references
  and C4, class, and sequence diagrams.
- Design writing guidance, diagram templates, a worked example, the PlantUML
  rendering helper, and evaluation scenario definitions.
- Getting-started guide covering installation, diagram setup, updates, and troubleshooting.
- Contribution guidelines, code of conduct, security reporting policy, and support guide.

### Changed

- Expanded the root README with an overview, skill catalog, quick start, workflow
  diagram, and documentation navigation.

### Import notes

The initial skills were copied from the corresponding personal Claude skill
folders. The requirements skill's entrypoint was renamed from `skill.md` to
`SKILL.md`; the imported file contents were preserved. The design evaluation
scenarios reference fixture projects that were not included in the source skill.

The agent instruction files skill was imported from
`primer/.claude/skills/agent-instruction-files/`. Its renderer and templates were
preserved. The instructions now use the installed skill path and identify the
Primer checkout as the place to run template export commands.
