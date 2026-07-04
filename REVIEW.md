# REVIEW Log

Site overhaul (July 2026), branch `site-overhaul`. Log of all changes, grouped by phase.

## Phase A — Template sync to al-folio v0.16.3

- Added `upstream` git remote (https://github.com/alshedivat/al-folio.git); fetched tag `v0.16.3`.
- Replaced stock template files wholesale from `v0.16.3`: `_includes/`, `_sass/`, `_plugins/`, `_layouts/` (custom `cv2.liquid` untouched), `_scripts/` JS (custom `generate_qk_geometric_intuition.py` + `render_qk_tex_labels.sh` untouched), `assets/js`, `assets/css`, `bin/`, `.github/`, `Gemfile`, `package.json`, `package-lock.json`, `purgecss.config.js`, `requirements.txt`, `docker-compose.yml`, `.prettierignore`, `.pre-commit-config.yaml`, and template docs (README/FAQ/CUSTOMIZE/INSTALL/CONTRIBUTING/LICENSE).
- Deleted files removed upstream: `_includes/social.liquid`, `_plugins/cache-bust.rb`, `_plugins/download-3rd-party.rb` (replaced by `jekyll-socials`, `jekyll-cache-bust`, `jekyll-3rd-party-libraries` gems).
- `_config.yml` reconciled with v0.16.3 stock changes: added `external_services` block; giscus `theme` → `dark_theme`/`light_theme`; added `teachings` collection; added the three new plugin gems to `plugins:`; removed duplicate `jekyll-scholar` plugin entry (kept `jekyll/scholar`); added `dimensions`/`eprint`/`hal`/`pmid` to `filtered_bibtex_keywords`; imagemagick webp now `-auto-orient -quality 85`.
- Deleted `assets/jupyter/blog.ipynb` (al-folio demo notebook; also broke local builds without nbconvert).
- Verified: production build succeeds; publications no longer show a spurious "July" on every entry (upstream jekyll-scholar month-persistence fix); distill post `/blog/2026/bias-and-rope-in-attention/` output structurally identical to live site (d-cite/plotly/d-article counts match); socials render via jekyll-socials; CV page unchanged.

## Phase B — Demo purge & config hygiene

- Deleted al-folio demo content: all 9 `_projects/*_project.md`, `_books/the_godfather.md` (+ cover in `assets/img/book_covers/`), `_pages/profiles.md`, `_pages/about_einstein.md`, `_pages/dropdown.md`, demo distill post `_posts/2025-08-23-example.md`, `assets/img/publication_preview/*.gif`, demo images `assets/img/{1..12}.jpg`, `rhino.png`, `template_error.png`, `assets/pdf/example_pdf.pdf`, `assets/json/resume.json` (Einstein demo), `assets/json/table_data.json`, `assets/plotly/demo.html`, `assets/html/relativity.html`, `_data/venues.yml`, and unreferenced 14 MB `assets/img/prof_pic_color.png`.
- `_config.yml`:
  - `exclude:` cleaned: removed stale entries for deleted pages and the `_pages/books.mc` typo; **added `CODEX.md`, `REVIEW.md`, `requirements.txt`** (these were publicly served on the live site — now excluded from the build); `_pages/books.md` temporarily excluded until a real book list is added.
  - Removed deprecated `disqus_shortname: al-folio` leftover (site uses giscus).
  - `enable_publication_thumbnails: false` (per owner decision — no per-paper thumbnails).
  - Removed `jekyll_get_json`/`jsonresume` blocks (resume.json deleted; CV will be driven by `_data/cv.yml`).
- Verified: `_site` no longer contains CODEX.md/REVIEW.md/requirements.txt or any Einstein/Godfather/lorem demo pages; sitemap has no project/book demo URLs. Remaining "Empty slug" build warnings traced to jekyll-scholar on publications.md — to be resolved with the Phase C bibliography rewrite.

## Phase C — Publications enrichment

- Added missing paper to `_bibliography/papers.bib`: **"Do Language Models Track Entities Across State Changes?"** (Tang, Zhao, Franco, Wijaya, Mueller, Schuster, Kim), **ICML 2026** (arXiv:2605.30233; confirmed "ICML main conference 2026" via arXiv comments).
- Corrected **"Singular Vectors of Attention Heads Align with Features"** from arXiv-only to **ICML 2026** (confirmed by author's own repo description "to appear in ICML 2026").
- Updated **"Finding Interpretable Prompt-Specific Circuits in Language Models"** title to match arXiv v2 (was "Finding Highly Interpretable…"); kept as arXiv preprint (under review at NeurIPS per owner).
- Fixed author lists to arXiv order (e.g. Franco, Tassis, Rohr, Crovella for 13483).
- Enriched **every** entry with al-folio fields: `abbr` (venue badge: NeurIPS/ICML/ACL Findings/KDD/RTSS/BRACIS/arXiv/Abakós), `bibtex_show={true}` (BibTeX popover), `arxiv=` (5 entries), `html=`/`doi=` (OpenReview for NeurIPS, ACL Anthology, ACM DL), `code=` GitHub links (8 entries, matched from the author's public repos), and `abstract=` (from arXiv/ACL, verbatim).
- Marked the 4 interpretability papers `selected={true}` (owner's choice): ICML'26 Entity Tracking, ICML'26 Singular Vectors, arXiv Prompt-Specific Circuits, NeurIPS'25 Pinpointing.
- `_pages/about.md`: `selected_papers: true` (homepage now shows the 4 selected papers).
- `_data/coauthors.yml`: added verified homepage links for Terzi, Kim, Mueller, Tang (co-author names now link on the publications page). Other co-authors left unlinked pending verified URLs.
- New news items: `_news/icml26_entity_tracking.md`, `_news/icml26_singular_vectors.md`. **NOTE: dates set to 2026-05-01 as an estimated ICML notification date — Gabriel to confirm/adjust.**
- Config: kept `enable_publication_thumbnails: true` because the venue badge shares that column; no `preview` fields defined, so badges render with **no** thumbnail images (exactly the requested look).
- Verified: 11 venue badges render, 0 thumbnail images; Abs/Bib/HTML/Code/arXiv buttons render per entry; homepage selected-papers section shows the 4 chosen papers; "Empty slug" warnings gone.

## Phase D — Data-driven CV page

- Switched `_pages/cv.md` from the custom `cv2` layout to the stock `cv` layout (renders `_data/cv.yml`), kept the PDF download button via `cv_pdf: /assets/pdf/CV.pdf`, and added a left sidebar table of contents (`toc.sidebar: left`).
- Deleted the custom `_layouts/cv2.liquid` (no longer used).
- Rewrote `_data/cv.yml` with Gabriel's real CV, transcribed from `assets/pdf/CV.pdf` and updated with verified 2026 facts: Education, Research & Industry Experience (BU RA, Microsoft intern, SEEK, Localiza, CAPES, CNPq/FAPEMIG), Selected Honors & Awards, Academic Service (ICLR 2026/2025, NeurIPS 2025 + MI Workshop), Teaching, Other Academic Productions (book chapter + SBRC short course), Technical Skills, Languages.
- Note: the demo `assets/json/resume.json` was already removed in Phase B, so the layout uses `_data/cv.yml` as the single source. The shipped `CV.pdf` is still the Nov 2025 export — **Gabriel to provide an updated PDF** (user-side checklist).
- Verified: CV page renders all 9 sections from real data, PDF button links to `/assets/pdf/CV.pdf`, sidebar TOC present, no Einstein/Zurich/Nobel leftovers.
