#!/usr/bin/env python3
"""Generate an encounter battlemap via a local Forge instance and save it into the repo.

Reads a "**Battlemap Prompt.**" fenced code block out of encounters/<slug>.md
(see .claude/skills/encounter-weaver/references/battlemap-style.md for that
convention), sends it through Forge with the battlemap LoRA applied, upscales
it toward a Roll20-friendly size, and saves the result under
assets/images/encounters/<slug>/.

Usage:
    python generate_battlemap.py the-golden-goose-chase
    python generate_battlemap.py the-golden-goose-chase --node "Node A"
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config import load_config
from forge_client import ForgeClient, build_lora_tag

REPO_ROOT = Path(__file__).resolve().parents[2]

BATTLEMAP_PROMPT_RE = re.compile(r"\*\*Battlemap Prompt\.\*\*.*?```\n(.*?)```", re.DOTALL)
NODE_HEADING_RE = re.compile(r"^###\s+.*$", re.MULTILINE)


def find_encounter_file(slug):
    candidate = REPO_ROOT / "encounters" / f"{slug}.md"
    if not candidate.exists():
        raise FileNotFoundError(f"No encounters/{slug}.md found")
    return candidate


def section_for_node(text, node_label):
    """Slices out the text between a ### heading matching node_label and the next ### (or end of file)."""
    headings = list(NODE_HEADING_RE.finditer(text))
    start = None
    end = len(text)
    for i, h in enumerate(headings):
        if node_label.lower() in h.group(0).lower():
            start = h.start()
            end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
            break
    if start is None:
        raise ValueError(f"No '### ...{node_label}...' heading found in this encounter")
    return text[start:end]


def extract_battlemap_prompt(text, node_label=None):
    search_space = section_for_node(text, node_label) if node_label else text
    match = BATTLEMAP_PROMPT_RE.search(search_space)
    if not match:
        where = f"node '{node_label}'" if node_label else "this file"
        raise ValueError(
            f"No '**Battlemap Prompt.**' fenced code block found in {where}. Add one first — "
            "see .claude/skills/encounter-weaver/references/battlemap-style.md"
        )
    return match.group(1).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("slug", help="Encounter file slug, e.g. 'the-golden-goose-chase'")
    parser.add_argument("--node", default=None, help="Node heading text to search within, e.g. 'Node A'. Omit to use the first Battlemap Prompt found anywhere in the file.")
    parser.add_argument("--label", default=None, help="Output filename (without extension). Defaults to the --node text, or 'map'.")
    parser.add_argument("--seed", type=int, default=-1)
    parser.add_argument("--config", default=None)
    parser.add_argument("--no-upscale", action="store_true", help="Skip the upscale pass and save the raw generation size")
    args = parser.parse_args()

    cfg = load_config(args.config)
    encounter_path = find_encounter_file(args.slug)
    text = encounter_path.read_text()
    prompt = extract_battlemap_prompt(text, args.node)

    bcfg = cfg["battlemap"]
    client = ForgeClient(cfg["forge"]["base_url"])
    client.set_checkpoint(bcfg["checkpoint"])

    trigger_words = bcfg["lora"].get("trigger_words", "")
    full_prompt = f"{trigger_words}, {prompt}" if trigger_words else prompt
    full_prompt += build_lora_tag(bcfg.get("lora"))

    print(f"Generating battlemap for '{args.slug}'" + (f" ({args.node})" if args.node else "") + " ...")
    images = client.txt2img(
        prompt=full_prompt,
        negative_prompt=bcfg.get("negative_prompt", ""),
        width=bcfg.get("generate_width", 1216),
        height=bcfg.get("generate_height", 832),
        steps=bcfg.get("steps", 30),
        cfg_scale=bcfg.get("cfg_scale", 7),
        sampler_name=bcfg.get("sampler_name", "DPM++ 2M Karras"),
        seed=args.seed,
    )
    image_bytes = images[0]

    if not args.no_upscale:
        print("Upscaling ...")
        image_bytes = client.upscale(
            image_bytes,
            upscaler_1=bcfg.get("upscaler", "4x-UltraSharp"),
            target_width=bcfg.get("target_width", 1400),
            target_height=bcfg.get("target_height", 1050),
        )

    label = args.label or (args.node.lower().replace(" ", "-") if args.node else "map")
    label = re.sub(r"[^a-z0-9-]", "", label)
    out_path = REPO_ROOT / "assets" / "images" / "encounters" / args.slug / f"{label}.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(image_bytes)
    print(f"Saved battlemap to {out_path.relative_to(REPO_ROOT)}")
    print("Review the result, then `git add` and commit it like any other file.")


if __name__ == "__main__":
    main()
