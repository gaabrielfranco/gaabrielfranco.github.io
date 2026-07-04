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

## Phase E — Projects, Repositories, Bookshelf

- **Projects**: un-excluded `_pages/projects.md`; changed it to a flat research portfolio (removed the demo `work`/`fun` categories, real description). Created 3 real project pages, each drafted from the papers' own wording with `related_publications: true` (auto-generated References section from `{% cite %}`) and links to the code repos:
  - `_projects/1_attention_causal_communication.md` — ACC / ACC++ circuit tracing (cites Pinpointing, Finding; links `accpp-tracer`).
  - `_projects/2_feature_geometry.md` — singular-vector/feature alignment (cites Singular Vectors, Sparse Attention; links `svf-alignment`).
  - `_projects/3_learning_from_label_proportions.md` — LLP model selection & benchmarks (cites KDD'23, Evaluating LLP).
  - Card thumbnails reuse Gabriel's own paper figures (`assets/img/posts/acc/fig3`, `fig1`). **Gabriel to review card text and swap images if desired.**
- **Repositories**: un-excluded `_pages/repositories.md`; extended `_data/repositories.yml` from 2 to 6 repos (added `accpp-tracer`, `pinpointing-attention-causal-communication`, `svf-alignment`, `llp-variants-datasets-benchmarks`). GitHub stat/trophy cards are fetched client-side on the live site.
- **Bookshelf**: still excluded (`_pages/books.md` in `exclude:`, nav hidden) until Gabriel provides a real book list — the demo "Godfather" book was already removed in Phase B.
- Nav bar is now: about, blog, publications, projects, repositories, cv, teaching & service.
- Verified: 3 project cards render (flat, no demo categories); each detail page shows a References section with its cited papers; repositories page builds with 6 repo cards + user/trophy widgets.

## Phase F — SEO, analytics, socials

- `_config.yml`: `serve_og_meta: true` and `serve_schema_org: true` (Open Graph + schema.org now emitted in `<head>`); set site-wide `og_image` to `.../assets/img/og_image.png`.
- Rewrote `description` to a real, keyword-rich sentence (used as the meta description + schema.org description).
- Analytics/verification: left `google_analytics` and `google_site_verification` empty with `TODO(Gabriel)` inline notes (paste ID/token, then flip the matching `enable_*` flag). Not enabled with empty values to avoid emitting broken tags.
- Created **`assets/img/og_image.png`** (1200×630): dark card with name, "Ph.D. Candidate, Computer Science / Boston University", research tagline, and a circular crop of the profile photo. Generated with PIL (script in scratchpad; not committed).
- `_data/socials.yml`: added `dblp_url: https://dblp.org/pid/255/9604`; un-hid `rss_icon: true` (feed is active); left `orcid_id: 0000-0003-0702-0146` commented with a `TODO(Gabriel)` to confirm ownership before enabling.
- Verified: homepage `<head>` emits og:title/url/description/image, twitter:card/image, and two JSON-LD blocks (`@type: Person`, `@type: WebSite`); DBLP + RSS icons render in the socials row; meta description is the new text.

### Still requires Gabriel (user-side)
- GA4 measurement ID (create property → paste into `google_analytics`, set `enable_google_analytics: true`).
- Search Console verification token (add property → paste into `google_site_verification`, set `enable_google_verification: true`); submit `sitemap.xml` after deploy.
- Confirm ORCID `0000-0003-0702-0146`, then uncomment in `socials.yml`.
- giscus `category_id` is still empty in `_config.yml` (blog comments won't post until set) — grab it from giscus.app.

## Phase G — Blog draft rewritten for the ACC++ paper

- Rewrote `_posts/2025-12-01-acc.md` from the old ACC (NeurIPS'25) explainer into a post about the new paper **"Finding Interpretable Prompt-Specific Circuits in Language Models"** (arXiv:2602.13483 v2), copying the paper and MechInterp-workshop poster language as literally as possible.
- Updated frontmatter: new title/description, author list (Franco, Tassis, Rohr, Crovella), date 2026-05-13. **Kept `published: false`** — the paper is under review at NeurIPS, so nothing goes live.
- Content follows the paper's narrative and wording: the question (why each head attends where it does) → from ACC to ACC++ (two conceptual advances + one technical advance, verbatim) → the 4-step method → circuits 2×–10× smaller with 50–90% fewer components → autointerpretation (63%/50%/31% interpretable, SAE-baseline comparison) → "no single circuit for IOI" (ABBA vs BABA clustering, name-mover head (9,9) receiving different signals) → multilingual (components reused, signals language-specific; URIEL+ correlations r=0.83/0.88) → limitations (verbatim from the paper).
- Figures: extracted 4 figures directly from the paper PDF (`_papers/2602.13483v2.pdf`) via pdftoppm — method diagram (Fig 1), IOI clustering (Fig 3), interpretable ABBA/BABA traces (Fig 5), multilingual clustering (Fig 6) — into `assets/img/posts/accpp/`. The old `assets/img/posts/acc/` figures remain (now reused as project-card thumbnails).
- `<d-cite>` references use only keys already present in `pinpointing-attention.bib`; the ACC prior work and the singular-vectors companion are linked in prose (no new bib entries added, per CODEX rules).
- Per the agreed change-tracking convention, this rewrite carries **no inline CHANGED comments** (previous ones removed); the record lives here.
- Verified: builds with `--unpublished` with no errors; 31 citations resolve (0 broken), all 4 figures present, mermaid pipeline diagram and MathJax render.

## Phase H — Staged MIT postdoc (invisible)

- `_news/mit_postdoc.md` with `published: false` and a `TODO(Gabriel)` note.
- Commented-out bio line in `_pages/about.md` (HTML comment).
- Verified: neither appears anywhere in the built `_site` (news, homepage, or as a leaked comment). Flip `published: true` (+ fix date) and uncomment the bio line when the position is public.

## Phase I — Final verification

- Full production build clean; `_site` contains no "Einstein"/"Godfather"/"lorem" and no `CODEX.md`/`REVIEW.md`/`requirements.txt`.
- `sitemap.xml` regenerated: real pages only (about, blog, publications, projects + 3 project pages, repositories, cv, teaching-service, news, 4 news items, 1 published blog post). No demo project/book URLs.
- `<head>` on key pages carries Open Graph, Twitter card, and schema.org JSON-LD; `og_image.png` referenced absolutely.
- Nav order: about / blog / publications / projects / repositories / cv / teaching & service.
- Delivered as PR from `site-overhaul` → `main` for Gabriel to review and merge (merge triggers the GitHub Pages deploy).

## Phase J — Follow-ups (Gabriel's inputs + fixes)

- Gabriel provided: GA4 ID `G-XCTMYC52RG`, Search Console token, uncommented ORCID, flipped `enable_google_analytics`/`enable_google_verification` to true, and dropped in an updated `assets/pdf/CV.pdf`. Verified GA4 tag + verification meta appear in the build.
- **giscus fixed**: the configured category "Comments" did not exist in the repo's Discussions (categories are Announcements/General/Ideas/Polls/Q&A/Show-and-tell). Switched to the giscus-recommended **Announcements** category with its real id `DIC_kwDOPjK62c4CuhmY` (fetched from giscus.app's public API). Values now bake into `assets/js/giscus-setup.js` at build. Comment posting also requires the **giscus GitHub App** installed on the repo (user action).
- **ICML news dates** corrected to **2026-04-30** (ICML 2026 author-notification date; conference is Jul 7–9, 2026).
- **Bookshelf → personal page**: removed `_pages/books.md` (per Gabriel, a bookshelf isn't the right fit); created `_pages/personal.md` (nav order 7, after teaching) as a scaffold for non-research interests (music, baking, gym, hobbies) with commented photo/gallery examples and `assets/img/personal/` as the image home. Content is placeholder for Gabriel to fill.
- Verified: full build clean; nav is about / blog / publications / projects / repositories / cv / teaching & service / personal.

## Phase K — News polish, CV/personal bug fixes, repositories removed

- **papers.bib**: removed the outdated `code` link from MEMSCOPE (RTSS); added `code` for the entity-tracking paper (`github.com/PootieT/entity-tracking-mi`).
- **News**: rewrote all items to be friendlier (a sentence or two on each work), highlighting the lead author when Gabriel is not first author (Zilu Tang → entity tracking, linked; Pedro Calais → ACL; Golsana Ghaemi → RTSS, bolded — no unverified homepage links). Added code links where public. Added a new **RTSS 2025** news item. Oldest news remains "started my PhD" (2021), per Gabriel.
- **CV (`_data/cv.yml`)**: fixed the `{"Advisor"=>...}` bug (YAML was parsing `- Advisor: X` and colon-containing bullets as maps → now quoted strings). Trimmed to a short, PhD-onward, research-focused CV (Education, Research & Industry Experience [BU RA + Microsoft intern], Selected Honors & Awards, Academic Service, Teaching); dropped pre-PhD industry, academic productions, skills, and languages (all still in the full PDF). Used compact date labels (e.g. "Summer 2024", "2021 – now") so the year column no longer overlaps the description.
- **Personal page**: the scaffold's example `{% include figure %}` executed inside an HTML comment (Liquid ignores HTML comments) and leaked broken markup. Rewrote without live Liquid; the photo example is now inside a `{% raw %}` code block.
- **Repositories page removed** (Gabriel's choice): the al-folio repo cards depend on `github-readme-stats.vercel.app`, which returns 503 when rate-limited (confirmed down). Since the projects page already links every repo, deleted `_pages/repositories.md` and orphaned `_data/repositories.yml`.
- Nav is now: about / blog / publications / projects / cv / teaching & service / personal.

## Phase L — Projects rework + talks in news

- **Projects reorganized** and rewritten in Gabriel's voice (no em-dashes, no marketing tone):
  - Project 1 renamed to **"Understanding why an attention head attends where it does"** and now spans the full ACC line of three papers: Sparse Attention Decomposition (the first version), Pinpointing ACC (NeurIPS 2025), and ACC++ (Finding Interpretable Prompt-Specific Circuits). Cites render distinctly (Franco & Crovella 2024, 2025; Franco et al. 2026).
  - Project 2 (**Feature Geometry in Attention Heads**) now cites only the ICML 2026 Singular Vectors paper (Sparse Attention Decomposition moved to Project 1). New thumbnail from Gabriel's SVF figures (`assets/img/projects/svf-geometry.png`, the geometric-intuition poster) instead of the ACC++ figure; added the SV/feature cosine-alignment plot in the body.
  - Project 3 (**Learning from Label Proportions**): disambiguated the two "Franco et al., 2023" citations by naming each venue in the prose ("our KDD 2023 paper" vs "a companion paper"). Note: literal "2023a/2023b" isn't emitted by jekyll-scholar (it doesn't run citeproc year-suffix disambiguation), and forcing it via the `year` field would break the publications page's year grouping — so prose disambiguation is used instead.
  - New project images live in `assets/img/projects/` (copied from Gabriel's `_papers` figures).
- **Talks added to news** (from the CV's Invited Talks section), in Gabriel's voice, grouping the talk given at two venues into one item:
  - `talk_ufv_2026.md` (UFV, 2026-04-04), `talk_attention_first_principles.md` (Brown + BU TINLab, 2026-03-12), `talk_acc_baaigl_2025.md` (BU BAAIGL Lab, 2025-09-24).
  - Each has a `TODO(Gabriel)` comment for attaching slides once available.
- Verified: build clean; all three project pages render with correct citations/figures; three talk items appear in news.
