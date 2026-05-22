# Gunthercraft Modpack - Server Mods List
# NeoForge 1.20.1
# ==========================================
# SERVER-SIDE ONLY. Do NOT install client-only mods on the server!
# Client-only mods: Rubidium, Oculus, JourneyMap client, Xaero's maps

## REQUIRED - Loader & Dependencies

| Mod | Download | Notes |
|-----|----------|-------|
| NeoForge 1.20.1 | https://neoforged.net/ | Download server installer |
| Kotlin for Forge | https://www.curseforge.com/minecraft/mc-mods/kotlin-for-forge | Dependency for many mods |
| Architectury API | https://www.curseforge.com/minecraft/mc-mods/architectury-api | Dependency |
| Forge Config API Port | https://www.curseforge.com/minecraft/mc-mods/forge-config-api-port | Dependency |

---

## WARFARE & MILITARY
*(Requested by: Cataclysm, CyberEnigma0, Smocka Republika, Jame Key Lie)*

| Mod | Download | Server-side? |
|-----|----------|--------------|
| Timeless & Classics Zero (TCZ) | https://www.curseforge.com/minecraft/mc-mods/timeless-and-classics-zero | YES - Required |
| Superb Warfare | https://www.curseforge.com/minecraft/mc-mods/superb-warfare | YES - Required |
| Create Big Cannons (CBC) | https://www.curseforge.com/minecraft/mc-mods/create-big-cannons | YES - Required |
| Immersive Vehicles | https://www.curseforge.com/minecraft/mc-mods/mrcrayfish-vehicle-mod | YES - Required |

---

## CREATE & TECH
*(Requested by: earlynyancat)*

| Mod | Download | Server-side? |
|-----|----------|--------------|
| Create (NeoForge) | https://www.curseforge.com/minecraft/mc-mods/create | YES - Required |
| Create: Steam 'n' Rails | https://www.curseforge.com/minecraft/mc-mods/create-steam-n-rails | YES - Required |
| Create Crafts & Additions | https://www.curseforge.com/minecraft/mc-mods/createaddition | YES - Required |

**Create dependencies (auto-installed via CurseForge App, download manually otherwise):**
- Flywheel (Create rendering lib)

---

## WORLD & MAPS
*(Requested by: david)*

| Mod | Download | Server-side? |
|-----|----------|--------------|
| Terra (Earth Map Generator) | https://www.curseforge.com/minecraft/mc-mods/terra | YES - worldgen |
| Xaero's Minimap | https://www.curseforge.com/minecraft/mc-mods/xaeros-minimap | Client-only (no server install needed) |
| Xaero's World Map | https://www.curseforge.com/minecraft/mc-mods/xaeros-world-map | Client-only |

**Terra setup:**
After installation, place the Earth Map pack in `config/terra/packs/`
Use the EarthMC pack or a custom Terra pack.

---

## HORROR & ATMOSPHERE
*(Requested by: Jame Key Lie)*

| Mod | Download | Server-side? |
|-----|----------|--------------|
| The Midnight | https://www.curseforge.com/minecraft/mc-mods/the-midnight | YES - Required |
| Cave Dweller Reimagined | https://www.curseforge.com/minecraft/mc-mods/cave-dweller-reimagined | YES - Required |
| From The Fog (Herobrine) | https://www.curseforge.com/minecraft/mc-mods/from-the-fog | YES - Required |

---

## CYBERPUNK & ROLEPLAY
*(Requested by: CyberEnigma0)*

| Mod | Download | Server-side? |
|-----|----------|--------------|
| MrCrayfish's Furniture Mod | https://www.curseforge.com/minecraft/mc-mods/mrcrayfish-furniture-mod | YES - Required |
| Simple Voice Chat | https://www.curseforge.com/minecraft/mc-mods/simple-voice-chat | YES - Required (server + client!) |
| Supplementaries | https://www.curseforge.com/minecraft/mc-mods/supplementaries | YES - Required |

**Simple Voice Chat port:**
Open port 24454 (UDP) in your firewall!
Config: `config/voicechat/voicechat-server.properties`

---

## OTHER COMMUNITY REQUESTS

| Mod | Download | Server-side? |
|-----|----------|--------------|
| Spore Mod (Cataclysm) | Not available for NeoForge 1.20.1 — Alternative: Alex's Mobs https://www.curseforge.com/minecraft/mc-mods/alexs-mobs | YES |

---

## PERFORMANCE (SERVER-SIDE)

| Mod | Download | Notes |
|-----|----------|-------|
| FerriteCore | https://www.curseforge.com/minecraft/mc-mods/ferritecore | RAM optimization |
| Clumps | https://www.curseforge.com/minecraft/mc-mods/clumps | XP orb merging |
| ModernFix | https://www.curseforge.com/minecraft/mc-mods/modernfix | Startup & RAM |
| Radium (server Sodium port) | https://www.curseforge.com/minecraft/mc-mods/radium-reforged | Server performance |

---

## PROTECTION & TEAMS

| Mod | Download | Server-side? |
|-----|----------|--------------|
| FTB Teams | https://www.curseforge.com/minecraft/mc-mods/ftb-teams | YES - Required |
| FTB Chunks | https://www.curseforge.com/minecraft/mc-mods/ftb-chunks | YES - Required |
| FTB Library | https://www.curseforge.com/minecraft/mc-mods/ftb-library | YES - Dependency for FTB |

---

## ESSENTIALS (SERVER-SIDE)

| Mod | Download | Notes |
|-----|----------|-------|
| JEI (Just Enough Items) | https://www.curseforge.com/minecraft/mc-mods/jei | Also works server-side for recipes |
| Crafting Tweaks | https://www.curseforge.com/minecraft/mc-mods/crafting-tweaks | Optional |

---

## CLIENT-ONLY (DO NOT INSTALL ON SERVER!)

These mods go in the client modpack only, not on the server:
- Rubidium / Embeddium (renderer)
- Oculus (shaders)
- JourneyMap (client map)
- Xaero's Minimap / World Map
- Iris (if using Modrinth instead of CurseForge)
- Entity Culling

---

## INSTALLATION

```bash
# 1. Install NeoForge 1.20.1 server:
java -jar neoforge-1.20.1-installer.jar --installServer

# 2. Set eula=true in eula.txt

# 3. Place all server-side mods in /mods/

# 4. Start the server:
./run.sh  (or start.sh)

# 5. Check logs/latest.log for errors
# 6. Check mod dependencies if a mod crashes
```

**Important:** Open port 24454 (UDP) in your firewall for Simple Voice Chat!
