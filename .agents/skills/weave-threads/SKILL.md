---
name: weave-threads
description: Analyse all published campaign content, reference lore, and trade goods price skews to surface up to 3 actionable tie-ins for future sessions. Discover lore from economic anomalies and iterate with the GM. No file path argument needed — this skill reads the entire repo.
argument-hint: none (reads the full repo) or optional trade good / focus topic
---

# Weave Threads

Read the full campaign corpus, reference PDFs, and trade goods data to find latent connections, forgotten threads, economic anomalies, and lore opportunities. Produce up to 3 actionable suggestions for future sessions, working iteratively with the GM when exploring price skews.

## Before starting: confirm with the user

When invoked, briefly confirm:

> I'll read all campaign content, trade ledgers, and reference digests. This will take a moment. Proceed?

If the user provided a specific trade good, region, or topic, confirm focusing on that area. Then begin.

## Files to read

### Repo content (use the Tier 1 catalogue)

- `.agents/AGENTS.md` — setting rules, tone, canon hierarchy.
- `.agents/context/catalog.json` — inspect all entities, parents, types, and connection graphs (`links_in` / `links_out`).
- `.agents/context/decisions.md` — active Tier 2 rulings.
- `trading/index.md` & `trading/*.md` — active trade goods, base values, price multipliers across trail stations, and market conditions (taboos, bubbles, crises, gluts).
- `.agents/context/trade_sheet_cache.csv` — raw trade multiplier data across trail stations.
- Use targeted reads on specific notes in `campaigns/` and `directory/` as needed to inspect specific details.

### Reference digests (Tier 3 canon — influence, not automatic canon)

Read from: `/Users/efsa/Library/CloudStorage/GoogleDrive-estevao.alvarenga@gmail.com/My Drive/RPG/campaigns/charged/_digests/`
(Consult `.agents/context/references.json` to find relevant files and sections).

Priority:
1. `uvg_2e_core.md` — primary setting, locations, factions, creatures, caravan rules.
2. `2400_xot.md` & `2400_exiles.md` — system layer, salvage, mechanics.
3. `sdm_eternal_return_key.md` — mechanical flavour, death, fantascience.
4. `the_alluring_trophy_gold.md` & `metamorphica_revised.md` — coastal incursions, mutations.
5. `electric_bastionland.md` — urban boroughs, failed careers, living machines, dilemma traps.

Read the digest summaries to understand the broader lore landscape (locations the caravan hasn't reached yet, factions not yet encountered, creatures and phenomena that could surface). Only inspect raw PDFs if exact table text or art is needed.

## What to produce

### 1. Thread suggestions (up to 3)

Each suggestion should be:

- **Actionable** — something the GM can introduce in the next 1–3 sessions.
- **Grounded** — rooted in content that already exists in the repo, trading tables, or reference digests.
- **Connective** — it ties together two or more things that are currently unlinked or underused. Preference order:
  1. Connections between recent sessions and older published material (best: an element from ep_001–003 that could resurface now).
  2. Trade goods price skews & market anomalies that reveal hidden lore (e.g. sudden markups, desperate shortages, strict taboos, or lucrative arbitrage routes that reflect faction conflicts, environmental crises, or occult rituals).
  3. Connections between published content and reference lore (e.g. an upcoming UVG location or faction that connects with the caravan's trajectory).
  4. NPCs or locations that exist in the directory but have empty `links_in` (no session appearances).
  5. Active PC situations and open contracts/debts.

For standard narrative suggestions, provide:
- **Title** — a short, evocative name for the thread.
- **The connection** — what two (or more) existing elements it ties together, with file links.
- **The hook** — how the GM could introduce it at the table. One or two sentences, in-voice.
- **Source** — whether this draws from repo content, reference digests, trade ledgers, or a combination.

For trade-skew-derived suggestions, provide:
- **Title** — an evocative name for the commercial or market thread.
- **The price skew** — item, price multiplier/divergence, stations involved, and local market condition (e.g. *Crystal shards: Porcelain Citadel €10/40 -> Steppe of Lime Nomads €200/800, $\times 20$ markup*).
- **The underlying lore** — the narrative reason for the price distortion (faction hoarding, technological necessity, sacred prohibition, impending catastrophe).
- **The table hook** — how the caravan encounters this (merchant rumours, strange cargo orders, customs blockades, desperate buyers).
- **Source** — link to the trade good note (`trading/*.md`) and related setting files.

### 2. Iterative lore discovery from trade skews

When an identified price skew exposes an unmapped aspect of the setting, do not lock in canon unilaterally. Instead, run an iterative brainstorm with the GM:

1. **Highlight the anomaly**: Present the trade good, the station price disparity, and any special market flags (`Crisis Demand`, `Market Bubble`, `Taboo`, `Illicit Contraband`).
2. **Offer 2–3 lore hypotheses**: Present distinct, evocative, setting-faithful explanations for why the price is skewed (e.g. option A: ritual use by a local cult; option B: military mobilisation by a rival faction; option C: ecological collapse or synthetic contamination).
3. **Solicit GM steer**: Ask the GM which hypothesis fits best, or invite them to tweak or combine elements.
4. **Consolidate**: Once agreed, weave the chosen lore into the session threads and record any firm table ruling in `.agents/context/decisions.md` if the GM confirms it.

### 3. Discovered tie-ins (optional)

If you find connections that already exist in the fiction but are not reflected in the file structure (e.g. a character mentioned in a session log who has no backlink from their directory entry, or two locations that are clearly related but not cross-linked), list them and **add the missing relative links directly to the files**.

Format link additions the same way existing links are formatted in the repo (relative paths with `.md` extensions). Only add links where the connection is clearly established in the text — do not invent connections.

## Procedure

1. Read `.agents/AGENTS.md`.
2. Inspect `.agents/context/catalog.json` and `.agents/context/decisions.md`.
3. Check `trading/index.md` and scan for significant price skews, extreme multipliers, or market anomalies (`Crisis Demand`, `Taboo`, `Market Bubble`, etc.).
4. Check recent session logs (`campaigns/UVG24XX/`) using line ranges for recent developments.
5. Consult Tier 3 digests in `charged/_digests/` for locations, factions, and creatures matching the caravan's trajectory.
6. Build a mental map of:
   - Active PCs, unresolved situations, and debt contracts.
   - Trade price skews and arbitrage corridors intersecting the caravan's route.
   - Locations visited vs. locations in the directory with no session appearances.
   - NPCs with empty `links_in` in `catalog.json`.
   - Lore from the digests that resonates with published content.
7. If exploring trade goods price skews, engage the GM iteratively with 2–3 potential lore explanations before locking in the final thread.
8. Identify the strongest thread candidates (up to 3). Rank by:
   - How naturally it could emerge from the current situation (recent sessions or trail position).
   - How far back it reaches (old threads resurfacing = high value).
   - How much it enriches existing lore rather than adding new complexity.
9. Write the output as an artifact (markdown file) and present it to the user.
10. If discovered tie-ins require link additions, edit the relevant files directly. The user will review line-by-line.

## Rules

- Never invent new canon unilaterally. Every suggestion must be grounded in existing repo content, reference PDFs, or trade ledgers.
- Treat price skew hypotheses as Tier 3 possibilities until the GM selects or refines them in conversation.
- Do not spoil content the PCs haven't encountered yet by writing it into session logs. Suggestions go into the artifact, not into campaign files.
- Suggestions should feel like they were always there, waiting to be noticed — not bolted on.
- Keep the artifact concise: 3 suggestions max, each no longer than a short paragraph.
- When adding links to files, follow existing formatting conventions exactly.
