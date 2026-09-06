---
name: Executive Cobalt Arcade
description: Premium executive design system for the Snoozer10 GitHub profile - cobalt gradient waves, Dracula surfaces, matrix-green terminal accents, and arcade motion layers.
colors:
  background: "#282A36"
  surface: "#44475A"
  foreground: "#F8F8F2"
  primary: "#00FF41"
  cobalt-deep: "#1A237E"
  cobalt-mid: "#3949AB"
  linkedin-blue: "#0077B5"
  discord-blurple: "#5865F2"
  gmail-red: "#D14836"
  sponsor-pink: "#EA4AAA"
  white: "#FFFFFF"
typography:
  display-mono:
    fontFamily: Fira Code
    fontSize: 20px
    fontWeight: 600
  body:
    fontFamily: system-ui
    fontSize: 16px
    fontWeight: 400
rounded:
  sm: 10px
  md: 12px
  lg: 16px
spacing:
  sm: 8px
  md: 16px
  lg: 32px
components:
  masthead-banner:
    backgroundColor: "{colors.cobalt-deep}"
    textColor: "{colors.white}"
    height: 220px
  typing-intro:
    typography: "{typography.display-mono}"
    textColor: "{colors.primary}"
  social-badge-linkedin:
    backgroundColor: "{colors.linkedin-blue}"
  social-badge-discord:
    backgroundColor: "{colors.discord-blurple}"
  social-badge-gmail:
    backgroundColor: "{colors.gmail-red}"
  social-badge-sponsor:
    backgroundColor: "{colors.sponsor-pink}"
  stats-card-streak:
    backgroundColor: "{colors.background}"
    textColor: "{colors.foreground}"
    rounded: "{rounded.sm}"
  stats-card-langs:
    backgroundColor: "{colors.background}"
    textColor: "{colors.foreground}"
    rounded: "{rounded.sm}"
  activity-graph:
    backgroundColor: "{colors.background}"
    textColor: "{colors.foreground}"
    rounded: "{rounded.lg}"
  taxonomy-column:
    textColor: "{colors.foreground}"
    padding: "{spacing.sm}"
  pacman-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.foreground}"
    rounded: "{rounded.lg}"
  footer-wave:
    backgroundColor: "{colors.cobalt-mid}"
    textColor: "{colors.white}"
    height: 110px
---

# DESIGN.md: Snoozer10 GitHub Profile

Extracted from `README.md` and `.github/workflows/` (activity-graph.yml, arcade.yml) on 2026-08-26. Tokens are normative; prose explains intent. Inferred values are labeled.

## Overview

**Executive Cobalt Arcade** — a premium executive identity fused with retro-terminal energy. Deep cobalt gradient waves sandwich the page (masthead top, footer bottom); all data surfaces sit on the Dracula dark palette; a single matrix-green terminal voice introduces the profile. Motion is arcade-flavored (twinkling waves, typing cursor, Pacman contribution graph) but confined to decorative layers — information surfaces stay static, dense, and scannable. Single-column, center-aligned GitHub profile: hero → credentials → skills → proof → metrics → contact.

## Colors

Dark-mode-first. The Dracula family carries all informational surfaces; brand colors appear only on badge chips; cobalt lives exclusively in the decorative wave gradients.

- **Background (`#282A36`)** — Dracula base; every stat card and graph canvas.
- **Surface (`#44475A`)** — current-line elevation; collapsed panels (Pacman details).
- **Foreground (`#F8F8F2`)** — off-white ink on all dark surfaces.
- **Primary (`#00FF41`)** — matrix green; reserved for the typing intro terminal voice. Never for body text.
- **Cobalt Deep (`#1A237E`) / Cobalt Mid (`#3949AB`)** — *(both inferred approximations of capsule-render `customColorList=6,11,20,29`)*; wave gradient endpoints.
- **Brand chips** — LinkedIn Blue `#0077B5`, Discord Blurple `#5865F2`, Gmail Red `#D14836`, Sponsor Pink `#EA4AAA`; badge backgrounds only.
- **White (`#FFFFFF`)** — glyph/text color over cobalt waves.

The Dracula comment gray `#6272A4` appears inside third-party themed SVGs (streak, languages, activity graph) and is intentionally **not** a token — never introduce it for readable copy; it fails WCAG AA on Dracula surfaces.

## Typography

- **Display Mono (`Fira Code`, weight 600, 20px)** — typing intro only. Terminal personality; monospace signals engineering voice.
- **Body (`system-ui`, 16px, weight 400)** — GitHub's native stack; no webfonts are loaded for prose.
- Bold `<b>` labels inside skill captions act as pseudo-headings; keep caption text short and noun-based.

## Layout

Single centered column inside GitHub's readme container. Rhythm comes from `---` horizontal rules separating six zones (hero, summary, taxonomy, projects, metrics, contact).

- Media spans `width="100%"`; paired cards sit in a 50%/50% outer table row.
- Taxonomy table fixes four equal `width="25%"` columns (mobile-hardened).
- Vertical breathing follows the spacing scale: `sm` intra-chip, `md` chip rows, `lg` between zones.
- Collapsible `<details>` hides the Pacman arcade below the fold.

## Elevation & Depth

Flat system — no box shadows. Hierarchy is achieved by surface steps (`background` → `surface`) and the top/bottom wave sandwich framing the page in cobalt depth. Card edges come from visible borders (`hide_border=false`) at the rounded scale, not shadow.

## Shapes

Radius ladder: **sm 10px** (stat cards), **md 12px**, **lg 16px** (activity graph, arcade panel). Badges render as shields.io pills (`for-the-badge` style). Masthead and footer are organic waving curves — the only non-rectilinear shapes on the page.

## Components

| Component | Background | Text/Glyph | Radius | Notes |
| :-- | :-- | :-- | :-- | :-- |
| `masthead-banner` | `{colors.cobalt-deep}` gradient wave | `{colors.white}` | 0 | capsule-render, twinkling |
| `typing-intro` | transparent | `{colors.primary}` | — | Fira Code 600, rotating lines |
| `social-badge-*` | brand chip colors | shields.io default white | pill | LinkedIn / Discord / Gmail / Sponsor |
| `stats-card-streak` | `{colors.background}` | `{colors.foreground}` | `{rounded.sm}` | streak-stats, dracula theme |
| `stats-card-langs` | `{colors.background}` | `{colors.foreground}` | `{rounded.sm}` | top-langs, compact dracula |
| `activity-graph` | `{colors.background}` | `{colors.foreground}` | `{rounded.lg}` | theme=dracula, area=true |
| `taxonomy-column` | transparent | `{colors.foreground}` | — | skillicons grid + bold caption |
| `pacman-panel` | `{colors.surface}` | `{colors.foreground}` | `{rounded.lg}` | inside collapsible details |
| `footer-wave` | `{colors.cobalt-mid}` gradient wave | `{colors.white}` | 0 | capsule-render, cobalt theme |

All dynamic SVGs are generated by GitHub Actions into output branches (`activity-graph-output`, `pacman-output`) — never hand-edit their bytes.

## Do's and Don'ts

**Do**

- Keep every informational card on the Dracula family; one theme across all services.
- Write descriptive `alt` text for every `<img>` (accessibility contract enforced by verify checks).
- Hold the 25% taxonomy column widths for mobile stacking.
- Assert new durable copy via a `verify/<section>_check.py` script.
- Label any inferred hex (e.g., cobalt stops) as inferred in prose.

**Don't**

- Don't use `primary` green or Dracula comment gray `#6272A4` for readable body copy (WCAG AA failures on light/low-contrast grounds).
- Don't mix a light-theme card into the dark surface stack.
- Don't add shadows, glow, or blur — depth is wave-based, not elevation-based.
- Don't hardcode stat SVG URLs to other branches or commit generated SVGs to main.
- Don't exceed one accent hue per zone; cobalt owns decoration, green owns voice, brand chips own identity.

## Responsive Behavior

GitHub strips custom CSS; responsiveness relies on structure: percentage-width images fluidly rescale; the 50/50 stats table stacks vertically on narrow screens while the 25%-column taxonomy stays legible four-abreast because cell content is icon grids, not prose. The Pacman arcade stays collapsed by default so mobile users scroll past zero-cost. Test edits against GitHub mobile widths before merging.

## Agent Prompt Guide

Quick reference for agents building new profile sections:

- Canvas `#282A36`, ink `#F8F8F2`, accent `#00FF41`, waves `#1A237E`→`#3949AB` (inferred), chips `#0077B5` `#5865F2` `#D14836` `#EA4AAA`.
- Radii 10/12/16; badges are pills; no shadows ever.
- Fonts: Fira Code 600 for terminal moments only; system-ui otherwise.

Sample prompts:

- *"Add a certifications section between projects and metrics: 50/50 card table on `{colors.background}`, radius `{rounded.sm}`, dracula-themed imagery, alt text on every image."*
- *"Introduce a new tech category in the taxonomy: mirror the existing `<td width="25%">` skillicons pattern exactly, then extend `verify/taxonomy_check.py` asserts."*
- *"Retheme the intro typing lines: keep Fira Code 600, keep `{colors.primary}`, rewrite copy only — never change the color."*
