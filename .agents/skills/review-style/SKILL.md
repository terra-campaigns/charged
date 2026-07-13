---
name: review-style
description: Review and polish a campaign file for the Charged setting voice. Use when a markdown file in campaigns/, directory/, systems/, or misc/ needs its prose brought into line with the later-earth retro psychedelic science-fantasy tone. Takes one file path as argument.
argument-hint: path to the markdown file to review (relative to repo root)
---

# Review Style

Apply the Charged setting voice to a campaign content file.
The goal is **minimal surgical edits that maximise flavour** — not a rewrite.

## Files to read before editing

**Always required to be in context:**
- `.agents/AGENTS.md` — for the canonical style rules, tone, and aesthetics.
- The target file itself.

**Also read for cross-reference (do not edit):**
- Nearby files in the same folder or parent folder, to absorb local naming conventions, existing tone, and linked content.

## What to change

1. **Prose voice.** Sharpen sentences toward the Charged register:
   - British English, with a very small touch of psychedelia.
   - Short, readable sentences. One sentence per line when practical.
   - Later-earth retro psychedelic science fantasy. Moebius, Miyazaki, Gene Wolfe, Jack Vance, Psychedelic Heavy Metal.
   - Caravan survival, decadent bureaucracy, strange commerce, absurd debt, soft body horror, broken futurity, beautiful ruins.
   - Do not over-flourish. A light hand is better than purple prose.

2. **Mechanical text.** Polish for readability, but never alter values, stats, dice, costs, or game meaning. If a hook or stat block reads flatly, you may tighten the wording — but the information must be identical.

3. **Formatting.** Follow existing conventions:
   - Skip a line between paragraphs, not within bulleted lists.
   - Preserve YAML front matter exactly as-is (keys, values, order).
   - Preserve all Liquid includes, Dataview queries, and Jekyll comment blocks verbatim.
   - Preserve all internal links exactly as they are (relative paths, `.md` extensions).
   - Preserve image references and gallery entries exactly.

## What NOT to change

- YAML front matter values (title, parent, nav_order, type, hooks, images, etc.).
- Liquid tags (`{% include ... %}`, `{% comment %}...{% endcomment %}`).
- Dataview code blocks.
- Internal link paths or link text that serves as a proper noun or canonical name.
- Game-mechanical values: dice, costs, hit points, inventory, stat lines.
- Content that is already in good voice — do not edit for the sake of editing.

## Procedure

1. Read `.agents/AGENTS.md` for the full style and tone reference.
2. Read the target file.
3. Read 2–3 nearby files in the same folder (siblings or parent index) to calibrate local tone and naming.
4. Identify passages where the prose is flat, generic, overly modern, or out-of-voice. Focus on:
   - Descriptions that lack texture (sensory detail, strangeness, or economy).
   - Sentences that are too long or too explanatory.
   - Mechanical text that is awkward but could be tightened without changing meaning.
5. Edit the file directly. The user will review changes line-by-line in the IDE.
6. If the file is already well-voiced, say so and make no changes.

## Calibration examples

These are illustrative, not prescriptive. Use them to calibrate intensity.

**Too flat:**
> The village is a place where retired caravan workers live. It has shops that sell used equipment.

**Too purple:**
> The village breathes with the dying exhalations of a thousand caravans, its market stalls dripping with the psychic residue of ten thousand journeys across the screaming wastes.

**In voice:**
> Village-camp of retired caravanserais that were not posh enough to retire in Violet City. It is a good place to trade for used caravan equipment and animals.

**Too flat:**
> The creature has many eyes and mouths and tries to eat her arm.

**In voice:**
> Shaggy opens its multitude of eyes and mouths within tongues within mouths within tongues. It tries to swallow her arm.

## Rules

- Never invent new lore, names, NPCs, locations, or continuity.
- Never remove content. If something reads poorly, improve it — do not delete it.
- When in doubt, leave it alone. The lightest edit that brings a passage into voice is the best edit.
- If the file is already well-voiced, say so and make no changes.
