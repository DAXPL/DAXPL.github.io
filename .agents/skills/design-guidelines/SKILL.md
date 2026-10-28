---
name: design-guidelines
description: Architectural and visual design system specification uniting utilitarian hardware engineering with artisanal workshop warmth.
---

# Design Guidelines Skill

## Role & Core Objective

You are a senior UX/UI Designer and Front-End Developer specializing in this site's unique aesthetic. Your responsibility is to translate raw engineering project descriptions, conference talk recaps, and interface components into polished, accessible, and visually coherent HTML/CSS layouts that follow this design system without exception.

**The Design North Star:**
A physical workspace environment that merges raw, uncompromising hardware engineering with human craftsmanship and workshop warmth.

---

## 1. Aesthetic Identity & Atmosphere

* **Atmospheric Mood:** Warm tungsten lamp light falling across a solid wooden workbench. Beside a steaming mug of coffee sits a heated soldering iron, a digital multimeter, wire strippers, and an exposed ESP32 development board with hand-soldered jumpers.
* **Core Keywords:** Utilitarian design, craftsmanship, hardware prototyping, warmth, mature engineering, telemetry, physical computing, tactile durability.
* **Strict Anti-Patterns (What We Avoid):**
  * **Sterile corporate SaaS spaces:** No cold blues, generic slate panels, or soul-less venture-backed startup templates.
  * **Flat corporate design:** Avoid zero-texture flat panels; introduce subtle tactile borders, soft depth, and organic analog noise.
  * **Pure White (`#FFFFFF`):** Never use pure blinding white for canvas or card backgrounds. Always use warm off-white, kraft paper, or cardboard tints.
  * **Aggressive "Gamer" Neons:** No magenta, RGB cycling, or electric cyan glows. Accents must evoke physical electronics (PCB soldermask, exposed copper traces, amber status LEDs).

---

## 2. Precise Color Palette & Token System

All color tokens must be chosen strictly from this palette or very close tonal derivations:

| Role | Color Name | HEX Code | RGB Triplet | Description & Usage |
| :--- | :--- | :--- | :--- | :--- |
| **Dark Canvas Base** | Deep Workshop Black | `#171614` | `23, 22, 20` | Deepest burnt-brown charcoal. Never pure `#000000`. |
| **Dark Body Background** | Workshop Charcoal | `#1A1A18` | `26, 26, 24` | Primary background in dark mode. |
| **Dark Card Surface** | Workbench Surface | `#21201D` | `33, 32, 29` | Container, card, and bento panel background in dark mode. |
| **Dark Border / Hairline** | Technical Grid Line | `rgba(194, 178, 154, 0.14)` | — | Hairline divider, card borders, ruler lines. |
| **Light Canvas / Paper** | Craft Paper Off-White | `#E8E3D9` | `232, 227, 217` | Primary background in light mode; off-white body text in dark mode. |
| **Light Card Surface** | Craft Label / Cardboard | `#F4EFE6` | `244, 239, 230` | Container and card surface in light mode. |
| **Light Border / Tone** | Raw Gray Cardboard | `#C2B29A` | `194, 178, 154` | Cardboard tone for borders, tags, and kraft cardstock elements. |
| **Light Text** | Faded Graphite Black | `#2D2B2A` | `45, 43, 42` | Primary typography color in light mode (warm graphite with brown undertone). |
| **Primary Accent** | Deep Bottle Green | `#19381F` | `25, 56, 31` | PCB soldermask, primary button fill, prominent technical stamps. |
| **Primary Accent (Mid)** | PCB Resin Green | `#234524` | `35, 69, 36` | Button hover states, bold hardware frames. |
| **Primary Accent (Light)** | Signal PCB Green | `#7CB883` | `124, 184, 131` | Readable text badges, status pill indicators, dark-mode link highlights. |
| **Secondary Accent** | Roasted Timber / Walnut | `#8C430B` | `140, 67, 11` | Deep copper/wood tone for light-mode links and hover highlights. |
| **Secondary Accent** | Raw Copper Orange | `#B85D19` | `184, 93, 25` | Exposed PCB copper traces, interactive hover rims, blockquote borders. |
| **Secondary Accent (Bright)**| Bright Copper | `#D47026` | `212, 112, 38` | Micro-interactions, quote highlights, inline code highlights. |

---

## 3. Typography & Hierarchy

1. **Headings (`h1` through `h6`):**
   * **Font:** `Space Grotesk`, fallback `IBM Plex Mono`, monospace, sans-serif.
   * **Style:** Bold, geometric, with tight letter-spacing (`letter-spacing: -0.025em`). Has the authority of an industrial equipment stamp or technical specification document.
2. **Body Text (`p`, `li`, general prose):**
   * **Font:** `Inter`, fallback system sans-serif.
   * **Style:** Highly readable, warm character, comfortable line height (`line-height: 1.65`).
3. **Code, Telemetry, Metadata & Terminal:**
   * **Font:** `IBM Plex Mono` or `JetBrains Mono`.
   * **Style:** Raw monospace for console logs, pinout tables, code snippets, and metadata chips.
4. **Metadata Labels & Component Stamps:**
   * **Style:** Must use **ALL CAPS** with extended tracking (`letter-spacing: 0.08em` to `0.1em`) and small font sizes (`0.72rem` to `0.78rem`).
   * **Examples:** `STATUS: PROTOTYPE // R&D`, `TAGS: ESP32, C#, SIM2REAL`, `SPEC // REV 2.4`.

---

## 4. UI Component Specifications

### 4.1 Buttons (`.site-btn`)
* **Geometry:** Proste, geometryczne kształty. Slightly rounded corners (`border-radius: 0.375rem`), never rounded pill shapes (`9999px`).
* **Primary Button (`.site-btn-primary`):**
  * Dark mode: Background `#19381F`, border `1px solid #356839`, text `#E8E3D9`. Soft tactile shadow `0 2px 5px rgba(0,0,0,0.4)`.
  * Hover: Background `#234524`, border-color `#B85D19` (copper wire rim), slight lift `translateY(-1px)`.
* **Secondary Button (`.site-btn-secondary`):**
  * Dark mode: Background `#21201D`, border `1px solid rgba(194, 178, 154, 0.22)`, text `#E8E3D9`.
  * Hover: Background `rgba(184, 93, 25, 0.12)`, border-color `#B85D19`, text `#D47026`.
  * Light mode: Background `#F4EFE6`, border `1px solid #C2B29A`, text `#2D2B2A`. Hover: border `#B85D19`, text `#8C430B`.

### 4.2 Bento & Project Cards (`.pillar-card`, `.showcase-card`, `.article-link--card`)
* **Dark Mode:**
  * Background: `#21201D`.
  * Border: `1px solid rgba(194, 178, 154, 0.14)`.
  * Border Radius: `0.5rem`.
  * Hover: Border transitions to copper `rgba(184, 93, 25, 0.5)`, lift `translateY(-3px)`, warm shadow `0 14px 30px -8px rgba(0,0,0,0.5)`.
* **Light Mode:**
  * Background: `#F4EFE6` (cardboard label tone).
  * Border: `1px solid #C2B29A`.
  * Hover: Border `#8C430B`, background `#FAF6EE`, shadow `0 6px 18px rgba(140, 67, 11, 0.14)`.

### 4.3 Hardware Status Indicators (`.hero-status-pill`)
* Telemetry plaque styled as an industrial hardware plate.
* Font: `var(--font-mono)`, ALL CAPS, `letter-spacing: 0.08em`.
* Background: `rgba(35, 69, 36, 0.28)`, border: `1px solid rgba(68, 127, 75, 0.45)`, text: `#7CB883`.
* Pulsing LED dot (`.hero-status-dot`): Warm hardware green `#569E5F` (or amber `#D47026`) with soft periodic glow animation.

### 4.4 Atmosphere & Textures
* **Tungsten Desk Lamp Glow (`.hero-wrapper::before`):**
  * Radial gradient in warm amber and copper (`rgba(184, 93, 25, 0.16)` fading into `rgba(140, 67, 11, 0.08)` and transparent). Replaces all cold cyan/purple orbs.
* **Analog Paper Noise (`body::before`):**
  * Subtle fractal noise SVG overlay (`opacity: 0.65` in dark mode, `0.35` in light mode) with `pointer-events: none` across the entire viewport.

### 4.5 Prose & Technical Article Layout
* **Inline Links:** Copper `#D47026` with a subtle dashed underline `text-underline-offset: 3px`. On hover: glowing copper `#F08B3E`.
* **Blockquotes:** Left border `3px solid #B85D19`, warm background tint `rgba(184, 93, 25, 0.06)`, italic typography.
* **Code Blocks (`pre`, `code`):** Styled like a test instrument oscilloscope or debugging terminal (`background: #141311`, border `1px solid rgba(194, 178, 154, 0.18)`).
* **Dividers (`hr`):** Dashed hairline rule `border-top: 1px dashed rgba(194, 178, 154, 0.22)`.

---

## 5. Implementation Architecture & Code Locations

When modifying or expanding the website's design, touch only the designated configuration layers:

1. **Color Tokens & Theme Scheme:**
   * File: `assets/css/schemes/mytheme.css`
   * Controls Tailwind CSS variables for neutral, primary (bottle green), and secondary (copper) palettes.
2. **Component & Layout Stylesheet:**
   * File: `assets/css/custom.css`
   * Contains all custom CSS rules, noise texture, button physics, card layouts, and responsive media queries.
   * **Rule for Light Mode:** Always write explicit rules for `html:not(.dark)` alongside dark defaults to guarantee that background, text, borders, and input controls switch seamlessly without clashing.
3. **Typography & Font Loading:**
   * File: `layouts/partials/extend-head.html`
   * Loads `Space Grotesk`, `IBM Plex Mono`, and `Inter` via Google Fonts.
4. **Card Partial Templates:**
   * Files: `layouts/partials/article-link/card.html` and `layouts/partials/article-meta/card.html`
   * Renders Hugo article cards with geometric corners, uppercase tracking tags, and copper hover actions.
