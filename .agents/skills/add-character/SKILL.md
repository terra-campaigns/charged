---
name: add-character
description: Create and integrate a new PC or NPC character note into the Charged directory with canonical YAML front matter, navigation parentage, campaign cross-link, Dataview scaffolding, and setting voice.
argument-hint: brief character concept, name, or role (optional)
---

# Add Character

Create and integrate a new character note (PC or NPC) into the Charged campaign directory.

## 1. Intake & Clarification

If the user's initial prompt does not supply all necessary details, ask clarifying questions before writing:

1. **Character Type**: Is this a Player Character (PC) or Non-Player Character (NPC)?
2. **Name & Title**: Full name and any epithets or formal titles.
3. **Role / Vocation**: Evocative later-earth vocation (e.g. *Redland bourgeoise mendicant healer*, *Wildfolk cult bio-mechanic*, *Financier from Banco de Aventuras*).
4. **Parent Directory Hub**: Which location, caravan, or faction folder does this character belong to?
   - Match the `parent:` field to the exact `title:` of the folder's `index.md` file (e.g. `Atles' Catlord Caravan` for `directory/Atles/`, `The Last Serai (8)` for `directory/LastSerai/`, `Violet City (1)` for `directory/VioletCity/`).
5. **Campaign Affiliation**: Which campaign does this character pertain to?
   - Available campaigns are in `campaigns/` (e.g. `UVG24XX`, `Anthology`).
   - Default is `UVG24XX` unless specified.
   - This determines the relative backlink placed inside the `{% comment %}` block so that Jekyll's data extractor links the character to that campaign.
6. **Key Details**:
   - **For PCs**: Background roll answers (Why are you on the road? Signature item? Machine interface or odd family connection? Disaster survived? Affinity pet?) and their debt contract (€ amount and creditor).
     - *Ignore* game abilities, inventory, and starting caravan data if supplied.
   - **For NPCs**: Motivation, strange technology, soft body horror, debts/patrons, and relationships with existing characters or factions.

## 2. Canon & Collision Check

Before creating the file:

1. Search existing files using `rg` for the character's proposed name to avoid duplicate titles or naming clashes.
2. Search for related NPCs, locations, or factions in `directory/` to identify potential cross-links.
3. Check the folder's `index.md` to confirm the exact `title:` value to use for `parent:`.

### Entity Relationships & Cross-Linking

When the user mentions or requests a connection between this character and another entity (PC, NPC, faction, or location):
1. **Prompt for relationship type**: If the prompt does not specify the exact dynamic, ask the user for the nature or reason of the relationship (proposing fitting setting options or allowing write-ins) rather than inventing continuity.
2. **Confirm link directionality**: Ask whether to update both character/entity files (bidirectional link) or only the newly created note.
3. **Format cross-links**: Use relative markdown links with `.md` extensions (e.g. `[Kur (Barista)](Barista.md)`) embedded naturally within the background or flavour sentences.

## 3. Template & Front Matter

Create the file in the designated subfolder (e.g. `directory/<Subfolder>/<ShortName>.md`).

### Front Matter Specification

```yaml
---
layout: default
template: 0.4
type: people
nav_exclude: false

parent: <Exact title of the parent index.md>
title: <Full Character Name>
role: <Vocation / Title>
status: 

images: 

---
```

> [!IMPORTANT]
> - Do **not** include the `hooks:` field. It has been discontinued.
> - `type:` must always be `people`.
> - `parent:` must exactly match the parent page's front matter `title`.
> - `status:` is reserved strictly for short symbols (such as `†` for deceased or a symbol when missing). Never put descriptive text or conditions here, as Jekyll prepends `status` directly to the character's name in galleries and headers. Document injuries and conditions in the markdown body instead.

### Scaffolding & Campaign Backlink

Immediately following the front matter, include the directory header and the Dataview comment block:

```markdown
{% include header_directories.md %}
{% comment %}
`=map(this.images, (x) => "![im|200](" + x + ")")`
```dataview
LIST without ID "["+ title + "](" + regexreplace(file.path, ".md", "") + ")" + ", from " + regexreplace(file.folder, "^[^\/]*\/", "") FROM ([[]]) OR outgoing([[]]) WHERE file.path != this.file.path SORT file.folder DESC
```
---
[campaign-relationship](<relative_path_to_campaign_index.md>)
{% endcomment %}
```

> [!NOTE]
> The link `[campaign-relationship](<relative_path_to_campaign_index.md>)` inside the comment block is parsed by Jekyll's native `_plugins/data_extractor.rb` to generate cross-link backlinks between the character and the campaign page. Calculate the relative path from the character's file location to the target campaign's `index.md` (e.g. `../../campaigns/UVG24XX/index.md` from `directory/Atles/`).

## 4. Prose Formatting

### For Player Characters (PCs)

Format background traits in bold question-and-answer pairs, separated by actual empty Markdown lines, followed by a debt contract:

```markdown
**Why are you on the road?** [Evocative reason, portents, or prophecy].

**What is your signature item?** [Weird relic, odd machine, or chitinous oddity].

**[Background Trait / Machine Interface / Star Sign / Family Connexion]:** [Detail].

**What disaster have you survived?** [Historical war, pacification, or vomish outbreak].

You have to repay € [Amount] to [Creditor / Patron] by the end of the caravan season.
```

> [!IMPORTANT]
> - **Always leave an empty blank line** between each prompt item; otherwise, Markdown parser will collapse consecutive lines into a single sentence on the rendered HTML page.
> - **Ignore abilities, inventory, and starting caravan** data when ingesting PCs. Do not include stat blocks, dice pools, rations, or mount lists.

### For Non-Player Characters (NPCs)

Write 2–4 short, punchy sentences in the Charged voice (one sentence per line where practical):
- Focus on decadent bureaucracy, absurd debts, soft body horror, odd machinery, or physical oddities.
- Connect the NPC to existing characters or factions using relative markdown links (e.g. `[Severa D'Arange](../VioletCity/Severa.md)`).

## 5. Verification Checklist

After writing the file:
1. Verify that all internal links resolve to existing files.
2. Confirm the heading spacing rule (blank line after any markdown headings).
3. Ensure British English spelling throughout.
4. Leave the created file unstaged in git for user review.
