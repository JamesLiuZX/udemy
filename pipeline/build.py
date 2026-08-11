#!/usr/bin/env python3
"""Build lectures: source .md → slides → narration → MP4 + SRT.

    python3 pipeline/build.py --course courses/ai-for-pms
    python3 pipeline/build.py --course courses/ai-for-pms --only 0.3 0.4
    python3 pipeline/build.py --course courses/ai-for-pms --provider elevenlabs
    python3 pipeline/build.py --course courses/ai-for-pms --slides-only

Rebuilds are incremental: narration audio is cached by its spoken text, so
editing one line re-synthesises one slide, not the course.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import captions as cap
import tts
import video as vid
from lecture import Lecture, load_course
from render import render_all
from slides import write_slides


def build_lecture(lec: Lecture, course: dict, out_root: Path, *,
                  provider: str, slides_only: bool = False,
                  force_audio: bool = False) -> dict:
    prod = course.get("production", {})
    width, height = prod.get("resolution", [1920, 1080])
    fps = prod.get("fps", 30)
    mark = course.get("title", "").split(":")[0].strip()

    work = out_root / "work" / lec.slug
    dist = out_root / "dist"
    work.mkdir(parents=True, exist_ok=True)
    dist.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    print(f"  · {lec.id:>5}  {lec.title[:58]:<58}", end="", flush=True)

    html = write_slides(lec, work / "html", mark)
    pngs = render_all(html, work / "png", width=width, height=height)

    if slides_only:
        print(f"  slides={len(pngs)}  ({time.time() - t0:.1f}s)")
        return {"id": lec.id, "slides": len(pngs), "video": None}

    tts_cfg = dict(prod.get("tts", {}))
    tts_cfg.pop("provider", None)

    segments: list[vid.Segment] = []
    for i, (slide, png) in enumerate(zip(lec.slides, pngs), start=1):
        wav = work / "audio" / f"slide-{i:03d}.wav"
        clip = tts.synthesize(slide.narration, wav, provider=provider,
                              cfg=tts_cfg, force=force_audio)
        segments.append(vid.Segment(png=png, audio=clip.path,
                                    seconds=clip.seconds,
                                    narration=tts.strip_pause(slide.narration)))

    narration = work / "narration.wav"
    spans = vid.build_audio(segments, narration, work / "tmp")

    mp4 = dist / f"{lec.slug}.mp4"
    vid.build_video(segments, narration, mp4, work / "tmp",
                    fps=fps, width=width, height=height)

    cues = cap.cues_for_segments(
        [(seg.narration, s, e) for seg, (s, e) in zip(segments, spans)]
    )
    srt = dist / f"{lec.slug}.srt"
    srt.write_text(cap.to_srt(cues), encoding="utf-8")

    info = vid.probe(mp4)
    print(f"  {info.get('duration', 0) / 60:5.1f}m  "
          f"{info.get('width')}x{info.get('height')}  "
          f"{len(pngs)} slides  ({time.time() - t0:.1f}s)")

    return {
        "id": lec.id,
        "title": lec.title,
        "slug": lec.slug,
        "video": str(mp4.relative_to(out_root)),
        "srt": str(srt.relative_to(out_root)),
        "slides": len(pngs),
        "duration": info.get("duration", 0.0),
        "width": info.get("width"),
        "height": info.get("height"),
        "channels": info.get("channels"),
        "voice": lec.voice,
        "verified": lec.verified,
        "words": lec.word_count,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", required=True)
    ap.add_argument("--out", default="build")
    ap.add_argument("--only", nargs="*", help="lecture ids to build")
    ap.add_argument("--provider", default=None,
                    help="override TTS provider (offline|elevenlabs|openai)")
    ap.add_argument("--slides-only", action="store_true")
    ap.add_argument("--force-audio", action="store_true",
                    help="ignore the narration cache and re-synthesise")
    args = ap.parse_args()

    course_dir = Path(args.course)
    course, lectures = load_course(course_dir)
    if args.only:
        wanted = set(args.only)
        lectures = [l for l in lectures if l.id in wanted]

    if not lectures:
        print("No lectures matched. Have you written any under lectures/ yet?")
        return 1

    provider = args.provider or course.get("production", {}).get("tts", {}).get(
        "provider", "offline")

    out_root = Path(args.out) / course["slug"]
    out_root.mkdir(parents=True, exist_ok=True)

    print(f"\n{course['title']}")
    print(f"  provider={provider}  lectures={len(lectures)}  out={out_root}\n")

    if provider == "offline" and not args.slides_only:
        print("  NOTE: 'offline' is the espeak scaffold voice — correct timings,")
        print("        unshippable quality. Use it to prove the build, not to publish.\n")

    results = []
    for lec in lectures:
        try:
            results.append(build_lecture(
                lec, course, out_root, provider=provider,
                slides_only=args.slides_only, force_audio=args.force_audio))
        except Exception as e:                      # keep going; report at the end
            print(f"  FAILED: {e}")
            results.append({"id": lec.id, "error": str(e)})

    manifest = out_root / "manifest.json"
    manifest.write_text(json.dumps(
        {"course": course["slug"], "title": course["title"],
         "provider": provider, "lectures": results}, indent=2), encoding="utf-8")

    total = sum(r.get("duration", 0) or 0 for r in results)
    failed = [r for r in results if r.get("error")]
    print(f"\n  built {len(results) - len(failed)}/{len(results)} · "
          f"total {total / 3600:.2f}h · manifest → {manifest}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
