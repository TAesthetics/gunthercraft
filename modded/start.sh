#!/usr/bin/env bash
# Gunthercraft Modded Server - Start Script
# NeoForge 1.20.1 | 16GB RAM
# ==========================================
# NeoForge generiert nach Installation automatisch run.sh.
# Wenn run.sh existiert -> DIESE hier nicht benutzen, stattdessen run.sh.
# user_jvm_args.txt wird von run.sh automatisch eingelesen.
#
# Manueller Start (falls run.sh fehlt):

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

# Alternativ wenn NeoForge run.sh vorhanden:
# ./run.sh
