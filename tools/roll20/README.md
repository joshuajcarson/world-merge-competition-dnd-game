# Roll20 prep

Files and helpers for loading encounters into the World Merge Competition Roll20 game.
The statblocks in `world/` and `encounters/` are the source of truth. Everything here
is a mechanical copy, rebuilt by the scripts below.

The game uses the **"D&D Fifth Edition (5E & 5.5E)"** character sheet.

## What's here

| Path | What | Built by |
|---|---|---|
| `maps/` | Encounter images sized for Roll20's 70 px grid. Battlemaps are 1540x1050 (22x15 squares, 5 ft each). Theater-of-the-mind backdrops are 1540 px wide at their own aspect ratio. | `build_maps.py` |
| `tokens/` | Transparent 512x512 token PNGs cut from the portraits. | `build_tokens.py` |
| `npcs/` | One statblock per creature as JSON. Use it as a reference when entering a sheet. | `build_npcs.py` |
| `sheet_fill.js` | Browser-console helpers that fill an NPC sheet by script. | written by hand |

Run the scripts from the repo root. They need Pillow (`build_maps.py`) and
`opencv-python-headless` + `numpy` (`build_tokens.py`). `build_npcs.py` uses only the
standard library.

```
python tools/roll20/build_maps.py
python tools/roll20/build_tokens.py
python tools/roll20/build_npcs.py
```

- **`build_maps.py`** resizes every `assets/images/encounters/*/*.png`. Images listed
  in its `BACKDROPS` set keep their aspect ratio. Everything else is stretched less
  than 1% to fit 22x15 squares. When you add a new backdrop, add it to `BACKDROPS`.
- **`build_tokens.py`** builds the creatures listed in `SOURCES`. It cuts each
  creature out with OpenCV GrabCut, which works on flat or gradient backgrounds. If a
  portrait has a busy background or a floor shadow, add it to `CIRCLE` to get a round
  bust token instead. Check every token by eye.
- **`build_npcs.py`** holds the statblocks as Python dicts. Edit them there when the
  markdown changes. The JSON follows the format of
  [ByteBard97/roll20-5e-npc-json-importer](https://github.com/ByteBard97/roll20-5e-npc-json-importer),
  but that importer targets the classic "D&D 5e by Roll20" sheet and **has never been
  run** against this game's sheet. Sheets have been filled by hand or with
  `sheet_fill.js`.

## Working in Roll20

Use **Claude in Chrome**. The built-in desktop browser pane fails Roll20's Cloudflare
check. Launch the game from `app.roll20.net/campaigns/search`.

### Pages

- Open the Pages drawer with the small briefcase button at the top of the canvas, left
  of the zoom bar.
- **Create Page > Upload Background** builds a page straight from an image (page name,
  folder, image). There's no Art Library drag and no manual fit.
- Battlemaps: 22 x 15 units at 70 px, grid on. The grid may not match the image
  exactly, so align it by eye in Page Settings.
- Backdrops: grid off. From the console:
  `Campaign.pages.models.find(p => p.get('name') === NAME).save({showgrid:false})`.
- Untick "Take me to the map layer" to skip the layer tour. The GM view jumps to the
  new page, but the players' ribbon stays where it is.

**Uploading files by script.** Roll20 adds the dialog's `input[type=file]` only after
the dialog opens, and there are several inputs that `find` can't tell apart. Before you
call `file_upload`, tag the right one with JS (each call allows 10 MB):

```js
[...document.querySelectorAll('input[type=file]')].filter(x => x.accept.includes('uvtt')).pop()
  .setAttribute('aria-label', 'BGUPLOAD')
```

- An `accept` containing `uvtt` is the page background input.
- `image/*, video/*` alone is Art Library > Upload.
- `audio` is the jukebox.

Re-tag for every dialog. Don't guess refs: a wrong ref uploads to the wrong place.

### Characters and statblocks

1. **Journal > + Character** creates a character with a random name and opens its edit
   dialog. Set the name with `form_input` and click **Save Changes**.
2. Fill the sheet by script with `sheet_fill.js`. It's much faster than the form. Its
   header comment covers the details:
   - Open the target sheet once so its attributes load. For the first creature,
     click **NPC** on the setup screen. Then close the sheet.
   - Paste `sheet_fill.js` with `javascript_tool`.
   - `__clone` copies a finished NPC and swaps in the new core numbers.
   - `__f` adds traits, actions, attacks with damage, languages, resistances and
     darkvision.
   - `__p` adds save and skill proficiencies and melee reach.
   - Reopen the sheet to confirm it rendered. A bad key does nothing and gives no
     error.
3. **Any action phrased as "DC X [Ability] save" is an Attack with Attack Type
   "Attack Save"**, with the save ability and DC filled in. That makes Roll20 roll the
   save and print the right chat text. Any other type leaves it as plain text.
   `sheet_fill.js` takes `save:{ability, dc}`.
4. **A second damage type on one attack** is a second Damage entry under that Attack.
   `__f` takes `dmg:[{...},{...}]`. The form shows the extra-damage control only after
   Sheet Settings > layout is set to "Standard".

If you have to use the form:

- Fields are plain inputs.
- The first click after a window opens is swallowed, so click twice.
- **Never press Tab.** Focus lands on an Add button, and typed spaces create empty rows.
- Proficiency is the circle under PROF.
- The stat-block view gets the proficiency bonus from CR.

### Avatars and tokens

1. Open the character's edit dialog. Tag the dialog's file inputs (`UPLOAD0`, `UPLOAD1`).
2. Upload the avatar (`assets/images/...`) to the first input and wait about 6 s while
   the dialog re-renders.
3. Re-tag, then upload the token (`tools/roll20/tokens/...`) to the remaining input.
   Click **Save Changes**.

Set bars, nameplate and size by writing the default-token blob. It's faster than the
Token Settings dialog. `c.save()` does **not** persist it, but `c.updateBlobs()` does:

```js
t = JSON.parse(c._blobcache.defaulttoken);
Object.assign(t, {width: 70*n, height: 70*n, showname: true,
  bar2_link: 'ac', bar3_link: 'hp', bar2_value: AC, bar3_value: HP, bar3_max: HP,
  showplayers_bar2: true, showplayers_bar3: true, playersedit_bar2: true, playersedit_bar3: true});
c.updateBlobs({defaulttoken: JSON.stringify(t)});
```

The sheet doesn't expose `ac` and `hp` through `c.attribs`, so pass the numbers in
yourself. The settings above match the existing tokens, which show players the exact
HP. For GM-only HP, set `showplayers_bar3` and `playersedit_bar3` to `false`.

Token sizes: Small and Medium 1x1 (70 px), Large 2x2, Huge 3x3.

## What's loaded

### Act Two and Sessions 8-9

Known to be built in the journal, by hand:

- The Alpha (Aether wolf).
- Session 9's mobs: Aether Hornback, Hornback Bull, Swan Cultist and Vainhusk.

To build a new mob by hand, duplicate a finished one so the sheet layout carries over:
pencil beside the name, then **Duplicate**. Untick the Alpha's WIS save proficiency on
the copy. Removing and re-uploading the token resets its bars.

`tokens/` and `npcs/` also cover the Hush Concord (Obby, Flue, skirmisher, Gale Organ),
the Sextonbacks (Deacon, Verger), Dale, Renee and Gary, and the Blood Bowl faction
leaders. Nothing records whether those were entered in Roll20. Token sizes for them:
skirmisher, Obby and Flue 1x1; Verger 2x2; Deacon and the Sextonback 3x3.

### The Underspill (Session 11)

Source: `encounters/the-underspill.md`. All of it is in the journal folder
"Session 11 - Underspill". **Nothing has been played yet.**

| Node | Page | Image | Creatures |
|---|---|---|---|
| A The Blue Sump | backdrop, no grid | `maps/the-underspill__node-a.png` | none (the Drums are a hazard) |
| B The Rising Water | backdrop, no grid | `maps/the-underspill__node-b.png` | none |
| E Gemlit Crossroads | 22x15 grid | `maps/the-underspill__node-e.png` | 5 Gemified Thralls; Bar-Bar Brute pair at Drums 4+ |
| I The Gem Works | 22x15 grid | `maps/the-underspill__node-i.png` | 2-3 Gem Works Duergar + a Hammerer, or 2 Brutes; Big Bar-Bar at Drums 7+ |
| J Bar-Bar's Reach | backdrop, no grid | `maps/the-underspill__node-j.png` | Big Bar-Bar; +2 Brutes at Drums 8 |

Nodes C, D, F, G and H have no image. Run them as theater of the mind.

Characters with full sheets, avatars and tokens:

| Character | Token | Notes |
|---|---|---|
| Gemified Thrall | 1x1, round bust | Fist has the second damage die (1d4 piercing). |
| Gem Works Duergar | 1x1, round bust | Standard MM Duergar. Enlarge and Invisibility are text only. |
| Bar-Bar Brute | 1x1, cutout | Glaive reach 15 ft. Won't Stay Down (1/Day) is manual. |
| Big Bar-Bar, War-Chief | 2x2, round bust | Reach 20 ft. Sweep is an Attack Save (Dex DC 15). Won't Stay Down (2/Day), Legendary Resistance, BAR! BAR!, Can't Outrun Me and the Hunt Clock are manual. |

Still open:

- Thrall **Shatterburst** (a Dex save when it drops to 0 HP) is plain text.
- The Duergar **Hammerer** and **Stone Guard** officers aren't built. Pull them from
  the compendium or a book.
- Delete the leftover blank `(MAP PENDING)` pages and the duplicate Node A and Node B
  images in the Art Library.
- No token has been dragged onto a page yet. Check bar values on a freshly dropped
  token and Big Bar-Bar's 2x2 footprint.
