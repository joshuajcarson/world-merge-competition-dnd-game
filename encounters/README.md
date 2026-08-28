# Encounters

Extended, multi-phase encounters that blend skill challenges and combat into
one branching scene — one file per encounter, named `<slug>.md`. Written by
the `encounter-weaver` skill.

## Entries

- [Chase Through the Grand Opening](chase-through-the-grand-opening.md) — Session 0 chase through Briarwood Mall's grand opening that runs straight into the World Merge Event.
- [Aether Breach at Briarwood](aether-breach-at-briarwood.md) — a wounded, high-CR Aether predator breaks into the mall; the level 1 party must fight, herd, or scare it off before it flees.
- [Mall Rats](mall-rats.md) — a merge-displaced closet opens onto an Administration storage sector for a cancelled ratkin race; the level 2 party has to clear it, rescue a hostage, and beat the reseal clock.
- [Swan Song](swan-song.md) — a flooded shrine between Scornubel and Briarwood, guarded by the Swanfolk; the level 2 party pushes through a territorial flock and a tragic boss while the chantry itself floods behind them.
- [Closing Time](closing-time.md) — the level 2 party fortifies Briarwood Mall's real weak points before whatever's outside — an Aether scavenger or a Faerun kobold raid, DM's choice — tests whichever one they left undone.
- [The Color Game](the-color-game.md) — the level 3 party competes for a Blood Bowl leadership seat against a rival Earth fragment while a rising Aether tide (and the Titans riding it) forces everyone toward high ground before time runs out.

---

Every file carries the frontmatter contract described in
`.claude/skills/encounter-weaver/references/dc-guide.md` so the GitHub Pages
site can index encounters without per-file special-casing.

## Conventions

- Encounter files are prep material through and through — the whole document
  is DM-facing by default, so `player_known` stays `false` at creation. It can
  be flipped to `true` later, but only after adding a short, non-spoiling
  `## The Hook` section and moving everything else (Premise onward) behind a
  `## DM Only` heading — see the frontmatter contract in
  `.claude/skills/encounter-weaver/references/dc-guide.md` for the exact
  pattern. Never publish the raw file as-is; it has no built-in player-facing
  half.
- DCs follow this campaign's fixed ladder (5/10/15/20), not default 5e
  difficulty numbers. See the DC guide above.
- No enemy statting or fight-difficulty calls happen until the party's tier
  or level is known — a file may ship with its combat notes explicitly
  marked pending that answer.
- The **Entries** list above is maintained by hand (by the skill on each
  write) so encounters stay reachable from the repo index.

[← Back to index](../README.md)
