# Spawn Effect

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `ServerScriptServiceAssets/ServerHandler/Services/GlobalCharacterControl/Custom/OnSpawnOrDeath/SpawnEffect.luau`
- Kind: Service
- Runtime: Server
- Module path: `ServerScriptServiceAssets/ServerHandler/Services/GlobalCharacterControl/Custom/OnSpawnOrDeath/SpawnEffect`

## Overview

This service is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`.

## Purpose

- Provide the `Spawn Effect` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/ServerScriptServiceAssets/ServerHandler/Services/GlobalCharacterControl/Custom/OnSpawnOrDeath/SpawnEffect.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/ServerScriptServiceAssets/ServerHandler/Services/GlobalCharacterControl/Custom/OnSpawnOrDeath/SpawnEffect.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================

────────────────────────────────────────────────────
📦 GlobalCharacterControl / Custom / OnSpawnOrDeath / SpawnEffect
────────────────────────────────────────────────────

Handles the spawn immortality + particle effect.
Moved here from Core/LifeHandler so devs can fully customize
or replace the spawn effect without touching core systems.

Customize freely — swap out the VFX path, change timing,
add sounds, screen effects, etc.
