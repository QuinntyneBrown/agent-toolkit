# Free tools worth knowing about

A catalog of free, publicly available tools and services that quietly replace
paid APIs. The trigger for this list: months of paying Azure Speech for
narration that `edge-tts` produces for free with the same Microsoft neural
voices. Most entries below are the same story in a different domain.

Two kinds of "free" appear here, and the difference matters:

- **Free software** runs on your own machine, forever, with no account. Check
  the license before shipping it in a product: MIT and Apache 2.0 allow
  commercial use; CC-BY-NC and "community" licenses do not.
- **Free tiers** are a vendor's monthly allowance. They are generous enough for
  most internal and documentation work, but limits and terms change, so check
  the current pricing page before relying on one.

Unofficial wrappers around a vendor's consumer endpoint (edge-tts is one) can
stop working without notice and may sit outside the vendor's terms for
commercial use. Use them for internal content and keep an offline fallback.

## Text to speech

| Tool | What it gives you | Caveats |
| --- | --- | --- |
| [edge-tts](https://github.com/rany2/edge-tts) | Microsoft Edge's online neural voices (the same `en-US-*Neural` voices Azure sells) from Python or a CLI. No key, no account. Hundreds of voices and languages; `python -m edge_tts --list-voices`. | Unofficial. Needs internet. No custom SSML, so handle pronunciation with text substitutions. Behind a TLS-intercepting proxy, add the proxy CA to Python's `certifi` bundle. |
| [Kokoro](https://huggingface.co/hexgrad/Kokoro-82M) | An 82M-parameter open-weight model with studio-quality English voices that runs faster than real time on a laptop CPU. Apache 2.0, so commercial use is fine. | English-first; other languages are weaker. |
| [Piper](https://github.com/rhasspy/piper) | Fully offline neural voices in dozens of languages, tiny models, MIT. Good enough for narration when internet is unavailable. | Less natural than Edge or Kokoro voices. |
| [Chatterbox](https://github.com/resemble-ai/chatterbox) | Open-weight, expressive voices with zero-shot voice cloning from a short sample. | Check the repository license and the model card before cloning a real person's voice; get consent. |
| [Dia](https://github.com/nari-labs/dia) | Open-weight dialogue model: multiple speakers, laughs, pauses, from a screenplay-style script. | Needs a GPU for comfortable speed. |
| macOS `say` | Built in. `say -v '?'` lists voices; download the higher-quality Siri voices in System Settings and use them from the shell. | macOS only. |
| Windows SAPI via PowerShell | `Add-Type -AssemblyName System.Speech` gives offline TTS on any Windows machine. | Voices are dated; fine for prototypes and alerts. |
| Browser Web Speech API | `speechSynthesis` in every modern browser, free and offline for prototypes and demos. | Voice set depends on the OS. |
| [Azure Speech F0 tier](https://azure.microsoft.com/pricing/details/speech/) | 0.5 million neural TTS characters per month, free, with SSML and the official SDK. | One concurrent request. Batch is not supported on F0. |
| [Google Cloud Text-to-Speech free tier](https://cloud.google.com/text-to-speech/pricing) | Monthly free characters: 4M Standard, 4M WaveNet, 1M Neural2. | Requires a billing account; usage above the allowance is charged. |

Roughly 150 words per spoken minute means a ten-minute narration is about
1,500 words or 9,000 characters. Even the vendor free tiers cover dozens of such
videos per month; edge-tts covers an unlimited number.

## Speech to text

This is the direction where the biggest savings usually hide: cloud
transcription is billed per audio hour, and the open models are now as accurate
as the paid ones for clear English.

| Tool | What it gives you | Caveats |
| --- | --- | --- |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | OpenAI's Whisper models, open source and offline, reimplemented on CTranslate2 for 4x the speed and a fraction of the memory. Transcribes, translates, and emits SRT/VTT. | The largest model wants a GPU; `small` and `medium` are fine on CPU for batch jobs. |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | Whisper in plain C/C++ with no Python. Runs on phones, Raspberry Pi, and Apple Silicon with Core ML. | Same model family as above; no diarization built in. |
| [WhisperX](https://github.com/m-bain/whisperX) | Whisper plus word-level timestamps and speaker diarization. The missing piece for accurate captions. | Diarization uses pyannote weights, which require accepting a gated license on Hugging Face. |
| [NVIDIA Parakeet](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2) | Open-weight English ASR that tops accuracy leaderboards and transcribes an hour of audio in seconds on a GPU. CC-BY-4.0. | English-focused; the multilingual Canary models cover more languages. |
| [Vosk](https://alphacephei.com/vosk/) | Lightweight offline recognition with 50 MB models and streaming support in many languages. Apache 2.0. | Lower accuracy than Whisper; ideal for command recognition and embedded devices. |
| Windows Live Captions and Voice Access | Built into Windows 11: real-time captions for any audio and voice control, offline, free. | Not scriptable as an API. |
| Browser Web Speech API | `SpeechRecognition` in Chrome gives free dictation for web prototypes. | Chrome sends audio to Google; not offline, not for sensitive content. |
| [Azure Speech F0 tier](https://azure.microsoft.com/pricing/details/speech/) | 5 audio hours per month of real-time transcription, free. | Batch transcription is not included on F0. |

## Hugging Face

Hugging Face is far more than a model download site. A free account gets:

- **The Hub.** Millions of models and datasets with git-based versioning, model
  cards, and 100 GB of private storage. Browse by task (`text-to-speech`,
  `automatic-speech-recognition`, `image-segmentation`) to find the current
  best open model for a job.
- **Spaces.** Host a Gradio or Streamlit demo on a free CPU container, or try
  other people's demos in the browser before installing anything. Most new
  models ship with a Space, so you can test a TTS voice on your own text in
  seconds.
- **ZeroGPU.** Spaces that borrow shared H200 GPUs on demand. Free accounts
  get a small daily quota, enough to try heavyweight models without owning a
  GPU.
- **Inference Providers.** One API and one token routed to many hosted
  inference vendors. The free monthly credit is small, but it is enough to
  evaluate a model before deciding where to run it.
- **Libraries.** `transformers`, `diffusers`, `datasets`, `sentence-transformers`,
  `accelerate`, and `peft` are all Apache 2.0 and run locally with no account.
- **Leaderboards and Arenas.** Community-run comparisons such as the TTS Arena
  and the Open ASR Leaderboard answer "which free model is best right now"
  better than any vendor page.
- **Datasets and courses.** Public datasets for evaluation and fine-tuning,
  and free courses on NLP, audio, and diffusion.

Caveats: a gated model still requires accepting its license on the model page;
free Spaces sleep after inactivity; and the hosted inference credit is for
evaluation, not production.

## Local language models and embeddings

| Tool | What it gives you | Caveats |
| --- | --- | --- |
| [Ollama](https://ollama.com/) | One-command local LLMs (Llama, Gemma, Qwen, Mistral, Phi) with an OpenAI-compatible API on localhost. | Quality tracks your hardware; 8B models run on a laptop, 70B needs a workstation. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | The engine under Ollama, with GGUF quantization for small memory footprints. | Lower level; use Ollama unless you need control. |
| [sentence-transformers](https://www.sbert.net/) | Free local embeddings for search and clustering, replacing per-token embedding APIs. | Pick a model from the MTEB leaderboard for your language. |
| [LM Studio](https://lmstudio.ai/) | Desktop app for running local models with a chat UI and local server. | Free for personal use; check the terms for business use. |

## Translation and OCR

| Tool | What it gives you | Caveats |
| --- | --- | --- |
| [Argos Translate](https://github.com/argosopentech/argos-translate) and [LibreTranslate](https://libretranslate.com/) | Offline neural translation and a self-hostable API with the same interface as paid services. | Quality below DeepL and Google for nuanced text. |
| [DeepL API Free](https://www.deepl.com/pro-api) | 500,000 characters per month of the best machine translation available. | Requires a card for identity, no charge; a monthly cap. |
| [Tesseract](https://github.com/tesseract-ocr/tesseract) | The standard offline OCR engine, 100+ languages, Apache 2.0. | Needs clean, upright scans; preprocess with ImageMagick. |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Modern OCR with layout and table detection, strong on multilingual and photographed text. | Heavier install. |
| Apple Vision and Windows OCR | Both operating systems ship OCR you can call from Swift/Python (`VNRecognizeTextRequest`) or WinRT (`Windows.Media.Ocr`). Fast and surprisingly accurate. | Platform-bound. |

## Audio and video processing

| Tool | What it gives you | Caveats |
| --- | --- | --- |
| [FFmpeg](https://ffmpeg.org/) | Encode, mux, cut, caption (`ass`/`subtitles` filters), loudness-normalize (`loudnorm`), generate silence, probe durations. Replaces most paid media APIs. | Build with libx264, libopus, libass for the full workflow. |
| Headless Chrome or Chromium | `--screenshot` and `--dump-dom` turn any HTML into pixel-perfect 1920x1080 frames, which is how the video-creator skill renders slides. Playwright bundles a copy. | Pin `--window-size` and device scale factor for deterministic output. |
| [Playwright](https://playwright.dev/) video | Records a WebM of a browser session for free; the demo-video skill builds on it. | Video only; add narration with FFmpeg afterward. |
| [Demucs](https://github.com/facebookresearch/demucs) | Separate vocals, drums, bass, and other stems from any track. MIT. | GPU recommended for long tracks. |
| [Audacity](https://www.audacityteam.org/) | Full audio editor with noise reduction and batch macros. | Desktop GUI; scripting via mod-script-pipe. |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Download media and subtitles from hundreds of sites for offline analysis. | Respect each site's terms and copyright. |
| [HandBrake](https://handbrake.fr/) | Batch transcoding presets with a GUI and CLI. | FFmpeg underneath; use FFmpeg directly for automation. |
| [Remotion](https://www.remotion.dev/) | Programmatic video from React components. | Free for individuals and small companies; a company license above that. |
| [Manim](https://www.manim.community/) | Mathematical and explanatory animations from Python. | Steep learning curve. |

## Images and assets

| Tool | What it gives you | Caveats |
| --- | --- | --- |
| [rembg](https://github.com/danielgatis/rembg) | Offline background removal, the free equivalent of remove.bg. | Fine edges (hair) are weaker than paid services. |
| [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | Upscale and restore images and video frames offline. | GPU for speed. |
| [ImageMagick](https://imagemagick.org/) and [sharp](https://sharp.pixelplumbing.com/) | Resize, convert, composite, and optimize in batch. | sharp is the faster choice in Node. |
| [Squoosh](https://squoosh.app/) | In-browser image compression with modern codecs; nothing is uploaded. | Manual, one image at a time; use its CLI for batches. |
| [Lucide](https://lucide.dev/), [Heroicons](https://heroicons.com/), [Tabler Icons](https://tabler.io/icons) | Thousands of consistent MIT-licensed icons. | Mixing sets looks inconsistent; pick one. |
| [Google Fonts](https://fonts.google.com/) and [Fontsource](https://fontsource.org/) | Open-licensed fonts, self-hostable via npm. | Check each font's license (most are OFL). |
| [Openverse](https://openverse.org/), [Unsplash](https://unsplash.com/), [Pexels](https://www.pexels.com/) | Free photos and illustrations with clear licenses. | Attribution rules vary by source. |

## Diagrams and documents

| Tool | What it gives you | Caveats |
| --- | --- | --- |
| [PlantUML](https://plantuml.com/) and [Mermaid](https://mermaid.js.org/) | Text-defined diagrams that live in git. GitHub renders Mermaid inline. | PlantUML needs Java; Mermaid needs Node or a browser. |
| [Kroki](https://kroki.io/) | One HTTP endpoint that renders PlantUML, Mermaid, Graphviz, D2, and twenty other diagram languages. Self-hostable. | The public instance is best-effort. |
| [draw.io](https://www.drawio.com/) and [Excalidraw](https://excalidraw.com/) | Free diagram editors that save as editable SVG or PNG. | draw.io files are XML; keep them in the repo. |
| [Pandoc](https://pandoc.org/) | Convert Markdown to DOCX, PDF, EPUB, and slides. | PDF output needs a LaTeX or HTML engine. |
| [Marp](https://marp.app/) | Slide decks from Markdown, exported to PDF, PPTX, and HTML. | Limited layout control compared with hand-written HTML. |

## Hosting, networking, and CI

| Tool | What it gives you | Caveats |
| --- | --- | --- |
| [GitHub Actions](https://docs.github.com/actions) and [GitHub Pages](https://pages.github.com/) | Unlimited CI minutes for public repositories, a monthly allowance for private ones, and free static hosting. | Private-repo minutes are capped by plan. |
| [Cloudflare Pages, Workers, and R2](https://developers.cloudflare.com/) | Free static hosting, a generous daily request allowance for serverless functions, and object storage with no egress fees. | Free tier CPU-time limits apply per request. |
| [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) | Expose a local service on a public HTTPS URL without opening ports. | Quick tunnels are temporary; named tunnels need a domain on Cloudflare. |
| [Tailscale](https://tailscale.com/) | A private network across your devices in minutes, free for personal use. | Device and user limits on the free plan. |
| [Oracle Cloud Always Free](https://www.oracle.com/cloud/free/) | Permanent free virtual machines, including ARM instances with several cores and gigabytes of RAM. | Capacity in popular regions is often unavailable; idle instances can be reclaimed. |
| [Supabase](https://supabase.com/) and [Neon](https://neon.tech/) | Hosted Postgres with free projects for prototypes. | Free projects pause after inactivity. |
| [Let's Encrypt](https://letsencrypt.org/) | Free, automated TLS certificates. | 90-day lifetime; automate renewal. |

## How to check before paying

1. Search the Hugging Face Hub for the task name and sort by trending; read
   the top model's license.
2. Search GitHub for `<vendor product> free` or `<task> offline`; a maintained
   open equivalent usually exists.
3. Read the vendor's pricing page for a free tier (F0, "always free",
   "hobby") before creating a paid resource.
4. Estimate monthly volume in the unit the vendor bills (characters, audio
   hours, requests). Documentation workloads are usually far below free-tier
   limits.
5. Keep an offline fallback for anything unofficial.
