# Security policy

This policy covers security issues in Agent Toolkit's skill instructions,
supporting resources, and helper scripts. Examples include unintended command
execution, disclosure of sensitive data, and file operations outside the intended
working scope caused by toolkit behavior.

## Report a vulnerability

Keep vulnerability details out of public issues and pull requests until a
maintainer has had an opportunity to assess them.

Use the repository's
[Security page](https://github.com/QuinntyneBrown/agent-toolkit/security) to submit
a private report if **Report a vulnerability** is available. If private reporting
is unavailable, [open an issue](https://github.com/QuinntyneBrown/agent-toolkit/issues/new)
containing only a request for a private security contact. Share reproduction steps
and sensitive details after a private channel is established.

## What to include privately

- The affected skill or script and the toolkit commit hash.
- The operating system, agent environment, and relevant tool versions.
- Minimal reproduction steps using synthetic data.
- Expected behavior, observed behavior, and the security impact.
- A proposed fix or mitigation, if available.

Remove credentials, tokens, personal information, and private project content
from examples and logs. If a report involves exposed credentials, redact them
and identify their type and location rather than sending their values.

## Scope and follow-up

Report issues in third-party tools directly to those projects when the toolkit
is not the cause. A report that spans both the toolkit and a dependency should
explain how the toolkit contributes to the issue.

Identify the exact repository revision affected. There is no published support
matrix for older revisions or guaranteed response timeline. Coordinate any public
disclosure with the maintainer handling the report.

For ordinary bugs and usage questions, see [SUPPORT.md](SUPPORT.md).
