---
name: add-chapter
description: Create and integrate a new campaign chapter or session log file with canonical YAML front matter, navigation ordering, region metadata, directory cross-links, and Charged setting voice.
argument-hint: session notes, title, or episode brief (optional)
---

# Add Chapter

Create and integrate a new chapter or session log into the campaign chronicles.

## 1. Intake & Clarification

If the user's prompt does not supply all required details, ask clarifying questions before writing:

1. **Campaign**: Which campaign does this chapter belong to?
   - Default is `UVG24XX` (`campaigns/UVG24XX/`) unless specified.
2. **Episode Number**: Automatically determine the next episode number by checking existing files in `campaigns/<Campaign>/` (e.g. `ep_010.md` -> `ep_011.md`).
3. **Chapter Title**: An evocative title matching the episode's central dilemma, creature, or weird event (e.g. *Potatoes*, *Shaggy and Fleshy*, *Doda now?*).
4. **In-Universe Date (`nav_order`)**: Date of the session in `YYYY-MM-DD` format (e.g. `3025-08-19`). Check the previous episode's date to maintain chronological order.
5. **Region & Location**: Where did the session take place? (e.g. `Last Serai`, `The Low Road and The High`, `Violet City`, `Fallen Umber`).
6. **Caravan Hub**: Which caravan index should be linked in the comment block? (Default is `[index](../../directory/Atles/index.md)` for `UVG24XX`).
7. **Session Notes**: Raw player actions, discoveries, trades, NPC interactions, debts, and mechanical consequences.

## 2. Entity Resolution & Cross-Linking

Before drafting the chapter prose:

1. **Identify mentioned entities**: Scan the session notes for all PCs, NPCs, factions, locations, and creatures.
2. **Search Directory**: Use `rg` to locate the exact filenames and paths in `directory/`.
3. **Format relative links**: Ensure every entity is linked on its first significant mention using relative paths (e.g. `[Kur (Barista)](../../directory/Atles/Barista.md)`, `[The Last Serai](../../directory/LastSerai/index.md)`).
4. **Clarify new connections**: If a new relationship between characters or factions emerges during the session, prompt the user for the specific relationship dynamic and whether to document it bidirectionally.

## 3. Template & Front Matter

Create the file as `campaigns/<Campaign>/ep_<NNN>.md`.

### Front Matter Specification

```yaml
---
layout: default
type: session
nav_exclude: false

parent: <Exact title of the campaign index, e.g. "UVG+24XX">
title: <Chapter Title>
region: <Region Name>
nav_order: <YYYY-MM-DD>
narration: 
footer_content: 

images:

---
```

> [!NOTE]
> - `type:` must be `session`.
> - `nav_order:` must be the in-universe date string (`YYYY-MM-DD`). Jekyll uses this to format the date in the chapter header and order episodes chronologically.
> - `narration:` is an optional list of character names if dedicated individual narrative sub-logs exist (e.g. `ep_011_Pilik.md`). Leave empty if none.

### Scaffolding & Comment Block

Immediately following front matter:

```markdown
{% include header_chapter.md %}
{% comment %}
`=map(this.images, (x) => "![im|200](" + x + ")")`
```dataview
LIST without ID "["+ title + "](" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE file.path != this.file.path SORT file.folder DESC
```
---

- [index](<relative_path_to_caravan_index.md>)

{% endcomment %}
```

> [!NOTE]
> The caravan link (e.g. `- [index](../../directory/Atles/index.md)`) inside the comment block ensures Jekyll's `_plugins/data_extractor.rb` builds bidirectional links connecting the caravan to this session.

## 4. Prose Formatting & Voice

Structure the chapter body into 2–4 themed subsections using `## Heading`:

1. **One sentence per line**: Write narrative prose using one sentence per line where practical.
2. **Heading cleanliness**: Always leave an empty blank line immediately following any Markdown heading (`#`, `##`, `###`).
3. **Setting register**:
   - British English spelling throughout.
   - Later-earth retro psychedelic science fantasy (Moebius, Vance, Wolfe).
   - Tone: caravan survival, strange commerce, absurd debt, soft body horror, broken futurity, and beautiful ruins.
   - Avoid purple prose or over-flourishing; dry, matter-of-fact absurdity works best.
4. **Factual fidelity**: Stay strictly faithful to the GM's play report. Do not invent plot developments, PC choices, or unearned successes.

## 5. Verification Checklist

After writing the file:
1. Verify that all internal links resolve to existing files on disk.
2. Confirm the sequential episode numbering and chronological date.
3. Run `bundle exec jekyll build` to ensure the site compiles cleanly.
4. Leave the created file unstaged in git for user review.
