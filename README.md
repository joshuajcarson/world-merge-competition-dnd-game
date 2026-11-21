# world-merge-competition-dnd-game

Markdown files and skills for tracking the World Merge Competition sessions.

A D&D 5.5e campaign in which four worlds — a conquered Faerûn, an aether-saturated
world of apex predators, a magicless Earth with nuclear weapons, and one the
Administration hasn't revealed — are smashed together for the entertainment of
100,000 broadcast channels.

The player-facing site: <https://joshuajcarson.github.io/world-merge-competition-dnd-game/>

## Index

- [The World](world/README.md) — the Session 0 primer, the party, NPCs, places, factions, and lore.
- [Sessions](sessions/README.md) — session notes and recaps.
- [Items](items/README.md) — magic items and the frontmatter contract they follow.
- [Encounters](encounters/README.md) — extended encounters blending skill challenges and combat.

## Repo layout

| Path | What |
|---|---|
| `world/`, `sessions/`, `items/`, `encounters/` | The campaign notes. Each folder has a `README.md` index for browsing on GitHub and an `index.html` that the site renders. |
| `assets/images/` | Portraits (`npcs/`, `races/`) and encounter maps (`encounters/<slug>/`), referenced from the notes. |
| `index.md`, `404.html`, `_config.yml`, `_layouts/`, `_includes/`, `assets/css/`, `assets/js/` | The Jekyll site published by GitHub Pages from `main`. |
| `tools/image-gen/` | Local Stable Diffusion (Forge) scripts that generate the portraits and battlemaps. See its [README](tools/image-gen/README.md). |
| `tools/roll20/` | Roll20 prep: grid-sized maps, transparent tokens, statblock data, and a sheet-filling console helper. See its [README](tools/roll20/README.md). |
| `.claude/skills/` | Claude Code skills that write the notes (below). |
| `CLAUDE.md` | Instructions for Claude Code, including the git workflow (all work goes through the `claude-code` branch and a PR). |

## Skills

DM tooling lives in `.claude/skills/`.

| Skill | Does |
|---|---|
| `magic-item-forge` | Drafts 5.5e magic items at a chosen rarity with setting-appropriate flavor. |
| `campaign-chronicle` | Captures or drafts session notes and world notes, cross-linked and indexed. Also writes Token Prompts for portrait art. |
| `encounter-weaver` | Designs extended encounters that branch between skill challenges and combat. Also writes Battlemap Prompts. |

## Conventions

Every note and item carries `player_known` in its frontmatter. It is `false` on
creation and is the gate that controls what the GitHub Pages site shows to
players. `## DM Only` sections are hidden from the player view of that site.

Note that this is a public repository: `player_known` and `## DM Only` control
what the *site* shows, not who can read the raw files here.

## DM view of the site

Add `?dm=1` to any page URL to reveal every `## DM Only` section and every entry
`player_known: false` withholds:

    https://joshuajcarson.github.io/world-merge-competition-dnd-game/world/?dm=1

The setting sticks for that browser tab, so links keep working without the
param, and it clears when the tab closes. `?dm=0` — or the "Back to player view"
link in the banner — returns to the player view immediately.

It is a display switch, not a lock: on a static site the DM text is in the HTML
that every visitor downloads, so a player who views source can read it. Same
posture as the public repo. Use it for "not at the table right now", not for
"players must never see this".
