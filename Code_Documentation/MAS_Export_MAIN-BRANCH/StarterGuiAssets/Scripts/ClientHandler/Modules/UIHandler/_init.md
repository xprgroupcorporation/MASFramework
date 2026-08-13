# Uihandler

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `StarterGuiAssets/Scripts/ClientHandler/Modules/UIHandler/_init.luau`
- Kind: Client Module
- Runtime: Client
- Module path: `StarterGuiAssets/Scripts/ClientHandler/Modules/UIHandler`

## Overview

This client module is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: (Made for MAS Framework — Public Standard Ver: 2.0.0+)

## Purpose

- Provide the `Uihandler` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Modules/UIHandler/_init.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Modules/UIHandler/_init.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================

Note: Our old official Roblox group was compromised. 
This project is our trademark framework and is not affiliated with any Roblox group.

────────────────────────────────────────────────────
📦 UIHandler — Version 0.5.1 (Client) (Module — Foundational)
(Made for MAS Framework — Public Standard Ver: 2.0.0+)
────────────────────────────────────────────────────

Overview:
The UIHandler is a core system that manages and refreshes client-side UI modules
in a unified, automated way. It mirrors the MAS Client Framework’s module handling
structure and supports the "ReloadReset" tag for dynamic UI reloads.
Purpose:
1) Simplifies UI module management by automatically replacing and reinitializing
tagged modules when reloaded.
2) Ensures clean and consistent UI state after player respawns, screen transitions,
or interface rebuilds.
3) Acts as the foundation for scalable UI systems that follow the same initialization
lifecycle as other MAS framework modules.

Behavior:
- Any ModuleScript under Active with the tag "ReloadReset" will be removed and
replaced with a fresh clone from the Utility folder.
- All active UI modules are then required and initialized again automatically.
- Supports Init() lifecycle methods for UI modules.

⚙️ Integration:

Always keep UIHandler within your client structure.

Attach the "ReloadReset" tag to any UI module that should reset when the player
respawns or when a full UI refresh occurs.
