"""Slide PNGs + narration audio → a finished lecture MP4.

Output targets Udemy's video/audio standards with headroom rather than sitting on
the limit: 1080p (they require ≥720p), 16:9, H.264 high profile, and true stereo
AAC normalised to −16 LUFS.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

# Beat of silence after each slide's narration, so cuts don't clip the last word
# and the learner gets a moment to read the slide before it changes.
SLIDE_TAIL_SECONDS = 0.55
LEAD_IN_SECONDS = 0.35


def _ffmpeg() -> str:
    return os.environ.get("FFMPEG_BIN") or shutil.which("ffmpeg") or "ffmpeg"


@dataclass
class Segment:
    png: Path
    audio: Path
    seconds: float          # audio length, before padding
    narration: str


def _run(args: list[str], timeout: int = 1800) -> None:
    proc = subprocess.run([_ffmpeg(), "-y", "-loglevel", "error", *args],
                          capture_output=True, timeout=timeout)
    if proc.returncode != 0:
        raise RuntimeError(
            f"ffmpeg failed:\n{' '.join(args)[:500]}\n"
            f"{proc.stderr.decode(errors='replace')[-3000:]}"
        )


def build_audio(segments: list[Segment], out_wav: Path, work: Path) -> list[tuple[float, float]]:
    """Concatenate per-slide narration with padding, then loudness-normalise.

    Returns (start, end) in seconds for each slide's *narration* — the span the
    voice is actually speaking, which is what captions must line up with.
    """
    work.mkdir(parents=True, exist_ok=True)
    parts: list[Path] = []
    spans: list[tuple[float, float]] = []
    cursor = LEAD_IN_SECONDS

    from tts import silence
    lead = work / "_lead.wav"
    silence(lead, LEAD_IN_SECONDS)
    parts.append(lead)

    for i, seg in enumerate(segments):
        parts.append(seg.audio)
        spans.append((cursor, cursor + seg.seconds))
        cursor += seg.seconds

        tail = work / f"_tail{i:03d}.wav"
        silence(tail, SLIDE_TAIL_SECONDS)
        parts.append(tail)
        cursor += SLIDE_TAIL_SECONDS

    listing = work / "audio_concat.txt"
    listing.write_text(
        "".join(f"file '{p.resolve()}'\n" for p in parts), encoding="utf-8"
    )

    raw = work / "_narration_raw.wav"
    _run(["-f", "concat", "-safe", "0", "-i", str(listing), "-c", "copy", str(raw)])

    # Two things at once: bring every lecture to the same perceived level, and
    # widen mono narration to true stereo (Udemy fails single-channel audio).
    _run([
        "-i", str(raw),
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11,aformat=channel_layouts=stereo",
        "-ar", "48000", "-ac", "2", str(out_wav),
    ])
    return spans


def build_video(
    segments: list[Segment],
    audio_wav: Path,
    out_mp4: Path,
    work: Path,
    *,
    fps: int = 30,
    width: int = 1920,
    height: int = 1080,
) -> Path:
    work.mkdir(parents=True, exist_ok=True)
    out_mp4.parent.mkdir(parents=True, exist_ok=True)

    listing = work / "image_concat.txt"
    lines: list[str] = []
    for seg in segments:
        hold = seg.seconds + SLIDE_TAIL_SECONDS
        if seg is segments[0]:
            hold += LEAD_IN_SECONDS
        lines.append(f"file '{seg.png.resolve()}'\nduration {hold:.3f}\n")
    # The concat demuxer drops the final entry's duration unless the last file is
    # repeated, which would otherwise truncate the closing slide.
    lines.append(f"file '{segments[-1].png.resolve()}'\n")
    listing.write_text("".join(lines), encoding="utf-8")

    _run([
        "-f", "concat", "-safe", "0", "-i", str(listing),
        "-i", str(audio_wav),
        "-vf", f"scale={width}:{height}:flags=lanczos,format=yuv420p,fps={fps}",
        "-c:v", "libx264", "-profile:v", "high", "-level", "4.1",
        "-preset", "medium", "-crf", "19",
        "-x264-params", "keyint=60:min-keyint=30:scenecut=0",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-movflags", "+faststart",
        "-shortest",
        str(out_mp4),
    ])
    return out_mp4


def probe(path: Path) -> dict:
    """Stream facts used by QC: dimensions, fps, duration, channel count."""
    ffprobe = os.environ.get("FFPROBE_BIN") or shutil.which("ffprobe") or "ffprobe"
    import json
    out = subprocess.run(
        [ffprobe, "-v", "error", "-print_format", "json",
         "-show_format", "-show_streams", str(path)],
        check=True, capture_output=True, timeout=300,
    ).stdout.decode()
    data = json.loads(out)

    info: dict = {"duration": float(data.get("format", {}).get("duration", 0.0))}
    for s in data.get("streams", []):
        if s.get("codec_type") == "video" and "width" not in info:
            info.update(
                width=s.get("width"), height=s.get("height"),
                vcodec=s.get("codec_name"),
                fps=_ratio(s.get("avg_frame_rate", "0/1")),
            )
        elif s.get("codec_type") == "audio" and "channels" not in info:
            info.update(
                channels=s.get("channels"), acodec=s.get("codec_name"),
                sample_rate=int(s.get("sample_rate", 0) or 0),
            )
    return info


def _ratio(text: str) -> float:
    try:
        num, den = text.split("/")
        return float(num) / float(den) if float(den) else 0.0
    except Exception:
        return 0.0


def measure_loudness(path: Path) -> dict:
    """Integrated loudness + true peak, read back from the encoded file so QC
    checks what actually shipped rather than what we intended."""
    proc = subprocess.run(
        [_ffmpeg(), "-hide_banner", "-nostats", "-i", str(path),
         "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json",
         "-f", "null", "-"],
        capture_output=True, timeout=900,
    )
    text = proc.stderr.decode(errors="replace")
    start = text.rfind("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        return {}
    import json
    try:
        raw = json.loads(text[start:end + 1])
    except json.JSONDecodeError:
        return {}
    return {
        "input_i": float(raw.get("input_i", 0) or 0),
        "input_tp": float(raw.get("input_tp", 0) or 0),
    }
