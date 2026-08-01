# world-merge-competition-dnd-game

Markdown files and skills for tracking the World Merge Competition sessions.

A D&D 5.5e campaign in which four worlds — a conquered Faerûn, an aether-saturated
world of apex predators, a magicless Earth with nuclear weapons, and one the
Administration hasn't revealed — are smashed together for the entertainment of
100,000 broadcast channels.

## Index

- [The World](world/README.md) — the Session 0 primer, NPCs, places, factions, and lore.
- [Sessions](sessions/README.md) — session notes and recaps.
- [Items](items/README.md) — magic items and the frontmatter contract they follow.

## Skills

DM tooling lives in `.claude/skills/`.

| Skill | Does |
|---|---|
| `magic-item-forge` | Drafts 5.5e magic items at a chosen rarity with setting-appropriate flavor. |
| `campaign-chronicle` | Captures or drafts session notes and world notes, cross-linked and indexed. |

## Conventions

Every note and item carries `player_known` in its frontmatter. It is `false` on
creation and is the gate that controls what a future GitHub Pages site shows to
players. `## DM Only` sections are never rendered to that site.

Note that this is a public repository: `player_known` and `## DM Only` control
what the *site* renders, not who can read the raw files here.
