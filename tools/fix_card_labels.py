#!/usr/bin/env python3
"""Stabilise the swatch-card label text (PANTONE / #HEX) in an AI-generated video.

For each look a reference frame with clean label text is chosen. In every other
frame of that look the label region is tracked with ECC (rotation + translation)
and the clean reference label is warped onto it. Only paper/ink pixels are
replaced, so the model standing in front of the cards is left untouched.

Usage: python3 tools/fix_card_labels.py IN.mp4 OUT.mp4 [--debug DIR]
"""
import argparse, subprocess
import numpy as np, cv2

# per look: active window (s), reference time (s), label boxes (x, y, w, h) in 1080x1918 coords
LOOKS = [
    {"t": (3.0, 5.3), "ref": 4.0, "boxes": [(145, 528, 225, 187), (719, 875, 252, 165), (221, 1298, 410, 233)]},
    {"t": (5.2, 7.3), "ref": 6.2, "boxes": [(206, 519, 170, 160), (218, 1321, 248, 199)]},
    {"t": (7.2, 9.3), "ref": 8.2, "boxes": [(224, 496, 190, 142), (228, 998, 167, 150), (237, 1349, 187, 168), (698, 939, 142, 148), (689, 1440, 109, 148)]},
    {"t": (9.2, 11.1), "ref": 10.0, "boxes": [(232, 483, 222, 147), (205, 1025, 143, 141), (276, 1323, 166, 162), (633, 1428, 129, 147)]},
]
PAD = 14


def paper_mask(fr):
    """Label paper (bright, unsaturated) plus the ink holes inside it."""
    hsv = cv2.cvtColor(fr, cv2.COLOR_BGR2HSV)
    m = ((fr.min(axis=2) > 232) & (hsv[..., 1] < 25)).astype(np.uint8) * 255
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    return cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((19, 19), np.uint8))


def fill_holes(m):
    """Fill ink holes / small gaps inside the paper so only the outline matters."""
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((31, 31), np.uint8))
    return m


def read_frames(path):
    cap = cv2.VideoCapture(path); fps = cap.get(cv2.CAP_PROP_FPS); out = []
    while True:
        ok, f = cap.read()
        if not ok: break
        out.append(f)
    return out, fps


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("inp"); ap.add_argument("out"); ap.add_argument("--debug")
    a = ap.parse_args()
    frames, fps = read_frames(a.inp)
    H, W = frames[0].shape[:2]
    out_frames = [f.copy() for f in frames]
    crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 60, 1e-5)
    stats = []
    for look in LOOKS:
        ri = int(round(look["ref"] * fps)); ref = frames[ri]
        i0, i1 = int(look["t"][0] * fps), min(int(look["t"][1] * fps), len(frames))
        for (bx, by, bw, bh) in look["boxes"]:
            x0, y0 = max(bx - PAD, 0), max(by - PAD, 0)
            x1, y1 = min(bx + bw + PAD, W), min(by + bh + PAD, H)
            ref_patch = ref[y0:y1, x0:x1]
            ref_paper = paper_mask(ref_patch)
            # track on the paper SHAPE only (text ignored), so garbled AI text does not break the match
            tmpl = cv2.GaussianBlur(fill_holes(ref_paper).astype(np.float32), (9, 9), 0)
            bw_, bh_ = x1 - x0, y1 - y0
            for direction in (+1, -1):
                # the crop window follows the label as it moves (cards fly in / drift)
                ox = oy = 0
                warp_prev = np.eye(2, 3, dtype=np.float32)
                rng = range(ri, i1) if direction > 0 else range(ri - 1, i0 - 1, -1)
                for fi in rng:
                    cx0, cy0 = x0 + ox, y0 + oy
                    if cx0 < 0 or cy0 < 0 or cx0 + bw_ > W or cy0 + bh_ > H:
                        stats.append(0); break
                    cur = frames[fi]
                    cur_g = cv2.GaussianBlur(fill_holes(paper_mask(cur[cy0:cy0 + bh_, cx0:cx0 + bw_])).astype(np.float32), (9, 9), 0)
                    if cur_g.max() == 0:
                        stats.append(0); break
                    warp = warp_prev.copy()
                    try:
                        cc, warp = cv2.findTransformECC(tmpl, cur_g, warp, cv2.MOTION_EUCLIDEAN, crit, None, 5)
                    except cv2.error:
                        cc = 0
                    if cc < 0.72 or abs(warp[0, 2]) > 60 or abs(warp[1, 2]) > 60:
                        stats.append(0); break
                    stats.append(1)
                    # composite the clean reference label into this frame
                    wp = cv2.warpAffine(ref_patch, warp, (bw_, bh_), flags=cv2.INTER_CUBIC | cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REPLICATE)
                    wm = cv2.warpAffine(ref_paper, warp, (bw_, bh_), flags=cv2.INTER_NEAREST | cv2.WARP_INVERSE_MAP)
                    cm = paper_mask(cur[cy0:cy0 + bh_, cx0:cx0 + bw_])
                    m = cv2.erode(((wm > 0) & (cm > 0)).astype(np.uint8), np.ones((3, 3), np.uint8))
                    m = cv2.GaussianBlur(m.astype(np.float32), (5, 5), 0)[..., None]
                    roi = out_frames[fi][cy0:cy0 + bh_, cx0:cx0 + bw_].astype(np.float32)
                    out_frames[fi][cy0:cy0 + bh_, cx0:cx0 + bw_] = (roi * (1 - m) + wp.astype(np.float32) * m).astype(np.uint8)
                    # move the window by the integer part of the found shift, keep the remainder in the warp
                    dx, dy = int(round(warp[0, 2])), int(round(warp[1, 2]))
                    ox += dx; oy += dy
                    warp[0, 2] -= dx; warp[1, 2] -= dy
                    warp_prev = warp
    print(f"tracked {sum(stats)}/{len(stats)} label-frames")
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-",
                            "-i", a.inp, "-map", "0:v", "-map", "1:a?", "-c:a", "copy", "-c:v", "libx264", "-crf", "15", "-preset", "slow",
                            "-pix_fmt", "yuv420p", a.out], stdin=subprocess.PIPE)
    for i, f in enumerate(out_frames):
        enc.stdin.write(f.tobytes())
        if a.debug and i % 15 == 0: cv2.imwrite(f"{a.debug}/f{i:04d}.png", f)
    enc.stdin.close(); enc.wait()


if __name__ == "__main__":
    main()
