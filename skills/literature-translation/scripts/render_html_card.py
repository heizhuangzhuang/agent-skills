#!/usr/bin/env python3
"""Render an HTML card/chart template to a high-DPI cropped PNG via headless Chrome."""

import argparse
import os
import shutil
import subprocess
import sys


CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
    shutil.which("chromium-browser") or "",
]


def find_chrome() -> str:
    for path in CHROME_CANDIDATES:
        if path and os.path.isfile(path) and os.access(path, os.X_OK):
            return path
    raise FileNotFoundError("Could not find Google Chrome or Chromium executable.")


def auto_crop_bottom(png_path: str, bottom_padding: int = 16) -> tuple[int, int]:
    from PIL import Image, ImageChops  # type: ignore

    im = Image.open(png_path).convert("RGB")
    bg = Image.new("RGB", im.size, (255, 255, 255))
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        cropped = im.crop((0, 0, im.width, min(im.height, bbox[3] + bottom_padding)))
        cropped.save(png_path)
        return cropped.size
    return im.size


def main() -> None:
    parser = argparse.ArgumentParser(description="Render HTML file to auto-cropped PNG.")
    parser.add_argument("html_path", help="Absolute path to input HTML file")
    parser.add_argument("output_png", help="Absolute path to output PNG file")
    parser.add_argument("--width", type=int, default=960, help="Viewport width in px (default: 960)")
    parser.add_argument("--height", type=int, default=1200, help="Initial viewport height in px (default: 1200)")
    parser.add_argument("--scale", type=float, default=2.0, help="Device scale factor for crisp text (default: 2.0)")
    args = parser.parse_args()

    html_abs = os.path.abspath(args.html_path)
    out_abs = os.path.abspath(args.output_png)
    if not os.path.isfile(html_abs):
        print(f"Error: HTML file not found: {html_abs}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(os.path.dirname(out_abs), exist_ok=True)
    chrome = find_chrome()

    cmd = [
        chrome,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--force-device-scale-factor={args.scale}",
        f"--window-size={args.width},{args.height}",
        f"--screenshot={out_abs}",
        f"file://{html_abs}",
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        size = auto_crop_bottom(out_abs, bottom_padding=int(16 * args.scale))
        print(f"Rendered and cropped PNG: {out_abs} ({size[0]}x{size[1]} px)")
    except ImportError:
        print(f"Rendered PNG (Pillow not installed, skipped crop): {out_abs}")


if __name__ == "__main__":
    main()
