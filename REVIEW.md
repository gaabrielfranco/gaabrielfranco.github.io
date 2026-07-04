# REVIEW Log

Site overhaul (July 2026), branch `site-overhaul`. Log of all changes, grouped by phase.

## Phase A — Template sync to al-folio v0.16.3

- Added `upstream` git remote (https://github.com/alshedivat/al-folio.git); fetched tag `v0.16.3`.
- Replaced stock template files wholesale from `v0.16.3`: `_includes/`, `_sass/`, `_plugins/`, `_layouts/` (custom `cv2.liquid` untouched), `_scripts/` JS (custom `generate_qk_geometric_intuition.py` + `render_qk_tex_labels.sh` untouched), `assets/js`, `assets/css`, `bin/`, `.github/`, `Gemfile`, `package.json`, `package-lock.json`, `purgecss.config.js`, `requirements.txt`, `docker-compose.yml`, `.prettierignore`, `.pre-commit-config.yaml`, and template docs (README/FAQ/CUSTOMIZE/INSTALL/CONTRIBUTING/LICENSE).
- Deleted files removed upstream: `_includes/social.liquid`, `_plugins/cache-bust.rb`, `_plugins/download-3rd-party.rb` (replaced by `jekyll-socials`, `jekyll-cache-bust`, `jekyll-3rd-party-libraries` gems).
- `_config.yml` reconciled with v0.16.3 stock changes: added `external_services` block; giscus `theme` → `dark_theme`/`light_theme`; added `teachings` collection; added the three new plugin gems to `plugins:`; removed duplicate `jekyll-scholar` plugin entry (kept `jekyll/scholar`); added `dimensions`/`eprint`/`hal`/`pmid` to `filtered_bibtex_keywords`; imagemagick webp now `-auto-orient -quality 85`.
- Deleted `assets/jupyter/blog.ipynb` (al-folio demo notebook; also broke local builds without nbconvert).
- Verified: production build succeeds; publications no longer show a spurious "July" on every entry (upstream jekyll-scholar month-persistence fix); distill post `/blog/2026/bias-and-rope-in-attention/` output structurally identical to live site (d-cite/plotly/d-article counts match); socials render via jekyll-socials; CV page unchanged.
