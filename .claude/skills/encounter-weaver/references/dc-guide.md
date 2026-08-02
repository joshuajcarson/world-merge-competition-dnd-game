# DC Ladder & Frontmatter Contract

## The DC ladder

This campaign uses a fixed four-rung ladder for every check in an extended encounter. It's calibrated to "how plausible is success without training," not to the default 5e difficulty table — don't reach for generic DCs (10/15/20/25/30) out of habit.

| DC | Meaning | Use for |
|---|---|---|
| **5** | Should usually succeed, even completely untrained. | The default "you can just try this" check — ducking under a table, shouting for help, noticing something in plain sight. A DC 5 exists mostly so a bad roll or bad modifier can still fail it, not to gate the action. |
| **10** | Difficult without training. A relevant skill or ability makes it comfortable; going in cold is a real risk. | Most of the encounter's meaningful checks live here — reading a crowd, picking a simple lock at speed, keeping pace in a foot chase. |
| **15** | Very hard without training. Even a competent generalist struggles; someone actually skilled in this can still fail. | The checks that should feel like a genuine swing — vaulting a barrier one-handed, talking down someone mid-panic, tracking a trail that's already gone cold. |
| **20** | Shouldn't be attempted without training at all — and even trained characters will likely still fail. | Reserve for the encounter's hardest single ask, or for something a character with no relevant background genuinely has no business trying. This is a "you probably don't, and here's what happens when you don't" DC, not a normal obstacle. |

Practical notes:

- Don't inflate DCs to make an encounter "hard." Difficulty comes from stacking checks, from failure having real costs (not just "nothing happens"), and from the clock the scene runs on — not from every check sitting at 15+.
- A node offering only one DC-20 approach and nothing else is a trap, not a challenge. Most nodes should have at least one DC 10 or lower option so an undertrained party still has something to try.
- State the DC next to each approach in the file. Don't make the DM compute it at the table.

## Frontmatter contract for encounter files

Matches the shared core used by other note types in this repo (`items/README.md`, `world/*` notes), with encounter-specific fields added.

| Field | Type | Notes |
|---|---|---|
| `name` | string | Display name of the encounter. |
| `title` | string | Same string as `name` — Jekyll reserves `name` for the filename. |
| `slug` | string | Matches the filename. |
| `type` | string | Always `encounter`. |
| `origin` | enum | `faerun`, `tiamat`, `aether`, `earth`, `administration`, `unknown`, `merged` — whichever world the scene is set in. |
| `tags` | list | Free-form; include the encounter's shape, e.g. `chase`, `heist`, `siege`, `social`. |
| `party_tier` | string or `null` | The level/tier the combat nodes are balanced for, e.g. `"levels 3-4"`. `null` if not yet known — see below. |
| `party_size` | string | Usually `"3-4"`. Note if the user specified something else. |
| `created` | date | `YYYY-MM-DD`. |
| `updated` | date | Bump on every edit. |
| `source` | string | `encounter-weaver`. |
| `player_known` | bool | Always `false`. Encounter files are prep material in their entirety — there's no player-facing half to publish, so this flag just keeps the whole thing off the players' site. It isn't meant to flip `true` later the way an NPC or lore entry's might. |

If `party_tier` is `null` because the user hasn't answered yet, say so plainly in your response — don't ship combat-node content that depends on it.
