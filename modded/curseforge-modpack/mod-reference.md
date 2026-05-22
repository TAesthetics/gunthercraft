# Gunthercraft Modpack — Mod Reference
# NeoForge 1.20.1 | CurseForge Modpack

## How to fill in fileIDs

Every entry in `manifest.json` needs a valid `fileID`.  
To find the fileID for a mod:

1. Go to the mod's CurseForge page
2. Click **Files** → filter by **NeoForge** + **1.20.1**
3. Click the correct file version
4. The fileID is the number at the end of the URL:
   `https://www.curseforge.com/minecraft/mc-mods/create/files/`**4624596**

Replace the `0` in `manifest.json` with that number.

---

## Mod List with projectIDs

| projectID | Mod | Category | CurseForge URL |
|-----------|-----|----------|----------------|
| 351264 | Kotlin for Forge | Dependency | https://www.curseforge.com/minecraft/mc-mods/kotlin-for-forge |
| 419699 | Architectury API | Dependency | https://www.curseforge.com/minecraft/mc-mods/architectury-api |
| 547270 | Forge Config API Port | Dependency | https://www.curseforge.com/minecraft/mc-mods/forge-config-api-port |
| 811925 | Timeless & Classics Zero | Warfare | https://www.curseforge.com/minecraft/mc-mods/timeless-and-classics-zero |
| 519791 | Create Big Cannons | Warfare | https://www.curseforge.com/minecraft/mc-mods/create-big-cannons |
| 250419 | MrCrayfish's Vehicle Mod | Warfare | https://www.curseforge.com/minecraft/mc-mods/mrcrayfish-vehicle-mod |
| 328085 | Create | Tech | https://www.curseforge.com/minecraft/mc-mods/create |
| 688231 | Create: Steam 'n' Rails | Tech | https://www.curseforge.com/minecraft/mc-mods/create-steam-n-rails |
| 437717 | Create Crafts & Additions | Tech | https://www.curseforge.com/minecraft/mc-mods/createaddition |
| 291584 | The Midnight | Horror | https://www.curseforge.com/minecraft/mc-mods/the-midnight |
| 829858 | Cave Dweller Reimagined | Horror | https://www.curseforge.com/minecraft/mc-mods/cave-dweller-reimagined |
| 618786 | From The Fog | Horror | https://www.curseforge.com/minecraft/mc-mods/from-the-fog |
| 228525 | MrCrayfish's Furniture Mod | RP | https://www.curseforge.com/minecraft/mc-mods/mrcrayfish-furniture-mod |
| 416089 | Simple Voice Chat | RP | https://www.curseforge.com/minecraft/mc-mods/simple-voice-chat |
| 412082 | Supplementaries | RP | https://www.curseforge.com/minecraft/mc-mods/supplementaries |
| 424371 | Alex's Mobs | Community | https://www.curseforge.com/minecraft/mc-mods/alexs-mobs |
| 667828 | FTB Library | Teams | https://www.curseforge.com/minecraft/mc-mods/ftb-library |
| 687943 | FTB Teams | Teams | https://www.curseforge.com/minecraft/mc-mods/ftb-teams |
| 667858 | FTB Chunks | Teams | https://www.curseforge.com/minecraft/mc-mods/ftb-chunks |
| 238222 | JEI (Just Enough Items) | Essentials | https://www.curseforge.com/minecraft/mc-mods/jei |
| 32274  | JourneyMap | Essentials | https://www.curseforge.com/minecraft/mc-mods/journeymap |
| 263420 | Xaero's Minimap | Essentials | https://www.curseforge.com/minecraft/mc-mods/xaeros-minimap |
| 317780 | Xaero's World Map | Essentials | https://www.curseforge.com/minecraft/mc-mods/xaeros-world-map |
| 908741 | Embeddium | Performance | https://www.curseforge.com/minecraft/mc-mods/embeddium |
| 581495 | Oculus | Performance | https://www.curseforge.com/minecraft/mc-mods/oculus |
| 535342 | FerriteCore | Performance | https://www.curseforge.com/minecraft/mc-mods/ferritecore |
| 257814 | Clumps | Performance | https://www.curseforge.com/minecraft/mc-mods/clumps |
| 790626 | ModernFix | Performance | https://www.curseforge.com/minecraft/mc-mods/modernfix |
| 566374 | Entity Culling | Performance | https://www.curseforge.com/minecraft/mc-mods/entity-culling |

---

## Notes

- **Superb Warfare** — verify CurseForge availability for NeoForge 1.20.1 before adding
- **Terra (Earth Map)** — not available as a NeoForge mod; use a pre-generated Earth Map world in `overrides/` instead, or set up Terra as a server plugin separately
- **NeoForge version** — `47.1.106` is used in `manifest.json`; update to the latest 47.x stable if needed: https://neoforged.net/

---

## Packaging for CurseForge

Once all fileIDs are filled in, zip the contents of this folder:

```
zip -r gunthercraft-1.0.0.zip manifest.json modlist.html overrides/
```

Then upload `gunthercraft-1.0.0.zip` to CurseForge or import it directly in the CurseForge App.
