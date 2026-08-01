---
name: campaign-chronicle
description: Capture or draft session notes and worldbuilding flavor notes (NPCs, places, factions, lore) as structured markdown, cross-linked and reachable from the repo index. Use when the user wants to write up or log a session, record what happened at the table, add or draft an NPC, location, faction, or piece of lore, take campaign notes, or flesh out the world — including phrasings like "write up session 4", "here's what happened tonight", "add an NPC for the quartermaster", "make me a frontier town on the Aether side", or "note that the party burned the bridge".
---

# Campaign Chronicle

Turn raw session recall and worldbuilding ideas into structured, cross-linked notes that are always reachable from the repo index. Two jobs: **capture** what the user dictates, and **generate** new NPCs/places/factions/lore on request.

## Note types

| Type | Path | Numbered |
|---|---|---|
| Session note | `sessions/NN-slug.md` | Yes, zero-padded to 2 |
| NPC | `world/npcs/slug.md` | No |
| Place | `world/places/slug.md` | No |
| Faction | `world/factions/slug.md` | No |
| Lore | `world/lore/slug.md` | No |

Frontmatter contracts and required sections for each type are in `references/note-types.md`. Read it before writing any file.

## Procedure

### 1. Identify the job

- **Capture** — the user is telling you what happened or what exists. Their content is authoritative. Structure and file it; do not embellish it into fiction they didn't write.
- **Generate** — the user is asking you to invent. Read `world/session-zero-primer.md` (its `## DM Only — Tone Cues` section) first and match the setting, exactly as `magic-item-forge` does.

Mixed requests are normal ("session 4 happened, and invent the innkeeper they met"). Capture first, then generate, so the generated content fits what actually occurred.

### 2. For session notes: determine the number

Check `sessions/` for the highest existing `NN`. Next session is `NN+1` unless the user names one. Never reuse or overwrite a number — if the file exists, ask which they meant.

### 3. Write the note

Use `assets/session-note-template.md` or `assets/lore-note-template.md`.

Every note has a player-facing body and a `## DM Only` section. The split is load-bearing: the site cuts every `## DM ...` heading and everything after it, so **the DM section must always be last in the file**. When in doubt about which side something belongs on, put it in `## DM Only` — over-hiding is recoverable at the table, under-hiding is not.

Set `title` to the same string as `name`. Jekyll reserves `name` for the filename, so `title` is what the site actually displays.

Set `player_known: false` on creation. Flipping it is the user's call.

### 4. Resolve every proper noun

Scan the note for named NPCs, places, factions, items, and lore concepts.

- If a file already exists → link to it with a relative markdown link.
- If not → **create a stub** at the right path: complete frontmatter, one or two lines of description drawn from the context you were given, and `needs_detail: true`. Then link to it.
- Never leave a named entity as plain text, and never write a link to a file that doesn't exist.

Stubs are cheap and broken links are not. But don't stub incidental nouns — a thing gets a file when it has a name and could plausibly come up again.

### 5. Verify reachability — do not skip

Follow `references/navigation.md`. Trace an actual path from `README.md` to every file you created or modified this turn, and update indexes as needed so the path exists.

A note the user can only find by knowing its filename is not filed, it is lost. Report the path you traced in your response.

### 6. Report

State what you wrote, what stubs you created (these are the user's to-do list), and the reachability path. Flag anything you put in `## DM Only` that you suspect the user wanted player-facing.

## Guardrails

- Capture mode does not invent facts. If the user's recall is thin, write it thin and note the gap — do not fill it in with plausible fiction that later contradicts the table's memory.
- Generated content must not contradict `world/session-zero-primer.md`. In particular: the fourth world's identity is unrevealed. Never invent it.
- Session notes are dated. Ask for the real-world date only if it matters and isn't inferable; otherwise use today's.
- The `## DM Only` section is not a secure boundary — the raw markdown is readable to anyone with repo access. If the user writes something genuinely sensitive there, say so once.
