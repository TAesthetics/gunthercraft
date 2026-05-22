# Gunthercraft Server Files

Complete server configurations for both Gunthercraft servers.

## Structure

```
crossplay/          ← Java + Bedrock | 8 GB RAM | Paper 1.21.x + GeyserMC
modded/             ← Java Only       | 16 GB RAM | NeoForge 1.20.1
```

---

## Crossplay Server (8 GB RAM)

**Software:** Paper 1.21.x + GeyserMC + Floodgate  
**Players:** 60–80 | Java Port: 25565 | Bedrock Port: 19132 (UDP)

```
crossplay/
├── start.sh / start.bat          Start scripts with Aikar's JVM flags
├── server.properties             Server configuration
├── eula.txt                      EULA (accepted)
├── bukkit.yml                    Spawn limits, autosave
├── spigot.yml                    Performance tweaks
├── paper-global.yml              Paper-specific globals
├── paper-world-defaults.yml      Anti-XRay, mob spawning, etc.
└── plugins/
    ├── PLUGINS-DOWNLOAD.txt      All plugin download links
    ├── Geyser-Spigot/config.yml  Bedrock bridge configuration
    ├── floodgate/config.yml      Bedrock auth (no Java account needed)
    ├── EssentialsX/config.yml    Homes, warps, economy
    ├── DiscordSRV/config.yml     Discord ↔ Minecraft chat (add bot token!)
    ├── LuckPerms/groups.yml      Group setup commands
    ├── WorldGuard/config.yml     World protection flags
    ├── CoreProtect/config.yml    Anti-grief logging
    ├── ChunkyBorder/config.yml   World borders + pre-generation
    └── BlueMap/                  3D world map (port 8100)
```

**Open ports:** `25565 TCP` (Java) + `19132 UDP` (Bedrock)

---

## Modded Server (16 GB RAM)

**Software:** NeoForge 1.20.1  
**Players:** 50–60 | Java Port: 25566

```
modded/
├── start.sh / start.bat          Start scripts
├── user_jvm_args.txt             JVM flags (read by run.sh automatically)
├── server.properties             Server configuration
├── eula.txt                      EULA (accepted)
├── mods/
│   └── MODS-SERVER.md            Full mod list with download links
└── config/
    ├── voicechat/                Simple Voice Chat (port 24454 UDP!)
    ├── ftbteams/                 Team system
    ├── ftbchunks/                Chunk claims & protection
    └── create/                   Create mod server settings
```

**Open ports:** `25566 TCP` (Java) + `24454 UDP` (Voice Chat)

---

## Quick Start

### Crossplay
1. Download Paper: https://papermc.io/downloads
2. Use `crossplay/` as the server directory
3. `chmod +x start.sh && ./start.sh` (stops for EULA — already accepted)
4. Place plugins from `PLUGINS-DOWNLOAD.txt` into `plugins/`
5. Install Floodgate first, then Geyser, then start the server

### Modded
1. Download the NeoForge 1.20.1 installer: https://neoforged.net/
2. Run `java -jar neoforge-installer.jar --installServer` inside `modded/`
3. Place server-side mods from `MODS-SERVER.md` into `mods/`
4. Run `./run.sh` (NeoForge generates run.sh automatically)
