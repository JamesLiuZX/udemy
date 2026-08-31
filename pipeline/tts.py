"""Narration → speech audio.

Providers are pluggable so the choice of voice vendor is a config line, not a
rewrite. `offline` (espeak-ng) exists so the whole pipeline — timings, captions,
video assembly, QC — can be exercised end to end with no API key and no spend.
It is a *scaffold* voice: never ship it.

Set credentials via environment:
    ELEVENLABS_API_KEY   OPENAI_API_KEY   GOOGLE_APPLICATION_CREDENTIALS
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

SAMPLE_RATE = 48000


class TTSError(RuntimeError):
    pass


@dataclass
class Clip:
    path: Path
    seconds: float
    text: str


# ---------------------------------------------------------------------------
# text preparation
# ---------------------------------------------------------------------------

# Words the model should say differently from how they're written.
_SPOKEN = {
    r"\bRAG\b": "rag",
    r"\bLLM\b": "L L M",
    r"\bPRD\b": "P R D",
    r"\bPM\b": "P M",
    r"\bp95\b": "p ninety-five",
    r"\bA/B\b": "A B",
    r"\bQ&A\b": "Q and A",
    r"\bAPI\b": "A P I",
    r"\bKPI\b": "K P I",
}


def speakable(text: str) -> str:
    """Strip authoring marks and expand things TTS reads badly.

    Narration is authored in the same file as slides, so it can pick up markdown
    and production markers. None of that should reach the voice.
    """
    t = text
    t = re.sub(r"\[INSTRUCTOR-INPUT:[^\]]*\]", " ", t)     # unfilled markers
    t = re.sub(r"\[[A-Z-]+:[^\]]*\]", " ", t)              # other direction marks
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = re.sub(r"\*\*([^*]*)\*\*", r"\1", t)
    t = re.sub(r"(?<!\*)\*([^*]*)\*(?!\*)", r"\1", t)
    t = re.sub(r"==([^=]*)==", r"\1", t)
    t = re.sub(r"\s*\n\s*", " ", t)
    for pat, rep in _SPOKEN.items():
        t = re.sub(pat, rep, t)
    return re.sub(r"\s{2,}", " ", t).strip()


# ---------------------------------------------------------------------------
# providers
# ---------------------------------------------------------------------------

def _ffmpeg() -> str:
    return os.environ.get("FFMPEG_BIN") or shutil.which("ffmpeg") or "ffmpeg"


def _to_wav(src: Path, dst: Path) -> None:
    """Normalise any provider output to mono 48k WAV for deterministic assembly."""
    subprocess.run(
        [_ffmpeg(), "-y", "-loglevel", "error", "-i", str(src),
         "-ac", "1", "-ar", str(SAMPLE_RATE), str(dst)],
        check=True, capture_output=True, timeout=300,
    )


def _synth_offline(text: str, out: Path, cfg: dict) -> None:
    exe = shutil.which("espeak-ng") or shutil.which("espeak")
    if not exe:
        raise TTSError("offline provider needs espeak-ng installed")
    raw = out.with_suffix(".raw.wav")
    subprocess.run(
        [exe, "-v", cfg.get("espeak_voice", "en-us"),
         "-s", str(cfg.get("espeak_wpm", 165)), "-p", "45",
         "-w", str(raw), text],
        check=True, capture_output=True, timeout=300,
    )
    _to_wav(raw, out)
    raw.unlink(missing_ok=True)


def _synth_elevenlabs(text: str, out: Path, cfg: dict) -> None:
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        raise TTSError("ELEVENLABS_API_KEY is not set")
    voice_id = cfg.get("voice_id") or os.environ.get("ELEVENLABS_VOICE_ID")
    if not voice_id:
        raise TTSError("no voice_id configured for elevenlabs")

    body = json.dumps({
        "text": text,
        "model_id": cfg.get("model", "eleven_v3"),
        "voice_settings": {
            "stability": cfg.get("stability", 0.45),
            "similarity_boost": cfg.get("similarity_boost", 0.80),
            "style": cfg.get("style", 0.35),
            "use_speaker_boost": True,
        },
    }).encode()

    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
        data=body,
        headers={"xi-api-key": key, "Content-Type": "application/json",
                 "Accept": "audio/mpeg"},
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            audio = resp.read()
    except urllib.error.HTTPError as e:
        raise TTSError(f"ElevenLabs {e.code}: {e.read()[:400]!r}") from e

    mp3 = out.with_suffix(".mp3")
    mp3.write_bytes(audio)
    _to_wav(mp3, out)
    mp3.unlink(missing_ok=True)


def _synth_openai(text: str, out: Path, cfg: dict) -> None:
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise TTSError("OPENAI_API_KEY is not set")
    body = json.dumps({
        "model": cfg.get("model", "gpt-4o-mini-tts"),
        "voice": cfg.get("voice", "alloy"),
        "input": text,
        "response_format": "wav",
    }).encode()
    req = urllib.request.Request(
        "https://api.openai.com/v1/audio/speech",
        data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            audio = resp.read()
    except urllib.error.HTTPError as e:
        raise TTSError(f"OpenAI TTS {e.code}: {e.read()[:400]!r}") from e
    tmp = out.with_suffix(".src.wav")
    tmp.write_bytes(audio)
    _to_wav(tmp, out)
    tmp.unlink(missing_ok=True)


# Loaded once per process; reloading the ONNX graph per slide would dominate
# synthesis time on a 100-lecture build.
_KOKORO: tuple[tuple[str, str], object] | None = None


def _synth_kokoro(text: str, out: Path, cfg: dict) -> None:
    """Free local synthesis via Kokoro-82M (Apache-2.0), through kokoro-onnx.

    No API key, no per-character spend, commercial use permitted. Unlike the
    espeak scaffold this is a *production* voice: near-commercial narration
    quality from an 82M model that runs acceptably on CPU. One-time setup
    (details and voice list in docs/07-tts.md):

        pip install kokoro-onnx soundfile
        # plus kokoro-v1.0.onnx and voices-v1.0.bin on disk,
        # pointed to by KOKORO_MODEL / KOKORO_VOICES or cfg paths
    """
    try:
        import soundfile  # type: ignore
        from kokoro_onnx import Kokoro  # type: ignore
    except ImportError as e:
        raise TTSError(
            "kokoro provider needs 'pip install kokoro-onnx soundfile' plus "
            "the model files. Setup steps in docs/07-tts.md"
        ) from e

    model = Path(cfg.get("model_path")
                 or os.environ.get("KOKORO_MODEL", "kokoro-v1.0.onnx"))
    voices = Path(cfg.get("voices_path")
                  or os.environ.get("KOKORO_VOICES", "voices-v1.0.bin"))
    for p in (model, voices):
        if not p.exists():
            raise TTSError(f"kokoro model file missing: {p} "
                           f"(download per docs/07-tts.md)")

    global _KOKORO
    key = (str(model), str(voices))
    if _KOKORO is None or _KOKORO[0] != key:
        _KOKORO = (key, Kokoro(str(model), str(voices)))
    engine = _KOKORO[1]

    samples, sr = engine.create(
        text,
        voice=cfg.get("voice", "bf_emma"),
        speed=float(cfg.get("speed", 1.0)),
        lang=cfg.get("lang", "en-gb"),
    )
    raw = out.with_suffix(".raw.wav")
    soundfile.write(str(raw), samples, sr)
    _to_wav(raw, out)
    raw.unlink(missing_ok=True)


PROVIDERS = {
    "offline": _synth_offline,
    "elevenlabs": _synth_elevenlabs,
    "openai": _synth_openai,
    "kokoro": _synth_kokoro,
}


# ---------------------------------------------------------------------------
# public API
# ---------------------------------------------------------------------------

def audio_seconds(path: Path) -> float:
    out = subprocess.run(
        [os.environ.get("FFPROBE_BIN") or shutil.which("ffprobe") or "ffprobe",
         "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(path)],
        check=True, capture_output=True, timeout=120,
    ).stdout.decode().strip()
    return float(out)


def synthesize(text: str, out: Path, *, provider: str = "offline",
               cfg: dict | None = None, force: bool = False) -> Clip:
    """Render one narration chunk. Cached on disk — re-running a build does not
    re-spend on unchanged narration."""
    cfg = cfg or {}
    out.parent.mkdir(parents=True, exist_ok=True)
    spoken = speakable(text)

    if not spoken:
        silence(out, 0.6)
        return Clip(out, 0.6, "")

    if out.exists() and not force:
        stamp = out.with_suffix(".txt")
        if stamp.exists() and stamp.read_text(encoding="utf-8") == spoken:
            return Clip(out, audio_seconds(out), spoken)

    fn = PROVIDERS.get(provider)
    if fn is None:
        raise TTSError(f"unknown TTS provider {provider!r}. "
                       f"Known: {', '.join(PROVIDERS)}")
    fn(spoken, out, cfg)
    out.with_suffix(".txt").write_text(spoken, encoding="utf-8")
    return Clip(out, audio_seconds(out), spoken)


def silence(out: Path, seconds: float) -> Path:
    out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [_ffmpeg(), "-y", "-loglevel", "error", "-f", "lavfi",
         "-i", f"anullsrc=r={SAMPLE_RATE}:cl=mono",
         "-t", f"{seconds:.3f}", str(out)],
        check=True, capture_output=True, timeout=120,
    )
    return out
