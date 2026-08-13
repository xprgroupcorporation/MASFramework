# Realistic First Person

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `StarterGuiAssets/Scripts/ClientHandler/Modules/RealisticFirstPerson.luau`
- Kind: Client Module
- Runtime: Client
- Module path: `StarterGuiAssets/Scripts/ClientHandler/Modules/RealisticFirstPerson`

## Overview

This client module is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: (Made for MAS Framework — Public Standard Ver: 2.0.0+)

## Purpose

- Provide the `Realistic First Person` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Modules/RealisticFirstPerson.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Modules/RealisticFirstPerson.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================

Note: Our old official Roblox group was compromised. 
This project is our trademark framework and is not affiliated with any Roblox group.

────────────────────────────────────────────────────
📦 RealisticFirstPerson — Version 0.5.5 (Client) (Module — Add-On)
(Made for MAS Framework — Public Standard Ver: 2.0.0+)
────────────────────────────────────────────────────

🧩 Description:
This module is designed to simulate a realistic first-person experience in Roblox by dynamically adjusting 
the LocalTransparencyModifier of the player's character parts, accessories, and VFXs. It selectively 
makes parts and VFX visible when in first-person view and avoid obstructing the player's vision.

It supports:
✅ Automatic handling of arms, accessories, folders, models, trails, emitters etc.
✅ Character respawn support via ChildAdded listeners
✅ Head accessory detection via AccessoryType (works on any rig, regardless of
   custom attachment naming — fixes hair/hats/face staying visible in 1st person
   on rigs whose attachment names don't match Roblox's 4 hardcoded defaults)

This module does not manage camera behavior or mouse input. Those should be handled by other parts 
of the MAS Framework
