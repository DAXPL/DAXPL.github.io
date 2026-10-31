# AGENTS.md

This file provides comprehensive guidance and operational rules for AI coding agents (Claude Code, Cursor, Copilot, Antigravity, etc.) working on this repository.

---

## 1. Project Overview & Brand Identity

* **Brand Name:** **Input Garage**
* **Site URL:** [https://daxpl.github.io/](https://daxpl.github.io/)
* **Operator & Author:** **Miłosz Klim** (based in Poznań, Poland)
* **Core Disciplines:** Hardware Prototyping & Diagnostics, Spatial Computing & XR (Unity/OpenXR), and Applied Edge AI (Sim2Real, local LLMs).
* **Aesthetic Philosophy:** Utilitarian hardware engineering meets artisanal workshop warmth (warm tungsten light, cardboard, PCB bottle green, copper orange traces, monospace telemetry stamps).

---

## 2. Architecture & Technology Stack

* **Static Site Generator:** [Hugo](https://gohugo.io/) (Extended edition, v0.160+).
* **Theme:** [Blowfish](https://blowfish.page/) integrated as a Git submodule in `themes/blowfish/`.
* **Locales:** Fully bilingual site:
  * Polish (`pl`): Content files named `*.pl.md`, served under `/pl/`.
  * English (`en`): Content files named `*.md`, served at root `/`.
* **Typography:**
  * Headings: `Space Grotesk` (industrial, geometric).
  * Body: `Inter` (readable, warm).
  * Code & Telemetry: `IBM Plex Mono` (terminal, hardware spec stamps).
  * Loaded via `layouts/partials/extend-head.html`.
* **Styling System:**
  * Pure CSS overrides in `assets/css/custom.css`.
  * Custom color scheme tokens in `assets/css/schemes/mytheme.css`.
* **Static Assets:** Static root files located in `static/` (favicons, manifests).

---

## 3. Directory Layout & Key Files

```text
DAXPL.github.io/
├── .agents/
│   └── skills/                  # Repository custom skills for AI agents
│       ├── design-guidelines/   # Visual design manual (colors, typography, UI components)
│       ├── writing-guidelines/  # Editorial guide (13 golden rules, storytelling, tag taxonomy)
│       └── release-website/     # 5-phase procedure for audit, parity, build & release
├── assets/
│   └── css/
│       ├── custom.css           # Utilitarian styling (radial glow, borders, buttons, kbd)
│       └── schemes/mytheme.css  # Exact HEX/RGB palette tokens
├── config/
│   └── _default/
│       ├── hugo.toml            # Hugo core config, minification settings (keepComments = true)
│       ├── params.toml          # Blowfish params (appearance, code copy, social links, author)
│       ├── menus.en.toml        # English main and footer menus
│       ├── menus.pl.toml        # Polish main and footer menus
│       ├── languages.en.toml    # English metadata and site descriptions
│       └── languages.pl.toml    # Polish metadata and site descriptions
├── content/
│   ├── _index.md / *.pl.md      # Homepage content & profile summary
│   ├── about/                   # About Me page (background, stack, contact)
│   ├── now/                     # Live workbench log (/now page inspired by Derek Sivers)
│   ├── uses/                    # Workshop inventory (/uses page inspired by uses.tech)
│   ├── posts/                   # Technical articles, conference talks, and event recaps
│   ├── projects/                # In-depth engineering case studies (e.g. WST, Minerwa, LabVR)
│   ├── img/ & img-compressed/   # Media assets
│   └── compressor.py            # Utility script for converting images to optimized .webp
├── layouts/                     # Custom template overrides (precedence over themes/blowfish/)
│   ├── _default/
│   │   └── baseof.html          # Root HTML layout with ASCII banner in view-source
│   ├── partials/
│   │   ├── extend-head.html     # Google Fonts preconnect & stylesheet links
│   │   ├── favicons.html        # Custom SVG & PNG favicon metadata
│   │   ├── header/basic.html    # Header partial with "🏠 home" link and navigation
│   │   └── article-link/ & ...  # Utilitarian card geometries
│   └── robots.txt               # Crawler instructions with ASCII art header
├── static/                      # Direct static root files (favicons, webmanifest)
├── themes/
│   └── blowfish/                # Upstream submodule (DO NOT EDIT DIRECTLY)
├── AGENTS.md                    # This instruction file
└── README.md                    # Repository documentation
```

---

## 4. Non-Negotiable Operational Rules for Agents

### Rule 1: Strictly Maintain Bilingual Parity
Every public page must exist in both languages:
* Polish: `[name].pl.md`
* English: `[name].md`
When creating or editing content in one language, you **must immediately synchronize** the other language version. All frontmatter keys (`date`, `summary`, `tags`, `categories`) and media shortcodes must match.

### Rule 2: Enforce Tag Discipline (The 3–4 Tag Rule)
Never pollute articles with arbitrary micro-tags, one-off names, or exhaustive tool lists. Every post and project must have **strictly 3 to 4 tags** selected from the canonical taxonomy (`writing-guidelines` Rule 13):
* **Engines & Gamedev:** `Unity`, `Gamedev`
* **Immersive Tech:** `VR`, `XR`
* **Hardware & Prototyping:** `Hardware`, `ESP32`, `Druk 3D` (PL) / `3D Printing` (EN)
* **AI & Robotics:** `AI`, `Sim2Real`, `Robotyka` (PL) / `Robotics` (EN)
* **Sensing & Vision:** `Biometria` (PL) / `Biometrics` (EN), `Computer Vision`, `Fotogrametria` (PL) / `Photogrammetry` (EN)
* **Events & Community:** `Wystąpienia` (PL) / `Public Speaking` (EN), `Wydarzenia` (PL) / `Events` (EN), `Edukacja` (PL) / `Education` (EN), `Open-Source`, `Security`

### Rule 3: Obey the Design Guidelines Palette
Never introduce generic SaaS styles or neon gamer aesthetics. Adhere to `design-guidelines`:
* **No pure `#000000` or `#FFFFFF`:** Canvas backgrounds must use Deep Workshop Black (`#171614`), Workshop Charcoal (`#1A1A18`), or Kraft Off-White (`#E8E3D9`).
* **Accent Colors:** Primary is Deep Bottle Green (`#19381F` / `#234524`), secondary is Raw Copper Orange (`#B85D19` / `#D47026`).
* **Cards & Badges:** Dark surfaces use `#21201D` with subtle brushed borders; light surfaces use `#F4EFE6`.
* **Metadata Stamps:** Must be uppercase monospace (`IBM Plex Mono`) with extended tracking (`letter-spacing: 0.08em`).

### Rule 4: Never Edit Upstream Theme Files
Never modify files inside `themes/blowfish/`. It is a Git submodule. Always apply customizations by creating corresponding overrides in `layouts/` or adding styles in `assets/css/custom.css`.

### Rule 5: Safe Character Encoding (UTF-8 Without BOM)
All files must be saved in **UTF-8 without BOM**.
* **Caution on Windows:** Built-in PowerShell 5.1 `Set-Content` or redirection defaults to ANSI or UTF-8 with BOM, which corrupts Polish diacritics (`ą`, `ę`, `ł`, `ó`, etc.). Use dedicated tool calls (`edit_file`, `write_file`) or Python with `encoding='utf-8'` for scripted file updates.

### Rule 6: Mandatory Build Verification
Before reporting completion of any task that modifies templates, styles, configuration, or markdown content, always run:
```powershell
hugo --gc --minify
```
The command must exit with code `0` and produce zero template errors, unresolved references, or broken links.

---

## 5. Skills Reference

When executing specialized tasks, consult and execute the procedures defined in the dedicated skills under `.agents/skills/`:
1. **`release-website`** (`.agents/skills/release-website/SKILL.md`): Full procedure for audit, parity check, media validation, production build, and commit staging.
2. **`design-guidelines`** (`.agents/skills/design-guidelines/SKILL.md`): Exhaustive visual system specification (colors, typography, UI components, interactive states, responsive behavior).
3. **`writing-guidelines`** (`.agents/skills/writing-guidelines/SKILL.md`): Golden editorial rules for authentic, captivating engineering articles, inquiry protocols, and canonical tag rules.
