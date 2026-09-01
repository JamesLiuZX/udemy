# MP4 builds — the upload files for all three courses

This branch holds ONLY rendered course videos + captions (regenerable,
gitignored on source branches — kept here so they survive ephemeral build
containers). Built from `main` @ f7672ab with Kokoro-82M `af_heart` (American female, the pack's highest-rated voice — James's ear-test choice 2026-09-01; earlier `bf_emma` and partial `af_sarah` renders remain in this branch's git history)
(production voice per docs/07-tts.md), pushed section-by-section as each
finished rendering.

- `ai-for-pms/` — 102 lectures (12 sections), target ~7.3h audio
- `ai-agents-for-work/` — 76 lectures (12 sections), ~3.4h audio
- `ai-ugc-ads/` — 81 lectures (12 sections), ~5.4h audio

Each folder: one `.mp4` + one `.srt` per lecture (filenames sort in
curriculum order), plus `qc-release.txt` (full release-QC output for that
course) and `manifest.json` from the build.

**Download:** clone just this branch —
`git clone --depth 1 --branch claude/mp4-builds https://github.com/JamesLiuZX/udemy mp4s`
— or use GitHub's "Download ZIP" on this branch.

**Before upload (from docs/PRODUCTION-REPORT.md §6):** your `verified: true`
sign-offs, the flagged screenshots, and the AI-narration disclosure line in
each course description. `ALL-DONE.txt` appears at repo root when every
course has rendered.
