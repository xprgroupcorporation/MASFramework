# Respawn System

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `ServerScriptServiceAssets/ServerHandler/Services/GlobalCharacterControl/Core/RespawnSystem.luau`
- Kind: Service
- Runtime: Server
- Module path: `ServerScriptServiceAssets/ServerHandler/Services/GlobalCharacterControl/Core/RespawnSystem`

## Overview

This service is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: (Made for MAS Framework — Public Standard Ver: 2.0.0+)

## Purpose

- Provide the `Respawn System` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/ServerScriptServiceAssets/ServerHandler/Services/GlobalCharacterControl/Core/RespawnSystem.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/ServerScriptServiceAssets/ServerHandler/Services/GlobalCharacterControl/Core/RespawnSystem.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================

────────────────────────────────────────────────────
📦 GlobalCharacterControl / Core / RespawnSystem
(Made for MAS Framework — Public Standard Ver: 2.0.0+)
────────────────────────────────────────────────────

Owns the respawn queue: who is waiting, how long they have left, and
whether they're allowed to spawn right now. Built so round/match-based
games can hold players in queue until the round actually starts,
instead of always respawning after a fixed delay.

RepStorage.GlobalCharacterControl.RespawnQueue/
  [PlayerName] (IntValue)        — seconds remaining (counts down to 0)
    Attribute: UserId    (number) — player's UserId
    Attribute: QueuedAt  (number) — os.clock() when they entered the queue
    Attribute: RespawnAt (number) — os.clock() timestamp they're due to respawn at

The countdown is ticked by LoopServer (SharedLoop) — once per second,
once per queued entry. When an entry hits 0 AND CanSpawn is true (both
globally and for that player), they are spawned and removed from queue.
If CanSpawn is false, the entry holds at 0 until it's allowed through —
this is what makes round/match gating possible.

Swap this whole module out if you need different respawn rules (e.g.
lives-based elimination, wave-based spawning, etc.) — nothing outside
Core/ depends on its internals, only on the functions exposed below.
