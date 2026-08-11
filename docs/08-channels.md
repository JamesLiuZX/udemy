# Channel map: where each asset can sell, and what each channel needs

> Decision record, August 2026. Rates and requirements here decay fast;
> re-verify a channel's terms the week you actually onboard it, and update
> this file. Priority verdicts assume the strategy docs' sequencing: finish
> and launch on the "now" channels before opening "later" ones.

## 1. What the pipeline already produces

Every channel below is fed by an asset this repo already builds. No channel
requires new production machinery, only packaging and accounts.

| Asset | Produced by | Feeds |
| --- | --- | --- |
| 1080p MP4 lectures + SRT captions | `pipeline/` | Udemy, YouTube, self-hosted course |
| Interior print PDF | `books/pipeline/` | KDP paperback |
| EPUB | `books/pipeline/build_epub.py` | Kindle, Apple, Kobo, Google Play, direct |
| Simplified Chinese editions (PDF/EPUB) | zh manuscript + CJK class | Google Play, Apple, direct (NOT KDP, see §4) |
| Narration audio (Kokoro/OpenAI, `docs/07-tts.md`) | `pipeline/tts.py` | Spotify audiobooks, Google Play audio, direct |
| Figures, scripts, chapters | everything | Short-form/social via `growth/` repurposer |

## 2. Video courses

| Channel | Your cut | What you need | Verdict |
| --- | --- | --- | --- |
| **Udemy marketplace** | **37% organic, 97% via your own coupon links**; Udemy Business subscription pool has stepped down yearly to ~15% (2026) | Instructor account, payout method, premium instructor application, course files (have), promo video in your real voice, AI disclosure line (wired) | **Now.** The 97% own-link rate is why the email list and coupon strategy in `docs/03` matter: drive your own traffic, keep 97% |
| **YouTube** | Free to publish; monetisation at 500 subs (entry) / 1,000 subs + 4,000 watch hours or 10M Shorts views (full) | Channel, 2FA, AdSense once monetising. Content: the free-preview lectures in full + Shorts from the repurposer | **Now, as funnel first.** Its job is search traffic to the list and course; ad revenue is a later bonus |
| Self-hosted (Podia/Teachable/Gumroad) | ~90%+ minus platform fee | Email list big enough to sell to, payment processor, hosting the MP4s | **Later.** Only once the list can carry a launch; premature self-hosting sells to nobody |
| Skillshare and similar pools | Low per-minute pool payouts | Re-upload of same videos | Skip unless zero-effort; pool economics are worse than Udemy Business |

## 3. Books (English)

| Channel | Your cut | What you need | Verdict |
| --- | --- | --- | --- |
| **Kindle (KDP ebook)** | 70% in the $2.99+ window (2026 ceiling raised; delivery fee shaves the effective rate) | KDP account, tax interview (see §6), cover (commissioned, human-made), EPUB (have), 7 keywords + 3 categories (`docs/05` §3), AI questionnaire answers | **Now** |
| **KDP paperback** | 60% of list minus printing | Same account; interior PDF (have), print cover with spine width after page count locks, ISBN (KDP free one or your own) | **Now**, same upload session |
| **Amazon/Audible audiobook** | Via **KDP Virtual Voice only** (free, Amazon's voices, labelled). ACX rejects external AI audio; its 2026 royalty model is 50% exclusive / 30% non-exclusive for human-narrated | Eligible KDP ebook live first; then a toggle | **Now**, the day the ebook is live |
| **Spotify (audiobooks)** | ~80% of net via Spotify for Authors direct upload | Spotify for Authors account, chapterised audio files (Kokoro/OpenAI render per `docs/07`), square cover art, AI-narration disclosure | **Now-ish**: cheap to do once one book's audio render exists |
| **Google Play Books** | ~52% ebook; free auto-narrated audiobook tool | Partner Center account, EPUB, bank details | **Now**: one account covers ebook + free audiobook + the zh editions' main storefront |
| Apple Books | 70% flat | Apple account + Books for Authors, or go via an aggregator | **Later via Draft2Digital** (one upload → Apple, Kobo, libraries, ~10% of list as the fee) rather than three more direct accounts |
| Kobo | 70% in the $2.99 to $12.99 band | Kobo Writing Life account, or the same aggregator | Later, same D2D upload |
| Direct (Gumroad / own site + Stripe) | ~97% minus processing | The email list, a storefront page, files you already have | **Later but strategic**: the only channel nobody can deplatform, and where the artifact-pack funnel already points |

## 4. Chinese editions

Amazon KDP does not accept Chinese-language books, so the zh-CN editions
route elsewhere: **Google Play Books** (primary storefront, zh supported),
Apple Books, and direct sales / lead-gen into Chinese-speaking communities.
Treat the zh editions as market experiments: if one earns real download or
sales volume, that is the signal to invest in that market properly.

## 5. Short-form and social

Not sales channels; funnel inputs fed by `growth/` (see `docs/06`):
LinkedIn (primary for the PM audience), X threads, YouTube Shorts,
answer-mining on Reddit/HN. Everything routes to the email list; the list
routes to the 97%-margin channels (Udemy own-coupon, direct sales).

## 6. The requirements you'll hit on every channel (do once)

1. **Identity and payout**: each platform wants a payout method and a tax
   interview. As a Singapore tax resident, expect the US platforms (Amazon,
   Google, Apple, Spotify/US) to apply **30% US withholding on US-source
   royalties**, since Singapore has no US income-tax treaty; confirm in each
   platform's tax interview rather than assuming, and keep the completed
   W-8BEN consistent across platforms.
2. **ISBNs**: decide once. KDP's free ISBN locks its imprint field and is
   Amazon-only; buying your own block keeps one identity across channels.
   Ebooks don't strictly need one on most stores; paperbacks do.
3. **Covers**: one commissioned series design (`docs/05` §3) yields the
   ebook cover, the print wrap, and the square audiobook art per title.
4. **AI disclosures**: every channel now asks. Answers are per-platform and
   already documented: Udemy line (wired into `course.yaml`), KDP
   questionnaire (`books/docs/00-kdp-compliance.md`), Spotify's AI-narration
   checkbox, Virtual Voice's automatic labelling. Answer deliberately, never
   by default.
5. **The one rule that spans all of them**: nothing ships anywhere until its
   `verified: true` is real. The channels differ; the signature doesn't.

## 7. Order of operations

1. With `stop-guessing` verified: KDP ebook + paperback same day, Virtual
   Voice toggle when the ebook is live, Google Play ebook + auto-narrated
   audiobook the same week.
2. Render one Kokoro audiobook and open Spotify for Authors with it.
3. Udemy launch per `docs/03` when course #1 is signed off; YouTube channel
   goes live the same week with the free-preview lectures.
4. zh editions to Google Play as they ship.
5. D2D (Apple/Kobo/libraries) and direct sales once the first royalty
   reports and the email list justify the admin.
