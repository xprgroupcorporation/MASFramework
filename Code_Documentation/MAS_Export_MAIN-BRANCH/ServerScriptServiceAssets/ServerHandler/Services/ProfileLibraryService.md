# Profile Library Service

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `ServerScriptServiceAssets/ServerHandler/Services/ProfileLibraryService.luau`
- Kind: Service
- Runtime: Server
- Module path: `ServerScriptServiceAssets/ServerHandler/Services/ProfileLibraryService`

## Overview

This service is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: (Made for MAS Framework — Public Standard Ver: 2.0.0+)

## Purpose

- Provide the `Profile Library Service` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/ServerScriptServiceAssets/ServerHandler/Services/ProfileLibraryService.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/ServerScriptServiceAssets/ServerHandler/Services/ProfileLibraryService.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================

Note: Our old official Roblox group was compromised. 
This project is our trademark framework and is not affiliated with any Roblox group.

────────────────────────────────────────────────────
📦 ProfileLibraryService — Version 0.4.9 (Server) (Service — Foundational)
(Made for MAS Framework — Public Standard Ver: 2.0.0+)
────────────────────────────────────────────────────

🌟 Description:
This service handles per-player data profiles for use across gameplay systems. 
It uses a deep copy of a predefined data template to ensure safe and isolated instances for each player.
Optimized for performance and modularity, this service defers the data structure to an external module 
to support lightweight initialization and easy maintenance.

🧩 Features:
- DeepClone-based safe template duplication (no use of "table.clone")
- Per-user profile storage using "UserId" as the key
- Automatic data creation on join and cleanup on leave
- Shared variable injection via ":Init()"
- Template is externally manageable (for optimization)

⚠️ Note:
Ensure "TemplateData" is populated externally before runtime for proper behavior.
