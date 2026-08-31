# TTS strategy: off ElevenLabs, onto free-or-cheap production voices

> Decision record, August 2026. ElevenLabs was the default because it led on
> quality; it no longer leads by enough to justify costing an order of
> magnitude more than everything else, and open-weight models now win blind
> tests against it. Prices and policies below decay: re-check before a
> production render, and note the check date here.

---

## 1. The cost picture, at this repo's actual sizes

One full course render is ~10 hours of narration: roughly 90,000 words,
~550,000 characters. Narration is cached by spoken text, so a full-price
render happens about once per course; edits re-spend only on changed lines.

| Option | Cost per full course render | Quality | Notes |
| --- | --- | --- | --- |
| ElevenLabs (old default) | ~$30 to $100+ (credit plans, ~$50+/1M chars effective) | Excellent | The premium no longer buys a clear win |
| **Kokoro-82M local (`kokoro`)** | **$0** | Very good; beats far larger models in blind tests | Apache-2.0, commercial OK. New provider in `tts.py` |
| **OpenAI `gpt-4o-mini-tts` (`openai`)** | **~$8** (~$15/1M chars) | Very good, steerable with voice instructions | Already wired; zero setup beyond `OPENAI_API_KEY` |
| Azure neural voices | ~$8.80/1M, first 500k chars each month free | Very good; has en-GB voices | Effectively free at one course/month; provider not yet wired |
| Google Chirp 3 HD | $30/1M, first 1M chars each month free | Very good | Effectively free monthly; provider not yet wired |
| Chatterbox-Turbo local | $0 | Preferred over ElevenLabs by 65% in blind tests | MIT licence; heavier than Kokoro, wants a GPU |

**Decision: default provider is `kokoro` (free, local, British voices).**
The one-command upgrade if a render disappoints or setup is unwanted:
`--provider openai` (~$8 per course, no model files, and its instruction
steering pairs naturally with the `delivery:` hints planned in
`docs/04-quality-bar.md` §5). ElevenLabs stays wired for A/B comparison but
is no longer the default anywhere.

## 2. Kokoro setup (once per build machine)

```bash
pip install kokoro-onnx soundfile
# model + voice pack (~350MB, one download) from the kokoro-onnx releases:
#   https://github.com/thewh1teagle/kokoro-onnx/releases
#   -> kokoro-v1.0.onnx  and  voices-v1.0.bin
export KOKORO_MODEL=/path/to/kokoro-v1.0.onnx
export KOKORO_VOICES=/path/to/voices-v1.0.bin
python3 pipeline/build.py --course courses/ai-for-pms --provider kokoro
```

Voices to audition first (set `production.tts.voice`): `bf_emma` (British
female, the default here since the scripts are en_GB), `bm_george` (British
male), `af_heart` (the American flagship, highest MOS). CPU renders slower
than the APIs but a full course is still an overnight job, not a blocker;
this is the one Python-dependency exception to the stdlib-only rule, and it
is optional (the provider errors with setup instructions if missing).

QC note: `qc.py --release` fails builds made with the espeak `offline`
scaffold. `kokoro` is a production voice and passes.

## 3. Books: audiobooks without paying per character

Platform policy, verified August 2026, decides this more than voice quality:

| Channel | Route | Cost |
| --- | --- | --- |
| Amazon/Audible | **KDP Virtual Voice** only: Amazon's own voices on an eligible KDP ebook, labelled as virtual voice. ACX still requires human narration and rejects external AI audio | Free |
| Google Play Books | Auto-narrated audiobooks, fully supported | Free |
| Spotify/Findaway | Allowed with the AI-narration disclosure checkbox | Free tooling; use Kokoro/OpenAI output |
| Direct sales / lead magnet | DIY: EPUB text through this repo's `tts.py` providers | $0 to ~$8 per book |

So the audiobook plan costs nothing: Virtual Voice for Amazon (turn it on
per title after the ebook is live), Google's auto-narration for Play Books,
and a DIY Kokoro render only if a direct-sales edition is wanted. Do not
attempt to feed external AI audio into ACX; that is the one forbidden path.

## 4. Chinese editions, later

Kokoro's zh support is limited. When the Simplified Chinese editions need
audio, the candidates are CosyVoice (Apache-2.0, strong zh) locally, or the
zh voices on Azure/Google within their free tiers. Decide when needed;
nothing above blocks on it.

## Sources

- [TextToLab: OpenAI TTS pricing](https://texttolab.com/blog/openai-tts-pricing) · [Azure TTS pricing](https://texttolab.com/blog/azure-text-to-speech-pricing) · [open-source TTS compared](https://texttolab.com/blog/open-source-text-to-speech)
- [LeanVox: TTS API pricing 2026](https://leanvox.com/blog/tts-api-pricing-comparison-2026)
- [FindSkill: Chatterbox vs ElevenLabs blind test](https://findskill.ai/blog/best-open-source-tts-2026/) · [Local AI Master: Kokoro vs XTTS vs Chatterbox](https://localaimaster.com/blog/kokoro-vs-xtts-vs-chatterbox)
- [KDP: audiobooks with Virtual Voice](https://kdp.amazon.com/en_US/help/topic/G3QRL9HQNF273Q2H) · [Audie: ACX AI policy 2026](https://www.audie.ai/does-acx-allow-ai-narrated-audiobooks-current-2026-policy) · [Parlixa: platform rules for AI audiobooks](https://www.parlixa.com/blog/ai-narrated-audiobooks-platform-rules)
