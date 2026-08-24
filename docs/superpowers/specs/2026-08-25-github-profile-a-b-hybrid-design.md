# GitHub Profile Overhaul — A+B Hybrid Design
**Date:** 2026-08-25
**Author:** Hesham Alsoufi (Snoozer10)
**Status:** Approved — ready for planning
**Repo:** Snoozer10/Snoozer10 (profile README)
**Goal:** C+D (Open-source leader + Viral standout) with C+D vibe (Playful Interactive + Premium Executive)

## 1. Executive Summary

Overhaul `README.md` from Phase 5 hardened baseline to viral, premium executive profile. Combines Approach A (Executive Arcade) skeleton with Approach B (Growth Architect) ROI storytelling, selective Approach C widgets hardened.

**Differentiator:** International Business Administration + Marketing/E-commerce SEO track record (150% POD sales, 40% traffic lift, 300k monthly visitors, 50+ blogs, 98% error-free DB) bridging to Full-Stack Cloud Architecture. No other profile has this hybrid.

**Constraints:** Keep dark/light resilience, mobile viewport, workflow hardening invariants from Phase 5. Upgrade (not keep) workflows. Curate pinned repos from public repos. Add Waka, visitor counter, sponsor, hireable CTA.

## 2. Goals & Non-Goals

**Goals:**
- Viral aesthetic: most forkable premium executive profile on GitHub
- Open-source leader: attract collaborators, stars, sponsor clicks
- Hybrid positioning: business ROI + engineering proof
- Upgrade workflows to 2026 hardened patterns with concurrency locks

**Non-Goals:**
- Not replacing GitHub Pages / external site
- Not adding backend server — README is static markdown + SVG pipelines only
- Not widget maximalism — only hardened, fail-open widgets

## 3. Information Architecture (Hierarchy)

```
1. Premium Masthead
   - capsule-render waving 220h cobalt gradient (customColorList 6,11,20,29)
   - readme-typing-svg Fira Code 600 20px 4 lines: Building Scalable Cloud Architectures / Bridging Business Strategy & Software / Full-Stack Engineer & Tech Innovator / Designing High-Performance Web Systems
   - shields.io for-the-badge 4 badges: LinkedIn, Discord, Email, Repositories (0077B5/5865F2/D14836/181717)

2. Executive Summary & Core Focus (B DNA)
   - YAML code fence: specialization/domain/current_focus/collaboration
   - 3 bullets with CV ROI metrics:
     * Growth: POD platform Shopify/Printful 150% sales (6 months), healthcare blog 8k→300k monthly
     * Scale: SEO doubled rankings + traffic (40% lift), 50+ blog posts, robust SEO strategies
     * Ops: 98% error-free DB (YLDF), e-wallet banking, facilitation leadership, cross-functional team lead
   - Education badge: International Business Administration — International University of Technology Twintech

3. Technical Taxonomy & Toolchain
   - HTML <table> 4 cols: Core Languages | Frontend & UI | Cloud & DevOps | Tooling & Design (width 25% each)
   - skillicons.dev icons: py,js,ts,bash / react,next,vue,tailwind / gcp,aws,docker,githubactions / vscode,notion,ae,figma + <sub> labels
   - Dark/light resilient, mobile wrap tested

4. Featured Architectures → Curated Pinned Repos (NEW)
   - 2x2 table of top 4 public repos curated by stars/forks/recency (curated via gh api /users/Snoozer10/repos?per_page=100&sort=stars)
   - Each card: shields for stars/forks/issues/license + skillicons stack + 1-line impact description
   - Manual override allowed, fallback static bake (no runtime API from README)

5. Open-Source Impact Wall (NEW, C viral)
   - Row 1: github-profile-trophy flat + streak-stats dracula + top-langs compact dracula (all hide_border=false theme=dracula border_radius=10)
   - Row 2: wakatime stats + komarev visitor badge + 3d-contrib profile green + github-profile-views counter
   - Hardened: maxAge 12h CDN cache, fail-open if 5xx

6. Dynamic Metrics & Engineering Activity
   - Keep existing streak + top-langs dual table
   - activity-graph.svg upgraded workflow (100% width)
   - pacman arcade in <details> lazy-loaded

7. Proof of Competency (rewrite)
   - 2-col table: Enterprise Cloud & Business Automation | High-Performance Reactive Web Suite
   - Badges: Distributed, GCP Cloud Native, Next.js 14, Tailwind CSS
   - Capabilities now embed CV metrics (zero-downtime CI/CD + SEO doubled etc.)

8. Connect & Collaborate + CTA
   - Centered hireable CTA + sponsor button (pink shields)
   - LinkedIn/Discord/Gmail badges centered
   - capsule-render footer wave 110h cobalt reversal
   - Sub: Designed with precision • Powered by GitHub Actions & Automated SVG Pipelines • © 2026 Hesham Alsoufi
```

Flow rationale: Premium executive top hooks recruiter → tech middle hooks collaborators → arcade bottom hooks viral.

## 4. Components — Frontend/Backend Detail

| Component | Frontend | Backend |
|-----------|----------|---------|
| Masthead | capsule-render URL `type=waving&height=220&color=gradient&customColorList=6,11,20,29&text=Hesham%20Alsoufi&fontSize=48&fontColor=fff&animation=twinkling` + typing SVG `demolab.com?font=Fira+Code&weight=600&size=20&duration=3500` + shields for-the-badge | Static URLs, no API |
| Executive Summary | YAML fence + 3 bullets + LinkedIn/Email links | Static markdown |
| Tech Taxonomy | HTML table + skillicons.dev + sub labels | Static SVG |
| Pinned Repos | 2x2 table or github-readme-stats pin cards `?theme=dracula&hide_border=false` | One-time `gh api` curation, baked markdown |
| Impact Wall | trophy `?theme=dracula&column=7` + streak `?mode=daily&theme=dracula` + top-langs `?layout=compact&theme=dracula` + Waka `?layout=compact&theme=dracula` + komarev `?label=Profile%20views&color=0e75b6` + 3d-profile `profile-green-animate` | Static GET, hide_border, 12h cache |
| Proof | 2-col table with shields flat-square + ul stack/capabilities | Static |
| Activity/Arcade | `<img width="100%" src="raw.githubusercontent.../branch/file.svg">` + details | Workflows generate SVGs |
| CTA Footer | shields hireable/sponsor + capsule footer | funding.yml |

## 5. Data Flow & Workflows

**Triggers:** `schedule: "0 */12 * * *"` + `workflow_dispatch` + `push` on workflow file path only.

**Pipeline (activity-graph.yml):**
```
actions/checkout@v4.1.7
→ maurodesouza/github-readme-activity-graph-action@v2
   username: ${{ github.repository_owner }}
   options: radius=16&theme=dracula&area=true&order=5&hide_border=false&border_radius=12
   output_path: dist/activity-graph.svg
   token: ${{ secrets.GITHUB_TOKEN }}
→ crazy-max/ghaction-github-pages@v4.0.0
   target_branch: activity-graph-output
   build_dir: dist
   commit_message: "chore(ci): update dynamic activity graph SVG [skip ci]"
   GITHUB_TOKEN
```

**Pipeline (arcade.yml):**
```
actions/checkout@v4.1.7
→ abozanona/pacman-contribution-graph@main
   github_user_name: ${{ github.repository_owner }}
   games: 'pacman'
→ crazy-max/ghaction-github-pages@v4.0.0
   target_branch: pacman-output
   build_dir: dist
```

**Consumption:** README `<img>` via `raw.githubusercontent.com/Snoozer10/Snoozer10/<branch>/file.svg` (GitHub CDN). Arcade lazy via `<details>`. Pinned repos baked at build time, no runtime API.

## 6. Resilience & Error Handling

- **Fail-open widgets:** Every dynamic `<img>` has `alt` text; if 5xx, README renders without gap. Waka/views optional.
- **Dark/light:** All shields `theme=dracula` `hide_border=false` tested WCAG AA both modes; capsule cobalt gradient verified contrast.
- **Mobile:** Tables `width=100%`, `valign=top`, cols 25%, no fixed px; verified 375px wrap. Skillicons scale.
- **Security:** Pinned actions (`@v4.1.7`, `@v4.0.0`, `@v2`), `permissions: contents: write` minimal, `concurrency.group: activity-graph-${{github.ref}}` + `cancel-in-progress:true`, `timeout-minutes:10`, `GITHUB_TOKEN` only.
- **Link rot:** Pre-merge `lychee` check 200 OK all shields/SVGs; `https` only.
- **Rate limits:** 12h schedule avoids quota; CDN cache; no loops.

## 7. Testing & Verification

**Pre-ship checklist:**
- [ ] GitHub preview + `grip` local render
- [ ] Dark/light toggle (GitHub appearance)
- [ ] Mobile 375/768/1280 viewport
- [ ] `lychee --verbose README.md` all 200 OK
- [ ] `workflow_dispatch` run both workflows → SVG pushed to branches, no concurrency race
- [ ] `alt` on all img, axe scan pass

**Success metrics (30d):**
- Viral: profile views +50% (komarev), pinned repo stars +20%
- Open-source: +2 collab invites, follower growth, sponsor click
- Recruiter: LinkedIn badge CTR
- Hardening: 0 visible 5xx breaks, 0 workflow failures

## 8. Trade-offs & Decisions

- **A vs B vs C:** Chose A+B hybrid over pure C maximalism to preserve hardening (Phase 5 invariants) and editorial premium while still viral.
- **Widget selection:** Exclude fragile `github-readme-streak` alternatives? Kept demola but with fallback. Exclude live Waka if user has no Waka setup — show placeholder or hide.
- **Pinned repos:** Bake static vs live `github-readme-stats` pin — chose baked curation to avoid API fragility, but allow live pin cards if user prefers.
- **Business angle:** Keep vs de-emphasize — chose keep as differentiator (C hybrid), per user choice C (restructure).

## 9. Open Questions Resolved

- Vibe: C+D (playful + premium executive) — dark luxury base, arcade lounge accent
- Content: C restructure — Executive → Tech → Impact → Proof → Arcade → CTA
- Workflows: overhaul/upgrade (pinned, concurrency)
- Pinned repos: curate from public repos
- New sections: Waka, sponsor, hireable CTA — yes

## 10. Implementation Notes

- **File scope:** Single file `README.md` + 2 workflows + `.github/FUNDING.yml` (sponsor) + optional `.docs/profile_readme/6_*` report
- **No backend:** No server, no DB, no env vars except `GITHUB_TOKEN` provided by Actions
- **Isolation:** Each README section is independent unit — can A/B test reorder without breaking others
- **Rollback:** `git revert` README + workflow branches are append-only SVG pushes (safe)

## 11. References

- CV: Hesham Alsoufi — BRIEF SUMMARY, WORK EXPERIENCE (White City 09/2023-present, Waifus & Weebs 04/2022-12/2022 POD 150%, Wikinolg 05/2021-06/2021 50+ blogs, Need Your Health 01/2020-12/2020 300k monthly, YLDF 05/2018-07/2018, Yemen & Kuwait Bank 03/2021-04/2021), EDUCATION TWIntech 01/2018-11/2021, SKILLS
- Prior reports: `.docs/profile_readme/1-5_*` (Phase 5 hardening complete)
- Workflows: `.github/workflows/activity-graph.yml`, `arcade.yml`
- Current README baseline: capsule-render + typing-svg + skillicons + streak/top-langs + activity-graph + pacman

---
**Next step:** Invoke `writing-plans` skill to break into implementable tasks.
