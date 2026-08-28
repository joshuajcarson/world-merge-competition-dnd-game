# Note Types

All notes share a common frontmatter core, matching the contract in `items/README.md` so one site build can index everything.

## Shared core

| Field | Type | Notes |
|---|---|---|
| `name` | string | Display name / session title. |
| `title` | string | Same string as `name`. Jekyll reserves `name` for the filename, so the site reads `title`. |
| `slug` | string | Matches the filename (without `NN-` prefix for sessions). |
| `type` | enum | `session`, `npc`, `pc`, `place`, `faction`, `lore`, `handout`, `race`. Required — the site's index pages filter on it, so an entry without it renders nowhere. |
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

## PC (Player Character)

Path: `world/people/slug.md`

Extra fields: `player` (string — the real person at the table), `species` (string — usually the pre-merge self, e.g. `human`; note the post-merge form in `## Description` since that's the more interesting fact), `role` (string, one-line hook), `status` (`alive`, `dead`, `unknown`, `missing`), `first_seen` (session number the character debuted in, almost always `0`).

Sections: `## Description` (pre-merge self and the post-merge transformation — a PC's post-merge form is usually their single most interesting fact in this setting), `## Story So Far` (the arc in play, drawn from session Recaps and updated as sessions happen — link every session it draws from), `## DM Only` (table dynamics, mechanical notes, threads the DM is tracking for this character — optional; a thin or empty section is fine, unlike NPCs there's no default assumption there's a secret here).

A PC entry differs from an NPC entry in one structural way: there is no `## What the Party Knows` section, because the party already knows everything about their own characters — `## Story So Far` does that section's job without the fiction of incomplete information. Keep the file `player_known: false` on creation like any other note; flipping it to `true` is still the user's call, same as everything else.

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

## Race

Path: `world/races/slug.md`

For a monster race or people-group meant to be reused across multiple encounters and NPCs — a Monster Manual-style entry, not a single creature. Modeled on the shared-lore + specific-examples shape of a Manual's "Goblins" or "Orcs" entry: the race file carries what's true of the whole population, and 2+ separate NPC files (linked from it) carry the specific, nameable individuals a table actually meets.

Extra fields: `origin_species` (string — what they were before whatever changed them, e.g. `"Earth human"`), `challenge_band` (string, optional — a rough tier/CR range for reskinning guidance, e.g. `"CR 1/8-2, kobold/goblin tier"`; omit if not yet decided).

Sections: `## Description` (what they are, how they came to be this — a race's most interesting fact in this setting is usually the specific catastrophe or merge event that made them), `## Racial Trait` (the shared mechanical hook every member of the race gets, written narratively enough to reskin onto any tier-appropriate base statblock — not a full stat block itself), `## Notable Examples` (bulleted, linked to the individual NPC files that give the race faces — at least two, per a Manual's usual "the rank and file" plus "the named variant/leader" split), `## What the Party Knows`, `## DM Only`.

An NPC that belongs to one of these races still lives at `world/npcs/slug.md` under the normal NPC contract — set its `species` field to the race's name and link back to the race file in prose. The race file doesn't need a new NPC-contract field for this; a prose link both directions is enough to keep it navigable.

---

## Stubs

A stub is a real file with complete frontmatter, `needs_detail: true`, and a short `## Description` of one or two sentences drawn from whatever context produced it. It has the same sections as a full entry, left empty rather than omitted, so filling it in later is additive.

Stubs exist to keep links unbroken. They are not placeholders to be deleted — they are entries awaiting detail.
