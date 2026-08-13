# Keybinds Service

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `StarterGuiAssets/Scripts/ClientHandler/Services/KeybindsService.luau`
- Kind: Service
- Runtime: Client
- Module path: `StarterGuiAssets/Scripts/ClientHandler/Services/KeybindsService`

## Overview

This service is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: (Made for MAS Framework — Public Standard Ver: 2.0.0+)

## Purpose

- Provide the `Keybinds Service` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Services/KeybindsService.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Services/KeybindsService.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================

Note: Our old official Roblox group was compromised. 
This project is our trademark framework and is not affiliated with any Roblox group.

────────────────────────────────────────────────────
📦 KeybindsService — Version 0.5.0 (Client) (Service — Foundational)
(Made for MAS Framework — Public Standard Ver: 2.0.0+)
────────────────────────────────────────────────────

Input & Keybinding Manager

🌟 Purpose:
KeybindsService centralizes all client-side input bindings into a single,
action-based system. It allows gameplay modules to react to named actions
instead of hardcoded keys, keeping input logic clean, modular, and scalable.

🎮 Features:
- Unified keyboard, mouse, and console controller support
- Start and end input state mapping for precise control
- Supports multiple actions per key
- Customizable keybind tables for easy extension

🕹️ Console ButtonA Fix:
Solves the Roblox issue where ButtonA is blocked by the default Jump action
by detecting input through Humanoid.Jump state changes, ensuring reliable
ButtonA press and release detection on consoles.

📈 Benefits:
- Cleaner gameplay code with no raw input handling per module
- Reliable cross-platform input behavior
- MAS-friendly, modular, and maintainable design
