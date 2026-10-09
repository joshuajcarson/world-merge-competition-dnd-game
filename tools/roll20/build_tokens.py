#!/usr/bin/env python3
"""Cut the Act Two portraits out onto transparent, square, downscaled token PNGs.

Uses OpenCV GrabCut (pip install opencv-python-headless). Output goes to
tools/roll20/tokens/ at 512x512. Review the results by eye: GrabCut is good on
flat or gradient backgrounds and can clip thin parts (Deacon's dangling chime).

    python tools/roll20/build_tokens.py
"""
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / "tokens"
SIZE = 512
PAD = 0.06  # fraction of the square left empty around the creature

SOURCES = {
    "obby-windlestraw": "assets/images/npcs/obby-windlestraw.png",
    "tamberlock-flue": "assets/images/npcs/tamberlock-flue.png",
    "deacon": "assets/images/npcs/deacon.png",
    "verger": "assets/images/npcs/verger.png",
    "hushbound-skirmisher": "assets/images/races/hushbound-gnomes.png",
    "sextonback": "assets/images/races/sextonbacks.png",
    "dale-pruitt": "assets/images/npcs/dale-pruitt.png",
    "renee-castillo": "assets/images/npcs/renee-castillo.png",
    "gary": "assets/images/npcs/gary.png",
    "ada-mae-quill": "assets/images/npcs/ada-mae-quill.png",
    "queen-ximena-goldleg": "assets/images/npcs/queen-ximena-goldleg.png",
    "aether-wolf": "assets/images/races/aether-wolves.png",
    "alpha-aether-wolf": "assets/images/npcs/alpha-aether-wolf.png",
}


# Busy backgrounds defeat GrabCut, so these become round bust tokens instead:
# name -> (center x, center y, radius) in the 1024 px source.
CIRCLE = {
    "dale-pruitt": (260, 300, 290),
    "renee-castillo": (540, 340, 300),
    "gary": (512, 480, 470),
    "ada-mae-quill": (500, 450, 500),
}


def circle_token(img, cx, cy, r):
    h, w = img.shape[:2]
    pad = r
    big = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    crop = big[cy:cy + 2 * r, cx:cx + 2 * r]
    mask = np.zeros(crop.shape[:2], np.uint8)
    cv2.circle(mask, (r, r), r - 2, 255, -1, cv2.LINE_AA)
    rgba = np.dstack([crop, cv2.GaussianBlur(mask, (3, 3), 0)])
    return cv2.resize(rgba, (SIZE, SIZE), interpolation=cv2.INTER_AREA)


def cut(img):
    h, w = img.shape[:2]
    m = 14
    mask = np.full((h, w), cv2.GC_PR_FGD, np.uint8)
    mask[:m, :] = cv2.GC_BGD
    mask[-m:, :] = cv2.GC_BGD
    mask[:, :m] = cv2.GC_BGD
    mask[:, -m:] = cv2.GC_BGD
    # pixels close to the border's own colour are probably background
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB).astype(np.float32)
    ring = np.concatenate([lab[:m].reshape(-1, 3), lab[-m:].reshape(-1, 3),
                           lab[:, :m].reshape(-1, 3), lab[:, -m:].reshape(-1, 3)])
    ref = np.median(ring, axis=0)
    close = np.linalg.norm(lab - ref, axis=2) < 14
    mask[close & (mask == cv2.GC_PR_FGD)] = cv2.GC_PR_BGD
    bgd = np.zeros((1, 65), np.float64)
    fgd = np.zeros((1, 65), np.float64)
    cv2.grabCut(img, mask, None, bgd, fgd, 8, cv2.GC_INIT_WITH_MASK)
    m8 = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
    n, lab_, stats, _ = cv2.connectedComponentsWithStats(m8)
    if n > 1:
        k = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
        m8 = np.where(lab_ == k, 255, 0).astype(np.uint8)
    m8 = cv2.morphologyEx(m8, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    return cv2.GaussianBlur(m8, (5, 5), 0)


def to_token(img, alpha):
    ys, xs = np.where(alpha > 40)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    rgba = np.dstack([img, alpha])[y0:y1, x0:x1]
    side = max(rgba.shape[:2])
    inner = int(SIZE * (1 - 2 * PAD))
    scale = inner / side
    rgba = cv2.resize(rgba, (max(1, int(rgba.shape[1] * scale)), max(1, int(rgba.shape[0] * scale))),
                      interpolation=cv2.INTER_AREA)
    canvas = np.zeros((SIZE, SIZE, 4), np.uint8)
    oy = (SIZE - rgba.shape[0]) // 2
    ox = (SIZE - rgba.shape[1]) // 2
    canvas[oy:oy + rgba.shape[0], ox:ox + rgba.shape[1]] = rgba
    return canvas


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for name, rel in SOURCES.items():
        img = cv2.imread(str(ROOT / rel))
        if name in CIRCLE:
            tok = circle_token(img, *CIRCLE[name])
        else:
            tok = to_token(img, cut(img))
        cv2.imwrite(str(OUT / f"{name}.png"), tok)
        print("wrote", name)
