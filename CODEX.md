# CODEX Memory

<!-- CHANGED: Added project workflow guardrails from user instructions. -->

## Project Rules

<!-- CHANGED -->

1. For everything that is changed, tag it with a `CHANGED` comment.

<!-- CHANGED -->

2. Every modification must also be recorded in `REVIEW.md` so you can review each change.

<!-- CHANGED -->

3. Be extra careful with math in this project.

<!-- CHANGED -->

4. Keep language simple and as close as possible to the reference paper wording.

<!-- CHANGED -->

5. This is a personal webpage: never add uncertain claims. Ask clarification questions when needed.

<!-- CHANGED -->

6. Never add references directly. You can suggest references, but they must be user-reviewed first.

<!-- CHANGED: Added practical execution policy to enforce the rules above. -->

## Execution Policy

<!-- CHANGED -->

- Prefer minimal, precise edits.
- Preserve existing style and structure unless a change is required.
- If any claim is not clearly supported by the paper or local files, stop and ask.
- Keep formulas and thresholds exactly aligned with the paper.

<!-- CHANGED: Added durable notes from latest blog-post workflow. -->

## Current Blog State (2026-02)

<!-- CHANGED -->

- Active post draft: `_posts/2026-02-16-bias-and-rope-in-attention.md`.
- This post uses `bibliography: pinpointing-attention.bib` and Distill citations (`<d-cite ...>`).

<!-- CHANGED -->

- Section 2 currently cites:
  - `NEURIPS2024_6216515a`
  - `merullo2024talkingheadsunderstandinginterlayer`
  - `franco2024sparseattentiondecompositionapplied`

<!-- CHANGED -->

- Figures for bias/RoPE intuition are embedded as local iframes:
  - `assets/plotly/bias-geometric-pipeline.html`
  - `assets/plotly/rope-geometric-pipeline.html`

<!-- CHANGED -->

- These figure HTML files are fully offline (no CDN/runtime math dependency).
- Math labels are pre-rendered SVG assets in:
  - `assets/img/posts/qk-bias-rope/tex/`

<!-- CHANGED -->

- Regenerate all figure math labels with:
  - `bash _scripts/render_qk_tex_labels.sh`
- Script location:
  - `_scripts/render_qk_tex_labels.sh`

<!-- CHANGED -->

- Current notation choice in RoPE toy figure is aligned with text:
  - `R_3`, `R_2` (no `(theta)` in labels).
- Equality label in figures uses `=` (not `\\equiv`).

<!-- CHANGED -->

- Current figure layout convention (both interactive figures):
  - 2x4 grid
  - Col 1: shared input (row span 2)
  - Cols 2-3: top row path A, bottom row path B
  - Col 4: equality comparison (row span 2)
