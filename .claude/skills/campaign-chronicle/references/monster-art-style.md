# Monster Art Style — Image Generator Prompts

Campaign-wide convention for building image-generator prompts for monster
and NPC tokens. Confirmed default as of 2026-09-24 after the DM tried
several options against a test creature.

Every prompt is built from three layers, always in this order, folded into
one flowing paragraph (no labels) when handed to an image generator:

1. **Universal style** — identical text on every prompt, campaign-wide.
2. **Origin-world palette** — swapped based on the creature's `origin`.
3. **Per-creature detail** — written fresh for whatever's being illustrated.

## Layer 1 — Universal Style (locked default): Glitch-Corrupted Render

```
A 3D-rendered creature deliberately corrupted like a damaged digital file —
datamoshing artifacts, torn and smeared polygon edges, color-channel
splitting, streaks of pixel-sorted noise bleeding across parts of the
image, set against a flat dark void. [creature detail from Layer 3, with
the corruption's color drawn from Layer 2]. The overall effect should feel
like watching something try to render correctly and fail.
```

Use this exact framing sentence-for-sentence at the start and end of every
prompt; only the middle (the creature description) changes per subject.

## Layer 2 — Origin-World Palettes

Pick based on the creature's `origin` field. Describe the corruption itself
(the glitch streaks, color-channel splitting) as bleeding this color,
rather than just tinting the creature — the corruption should look like
it's native to that world.

- **Aether:** sickly, mold-green color-channel bleed and datamosh streaks.
- **Faerun:** cool, pale sage-green and moon-grey color-channel bleed,
  reading damp and still-water rather than toxic.
- **Earth:** harsh electric-blue and arc-white color-channel splitting —
  reads as a power surge or lightning strike rather than organic rot.
  (Confirmed against the Fulgurites, whose glassy fused skin patches are a
  natural in-fiction excuse for exactly this palette — reuse it for other
  Earth-origin subjects even without that justification.)
- **Merged/other:** not yet needed — pick whichever of the above reads
  closest, or blend two if the creature's origin genuinely straddles worlds
  (see Swanfolk, filed under Faerun despite being an Earth/Faerun fusion,
  since the swanmay half is what visually dominates).

## Layer 3 — Per-Creature Detail

Write this fresh each time: body plan, texture, pose, one small detail that
implies behavior or personality, and where on the body the corruption
should visibly concentrate (a wound, a weapon, a fused patch of skin — pick
something that already means something in the creature's own fiction).

**Worked examples on file**, for reference or reuse:

- **Aether Leprechaun (rank-and-file):** small, wiry, green-skinned
  humanoid, too many crooked teeth, clutching an old filthy sack (not a
  visible Doombow — see note below). See
  [Aether Leprechauns](../../../world/races/aether-leprechauns.md).
- **Warrenwright:** stocky, thick-clawed burrower, pelt part fur/part bark,
  corruption bleeding across the flank and tail-tip. See
  [Warrenwrights](../../../world/races/warrenwrights.md).
- **Swanfolk:** humanoid enough to stand upright, feathered enough that
  "person" is the wrong word, corruption rippling across the feathers like
  water damage. See [Swanfolk](../../../world/races/swanfolk.md).
- **Fulgurite:** an ordinary person a few days post-transformation, harsh
  blue-white corruption originating from the glassy fused patches of skin.
  See [Fulgurites](../../../world/races/fulgurites.md).

**Note on the Doombow.** The DM asked for the Doombow specifically left out
of Leprechaun token art — an old, filthy sack reads better visually and
still fits Gold Hunger. This is a token-art decision only; it does not
change the Doombow as a combat mechanic in
[Gildrot](../../../world/npcs/gildrot.md)'s statblock.

## When writing a new race or NPC file

Add a short **Token Prompt** entry under that file's `## DM Only` section
once art is actually needed — a single fenced code block with the full
three-layer prompt already assembled, ready to copy-paste. Don't
pre-generate these for every stub; add them when a table's about to need a
real token, the same way statblocks get filled in only once a tier is
known.
