# AGENTS.md

This file provides context about this Obsidian vault for AI agents.

## Vault Overview

This vault is a comprehensive TTRPG campaign management system and world-building gazetteer, specifically designed to function as the source for a Jekyll-based static website. It primarily documents adventures in the **Ultra Violet Grasslands (UVG)** setting, utilising the **24XX** and **Charged RPG** systems to facilitate a 'weird science-fantasy' aesthetic.

## Organization

The vault follows a highly structured, folder-based hierarchy designed for both navigation and web publishing:

- **`campaigns/`**: Organized by specific game runs (e.g., *UVG24XX*, *FailedExports*). Files within follow a chronological episodic naming convention (e.g., `ep_001`, `ep_002`).
- **`directory/`**: Acts as a world gazetteer or atlas. Subfolders represent major regions or hubs (e.g., *Atles*, *Violet City*, *Low Road High*, *Lime Nomads*), each containing an `index` file and individual notes for specific points of interest, NPCs, or factions.
- **`systems/`**: Contains mechanical data and scripts, specifically integration with the **Perchance** random generator platform for the 'Charged RPG' system.
- **Web Infrastructure**: Folders like `_includes`, `_sass`, and `_site` indicate the vault is managed as a codebase for a digital garden or campaign wiki.

Notes are connected through a hub-and-spoke model where `index` files serve as Maps of Content (MOCs) for their respective directories.

## Key Topics

- **Ultra Violet Grasslands (UVG)**: The primary science-fantasy setting for the campaigns.
- **24XX & Charged RPG**: The rules-light TTRPG systems being utilised for gameplay and procedural generation.
- **Episodic Session Logs**: Detailed records of gameplay sessions (e.g., *Failed Exports*, *Anthology*).
- **Regional World-building**: Deep dives into specific locales including *Atles*, *The Porcelain Citadel*, *Last Serai*, and *The Folded Below*.
- **Procedural Generation**: Extensive use of Perchance scripts for 'Charged RPG' and UVG-specific tables.
- **NPC & Faction Tracking**: Detailed character dossiers located within regional directories (e.g., *Cianur*, *Barista*, *Leonti Vites*).

## User Preferences

The user demonstrates a strong preference for **structured, modular documentation**. Note titles are concise and follow a strict naming schema (e.g., `ep_XXX` for sessions), suggesting the agent should maintain this consistency when suggesting new files.

The writing style leans towards the **descriptive yet functional** tone common in OSR (Old School Renaissance) gaming—prioritising clarity, atmosphere, and 'gameable' information over long-form prose. There is also a clear technical preference for integrating automated tools and web-ready formatting, such as Liquid tags and frontmatter.

## Custom Instructions

- **Naming Conventions**: Always use the `ep_00X` format for session logs and ensure every new directory has an `index.md` file to maintain the MOC structure.
- **Cross-Linking**: When mentioning a location or NPC in a campaign log, check the `directory/` folder to create a [[WikiLink]] to the corresponding entry.
- **TTRPG Context**: Assume a 'weird fantasy' or 'science-fantasy' aesthetic consistent with the Ultra Violet Grasslands setting when generating creative content.
- **Technical Awareness**: Be mindful that markdown files contain Liquid tags or frontmatter intended for static site generation; preserve these structures during edits.
- **Hub-and-Spoke Maintenance**: When adding a new note to a sub-directory, ensure it is linked within that directory's `index.md` file.
