# verify/ — README QA Checks

## Purpose

- Standalone Python checks guarding durable content contracts in the root `README.md` (GitHub profile page) and `DESIGN.md` (design system tokens/sections)
- Each check asserts one document section survives edits without drift

## Ownership

- Owns: every file under `verify/`
- Does NOT own: `README.md` or `DESIGN.md` themselves (root-owned); asserts track approved root changes, never dictate them

## Local Contracts

- Stdlib-only Python 3; no dependencies, no test framework
- Run from repo root: `python verify/<check>.py`
- Each script reads its target file (`README.md`, `DESIGN.md`) relative to CWD, prints `<section> OK` on pass, non-zero exit on assertion failure
- One check per guarded README section; filename matches `<section>_check.py`

## Work Guidance

- Add a new `<section>_check.py` whenever the README gains a durable section worth guarding
- Assert on stable anchors: headings, badge URLs, key metrics — not volatile phrasing
- When an approved README change breaks asserts, update asserts in the same change; never delete a check silently
- Keep each check minimal: asserts plus one print line; no config files

## Verification

Run all seven from repo root after any README, DESIGN.md, or verify/ edit:

```
python verify/masthead_check.py
python verify/summary_check.py
python verify/taxonomy_check.py
python verify/pinned_check.py
python verify/impact_check.py
python verify/design_check.py
python verify/workflow_check.py
python verify/final_check.py
```

All seven must print OK; any traceback fails the change. DESIGN.md additionally lints clean via:

```
npx -y -p "@google/design.md" designmd lint DESIGN.md
```

## Child DOX Index

- None.
