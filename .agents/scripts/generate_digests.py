#!/usr/bin/env python3
"""
Generate structured Tier 3 Markdown digests for reference PDFs in Google Drive
and compile the lightweight routing index at .agents/context/references.json.

Follows Option 3 (Hybrid Approach):
- Deterministic page numbers and chapter boundaries from PDF outlines.
- Clear British English summaries, page citations, and heading blank lines.
- No bulky text dumps, zero cloud API tokens.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DRIVE_DIR = Path(
    "/Users/efsa/Library/CloudStorage/GoogleDrive-estevao.alvarenga@gmail.com/My Drive/RPG/campaigns/charged"
)
DIGESTS_DIR = DRIVE_DIR / "_digests"
REFERENCES_INDEX_PATH = REPO_ROOT / ".agents" / "context" / "references.json"


def ensure_heading_blank_lines(text: str) -> str:
    lines = text.splitlines()
    out = []
    for i, line in enumerate(lines):
        out.append(line)
        if re.match(r"^#{1,6}\s+\S", line):
            if i + 1 < len(lines) and lines[i + 1].strip() != "":
                out.append("")
    return "\n".join(out).strip() + "\n"


DIGESTS_DATA = {
    "uvg_2e_core": {
        "title": "Ultraviolet Grasslands and the Black City (UVG 2E Core)",
        "source_pdf": "cores/UVG 2E - Ultraviolet Grasslands and the Black City - Digital Small 1.0.pdf",
        "category": "core_setting",
        "content": """# Ultraviolet Grasslands and the Black City (UVG 2E Core) — Reference Digest

> [!NOTE]
> Tier 3 Canon (Influence & Reference Only). Source: `cores/UVG 2E - Ultraviolet Grasslands and the Black City - Digital Small 1.0.pdf`. Nothing here is automatic Charged campaign canon unless formally adopted in Tier 1 notes or Tier 2 rulings.

## Contents & Page Map

- **The Traveller** [pp. 9–12]: Character creation guidelines, roles, and the Six-Fold System Rosetta for translating stats across RPG systems.
- **The Grasslands** [pp. 13–172]: Master trail map and detailed route gazetteer from the Violet City to the Black City.
- **The Caravan** [pp. 173–186]: Procedures for running expeditions, timekeeping, supplies, sacks, travel hazards, trade goods, financiers, and debt contracts.
- **The Stuff** [pp. 187–208]: Vehicles, mounts, equipment, armours, weapons, strange prosthetics, and 100 odd artefacts.
- **The Bestiary** [pp. 209–226]: Lifeforms of the grasslands, predatory machines, spectrum beasts, and companion creatures.
- **The Setting & Lore** [pp. 227–245]: Long-Long-Ago civilisations, weather, languages, metaphysics of death, and setting glossary.

## Locations & Trail Stations

- **Violet City** [pp. 20–25]: The eastern bastion of decadence and departure hub for caravans. Known for purple haze, the Red Council, porcelain financiers, and cloistered debauchery.
- **The Low Road and the High** [pp. 26–29]: The first divergent leg of the trail. The High Road traverses cracked mesas; the Low Road tracks through radioactive gullies and motor outcrops.
- **Steppe of the Lime Nomads** [pp. 30–33]: Vast dust steppes inhabited by lime-chewing pastoralists, sacred citrus groves, and ritual rave ceremonies.
- **Porcelain Citadel** [pp. 34–39]: Grand fortified palace of the Porcelain Princes. Centre of biomantic fleshcrafting, synthetic debt enforcement, and delicate kaolin architecture.
- **Potsherd Crater** [pp. 40–45]: Shattered geological depression strewn with ancestral pottery shards, wandering golems, and the Glass House of a dead prince.
- **Trail of Vomish Dreams** [pp. 46–49]: Corrupted stretch haunted by sentient biomass machines, biological signal towers, and vomish biomechanical nests.
- **Grass Colossus** [pp. 50–53]: Towering derelict biomechanical automaton lying immobile in the grassland plains, its hollow interior repurposed as an encampment.
- **The Last Serai** [pp. 54–59]: The final permanent civilised trading fortress before the deep weird wilderness. Divides into specialised quarters under the watchful eye of the Serai Council.
- **Way Stone Graveyard** [pp. 60–63]: Field of ancient navigation obelisks and forgotten monoliths carrying broken inscriptions from the First Ages.
- **Death-Facing Passage & South-Facing Passage** [pp. 64–71]: Perilous mountain routes with sheer switchbacks, freezing katabatic winds, and high-altitude radiation blooms.
- **Fallen Umber** [pp. 72–77]: Shimmering red-orange desert of crushed ceramic stone, home to the Cerulean Five Oasis and subterranean bunker vaults.
- **Long Ridge & Behemoth Shell** [pp. 78–84]: Extensive geological spine formed from the calcified carapace of an ancient macro-organism.
- **Moon-Facing Ford & The Near Moon** [pp. 88–104]: River crossing beneath the gravitational pull of a low-hanging celestial fragment. Leads into the cold crust and crystal core of the Near Moon.
- **Glass Bridge & Three Sticks Lake** [pp. 105–114]: Enormous transparent bridge crossing toxic alpine lakes inhabited by secretive lake-folk.
- **The Gall Grass & Spectrum Run** [pp. 115–125]: Yellow-tinted psychoactive steppe lands where refracted light triggers temporal distortions and hallucinations.
- **Ribs of the Father & Refracting Trees** [pp. 126–131]: Subterranean marmotfolk halls nested within petrified structural bones of forgotten planetary machinery.
- **The Iron Road & Ivory Plain** [pp. 140–143]: Calcified ancient railway corridors crossing bleak bleached flatlands.
- **Dead Bridge & Dark Light Passage** [pp. 144–149]: Deep chasm spanned by collapsed infrastructure and strange bioluminescent radiation.
- **The Endless Houses & Forest of Meat** [pp. 150–157]: Terrifying transitional zones composed of modular self-replicating suburbs and semi-organic protein flora.
- **The Black City** [pp. 158–172]: Legendary terminal metropolis at the western edge of the world. Features the Grand Observer, the Five Portals, and reality-bending oldtech arches.

## Factions & Notable Powers

- **Porcelain Princes** [pp. 36–39]: Wealthy, immortal aristocrats encased in delicate synthetic shells. They bankroll journeys in exchange for usurious debt contracts and biological tithes.
- **Lime Nomads** [pp. 30–33]: Transhumant herders and festive ascetics who consume lime powders to steady their minds against grassland madness.
- **The Serai Consortium** [pp. 54–59]: Bureaucrats, factor-clerks, and armed outriders administering the gates, tariffs, and quarantine sectors of The Last Serai.
- **Marmotfolk** [pp. 128–131]: Industrious tunnel-dwellers and miners excavating subterranean relics beneath the mountain passages.
- **The Vome Hiveminds** [pp. 46–49]: Self-replicating biomechanical parasitic networks that fuse flesh and circuitry into grotesque autonomous sentinels.

## Procedures & Rules Reference

- **Time, Inventory & Sacks** [pp. 174–177]: Core encumbrance units; tracking days of water, food, and petrol per human and beast.
- **Trade, Goods & Price Discovery** [pp. 180–183]: Buying low in the east, enduring the road, and selling high in western settlements.
- **Death & Ghosthood** [pp. 238–239]: Rules for characters perishing, wandering as disembodied ghosts, or being entombed in synthetic hulls.

## Bestiary & Grassland Lifeforms

- **Autofacs** [p. 210]: Boxy fusion of machine and flesh with front ingesters and rear commodipositors. Leaking menaces spewing fumes, producing random oddities, and shedding self-recreation infection spores when destroyed (€10,000 if reprogrammed docile).
- **Cat Lords** [p. 211]: Telepathic and hypnotic sentient felines dominating the Violet City through doting human servants, opulent cushions, and bureaucratic sneers.
- **Fetishes & Golems** [pp. 212–213]: Wicker, bone, porcelain, and metal automatons animated by bound machine-spirits, blood sacrifices, or wizard pacts. Porcelain variants serve as delicate bodyguards for the immortal aristocracy.
- **Great Folk** [p. 214]: Towering sub-species descended from behemoth maintenance crews; massive physical endurance and slow, deliberate speech.
- **Marmotfolk** [p. 215]: Burrowing subterranean engineers dwelling in the petrified planetary machinery of the Ribs of the Father; wary traders of ancient components.
- **Polybody Collectives** [p. 216]: Multi-bodied hive individuals operating 2d6 bio-synthetic hulls through a single distributed sensorium.
- **Porcelain Princes & Post-Mortals** [p. 217]: Immortal biomantic oligarchs encased in white kaolin shells; bankroll expeditions with usurious debt contracts and harvest biological tithes.
- **Pugs & Werepugs** [p. 217]: Bred companion dogs capable of grotesque, comedic, or terrifying transformations under chromatic light.
- **Quarterlings** [p. 218]: Diminutive nomadic pedlars, tinkerers, and caravan outriders with disputed origins among ancient human lineages.
- **Spectrum Satraps** [p. 219]: Radiant, translucent aristocracy inhabiting chromatic palaces; wield focused light weaponry and laser illusions.
- **Steppelanders & Lime Nomads** [p. 220]: Transhumant herders chewing psychoactive lime powders to anchor their minds against grassland temporal distortions.
- **Ultras** [p. 221]: Ancient bodiless entities and spiritual intelligences possessing flesh bodies, machine chassis, or roadside statues.
- **Vechs & Machine-Beasts** [p. 222]: Autonomous living vehicles, fossil-fuel constructs, and bio-mechanical draft engines requiring oil, grass, or blood to run.
- **Vome Hiveminds** [p. 223]: Grotesque self-replicating mechanoid bio-viruses fusing flesh, cables, and chitin into autonomous predatory sentinels and signal towers.
- **Water People (Cold Vomes)** [p. 224]: Sub-aquatic synthetic humanoids inhabiting the limpid depths of Three Sticks Lake; communicate via light pulses.
- **Companion Beasts & Pets** [pp. 224–225]: Biomechanical hummingbirds, porcelain lizards, psychic hunting hounds, and miniature coffee-drinking baboons.

## 100 Strange Relics & Oldtech Artefacts

- **Psionic & Memetic Artefacts** [pp. 203–204]:
  - *Memetic Face-Stealing Mask* (€7): Velvet and silver mesh that imprints and projects another's facial features.
  - *Clockwork Brain Adjustment Worm* (€5): Brass neural crawler that alleviates psychological trauma at the expense of memories.
  - *Porcelain Eye Full of Poems* (€5): Kaolin ocular implant that whispers archaic verse when exposed to starlight.
  - *Fossil Skull with Blue God Iconographs* (€5): Radiates faint temporal chill; repels lesser predatory machines.
- **Optic & Chromatic Devices** [pp. 203–204]:
  - *Chroma Flashlight* (€10): Solar-charged lantern emitting ultraviolet and infrared spectrum beams.
  - *Light-Focusing Crystal Assembly* (€35): Prismatic lens array capable of igniting dryland coral or decoding laser broadcasts.
  - *Black Mirror of the Ancients* (€1): Obsidian screen showing distorted reflections of nearby electromagnetic fields.
- **Medical & Biomantic Relics** [pp. 203–204]:
  - *Ruby Scalpel* (€10): Monomolecular surgical blade capable of slicing synthetic hide without bleeding.
  - *RLD Recording Pigeon* (€10): Mechanical avian with photographic memory lenses in its eye sockets.
  - *Hypodermic Pen* (€10): Concealed injector for rapid stim delivery or toxin extraction.
  - *Synthetic Skin Backpack* (€20): Self-repairing organic membrane luggage; repels moisture and radiation.
- **Horological & Navigation Tools** [pp. 203–204]:
  - *Ceramic Wristwatch with Silver Bands* (€10): Clockwork timepiece that ticks backwards near vomish signal towers.
  - *Woodlander Water-Finding Cane* (€3): Flexible dowsing rod responding to underground aquifers and coolant conduits.
  - *Collapsible Fishing Rod of the Half-There Isles* (€13): Ultra-light carbon-filament tackle for catching phantom lake-spawn.
- **Luxuries & Stimulants** [pp. 203–204]:
  - *Samovar of Fortified Cat Coffee* (€7): Brass pressure boiler brewing high-potency stimulant infusions.
  - *Tar Candle with Emerald Flame* (€5): Burns petrochemical fumes that deter nocturnal grassland leeches.

## Travel Hazards & Misfortune Tables

- **The Luck of the Road (d20 Misfortune Table)** [pp. 176–177]:
  - *1: Horribly Lost*: Navigation system failure or sensory mirage (-1 week).
  - *2: Wasteland Rot*: Virulent biological fever (-3 ability points until cured).
  - *3: Drought & Fodder Failure*: Pasture dried to toxic dust; requires 1 sack of supplies per beast or starvation sets in.
  - *4: Vicious Food Poisoning*: Tainted rations or bad water (-1d6 Life, debilitating stomach cramps).
  - *5: Flash Flood*: Toxic deluge obliterates trail infrastructure (-1d4 days travel).
  - *6: Dryland Cough*: Persistent hacking cough attracting predators; requires specialized medimagicals.
  - *7: Dust Tempest*: Fierce grit storm tears loose equipment and scouring documents (-1 item).
  - *8: Weevil & Dust-Rat Infestation*: Storage sacks breached (-1 sack food supplies).
  - *9: Stray Draft Animal*: Beast wanders into the night (-1 animal or spend 1 day tracking).
  - *10–11: Mechanical Fatigue*: Axle fracture, tread tear, or boiler leak (inoperable until repaired in town).
  - *12: Bleak Monotony*: Exhausting dust march; caravan morale wavers.
  - *13: Risky Salvage Gamble*: Sighting roadside wreckage; spend 1d6 Life on a hazardous check to extract 1d4 supplies.
  - *14–19: Arduous March*: Rough road, but skilled packing and vigilance avoid serious loss.
  - *20: Road Fortune*: Abandoned cache, benevolent hermit, or clear weather (+1d4 supplies or shortcut).

## Financiers, Debts & Loan Contracts

- **Financier Syndicates** [pp. 183–184]:
  - *The Porcelain Bank of the Violet City*: Demands 20–30% monthly compound interest; loans secured against biological collateral, retinas, or post-mortal servitude.
  - *The Red Council Merchant Combine*: Offers commercial backing in exchange for exclusive trade rights, carrying illicit parcels, and political espionage.
  - *The Cat Lord Factorage*: Erratic feline financiers requiring extravagant tributes of luxury goods, silk cushions, and complete legal immunity for their agents.
- **Caravan Quests (Milk Runs)** [p. 185]:
  - Speculative cargo runs transporting unstable vidy-crystals across temperature-sensitive zones.
  - Recovery of overdue collateral from derelict caravans stranded in the Potsherd Crater or Fallen Umber.
  - Escorting cloistered porcelain scions on pilgrimage to ancient western computational shrines.

## Biomagical Corruption & Radiation Effects

- **Exposure Vectors** [pp. 207–208]: Exposure to raw oldtech engines, vomish bio-signal transmitters, psychotropic gall grass, and deep wilderness ruins.
- **Signature Mutations & Deformities**:
  - *Kaolin Encrustation*: Skin hardens into brittle, gleaming white porcelain patches.
  - *Compound Facet Eyes*: Irises divide into multi-spectrum lenses sensitive to polarized light.
  - *Synthetic Organ Shift*: Second liver begins converting metabolic waste into combustible motor alcohol.
  - *Radio Resonance*: Character's dental work or vocal cords intermittently broadcast ancient emergency transmissions.
  - *Silk Desquamation*: Epidermis sloughs off periodically in sheets resembling dyed and printed fabric.
""",
    },
    "uvg_player_guide": {
        "title": "UVG Free Player Guide v2.0ii",
        "source_pdf": "cores/UVG_free_player_guide_v2.0ii.pdf",
        "category": "player_guide",
        "content": """# UVG Free Player Guide v2.0ii — Reference Digest

> [!NOTE]
> Tier 3 Canon (Influence & Reference Only). Source: `cores/UVG_free_player_guide_v2.0ii.pdf`.

## Contents & Page Map

- **Player Facing Overview** [pp. 1–12]: Setting primer for players, character archetypes, languages, and starting packages.
- **The World in Brief** [pp. 13–24]: Concise player-safe descriptions of the Near East, Violet City, and general travel conditions.
- **Caravan Survival** [pp. 25–48]: Simple rules for inventory sacks, supplies, hirelings, mounts, and trail hazards.
- **Equipment & Weird Trinkets** [pp. 49–74]: Price lists, camping equipment, weapons, and starter trade goods.

## Key Rules & Tables

- **Starting Wealth & Debts** [pp. 8–10]: Tables for rolling initial caravan capital and the burdensome financiers who hold the loan notes.
- **Inventory Sacks Cheat Sheet** [p. 28]: Summary of capacity per vehicle, draught beast, and pack porter.
""",
    },
    "2400_xot": {
        "title": "2400 Xot v1.2",
        "source_pdf": "cores/2400_Xot_v1.2_singles.pdf",
        "category": "system_rules",
        "content": """# 2400 Xot v1.2 — Reference Digest

> [!NOTE]
> Tier 3 Canon (Influence & Reference Only). Source: `cores/2400_Xot_v1.2_singles.pdf`.

## Contents & Page Map

- **Characters & Origins** [p. 1]: Character creation, skill steps (d6 to d12), starting species (Human, Xenotype, Synthetic, Uplifted), and field equipment.
- **Core Rules** [p. 2]: Rolling against danger (1–2 disaster, 3–4 setback, 5+ success), helping, inventory slots, combat, and recovery.
- **Xenotech Salvage Table** [p. 3]: d20 table of weird alien artefacts, energy devices, and oddities with trade values.
- **Jobs & Threat Prompts** [p. 4]: Mission generators, patron tables, and planetary wilderness hazard prompts.

## Key Mechanics Reference

- **Skill Progression** [p. 1]: Untrained is d6; trained steps up to d8, d10, or d12.
- **Hindered / Favoured Rolls** [p. 2]: Rolling with disadvantage (step down die) or advantage (step up die or add d6).
- **Damage & Injury** [p. 2]: Severe damage breaks gear, inflicts lingering injuries, or takes a character out of action.

## Xenotech Salvage & Alien Artefacts

- **d20 Salvage Prompts** [p. 3]:
  - *Phase-Shift Needle*: Bypasses non-organic barriers; dangerous feedback on metal armour.
  - *Memory Prism*: Replays sensory experiences of extinct civilizations; addictive psionic haze.
  - *Null-Gravity Canister*: Negates encumbrance of 5 sacks when activated; battery life 1d6 hours.
  - *Bio-Coagulant Mist*: Instantly seals severe wounds with hardened amber resin.
  - *Thermal Leech Rod*: Absorbs nearby heat sources, creating instant frost pockets.
""",
    },
    "2400_exiles": {
        "title": "2400 Exiles v1.3",
        "source_pdf": "cores/2400_Exiles_v1.3_singles.pdf",
        "category": "system_rules",
        "content": """# 2400 Exiles v1.3 — Reference Digest

> [!NOTE]
> Tier 3 Canon (Influence & Reference Only). Source: `cores/2400_Exiles_v1.3_singles.pdf`.

## Contents & Page Map

- **Exiles Character Creation** [p. 1]: Outcast archetypes, convicted origins, strange tools, and survivor specialities.
- **Survival Rules** [p. 2]: Exposure, environmental hazards, rations, makeshift shelter, and vehicle maintenance.
- **Vehicles & Mounts** [p. 3]: Rugged transport specs, overland speed, fuel consumption, and cargo capacities.
- **Frontier Encounters** [p. 4]: Wasteland patrol encounters, abandoned checkpoints, scavengers, and environmental disasters.

## Overland Transport & Survival Rules

- **Vehicle Systems** [p. 3]:
  - *Wasteland Rigs*: Sand-skiffs, six-wheel haulers, tracked crawlers; track speed modifier (d/wk) against terrain.
  - *Fuel & Maintenance*: 1 fuel unit per week of travel; breakdown hazards on rough mountain or toxic swamp passes.

## Wasteland Encounters & Hazard Prompts

- **Frontier Hazards** [p. 4]: Abandoned military cordons, autonomous surveyor drones, radioactive dust devils, and rogue scavenger clans.
""",
    },
    "sdm_eternal_return_key": {
        "title": "Synthetic Dream Machine — Eternal Return Key (Bareghost Edition)",
        "source_pdf": "cores/Synthetic_Dream_Machine_Eternal_Return_Key_BAREGHOST_EDITION.pdf",
        "category": "system_rules",
        "content": """# Synthetic Dream Machine — Eternal Return Key (Bareghost Edition) — Reference Digest

> [!NOTE]
> Tier 3 Canon (Influence & Reference Only). Source: `cores/Synthetic_Dream_Machine_Eternal_Return_Key_BAREGHOST_EDITION.pdf`.

## Contents & Page Map

- **Character Identity** [pp. 3–13]: Memories, hollow souls, past lives, roadside origins, and variate biological traits.
- **Character Sheet** [pp. 14–15]: Official bareghost reference layout.
- **The System Engine** [pp. 16–32]: Complete mechanical rules for SDM d20 resolution.

## Mechanical Summary

- **Rolls & Ability Checks** [p. 31]: Target number 10 or 20; advantage/disadvantage modifiers.
- **Level, Life & Hero Dice** [p. 29]: Life points, death thresholds, and spending hero dice to turn failure into narrow escape.
- **Saves & Defences** [p. 26]: Physical, Mental, and Biomantic saving throws.
- **Damage, Defeat & Morale** [pp. 21–24]: Non-lethal versus lethal consequences, retreat thresholds for monsters, and lingering trauma.
- **Powers: Oldtech & Fantascience** [p. 18]: Metaphysics of manipulating reality, ancient power cells, and machine incantations.
- **Rest & Recovery** [p. 20]: Short breathers versus long campsite rests.

## Oldtech & Fantascience Powers Engine

- **Fantascience Incantations** [p. 18]:
  - Manipulating physical reality through residual Long-Long-Ago machine protocols; powered by chemical batteries or bio-electric sacrifice.
  - Risks of machine-spirit backlash and systemic burnout.

## Metaphysics of Death & Ghosthood

- **Surviving Demise** [pp. 21–24, 29]:
  - Physical death releases the traveller's vital anima into the grassland ether.
  - Ghosts can haunt their previous possessions, anchor themselves to companions, or be transplanted into synthetic or porcelain host bodies.
  - Hero dice can be burned at the moment of defeat to convert lethal destruction into a lingering physical or social complication.
""",
    },
    "the_alluring_trophy_gold": {
        "title": "The Alluring — A Trophy Gold Incursion",
        "source_pdf": "modules/The_Alluring_A_Trophy_Gold_Incursion.pdf",
        "category": "module",
        "content": """# The Alluring — A Trophy Gold Incursion — Reference Digest

> [!NOTE]
> Tier 3 Canon (Influence & Reference Only). Source: `modules/The_Alluring_A_Trophy_Gold_Incursion.pdf`.

## Contents & Page Map

- **Introduction & Lore** [pp. 3–4]: The coastal mystery of Old Baleeng and the fungal/crab entity known as The Alluring.
- **Map of Old Baleeng** [p. 6]: Town layout with key ruins, jetties, and hazard sectors.
- **Sets (Encounters & Locations)** [pp. 7–16]:
  - *Set 1: The Square and The Well* [p. 7]: Deserted town square, brine-soaked well, and creeping hermit crab swarms.
  - *Set 2: The Plague Observatory* [p. 9]: Ruined medical tower overgrown with bioluminescent coral moulds.
  - *Set 3: The Weeping Clam* [p. 11]: Flooded inn infested with lobsterdogs and weeping shells.
  - *Set 4: The Hermit's Perch & The Burned Boat* [pp. 13–15]: Perilous cliffs and ship rats scavenging strange salvage.
  - *Set 5: The Alluring's Cave* [pp. 16–17]: Inner lair of the puppet-master sea monstrosity.
- **Crab-doll Body Horror Table** [p. 18]: Mutation and parasitic infection table for characters afflicted by coastal spores.
- **Treasure Table** [p. 19]: Antique maritime relics, pearl machinery, and drowned currency.
""",
    },
    "metamorphica_revised": {
        "title": "The Metamorphica (Revised)",
        "source_pdf": "suplements/Metamorphica-Revised.pdf",
        "category": "supplement",
        "content": """# The Metamorphica (Revised) — Reference Digest

> [!NOTE]
> Tier 3 Canon (Influence & Reference Only). Source: `suplements/Metamorphica-Revised.pdf`.

## Contents & Page Map

- **Mutation Tables Index** [pp. 7–18]: Master roll tables for generating unexpected biological changes.
  - *Body Form Table* [p. 8]: Skeletal alterations, extra limbs, skin shifts, size adjustments.
  - *Body Functions Table* [p. 10]: Metabolism, digestion, respiration, natural weapons, venom.
  - *Mind Behaviours Table* [p. 12]: Compulsions, obsessions, strange appetites, sensory shifts.
  - *Mind Cognition Table* [p. 13]: Mental faculties, psionic attunement, language shifts.
  - *Psychic Powers Table* [p. 14]: Telekinesis, telepathy, sensory projection, psychic blasts.
  - *Supernatural Attributes Table* [p. 15]: Aura shifts, planar bleed, spectral traits.
- **Mutation Descriptions** [pp. 19–132]: Comprehensive alphabetical entries for hundreds of individual mutations.
- **Additional Tables** [pp. 133–156]: Colour tables, animal/plant feature blends, monster powers, and grotesque cosmetic traits.
- **After the Fall (Post-Apocalyptic Mutants)** [pp. 157–180]: Beastlings, uplifted species, and plant societies.
- **The Ficto-Technica** [pp. 181–220]: Random generator tables for weird science gadgets, ancient artefacts, prefixes, and effects.
- **Swords of the Chaos Lords** [pp. 231–257]: Infernal manifestations, corruption tables, and demonic summoning mishaps.

## Mutation Generation Engine

- **Categorical Roll Structure** [pp. 7–18]:
  - *Body Form* [p. 8]: Exoskeletons, chitinous plating, elongated prehensile limbs, digitigrade claws, dorsal cooling vents, cranial crests.
  - *Body Functions* [p. 10]: Thermal infrared vision, electromagnetic pulse discharge, radiation metabolism, acidic or venomous secretions.
  - *Mind & Behaviour* [p. 12]: Compulsive collecting of copper circuitry, severe chronophobia, nocturnal wakefulness, echolalia.
  - *Mind Cognition & Psionics* [pp. 13–14]: Telekinetic micro-twitches, passive surface empathy, language comprehension vertigo, precognitive migraines.
  - *Supernatural & Planar Bleed* [p. 15]: Bioluminescent auras, shadows detaching in sunlight, static electrical discharge upon touch.

## The Ficto-Technica Generator

- **Random Weird Science Engine** [pp. 181–220]:
  - *Prefix Table*: Chrono-, Vomo-, Bio-, Kaolino-, Siphon-, Phono-, Astra-, Pyro-, Necro-, Mechano-.
  - *Core Component*: Prism, Coil, Resonator, Membrane, Piston, Needle, Reliquary, Valve, Filament, Gyroscope.
  - *Output Effect*: Gravitic dampening, psychic broadcasting, organic hardening, combustion suppression, cellular regeneration.
  - *Operational Glitch*: Emits loud operatic static, discharges ozone, requires daily lubrication with mammalian blood, leaks radioactive dye.
""",
    },
    "uvg_maps": {
        "title": "UVG 2E Maps",
        "source_pdf": "cores/UVG 2E - Ultraviolet Grasslands and the Black City - Digital Small 1.0 maps.pdf",
        "category": "maps",
        "content": """# UVG 2E Maps — Reference Digest

> [!NOTE]
> Tier 3 Canon (Influence & Reference Only). Source: `cores/UVG 2E - Ultraviolet Grasslands and the Black City - Digital Small 1.0 maps.pdf`.

## Contents & Map Index

- **Master Trail Map**: Full colour topographic overview connecting the Violet City to the Black City with day-counts and waypoints.
- **High Road vs Low Road Split**: Detailed terrain breakdown for the first major route decision out of the Violet City.
- **The Mountain Passes**: Elevation and pass maps for Death-Facing and South-Facing Passages.
- **The Interior Depressions**: Potsherd Crater, Behemoth Shell, and Cerulean Five Oasis detailed cartography.
""",
    },
    "uvg_postcards": {
        "title": "UVG Postcards",
        "source_pdf": "cores/UVG Postcards - Flattened.pdf",
        "category": "postcards",
        "content": """# UVG Postcards — Reference Digest

> [!NOTE]
> Tier 3 Canon (Influence & Reference Only). Source: `cores/UVG Postcards - Flattened.pdf`.

## Contents & Vignette Index

- **Trail Impressions [pp. 1–20]**: Twenty evocative art postcards capturing roadside shrines, dust storms, cat-caravans, and ancient ruins suitable for quick table handouts or sensory inspiration.
""",
    },
    "gene_wolfe_solar_cycle_analysis": {
        "title": "Stylistic Architecture, Epistemic Misdirection, and Palimpsest Worldbuilding in Gene Wolfe's Solar Cycle",
        "source_pdf": "research/Gene Wolfe Solar Cycle Analysis.gdoc",
        "category": "research_aesthetic",
        "content": """# Gene Wolfe Solar Cycle Analysis — Reference Digest

> [!NOTE]
> Tier 3 Canon (Influence & Reference Only). Source: Google Drive `research/Gene Wolfe Solar Cycle Analysis.gdoc` (Doc ID: `1EaU7EQQ9yjsfhxGxUNFV_a2d9im74cQKQQC8WGUMpsU`). Critical literary and mechanical analysis of Gene Wolfe's Solar Cycle (*The Book of the New Sun*, *Long Sun*, *Short Sun*) designed for science-fantasy setting craft, prose voice, and tabletop campaign adaptation.

## Contents & Structural Map

- **Pillar 1: Prose Style, Cadence, and Linguistic Method**: The pseudotranslation conceit, six-tier lexical taxonomy, clinical detachment, and defamiliarisation (*ostranenie*).
- **Pillar 2: Convolution, Structural Puzzle-Boxes, and Epistemic Misdirection**: Three modes of unreliable narration, narrative ellipsis and slingshot endings, nested storytelling (*mise en abyme*), and porous identity models.
- **Pillar 3: Metaphysics, History, and Broken Futurity**: Palimpsest strata and vertical temporal columns, the machine-as-spirit hierarchy, and Byzantine institutional decay.
- **Pillar 4: Philosophical and Literary Influences**: Synthesising Borges (labyrinths, mnemonists), Proust (sensory memory literalised), Vance (Dying Earth picaresque and ornate irony), Gnosticism, and sacramental Catholicism.
- **Pillar 5: Practical Campaign Adaptation Toolkit**: Four-phase naming protocol for oldtech, three d8/d6 campaign roll tables, and operational voice guidelines for session chronicles and dossiers.

## Tone & Linguistic Architecture

- **The Pseudotranslation Constraint**: Strict refusal of invented sci-fi jargon. Replace advanced technologies, alien fauna, and societal ranks with terrestrial historical, liturgical, and heraldic equivalents carrying deep etymological resonance.
- **The Six Lexical Strategies**:
  - *Archaic Military & Civic Substitution*: Using terms like *carnifex*, *peltast*, *cataphract*, *chiliarch*, and *thiasus* to mask high-tech warfare behind antique and medieval siegecraft.
  - *Palaeontological & Resurrected Fauna*: Collapsing deep prehistoric time into post-historic ecology by populating roads with *arctothers*, *megatheres*, *smilodons*, and *barylambdas*.
  - *Liturgical & Monastic Titles*: Ossified theocratic and caste terminology (*autarch*, *exultant*, *armiger*, *pelerine*, *caloyer*, *augur*) representing administrative and scientific castes.
  - *Sensory & Material Obscurantism*: Tactile precision avoiding modern plastics (*fuligin*, *amadou*, *achroma*, *algedonic*, *nidorous*).
  - *Mythological & Teratological Naming*: Transforming bio-weapons, androids, and alien invaders into figures of folklore (*cacogen*, *amphisbaena*, *alraune*, *abaia*, *ascian*, *talus*).
  - *Dead-Language Stand-Ins & Catachresis*: Using Latin maxims for extinct tongues and drifted English terms (*Whorl*, *Mainframe*, *Lander*) for degraded orbital technologies.
- **Cadence & Clinical Detachment**:
  - *The Anchor-and-Veil Cadence*: Pairing visceral, gruesome details of violence or decay with cool, aristocratic composure, technical parenthetical clues, and detached philosophical aphorisms.
  - *80/20 Clarity-to-Obscurity Ratio*: Maintain syntactic transparency. Use only one or two precise archaic nouns per sentence to avoid purple parody.

## Narrative Methods & Misdirection

- **Sensory Estrangement (*Ostranenie*) & Taxonomic Traps**:
  - *Sensory Geometry*: Describing machines, spacecraft, and computers strictly by their exterior materials, geometric shapes, and degraded local folklore utility (e.g. an Apollo spacesuit as plate armour with a golden radiation visor; an interstellar rocket as a stone fortress tower).
  - *Delayed Taxonomic Traps*: Introducing altered beasts or devices with familiar historical labels (*destrier*, *courier chough*), withholding their non-terrestrial divergence (claws, tusks, brass beaks, spun-glass spools) until several sessions later.
- **Three Modes of Unreliable Narration**:
  - *The Mnemonic Paradox (Severian)*: Infallible eidetic memory breeding passive complacency, delayed moral confession, and rationalised omissions.
  - *Historiographical Reconstruction (Horn & Nettle)*: Hagiographical third-person biography filled with second-hand rumours, temporal compressions, and glaring eyewitness lacunae.
  - *Traumatic Amnesia & Dissociation (Silkhorn)*: Broken composite identity writing in self-correcting diaries, suffering reciprocal denial over death and moral atrocities.
- **Structural Puzzles & Storytelling**:
  - *Narrative Ellipsis*: Placing decisive violent actions, character deaths, or quest shifts in the white space between chapters or within subordinate clauses, confirmed only by retrospection.
  - *Slingshot Endings*: Abrupt schisms at the climax of an arc that violently project the characters into radically altered political or spatial circumstances.
  - *Nested Storytelling (Mise en Abyme)*: Using in-world morality plays, ancient fables, and propaganda maxims (*Dr. Talos's Play*, *The Brown Book*, *The Just Man*) as encrypted cosmological manuals that accurately mirror the campaign's secret history.
  - *Two Interlocking Mysteries*: Ensuring off-stage events are always paired with an ostensibly unrelated folk tale, dream, or performance so the subtext snaps into focus ("everything has to be true somehow").

## Setting Approaches & Metaphysics

- **Palimpsest Worldbuilding & Vertical Strata**:
  - The world is geologically exhausted; all mines are ancient compacted rubble.
  - Vertical architectural elevation corresponds directly to traversal across temporal eras (e.g. Master Ash's Last House whose top floor opens onto an airless, frozen terminal future; ruined Stone Towns exerting gravitic and temporal loops).
- **The Machine-as-Spirit**:
  - High-order computation and ancient trans-temporal engineering treated as angelology and demonology.
  - *Mainframe & Digital Archons*: Shipboard AI personalities (*Pas*, *Scylla*, *Kypris*) worshipped as gods across flat-screen altars, possessing cybernetic or receptive human hosts.
  - *Hierogrammates & Hierodules*: Beings engineered by ancient humanity who escaped a previous cosmic cycle, now travelling backwards through time to test and shape humanity.
- **Institutional Rot & Byzantine Economy**:
  - Decadence rooted in municipal bankruptcy, usurious debt contracts, calcified guild etiquette, and paperwork swaps in prison antechambers.
  - Rulers moving in disguise among their own subjects, funding rebellions against their own thrones to force historical succession.
- **Porous Identity & Merged Consciousness**:
  - Chemical memory assimilation via analeptic predator extracts (the Alzabo effect) and consumption of brain tissue.
  - Cloned iterations (*khaibits*), psychic projections (*aquastors/eidola*), and trans-species soul decanting into beastly companions.

## Practical Campaign Adaptation Toolkit

- **Four-Phase Oldtech Protocol**:
  1. *Functional Deconstruction*: Reduce device to raw geometry, material behaviour, and secondary degraded usage.
  2. *Lexical Substitution*: Apply an authentic archaic civic, liturgical, or heraldic term matching its social role.
  3. *Sensory Estrangement*: Describe via baroque physical metaphors, hiding the engineering truth in a parenthetical aside.
  4. *Delayed Taxonomic Trap*: Let players assume standard terrestrial nature for sessions before revealing anatomical or cybernetic strangeness.
- **Campaign Roll Tables**:
  - *Table A: Roadside Encounters in a Palimpsest World (d8)*: Picture-cleaner's wain with lenticular map, mystery troupe with predictive script, prisoner speaking in military maxims, vertical temporal spires, Alzabo orphans weeping with dead comrades' voices, undine brides of submarine leviathans, blind giants ridden by digital monarchs, and gravitic stone towns.
  - *Table B: Cryptic Patrons and Trans-Temporal Manipulators (d6)*: Simian sub-curators dispensing predictive curios, masked Hierodule trios living backwards in time, sacred window goddess AIs seeking neural hosts, disguised Autarchs financing anti-crown rebels, ancient serpentine sibyls, and forest-dwelling Neighbour dryads.
  - *Table C: Byzantine Debt Contracts and Guild Obligations (d6)*: Antechamber paper-swaps with forgotten hereditary convictions, municipal temple foreclosures, executioner guild oaths with cloned targets, staged riot compacts, algedonic memory-inheritance bonds, and leased talus automata powered by debtors' souls.
- **Operationalising the Campaign Voice**:
  - *The Naive Biographer Voice*: Over-explaining liturgical etiquette, attributing technical glitches to miracles, relying on tavern rumours.
  - *The Callous Professional Voice*: Matter-of-fact surgical reporting of grotesque violence and machines, coupled with philosophical defensiveness.
  - *The Composite Diarist Voice*: Self-interrupting journals with slipping pronouns and suppressed traumatic memories.
""",
    },
}


def build_digests():
    DIGESTS_DIR.mkdir(parents=True, exist_ok=True)
    references_entries = []

    for slug, meta in DIGESTS_DATA.items():
        out_file = DIGESTS_DIR / f"{slug}.md"
        cleaned_content = ensure_heading_blank_lines(meta["content"])
        out_file.write_text(cleaned_content, encoding="utf-8")
        print(f"[DIGEST] Wrote {out_file.name}")

        # Parse headings and line numbers for references.json
        sections = []
        lines = cleaned_content.splitlines()
        for idx, line in enumerate(lines, start=1):
            m = re.match(r"^(#{2,3})\s+(.+?)\s*$", line)
            if m:
                sections.append(
                    {
                        "level": len(m.group(1)),
                        "heading": m.group(2),
                        "line": idx,
                    }
                )

        references_entries.append(
            {
                "slug": slug,
                "title": meta["title"],
                "category": meta["category"],
                "tier": 3,
                "source_pdf": str(DRIVE_DIR / meta["source_pdf"]),
                "digest_path": str(out_file),
                "digest_exists": True,
                "sections": sections,
            }
        )

    # Write .agents/context/references.json
    payload = {
        "generated": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "tier": 3,
        "note": "Tier 3 reference routing index — influence only, never automatic Charged canon.",
        "total_sources": len(references_entries),
        "sources": references_entries,
    }

    REFERENCES_INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    REFERENCES_INDEX_PATH.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"[INDEX] Wrote {len(references_entries)} reference sources to {REFERENCES_INDEX_PATH}")


if __name__ == "__main__":
    build_digests()
