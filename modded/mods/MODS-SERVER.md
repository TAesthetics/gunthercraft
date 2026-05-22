# Gunthercraft Modpack - Server-Mods Liste
# NeoForge 1.20.1
# ==========================================
# NUR Server-kompatible Mods hier.
# Client-Only-Mods (Rubidium, Oculus, JourneyMap-Client) NICHT auf dem Server installieren!

## PFLICHT - Loader & Dependencies

| Mod | Download | Hinweis |
|-----|----------|---------|
| NeoForge 1.20.1 | https://neoforged.net/ | Server-Installer herunterladen |
| Kotlin for Forge | https://www.curseforge.com/minecraft/mc-mods/kotlin-for-forge | Dependency für viele Mods |
| Architectury API | https://www.curseforge.com/minecraft/mc-mods/architectury-api | Dependency |
| Forge Config API Port | https://www.curseforge.com/minecraft/mc-mods/forge-config-api-port | Dependency |

---

## KRIEGSFÜHRUNG & MILITÄR
*(Requested: Cataclysm, CyberEnigma0, Smocka Republika, Jame Key Lie)*

| Mod | Download | Server-seitig? |
|-----|----------|----------------|
| Timeless & Classics Zero (TCZ) | https://www.curseforge.com/minecraft/mc-mods/timeless-and-classics-zero | JA - Pflicht |
| Superb Warfare | https://www.curseforge.com/minecraft/mc-mods/superb-warfare | JA - Pflicht |
| Create Big Cannons (CBC) | https://www.curseforge.com/minecraft/mc-mods/create-big-cannons | JA - Pflicht |
| Immersive Vehicles | https://www.curseforge.com/minecraft/mc-mods/mrcrayfish-vehicle-mod | JA - Pflicht |

---

## CREATE & TECHNIK
*(Requested: earlynyancat)*

| Mod | Download | Server-seitig? |
|-----|----------|----------------|
| Create (NeoForge) | https://www.curseforge.com/minecraft/mc-mods/create | JA - Pflicht |
| Create: Steam 'n' Rails | https://www.curseforge.com/minecraft/mc-mods/create-steam-n-rails | JA - Pflicht |
| Create Crafts & Additions | https://www.curseforge.com/minecraft/mc-mods/createaddition | JA - Pflicht |

**Create Dependencies (automatisch installiert via CurseForge App, manuell herunterladen):**
- Flywheel (Create-Rendering-Lib)

---

## WELT & KARTEN
*(Requested: david)*

| Mod | Download | Server-seitig? |
|-----|----------|----------------|
| Terra (Earth Map Generator) | https://www.curseforge.com/minecraft/mc-mods/terra | JA - Worldgen |
| Xaero's Minimap | https://www.curseforge.com/minecraft/mc-mods/xaeros-minimap | Client-only (kein Server-install nötig) |
| Xaero's World Map | https://www.curseforge.com/minecraft/mc-mods/xaeros-world-map | Client-only |

**Terra-Setup:**
Nach Installation Terra-Config auf Earth-Map einstellen:
`config/terra/packs/` -> EarthMC-Pack oder custom Terra-Pack platzieren.

---

## HORROR & ATMOSPHÄRE
*(Requested: Jame Key Lie)*

| Mod | Download | Server-seitig? |
|-----|----------|----------------|
| The Midnight | https://www.curseforge.com/minecraft/mc-mods/the-midnight | JA - Pflicht |
| Cave Dweller Reimagined | https://www.curseforge.com/minecraft/mc-mods/cave-dweller-reimagined | JA - Pflicht |
| From The Fog (Herobrine) | https://www.curseforge.com/minecraft/mc-mods/from-the-fog | JA - Pflicht |

---

## CYBERPUNK & ROLEPLAY
*(Requested: CyberEnigma0)*

| Mod | Download | Server-seitig? |
|-----|----------|----------------|
| MrCrayfish's Furniture Mod | https://www.curseforge.com/minecraft/mc-mods/mrcrayfish-furniture-mod | JA - Pflicht |
| Simple Voice Chat | https://www.curseforge.com/minecraft/mc-mods/simple-voice-chat | JA - Pflicht (Server + Client!) |
| Supplementaries | https://www.curseforge.com/minecraft/mc-mods/supplementaries | JA - Pflicht |

**Simple Voice Chat Port:**
Port 24454 (UDP) in der Firewall öffnen!
Config: `config/voicechat/voicechat-server.properties`

---

## SONSTIGE COMMUNITY-REQUESTS

| Mod | Download | Server-seitig? |
|-----|----------|----------------|
| Spore Mod (Cataclysm) | Nicht verfügbar für NeoForge 1.20.1, Alternativ: Alex's Mobs https://www.curseforge.com/minecraft/mc-mods/alexs-mobs | JA |

---

## PERFORMANCE (SERVER-SIDE)

| Mod | Download | Hinweis |
|-----|----------|---------|
| FerriteCore | https://www.curseforge.com/minecraft/mc-mods/ferritecore | RAM-Optimierung |
| Clumps | https://www.curseforge.com/minecraft/mc-mods/clumps | XP-Orb-Merge |
| ModernFix | https://www.curseforge.com/minecraft/mc-mods/modernfix | Startup & RAM |
| Radium (Server-Sodium-Port) | https://www.curseforge.com/minecraft/mc-mods/radium-reforged | Server-Performance |

---

## SCHUTZ & TEAMS

| Mod | Download | Server-seitig? |
|-----|----------|----------------|
| FTB Teams | https://www.curseforge.com/minecraft/mc-mods/ftb-teams | JA - Pflicht |
| FTB Chunks | https://www.curseforge.com/minecraft/mc-mods/ftb-chunks | JA - Pflicht |
| FTB Library | https://www.curseforge.com/minecraft/mc-mods/ftb-library | JA - Dependency für FTB |

---

## ESSENTIALS (SERVER-SIDE)

| Mod | Download | Hinweis |
|-----|----------|---------|
| JEI (Just Enough Items) | https://www.curseforge.com/minecraft/mc-mods/jei | Läuft auch Server-side für Rezepte |
| Crafting Tweaks | https://www.curseforge.com/minecraft/mc-mods/crafting-tweaks | Optional |

---

## CLIENT-ONLY (NICHT AUF SERVER INSTALLIEREN!)

Diese Mods nur im Client-Modpack, nicht im Server:
- Rubidium / Embeddium (Renderer)
- Oculus (Shader)
- JourneyMap (Client-Map)
- Xaero's Minimap / World Map
- Iris (falls Modrinth statt CurseForge)
- Entity Culling

---

## INSTALLATION

```bash
# 1. NeoForge 1.20.1 Server installieren:
java -jar neoforge-1.20.1-installer.jar --installServer

# 2. eula.txt: eula=true setzen

# 3. Alle Server-Mods in /mods/ legen

# 4. Server starten:
./run.sh  (oder start.sh)

# 5. Auf Fehler in logs/latest.log prüfen
# 6. Dependencies prüfen wenn ein Mod crasht
```

**Wichtig:** Simple Voice Chat Port 24454 (UDP) in Firewall öffnen!
