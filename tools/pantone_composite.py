#!/usr/bin/env python3
"""Composite a green-screen model plate onto the Pantone swatch-card lookbook layout.

Usage:
  python3 tools/pantone_composite.py PLATE.mp4 OUT.mp4 [--audio AUDIO] [--preview T1,T2,...]

All timing lives in TIMELINE below; card motion, colour drain/flood and the
bottom fan are driven from those times so they stay locked to the model's spin.
"""
import argparse, math, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS, DUR = 720, 1280, 30, 11.1
BG = (246, 246, 244)
FONT_B = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
FONT_R = "/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf"

LOOKS = [
    {"cards": ["#D6C3A5", "#F4F2EC", "#A8744F"], "fan": ["#E9D9BC", "#D6C3A5", "#C9A27A", "#B8835A", "#A8744F", "#D9946B", "#E8B48C"]},
    {"cards": ["#6F8FD8", "#FFFFFF", "#1F2A55"], "fan": ["#C9D6F2", "#9DB3E6", "#6F8FD8", "#4D6BC0", "#2F4A93", "#1F2A55", "#8FA9E0"]},
    {"cards": ["#F3E3A2", "#5A3A2A", "#EFE9DC"], "fan": ["#F6EBB8", "#F3E3A2", "#E6C766", "#C9A04A", "#8E6A3C", "#5A3A2A", "#EFE9DC"]},
    {"cards": ["#B5121B", "#A9CBE8", "#6B6B3A"], "fan": ["#E05A5F", "#B5121B", "#A9CBE8", "#7FA9D6", "#9AA35A", "#6B6B3A", "#E8E1D0"]},
]
INTRO_FAN = ["#F2C14E", "#F0A04B", "#EE7D45", "#E8583F", "#D9363E", "#C7284F", "#B21F66", "#9C1C78"]

# ---- timeline (seconds). Filled in from the plate analysis. ----
TIMELINE = {
    "zoom_end": 2.0,          # intro zoom-out finishes
    "intro_fan_drop": (1.4, 2.0),
    "flood1": (2.0, 2.4),     # Look 1 colour floods in (cards fly in)
    # per transition: drain = spin start -> back to camera, flood = just after the outfit swap -> landing
    "transitions": [
        {"drain": (3.9, 4.15), "flood": (4.25, 4.6)},
        {"drain": (6.4, 6.65), "flood": (6.72, 6.95)},
        {"drain": (8.3, 8.55), "flood": (8.62, 8.95)},
    ],
}

# card layout: (cx, cy, angle) for top / middle / bottom
CARD_POS = [(330, 360, 11), (440, 650, -13), (320, 950, 11)]
CARD_W, CARD_H, LABEL_H = 360, 400, 104


def hex2rgb(h):
    h = h.lstrip("#"); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def ease_out(t): return 1 - (1 - t) ** 3
def ease_in(t): return t ** 3
def ease_io(t): return 3 * t * t - 2 * t * t * t
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def prog(t, a, b): return clamp((t - a) / (b - a)) if b > a else float(t >= b)


def pinked_polygon(w, h, tooth=9):
    pts = []
    for x in range(0, w + 1, tooth * 2):  # top
        pts += [(x, 0), (min(x + tooth, w), tooth * 0.9)]
    for y in range(0, h + 1, tooth * 2):  # right
        pts += [(w, y), (w - tooth * 0.9, min(y + tooth, h))]
    for x in range(w, -1, -tooth * 2):  # bottom
        pts += [(x, h), (max(x - tooth, 0), h - tooth * 0.9)]
    for y in range(h, -1, -tooth * 2):  # left
        pts += [(0, y), (tooth * 0.9, max(y - tooth, 0))]
    return pts


_card_cache = {}
def card_image(hexcol):
    if hexcol in _card_cache: return _card_cache[hexcol]
    pad = 24
    im = Image.new("RGBA", (CARD_W + pad * 2, CARD_H + pad * 2), (0, 0, 0, 0))
    shadow = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).polygon([(x + pad + 4, y + pad + 6) for x, y in pinked_polygon(CARD_W, CARD_H)], fill=(0, 0, 0, 60))
    shadow = shadow.filter(ImageFilter.GaussianBlur(8))
    im.alpha_composite(shadow)
    card = Image.new("RGBA", (CARD_W, CARD_H), (0, 0, 0, 0))
    mask = Image.new("L", (CARD_W, CARD_H), 0)
    ImageDraw.Draw(mask).polygon(pinked_polygon(CARD_W, CARD_H), fill=255)
    face = Image.new("RGBA", (CARD_W, CARD_H), (255, 255, 255, 255))
    d = ImageDraw.Draw(face)
    col = hex2rgb(hexcol)
    d.rectangle([0, 0, CARD_W, CARD_H - LABEL_H], fill=col + (255,))
    if sum(col) > 720:  # near-white swatch: hairline so it reads on white
        d.line([(10, CARD_H - LABEL_H), (CARD_W - 10, CARD_H - LABEL_H)], fill=(220, 220, 220, 255), width=2)
    fb = ImageFont.truetype(FONT_B, 34); fr = ImageFont.truetype(FONT_R, 28)
    d.text((26, CARD_H - LABEL_H + 16), "PANTONE", font=fb, fill=(20, 20, 20, 255))
    tw = d.textlength("PANTONE", font=fb)
    d.text((26 + tw + 2, CARD_H - LABEL_H + 14), "®", font=ImageFont.truetype(FONT_R, 16), fill=(20, 20, 20, 255))
    d.text((26, CARD_H - LABEL_H + 56), hexcol.upper(), font=fr, fill=(40, 40, 40, 255))
    card.paste(face, (0, 0), mask)
    im.alpha_composite(card, (pad, pad))
    _card_cache[hexcol] = im
    return im


def paste_rotated(canvas, im, cx, cy, angle, alpha=1.0, blur_dy=0.0):
    r = im.rotate(angle, resample=Image.BICUBIC, expand=True)
    if alpha < 1:
        a = r.getchannel("A").point(lambda v: int(v * alpha)); r.putalpha(a)
    if blur_dy > 2:  # cheap vertical motion blur: average shifted copies
        n = 5
        acc = Image.new("RGBA", (r.width, r.height + int(blur_dy)), (0, 0, 0, 0))
        for k in range(n):
            layer = Image.new("RGBA", acc.size, (0, 0, 0, 0))
            layer.paste(r, (0, int(blur_dy * k / (n - 1))))
            a = layer.getchannel("A").point(lambda v: v // n); layer.putalpha(a)
            acc.alpha_composite(layer)
        r = acc
    canvas.alpha_composite(r, (int(cx - r.width / 2), int(cy - r.height / 2)))


def draw_fan(canvas, cx, cy, radius, inner, colours, rot_deg, span=(180, 360), n=44, label=True):
    d = ImageDraw.Draw(canvas)
    a0, a1 = span
    for i in range(n):
        a = math.radians(a0 + (a1 - a0) * (i + 0.5) / n + rot_deg)
        col = hex2rgb(colours[int(i * len(colours) / n) % len(colours)])
        half = math.radians((a1 - a0) / n * 0.62)
        p = lambda r, ang: (cx + r * math.cos(ang), cy + r * math.sin(ang))
        d.polygon([p(inner, a - half), p(radius, a - half * 0.9), p(radius, a + half * 0.9), p(inner, a + half)], fill=col + (255,), outline=(255, 255, 255, 255))
        if label:
            lr = radius * 0.9
            d.polygon([p(lr, a - half * 0.9), p(radius, a - half * 0.9), p(radius, a + half * 0.9), p(lr, a + half * 0.9)], fill=(255, 255, 255, 255))


def lerp_palette(p1, p2, t):
    out = []
    for a, b in zip(p1, p2):
        ca, cb = hex2rgb(a), hex2rgb(b)
        out.append("#%02x%02x%02x" % tuple(int(ca[i] + (cb[i] - ca[i]) * t) for i in range(3)))
    return out


def key_green(frame):
    f = frame.astype(np.float32)
    r, g, b = f[..., 0], f[..., 1], f[..., 2]
    green = g - np.maximum(r, b)
    alpha = 1.0 - np.clip((green - 10) / 16.0, 0, 1)
    # despill: clamp green to max(r,b) where it dominates
    spill = np.maximum(r, b)
    g2 = np.where(g > spill, spill + (g - spill) * 0.15, g)
    f[..., 1] = g2
    a = Image.fromarray((alpha * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    return f.astype(np.uint8), np.asarray(a).astype(np.float32) / 255.0


def gray_amount_map(t, ys, top, bottom):
    """Return per-row grey factor (1 = black-and-white) for the model."""
    tl = TIMELINE
    span = max(bottom - top, 1)
    rel = (ys - top) / span  # 0 at head, 1 at feet

    def drain(p):   # grey grows from feet upward
        line = 1 - p * 1.15
        return np.clip((rel - line) / 0.08 + 0.5, 0, 1)

    def flood(p):   # colour grows from feet upward
        line = 1 - p * 1.15
        return 1 - np.clip((rel - line) / 0.08 + 0.5, 0, 1)

    if t < tl["flood1"][0]: return np.ones_like(rel)
    if t < tl["flood1"][1]: return flood(prog(t, *tl["flood1"]))
    for tr in tl["transitions"]:
        if t < tr["drain"][0]: return np.zeros_like(rel)
        if t < tr["drain"][1]: return drain(prog(t, *tr["drain"]))
        if t < tr["flood"][0]: return np.ones_like(rel)
        if t < tr["flood"][1]: return flood(prog(t, *tr["flood"]))
    return np.zeros_like(rel)


def card_states(t):
    """List of (hex, cx, cy, angle, blur) for cards visible at time t."""
    tl = TIMELINE
    out = []
    windows = [(0, tl["flood1"], tl["transitions"][0]["drain"])]
    for i, tr in enumerate(tl["transitions"]):
        nxt = tl["transitions"][i + 1]["drain"] if i + 1 < len(tl["transitions"]) else (99, 99)
        windows.append((i + 1, tr["flood"], nxt))
    for look, fin, fout in windows:
        for k, (cx, cy, ang) in enumerate(CARD_POS):
            # enter: bottom card first is hidden behind? original: all sweep up from below, staggered
            s_in = fin[0] - 0.08 + (2 - k) * 0.04
            e_in = s_in + 0.32
            s_out = fout[0] + k * 0.1
            e_out = s_out + 0.28
            if t < s_in or t > e_out: continue
            dy, blur = 0.0, 0.0
            if t < e_in:
                p = prog(t, s_in, e_in); dy = (1 - ease_out(p)) * (H + 200 - cy + 300)
                blur = 60 * (1 - p)
            elif t > s_out:
                p = prog(t, s_out, e_out); dy = -ease_in(p) * (cy + 500)
                blur = 60 * p
            drift_a = 2.0 * math.sin(t * 1.7 + k)
            drift_y = 6.0 * math.sin(t * 1.3 + k * 2)
            spin = 0.0 if blur == 0 else (6 if dy > 0 else -6) * (blur / 60)
            out.append((LOOKS[look]["cards"][k], cx, cy + dy + drift_y, ang + drift_a + spin, blur))
    return out


def fan_state(t):
    tl = TIMELINE
    rot = t * 8.0
    fast = 0.0
    pal = LOOKS[0]["fan"]
    for i, tr in enumerate(tl["transitions"]):
        a, b = tr["drain"][0], tr["flood"][1]
        if t >= a:
            p = prog(t, a, b)
            fast += 220 * ease_io(p)
            pal = lerp_palette(LOOKS[i]["fan"], LOOKS[i + 1]["fan"], ease_io(p))
    return rot + fast, pal


def render_frame(t, plate_rgb, alpha, bbox):
    canvas = Image.new("RGBA", (W, H), BG + (255,))
    tl = TIMELINE
    # intro big fan
    a, b = tl["intro_fan_drop"]
    if t < b + 0.05:
        p = prog(t, a, b)
        cx = -60 + 420 * ease_io(p); cy = 1180 + 330 * ease_io(p)
        rad = 980 * (1 - 0.52 * ease_io(p)); inner = rad * (0.32 + 0.4 * ease_io(p))
        draw_fan(canvas, cx, cy, rad, inner, INTRO_FAN, -20 + 140 * ease_io(p), span=(180, 330), n=26)
    # cards
    for hexcol, cx, cy, ang, blur in card_states(t):
        paste_rotated(canvas, card_image(hexcol), cx, cy, ang, blur_dy=blur)
    # bottom fan
    if t > a:
        rot, pal = fan_state(t)
        fade = prog(t, a + 0.3, b)
        fan = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        draw_fan(fan, W / 2, H + 330, 470, 340, pal, rot % (360 / 44 * 7), n=52)
        if fade < 1:
            fan.putalpha(fan.getchannel("A").point(lambda v: int(v * fade)))
        canvas.alpha_composite(fan)
    # model with grey wipe
    top, bottom = bbox
    ys = np.arange(H, dtype=np.float32)[:, None]
    gmap = gray_amount_map(t, ys, top, bottom)
    f = plate_rgb.astype(np.float32)
    lum = (0.299 * f[..., 0] + 0.587 * f[..., 1] + 0.114 * f[..., 2])[..., None]
    model = f * (1 - gmap[..., None]) + lum * gmap[..., None]
    base = np.asarray(canvas.convert("RGB")).astype(np.float32)
    comp = base * (1 - alpha[..., None]) + model * alpha[..., None]
    img = Image.fromarray(np.clip(comp, 0, 255).astype(np.uint8))
    # intro zoom-out (scale about model's upper body)
    z = 1.0 + 0.45 * (1 - ease_out(prog(t, 0.0, tl["zoom_end"])))
    if z > 1.001:
        cw, ch = W / z, H / z
        cx, cy = W / 2, H * 0.55
        x0 = clamp(cx - cw / 2, 0, W - cw); y0 = clamp(cy - ch / 2, 0, H - ch)
        img = img.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((W, H), Image.LANCZOS)
    return img


def read_plate(path):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf", f"scale={W}:{H},fps={FPS}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    frames = []
    while True:
        buf = p.stdout.read(W * H * 3)
        if len(buf) < W * H * 3: break
        frames.append(np.frombuffer(buf, np.uint8).reshape(H, W, 3))
    return frames


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plate"); ap.add_argument("out")
    ap.add_argument("--audio"); ap.add_argument("--preview")
    args = ap.parse_args()
    frames = read_plate(args.plate)
    n_out = int(DUR * FPS)
    times = [i / FPS for i in range(n_out)]
    if args.preview:
        sel = [float(x) for x in args.preview.split(",")]
        tiles = []
        for t in sel:
            fr = frames[min(int(t * FPS), len(frames) - 1)]
            rgb, a = key_green(fr)
            rows = np.where(a.max(axis=1) > 0.5)[0]
            bbox = (rows.min(), rows.max()) if len(rows) else (0, H)
            tiles.append(render_frame(t, rgb, a, bbox).resize((240, 427)))
        sheet = Image.new("RGB", (240 * len(tiles), 427), "white")
        for i, im in enumerate(tiles): sheet.paste(im, (240 * i, 0))
        sheet.save(args.out); return
    enc = ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-"]
    if args.audio: enc += ["-i", args.audio, "-map", "0:v", "-map", "1:a", "-c:a", "aac", "-b:a", "192k", "-shortest"]
    enc += ["-c:v", "libx264", "-crf", "16", "-preset", "slow", "-pix_fmt", "yuv420p", args.out]
    p = subprocess.Popen(enc, stdin=subprocess.PIPE)
    last_bbox = (0, H)
    for i, t in enumerate(times):
        fr = frames[min(i, len(frames) - 1)]
        rgb, a = key_green(fr)
        rows = np.where(a.max(axis=1) > 0.5)[0]
        if len(rows): last_bbox = (rows.min(), rows.max())
        p.stdin.write(np.asarray(render_frame(t, rgb, a, last_bbox)).tobytes())
        if i % 30 == 0: print(f"frame {i}/{n_out}", file=sys.stderr)
    p.stdin.close(); p.wait()


if __name__ == "__main__":
    main()
