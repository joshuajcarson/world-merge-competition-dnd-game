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
3. **Launch Forge with the API on.** The API is *not* served by default —
   without it every `/sdapi/...` call returns 404. Set
   `set COMMANDLINE_ARGS=--api` in `webui/webui-user.bat` (or
   `COMMANDLINE_ARGS="--api"` in `webui-user.sh`), then launch with
   `run.bat` (the one-click package) or `webui-user.bat`. Forge serves on
   `http://127.0.0.1:7860`. The first launch installs some extension
   packages and takes a few minutes.
4. **Install an upscaler.** 4x-UltraSharp is what the battlemap config
   defaults to, and it is *not* built in. Download `4x-UltraSharp.pth`
   (about 67 MB) from <https://huggingface.co/Kim2091/UltraSharp> into
   `models/ESRGAN`, then restart Forge — it only lists upscalers at startup.
   Or change `battlemap.upscaler` in `config.yaml` to a built-in one (e.g.
   `R-ESRGAN 4x+`).
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
applied, upscales (4x-UltraSharp, no cropping — the result is about 1528×1048,
height-matched to `target_height`, width following the map's own proportions), and saves to
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

- **Connection refused / 404 on `/sdapi/...`** — Forge isn't running, or was
  launched without `--api`. Confirm `http://127.0.0.1:7860/sdapi/v1/options`
  returns JSON. (Don't use `/sdapi/v1/sd-models` to check: on current Forge
  it returns HTTP 500 whenever an SDXL checkpoint is present, even though
  generation works.)
- **"No checkpoint configured" / "No LoRA configured"** — you haven't
  edited `config.yaml` yet; it ships with placeholder values on purpose.
- **Upscaler name not found** — check Forge's web UI (Extras tab) for the
  exact name it expects and update `battlemap.upscaler` in `config.yaml`.
- **Results look nothing like the style** — double-check the Token/
  Battlemap Prompt block was copied in full, and that the LoRA weight in
  `config.yaml` isn't zero.
