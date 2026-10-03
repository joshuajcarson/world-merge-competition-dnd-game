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
