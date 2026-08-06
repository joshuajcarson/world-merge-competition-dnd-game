# Navigation & Reachability

The rule: **every note must be reachable from `README.md` by following links.** Directly or indirectly — depth doesn't matter, existence does.

## The index tree

```
README.md                      <- root
├── world/README.md            <- world index
│   ├── session-zero-primer.md
│   ├── npcs/      (listed in world/README.md)
│   ├── places/    (listed in world/README.md)
│   ├── factions/  (listed in world/README.md)
│   ├── lore/      (listed in world/README.md)
│   └── races/     (listed in world/README.md)
├── sessions/README.md         <- session index
│   └── NN-slug.md
└── items/README.md            <- item index
    └── slug.md
```

## Two ways to be reachable

1. **Directly** — listed in the index for its type. Every session note and every world note gets a line in the relevant index. This is the default and should be true of nearly everything.
2. **Indirectly** — linked from a note that is itself reachable. A minor NPC stub linked from session 4's recap is reachable, because `README.md → sessions/README.md → 04-slug.md → the NPC`.

Indirect reachability is legitimate, but prefer direct for anything the user will want to look up on purpose. Stubs generated in bulk from one session are the main case where indirect-only is fine.

## The check

After writing files, for each one:

1. Start at `README.md`.
2. Follow links until you reach the file, or exhaust the tree.
3. If you cannot reach it, fix it — add it to its index, or link it from a reachable parent — then re-trace.
4. Report the path you traced.

Do this by actually reading the index files, not by assuming they were updated.

## Index entry format

One line per entry, newest or alphabetical depending on the index:

```markdown
- [Display Name](path/to/file.md) — one-clause hook.
```

Mark stubs so the user can see their to-do list at a glance:

```markdown
- [Display Name](path/to/file.md) — one-clause hook. *(stub)*
```

Session index entries lead with the number and date:

```markdown
- **04** · 2026-08-15 — [The Quartermaster's Price](04-the-quartermasters-price.md)
```

## Broken links

Never write a link to a file that does not exist. If a note references something with no file, create the stub first, then link. A broken link is a navigability failure identical to an unreachable file.

## Transitional note

These `README.md` indexes are hand-maintained by this skill and render as navigation in the GitHub repo browser. When the GitHub Pages layer is built, index pages will be generated from collection frontmatter instead, and this skill should stop maintaining them by hand. Until then, maintaining them is required — an index that lags behind the files is worse than no index, because it looks complete.
