# Copilot Instructions for this Repository

Purpose: Enable AI agents to rapidly and safely extend this static site generator + content repo.
Keep answers specific, concise, and map suggestions to existing patterns.

## 1. Big Picture
A lightweight Python static site generator builds markdown content in `content/` into a publishable site in `docs/` (GitHub Pages output). Build pipeline:
`config.toml` -> load_config -> load_content_items (front‑matter + markdown -> HTML via mistletoe + custom Mermaid renderer) -> load_templates (Jinja2 env for selected theme) -> render_site (writes per‑item `index.html`, homepage, RSS, sitemap, static assets, CNAME).

## 2. Key Directories
- `content/`: Authoring source. Subfolders named by plural of type: `posts/`, `pages/`. Each file: TOML front‑matter separated from body by `++++++` line (exact regex split). Filename (minus .md) becomes slug.
- `themes/<theme>/`: Jinja2 templates plus static assets. `config.toml` selects theme via `theme` key.
- `docs/`: Generated output, committed for GitHub Pages hosting. Never hand‑edit.
- `site_functions.py`: Core build engine (parsing, rendering, RSS, sitemap, static copy logic, grouping posts by year).
- `build.py` / `autobuild.py`: One‑shot build vs livereload dev server (serves from `docs/`).
- `config.toml`: Site+type configuration (types list drives dynamic behavior; each <type>.* keys define behavior).

## 3. Content Conventions
Front‑matter is TOML (NOT YAML). Required keys observed in samples: `title`, `date` (parsed as datetime), `published` boolean, optional others (tags not yet implemented). Drafts: `published = false` are skipped.
URLs: If `<type>.dateInURL = true` then `/YYYY/MM/DD/slug/`, else `/slug/`.
Sorting per type uses `<type>.sortBy` and `<type>.sortReverse`.

## 4. Rendering & Extensions
Markdown rendered with `mistletoe.markdown(content, MermaidRenderer)` allowing fenced code blocks with language `mermaid` -> wrapped `<div class="mermaid">` (front‑end lib must hydrate). Additional python-markdown extensions listed but currently commented out.
HTML stripping for RSS description done by a simple `HTMLParser` subclass (`remove_html_tags`). Summary truncated to first 128 chars at word boundary.

## 5. Generated Artifacts
Per content item: `docs/<url>/index.html`.
Global: `docs/index.html` (homepage), `docs/feed/rss.xml`, `docs/sitemap.xml`, `docs/CNAME`, copied theme/static assets under `docs/static/` plus any `content/static` tree overlay.
`posts_grouped_by_year` is injected into `content` for templates (iterator of (year, posts)).

## 6. Build / Dev Workflows
Preferred modern tool (from README):
- Install deps: `uv sync`
- Build: `uv run build.py`
- Preview: `uv run python -m http.server -d docs/`
Legacy Make targets assume a `venv/` with Python: `make build`, `make dev` (livereload on port 8000), `make run`.
Autobuild (`autobuild.py`) watches markdown + theme files; on change reruns full render then serves `docs/`.

## 7. Adding a New Content Type
1. Add the singular type name to `types` array in `config.toml` (e.g. `"note"`).
2. Define its block: `note.dateInURL`, `note.sortBy`, `note.sortReverse`.
3. Create directory `content/notes/` (plural auto-generated via `inflect` engine; ensure pluralization matches your folder name assumptions if irregular).
4. Provide `themes/<theme>/<type>.html` template.
5. Rebuild.

## 8. Theming
Template resolution: `<type>.html`, plus `index.html`. Static assets copied from `themes/<theme>/static` then overlaid by `content/static` if present. Avoid naming collisions unless intentionally overriding.

## 9. Safety / Idempotency Notes
`render_site` deletes the entire output directory before rebuilding. Do not store generated-but-manually-edited files there. Always modify sources in `content/` or theme.
Config mistakes (missing template, missing plural folder) will raise errors at runtime; no custom validation layer present.

## 10. Extending Functionality
- Tags: Not yet implemented; would require parsing tag array in front‑matter, aggregating, generating per-tag listings, and adding templates.
- Draft previews: Could add a flag in build script to include `published = false` items.
- Atom feed: Only RSS implemented; reuse feedgenerator with different class if needed.

## 11. Style / Tooling
Formatting: `black` + `isort` targets in Makefile (legacy versions pinned in `requirements.txt`; pyproject uses modern deps via `uv`). Use modern dependency management where possible; keep consistency (avoid reintroducing old `Markdown` lib unless fully switching back from `mistletoe`).

## 12. When Writing Code Changes
- Reuse existing helper patterns (e.g., copy logic with `copytree(..., dirs_exist_ok=True)` and ignore patterns).
- Maintain TOML front‑matter split logic: regex `^\+\+\+\+\+$` (exact 6 pluses) separating front‑matter from body.
- Keep year grouping contract: `posts_grouped_by_year` consumed by templates (assume iteration semantics from `itertools.groupby`).

## 13. Quick Reference
Core pipeline functions (in order):
`load_config` -> `load_content_items` -> `load_templates` -> `render_site`
Important globals: `markdown_extensions` / `markdown_extension_configs` (currently unused) for future switch back to python-markdown.

---
If anything above seems incomplete (e.g. template expectations, missing front‑matter keys, tagging roadmap) let me know which section to refine.
