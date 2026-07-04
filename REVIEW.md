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
