# Encounters

Extended, multi-phase encounters that blend skill challenges and combat into
one branching scene — one file per encounter, named `<slug>.md`. Written by
the `encounter-weaver` skill.

## Entries

- [Chase Through the Grand Opening](chase-through-the-grand-opening.md) — Session 0 chase through Briarwood Mall's grand opening that runs straight into the World Merge Event.
- [Aether Breach at Briarwood](aether-breach-at-briarwood.md) — a wounded, high-CR Aether predator breaks into the mall; the level 1 party must fight, herd, or scare it off before it flees.

---

Every file carries the frontmatter contract described in
`.claude/skills/encounter-weaver/references/dc-guide.md` so the GitHub Pages
site can index encounters without per-file special-casing.

## Conventions

- Encounter files are prep material through and through — the whole document
  is DM-facing, so `player_known` stays `false` permanently rather than being
  a flag that later flips `true` the way an NPC or lore entry's might.
- DCs follow this campaign's fixed ladder (5/10/15/20), not default 5e
  difficulty numbers. See the DC guide above.
- No enemy statting or fight-difficulty calls happen until the party's tier
  or level is known — a file may ship with its combat notes explicitly
  marked pending that answer.
- The **Entries** list above is maintained by hand (by the skill on each
  write) so encounters stay reachable from the repo index.

[← Back to index](../README.md)
