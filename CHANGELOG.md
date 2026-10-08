# Changelog

Notable changes to Agent Toolkit are recorded here. Pending changes are listed
under **Unreleased** until a release is published.

## Unreleased

### Added

- Video creator skill for narrated slide-deck videos: a transcript, a cued
  HTML slide deck, and an outline in `docs/videos/`, synthesized with free
  `edge-tts` narration and encoded as a captioned 1080p MP4 with headless
  Chrome and ffmpeg, with Codex UI metadata.
- Demo video skill for repository discovery and verified local recordings of web,
  CLI, API, worker, and native applications, with captions, posters, chapters,
  reproducible commands, capture references, and evaluation scenarios.
- Codex and Claude Code plugin manifests and repository marketplaces packaging
  all three skills as `agent-toolkit` version `0.1.0`.
- Marketplace installation, updates, and standalone migration instructions.
- Agent instruction files skill from Primer, including the web and CLI templates
  and Python generator for `AGENTS.md` and agent-specific pointer files.
- Codex UI metadata for the requirements and design skills and a verified,
  non-overwriting local installer at `scripts/install_skills.py`.
- Requirements engineer skill for L1/L2 specifications, Given/When/Then acceptance
  criteria, and acceptance test traceability.
- Software design document skill for feature designs with requirement references
  and C4, class, and sequence diagrams.
- Design writing guidance, diagram templates, a worked example, the PlantUML
  rendering helper, and evaluation scenario definitions.
- Getting-started guide covering installation, diagram setup, updates, and troubleshooting.
- Contribution guidelines, code of conduct, security reporting policy, and support guide.

### Changed

- Renamed all five skills to consistent gerund-form names following the
  [skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#naming-conventions),
  and advanced both plugin manifests to `0.4.0`. Folder names, frontmatter
  names, Codex display names, example prompts, evaluation metadata, and
  documentation were updated together. Standalone installs under the old
  folder names should be removed before reinstalling; plugin installs pick up
  the new names on upgrade. Invoke the skills by their new names:

  | Previous name | New name |
  | --- | --- |
  | `agent-instruction-files` | `writing-agent-instructions` |
  | `requirements-engineer` | `writing-requirements` |
  | `software-design-document` | `writing-design-documents` |
  | `demo-video` | `recording-demo-videos` |
  | `video-creator` | `creating-narrated-videos` |

- The demo video skill now requires edge-tts voice narration using the same
  narrator and second-speaker voices as the video creator skill, synthesized
  before capture, timed to the captions, and muxed into the WebM as an Opus
  track; ffmpeg and Python with `edge-tts` are now demo prerequisites, and a
  narration-unavailable evaluation scenario was added.
- Advanced both plugin manifests to `0.3.0` and expanded the catalog, setup
  guidance, and troubleshooting table to include all five skills.
- Advanced both plugin manifests to `0.2.0` and expanded the catalog and setup
  guidance to include all four skills.
- Made plugin marketplace installation the primary quick start for Codex and
  Claude Code, retaining the standalone Python installer as an alternative.
- Made Codex installation and `$skill-name` invocation the primary setup path.
- The design requirements gate now recognizes plain `L1-001` / `L2-001` IDs
  produced by requirements-engineer, with a search usable in PowerShell.
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

The video creator skill was imported from
`saturdaze/.agents/skills/video-creator/SKILL.md`. Its workflow, file formats,
and tooling description were preserved. The description now distinguishes it
from the demo video skill, and the tooling example no longer names that
product or assumes its scripts exist; it links to the Saturdaze implementation
as a reference instead. The Node tools and shared slide assets were not
bundled because they carry that product's branding and pronunciation lexicon.
