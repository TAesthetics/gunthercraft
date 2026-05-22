#!/usr/bin/env bash
# Gunthercraft Modded Server - Start Script
# NeoForge 1.20.1 | 16GB RAM
# ==========================================
# NeoForge generates run.sh automatically after installation.
# If run.sh exists -> use that instead; it reads user_jvm_args.txt automatically.
#
# Manual start (if run.sh is missing):

java \
  -Xms16G \
  -Xmx16G \
  -XX:+UseG1GC \
  -XX:+ParallelRefProcEnabled \
  -XX:MaxGCPauseMillis=200 \
  -XX:+UnlockExperimentalVMOptions \
  -XX:+DisableExplicitGC \
  -XX:+AlwaysPreTouch \
  -XX:G1NewSizePercent=30 \
  -XX:G1MaxNewSizePercent=40 \
  -XX:G1HeapRegionSize=16M \
  -XX:G1ReservePercent=20 \
  -XX:G1HeapWastePercent=5 \
  -XX:G1MixedGCCountTarget=4 \
  -XX:InitiatingHeapOccupancyPercent=15 \
  -XX:G1MixedGCLiveThresholdPercent=90 \
  -XX:G1RSetUpdatingPauseTimePercent=5 \
  -XX:SurvivorRatio=32 \
  -XX:+PerfDisableSharedMem \
  -XX:MaxTenuringThreshold=1 \
  -XX:MetaspaceSize=512M \
  -XX:MaxMetaspaceSize=512M \
  -Dusing.aikars.flags=https://mcflags.emc.gs \
  -Daikars.new.flags=true \
  @libraries/net/neoforged/neoforge/*/unix_args.txt \
  nogui

# If NeoForge run.sh is present, use this instead:
# ./run.sh
