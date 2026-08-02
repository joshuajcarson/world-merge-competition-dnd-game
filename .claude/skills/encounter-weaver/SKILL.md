---
name: encounter-weaver
description: Design extended, multi-phase D&D encounters that blend skill challenges and combat into one branching scene — chases, heists, sieges, evacuations, anything where the party's choices should be able to turn a social/exploration problem into a fight (or vice versa) without the DM having pre-scripted it. Use whenever the user wants a "chase encounter," "extended encounter," "skill challenge," a scene that could "go loud," a multi-stage set piece, or describes something like "the party is chasing/pursuing someone through a crowd/building and it might turn into combat." Also use for escalating-event encounters (something big happens mid-scene, like a world-merge event, and the stakes or threat level jump). Saves the result as a structured markdown encounter file, cross-linked into the repo index like the other campaign notes.
---

# Encounter Weaver

Build encounters as a small branching graph of **nodes**, not a linear script. Each node is a situation the party is in; it offers a few approaches (mostly skill checks, sometimes combat, sometimes both), and each approach's outcome points to the next node. Combat is not a separate mode bolted onto the end — it's just what happens when a node's outcome (or the party's own choice) makes it happen.

This is the core idea worth holding onto: **the DM doesn't decide in advance whether this encounter has combat in it.** The party's rolls and choices decide, live at the table. Your job is to build a scene sturdy enough to survive being played in an order you didn't predict.

## Procedure

### 1. Get the premise

You need: what's actually happening (a chase, a heist, an evacuation, a negotiation gone sideways...), where, and what the party is trying to accomplish or prevent. If the user gives you a rich scenario (like a shoplifter chase through a mall), don't dilute it by genericizing — use their specific details as the actual node content, not as flavor sprinkled over a generic template.

Don't interrogate for every detail up front. Infer what you reasonably can from the setting (read `world/session-zero-primer.md`'s tone cues if this is set in the campaign world) and from any location file the scene is tied to. Ask only for things you can't infer and that materially change the design — see steps 2 and 3, which are both worth blocking on.

### 2. Ask what could trigger combat, and when

Every extended encounter needs at least one honest answer to "what would make this fight break out?" Sometimes it's a specific story beat the user already has in mind (a world-merge event landing mid-chase). Sometimes it's a threshold that emerges from play (the quarry gets cornered and has nothing left to lose, a complication goes badly, the party corners them somewhere with a weapon handy). Identify these as **triggers**, not certainties — a trigger makes combat *possible* at that node, it doesn't force it. The party or the quarry might still talk, flee, or fail their way past it without a single die of damage rolled.

If the user hasn't told you the trigger(s), ask. This is the one thing worth blocking on if it's unclear, because it's the hinge the whole encounter turns on.

### 3. Ask about the party — required before any combat content

**Never stat or suggest enemies, or size up a fight, until you know what tier or level the party is.** Ask directly if it's not stated. Don't assume — a "shoplifter" fight at level 2 and level 12 are unrecognizable. Once you know the tier, keep party size in mind too: assume 3–4 members unless told otherwise, and say so in the file so a DM reading it later knows what it was balanced for.

This only blocks the combat-flavored nodes. You can draft the skill-challenge nodes without this answer, but don't hand back a finished encounter with unstatted "TBD" fights — ask before you write those sections.

### 4. Read the DC ladder

Read `references/dc-guide.md` before assigning any DC. This campaign uses a specific four-rung ladder (5/10/15/20) tied to how plausible success is *without* training, not the default 5e ladder — use it consistently across every node.

### 5. Read how combat integration works

Read `references/combat-integration.md` for how to write the combat-capable nodes — how to size a fight for a tier without over-speccing it, how to write triggers so combat feels earned rather than scripted, and how to handle partial escalations (one person draws a weapon; it isn't yet a full fight).

### 6. Build the node graph

Follow `assets/encounter-template.md` for file structure. The shape to aim for:

- A handful of nodes (4–8 is typical for something chase-sized; fewer for a tighter scene, more if the user wants a sprawling set piece).
- Each node: the situation, 2–4 approaches with DCs, what success/failure/partial-success does, and where each outcome leads (another node, an ending, or a combat trigger).
- At least one **escalation point** — a moment, condition, or specific trigger (per step 2) where the ceiling on what can happen rises. Before it, combat might be off the table entirely or minor; after it, it's a live option.
- A **complication bank** — a short list of extra reversals the DM can drop into any node on the fly (a hostage, an improvised weapon nearby, a crowd that scatters or clots, a shortcut only some of the party notices) so a replay or a table that zigs where you predicted a zag doesn't leave the DM stranded. Draw these from the user's scenario details first, then invent more in the same register.
- Multiple endings are fine and good — chase caught, chase lost, fight won, fight fled, hostage situation resolved badly. Don't force convergence back to one outcome.

Resist the urge to make this a flowchart the party can "solve." The point isn't one correct path — it's a set of honest situations where different tools (skills, spells, combat, cleverness) plausibly work, and the DM adjudicates what the players actually try.

### 7. Read the setting's tone

If this encounter is set in the campaign world (not a one-off outside it), read `world/session-zero-primer.md`'s `## DM Only — Tone Cues` section, and read any linked location/NPC files (e.g. a mall's place file) so the encounter's specific beats — what's in the maintenance closet, who's in the food court — match established canon rather than contradicting it.

### 8. Write the file

Save to `encounters/<slug>.md`. Frontmatter follows the shared core contract (see `references/dc-guide.md` for the exact fields) with `type: encounter`. Unlike NPC/place/lore notes, an encounter file is prep material through and through — there's no player-facing half to preserve, so don't bother splitting sections into a `## DM Only` block. Just set `player_known: false` and leave it there; the site's publication gate hides the whole entry, which is the correct amount of hiding for a document that's entirely spoilers by nature.

**Never overwrite an existing file.** Check first, same as the other content skills.

Then add a line to the **Entries** list in `encounters/README.md` (create that index file from `assets/encounter-template.md`'s README pattern if this is the first encounter in the repo) so it's reachable from the repo root, and confirm `README.md` at the repo root links to `encounters/README.md` — add it to the root index if it's missing.

### 9. Report

Show the node graph in your response (a compact outline is enough — the file has the full detail), state the escalation trigger(s) clearly, and confirm the path you traced to make it reachable from the repo index. If you blocked on party tier for the combat nodes, say what you built without it and what's still pending.

## Guardrails

- Don't pre-decide the outcome. An encounter file that only has one route to "success" isn't an extended encounter, it's a puzzle with one answer.
- DCs are the campaign's ladder (`references/dc-guide.md`), not generic 5e defaults — a DC 15 here means "very hard without training," not "hard."
- No enemy stats or fight difficulty before the party's tier is known.
- Don't contradict established world/location/NPC files. If the scene uses a place or NPC that already has a file, read it and build around what's already true, not what would be more convenient.
- Big, dramatic mid-scene events (a merge event, a building collapse, a betrayal) belong to the user's story — don't invent one to fill a gap unless asked. If they haven't given you an escalation trigger, ask rather than inventing the campaign's next major beat yourself.
