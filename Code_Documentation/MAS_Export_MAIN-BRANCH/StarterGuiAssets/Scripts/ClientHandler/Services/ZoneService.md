# Zone Service

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `StarterGuiAssets/Scripts/ClientHandler/Services/ZoneService.luau`
- Kind: Service
- Runtime: Client
- Module path: `StarterGuiAssets/Scripts/ClientHandler/Services/ZoneService`

## Overview

This service is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: (Made for MAS Framework — Public Standard Ver: 2.0.0+)

## Purpose

- Provide the `Zone Service` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Services/ZoneService.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Services/ZoneService.md`

## Source Comment

============================
|                    XPR Studio™
|    Exotic • Passionate • Revolutionize
|     ©2025-2026 All Rights Reserved.
============================

Note: Our old official Roblox group was compromised.
This project is our trademark framework and is not affiliated with any Roblox group.

────────────────────────────────────────────────────
📦 ZoneService — Version 1.1.0 (Client) (Service — Foundational)
(Made for MAS Framework — Public Standard Ver: 2.0.0+)
────────────────────────────────────────────────────

ZoneService provides a centralized zone detection system
for client-side gameplay.

Instead of every module creating its own loop and zone checks,
modules register folders and callbacks through this service.

Benefits:
- One shared loop for all zone systems
- Better performance
- Reusable across multiple modules
- Easy future expansion

Example Uses:
- Sound Zones
- Safe Zones
- PvP Zones
- Damage Zones
- Weather Zones
- Quest Zones
- Cutscene Trigger Zones

Supported Shapes:
- Block
- Ball

Zone Behavior:
- Enter callback fires once when entering.
- Leave callback fires once when leaving.
- Supports moving directly between zones.
