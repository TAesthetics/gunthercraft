# Gunthercraft

Server plan for the Gunthercraft Minecraft community — two parallel servers for 50+ players.

## Pages

- **`index.html`** — Landing page with both server options
- **`crossplay.html`** — Crossplay server plan (Java + Bedrock via GeyserMC + Floodgate, plugin-based)
- **`modpack.html`** — Modpack server plan (Java only, NeoForge with the full community modpack)

## Concept

Bedrock players can't connect to Forge/NeoForge modded servers. So Gunthercraft runs two servers in parallel:

1. **Crossplay Server** — Paper + GeyserMC + Floodgate, near-vanilla with plugins, Earth Map, accessible to everyone
2. **Modpack Server** — NeoForge 1.20.1, full community-built modpack (warfare, Create, horror, cyberpunk, RP)

## Local Preview

Open `index.html` directly in a browser, or serve the folder with any static HTTP server:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.
