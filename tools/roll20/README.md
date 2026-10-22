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
5. Drag the finished mobs into the journal folder.
