# Browser recording

Use for web applications. Prefer the repository's installed Playwright version
and existing page objects. Add a separate recording configuration rather than
changing normal acceptance-test pacing, timeouts, or video policy.

## Configure the take

Use one worker, no parallel stories that share state, and zero automatic retries.
Defaults to adapt to the existing configuration:

```ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './demo',
  fullyParallel: false,
  workers: 1,
  retries: 0,
  timeout: 12 * 60_000,
  expect: { timeout: 30_000 },
  outputDir: './test-results/demo',
  use: {
    browserName: 'chromium',
    viewport: { width: 1280, height: 720 },
    video: { mode: 'on', size: { width: 1280, height: 720 } },
    launchOptions: { slowMo: 120 },
    actionTimeout: 30_000,
    navigationTimeout: 30_000,
    trace: 'retain-on-failure',
  },
});
```

Set the verified local base URL and startup commands for the consuming repository.
Use per-run output directories if concurrent invocations are possible. With the
library API rather than Playwright Test, explicitly implement the total deadline
and assertion timeouts as well as page action/navigation timeouts. If a device
preset is spread into configuration, apply the desired viewport afterward.

Record successful runs with `video: 'on'`; failure-only and retry-only video
settings cannot produce the intended deliverable. Set both viewport and video
size to avoid Playwright's default downscaling. Await browser-context closure
before reading or exporting the completed file. These requirements follow the
[Playwright video guide](https://playwright.dev/docs/videos).
Retain `page.video()` before closing, then use its awaited `saveAs()` to export
to staging; see the [Video API](https://playwright.dev/docs/api/class-video).
Keep long take budgets separate from step deadlines as described in
[Playwright timeouts](https://playwright.dev/docs/test-timeouts).

## Make the story readable and truthful

- Implement a small project-local narration helper for opening/chapter cards,
  captions, quiet intervals, and timestamp events. Use text nodes or `textContent`
  for caption strings, scoped styles, and `pointer-events: none`. Reapply overlays
  after full navigation. Keep narration isolated from application source and
  avoid changing layout or behavior to hide defects.
- Allow roughly 3–8 seconds for ordinary short captions, longer for more text.
  Prefer short captions and quiet moments to covering the product continuously.
  Scroll important content into view and clear overlays when they obscure it.
- Wait for actual UI state and assert results. For meaningful images, wait until
  `complete` is true and `naturalWidth > 0`, then inspect their appearance. Use
  appropriate load/playback checks for other media rather than attribute checks.
- Seed prerequisites through authorized local APIs or fixtures. Perform actions
  that the narration attributes to the user through the UI. Do not route product
  APIs to invented responses or inject state to bypass a demonstrated rule.
- Keep the main story in one recorded page. Playwright produces separate videos
  for separate pages; switching to a popup will not move its footage into the
  original video's stream. Adapt the story to the main page when truthful, or use
  whole-window capture if multiple windows are essential. Do not silently omit
  those interactions or pretend separate page videos are one continuous take.

## Finalize and review

Start chapter timing at capture start, not at the start of setup or the test.
Browser wall-clock events may have an offset from the encoded timeline: compare
visible title cards with playback and correct that offset before publishing.

Validate the finalized file using a local browser video player or available media
tools. Seek through the beginning, chapters, important outcomes, and ending, and
watch transitions at normal speed. Read duration and native video dimensions from
the decoded media. If using browser decoding, serve the video locally with seek
support, wait for `loadedmetadata` and each `seeked` event, and draw a decoded frame
to a canvas for a poster. Document the extraction method in the rerun script.

An available full FFmpeg build may also extract posters and inspect media. Do not
assume Playwright's bundled encoder provides ffprobe, arbitrary decoding, or MP4
encoding. WebM is the default; add a converter only when a requested output format
requires it. A poster captured from the live page must not be described as an
extracted video frame.
