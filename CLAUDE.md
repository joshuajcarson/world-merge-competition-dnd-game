# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Git workflow

- Never commit directly to `main`. All work — including work done by a skill
  (`campaign-chronicle`, `encounter-weaver`, `magic-item-forge`, etc.) — goes on
  a single shared branch named `claude-code`.
- Before starting a new round of changes, make sure `claude-code` is current:
  if the last PR from it has already merged into `main`, reset the branch
  from the latest `main` instead of stacking new work on old merged history
  (`git fetch origin main && git checkout -B claude-code origin/main`). If it
  hasn't merged yet, keep committing onto it as-is.
- Commit changes onto `claude-code` and push.
- Open a pull request from `claude-code` into `main`, then merge it.
- Do not delete `claude-code` after merging — it's reused for the next round
  of changes. The flow repeats: request comes in, changes land on
  `claude-code`, PR merges into `main`, branch resets for next time.
