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

Pick from a batch instead of taking the first result:
    python generate_battlemap.py the-golden-goose-chase --node "Node A" --count 4
    python generate_battlemap.py the-golden-goose-chase --node "Node A" --pick 123456
Candidates are saved un-upscaled in tools/image-gen/candidates/ (not committed).
--pick upscales only the chosen one and saves it into assets/. Re-run --count to
add more candidates if none are good.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from candidates import candidate_dir, load_candidate, save_candidates
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


def embed_battlemap(encounter_path, node_label, slug, label):
    """Put the chosen map into the encounter file, right under its Battlemap Prompt.

    The link is relative to encounters/ so it resolves both in the GitHub repo browser
    and on the Jekyll site. Idempotent: does nothing if that image is already linked.
    Returns True if the file was changed.
    """
    text = encounter_path.read_text(encoding="utf-8")
    rel = f"../assets/images/encounters/{slug}/{label}.png"
    if f"]({rel})" in text:
        return False
    start, end = 0, len(text)
    if node_label:
        section = section_for_node(text, node_label)
        start = text.index(section)
        end = start + len(section)
    match = BATTLEMAP_PROMPT_RE.search(text, start, end)
    if not match:
        return False
    alt = f"Battlemap: {node_label}" if node_label else "Battlemap"
    embed = "\n\n" + f"![{alt}]({rel})" + "\n"
    text = text[: match.end()] + embed + text[match.end():]
    encounter_path.write_text(text, encoding="utf-8")
    return True


def upscale(client, bcfg, image_bytes):
    return client.upscale(
        image_bytes,
        upscaler_1=bcfg.get("upscaler", "4x-UltraSharp"),
        target_width=bcfg.get("target_width", 1400),
        target_height=bcfg.get("target_height", 1050),
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("slug", help="Encounter file slug, e.g. 'the-golden-goose-chase'")
    parser.add_argument("--node", default=None, help="Node heading text to search within, e.g. 'Node A'. Omit to use the first Battlemap Prompt found anywhere in the file.")
    parser.add_argument("--label", default=None, help="Output filename (without extension). Defaults to the --node text, or 'map'.")
    parser.add_argument("--seed", type=int, default=-1)
    parser.add_argument("--count", type=int, default=1, help="Generate N un-upscaled candidates into tools/image-gen/candidates/ to choose from (default 1: save straight into assets/)")
    parser.add_argument("--pick", type=int, default=None, metavar="SEED", help="Upscale and promote the candidate with this seed into assets/; no generation")
    parser.add_argument("--lora-weight", type=float, default=None, help="Override battlemap.lora.weight from config.yaml for this run (lower = less of the LoRA's clean map look, more of the base model's own detail)")
    parser.add_argument("--config", default=None)
    parser.add_argument("--no-upscale", action="store_true", help="Skip the upscale pass and save the raw generation size")
    parser.add_argument("--no-embed", action="store_true", help="Don't add the image to the encounter file under its Battlemap Prompt")
    args = parser.parse_args()

    cfg = load_config(args.config)
    bcfg = cfg["battlemap"]
    client = ForgeClient(cfg["forge"]["base_url"])

    label = args.label or (args.node.lower().replace(" ", "-") if args.node else "map")
    label = re.sub(r"[^a-z0-9-]", "", label)
    out_path = REPO_ROOT / "assets" / "images" / "encounters" / args.slug / f"{label}.png"
    cdir = candidate_dir(args.slug, label)

    if args.pick is not None:
        image_bytes = load_candidate(cdir, args.pick)
        if not args.no_upscale:
            print("Upscaling the chosen candidate ...")
            image_bytes = upscale(client, bcfg, image_bytes)
        save_final(out_path, image_bytes)
        finish_embed(args, label)
        return

    encounter_path = find_encounter_file(args.slug)
    text = encounter_path.read_text(encoding="utf-8")
    prompt = extract_battlemap_prompt(text, args.node)

    client.set_checkpoint(bcfg["checkpoint"])

    trigger_words = bcfg["lora"].get("trigger_words", "")
    full_prompt = f"{trigger_words}, {prompt}" if trigger_words else prompt
    extra_detail = (bcfg.get("extra_detail") or "").strip()
    if extra_detail:
        full_prompt += " " + extra_detail
    lora_cfg = dict(bcfg.get("lora") or {})
    if args.lora_weight is not None:
        lora_cfg["weight"] = args.lora_weight
    full_prompt += build_lora_tag(lora_cfg)

    print(f"Generating {args.count} battlemap(s) for '{args.slug}'" + (f" ({args.node})" if args.node else "") + " ...")
    images = client.txt2img(
        prompt=full_prompt,
        negative_prompt=bcfg.get("negative_prompt", ""),
        width=bcfg.get("generate_width", 1216),
        height=bcfg.get("generate_height", 832),
        steps=bcfg.get("steps", 30),
        cfg_scale=bcfg.get("cfg_scale", 7),
        sampler_name=bcfg.get("sampler_name", "DPM++ 2M Karras"),
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
        node_arg = f' --node "{args.node}"' if args.node else ""
        label_arg = f" --label {args.label}" if args.label else ""
        print("Open those, then keep one with:")
        print(f"  python generate_battlemap.py {args.slug}{node_arg}{label_arg} --pick <seed>")
        print(f"or run --count {args.count} again for a fresh batch. Nothing has been written to assets/.")
        return

    image_bytes = images[0][0]
    if not args.no_upscale:
        print("Upscaling ...")
        image_bytes = upscale(client, bcfg, image_bytes)
    save_final(out_path, image_bytes)
    finish_embed(args, label)


def finish_embed(args, label):
    if args.no_embed:
        return
    path = find_encounter_file(args.slug)
    if embed_battlemap(path, args.node, args.slug, label):
        print(f"Embedded the map in {path.relative_to(REPO_ROOT)} under its Battlemap Prompt.")
    else:
        print("Encounter file already links this image (or has no Battlemap Prompt to attach it to); left unchanged.")


def save_final(out_path, image_bytes):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(image_bytes)
    print(f"Saved battlemap to {out_path.relative_to(REPO_ROOT)}")
    print("Review the result, then `git add` and commit it like any other file.")


if __name__ == "__main__":
    main()
