# CODEX Memory

## Project Rules

1. Record edits in `REVIEW.md`.
2. Be extra careful with math in this project.
3. Keep language simple and as close as possible to the reference paper wording.
4. This is a personal webpage: never add uncertain claims. Ask clarification questions when needed.
5. Never add references directly. You can suggest references, but they must be user-reviewed first.

## Execution Policy

- Prefer minimal, precise edits.
- Install the locked formatter with `npm ci` and run `npx prettier . --check` before handing off edits.
- Preserve existing style and structure unless a change is required.
- If any claim is not clearly supported by the paper or local files, stop and ask.
- Keep formulas and thresholds exactly aligned with the paper.

## Current Blog State (2026-02)

- Active post draft: `_posts/2026-02-16-bias-and-rope-in-attention.md`.
- This post uses `bibliography: pinpointing-attention.bib` and Distill citations (`<d-cite ...>`).

- Section 2 currently cites:
  - `NEURIPS2024_6216515a`
  - `merullo2024talkingheadsunderstandinginterlayer`
  - `franco2024sparseattentiondecompositionapplied`

- Figures for bias/RoPE intuition are embedded as local iframes:
  - `assets/plotly/bias-geometric-pipeline.html`
  - `assets/plotly/rope-geometric-pipeline.html`

- These figure HTML files are fully offline (no CDN/runtime math dependency).
- Math labels are pre-rendered SVG assets in:
  - `assets/img/posts/qk-bias-rope/tex/`

- Regenerate all figure math labels with:
  - `bash _scripts/render_qk_tex_labels.sh`
- Script location:
  - `_scripts/render_qk_tex_labels.sh`

- Current notation choice in RoPE toy figure is aligned with text:
  - `R_3`, `R_2` (no `(theta)` in labels).
- Equality label in figures uses `=` (not `\\equiv`).

- Current figure layout convention (both interactive figures):
  - 2x4 grid
  - Col 1: shared input (row span 2)
  - Cols 2-3: top row path A, bottom row path B
  - Col 4: equality comparison (row span 2)
