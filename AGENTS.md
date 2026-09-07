## Project Overview

Agent Toolkit is a version-controlled collection of reusable agent skills,
shared references, and helper scripts for use across projects.

## Speed Is Not the Goal

Quality and completeness beat finishing fast. Finish the whole task - edge cases,
error paths, no stubs or `TODO`s. If it is bigger than it looked, complete it and
say what it cost rather than quietly narrowing scope.

## Folder Structure

```text
agent-toolkit/
├── README.md
├── AGENTS.md
├── skills/
│   └── <skill-name>/
│       └── SKILL.md
├── references/
└── scripts/
```

Keep each skill in its own folder. Add references and scripts only when needed.
This AGENTS.md governs work on this repository; project-specific rules belong
in each consuming project's AGENTS.md.
