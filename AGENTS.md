# AGENTS.md

Instructions for any coding agent (Claude Code, Codex, others) working in this repository. `CLAUDE.md` is a symlink to this file; edit `AGENTS.md` only.

## What this repo is

`ssul` is an agent skill that writes, polishes, and audits Korean social posts so they read like a real person telling a true story. It is distributed as a Claude Code plugin and as a plain skill folder.

```text
skills/ssul/SKILL.md            the skill (entry point)
skills/ssul/references/*.md     loaded on demand by SKILL.md
.claude-plugin/plugin.json      plugin manifest (holds the version)
.claude-plugin/marketplace.json marketplace manifest (holds the version)
README.md / README.ko.md        English and Korean docs; keep them in sync
assets/banner.png               README hero image
CHANGELOG.md                    one entry per release
ATTRIBUTIONS.md                 credits to source projects
```

## Rules for every change

1. **Commit and push after every change.** One logical change per commit. Push to `main` right after committing. Do not leave work uncommitted at the end of a task.
2. **Release only for distribution changes.** A change is a distribution change when it alters what users install or how the skill behaves: anything under `skills/`, `.claude-plugin/`, or install instructions that change the install command. For these:
   - bump the version by one step (patch for fixes and rule tweaks, minor for new modes or references, major for breaking renames), in both `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`
   - add a `CHANGELOG.md` entry
   - commit, push, then tag and release:
     ```bash
     git tag -a vX.Y.Z -m "vX.Y.Z"
     git push origin vX.Y.Z
     gh release create vX.Y.Z --title "vX.Y.Z" --notes-file <notes>
     ```
3. **Docs-only changes do not release.** README edits, `AGENTS.md`, `ATTRIBUTIONS.md`, images, and typo fixes are committed and pushed with no version bump, tag, or release.
4. **Keep READMEs in sync.** Any change to `README.md` gets the same change in `README.ko.md`, and the reverse.
5. **Validate before committing** a distribution change: `claude plugin validate .` must pass.

## Writing rules for the skill itself

- Do not copy text from other projects. Credit ideas in `ATTRIBUTIONS.md`. `crazyrookie777/gueoche-guard` has no license; never copy from it.
- Examples must be real or clearly marked as placeholders. Never add invented biography as an example of a good post.
- No company names, internal project names, or private information in examples.
- Korean examples are written in Korean, not translated from English.
- `SKILL.md` stays under 200 lines; move detail into `references/`.

## Commit messages

Imperative, short subject. Example: `Add reversal shape to formats`.
