#!/usr/bin/env python3
"""Write Roll20 5e NPC importer JSON (see JSON_STRUCTURE.md in
ByteBard97/roll20-5e-npc-json-importer) for the Act Two creatures.

Source of truth for the statblocks is the markdown in world/ and encounters/;
this file is a mechanical transcription. Run from the repo root:
    python tools/roll20/build_npcs.py
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "npcs"


def atk(name, type_, tohit, dist, dmg, dtype, desc, target="one target"):
    return {
        "name": name,
        "attack": {"type": type_, "tohit": tohit, "distance": dist, "target": target,
                   "dmg1": dmg, "type1": dtype},
        "desc": desc,
    }


GC = {"name": "Gnome Cunning",
      "desc": "Advantage on Intelligence, Wisdom and Charisma saving throws against magic."}

SEXT_TRAITS = [
    {"name": "Last Rites", "desc": (
        "Always knows the location of any dead creature within a mile. On its turn, if within "
        "5 feet of a corpse, it uses its action to eat it: the body is destroyed and anything "
        "carried is swallowed. Takes 1 round for a Medium or smaller body, 2 for Large, 4 for "
        "Huge. An eaten body cannot be raised or revived short of a wish. Swallowed items can "
        "be recovered only from the beast's remains.")},
    {"name": "Docile", "desc": (
        "Does not attack unless it takes damage, or something is taken out of its mouth or from "
        "under its muzzle. Calms again once the provocation is gone and there is a corpse to eat.")},
    {"name": "Toll", "desc": (
        "While it feeds or is startled, its bone-chimes ring, audible out to 300 feet "
        "(DC 10 Perception to hear it coming).")},
]

npcs = {}

npcs["obby-windlestraw"] = {
    "name": "Prelate Obby Windlestraw", "size": "Small", "type": "humanoid (gnome)",
    "alignment": "Lawful Evil", "ac": {"value": 15, "notes": "Wind Veil"},
    "hp": {"average": 52, "formula": "8d6+24"}, "speed": "25 ft., fly 30 ft. (hover)",
    "abilities": {"str": 8, "dex": 14, "con": 16, "int": 14, "wis": 16, "cha": 13},
    "saves": {"con": "+6", "wis": "+6"},
    "skills": {"religion": "+4", "persuasion": "+4", "performance": "+4"},
    "senses": "darkvision 60 ft., passive Perception 13",
    "languages": "Common, Gnomish, Auran", "cr": "4", "init_tiebreaker": "@{dexterity}/100",
    "bio": ("Priest of the Prince of Evil Air and leader of the Hush Concord. A very old gnome who "
            "hovers on his own updraft and flicks a lace handkerchief before he speaks. Breaks off "
            "at 13 hp or fewer, or when a camera turns on him."),
    "traits": [GC,
               {"name": "Wind Veil", "desc": "Ranged attack rolls against Obby have disadvantage while he is conscious and unrestrained."},
               {"name": "Held Breath", "desc": "Obby does not need to breathe. Stolen Breath and Pocket Calm effects do not impair him."}],
    "actions": [
        {"name": "Multiattack", "desc": "Obby makes two Gale Lance attacks."},
        atk("Gale Lance", "Ranged", "+6", "60 ft.", "2d6+3", "bludgeoning",
            "Hit: 10 (2d6 + 3) bludgeoning damage, and the target is pushed 5 feet."),
        {"name": "Stolen Breath (Recharge 5-6)", "desc": (
            "30-foot cone. Each creature makes a DC 14 Constitution saving throw. Fail: 22 (5d8) force "
            "damage and the creature cannot speak or cast spells with verbal components until the end "
            "of its next turn. Success: half damage only.")},
        {"name": "Pocket Calm (1/Day)", "desc": (
            "A 20-foot-radius sphere centred on a point within 60 feet goes completely still and silent "
            "for 1 minute (concentration). No sound passes in or out, gas and smoke are dispelled, and "
            "non-magical flame inside it goes out. No spoken spells inside.")},
    ],
    "reactions": [{"name": "Exhale", "desc": "When a creature within 5 feet hits him with a melee attack, it makes a DC 14 Strength saving throw or is pushed 10 feet."}],
}

npcs["tamberlock-flue"] = {
    "name": "Tamberlock \"Flue\" Gearwhistle", "size": "Small", "type": "humanoid (gnome)",
    "alignment": "Lawful Neutral", "ac": 14, "hp": {"average": 38, "formula": "7d6+14"},
    "speed": "25 ft.", "abilities": {"str": 9, "dex": 14, "con": 14, "int": 16, "wis": 11, "cha": 9},
    "senses": "darkvision 60 ft., passive Perception 10", "languages": "Common, Gnomish",
    "cr": "2", "init_tiebreaker": "@{dexterity}/100",
    "bio": ("The Hush Concord's tinker. Builds and crews the Gale Organ. Wants it to sing at full "
            "pressure at least once on camera; can be flattered or hired by someone who respects the machine."),
    "traits": [GC, {"name": "Machine Sense", "desc": "Flue knows the Gale Organ's exact Pressure at all times and notices tampering automatically."}],
    "actions": [
        atk("Spanner", "Melee", "+4", "5 ft.", "1d6+2", "bludgeoning", "Hit: 5 (1d6 + 2) bludgeoning damage."),
        atk("Valve Pistol", "Ranged", "+4", "30/90 ft.", "1d8+2", "bludgeoning",
            "Hit: 7 (1d8 + 2) bludgeoning damage, and the target is pushed 5 feet."),
    ],
    "bonus_actions": [{"name": "Crank", "desc": "Adds 1 Pressure to the Gale Organ while Flue is within 5 feet of it."}],
    "reactions": [{"name": "Reroute", "desc": "When the Gale Organ would discharge, Flue redirects its line by up to 45 degrees."}],
}

npcs["hushbound-skirmisher"] = {
    "name": "Hushbound Skirmisher", "size": "Small", "type": "humanoid (gnome)",
    "alignment": "Lawful Evil", "ac": 14, "hp": {"average": 22, "formula": "5d6+5"},
    "speed": "25 ft.", "abilities": {"str": 8, "dex": 14, "con": 12, "int": 13, "wis": 10, "cha": 8},
    "senses": "darkvision 60 ft., passive Perception 10", "languages": "Common, Gnomish",
    "cr": "1/2", "init_tiebreaker": "@{dexterity}/100",
    "bio": "Rank-and-file soldier of the Hush Concord, wearing a brass lung-pack of the Prince of Air's breath.",
    "traits": [GC, {"name": "Borrowed Breath", "desc": (
        "Once per short rest, as a bonus action: Gale Shove (DC 12 Str, push 15 ft and prone, 15 ft range), "
        "Stolen Breath (DC 12 Con, no speech or verbal spells until end of its next turn, 20 ft range), or "
        "Pocket Calm (10-ft-radius silence within 30 ft until the start of its next turn). Afterwards it has "
        "disadvantage on Strength checks and can't Dash until a short rest.")}],
    "actions": [
        atk("Bellows-Lance", "Ranged", "+4", "30/90 ft.", "1d8+2", "bludgeoning",
            "Hit: 7 (1d8 + 2) bludgeoning damage, and the target is pushed 5 feet."),
        {"name": "Breathless Puff (Recharge 5-6)", "desc": (
            "15-foot cone. DC 12 Constitution saving throw. Fail: 7 (2d6) bludgeoning damage and no speech "
            "or verbal spells until the end of its next turn. Success: half damage, no silence.")},
    ],
}

SEXTONBACK = {
    "name": "Sextonback", "size": "Huge", "type": "beast", "alignment": "Unaligned",
    "ac": {"value": 16, "notes": "natural armor, bone plates"},
    "hp": {"average": 168, "formula": "16d12+64"}, "speed": "20 ft.",
    "abilities": {"str": 22, "dex": 6, "con": 18, "int": 2, "wis": 11, "cha": 5},
    "senses": "blindsight 30 ft., passive Perception 10", "languages": "-", "cr": "6",
    "bio": "The Aether World's undertaker: a huge, gentle, sloth-like corpse-eater with a ridge of bone-chimes. Passive; the clock is the point.",
    "traits": SEXT_TRAITS + [
        {"name": "Bulwark", "desc": "Its flank provides total cover to creatures behind it."},
        {"name": "Slow Mass", "desc": "Moves through other creatures' spaces as if they were difficult terrain, but cannot end its move in one."}],
    "actions": [
        {"name": "Multiattack (provoked only)", "desc": "One Slam and one Trample."},
        atk("Slam", "Melee", "+9", "10 ft.", "2d10+6", "bludgeoning", "Hit: 17 (2d10 + 6) bludgeoning damage. Provoked only."),
        {"name": "Trample", "desc": "One Large or smaller prone creature in its reach makes a DC 16 Strength saving throw, taking 19 (3d8 + 6) bludgeoning damage on a failure, half on a success."},
    ],
    "reactions": [{"name": "Mournful Bellow", "desc": "When it first takes damage, every creature within 30 feet makes a DC 14 Wisdom saving throw or is frightened until the end of its next turn."}],
}
npcs["sextonback"] = SEXTONBACK
npcs["deacon"] = dict(SEXTONBACK, name="Deacon (adult Sextonback)",
                      bio="The Blood Bowl's mascot, the Cleanup Crew. One cracked chime that rings flat. Agent protects it: harming it costs ratings.")
npcs["verger"] = {
    "name": "Verger (Sextonback calf)", "size": "Large", "type": "beast", "alignment": "Unaligned",
    "ac": 13, "hp": {"average": 45, "formula": "6d10+12"}, "speed": "30 ft.",
    "abilities": {"str": 16, "dex": 8, "con": 14, "int": 2, "wis": 11, "cha": 5},
    "senses": "blindsight 30 ft., passive Perception 10", "languages": "-", "cr": "1",
    "bio": "A skittish Sextonback calf, Deacon's shadow. Not a threat unless somebody hits it, and then it brings Deacon. Ability scores other than Strength are estimates.",
    "traits": SEXT_TRAITS + [{"name": "Eager Eater", "desc": "Eats corpses one size category faster than an adult."}],
    "actions": [atk("Slam", "Melee", "+5", "5 ft.", "1d12+3", "bludgeoning",
                    "Hit: 9 (1d12 + 3) bludgeoning damage. If hit, it Dashes away in a panic instead of fighting a second round.")],
}
npcs["gale-organ"] = {
    "name": "Gale Organ", "size": "Large", "type": "object", "alignment": "Unaligned",
    "ac": 15, "hp": {"average": 45, "formula": "object"}, "speed": "0 ft.",
    "abilities": {"str": 10, "dex": 1, "con": 10, "int": 1, "wis": 1, "cha": 1},
    "damage_immunities": "poison, psychic", "cr": "2",
    "bio": ("Hush Concord siege rig, crewed by Flue or a skirmisher. Gains 1 Pressure at the end of each round; at "
            "Pressure 3 it discharges. While Pressure is 2+, sound within 30 ft is dampened. Track Pressure by hand."),
    "actions": [{"name": "Discharge (Pressure 3)", "desc": (
        "60-foot line, 10 feet wide. DC 13 Dexterity saving throw: 3d8 force damage (half on a success); a failed "
        "save is also pushed 15 feet and knocked prone. Pressure resets to 0. If destroyed at Pressure 2+, it vents "
        "in a 10-foot burst (DC 13 Dex, 2d8 force).")}],
}

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for key, data in npcs.items():
        (OUT / f"{key}.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print("wrote", key)
