# Local Image Generation

Generates NPC/monster token portraits and encounter battlemaps on your own
GPU via [Forge](https://github.com/lllyasviel/stable-diffusion-webui-forge),
saving the results straight into this repo so they get committed alongside
the markdown they illustrate. This cannot run inside a Claude Code cloud
session — there's no GPU there. It's meant to run on your own machine.

## One-time setup

1. **Install Forge** and download an SDXL checkpoint (e.g. the base SDXL
   1.0 model) into its `models/Stable-diffusion` folder. Forge's own docs
   cover installation; a 4060 with 8GB VRAM comfortably runs SDXL at
   1024×1024 in roughly 10-15 seconds per image.
2. **Download a battlemap LoRA** for SDXL (search Civitai for "SDXL
   battlemap" — several exist) and drop the `.safetensors` file into
   Forge's `models/Lora` folder. Note its filename and whatever trigger
   words its model card lists.
3. **Launch Forge** normally (`webui-user.bat` / `./webui.sh`). Recent
   Forge builds serve the Automatic1111-compatible API by default on
   `http://127.0.0.1:7860` with no extra flags. If yours doesn't respond,
   add `--api` to the launch command line (`COMMANDLINE_ARGS` in
   `webui-user.bat`/`.sh`) and relaunch.
4. **Install an upscaler** if you don't already have one — 4x-UltraSharp
   is what the battlemap config defaults to. Forge ships with several
   built in; check Settings → Upscaler in its web UI if `4x-UltraSharp`
   isn't listed, and change `battlemap.upscaler` in `config.yaml` to match
   whatever you actually have installed.
5. **Python deps**, in this folder:
   ```
   pip install -r requirements.txt
   ```
6. **Edit `config.yaml`** — fill in your real checkpoint filename (both
   `portrait.checkpoint` and `battlemap.checkpoint`) and your battlemap
   LoRA's filename + trigger words. Nothing in this file is secret; it's
   just local machine settings, and it's checked into the repo so you only
   set it up once.

## Generating an NPC/monster portrait

Every NPC or race file that's gotten art treatment has a **Token Prompt**
block under its `## DM Only` section (see
`.claude/skills/campaign-chronicle/references/monster-art-style.md` for
that convention — the three-layer style/palette/detail system). With Forge
running:

```
python generate_npc_portrait.py gildrot
```

This reads `world/npcs/gildrot.md`'s Token Prompt, generates a 1024×1024
portrait, saves it to `assets/images/npcs/gildrot.png`, and writes
`image: assets/images/npcs/gildrot.png` back into the file's frontmatter.

Works the same way for a race file (`world/races/<slug>.md`), e.g.:
```
python generate_npc_portrait.py aether-leprechauns
```

Flags: `--seed N` to reproduce or vary a specific result, `--out <path>`
to override where it saves, `--no-frontmatter` to skip editing the
markdown file.

**If a file doesn't have a Token Prompt block yet**, write one first —
either by hand following `monster-art-style.md`'s format, or by asking
Claude (the `campaign-chronicle` skill writes these as part of drafting a
new NPC/race now).

## Generating an encounter battlemap

Encounter files that want a map get a **Battlemap Prompt** block under the
relevant node — see
`.claude/skills/encounter-weaver/references/battlemap-style.md`. With
Forge running:

```
python generate_battlemap.py the-golden-goose-chase --node "Node A"
```

This finds the `### Node A — ...` section in `encounters/the-golden-goose-chase.md`,
pulls its Battlemap Prompt, generates at 1216×832 with the battlemap LoRA
applied, upscales to 1400×1050 (Roll20-friendly), and saves to
`assets/images/encounters/the-golden-goose-chase/node-a.png`.

Omit `--node` for an encounter with just one overall map (it uses the
first Battlemap Prompt block found anywhere in the file). Flags:
`--label <name>` to control the output filename, `--no-upscale` to skip
the upscale pass, `--seed N` as above.

## Picking from a batch

SDXL output needs the occasional reroll, so both scripts can generate several
candidates and let you choose. Add `--count N` to either command:

```
python generate_npc_portrait.py gildrot --count 4
```

This saves four images to `tools/image-gen/candidates/gildrot/<seed>.png`
(gitignored — nothing is written to `assets/` or the note yet) and prints the
exact prompt it sent plus each image's seed. Open them, then keep one:

```
python generate_npc_portrait.py gildrot --pick 123456
```

That copies the chosen image to `assets/images/npcs/gildrot.png` and writes the
`image:` frontmatter field. If none are good, run `--count 4` again — new
candidates are added alongside the old ones, so you can pick across batches.

Battlemaps work the same way (`--count 4`, then `--pick <seed>`, with the same
`--node` / `--label`), except candidates are saved un-upscaled and only the one
you pick gets the upscale pass, which keeps batches fast.

Without `--count`, a run still makes one image and saves it straight into
`assets/`, as before.

## Where images end up

```
assets/images/
  npcs/<slug>.png
  races/<slug>.png
  encounters/<slug>/<node-label-or-map>.png
```

These are committed to the repo like any other file — review each
generation before `git add`-ing it; SDXL output needs the occasional
reroll.

## Troubleshooting

- **Connection refused** — Forge isn't running, or isn't serving the API.
  Confirm `http://127.0.0.1:7860/sdapi/v1/sd-models` loads in a browser.
- **"No checkpoint configured" / "No LoRA configured"** — you haven't
  edited `config.yaml` yet; it ships with placeholder values on purpose.
- **Upscaler name not found** — check Forge's web UI (Extras tab) for the
  exact name it expects and update `battlemap.upscaler` in `config.yaml`.
- **Results look nothing like the style** — double-check the Token/
  Battlemap Prompt block was copied in full, and that the LoRA weight in
  `config.yaml` isn't zero.
