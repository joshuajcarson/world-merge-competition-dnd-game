---
name: "The Color Game"
title: "The Color Game"
slug: the-color-game
type: encounter
origin: merged
tags: [blood-bowl, briarwood-mall, agent, regicide, survival, flood, multi-threat, meridian-peak]
party_tier: "level 3"
party_size: "4"
created: 2026-08-28
updated: 2026-08-28
source: encounter-weaver
player_known: false
---

# The Color Game

**Note on party tier.** Not confirmed by the table — inferred from actual
play. Session 1's recap logs two explicit level-ups (after Gnashwhisker,
then again after the Fearus Dungeon); Session 2's recap logs none. Built for
**level 3, party of 4** on that basis. Rescale Combat Notes if the table is
actually somewhere else by tonight.

## Premise

Mid-morning, mid-[Blood Bowl](../world/lore/the-blood-bowl.md) countdown,
time freezes and [Agent](../world/npcs/agent.md) opens with something
closer to a complaint than an announcement: disappointing how many people
are still surviving, more disappointing that almost none of the *interesting*
ones — the higher-profile, higher-level ones — are getting sick along with
everyone else. Then, brighter: every fragment should have royalty by now,
and the fastest way to a crown is regicide. Real prize talk follows — a
game, for a leadership seat, tonight.

**The Color Game.** Seven tokens, one for each band of the electromagnetic
spectrum reskinned as "colors" for the cameras — radio, microwave, infrared,
visible, ultraviolet, x-ray, gamma. Seven leadership seats going into the
Blood Bowl. Whichever fragment has one of its own people physically holding
a color's token when the game ends wins that seat, and the seat carries a
**Hazard Nomination** — the right to name another fragment for the worst
threat Agent has queued up for the Bowl itself.

Agent pulls delegations onto the floor for the reveal — Briarwood's own,
plus [Scornubel](../world/places/scornubel.md)'s (represented, to her own
visible unhappiness, by [Miriel Ashgrove](../world/npcs/miriel-ashgrove.md),
who the Coster Council could spare on an hour's notice and nobody else
could), plus a delegation nobody's met: **[Meridian Peak](../world/factions/meridian-peak.md)**,
a private Colorado wellness-and-survival compound merged in as its own
Earth fragment, led by a woman who introduces herself as **Sovereign
[Helena Marsh](../world/npcs/helena-marsh.md)** before Agent's even
finished talking.

What none of this mentions out loud: something is already rising through
Briarwood's fragile, merge-stitched geography underneath the game floor.
See **The Aether Tide**, below the node graph — it isn't a clock the party
gets told about, and when it finally swallows the floor, the game ends
whether anyone's ready or not.

## Escalation Trigger(s)

Three, doing different jobs:

1. **Ambient — Regicide Attempts & Wandering Threats.** Rolled every time
   the Aether Tide rises a tier (see below). Not mandatory combat, but a
   live possibility from the moment Agent's announcement ends, at whatever
   node the party happens to be in.
2. **Hard, local — The Gamma Vault (Node D).** Meridian Peak's security is
   already staged to hold the isotope capsule. Approaching it puts combat
   within one bad roll's reach — talking, trickery, and stealth all remain
   live options throughout, and their guards would rather retreat than die
   for one token (see Combat Notes).
3. **Hard, global — Submerged (Node E).** The instant the Aether Tide hits
   its final tier, the competition ends, full stop, regardless of what node
   the party is in. Not rolled. See The Aether Tide.

## Party

- **Tier/level:** Level 3 (inferred — see note above).
- **Assumed size:** 4, matching this table's actual roster across Sessions
  0-2 rather than the campaign's usual 3-4 default.
- Nothing at this tier is meant to be a fair fight against a Tide-Titan —
  see below. The Meridian Peak confrontation and the wandering-threats table
  are the fights actually sized for this party.

## Node Graph

{% raw %}
```mermaid
flowchart TD
    A{{"A · Agent's Decree & the Color Game"}}
    B["B · The Game Floor"]
    C["C · Working the Minor Stations"]
    D[["D · The Gamma Vault<br/>(combat becomes a live option)"]]
    E{{"E · Submerged: Time's Up<br/>(hard trigger — fires from anywhere)"}}

    EndCrowned(["Ending: Crowned Above the Waterline"])
    EndWet(["Ending: A Wet Victory"])
    EndSovereign(["Ending: The Sovereign's Seat"])
    EndChaos(["Ending: Drowned Chaos"])

    A --> B
    B -->|"pick a station"| C
    B -->|"commit to the featured seat"| D
    C -.->|"tide rises, or party commits"| D
    C -.->|"Aether Tide reaches Submerged"| E
    D -.->|"Aether Tide reaches Submerged"| E
    B -.->|"Aether Tide reaches Submerged"| E
    D -->|"seat won clean"| EndCrowned
    D -->|"seat won, cost paid"| EndWet
    D -->|"Meridian Peak keeps the seat"| EndSovereign
    E --> EndChaos
    E -.->|"most seats already resolved"| EndCrowned
    E -.->|"most seats already resolved, at a cost"| EndWet
```
{% endraw %}

Node B is a hub, not a gate — the party can work minor stations, commit to
the Gamma Vault, or bounce between both in any order. The dotted edges into
E are the Aether Tide's hard deadline; it can fire from anywhere, at any
point in the party's own plan, and doesn't wait for them to be ready.

### Node A — Agent's Decree & the Color Game

**Situation:** Time freezes. Agent's voice, casual and a little bored,
opens with the "disappointing survival numbers" line, pivots to the
royalty-and-regicide announcement, then brightens into the Color Game
reveal — rules, stakes, and the delegations pulled onto the floor in real
time: Scornubel's Miriel, visibly unhappy about being volunteered; Meridian
Peak's Marsh, already using the word "Sovereign" like she's rehearsed it.

No roll — this is Agent's scripted opening. Give the party one beat to
react (react to the decree, size up Marsh, check on Phil) before Node B
starts moving.

---

### Node B — The Game Floor

**Situation:** The fountain court and promenade, restyled overnight into
seven stations spread across both levels. Other delegations are visibly
working the floor — Briarwood residents pitching in informally, Scornubel
guards flanking Miriel, and Meridian Peak's security detail: armed,
disciplined, and unnervingly calm, physically moving weaker searching
contestants — refugees, a couple of kids — out of their way without
acknowledging them as people. Distant water-sound is already audible,
more curiosity than threat yet (Aether Tide, Tier 1).

**Approaches:**
- *Read the floor before committing* — DC 10 (Investigation or
  Perception). Success: the party clocks which stations are genuinely
  contested versus which nobody's bothered with yet, plus a first glimpse
  of something Meridian Peak is keeping out of sight near their staging
  area — a seed for Node D's manifest.
- *Talk to another delegation* — DC 5 (Persuasion or Insight, target
  varies). Success against Miriel: she admits, quietly, she didn't ask for
  this and would rather it be over than won. Success against a Meridian
  Peak guard (DC 10 Insight instead): the party catches the specific,
  professional unease of being sized up like livestock, not like a threat.
- *Just start working a station* — no roll. Heads straight to Node C or,
  if the party wants to commit early, Node D.

**Complications available here:** pull from the bank, or use "someone
else is also reading the floor" — a generic rival contestant running the
same recon, an opening for cooperation or petty sabotage.

---

### Node C — Working the Minor Stations

**Situation:** Six of the seven stations — everything but Gamma — share the
same shape: figure out what the object has to do with its color, then hold
onto it against whoever else wants it. This node represents that loop and
can be revisited for any of the six, in any order, as many times as the
party has runway for before the tide or their own choices end the scene.

| Color | Token | Deduce | Hold | Flavor note |
|---|---|---|---|---|
| Radio | A CB radio handset | DC 10 | DC 10 | Low stakes, mostly texture. |
| Microwave | A garage door opener | DC 5 | DC 10 | The obvious one; everyone gets this fast. |
| Infrared | A forehead/fever IR thermometer | DC 10 | DC 10 | DC 15 (Medicine) extra: it's reading *something* about whoever's holding it — a quiet echo of Agent's "getting sick" line, not an explained one. |
| Visible | A laser pointer | DC 10 | DC 15 | Reads as a sniper's sight from across the floor — drawing it near a royal can trigger a false Regicide Attempt roll (DM's call). |
| Ultraviolet | A bug zapper's UV tube | DC 10 | DC 10 | Glass and a little mercury — broken roughly, treat as a minor hazard (1 point of damage, no lasting effect) rather than a real danger. |
| X-ray | Vintage "X-ray Specs" novelty glasses | DC 5 | DC 5 | Pure comedy, no danger. The DM should let this one be funny. |

**Approaches (apply to whichever token the party is working):**
- *Deduce it* — DC per table above (Investigation).
- *Hold it against a rival claimant* — DC per table above (contested, if
  someone else is also going for it; otherwise treat as the listed DC
  straight).
- *Cause chaos to cover a grab* — DC 15 (Deception or Sleight of Hand).
  Success: token secured cleanly. Failure or success either way: triggers
  one complication elsewhere on the floor (a Regicide Attempt roll, a
  Wandering Threat, or an Aether Tide tier — DM's pick, see below).

**Complications available here:** the bank, plus the per-token flavor notes
above.

---

### Node D — The Gamma Vault

**Situation:** A separate, guarded alcove — a former Sears service bay,
repurposed overnight — holds Gamma's token: a smoke detector's
americium-241 capsule, in a lead-lined display case, ringed by Meridian
Peak's own security. They already treat this seat as theirs. Half-hidden
nearby, if anyone looks: a clipboard manifest and a fenced-off holding area
where a handful of arrivals Meridian Peak judged "non-viable" have been cut
loose from care — the hard evidence of what their medicine is actually for.

**Approaches:**
- *Talk or bluff past the guards* — DC 15 (Persuasion or Deception). They're
  disciplined, not stupid, but success gets the party close without a
  fight.
- *Stealth in* — DC 15 (Stealth). The vault is watched, not omniscient.
- *Search the staging area for the manifest* — DC 10 (Investigation),
  independent of the token grab itself. This is how the party gets hard,
  portable evidence of the culling, whether or not they walk out with the
  token.
- *Force it* — combat resolution. See Combat Notes. A guard drawing a
  weapon without yet attacking is its own beat — DC 10 to talk it back down
  before anyone swings.

**What ends this without a kill:** Sovereign Marsh calls a retreat the
instant the optics turn against her on camera — she's performing for the
same broadcast Agent is running. Her guards fall back rather than die for
one token; see Combat Notes.

**Complications available here:** the bank, plus the capsule itself — bare
handling of the americium capsule risks exposure (DC 13 Constitution save
per round held ungloved/uncontained; failure: 1d4 necrotic damage,
cumulative). A container or improvised shielding (lead apron, thick glass)
negates this entirely — a smart party solves it rather than eating the
damage.

---

### Node E — Submerged: Time's Up

**Situation:** Fires the instant the Aether Tide reaches its final tier —
see below — regardless of where the party is or what they were mid-doing.
Nothing is rolled here. Agent calls the game the second the floor goes
under; whatever's held at that moment is final. Give the party one beat to
grab what they're carrying and get to real high ground before resolving
into an ending.

---

## Endings

- **Ending: Crowned Above the Waterline.** The party (or Briarwood, via the
  party's work) holds the Gamma seat plus a real haul of minor tokens, no
  royal was lost, and the evacuation was clean. Briarwood gets genuine
  leadership standing going into the Blood Bowl; the manifest, if found,
  exposes Meridian Peak publicly. The strongest outcome, and it should feel
  earned rather than default.
- **Ending: A Wet Victory.** The party wins the Gamma seat or most of the
  minor tokens, but it cost something — a regicide attempt landed, a Titan
  redirect backfired, or the evacuation was chaotic rather than clean. Still
  a win Briarwood can use, just an expensive one.
- **Ending: The Sovereign's Seat.** Meridian Peak secures Gamma. Marsh's
  Hazard Nomination is now a real, hanging threat over the next Blood Bowl
  session — the party got out, but ceded real ground, and Meridian Peak is
  now a returning antagonist with actual standing.
- **Ending: Drowned Chaos.** The Aether Tide reaches Submerged before much
  of anything got resolved. Agent calls the game early — great television,
  bad for everyone's actual standing. Tokens end up scattered or unclaimed,
  a regicide attempt may have landed unnoticed in the confusion, and someone
  might still be unaccounted for below the waterline. A genuine cliffhanger,
  not a failure state — pick up the loose ends next session.

## The Aether Tide

Not a countdown stated to the players — narrate it the way Swan Song
narrates its own rising water ("it's past your knees on the lower level
now," "the escalator's the only dry way up left"), and let the party draw
their own conclusions about how much runway remains. This is also the
clock the whole encounter runs on: it decides how many stations are
reachable, when Tide-Titans first appear, and when the game ends outright.

1. **Ankle-deep.** Distant water-sound, no mechanical effect. Baseline,
   present from Node A onward.
2. **Knee-deep, lower level.** Lower-level stations (DM assigns roughly
   half of the six minor stations here) become difficult terrain. **First
   Tide-Titan sighting**, at a distance — see below; the avoid-or-redirect
   subsystem goes live from here on.
3. **Waist-to-chest deep, lower level; upper level flooding at its edges.**
   Most remaining lower-level stations need DC 15 instead of their listed
   DC just to reach. Titans are now close enough to be a direct risk if
   noticed, not just a distant shape.
4. **Submerged.** Fires Node E immediately, wherever the party is.

**The state rises one tier whenever:** the party fails an approach roll at
Node C or D; a fight at Node D runs more than a couple of rounds; the party
is noticed by a Tide-Titan and doesn't successfully evade or redirect it; or
the DM's pacing calls for it after a quiet stretch. **Roll one Regicide
Attempt and consider one Wandering Threat every time the tier rises** — this
is the encounter's actual pacing engine, replacing a hard scene-by-scene
script with "the water decides when something happens next."

### Tide-Titans

Two or more towering, amphibious Aether predators, dragged in with the tide
itself rather than arriving on their own — the same "leviathans in the
ocean" register the primer establishes for the Aether world, just close
enough now to be a table problem. Dumb, food-and-noise-and-panic driven, not
tactical. **Not a fair fight at this tier — CR 8+, explicitly meant to be
avoided, not fought.** See Combat Notes for what happens if the party
forces the issue anyway.

**Approaches, once a Titan is nearby (Tier 2+):**
- *Stay unnoticed* — DC 15 (Stealth).
- *Redirect it onto someone else* — DC 15 (Deception or Sleight of Hand),
  using noise, blood, or a marked target — a rival delegation's own
  commotion, a thrown noisemaker, anything that reads as prey or threat
  louder than the party does. Success: the Titan commits to the new target
  instead. Failure: it notices the party instead, and the Tide advances a
  tier immediately regardless of the normal triggers.
- *Just run for high ground* — DC 10 (Athletics). Always available, no
  special downside beyond losing time — which is itself what feeds the
  Tide.

Redirecting a Titan onto Meridian Peak's people specifically is a legitimate
play the scene supports — a quieter, uglier way to hurt them than a direct
fight, and one the party may reach for on their own once they've seen the
manifest.

## Wandering Threats

Generic, actually-fightable monsters for pacing — separate from the
Tide-Titans, and separate from the Meridian Peak confrontation. Drop one in
whenever a Wandering Threat consideration comes up (see The Aether Tide) and
the DM wants a fight rather than another complication.

- **Faerun option — Kobold Raiders.** Reuse [Closing Time](closing-time.md)'s
  3-4 **Kobolds** (CR 1/8) plus one **Kobold packleader** (reskin **Goblin
  Boss**, CR 1) — flushed toward high ground by the same tide, opportunistic
  rather than organized.
- **Aether option — Aether Scavenger.** Reuse [Closing Time](closing-time.md)'s
  reskinned **Giant Vulture/Weasel** (CR 1/4-1/2), Drawn to Light — now
  drawn to the game floor's noise and lights instead.
- **Earth option — Corrupted Puma.** New: a Bellcross-area cougar that
  wandered too close to one of the mall's merge seams. Reskin a **Panther**
  (CR 1/4) with one added trait — **Aether Bleed**: the first time it's
  bloodied in a fight, it releases a burst of raw energy in a 5-foot radius;
  each creature in range must succeed on a DC 13 Constitution save or be
  knocked prone. Otherwise fights exactly like a base Panther.

## Regicide Attempts

Rolled per the Aether Tide's pacing (once per tier-up, plus DM discretion).
Reusable all event long — roll again each time. Targets: **Phil Bernard**,
**Miriel Ashgrove**, or **Sovereign Marsh**, whichever reads as most exposed
at the moment (DM's call, or roll a d3).

1. A grieving Sector 7 survivor, convinced Phil let people die during Mall
   Rats, rushes him with a scavenged blade.
2. A bystander radicalized by Agent's morning announcement takes a swing at
   whichever royal is standing in the open.
3. A Circuit-affiliated opportunist tries to stage Phil's death as an
   accident — a "loose" grille, a "stray" crossbow bolt — a quiet nod to
   [Wade Kessler](../world/npcs/wade-kessler.md)'s simmering Act 1 threat,
   not a confirmed hit.
4. One of Meridian Peak's own security detail tests whether Marsh's crown is
   actually defended, gauging the party's response as much as hers.
5. A panicked contestant grabs a station prop as an improvised weapon rather
   than attacking anyone directly — chaos, not malice.
6. Someone shouts "regicide" as a joke and three other people take it
   seriously at once — a scrum, not an assassin.
7. A Scornubel guard, overprotective of Miriel and spooked by the crowd,
   nearly attacks an innocent bystander who got too close to her.
8. The Aether Tide itself does the work — a Titan sighting (see above)
   panics a knot of people directly toward whichever royal is nearest,
   and nobody can tell if it's an attack or a stampede until it's on top
   of them.

**Miriel Ashgrove has no PC levels and won't fight back** — per her own
file, a serious attempt against her resolves in one round unless the party
physically intervenes. Play any attempt on her as a rescue the party has to
choose to make, not a fight she survives on her own.

## Complication Bank

- **A token's in the water.** Something dropped or knocked loose during a
  scramble is now floating, retrievable but exposed.
- **A rival delegate asks for help.** A generic contestant, overwhelmed,
  asks the party for aid at a station — cooperation or a wasted turn,
  their call.
- **Somebody recognizes Meridian Peak.** A Briarwood resident who watched
  too much cable news pre-merge places the compound's name from a real,
  damning pre-merge exposé — a rumor the party can use, not proof by
  itself.
- **A station prop floats away mid-search**, forcing a choice between
  finishing the search and chasing the prop before it's lost for good.

## Combat Notes

- **Meridian Peak security** (Node D): 2 **elite guards** — reskin
  **Veteran** (CR 3) — plus 2-3 **rank-and-file** — reskin **Guard**
  (CR 1/8). Disciplined, not fanatical; see "what ends this without a kill"
  above.
- **Sovereign Marsh** — no PC levels, command presence only. Reskin a
  **Noble** or **Spy** (CR 1) with a command-flavored feature. She directs
  the fight and retreats early; she never melees.
- **Tide-Titans** — explicitly not sized for this fight. If the party
  forces an engagement anyway, treat as CR 8-10 brutes: a single slam or
  bite attack that deals lethal damage to a level 3 character on a hit.
  This number exists so the DM has something to adjudicate if a table
  ignores "avoid," not as an invitation to run a real fight here.
- **Wandering Threats** — see above; all sized to be winnable, unlike the
  Titans.
- **Party disadvantage factors:** by the time the party reaches Node D, they
  may already have spent resources on a Regicide Attempt, a Titan evasion,
  or a Wandering Threat. Size Node D's fight as attrition, not a fresh
  encounter.
- **What ends a fight without a kill:** Marsh's guards fall back once
  clearly losing or once she calls the retreat; the Titans were never
  fightable to begin with and simply move on once their attention shifts;
  wandering threats per their own listed behavior (kobolds rout, the
  Scavenger flees, the Puma disengages once bloodied and released its
  Aether Bleed).

---

[← Back to encounters index](README.md)
