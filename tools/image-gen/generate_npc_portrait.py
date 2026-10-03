#!/usr/bin/env python3
"""Generate an NPC/race token portrait via a local Forge instance and save it into the repo.

Reads the "**Token Prompt.**" fenced code block out of world/npcs/<slug>.md
or world/races/<slug>.md (see
.claude/skills/campaign-chronicle/references/monster-art-style.md for that
convention), sends it to Forge, and saves the result under
assets/images/npcs/ or assets/images/races/. Also records the image path
back into the file's frontmatter unless --no-frontmatter is passed.

Usage:
    python generate_npc_portrait.py gildrot
    python generate_npc_portrait.py aether-leprechauns --seed 42

Pick from a batch instead of taking the first result:
    python generate_npc_portrait.py gildrot --count 4      # saves 4 candidates
    python generate_npc_portrait.py gildrot --pick 123456  # promotes one by its seed
Re-run --count to add more candidates if none are good. Candidates live in
tools/image-gen/candidates/ (not committed); only the pick lands in assets/.
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config import load_config
from candidates import candidate_dir, load_candidate, save_candidates
from forge_client import ForgeClient, build_lora_tag

REPO_ROOT = Path(__file__).resolve().parents[2]

TOKEN_PROMPT_RE = re.compile(r"\*\*Token Prompt\.\*\*.*?```\n(.*?)```", re.DOTALL)
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def find_note_file(slug):
    for subdir in ("npcs", "races"):
        candidate = REPO_ROOT / "world" / subdir / f"{slug}.md"
        if candidate.exists():
            return candidate, subdir
    raise FileNotFoundError(f"No world/npcs/{slug}.md or world/races/{slug}.md found")


def extract_token_prompt(text):
    match = TOKEN_PROMPT_RE.search(text)
    if not match:
        raise ValueError(
            "No '**Token Prompt.**' fenced code block found. Add one under "
            "that file's '## DM Only' section first — see "
            ".claude/skills/campaign-chronicle/references/monster-art-style.md"
        )
    return match.group(1).strip()


def write_image_field(text, image_rel_path, today):
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("No frontmatter block found at the top of the file")
    fm_block = match.group(1)
    if re.search(r"^image:", fm_block, re.MULTILINE):
        fm_block = re.sub(r"^image:.*$", f"image: {image_rel_path}", fm_block, flags=re.MULTILINE)
    else:
        fm_block += f"\nimage: {image_rel_path}"
    if re.search(r"^updated:", fm_block, re.MULTILINE):
        fm_block = re.sub(r"^updated:.*$", f"updated: {today}", fm_block, flags=re.MULTILINE)
    return f"---\n{fm_block}\n---\n" + text[match.end():]


def save_final(note_path, text, out_path, image_bytes, no_frontmatter):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(image_bytes)
    print(f"Saved portrait to {out_path.relative_to(REPO_ROOT)}")

    if not no_frontmatter:
        image_rel_path = out_path.relative_to(REPO_ROOT).as_posix()
        today = datetime.date.today().isoformat()
        note_path.write_text(write_image_field(text, image_rel_path, today), encoding="utf-8")
        print(f"Updated {note_path.relative_to(REPO_ROOT)} frontmatter with image: {image_rel_path}")

    print("Review the result, then `git add` and commit it like any other file.")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("slug", help="NPC or race file slug, e.g. 'gildrot' or 'aether-leprechauns'")
    parser.add_argument("--seed", type=int, default=-1)
    parser.add_argument("--count", type=int, default=1, help="Generate N candidates into tools/image-gen/candidates/ to choose from (default 1: save straight into assets/)")
    parser.add_argument("--pick", type=int, default=None, metavar="SEED", help="Promote the candidate with this seed into assets/ and update frontmatter; no generation")
    parser.add_argument("--config", default=None, help="Path to an alternate config.yaml")
    parser.add_argument("--out", default=None, help="Override output path (default: assets/images/<npcs|races>/<slug>.png)")
    parser.add_argument("--no-frontmatter", action="store_true", help="Don't write the image path back into the markdown file")
    args = parser.parse_args()

    cfg = load_config(args.config)
    note_path, subdir = find_note_file(args.slug)
    text = note_path.read_text(encoding="utf-8")
    out_path = Path(args.out) if args.out else REPO_ROOT / "assets" / "images" / subdir / f"{args.slug}.png"
    cdir = candidate_dir(args.slug)

    if args.pick is not None:
        image_bytes = load_candidate(cdir, args.pick)
        save_final(note_path, text, out_path, image_bytes, args.no_frontmatter)
        return

    prompt = extract_token_prompt(text)

    pcfg = cfg["portrait"]
    client = ForgeClient(cfg["forge"]["base_url"])
    client.set_checkpoint(pcfg["checkpoint"])

    full_prompt = prompt + build_lora_tag(pcfg.get("lora"))

    print(f"Generating portrait for '{args.slug}' from {note_path.relative_to(REPO_ROOT)} ...")
    images = client.txt2img(
        prompt=full_prompt,
        negative_prompt=pcfg.get("negative_prompt", ""),
        width=pcfg.get("width", 1024),
        height=pcfg.get("height", 1024),
        steps=pcfg.get("steps", 30),
        cfg_scale=pcfg.get("cfg_scale", 7),
        sampler_name=pcfg.get("sampler_name", "DPM++ 2M Karras"),
        seed=args.seed,
        count=args.count,
    )

    if args.count > 1:
        print("Prompt sent to Forge:")
        print(full_prompt)
        print()
        for seed, path in save_candidates(cdir, images):
            print(f"  seed {seed}: {path}")
        print()
        print("Open those, then keep one with:")
        print(f"  python generate_npc_portrait.py {args.slug} --pick <seed>")
        print(f"or run --count {args.count} again for a fresh batch. Nothing has been written to assets/ or the note.")
        return

    save_final(note_path, text, out_path, images[0][0], args.no_frontmatter)


if __name__ == "__main__":
    main()
