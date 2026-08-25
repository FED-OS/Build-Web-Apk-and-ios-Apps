#!/usr/bin/env python3
"""Generate PWA icon sizes + favicon + SVG from the source icon."""
import os
from PIL import Image, ImageDraw

SRC = "/workspace/web2apk/resources/icon/icon.png"
ASSETS = "/workspace/web2apk/www/assets"
SPLASH_DIR = "/workspace/web2apk/resources/splash"

os.makedirs(ASSETS, exist_ok=True)
os.makedirs(SPLASH_DIR, exist_ok=True)

src = Image.open(SRC).convert("RGBA")

# Standard PWA sizes
for size in (192, 512):
    out = src.resize((size, size), Image.LANCZOS)
    out.save(os.path.join(ASSETS, f"icon-{size}.png"))

# Maskable variants: add a safe-zone padding (background fill) of ~20%
bg = (11, 16, 32, 255)  # #0b1020
for size in (192, 512):
    canvas = Image.new("RGBA", (size, size), bg)
    inner = src.resize((int(size * 0.72), int(size * 0.72)), Image.LANCZOS)
    offset = ((size - inner.width) // 2, (size - inner.height) // 2)
    canvas.paste(inner, offset, inner)
    canvas.save(os.path.join(ASSETS, f"icon-maskable-{size}.png"))

# Favicon (32px) and a 16
src.resize((32, 32), Image.LANCZOS).save(os.path.join(ASSETS, "favicon-32.png"))
src.resize((16, 16), Image.LANCZOS).save(os.path.join(ASSETS, "favicon-16.png"))

# Compose a .ico with 16+32+48
src.resize((48, 48), Image.LANCZOS).save(
    os.path.join(ASSETS, "favicon.ico"),
    format="ICO",
    sizes=[(16, 16), (32, 32), (48, 48)],
)

# A simple SVG icon (gradient rounded square + arc) for mask-icon / scalable use.
svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#4f8cff"/>
      <stop offset="1" stop-color="#9b5cff"/>
    </linearGradient>
  </defs>
  <rect x="4" y="4" width="56" height="56" rx="14" fill="url(#g)"/>
  <path d="M20 40c0-8 6-14 12-14s12 6 12 14" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/>
  <circle cx="26" cy="28" r="3" fill="#fff"/>
  <circle cx="38" cy="28" r="3" fill="#fff"/>
</svg>
"""
with open(os.path.join(ASSETS, "icon.svg"), "w") as f:
    f.write(svg)

# Splash source: 2732x2732 (iPad) with the icon centered on the brand bg.
SPLASH = 2732
splash = Image.new("RGBA", (SPLASH, SPLASH), bg)
# subtle radial vignette via concentric translucent rings
d = ImageDraw.Draw(splash)
for r in range(SPLASH // 2, 0, -120):
    alpha = max(0, 8 - (SPLASH // 2 - r) // 120)
    d.ellipse(
        [SPLASH // 2 - r, SPLASH // 2 - r, SPLASH // 2 + r, SPLASH // 2 + r],
        fill=(26, 35, 66, alpha),
    )
icon_size = int(SPLASH * 0.22)
inner = src.resize((icon_size, icon_size), Image.LANCZOS)
splash.paste(
    inner, ((SPLASH - icon_size) // 2, (SPLASH - icon_size) // 2), inner
)
splash.save(os.path.join(SPLASH_DIR, "splash.png"))

print("Generated assets:")
for name in sorted(os.listdir(ASSETS)):
    print("  www/assets/" + name)
print("  resources/splash/splash.png")
