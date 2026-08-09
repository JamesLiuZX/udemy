"""HTML slide → PNG, via headless Chromium.

`--virtual-time-budget` makes Chromium advance its clock until pending work
settles, so KaTeX and Mermaid finish drawing before the screenshot is taken.
Without it you get half-rendered diagrams intermittently.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

_CANDIDATES = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/opt/pw-browsers/chromium/chrome-linux/chrome",
]


def find_chrome() -> str:
    if os.environ.get("CHROME_BIN"):
        return os.environ["CHROME_BIN"]
    for c in _CANDIDATES:
        if Path(c).exists():
            return c
    for name in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        found = shutil.which(name)
        if found:
            return found
    # Late glob: browser revision numbers change between Playwright versions.
    for root in (Path("/opt/pw-browsers"), Path.home() / ".cache/ms-playwright"):
        if root.exists():
            for p in root.glob("chromium-*/chrome-linux/chrome"):
                return str(p)
    raise RuntimeError(
        "No Chromium found. Set CHROME_BIN to a Chrome/Chromium binary."
    )


_PROBE = (
    "<html><body style='margin:0'><div id=o></div><script>"
    "document.getElementById('o').textContent='VP '+window.innerWidth+' '+window.innerHeight;"
    "</script></body></html>"
)

_offset_cache: dict[tuple[int, int], tuple[int, int]] = {}


def viewport_offset(width: int, height: int) -> tuple[int, int]:
    """Chrome reserves window chrome, so `--window-size=W,H` does NOT give a
    W×H viewport — on this build it costs 87 vertical pixels, which silently
    crops the bottom of every slide.

    The reservation differs across Chrome builds and platforms, so we measure it
    once per process rather than hardcoding a magic number.
    """
    key = (width, height)
    if key in _offset_cache:
        return _offset_cache[key]

    offset = (0, 0)
    try:
        with tempfile.TemporaryDirectory() as td:
            probe = Path(td) / "probe.html"
            probe.write_text(_PROBE, encoding="utf-8")
            out = subprocess.run(
                [
                    find_chrome(), "--headless", "--no-sandbox", "--disable-gpu",
                    "--disable-dev-shm-usage", f"--window-size={width},{height}",
                    "--virtual-time-budget=3000", "--dump-dom", probe.as_uri(),
                ],
                capture_output=True, timeout=60,
            ).stdout.decode(errors="replace")
        m = re.search(r"VP (\d+) (\d+)", out)
        if m:
            offset = (width - int(m.group(1)), height - int(m.group(2)))
    except Exception:
        offset = (0, 0)          # fall back to no correction rather than failing

    _offset_cache[key] = offset
    return offset


def render_png(
    html_path: Path,
    png_path: Path,
    *,
    width: int = 1920,
    height: int = 1080,
    timeout: int = 90,
) -> Path:
    png_path.parent.mkdir(parents=True, exist_ok=True)
    dw, dh = viewport_offset(width, height)
    cmd = [
        find_chrome(),
        "--headless",
        "--no-sandbox",
        "--disable-gpu",
        "--disable-dev-shm-usage",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        "--default-background-color=0B0E13",
        f"--window-size={width + dw},{height + dh}",
        "--virtual-time-budget=10000",
        "--run-all-compositor-stages-before-draw",
        f"--screenshot={png_path}",
        html_path.resolve().as_uri(),
    ]
    proc = subprocess.run(cmd, capture_output=True, timeout=timeout)
    if not png_path.exists() or png_path.stat().st_size == 0:
        raise RuntimeError(
            f"Chromium produced no image for {html_path.name}\n"
            f"{proc.stderr.decode(errors='replace')[-2000:]}"
        )

    # Chrome captures the whole window, which now includes the chrome we added
    # back above. Trim to the exact slide frame so downstream assets are exact.
    got = png_size(png_path)
    if got != (width, height):
        _crop_to(png_path, width, height)
        got = png_size(png_path)
        if got != (width, height):
            raise RuntimeError(
                f"{png_path.name}: expected {width}x{height}, got {got[0]}x{got[1]}"
            )
    return png_path


def _crop_to(png_path: Path, width: int, height: int) -> None:
    """Crop in place, anchored top-left (the slide is laid out from the origin)."""
    tmp = png_path.with_suffix(".crop.png")
    subprocess.run(
        [_ffmpeg(), "-y", "-loglevel", "error", "-i", str(png_path),
         "-vf", f"crop={width}:{height}:0:0", str(tmp)],
        check=True, capture_output=True, timeout=120,
    )
    tmp.replace(png_path)


def _ffmpeg() -> str:
    return os.environ.get("FFMPEG_BIN") or shutil.which("ffmpeg") or "ffmpeg"


def render_all(html_paths: list[Path], out_dir: Path, **kw) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    return [
        render_png(h, out_dir / f"{h.stem}.png", **kw) for h in html_paths
    ]


def png_size(path: Path) -> tuple[int, int]:
    """Read dimensions straight from the IHDR chunk — avoids a Pillow dependency."""
    import struct
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path} is not a PNG")
    w, h = struct.unpack(">II", head[16:24])
    return w, h
