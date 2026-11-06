# Motion upgrade and Katana: research and proposal, 2026-11-06

> **Status.** Direction from James (2026-11-06): redo the three courses
> properly, with motion animation, made with Claude (Opus 5.5). The detail
> below is a proposal. It does not change the gate, the sign-off rules in
> CLAUDE.md §1, or any queue in `JamesLiuZX/command`. Open decisions are in
> §7. Portfolio context: `plans/2026-11-06-strategy-brief.md` in the command
> repo.

---

## 1. What "Opus 5.5 makes videos" actually means

Opus 5.5 does not output video. It writes code that draws every frame, a
headless browser captures the frames, and ffmpeg encodes them. That suits
motion graphics and explainers, not live footage.

This repo already works that way: lecture source becomes HTML slides,
Chromium renders them, ffmpeg joins them with narration. Motion is therefore
an extension of `render.py` and `video.py`, not a new system.

## 2. Sequencing: v1 ships first, motion lands as v2

- v1 (designed stills plus Kokoro `af_heart` narration) is fully rendered.
  It is blocked only by the items in CLAUDE.md §10: sign-offs, screenshots,
  B10 and B11, title lengths. **Motion must not join that list.** A course
  that is 100% animated and unsubmitted earns less than a v1 that is live.
- Udemy lets instructors update lectures in a published course, so motion
  can replace lectures section by section after launch.
- v2 order:
  1. Promo video.
  2. The free previews: ai-for-pms `0.1`, `0.3` and `4.1`. They sell the
     course.
  3. The lectures with the most diagram content.

## 3. What motion is for: teaching, not decoration

Use motion only where it carries the argument:

1. **Reveal in step with narration.** An element appears as the narrator
   reaches it, instead of all bullets landing at once.
2. **Emphasis shifts.** Colour one thing and grey the rest. This is already
   the chart rule in CLAUDE.md §6, animated as a focus move.
3. **Flows that draw in.** Mermaid nodes and edges appear in reading order.
4. **Charts that build.** Marks enter in data order, and each value is
   labelled as it lands. There is still no hover layer (CLAUDE.md §6).
5. **Before and after.** A weak prompt or spec transforms into the fixed one.

Never use bounce or elastic easing, decorative particles, camera shake, or
the dark-neon look (rejected in CLAUDE.md §5). Keep eases short (200 to
400 ms). The eyebrow and heading never move between cuts (top-aligned rule).

Anything with labels, numbers or factual structure stays generated from data
(docs/09 §1). Motion code animates the pipeline's own HTML and SVG, so it
cannot mangle a label the way a generative model can.

## 4. Tooling options

| Option | What it is | Fit for this repo | Cost |
| --- | --- | --- | --- |
| **A. Extend `render.py`** (recommended for lectures) | Pause the slide's CSS and Web Animations, seek them to each frame's time, screenshot from the existing slide HTML, encode per slide | Keeps the PyYAML-only, ffmpeg-and-Chromium rule. Keeps `deck.css`. Keeps the TTS cache. | Free; render time only |
| **B. HyperFrames** (HeyGen, Apache 2.0) | HTML, CSS and GSAP rendered to MP4 by headless Chrome and FFmpeg. Ships 21 agent skills: `npx skills add heygen-com/hyperframes`. Workflows include motion graphics, Figma-to-motion and product intros. | Best outside the lecture pipeline: promo video, cold opens, section intros, LinkedIn clips | Free, no per-render fees; adds a Node dependency |
| C. Remotion Agent Skills | React video framework. Official skills: `npx skills add remotion-dev/skills`. Remotion also maintains a Claude Code plugin. | Mature, but React plus Node is the dependency tree this repo avoids on purpose | Check Remotion's licence terms before commercial use |
| D. claude.ai's built-in video-making skill | Render guidance inside the chat app | One-off clips from a phone, nothing systematic | Free |

### Option A, sketch for the pilot session

1. **Cues.** Add a cue marker inside `@narrate` at each reveal step.
   Synthesise each segment separately. The cache is keyed by spoken text, so
   segments cache independently, and their durations become the reveal
   timestamps.
2. **Steps.** In the slide HTML, give each revealable element a step index
   and a paused CSS animation. For a frame at time t, set each animation's
   `currentTime` from the cue table, then screenshot.
3. **Encoding.**
   - Encode one file per slide at 30 fps, with identical size, frame rate
     and encoder settings everywhere.
   - Join them with the concat demuxer and `-c copy`, then add sound with
     `-c:v copy`. Put any crossfade inside a slide's file.
   - Write to a temporary name ending in `.mp4`, and rename it when ffmpeg
     exits 0.
   - Use JPEG screenshots at quality 92 for filmed frames.
4. **Render budget.** 8.2 h at 30 fps is about 885,000 frames. Render only
   the frames inside transitions, and hold stills between cues as a looped
   frame. Estimate the time on the pilot before you commit a course.
5. **Gate.** Add a `--release` check that the duration of every animated
   lecture matches its narration within a frame.

Pilot suggestion: **ai-for-pms `0.3` (the one idea)**. It is a free preview
and has two figure or mermaid blocks, so it tests every motion type above on
the lecture that most affects sales.

## 5. Katana (Higgsfield): what it is and where it fits

**What it is.** Katana is a Higgsfield skill for Claude, launched around
2026-10-08.
- It rebuilds a reference video edit with up to five photos of your own
  characters, products or clothing.
- It runs through the Higgsfield MCP connector, on the same account and
  credits as higgsfield.ai.
- Its presets are personalised edits, style transfer and motion transfer.
- In Claude, `/katana` opens the preset catalogue.

**Verdict for this repo.**
- **Not for lectures.** Its output is generated video. docs/09 bars
  generated visuals from anything carrying labels, numbers or structure, and
  generated video cannot be rebuilt from source after a script edit.
- **Allowed lanes.** These are the docs/09 §1 lanes:
  - Specimens in `ai-ugc-ads`. Katana is itself an AI UGC and edit tool.
  - Text-free atmosphere.

  A Katana lecture or update in ai-ugc-ads would be a tool lecture, so it
  needs real screenshots from James's account (`[SCREENSHOT-NEEDED]`) and a
  `freshness_watch` entry. That is a curriculum change and James's call.
- **Promo video.** Katana could supply b-roll at most. docs/08 still asks
  for the promo in James's real voice.
- **Cost.**
  - Katana needs a paid plan. MCP is not on the free plan, and the free plan
    excludes commercial use.
  - Every MCP generation spends credits, even on unlimited plans.
  - In September 2026, Starter was about 19 USD a month, billed annually,
    for 270 credits.

## 6. Udemy facts rechecked on 2026-11-06

These are consistent with CLAUDE.md §1 and docs/08:

- **AI policy.**
  - AI-generated visuals and animations are permitted if they are high
    quality and clearly relevant to the audio instruction.
  - Quality text-to-speech is accepted.
  - AI use must be disclosed in the course description.
  - Courses that are entirely AI-generated are declined.
- **Merger.** Coursera completed its all-stock combination with Udemy on
  2026-05-11. Instructor agreements, economics and support structures were
  unchanged at close, and integration is still ahead. Re-check terms before
  launch.
- **Revenue share.** Unchanged from docs/08: 97% on own coupon or referral
  links, 37% organic, and a 15% subscription pool since January 2026.

## 7. Decisions for James

1. Should v1 ship first, with motion as a v2 upgrade? Recommended: yes.
2. Which tooling? Recommended: Option A for lectures, and Option B for the
   promo video and LinkedIn clips.
3. Should the pilot lecture be ai-for-pms `0.3`, or another lecture?
4. Should ai-ugc-ads get a Katana tool lecture or update? It needs
   screenshots from your account.
5. Voice stays as you decided (Kokoro `af_heart`, TTS with the disclosure
   line). Re-check Udemy's AI narration policy before upload, as in CLAUDE.md
   §10, item 5.

## Sources

- Opus 5.5 video is code-generated: https://blog.laozhang.ai/en/posts/claude-opus-5-5-video-generation
- HyperFrames: https://themenonlab.blog/blog/heygen-hyperframes-video-as-code (repo github.com/heygen-com/hyperframes) and workflows: https://aiidelist.com/blog/opus-5-5-motion-design
- Remotion skills and plugin: https://www.remotion.dev/docs/ai/skills, https://remotion.dev/docs/ai/claude-code-plugin
- Katana: https://higgsfield.ai/blog/higgsfield-katana, https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-use-katana, release date: https://thepostflow.com/?p=9453
- Higgsfield MCP plans and credits: https://creatify.ai/fr/blog/what-is-higgsfield-mcp-what-it-does-what-it-costs-and-how-to-use-it, https://www.layer3labs.io/guides/higgsfield-mcp
- Udemy AI checklist: https://support.udemy.com/hc/en-us/articles/30999984483607-Course-Quality-Checklist-Use-of-AI
- Udemy disclosure and fully AI-generated rule: https://support.udemy.com/hc/sections/360001167193-Course-Material-Basics
- Coursera and Udemy merger: https://edtechinnovationhub.com/news/coursera-and-udemy-complete-merger-but-platform-integration-still-lies-ahead
- Udemy revenue share: https://support.udemy.com/hc/articles/229605008-Instructor-revenue-share, https://udemy.gcs-web.com/node/9001/html
