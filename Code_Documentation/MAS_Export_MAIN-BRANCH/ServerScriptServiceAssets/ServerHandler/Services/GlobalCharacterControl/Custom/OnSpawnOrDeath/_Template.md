# Template

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `ServerScriptServiceAssets/ServerHandler/Services/GlobalCharacterControl/Custom/OnSpawnOrDeath/_Template.luau`
- Kind: Service
- Runtime: Server
- Module path: `ServerScriptServiceAssets/ServerHandler/Services/GlobalCharacterControl/Custom/OnSpawnOrDeath/_Template`

## Overview

This service is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`.

## Purpose

- Provide the `Template` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/ServerScriptServiceAssets/ServerHandler/Services/GlobalCharacterControl/Custom/OnSpawnOrDeath/_Template.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/ServerScriptServiceAssets/ServerHandler/Services/GlobalCharacterControl/Custom/OnSpawnOrDeath/_Template.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================

────────────────────────────────────────────────────
📦 GlobalCharacterControl / Custom / OnSpawnOrDeath / Template
────────────────────────────────────────────────────

Drop a copy of this in Custom/OnSpawnOrDeath/ and rename it. GCCS will
auto-discover it and call InitSpawn on every spawn, InitDeath on every
death — no manual registration needed. Both fire regardless of the
ApplyCustomMASStatSys setting. Define either one, both, or neither
(a module with neither is just ignored with a warning).

Delete this file (or leave it, it's ignored unless you rename it) —
it's just a reference for the expected shape.
