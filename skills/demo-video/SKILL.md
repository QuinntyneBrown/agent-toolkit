---
name: demo-video
description: >-
  Create or refresh demo videos of a repository's executable applications.
  Use when asked to record application demos, product walkthroughs, or a video
  for each app. Discover the applications, run them locally, and deliver verified,
  captioned WebM recordings with posters, chapters, and rerun commands.
  Covers web, CLI, API, worker, and native applications; not promotional animation
  or video editing unrelated to running software.
---

# Demo video

Create a watchable demonstration of each executable application: real execution,
readable captions, and verified outcomes. The default is a silent, continuous
successful take at 1280 × 720, roughly two to five minutes per application.
Adjust length to useful workflow coverage rather than padding or rushing it.
Honor a user's requested applications, format, and presentation overrides.

Resolve supporting references relative to this installed skill folder; resolve
application files and `docs/demo/` relative to the consuming repository.

## 1. Understand the repository and identify applications

Read applicable agent instructions, README files, workspace/project manifests,
entrypoints, startup scripts, tests, and existing demo tooling. Read useful content
under `docs/specs/` and `docs/detailed-designs/` when present. Neither directory is
required: infer behavior from source, tests, and runtime inspection when absent.
If documents disagree with the implementation, demonstrate what actually works
and record the discrepancy; do not claim unimplemented requirements.

Inventory every executable application before selecting scenes. Record its
purpose, audience, entrypoint, run command, local endpoint or interaction surface,
dependencies, authentication, and candidate workflows. Count independently
runnable first-party APIs and workers even when a web app also depends on them.
Separate user-facing apps served by one host still deserve separate videos.
Exclude libraries, migrations, test runners, repository maintenance scripts, and third-party
infrastructure unless the user explicitly wants to demonstrate those tools.

Assign stable lowercase hyphenated slugs, preserving established demo names.
Disambiguate duplicate names with their subsystem. Account for every application
as recorded, blocked with a reason, or excluded by the user's scope. A repository
with no executable applications needs an explanation, not an invented demo.

## 2. Choose workflows and the recording method

Build a short storyboard per application: purpose, starting state, actions,
observable assertions, captions, and a useful final state. Prefer complete user
journeys over touring every route or endpoint. Include meaningful validation or
permission behavior when it explains the product. Avoid exposing credentials,
private records, tokens, or sensitive shell history in footage and diagnostics.

Reuse existing acceptance helpers and demo conventions when suitable. Select the
capture method from available tools and the application's real interaction surface:

- Browser UI: read [browser recording](references/browser-recording.md).
- CLI, API, worker, or native UI: read
  [terminal and native recording](references/terminal-native-recording.md).

If apps share data, order their stories by dependency and reuse deterministic
synthetic fixtures. Explain which earlier recording establishes later state.
Provide a command that reproduces the whole sequence from a clean environment;
an individual rerun must prepare its prerequisites or name the required sequence.

## 3. Prepare a reproducible local run

Verify the required runtimes, locked dependencies, capture tools, database,
configuration, and local credentials. Prefer repository setup/build scripts.
Use normal authorized local setup to resolve missing dependencies; if credentials,
platform support, or external access remain unavailable, report exactly what is
needed and continue independent applications.

Use disposable demo storage and synthetic identities. Before any reset or cleanup,
verify the resolved database, directory, or container belongs to this run. Never
inherit a reset-on-start setting against an existing development database. Do not
reuse a listening server unless its identity, configuration, and data isolation
are established; otherwise choose unused ports. Bind demo-only services locally.

Use real application services and persistence where the application requires them.
Existing local adapters for mail, payments, AI, or other external integrations are
acceptable when disclosed. Do not substitute mocked product responses or remove
authentication to make the demo pass. Avoid actual external sends or purchases
without authorization already covering them.

Create application-specific recording scripts in the repository's existing test
or script structure. Keep recordings separate from the ordinary acceptance run
and its commit gates. Give startup, individual actions, the whole take, and
teardown finite timeouts. Check readiness before recording; do not fill the video
with build logs or server startup waits.

Track owned processes and resources from their creation. Enclose startup as well
as recording in cleanup handling so partial setup failures also clean up. On
Windows, launch background helpers hidden. Stop only owned processes, restore
changed environment settings, and report any cleanup failures and resources left.
Keep temporary video, trace, credentials, and logs in an ignored run directory.

## 4. Record and verify

Use readable pacing, a brief opening, chapter transitions, and captions explaining
the user's outcome. Keep captions clear of the controls or output being shown.
Presentation delays are for reading; readiness must use observable conditions.
Assert actual results before narrating that they succeeded: persisted state,
calculated values, loaded media, returned responses, or completed jobs.

Record one continuous successful take per application. For browser capture, keep
the main story in one recorded page. Multiple actors may switch authenticated
sessions within that story without exposing secrets. Do not splice failed scenes
into a successful recording. Disable automatic retries; diagnose a failed take
and re-record it in full after a justified harness or setup correction.

Fix local setup and recording-harness problems within the request. Product bugs
are outside this skill's default repair scope: capture the failing step and
expected versus actual behavior, mark the affected demo blocked, and finish
independent apps. Do not repeatedly retry unchanged failures or weaken assertions.
User authorization for product repairs can expand that scope explicitly.

After capture has finalized, open and inspect the encoded WebM itself. Check
playback, measured duration and dimensions, beginning and ending, each chapter,
caption readability, and important visual outcomes. Sample frames are useful but
do not replace playback review for pacing. Verify media really loaded; an image's
URL or alt text alone is not evidence. Derive chapter times from the recording
timeline, verify them against playback, and choose a representative poster from
the successful footage. A nonempty file is not sufficient validation.

## 5. Deliver artifacts and rerun instructions

Stage each application's video, poster, and chapter metadata outside final paths.
Promote the verified set only after its assertions and video review pass. Back up
existing files and restore them if promotion fails; do not mix an old video with
new chapter times or a new poster. Preserve unrelated demos and manual README
content. If a rerun fails, distinguish any retained prior video from this run.

Default deliverables in the consuming repository:

```text
docs/demo/
├── README.md
├── <app-slug>.webm
└── <app-slug>-poster.png
```

Repeat the video/poster pair for every application. The README must include:

- An application inventory with links, purpose, and recorded/blocked status.
- Measured video duration, dimensions, file size, and linked poster per recording.
- Chapter timestamps and the verified workflows they demonstrate.
- Exact setup and rerun commands, working directories, tool prerequisites,
  configuration variable names, data preparation, and cleanup behavior.
- Recording order, relevant source/test links and revision when available,
  integration substitutions, product limitations, and actionable blockers.

Record the actual commands, not an assumed universal `npm run demo`. Keep secrets
out of documentation. Include reproducible recording sources, but keep transient
logs and failure artifacts out of the deliverable set. Report completion only
when every in-scope application has a reviewed video; otherwise report partial
completion with explicit blockers and links to the successful artifacts.
