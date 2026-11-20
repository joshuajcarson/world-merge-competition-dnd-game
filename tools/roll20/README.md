# Roll20 prep

Generated files for loading the Act Two content into Roll20. The statblocks in
`world/` and `encounters/` stay the source of truth; these are mechanical copies.

| Folder | What | Build |
|---|---|---|
| `maps/` | Battlemaps resized to 1540x1050 px = **22x15 squares** at Roll20's 70 px grid | `python tools/roll20/build_maps.py` |
| `tokens/` | Transparent 512x512 token PNGs (GrabCut cutouts; check by eye) | `python tools/roll20/build_tokens.py` |
| `npcs/` | Statblock JSON for the 5e NPC importer | `python tools/roll20/build_npcs.py` |

Token sizes on the grid: skirmisher, Obby, Flue 1x1 (Small); Verger 2x2 (Large);
Deacon and the Sextonback 3x3 (Huge). Maps are 5 ft per square.

## Loading it

1. **Maps.** Upload each `maps/*.png` to your Art Library or a page, set the page to
   22 x 15 units at 70 px per square, and drag the image to fit.
2. **Tokens.** Upload `tokens/*.png`, then save each as a character's default token
   at the sizes above.
3. **Statblocks.** The `npcs/*.json` files are for
   [ByteBard97/roll20-5e-npc-json-importer](https://github.com/ByteBard97/roll20-5e-npc-json-importer)
   (MIT; reviewed 2026-10-07, commit 6ac926d: no network calls, no `eval`). Install it
   under Game Settings > Mod Scripts (Pro). Put a creature's JSON in a handout's GM Notes
   and run `!5enpcimport handout|<HANDOUT NAME>`.

## Known problem: the sheet

The importer targets the classic **"D&D 5e by Roll20"** sheet and its author says the 2024
sheet is untested. The World Merge Competition game uses the newer
**"D&D Fifth Edition (5E & 5.5E)"** sheet, so the importer is **not verified to work
there** and has not been run. Options: run it in a separate test game on the classic sheet
and transfer, paste statblocks into token GM Notes by hand, or enter them in the new sheet.

A script can only set a token's image to one already in a Roll20 library, so image uploads
stay manual either way.

## Building a mob by hand in the new sheet (what worked, 2026-10-22)

Session 9's mobs (Aether Hornback, Hornback Bull, Swan Cultist, Vainhusk) were built in the
journal by hand, with tokens from `tokens/`.

1. In the journal, open an existing finished mob (the Alpha), click the pencil beside its name,
   and press **Duplicate**. This keeps the sheet layout.
2. Open the copy's edit dialog. Hover the avatar and the default token and press **Remove** on
   each (confirm the token deletion), then upload the new avatar (`assets/images/...`) and token
   (`tools/roll20/tokens/...`). Removing the image re-creates the drop zone.
3. Rename it, then **Edit Token Properties**: Bar 2 attribute `ac`, Bar 3 attribute `hp`,
   both bars visible and editable to players, nameplate on. Removing the token resets these.
4. On the sheet press **Edit** and fill in the stat block (type, size, CR, XP, AC, HP, speed,
   abilities, traits, actions). Duplicates carry the Alpha's WIS save proficiency, so untick it.
5. **For any action written as a saving throw** (anything in the markdown phrased "DC X
   [Ability] save," not a to-hit roll — e.g. Vainhusk's Peak), set that entry's **type** to
   **Spell Save**, then fill in the saving throw ability and the DC fields to match the text.
   Corrected on Vainhusk's sheet 2026-11-05: it was entered as a different type and the DC/save
   had to be set by hand afterward to line up with the description. **Spell Save** is what makes
   Roll20 auto-roll the save and generate correct chat text for that action — any other type
   leaves it as inert text the table has to adjudicate manually.
6. Drag the finished mobs into the journal folder.

## The Underspill (level 5 Underdark escape)

Source: `encounters/the-underspill.md`. Nothing here has been run in Roll20.

**Pages.** Nodes A and B are theater of the mind, so they are *backdrops*, not gridded
maps: `build_maps.py` resizes them to 1540 px wide keeping their 16:9 shape (1540x880, no
stretch). Make one page, 22 x 13 units at 70 px, turn the grid off, and drag the image in
as the background. Nodes E, I and J are real battlemaps (1540x1050 = 22x15 squares, same as
every other map): one page each, grid on.

| Node | Page | Image (after `build_maps.py`) | Creatures |
|---|---|---|---|
| A The Blue Sump | backdrop, no grid | `maps/the-underspill__node-a.png` | none (the Drums are a hazard) |
| B The Rising Water | backdrop, no grid | `maps/the-underspill__node-b.png` | none |
| E Gemlit Crossroads | 22x15 grid | `maps/the-underspill__node-e.png` | 5 Gemified Thralls; Bar-Bar Brute pair at Drums 4+ |
| I The Gem Works | 22x15 grid | `maps/the-underspill__node-i.png` | 2-3 Gem Works Duergar + a Hammerer, or 2 Brutes; Big Bar-Bar at Drums 7+ |
| J Bar-Bar's Reach | 22x15 grid | `maps/the-underspill__node-j.png` | Big Bar-Bar; +2 Brutes at Drums 8 |

Nodes C, D, F, G and H have no map; run them as theater of the mind.

**Maps pending.** `node-e.png`, `node-i.png` and `node-j.png` are not in
`assets/images/encounters/the-underspill/` yet (still being chosen). Once they land, run
`python tools/roll20/build_maps.py` and the three gridded maps appear in `maps/`.

**Statblocks** (`npcs/`, built by `build_npcs.py`; same sheet caveats as above):

| File | Token size | Hand entry in Roll20 |
|---|---|---|
| `gemified-thrall.json` | Medium, 1x1 | Fist does bludgeoning + piercing: check the second damage die imported. Shatterburst is a Dex save: set Spell Save by hand. |
| `gem-works-duergar.json` | Medium, 1x1 (Large 2x2 while enlarged, if you resize) | Standard MM Duergar. The Hammerer / Stone Guard officers are not transcribed: pull them from the compendium or a book. Enlarge and Invisibility are text only. |
| `bar-bar-brute.json` | Medium, 1x1 | Glaive reach is 15 ft.: the sheet won't show it. Won't Stay Down (1/Day) is manual. |
| `big-bar-bar.json` | **Large, 2x2** | Reach 20 ft. Set Sweep (DC 15 Dex) to Spell Save. Won't Stay Down (2/Day), Legendary Resistance (1/Day), BAR! BAR! and Can't Outrun Me are manual. Track the Hunt Clock by hand. |

The Gem Works Duergar JSON also uses `damage_resistances` / `dmg2` keys that I did not check
against the importer's schema; if it rejects them, enter those by hand.

**Tokens pending.** None of these four have a token yet (images are still being chosen):
Gemified Thrall, Gem Works Duergar, Bar-Bar Brute, Big Bar-Bar. Nothing in `tokens/` for them.

## Uploading with Claude in Chrome (worked 2026-11-19)

The built-in Claude desktop browser pane fails Roll20's Cloudflare check (endless 403 loop);
**Claude in Chrome** (real Chrome, already signed in) does not. Launch the game from
`app.roll20.net/campaigns/search`. Scripted, no drag and drop:

- **Pages drawer:** the small briefcase button at the top of the canvas (left of the zoom bar) opens it.
  Create Page > **Upload Background** opens "Upload your own map" (page name, folder, image).
  It builds a page straight from the image: no Art Library drag, no manual fit.
- **File inputs:** Roll20 only adds the dialog's `input[type=file]` to the DOM once the dialog is
  open, and `find` can't tell the several inputs apart. Tag the right one first with JS, then
  find it by that label and call `file_upload` on it (10 MB per call):
  `[...document.querySelectorAll('input[type=file]')].find(x=>x.accept.includes('uvtt')).setAttribute('aria-label','BGUPLOAD')`
  (`uvtt` accept = page background; `image/*, video/*` only = Art Library > Upload; `audio` = jukebox).
  Don't guess refs: a wrong one uploads to the wrong place (Node A went into the Art Library twice).
- **Unticking** "Take me to the map layer" avoids the layer tour; the GM view still jumps to the new page,
  the players' page (ribbon) does not move.
- **Blank page:** Create Page > Create Blank Page is instant; double-click the card title to rename inline.
- **Character:** Journal > **+ Character** creates one at once (random name) and opens its edit dialog;
  `form_input` sets the name, scroll the dialog, click the **GM Notes** editor (TinyMCE) and `type` into it,
  **Save Changes** (opens the sheet window; close it). Verify with
  `Campaign.characters.models` (`_blobcache.gmnotes`, URL-encoded).
- Batch calls where possible; refs change on every dialog open, so re-`find` the name box each time.

### State after the 2026-11-19 session (nothing played yet)

Pages created (top level, not in a folder): `The Underspill - Node A: The Blue Sump`, `... Node B: The Rising Water`
(backdrops from `maps/`, grid still on: turn it off in Page Settings and set 22 x 13 units), and blank
`Node E / Node I / Node J ... (MAP PENDING)` (upload with Upload Background once `node-e/i/j.png` exist, or
set the page background in Page Settings). Characters `Gemified Thrall`, `Gem Works Duergar`, `Bar-Bar Brute` and `Big Bar-Bar, War-Chief` are in the
journal folder "Session 11 - Underspill" with **full NPC stat blocks** (abilities, AC, HP, speed, saves, skills,
senses, languages, resistances, traits, actions, attacks with damage, reach), filled 2026-11-19 by script and checked
by reopening each sheet. GM Notes still carry the earlier plain-text statblock. No avatars/tokens.
Art Library has `the-underspill_node-a/b.webp` (plus one duplicate each: delete the extras).
Done by hand by the user afterwards: Sweep set to Attack Save (Dex DC 15) and the Thrall's second damage die (1d4
piercing) added. Still open: Shatterburst (Thrall, a 0-HP trait, plain text), the Duergar Hammerer / Stone Guard officers, Big Bar-Bar's passive tracking of Hunt Clock, tokens (Bar 2 `ac`, Bar 3 `hp`).

### Filling the new sheet by script (worked 2026-11-19; much faster than the form)

The D&D 5E & 5.5E sheet keeps everything in one `store` attribute (a graph of "integrants": Attack, Damage, Action,
Features, Proficiency, Ability Score ...). `sheet_fill.js` (this folder) has three console helpers:
`__clone` (copy a finished NPC and swap the core numbers), `__f` (traits, actions, attacks+damage, languages,
resistances, darkvision) and `__p` (save/skill proficiency, melee reach). Steps:

1. Open the target sheet once (loads its attributes), click **NPC** on the setup screen for the first creature
   only, close it. (`Campaign.characters.models[...].attribs` is empty until a sheet is opened.)
2. Close the sheet, paste `sheet_fill.js` with `javascript_tool`, run `__clone` / `__f` / `__p`.
3. Reopen the sheet and confirm it renders (the `store` write shows up live; no reload needed).

Form facts if you must click: fields are plain inputs, the first click after a window opens is swallowed (click
twice), **never press Tab** (focus lands on an Add button and typed spaces create empty rows), the Attack row has
To Hit = flat bonus, On Hit = dice, damage type; save/skill proficiency is the circle under PROF (dropdown:
Untrained/Half/Proficient/Expertise). Stat-block display gets proficiency bonus from CR.

Lessons from the user's hand edits: **any saving-throw action should be an Attack with Attack Type "Attack Save"**
(`attack.type 'Attack Save'`, `save:{saveAbility,saveFlat:DC}`, `autoHit:false`; it was in the Action/Attack and Attack
Type dropdowns I'd already opened, so do it up front, `sheet_fill.js` now supports `save:{ability,dc}`). A **second damage
type** on one attack is a second `Damage` child under the Attack; the form only shows the extra-damage control after
Sheet Settings > layout is set to "Standard" (it was "Stat Block"); `__f` already takes `dmg:[{...},{...}]`.

### Underspill maps E, I, J (added 2026-11-20)

`build_maps.py` now builds all five Underspill images: E and I are gridded (22x15 at 70 px), A, B and J are
no-grid backdrops (J is 1540x803). Pages were made with Upload Background into "Session 11 - Underspill":
`Node E: Gemlit Crossroads`, `Node I: The Gem Works`, `Node J: Bar-Bar's Reach`. Grid is off on A, B, J (set
with `Campaign.pages.models.find(...).save({showgrid:false})`). The E/I grid size is arbitrary: align it by eye
in Page Settings. The old blank `(MAP PENDING)` pages are now redundant; delete them.
The aria-label tag must be re-applied for each dialog (`.pop()` the newest `uvtt` input), and the Create Page
menu refs (`ref_120`, `ref_2896`) stayed stable within a session.

### Avatars and tokens by script (worked 2026-11-20)

`build_tokens.py` now includes the four Underspill creatures. GrabCut kept the floor/shadow on the Thrall,
Duergar and Big Bar-Bar, so those three are round bust tokens (`CIRCLE`); the Brute is a clean full-body cutout.
Per character: journal > name > click the avatar (pencil) to open Edit. In the dialog tag the file inputs
(`input[type=file]` inside the dialog, label them `UPLOAD0/1`), `file_upload` the avatar to the first one and wait
~6 s (the dialog re-renders), re-tag, then upload the token to the single remaining input. Save Changes.
Bars, nameplate and size can be written straight into the default-token blob, much faster than the Token Settings
dialog (`c.save()` does NOT persist it; `c.updateBlobs()` does, and it survives a reload):
`t=JSON.parse(c._blobcache.defaulttoken); Object.assign(t,{width:70*n,height:70*n,showname:true,bar2_link:'ac',
bar3_link:'hp',bar2_value:AC,bar3_value:HP,bar3_max:HP,showplayers_bar2:true,showplayers_bar3:true,
playersedit_bar2:true,playersedit_bar3:true}); c.updateBlobs({defaulttoken:JSON.stringify(t)})`.
The new sheet exposes `ac`/`hp` only to the token dialog, not `c.attribs`, so pass the numbers in yourself.
Set: Thrall, Duergar, Brute 70x70 (1x1); Big Bar-Bar 140x140 (2x2). Not verified: how the tokens look when dragged
onto a page (bar values for a freshly dropped token), and the Big Bar-Bar bust has a 2x2 footprint.
