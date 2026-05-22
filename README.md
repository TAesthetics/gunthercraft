# Gunthercraft Server Files

Komplette Server-Konfigurationen für beide Gunthercraft-Server.

## Struktur

```
crossplay/          ← Java + Bedrock | 8 GB RAM | Paper 1.21.x + GeyserMC
modded/             ← Java Only       | 16 GB RAM | NeoForge 1.20.1
```

---

## Crossplay Server (8 GB RAM)

**Software:** Paper 1.21.x + GeyserMC + Floodgate  
**Spieler:** 60–80 | Java Port: 25565 | Bedrock Port: 19132 (UDP)

```
crossplay/
├── start.sh / start.bat          Startskripte mit Aikar's JVM-Flags
├── server.properties             Serverkonfiguration
├── eula.txt                      EULA (accepted)
├── bukkit.yml                    Spawn-Limits, Autosave
├── spigot.yml                    Performance-Tweaks
├── paper-global.yml              Paper-spezifische Globals
├── paper-world-defaults.yml      Anti-XRay, Mob-Spawning etc.
└── plugins/
    ├── PLUGINS-DOWNLOAD.txt      Alle Download-Links
    ├── Geyser-Spigot/config.yml  Bedrock-Bridge Konfiguration
    ├── floodgate/config.yml      Bedrock-Auth (kein Java-Account nötig)
    ├── EssentialsX/config.yml    Homes, Warps, Economy
    ├── DiscordSRV/config.yml     Discord ↔ Minecraft Chat (Token eintragen!)
    ├── LuckPerms/groups.yml      Gruppen-Setup Befehle
    ├── WorldGuard/config.yml     Weltschutz-Flags
    ├── CoreProtect/config.yml    Anti-Grief Logging
    ├── ChunkyBorder/config.yml   Weltgrenzen + Pregeneration
    └── BlueMap/                  3D-Weltkarte (Port 8100)
```

**Ports öffnen:** `25565 TCP` (Java) + `19132 UDP` (Bedrock)

---

## Modded Server (16 GB RAM)

**Software:** NeoForge 1.20.1  
**Spieler:** 50–60 | Java Port: 25566

```
modded/
├── start.sh / start.bat          Startskripte
├── user_jvm_args.txt             JVM-Flags (von run.sh eingelesen)
├── server.properties             Serverkonfiguration
├── eula.txt                      EULA (accepted)
├── mods/
│   └── MODS-SERVER.md            Komplette Mod-Liste mit Download-Links
└── config/
    ├── voicechat/                Simple Voice Chat (Port 24454 UDP!)
    ├── ftbteams/                 Team-System
    ├── ftbchunks/                Chunk-Claims & Schutz
    └── create/                   Create Mod Server-Settings
```

**Ports öffnen:** `25566 TCP` (Java) + `24454 UDP` (Voice Chat)

---

## Quick Start

### Crossplay
1. Paper herunterladen: https://papermc.io/downloads
2. `crossplay/` als Server-Verzeichnis nutzen
3. `chmod +x start.sh && ./start.sh` (stoppt wegen EULA — schon accepted)
4. Plugins aus `PLUGINS-DOWNLOAD.txt` in `plugins/` legen
5. Geyser/Floodgate zuerst installieren, dann Server starten

### Modded
1. NeoForge 1.20.1 Installer herunterladen: https://neoforged.net/
2. `java -jar neoforge-installer.jar --installServer` im `modded/`-Ordner
3. Mods aus `MODS-SERVER.md` in `mods/` legen
4. `./run.sh` (NeoForge generiert run.sh automatisch)
