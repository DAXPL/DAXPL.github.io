---
name: release-website
description: Comprehensive operational procedure for auditing, translating, synchronizing, building, and deploying the website.
---

# Release Website Skill

Use this skill whenever preparing, verifying, or executing a production release of the website. It ensures strict bilingual parity between Polish and English content, audits recent changes, optimizes static assets, and validates that Hugo builds cleanly with zero errors or broken paths.

---

## 1. Release Workflow Overview

The release process consists of five sequential phases:
```
1. Parity Audit  -->  2. Diff & Sync  -->  3. Asset Check  -->  4. Hugo Build  -->  5. Deployment Verification
```

---

## 2. Phase 1: Bilingual Content Parity Audit

The site is fully bilingual (Polish `pl` and English `en`). Every public content page must exist in both languages:

* **File Naming Convention:**
  * Polish versions: `[name].pl.md` (e.g., `content/posts/my-post.pl.md`, `content/projects/wst.pl.md`, `content/_index.pl.md`)
  * English versions: `[name].md` (e.g., `content/posts/my-post.md`, `content/projects/wst.md`, `content/_index.md`)

* **Execution Steps:**
  1. Scan all markdown files under `content/` (excluding archetypes and utility scripts).
  2. For every `*.pl.md` file, verify that an equivalent `*.md` file exists in the identical directory.
  3. For every `*.md` file (that is not named `*.pl.md`), verify that an equivalent `*.pl.md` file exists.
  4. If any file is missing, translate the entire document while strictly preserving:
     * **YAML/TOML Front Matter:** Ensure keys like `date`, `summary`, `tags`, `categories`, `draft`, `externalUrl`, and image paths match semantically.
     * **Hugo Shortcodes:** Keep shortcodes such as `{{< figure ... >}}`, `{{< button ... >}}`, `{{< gallery ... >}}`, and `{{< typeit ... >}}` intact with correct relative paths.
     * **Tone & Voice:** Follow the guidelines defined in the `writing-guidelines` skill.

---

## 3. Phase 2: Incremental Diff & Synchronization

Often, content updates, paragraph edits, or technical fixes are made in one language (typically Polish) without being propagated to the other.

* **Execution Steps:**
  1. Run `git status` and `git diff` to identify files modified in recent commits or currently unstaged.
  2. If a Polish document (`*.pl.md`) was modified:
     * Inspect the exact paragraph or section changes.
     * Apply corresponding updates to the English document (`*.md`).
  3. If an English document (`*.md`) was modified:
     * Check if the Polish document requires equivalent adjustments.
  4. Verify that technical specifications, pin numbers, software versions, and code snippets remain 100% synchronized across both language versions.

---

## 4. Phase 3: Static Asset & Media Integrity Check

1. **Images and Diagrams:**
   * Confirm that all paths referenced in markdown (e.g. `/img-compressed/...` or `/img/...`) exist under `static/` or `content/`.
   * Check for oversized, unoptimized images. Note: `content/compressor.py` is available in the repository to convert heavy images to compressed `.webp` format.
2. **Downloadable Files & PDFs:**
   * Verify that the downloadable CV files exist in `static/`:
     * Polish CV: `/Miłosz Klim - CV.pdf`
     * English CV: `/Miłosz Klim - CV EN.pdf`
   * Confirm that all homepage and about-page download buttons point to the correct filenames.
3. **Menus & Navigation Parity:**
   * Verify both menu configuration files:
     * Polish menu: `config/_default/menus.pl.toml`
     * English menu: `config/_default/menus.en.toml`
   * Ensure weights, links, and structure match between both locales.

---

## 5. Phase 4: Production Hugo Build & Validation

Run the production build using the Hugo CLI:

```powershell
hugo --minify --gc
```

* **Validation Checklist:**
  * **Exit Code:** The process must exit with code `0`.
  * **Warning Inspection:** Check the terminal output for:
    * Missing translations or i18n warnings.
    * Unresolved page refs or broken internal links (`relref`).
    * Invalid front-matter syntax or missing shortcode templates.
  * **Output Directory:** Verify that the `public/` directory contains generated artifacts for both locales (`public/` for English, `public/pl/` for Polish).

---

## 6. Phase 5: Git Commit & Release Summary

Once the build is verified:
1. Review all staged changes with `git status`.
2. Ensure no scratch files, debug logs, or unintended lockfiles are committed.
3. Formulate a concise, conventional commit message, for example:
   * `feat(content): sync en translations for oceta-2026 talk`
   * `fix(styles): improve light mode contrast on project cards`
   * `release: site update vX.Y`
4. Provide the user with a bulleted summary of files updated, translations synchronized, and confirmation of clean Hugo build status.
