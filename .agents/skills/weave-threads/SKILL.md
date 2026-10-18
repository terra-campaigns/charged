---
name: weave-threads
description: Analyse all published campaign content and reference lore to surface up to 3 actionable tie-ins for future sessions. Use when the GM wants narrative threads, forgotten connections, or lore hooks to weave into upcoming play. No file path argument needed — this skill reads the entire repo.
argument-hint: none (reads the full repo)
---

# Weave Threads

Read the full campaign corpus and reference PDFs to find latent connections, forgotten threads, and lore opportunities. Produce up to 3 actionable suggestions for future sessions.

## Before starting: confirm with the user

When invoked, briefly confirm:

> I'll read all campaign content and reference PDFs. This will take a moment. Proceed?

Then begin.

## Files to read

### Repo content (use the Tier 1 catalogue)

- `.agents/AGENTS.md` — setting rules, tone, canon hierarchy.
- `.agents/context/catalog.json` — inspect all entities, parents, types, and connection graphs (`links_in` / `links_out`).
- `.agents/context/decisions.md` — active Tier 2 rulings.
- Use targeted reads on specific notes in `campaigns/` and `directory/` as needed to inspect specific details.

### Reference digests (Tier 3 canon — influence, not automatic canon)

Read from: `/Users/efsa/Library/CloudStorage/GoogleDrive-estevao.alvarenga@gmail.com/My Drive/RPG/campaigns/charged/_digests/`
(Consult `.agents/context/references.json` to find relevant files and sections).

Priority:
1. `uvg_2e_core.md` — primary setting, locations, factions, creatures, caravan rules.
2. `2400_xot.md` & `2400_exiles.md` — system layer, salvage, mechanics.
3. `sdm_eternal_return_key.md` — mechanical flavour, death, fantascience.
4. `the_alluring_trophy_gold.md` & `metamorphica_revised.md` — coastal incursions, mutations.

Read the digest summaries to understand the broader lore landscape (locations the caravan hasn't reached yet, factions not yet encountered, creatures and phenomena that could surface). Only inspect raw PDFs if exact table text or art is needed.

## What to produce

### 1. Thread suggestions (up to 3)

Each suggestion should be:

- **Actionable** — something the GM can introduce in the next 1–3 sessions.
- **Grounded** — rooted in content that already exists in the repo or in the reference digests.
- **Connective** — it ties together two or more things that are currently unlinked or underused. Preference order:
  1. Connections between recent sessions and older published material (best: an element from ep_001–003 that could resurface now).
  2. Connections between published content and reference lore (e.g. an upcoming UVG location or faction that connects with the caravan's trajectory).
  3. NPCs or locations that exist in the directory but have empty `links_in` (no session appearances).
  4. Active PC situations and open contracts/debts.

For each suggestion, provide:
- **Title** — a short, evocative name for the thread.
- **The connection** — what two (or more) existing elements it ties together, with file links.
- **The hook** — how the GM could introduce it at the table. One or two sentences, in-voice.
- **Source** — whether this draws from repo content, reference digests, or both.

### 2. Discovered tie-ins (optional)

If you find connections that already exist in the fiction but are not reflected in the file structure (e.g. a character mentioned in a session log who has no backlink from their directory entry, or two locations that are clearly related but not cross-linked), list them and **add the missing relative links directly to the files**.

Format link additions the same way existing links are formatted in the repo (relative paths with `.md` extensions). Only add links where the connection is clearly established in the text — do not invent connections.

## Procedure

1. Read `.agents/AGENTS.md`.
2. Inspect `.agents/context/catalog.json` and `.agents/context/decisions.md`.
3. Check recent session logs (`campaigns/UVG24XX/`) using line ranges for recent developments.
4. Consult Tier 3 digests in `charged/_digests/` for locations, factions, and creatures matching the caravan's trajectory.
5. Build a mental map of:
   - Active PCs, unresolved situations, and debt contracts.
   - Locations visited vs. locations in the directory with no session appearances.
   - NPCs with empty `links_in` in `catalog.json`.
   - Lore from the digests that resonates with published content.
6. Identify the strongest thread candidates. Rank by:
   - How naturally it could emerge from the current situation (recent sessions).
   - How far back it reaches (old threads resurfacing = high value).
   - How much it enriches existing lore rather than adding new complexity.
7. Write the output as an artifact (markdown file) and present it to the user.
8. If discovered tie-ins require link additions, edit the relevant files directly. The user will review line-by-line.

## Rules

- Never invent new canon. Every suggestion must be grounded in existing repo content or reference PDFs.
- Treat PDF content as Tier 3 canon — influence and possibility, not fact until the GM adopts it.
- Do not spoil content the PCs haven't encountered yet by writing it into session logs. Suggestions go into the artifact, not into campaign files.
- Suggestions should feel like they were always there, waiting to be noticed — not bolted on.
- Keep the artifact concise: 3 suggestions max, each no longer than a short paragraph.
- When adding links to files, follow existing formatting conventions exactly.
