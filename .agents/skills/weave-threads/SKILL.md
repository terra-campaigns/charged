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

### Repo content (read all of these)

- `.agents/AGENTS.md` — setting rules, tone, canon hierarchy.
- All markdown files in `campaigns/` — session logs and arc indices.
- All markdown files in `directory/` — NPCs, locations, factions, creatures, objects.
- All markdown files in `systems/` and `misc/` if they exist.
- Pay special attention to YAML front matter fields: `hooks`, `role`, `status`, `type`, `region`.

### Reference PDFs (Tier 3 canon — influence, not automatic canon)

Read from: `/Users/efsa/Library/CloudStorage/GoogleDrive-estevao.alvarenga@gmail.com/My Drive/RPG/campaigns/charged/cores/`

Priority:
1. `UVG 2E - Ultraviolet Grasslands and the Black City - Digital Small 1.0.pdf` — primary setting, locations, factions, creatures.
2. `2400_Xot_v1.2_singles.pdf` — system layer, tone.
3. `Synthetic_Dream_Machine_Eternal_Return_Key_BAREGHOST_EDITION.pdf` — mechanical flavour.

Also check `modules/` and `suplements/` for anything relevant.

Read enough to understand the broader lore landscape (locations the caravan hasn't reached yet, factions not yet encountered, creatures and phenomena that could surface).

## What to produce

### 1. Thread suggestions (up to 3)

Each suggestion should be:

- **Actionable** — something the GM can introduce in the next 1–3 sessions.
- **Grounded** — rooted in content that already exists in the repo (characters, hooks, locations, objects) or in the reference PDFs.
- **Connective** — it ties together two or more things that are currently unlinked or underused. Preference order:
  1. Connections between recent sessions and older published material (best: a thread from ep_001–003 that could resurface now).
  2. Connections between published content and reference lore (e.g. a UVG location or faction that maps onto something the PCs have already encountered).
  3. Hooks declared in front matter (`hooks:` field) that have never been followed up on.
  4. NPCs or locations that exist in the directory but have not appeared in any session log.

For each suggestion, provide:
- **Title** — a short, evocative name for the thread.
- **The connection** — what two (or more) existing elements it ties together, with file links.
- **The hook** — how the GM could introduce it at the table. One or two sentences, in-voice.
- **Source** — whether this draws from repo content, reference PDFs, or both.

### 2. Discovered tie-ins (optional)

If you find connections that already exist in the fiction but are not reflected in the file structure (e.g. a character mentioned in a session log who has no backlink from their directory entry, or two locations that are clearly related but not cross-linked), list them and **add the missing relative links directly to the files**.

Format link additions the same way existing links are formatted in the repo (relative paths with `.md` extensions). Only add links where the connection is clearly established in the text — do not invent connections.

## Procedure

1. Read `.agents/AGENTS.md`.
2. Read all campaign session logs (`campaigns/`) in chronological order (by `nav_order`).
3. Read all directory entries (`directory/`).
4. Read reference PDFs — focus on the UVG 2E core for locations, factions, and creatures the campaign might encounter next based on caravan trajectory.
5. Build a mental map of:
   - Active PCs, their hooks, and unresolved situations.
   - Locations visited vs. locations that exist in the directory but haven't appeared in session logs.
   - Hooks declared in front matter that remain open.
   - NPCs with no session appearances.
   - Lore from the PDFs that resonates with published content.
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
