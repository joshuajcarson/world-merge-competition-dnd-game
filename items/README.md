# Items

Generated magic items, one file per item, named `<slug>.md`. Written by the `magic-item-forge` skill.

## Entries

- [Cohort 18 Slag Ring](cohort-18-slag-ring.md) — Rare ring; salvage from the merge the Administration lost.
- [Mall Security Keyring](mall-security-keyring.md) — Uncommon wondrous item; a night guard's keys that lock any door for eight hours.
- [Cindercrest Commendation Fang](cindercrest-commendation-fang.md) — Uncommon wondrous item; Agent's on-camera reward fang, warns of danger and can track a fled beast.
- [Fulgurite Splinter](fulgurite-splinter.md) — Uncommon wondrous item; single-use, cut from a spent Fulgurite, crush it to release one Overcharge effect.
- [Protein Shake](protein-shake.md) — Common potion; a GNC shelf item, single-use, heals 2d4+2.
- [Ginsu Knife](ginsu-knife.md) — Common weapon; an As Seen On TV display unit, single-use, one devastating cut.
- [Mood Ring](mood-ring.md) — Common ring; a Spencer Gifts spinner-rack find, single-use, forces one honest answer.

---


Every file carries the frontmatter contract below so the GitHub Pages site can index items without per-file special-casing.

## Frontmatter contract

| Field | Type | Notes |
|---|---|---|
| `name` | string | Display name. |
| `title` | string | Same string as `name`. Jekyll reserves `name` for the filename, so the site reads `title`. |
| `slug` | string | Must match the filename. Lowercase, hyphenated. |
| `type` | string | Always `item`. This is what the site's index pages filter on — an entry without it renders nowhere. |
| `rarity` | enum | `Common`, `Uncommon`, `Rare`, `Very Rare`, `Legendary`, `Artifact`. |
| `item_type` | enum | `weapon`, `armor`, `wondrous`, `potion`, `scroll`, `ring`, `rod`, `staff`, `wand`. |
| `attunement` | `false` or string | The full attunement clause when true, e.g. `"Requires Attunement by a Cleric"`. |
| `origin` | enum | Which merged world it came from: `faerun`, `tiamat`, `aether`, `earth`, `administration`, `unknown`. |
| `theme` | string | Short motif phrase. |
| `tags` | list | Free-form, for site filtering. |
| `charges` | int | `0` if none. |
| `cursed` | bool | Curse mechanics live in `## DM Notes`, never in player-facing text. |
| `created` | date | `YYYY-MM-DD`. |
| `source` | string | `magic-item-forge`, or `manual` for hand-written items. |
| `player_known` | bool | **Publication gate.** Always `false` at creation. The site publishes only `true`. |

## Conventions

- Filenames are stable. Renaming an item means a new file plus a deliberate decision about the old one — the skill never overwrites an existing slug.
- Hand-written items are welcome; set `source: manual` and keep the same frontmatter fields.
- `player_known: true` is a DM action, not a generation-time default.
- The **Entries** list above is maintained by hand (by the skill on each write) so items stay reachable from the repo index. The Pages build will generate it from frontmatter instead, at which point the hand-maintained list goes away.

[← Back to index](../README.md)
