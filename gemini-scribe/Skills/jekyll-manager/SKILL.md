---
name: jekyll-manager
description: Manage the Jekyll build process and regenerate data links for the campaign repository. Use this to update the site data and run the local server.
---

# Jekyll Manager Skill

This skill contains automation scripts for regenerating site data and serving the Jekyll website.

## Scripts

All scripts are located in `gemini-scribe/Skills/jekyll-manager/scripts/`.

- `extract_links.py`: Regenerates `_data/markdown_links.json`.
- `extract_images.py`: Regenerates `_data/gallery_links.json`.
- `extract_lastmod.py`: Regenerates `_data/lastmod.json`.
- `emulate_repo.py`: A wrapper that runs all the extraction scripts and then serves the Jekyll site using `bundle exec jekyll serve`.

## Instructions

- When asked to update the site data, run the `extract_*.py` scripts from the repository root using python3.
- When asked to preview or emulate the repo, run `python3 gemini-scribe/Skills/jekyll-manager/scripts/emulate_repo.py --directory .` from the repository root.
