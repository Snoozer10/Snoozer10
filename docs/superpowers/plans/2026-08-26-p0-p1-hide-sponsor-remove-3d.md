# P0+P1 Hide Sponsor + Remove 3D Fix Batch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Hide sponsor badges until GitHub Sponsors enabled, remove 3D 404 image until branch exists, pin arcade workflow, add .gitignore, verify 7/7 checks and workflows green

**Architecture:** Single-file README hygiene + 1 workflow SHA-pin + .gitignore. No new runtime. 1×2 pinned stays 200 OK, 3D removed fail-open, arcade@main→SHA hardening, .gitignore stops cache leak.

**Tech Stack:** Markdown, shields.io, skillicons.dev, actions/checkout@v4.1.7, crazy-max/ghaction-github-pages@v4.0.0, abozanona/pacman-contribution-graph SHA-pinned, gh CLI 2.98.0, lychee, designmd

## Global Constraints

- Dark/Light WCAG AA, theme dracula hide_border=false border_radius=10
- Mobile 375 wrap, tables width 100% no fixed px
- Pinned actions: actions/checkout@v4.1.7, crazy-max/ghaction-github-pages@v4.0.0, maurodesouza/github-readme-activity-graph-action@v1, abozanona/pacman-contribution-graph@SHA
- Permissions contents: write minimal, concurrency group activity-graph-${{github.ref}} / arcade-animation-${{github.ref}} cancel:true timeout:10
- Schedule cron "0 */12 * * *" + workflow_dispatch + push on workflow file only
- Output branches activity-graph-output / pacman-output build_dir dist commit_message "chore(ci): update ... [skip ci]"
- Widgets fail-open every img alt, no single-point failure, https only, no placeholders

---

### Task 1: Hide Sponsor Badges + Add .gitignore

**Files:**
- Modify: `README.md:24-26` (masthead Sponsor anchor)
- Modify: `README.md:254-256` (footer Sponsor anchor)
- Create: `.gitignore`
- Test: `verify/masthead_check.py`, `verify/final_check.py`

**Interfaces:**
- Consumes: none (first)
- Produces: README without Sponsor EA4AAA badges (4 badges remain masthead, 3 footer), .gitignore tracked

**Steps:**

- [ ] **Step 1: Write failing check for sponsor hidden**

```python
# verify_sponsor_hide.py (temp)
with open("README.md", encoding="utf-8") as f:
    md = f.read()
assert "Sponsor-EA4AAA" not in md, "Sponsor badge still present masthead"
assert "github.com/sponsors/Snoozer10" not in md, "Sponsor link still present"
assert md.count("for-the-badge") >= 6, "lost too many badges"
print("sponsor hide OK")
```

- [ ] **Step 2: Run to verify baseline FAIL (sponsor present)**

Run: `python verify_sponsor_hide.py`
Expected: FAIL AssertionError Sponsor badge still present

- [ ] **Step 3: Remove sponsor badges**

In `README.md:24-26` delete:
```html
  <a href="https://github.com/sponsors/Snoozer10" target="_blank">
    <img src="https://img.shields.io/badge/Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Sponsor Badge" />
  </a>
```

In `README.md:254-256` delete footer Sponsor anchor:
```html
  <a href="https://github.com/sponsors/Snoozer10"><img src="https://img.shields.io/badge/Sponsor-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Sponsor" /></a>
```
Keep Hireable `00C853` and `© 2026 Hesham Alsoufi`.

- [ ] **Step 4: Create .gitignore**

File `.gitignore`:
```
__pycache__/
.superpowers/sdd/
verify/__pycache__/
.docs/design_preview.html
verify_url_check.py
*.log
```

- [ ] **Step 5: Verify passes**

Run: `python verify_sponsor_hide.py` Expected: sponsor hide OK
Run: `python verify/masthead_check.py` Expected: masthead OK (still 4 badges for-the-badge >=4)
Run: `python verify/final_check.py` Expected: final OK (for-the-badge >=6 still via 8 remaining)
Run: `git status` Expected: .gitignore untracked now tracked, README modified, verify files still OK

- [ ] **Step 6: Commit**

```bash
git add README.md .gitignore
git commit -m "fix(profile): hide sponsor badges until Sponsors enabled + add gitignore"
```

---

### Task 2: Pin Arcade SHA + Remove 3D Image

**Files:**
- Modify: `.github/workflows/arcade.yml:30`
- Modify: `README.md:148`
- Test: `verify/workflow_check.py`, `verify/impact_check.py`

**Interfaces:**
- Consumes: Task1 README without Sponsor
- Produces: arcade workflow SHA-pinned, README without 3D 404 image

**Steps:**

- [ ] **Step 1: Get arcade SHA**

Run: `gh api repos/abozanona/pacman-contribution-graph/commits/main --jq .sha`
Expected: 40-char SHA e.g., `7ab...` (use actual output verbatim)

- [ ] **Step 2: Write failing check for SHA pinned + 3D removed**

```python
# verify_arcade_3d.py
with open(".github/workflows/arcade.yml") as f:
    txt = f.read()
assert "abozanona/pacman-contribution-graph@main" not in txt, "still @main unpinned"
assert "abozanona/pacman-contribution-graph@" in txt, "missing pinned"
with open("README.md", encoding="utf-8") as f:
    md = f.read()
assert "3d-profile/profile-green-animate.svg" not in md, "3D still present"
assert "3d" not in md.lower() or "3d-contrib" not in md.lower() or "profile-3d" not in md.lower() or "komarev" in md, "3D check failed but komarev fallback missing"
print("arcade SHA + 3D remove OK")
```

- [ ] **Step 3: Run baseline FAIL**

Run: `python verify_arcade_3d.py` Expected: FAIL still @main unpinned + 3D still present

- [ ] **Step 4: Pin arcade**

In `.github/workflows/arcade.yml:30` replace:
```yaml
        uses: abozanona/pacman-contribution-graph@main
```
with:
```yaml
        uses: abozanona/pacman-contribution-graph@<SHA>
```
where `<SHA>` is 40-char from Step1. Example: `uses: abozanona/pacman-contribution-graph@e3f7c9a...`

- [ ] **Step 5: Remove 3D image**

In `README.md:148` delete:
```html
<!-- 3D Contribution -->
<img src="https://raw.githubusercontent.com/Snoozer10/Snoozer10/3d-profile/profile-green-animate.svg" width="100%" alt="3D Contribution Graph" onerror="this.style.display='none'" />
```
Keep surrounding `</div>` `---`.

- [ ] **Step 6: Verify passes**

Run: `python verify_arcade_3d.py` Expected: arcade SHA + 3D remove OK
Run: `python verify/impact_check.py` Expected: impact OK (passes via komarev OR, 3D no longer required but waka|komarev true)
Run: `python verify/workflow_check.py` Expected: workflows OK
Run: `cat .github/workflows/arcade.yml | grep pacman` Expected: SHA-pinned

- [ ] **Step 7: Commit**

```bash
git add .github/workflows/arcade.yml README.md
git commit -m "fix(profile): pin arcade to SHA, remove 3D graph until branch exists"
```

---

### Task 3: Verification 7/7 + Workflow Runs

**Files:**
- Test: `verify/masthead_check.py`, `verify/summary_check.py`, `verify/taxonomy_check.py`, `verify/pinned_check.py`, `verify/impact_check.py`, `verify/final_check.py`, `verify/workflow_check.py`, `DESIGN.md`
- Trigger: `gh workflow run`

**Interfaces:**
- Consumes: Task1+2 outputs
- Produces: verified main branch ready for push

**Steps:**

- [ ] **Step 1: Run all 7 verifies**

```bash
python verify/masthead_check.py && python verify/summary_check.py && python verify/taxonomy_check.py && python verify/pinned_check.py && python verify/impact_check.py && python verify/final_check.py && python verify/workflow_check.py && echo "ALL_VERIFY_OK"
```
Expected: ALL_VERIFY_OK (each prints OK)

- [ ] **Step 2: Design lint**

Run: `npx -y -p "@google/design.md" designmd lint DESIGN.md`
Expected: errors:0 warnings:0

- [ ] **Step 3: Lychee sample**

Run: `python -c "import urllib.request; [print(u, urllib.request.urlopen(u).status) for u in ['https://github.com/Snoozer10/local-youtube-automation','https://github.com/Snoozer10/Snoozer10','https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin']]"` etc. Expect 200.

- [ ] **Step 4: Trigger workflows**

Run: `gh workflow run "Update Activity Graph" --ref main && gh workflow run "Generate Arcade Animation" --ref main`
Expected: URLs `https://github.com/Snoozer10/Snoozer10/actions/runs/...` 2 runs, then `gh run list --limit 2` shows `success` after ~30s.

- [ ] **Step 5: Commit check (no prod edits, just verify)**

No commit if all pass, report only.

---

## Self-Review

- Spec A/B honored: Sponsor hidden (not deleted FUNDING.yml, keep for future enable), 3D removed until branch exists (impact_check OR fallback keeps PASS)
- No placeholders: SHA pinned is real commit, not `main` floating
- Type consistency: dracula hide_border, alt, https preserved, for-the-badge still >=6 after sponsor removal (10→8)
- Verify tracking: .gitignore stops cache leak, verify files remain minimal per verify/AGENTS.md

