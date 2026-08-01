# Note Types

All notes share a common frontmatter core, matching the contract in `items/README.md` so one site build can index everything.

## Shared core

| Field | Type | Notes |
|---|---|---|
| `name` | string | Display name / session title. |
| `title` | string | Same string as `name`. Jekyll reserves `name` for the filename, so the site reads `title`. |
| `slug` | string | Matches the filename (without `NN-` prefix for sessions). |
| `type` | enum | `session`, `npc`, `place`, `faction`, `lore`, `handout`. Required — the site's index pages filter on it, so an entry without it renders nowhere. |
| `origin` | enum | `faerun`, `tiamat`, `aether`, `earth`, `administration`, `unknown`, `merged`. Use `merged` for anything native to the combined world. |
| `tags` | list | Free-form, for filtering. |
| `created` | date | `YYYY-MM-DD`. |
| `updated` | date | Bump on every edit. |
| `source` | string | `campaign-chronicle` or `manual`. |
| `player_known` | bool | Publication gate. `false` on creation, always. |
| `needs_detail` | bool | `true` on stubs. Omit or `false` on full entries. |

---

## Session note

Path: `sessions/NN-slug.md`

Extra fields: `session_number` (int), `played` (date), `players_present` (list, optional).

Sections:

```markdown
# Session NN — Title

## Recap
Player-facing narrative of what happened. Past tense, readable months later
by someone who wasn't there. Link every named entity.

## Loose Threads
Unresolved hooks, open questions, promises the party made. Bulleted.

## Loot & Rewards
Items gained, linked to items/ files. Omit the section if nothing was gained.

## DM Only
What the players don't know: what was really going on, what you improvised,
what you're planning next, which rolls you fudged.
```

Keep the Recap to what the table actually experienced. If the party misunderstood something, the Recap reflects their understanding and `## DM Only` records the truth.

---

## NPC

Path: `world/npcs/slug.md`

Extra fields: `species` (string), `role` (string), `faction` (slug or `null`), `status` (`alive`, `dead`, `unknown`, `missing`), `first_seen` (session number or `null`).

Sections: `## Description` (what the players can observe — appearance, manner, one memorable detail), `## What the Party Knows`, `## DM Only` (true motives, secrets, statblock notes, what they'd do under pressure).

An NPC's `## Description` should give the DM enough to play them in one line of voice. Three adjectives is not a character; one specific habit is.

---

## Place

Path: `world/places/slug.md`

Extra fields: `region` (string), `settlement_type` (optional: `city`, `town`, `outpost`, `ruin`, `wilderness`, `structure`), `controlled_by` (faction slug or `null`).

Sections: `## Description`, `## Notable Locations` (bulleted, linked where they have their own files), `## What the Party Knows`, `## DM Only`.

In this setting, a place's most interesting fact is usually which world it came from and what it is now touching that it never should have.

---

## Faction

Path: `world/factions/slug.md`

Extra fields: `scope` (`local`, `regional`, `world`, `cosmic`), `disposition` (`ally`, `neutral`, `hostile`, `unknown`), `leader` (NPC slug or `null`).

Sections: `## Description`, `## Goals` (what they want, bulleted), `## Notable Members` (linked NPCs), `## What the Party Knows`, `## DM Only`.

---

## Lore

Path: `world/lore/slug.md`

For concepts, events, and rules of the world that aren't a person, place, or group — the merge itself, aether, the Administration's procedures, previous cohorts, the fate of a god.

Sections: `## Overview`, `## What the Party Knows`, `## DM Only`.

---

## Stubs

A stub is a real file with complete frontmatter, `needs_detail: true`, and a short `## Description` of one or two sentences drawn from whatever context produced it. It has the same sections as a full entry, left empty rather than omitted, so filling it in later is additive.

Stubs exist to keep links unbroken. They are not placeholders to be deleted — they are entries awaiting detail.
