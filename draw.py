#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news front page (1024x1024 PNG).

Deterministic: no randomness, no network, no timestamps. Pillow only.
Run: python3 draw.py  -> writes entry.png beside this file.
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

PAPER = (247, 243, 232)
INK = (26, 26, 26)
NAVY = (24, 38, 64)
GOLD = (201, 162, 75)
GOLD_L = (232, 196, 110)
RED = (178, 34, 34)
TEAL = (18, 92, 96)
RUST = (176, 92, 32)
CREAM = (250, 246, 236)
GREY = (90, 90, 88)
RULE = (150, 140, 120)
GREEN = (118, 185, 0)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading=None):
    """Draw wrapped text; returns y just below the last line."""
    if leading is None:
        leading = int(fnt.size * 1.28)
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def hline(draw, x0, x1, y, fill, width=1):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def label(draw, x, y, text, color, size=21):
    """Small caps section label with a short rule after it."""
    fnt = font(SANS_B, size)
    draw.text((x, y), text, font=fnt, fill=color)
    w = draw.textlength(text, font=fnt)
    hline(draw, x + w + 10, x + w + 46, y + size // 2 + 1, color, 3)
    return y + size + 6


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 118], fill=NAVY)
d.rectangle([0, 118, W, 124], fill=GOLD)
d.text((28, 14), "THE WORLD IN ONE DAY", font=font(SANS_B, 24),
       fill=GOLD_L)
d.text((28, 40), "WORLD NEWS", font=font(SERIF, 58), fill=(250, 248, 240))
d.text((28, 96), "Tuesday, 24 November 2026",
       font=font(SANS_B, 22), fill=GOLD_L)
d.text((W - 28, 22), "SIX STORIES", font=font(SANS_B, 30),
       fill=(250, 248, 240), anchor="ra")
d.text((W - 28, 56), "that defined the day", font=font(SANS, 22),
       fill=(210, 210, 205), anchor="ra")
d.text((W - 28, 94), "NVIDIA  •  SEOUL  •  GULF",
       font=font(SANS_B, 17), fill=GOLD_L, anchor="ra")

# ------------------------------------------------------------- hero: Nvidia
HX, HY, HW, HH = 28, 140, 968, 300
d.rectangle([HX, HY, HX + HW, HY + HH], outline=INK, width=2)
# dark green boardroom/chart backdrop
d.rectangle([HX + 2, HY + 2, HX + HW - 2, HY + 164], fill=(8, 30, 22))
# rising chart line in gold, left to right
pts = [(HX + 40, HY + 140), (HX + 160, HY + 118), (HX + 280, HY + 126),
       (HX + 400, HY + 88), (HX + 520, HY + 96), (HX + 640, HY + 52),
       (HX + 760, HY + 60), (HX + 880, HY + 22)]
d.line(pts, fill=GOLD, width=5)
for px, py in pts:
    d.ellipse([px - 6, py - 6, px + 6, py + 6], fill=GOLD_L)
# chip in the centre-left
CX0, CY0, CX1, CY1 = HX + 330, HY + 48, HX + 560, HY + 148
for px in range(CX0 - 26, CX1 + 26, 34):
    d.rectangle([px, CY0 - 16, px + 14, CY0], fill=(60, 60, 60))
    d.rectangle([px, CY1, px + 14, CY1 + 16], fill=(60, 60, 60))
for py in range(CY0 + 4, CY1, 34):
    d.rectangle([CX0 - 16, py, CX0, py + 14], fill=(60, 60, 60))
    d.rectangle([CX1, py, CX1 + 16, py + 14], fill=(60, 60, 60))
d.rectangle([CX0, CY0, CX1, CY1], fill=(24, 48, 30),
            outline=(90, 140, 60), width=3)
d.rectangle([CX0 + 70, CY0 + 22, CX1 - 70, CY1 - 22], fill=GREEN)
d.text(((CX0 + CX1) // 2, (CY0 + CY1) // 2), "NVDA",
       font=font(SANS_B, 40), fill=(250, 250, 250), anchor="mm")
# +31% callout at the right
d.text((HX + HW - 60, HY + 58), "+31%", font=font(SANS_B, 72),
       fill=GOLD_L, anchor="ra")
d.text((HX + HW - 60, HY + 132), "shares on Monday",
       font=font(SANS, 20), fill=(210, 210, 205), anchor="ra")
# hero caption block under the art band
d.rectangle([HX, HY + 166, HX + HW, HY + HH], fill=CREAM)
label(d, HX + 18, HY + 176, "LEAD STORY  •  NVIDIA", RED, 21)
d.text((HX + 18, HY + 204), "Nvidia reinstates Huang as CEO",
       font=font(SERIF, 38), fill=INK)
text_block(d, HX + 18, HY + 248,
           "Board voted unanimously Monday, 11 days after he resigned. "
           "Trump pressed the board; shares soared 31%. Commerce "
           "blacklisted Megaspeed, the chip firm at the scandal's centre.",
           font(SANS, 21), INK, HW - 36, leading=26)

# ------------------------------------------------- second row: two panels
RY, RH = 452, 228
PW = 474
# --- left: South Korea / Ulleung alert
LX, LW = 28, PW
d.rectangle([LX, RY, LX + LW, RY + RH], outline=INK, width=2)
d.rectangle([LX + 2, RY + 2, LX + LW - 2, RY + 86], fill=(16, 30, 54))
# sea at the bottom of the art band
d.rectangle([LX + 2, RY + 62, LX + LW - 2, RY + 86], fill=(24, 58, 78))
# Ulleung island silhouette
d.polygon([(LX + 150, RY + 62), (LX + 190, RY + 30), (LX + 240, RY + 26),
           (LX + 280, RY + 48), (LX + 260, RY + 62)], fill=(46, 90, 52))
# two fighter jets with contrails
for jx, jy in [(LX + 60, RY + 30), (LX + 320, RY + 18)]:
    d.line([(jx - 70, jy + 8), (jx - 8, jy + 2)], fill=(200, 200, 200),
           width=2)
    d.polygon([(jx, jy), (jx + 34, jy + 8), (jx, jy + 16),
               (jx + 10, jy + 8)], fill=(220, 220, 220))
# red shelter-alert triangle
d.polygon([(LX + LW - 70, RY + 12), (LX + LW - 34, RY + 66),
           (LX + LW - 106, RY + 66)], fill=RED,
          outline=(250, 250, 250), width=2)
d.text((LX + LW - 70, RY + 46), "!", font=font(SANS_B, 30),
       fill=(250, 250, 250), anchor="mm")
d.rectangle([LX, RY + 88, LX + LW, RY + RH], fill=CREAM)
label(d, LX + 16, RY + 98, "SOUTH KOREA  •  ULLEUNG ISLAND", RUST, 19)
d.text((LX + 16, RY + 124), "Russian jets trigger\nshelter alert off Ulleung",
       font=font(SERIF, 28), fill=INK)
text_block(d, LX + 16, RY + 190,
           "Seoul scrambled jets; the planes entered the air defence "
           "zone — not airspace. Alert lifted in minutes.",
           font(SANS, 16), INK, LW - 32, leading=20)

# --- right: Iran / Gulf
RX = 522
d.rectangle([RX, RY, RX + PW, RY + RH], outline=INK, width=2)
d.rectangle([RX + 2, RY + 2, RX + PW - 2, RY + 86], fill=(18, 36, 44))
# gulf sea + two naval vessels
d.rectangle([RX + 2, RY + 58, RX + PW - 2, RY + 86], fill=(16, 52, 68))
for sx, sw in [(RX + 40, 150), (RX + 260, 170)]:
    d.rectangle([sx, RY + 40, sx + sw, RY + 58], fill=(14, 14, 16))
    d.rectangle([sx + sw - 44, RY + 22, sx + sw - 20, RY + 40],
                fill=(14, 14, 16))
    d.rectangle([sx + 10, RY + 48, sx + sw - 10, RY + 58],
                fill=(52, 44, 34))
# missile arcs + flashes over the gulf
d.arc([RX + 300, RY - 30, RX + 440, RY + 70], start=200, end=340,
      fill=(250, 200, 60), width=3)
for fx, fy, r in [(RX + 330, RY + 16, 12), (RX + 380, RY + 8, 15)]:
    d.ellipse([fx - r, fy - r, fx + r, fy + r], fill=(232, 132, 30))
    d.ellipse([fx - r // 2, fy - r // 2, fx + r // 2, fy + r // 2],
              fill=(250, 200, 60))
d.rectangle([RX, RY + 88, RX + PW, RY + RH], fill=CREAM)
label(d, RX + 16, RY + 98, "IRAN  •  GULF", TEAL, 19)
d.text((RX + 16, RY + 124), "Iran steps up strikes\nas US blockade bites",
       font=font(SERIF, 28), fill=INK)
text_block(d, RX + 16, RY + 190,
           "Tehran vows to use 'all its tools' against the blockade. "
           "US sanctioned dozens over shadow banking.",
           font(SANS, 16), INK, PW - 32, leading=20)

# -------------------------------------------------- third row: two panels
LY, LH = 692, 160
# --- left: NATO AWACS to Poland
d.rectangle([LX, LY, LX + LW, LY + LH], outline=INK, width=2)
d.rectangle([LX + 2, LY + 2, LX + LW - 2, LY + 58], fill=(30, 44, 70))
# clouds + AWACS silhouette (fuselage, wings, radar disc)
for cx, cy, r in [(LX + 60, LY + 16, 12), (LX + 90, LY + 22, 9),
                  (LX + 400, LY + 14, 11), (LX + 428, LY + 20, 8)]:
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(200, 205, 215))
d.ellipse([LX + 180, LY + 30, LX + 300, LY + 44], fill=(220, 220, 220))
d.polygon([(LX + 150, LY + 34), (LX + 190, LY + 26), (LX + 330, LY + 26),
           (LX + 350, LY + 34), (LX + 330, LY + 42), (LX + 190, LY + 42)],
          fill=(220, 220, 220))
d.polygon([(LX + 210, LY + 42), (LX + 240, LY + 56), (LX + 260, LY + 42)],
          fill=(200, 200, 200))
d.rectangle([LX + 236, LY + 16, LX + 240, LY + 26], fill=(200, 200, 200))
d.ellipse([LX + 216, LY + 8, LX + 264, LY + 20], fill=(240, 240, 240),
          outline=(180, 180, 180))
d.rectangle([LX, LY + 60, LX + LW, LY + LH], fill=CREAM)
label(d, LX + 16, LY + 68, "NATO  •  POLAND", (30, 70, 120), 17)
d.text((LX + 16, LY + 92), "NATO sends AWACS jet to Poland",
       font=font(SERIF, 25), fill=INK)
text_block(d, LX + 16, LY + 122,
           "Alliance deploys early-warning aircraft after three "
           "Russian missiles landed Friday.",
           font(SANS, 16), INK, LW - 32, leading=19)

# --- right: EU 22nd sanctions package
d.rectangle([RX, LY, RX + LW, LY + LH], outline=INK, width=2)
d.rectangle([RX + 2, LY + 2, RX + PW - 2, LY + 58], fill=(0, 51, 153))
# circle of twelve gold stars (EU flag)
scx, scy, sr = RX + 90, LY + 30, 20
for k in range(12):
    ang = 2 * math.pi * k / 12 - math.pi / 2
    sx, sy = scx + sr * math.cos(ang), scy + sr * math.sin(ang)
    d.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=(255, 204, 0))
# document stamped "22"
d.rectangle([RX + 200, LY + 10, RX + 330, LY + 50], fill=(244, 240, 228),
            outline=(120, 110, 96))
d.text((RX + 265, LY + 30), "22", font=font(SERIF, 30),
       fill=NAVY, anchor="mm")
d.line([(RX + 210, LY + 44), (RX + 320, LY + 44)], fill=(150, 142, 126),
       width=2)
d.rectangle([RX, LY + 60, RX + PW, LY + LH], fill=CREAM)
label(d, RX + 16, LY + 68, "EU  •  BRUSSELS", (0, 51, 153), 17)
d.text((RX + 16, LY + 92), "EU proposes 22nd sanctions package",
       font=font(SERIF, 25), fill=INK)
text_block(d, RX + 16, LY + 122,
           "Russian teams barred from competing under their flag; "
           "banks, crypto and ex-combatants targeted.",
           font(SANS, 16), INK, PW - 32, leading=19)

# ------------------------------------------- bottom strip: three short items
BY, BH, BW, GAP = 864, 104, 312, 16


def strip_item(x, tag, accent, headline, body):
    d.rectangle([x, BY, x + BW, BY + BH], outline=INK, width=2)
    d.rectangle([x + 2, BY + 2, x + BW - 2, BY + BH - 2], fill=CREAM)
    label(d, x + 14, BY + 10, tag, accent, 15)
    y = text_block(d, x + 14, BY + 34, headline, font(SERIF, 19), INK,
                   BW - 28, leading=22)
    text_block(d, x + 14, y + 2, body, font(SANS, 15), INK, BW - 28,
               leading=18)


strip_item(28, "UKRAINE  •  ODESA", RED,
           "Odesa without power, heat or water",
           "Russian strikes hit the city overnight.")
strip_item(28 + BW + GAP, "VANUATU  •  PACIFIC", TEAL,
           "6.5-magnitude quake hits Vanuatu",
           "No tsunami threat, officials say.")
strip_item(28 + 2 * (BW + GAP), "GAZA", RUST,
           "Gaza strikes kill at least three",
           "Including a UNRWA worker, on Monday.")

# ------------------------------------------------------------------ footer
hline(d, 28, W - 28, 974, RULE, 2)
d.text((28, 984), "Sources: Reuters, AP, CNN, Al Jazeera, BBC  •  24 November 2026",
       font=font(SANS, 18), fill=GREY)
d.text((W - 28, 984), "make.fun  •  news-image-20261124",
       font=font(SANS, 18), fill=GREY, anchor="ra")

img.save(OUT, "PNG")
print("wrote", OUT, os.path.getsize(OUT), "bytes")
