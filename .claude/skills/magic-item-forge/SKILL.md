---
name: magic-item-forge
description: Draft D&D 5.5e magic items with setting-appropriate flavor text at a chosen rarity, and save them as structured markdown. Use when the user asks for a magic item, magical item, enchanted weapon or armor, wondrous item, potion, artifact, loot, treasure, or hoard contents — including phrasings like "make me a rare wondrous item", "I need three uncommons for a dragon hoard", "cursed item for the rogue", or "something legendary tied to the world's history".
---

# Magic Item Forge

Draft magic items that are mechanically legal for 5.5e at their stated rarity and that sound like they came from *this* campaign world rather than a generic fantasy shelf.

## Procedure

### 1. Gather inputs

**Rarity is required.** Everything else is optional and should be inferred rather than interrogated.

- If the user did not state a rarity (or a party level you can map to one), ask for it. That's the one question worth blocking on.
- If they gave a party level instead, map it: levels 1–4 → Common/Uncommon, 5–10 → Rare, 11–16 → Very Rare, 17+ → Legendary.
- Optional inputs to use if offered, infer if not: item type, theme/motif, intended recipient (class or character), cursed or not, whether it should carry a story hook.

Do not ask a list of clarifying questions. One item is cheap to redo; a five-question intake is not.

### 2. Read the world's tone

Read `world/session-zero-primer.md` — especially its `## DM Only — Tone Cues` section — **before naming anything**. Names, materials, and provenance should draw on the setting's own vocabulary.

If that file is missing, empty, or still a placeholder, proceed with generic high-fantasy flavor and say so plainly in your response ("no world primer found, so this is setting-neutral — paste your lore and I can re-theme it").

### 3. Check the power budget

Read `references/rarity-budgets.md` and find the row for the chosen rarity. Stay inside it. The "Never exceed" line for each tier is a hard stop, not a suggestion — an item that breaks it is mislabeled, not creative.

### 4. Draft the item

Follow `assets/item-template.md` for structure and `references/flavor-craft.md` for the prose. Every item gets three flavor beats: appearance, provenance, quirk.

### 5. Write the file

Save to `items/<slug>.md` where `<slug>` is the item name lowercased, non-alphanumerics collapsed to hyphens (`Lantern of the Drowned Choir` → `lantern-of-the-drowned-choir`).

**Never overwrite an existing file.** Check first. If the slug is taken, either pick a distinct name or ask the user which they meant to keep — do not silently clobber a previous item.

Frontmatter must match the contract in `items/README.md` exactly, including `title` (same string as `name` — Jekyll reserves `name` for the filename, so `title` is what the site displays) and `player_known: false`. That flag is what gates publication to the players' site later; it is never `true` at creation time.

Then add a line for the item to the **Entries** list in `items/README.md`, so it is reachable from the repo index rather than only by knowing its filename:

```markdown
- [Item Name](slug.md) — Rarity type; one-clause hook.
```

### 6. Report inline

Show the full item in your chat response too — statblock and flavor both. The user should be able to react to it without opening the file. End with a one-line pointer to the path.

## Batch requests

"Five uncommons for a hoard" → one file per item, then a summary table in chat:

| Item | Type | Attunement | Hook |
|---|---|---|---|

Vary type and function across a batch — five variations on "a +1 weapon" is a failed hoard. Deliberately mix one utility item, one social/exploration item, and one combat item into any batch of three or more.

## Guardrails

- Rarity is a contract with the DM. If the concept the user described genuinely needs more power than the tier allows, build it inside the tier and say in your response what a bump to the next rarity would unlock.
- Cursed items only when asked for. When cursed, the curse goes in `## DM Notes`, never in the player-facing flavor.
- Do not invent contradictions with the world primer. If the primer says magic is scarce and industrial, don't hand out fey-blessed elven silverwork.
