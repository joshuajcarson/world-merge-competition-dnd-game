# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Git workflow

- Never commit directly to `main`. Every change — including work done by a skill
  (`campaign-chronicle`, `encounter-weaver`, `magic-item-forge`, etc.) — goes on
  its own new branch, created off the latest `main`.
- Name the branch after the content being added or changed, not after the
  session or a generic label. Examples: `agent-npc`, `mall-rats-encounter`,
  `bellcross-drug-faction`.
- Open a pull request from that branch into `main`, then merge it.
- Delete the branch (remote and local) once its PR has merged. A branch with
  no unmerged commits ahead of `main` shouldn't stick around.
