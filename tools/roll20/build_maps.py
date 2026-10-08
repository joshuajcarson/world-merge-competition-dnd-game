#!/usr/bin/env python3
"""Resize each battlemap to a whole number of Roll20 grid squares.

Roll20 draws a 5-foot square on a 70 px grid, so a map that is a multiple of 70 px
in both directions lines up with the grid without nudging. The generated maps are
1528x1048, so they are resized (a <1% stretch) to 22x15 squares = 1540x1050 px.

    python tools/roll20/build_maps.py
Writes tools/roll20/maps/<encounter>__<node>.png and prints the page size to enter
in Roll20 (width x height in squares, at 70 px per square).
"""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / "maps"
SQUARE = 70
COLS, ROWS = 22, 15

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for src in sorted((ROOT / "assets/images/encounters").glob("*/*.png")):
        im = Image.open(src).convert("RGB").resize((COLS * SQUARE, ROWS * SQUARE), Image.LANCZOS)
        dst = OUT / f"{src.parent.name}__{src.stem}.png"
        im.save(dst, optimize=True)
        print(f"{dst.name}: {im.size[0]}x{im.size[1]} px = {COLS}x{ROWS} squares")
