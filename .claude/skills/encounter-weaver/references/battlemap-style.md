# Battlemap Style — Image Generator Prompts

Companion to
`.claude/skills/campaign-chronicle/references/monster-art-style.md`, but
for encounter battlemaps instead of NPC/monster tokens. Generated locally
via `tools/image-gen/generate_battlemap.py` (SDXL + a battlemap LoRA,
through Forge) rather than copy-pasted into an external tool — see that
script's own `README.md` for the generation side.

Same three-layer idea as the monster art style, with one difference: a
battlemap LoRA already carries most of "Layer 1" in its trigger words, so
Layer 1 here is short and mostly about framing/angle, not a long style
paragraph.

## Layer 1 — Universal Framing

```
Top-down tabletop battlemap, straight overhead angle, evenly lit with no
hard directional shadows obscuring terrain, clean enough to drop a grid
over without losing readability. No characters, miniatures, or tokens in
the scene — terrain and set dressing only.
```

Your battlemap LoRA's trigger words (set in `config.yaml`'s
`battlemap.lora.trigger_words`) get prepended automatically by the
generation script — don't repeat them by hand in Layer 3.

## Layer 2 — Origin-World Terrain Palettes

Pick based on where the scene is actually set, same as the monster style
guide's origin-world logic.

- **Aether:** oversaturated, faintly bioluminescent flora and fungus;
  ground textures that look grown rather than built, even in "natural"
  terrain; an unnatural light source implied even in daylight scenes.
- **Faerun:** natural fantasy terrain — weathered stone, packed earth,
  timber, moss — lit like an ordinary outdoor or dungeon scene, nothing
  about the lighting itself should read as wrong.
- **Earth:** mundane, recognizable real-world materials — asphalt, drywall,
  linoleum, chain-link — slightly worn, exactly as ordinary as the setting
  demands. The "wrongness" in an Earth-side scene should come from what's
  merged into it, not the rendering style.
- **Merged/Administration:** sterile, deliberately staged — the Flood
  Stage's "purpose-built arena" register (see
  `../../../../world/places/the-flood-stage.md`) is the model: a space built
  for broadcast, not for the people standing in it.

## Layer 3 — Per-Node Detail

Write this fresh per node: the specific layout, key terrain features
(cover, hazards, choke points, anything an Approach in that node actually
calls back to), lighting/time of day, and scale cues. Pull directly from
that node's own **Situation** prose rather than inventing new geography —
the map should match what the node already says is there.

## Where this lives in an encounter file

Add a **Battlemap Prompt** entry under whichever node needs a map, same
placement convention as a Token Prompt in an NPC file — a fenced code
block with Layer 1 + Layer 2 + Layer 3 already folded into one paragraph,
ready for the generation script to pull out directly:

````markdown
**Battlemap Prompt.**

```
Top-down tabletop battlemap, straight overhead angle, evenly lit with no
hard directional shadows obscuring terrain, clean enough to drop a grid
over without losing readability. No characters, miniatures, or tokens in
the scene — terrain and set dressing only. [per-world palette cues].
[per-node detail].
```
````

Don't pre-generate one for every node in every encounter — add it once a
table's actually about to need the map, the same discipline
`monster-art-style.md` uses for Token Prompts.

## Generating from the prompt

`tools/image-gen/generate_battlemap.py` prepends the LoRA's trigger words, appends
`battlemap.extra_detail` from `tools/image-gen/config.yaml` (a generic "rich, varied,
several distinct points of interest" line), and adds the LoRA tag. So a Battlemap
Prompt should stay about **terrain and the node's specific hazards**; don't spend words
asking for "interesting details" in each one. The negative prompt already rejects
angled views, parchment, borders, legends and text. See `encounter-weaver/SKILL.md`
step 9 for the batch-and-pick workflow.

## Keep the prompt short — long prompts stop producing battlemaps

Learned 2026-10-07 on three maps. Long Layer 3 paragraphs (60-120 words, a dozen
objects, edge-by-edge layout, lighting talk) made SDXL abandon the top-down
battlemap and draw an **angled landscape photo** or a **city-block plan** instead:
in the first batches only 0-1 of 4 images were usable battlemaps, and several carried
legend text. Rewriting the same scenes shorter fixed it.

Rules for the per-node paragraph:

- **One sentence of terrain, one or two of dressing, about 45-70 words in total.**
  Name the place, then 4-6 concrete things. Cut everything else.
- **Say "seen from directly above" once, right after the place noun** ("a ruined
  parking lot seen from directly above, ..."). Don't rely on Layer 1 alone.
- **Drop words that imply a viewpoint or a scene rather than a surface:** facade,
  tower, canopy, sky, horizon, daylight, dappled, sunlight, shadows, "camp", "wagon
  carrying", and anything that only makes sense from the side. Say "windmill
  ruin", not "windmill tower".
- **Don't lay out edges** ("along the top edge... along the bottom edge...").
  SDXL ignores it. Put the camp, doors or Pylon on the map in Roll20, or
  describe them once as "at one end".
- **Prefer ground-level surfaces to landmarks:** cracked asphalt, hardpan, moss,
  pool, rubble. Landmarks the node needs can be tokens.
- **Expect about 1-2 usable maps in 4 even with a short prompt.** That's normal at `--count 4`; if none is
  top-down, shorten again rather than adding more detail.

**Verified 2026-10-07:** a deliberately new scene written to these rules (a space
station deck over Jupiter, about 45 words) produced 4 of 4 top-down battlemaps. The
one thing it dropped was the "outside the map" backdrop: Jupiter showed up only as
orange accents. Backdrops seen *through* a window, over an edge or beyond the map
don't survive; add them in the VTT.

Before and after (mall parking lot):

```
BEFORE (1 of 4 usable; the rest were a street-level garage photo and two city plans):
...a large, broken-down shopping-mall parking lot seen from directly above,
cracked grey asphalt with weeds, dandelions and grass pushing up through every
seam, faded white parking-space lines, oil stains, a few rusted abandoned
sedans and a station wagon with flat tires parked at angles, a toppled light
pole..., Along one short edge of the map, the beige concrete facade of the mall...

AFTER (1 of 4 usable, and it was a clean, table-ready map):
...a ruined shopping-mall parking lot seen from directly above, cracked grey
asphalt with weeds growing through the cracks, faded white parking-space lines,
many rusted abandoned cars parked at angles, a toppled light pole, overturned
shopping carts.
```

## Worked example

**[The Preening Grounds](../../../../world/places/the-preening-grounds.md)**,
Faerun-origin wetland, cracking apart under the quake:

```
Top-down tabletop battlemap, straight overhead angle, evenly lit with no
hard directional shadows obscuring terrain, clean enough to drop a grid
over without losing readability. No characters, miniatures, or tokens in
the scene — terrain and set dressing only. Natural fantasy wetland
terrain — reed beds, black standing water, packed mud hummocks, weathered
stone ruins half-submerged at one edge — lit like an ordinary overcast
day, nothing about the lighting itself reading as wrong. Several jagged
cracks run through the mud and shallow water, one already a dry-edged
fissure wide enough to be a hazard, water visibly draining into it at one
corner of the map.
```
