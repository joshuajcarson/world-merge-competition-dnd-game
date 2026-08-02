---
name: "Encounter Name"
title: "Encounter Name"
slug: encounter-name
type: encounter
origin: faerun | tiamat | aether | earth | administration | merged | unknown
tags: []
party_tier: "levels X-Y"   # or null if not yet known — see references/dc-guide.md
party_size: "3-4"
created: YYYY-MM-DD
updated: YYYY-MM-DD
source: encounter-weaver
player_known: false
---

# Encounter Name

## Premise

What's happening, where, and what the party is trying to do or stop. Two or
three sentences of scene-setting a DM can reread cold and immediately know
what to run.

## Escalation Trigger(s)

The specific beat, threshold, or condition that raises the ceiling on what's
possible in this scene — most often the moment combat goes from off-the-table
to a live option. Name it precisely enough that the DM knows exactly when
it fires. Note what changes after it (new enemies/weapons available, higher
stakes, environment shift) — not a guarantee that combat happens, just that
it now can.

## Party

- **Tier/level:** from frontmatter `party_tier`.
- **Assumed size:** from frontmatter `party_size`.
- Note any combat-node content that's blocked pending this info.

## Node Graph

One `###` subsection per node. Keep the outline skimmable — a DM should be
able to run this cold at the table without rereading prose.

### Node A — [Name]

**Situation:** what the party is looking at / dealing with right now.

**Approaches:**
- *[Approach, e.g. "Push through the crowd"]* — DC N ([skill/ability]).
  Success: → Node B. Failure: [cost/complication] → Node C.
- *[Another approach]* — DC N. Success: [effect]. Failure: [effect].
- *(Combat option, if live at this node)* — [what triggers it, what it looks
  like]. See Party section for tier gating.

**Complications available here:** pull from the Complication Bank below, or
note ones specific to this node.

### Node B — [Name]

(repeat structure)

### Ending: [Name]

Each distinct resolution gets its own short ending — don't force convergence
to a single outcome. Cover at minimum: full success, full failure/loss, and
at least one messier in-between (caught but cost something, escaped but the
party learned nothing, fight won but the objective was lost anyway).

## Complication Bank

A grab-bag of reversals the DM can drop into *any* node on the fly, so a
table that goes off-script isn't left stranded. Draw these from the specific
scenario first (what's actually in this location, who's actually nearby)
before inventing generic ones.

- [Complication tied to the scene's specific location/props]
- [Complication involving a bystander or crowd]
- [Complication that offers the party an unexpected shortcut or advantage]
- [Complication that raises the stakes without forcing combat]

## Combat Notes

*(Only fill in once party tier is known — see references/combat-integration.md)*

- **Likely combatants:** role and rough toughness, not full statblocks —
  point to a tier-appropriate monster/NPC block to reskin.
- **Party disadvantage factors:** anything about how this fight would start
  (split up, mid-chase, resources already spent) that should make the DM
  size it lighter than a fresh, dedicated combat encounter.
- **What ends the fight without a kill:** surrender conditions, an escape
  route, a reason the enemy would rather flee — extended encounters rarely
  need combat to resolve by TPK-or-total-kill.

---

[← Back to encounters index](README.md)
