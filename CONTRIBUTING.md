# Contributing to Agent Toolkit

Contributions should make a reusable engineering workflow clearer, more reliable,
or easier to apply across projects. Useful changes include focused skill updates,
better examples, corrected references, and improvements to helper scripts.

Read [AGENTS.md](AGENTS.md) for repository rules and
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community expectations.

## Before making a change

Search [existing issues](https://github.com/QuinntyneBrown/agent-toolkit/issues)
for related work. For a substantial new skill or a change to an existing workflow,
describe the use case and expected output in an issue so the scope can be discussed.
Small fixes can be submitted directly as pull requests.

Use [SECURITY.md](SECURITY.md) for vulnerabilities rather than a public bug report.

## Skill structure

Each skill belongs in `skills/<skill-name>/` and has a `SKILL.md` entrypoint.
Use lowercase words separated by hyphens for the folder and skill name. Include
YAML frontmatter with `name` and `description`; the description explains what
the skill does and when it applies.

Keep task-specific references and scripts inside the skill folder. Add them only
when they support the workflow, and reference them from the instructions that
need them. Shared resources belong at the repository root only when multiple
skills need the same material.

Write portable paths and state external tool dependencies. Keep rules specific
to a consuming project in that project's `AGENTS.md`.

The agent instruction skill's templates are exported from Primer. Follow its
[template maintenance instructions](skills/agent-instruction-files/SKILL.md#where-the-guidance-comes-from)
to regenerate them in a Primer checkout and copy the exports here. Keep the
bundled assets aligned with that source.

Codex UI metadata lives in each skill's `agents/openai.yaml`. Keep display names,
descriptions, and `$skill-name` example prompts aligned with the entrypoint.
The local installer copies complete folders without changing their contents.

## Development workflow

1. Fork or clone the repository and create a branch for the change.
2. Read the affected skill and its supporting resources before editing.
3. Make a complete, focused change, including relevant error paths and examples.
4. Update the skill catalog, setup documentation, and changelog when behavior,
   dependencies, or outputs change.
5. Validate the change and describe the results in the pull request.

## Validation

### Plugin releases

The repository root is one plugin shared by both clients. Keep the name
`agent-toolkit` and the same semantic version in `.codex-plugin/plugin.json` and
`.claude-plugin/plugin.json`. Bump both versions for every published plugin
change, including bundled skills and resources. Keep version numbers out of the
marketplace entries so the plugin manifests remain their source of truth.

Both marketplace sources point to `./`; keep all bundled resources inside the
repository. Validate the Claude manifests with:

```sh
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
```

The warning that the repository's `CLAUDE.md` is not loaded as plugin context is
expected: that file is contributor guidance, and the skills supply plugin
instructions. Validate Codex packaging with the plugin-creator skill's validator
when available, and test both clients' local marketplace-add and install flows
in isolated configurations. Confirm all four skills and their supporting files
exist in each installed bundle. Publish the manifests on the default branch
before advertising GitHub installation as tested.

### Checks for changes

Match validation to the change. Documentation edits need working links, readable
Markdown, and commands that match the repository. Skill changes also need a
representative request exercised in a separate sample project.

Before submitting:

- Confirm the skill name matches its directory and the frontmatter is valid YAML.
- Check that referenced resources exist and remain usable after copying the folder.
- Exercise changed scripts, including relevant failure cases, and report the tools
  and inputs used.
- For diagram changes, render the affected templates and inspect the PNG images.
- Check that examples contain no credentials, private project data, or machine-specific
  dependencies presented as universal requirements.
- Review the diff for unfinished content and unrelated changes.

Run the whitespace check after staging the intended changes:

```sh
git diff --cached --check
```

When changing installation behavior, run the isolated installer tests:

```sh
python -B scripts/test_install_skills.py
```

The design skill's [evaluation scenarios](skills/software-design-document/evals/evals.json)
describe expected behaviors. Their named fixture projects were not included in
the original import, and the repository has no bundled evaluation runner. Use
appropriate sample projects and state which scenarios were actually exercised.

The demo skill's [evaluation scenarios](skills/demo-video/evals/evals.json) cover
application discovery, real recordings, failure handling, and resource ownership.
Create the described fixtures in disposable sample projects; no agent evaluation
runner is bundled. Inspect the encoded videos and record actual results separately
from the scenario definitions.
See the [demo validation record](skills/demo-video/evals/validation.md) for the
executed sample and coverage limits.

## Pull requests

Use a title that describes the resulting change. The description should explain
the problem, the new behavior, and how the change was validated. Include a concrete
before-and-after example when it makes a workflow change easier to review.

Link related issues and call out changes to output locations, requirement
conventions, dependencies, or installation steps. Include migration instructions
when existing installations need to be updated differently.

Do not include generated sample-project artifacts unless they are intentional,
documented fixtures or examples maintained by the repository.
