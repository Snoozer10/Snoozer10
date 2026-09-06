# DOX framework

- DOX is highly performant AGENTS.md hierarchy installed here
- Agent must follow DOX instructions across any edits

## Core Contract

- AGENTS.md files are binding work contracts for their subtrees
- Work products, source materials, instructions, records, assets, and durable docs must stay understandable from the nearest applicable AGENTS.md plus every parent AGENTS.md above it

## RESPONSES

- Keep responses concise and to the point - unless the user asks otherwise

## PLANNING MODE

- Always ask clarifying questions
- Never assume design, tech stack or features
- Use deep-dive sub-agents to assist with research
- Use deep-dive sub-agents to review the different aspects of your plan before presenting to the user

## CHANGE / EDIT MODE

- Never implement features yourself when possible - use sub-agents!
- Identify changes from the plan that can be implemented in parallel, and use sub-agents to implement the features efficiently
- When using sub-agents to implement features, act as a coordinator only
- Use the best model for the task - premium models for complex tasks (like coding) and mid-tier models for simpler tasks, like documentation
- After completing features (large or small), always run commands like lint, type check and next build to check code quality

## Read Before Editing

1. Read the root AGENTS.md
2. Identify every file or folder you expect to touch
3. Walk from the repository root to each target path
4. Read every AGENTS.md found along each route
5. If a parent AGENTS.md lists a child AGENTS.md whose scope contains the path, read that child and continue from there
6. Use the nearest AGENTS.md as the local contract and parent docs for repo-wide rules
7. If docs conflict, the closer doc controls local work details, but no child doc may weaken DOX

Do not rely on memory. Re-read the applicable DOX chain in the current session before editing.

## Update After Editing

Every meaningful change requires a DOX pass before the task is done.

Update the closest owning AGENTS.md when a change affects:

- purpose, scope, ownership, or responsibilities
- durable structure, contracts, workflows, or operating rules
- required inputs, outputs, permissions, constraints, side effects, or artifacts
- user preferences about behavior, communication, process, organization, or quality
- AGENTS.md creation, deletion, move, rename, or index contents

Update parent docs when parent-level structure, ownership, workflow, or child index changes. Update child docs when parent changes alter local rules. Remove stale or contradictory text immediately. Small edits that do not change behavior or contracts may leave docs unchanged, but the DOX pass still must happen.

## Hierarchy

- Root AGENTS.md is the DOX rail: project-wide instructions, global preferences, durable workflow rules, and the top-level Child DOX Index
- Child AGENTS.md files own domain-specific instructions and their own Child DOX Index
- Each parent explains what its direct children cover and what stays owned by the parent
- The closer a doc is to the work, the more specific and practical it must be

## Child Doc Shape

- Create a child AGENTS.md when a folder becomes a durable boundary with its own purpose, rules, responsibilities, workflow, materials, or quality standards
- Work Guidance must reflect the current standards of the project or user instructions; if there are no specific standards or instructions yet, leave it empty
- Verification must reflect an existing check; if no verification framework exists yet, leave it empty and update it when one exists

Default section order:

- Purpose
- Ownership
- Local Contracts
- Work Guidance
- Verification
- Child DOX Index

## Style

- Keep docs concise, current, and operational
- Document stable contracts, not diary entries
- Put broad rules in parent docs and concrete details in child docs
- Prefer direct bullets with explicit names
- Do not duplicate rules across many files unless each scope needs a local version
- Delete stale notes instead of explaining history
- Trim obvious statements, repeated rules, misplaced detail, and warnings for risks that no longer exist

## Closeout

1. Re-check changed paths against the DOX chain
2. Update nearest owning docs and any affected parents or children
3. Refresh every affected Child DOX Index
4. Remove stale or contradictory text
5. Run existing verification when relevant
6. Report any docs intentionally left unchanged and why

## User Preferences

When the user requests a durable behavior change, record it here or in the relevant child AGENTS.md

## Repository Facts

- This repo IS the shipped product: `README.md` renders at github.com/Snoozer10; no package.json, no build system, no test framework — Python check scripts under `verify/` are the entire QA surface
- `DESIGN.md` is the normative design contract ("Executive Cobalt Arcade", Stitch-spec tokens): every visual edit to README or workflows must stay on-token; inferred hexes stay labeled
- Stat SVGs are generated artifacts on output branches (`activity-graph-output`, `pacman-output`, `wakatime-output`) refreshed by `.github/workflows/` every 12 hours — never hand-edit them or commit generated SVGs to main
- `docs/superpowers/specs|plans/` = dated SDD archive (`YYYY-MM-DD-*.md`); `.docs/profile_readme/` = audit reports; `.superpowers/sdd/` = local tooling state

## Commands & Verification

Run all seven checks from repo root after ANY README / DESIGN.md / verify change (stdlib-only Python 3, zero deps):

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

Expected: each prints `<name> OK`. Design-token lint (expect 0 errors, 0 warnings):

```
npx -y -p "@google/design.md" designmd lint DESIGN.md
```

Windows quirk: use the dot-free `designmd` alias — invoking bin name `design.md` directly collides with Markdown file association and silently misresolves.

## Conventions & Gotchas

- One `verify/<section>_check.py` per durable README section, asserting stable anchors (headings, badge URLs, key metrics); update asserts in the same change as approved copy edits — never delete a check silently
- Conventional commits: `feat(profile):`, `fix(profile):`, `docs(spec|plan):`
- Work rides feature branches (`feat/*`)
- Windows host, PowerShell shell; quote `"@google/design.md"` in npm invocations
- No `.gitignore` exists yet — keep junk (`__pycache__/`, scratch files) out of staging

## Child DOX Index

- `verify/AGENTS.md` — standalone QA checks asserting durable README content contracts.
- Root-owned: `README.md` (GitHub profile page), `DESIGN.md` (Executive Cobalt Arcade design contract), `.github/workflows/` (automation SVG pipelines), `docs/superpowers/` (plans/specs archive), `.docs/profile_readme/` (audit reports), `.superpowers/sdd/` (tooling state).
