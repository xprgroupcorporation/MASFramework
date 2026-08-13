# Animate

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `StarterGuiAssets/Scripts/ClientHandler/Modules/Animate.luau`
- Kind: Client Module
- Runtime: Client
- Module path: `StarterGuiAssets/Scripts/ClientHandler/Modules/Animate`

## Overview

This client module is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: (Made for MAS Framework — Public Standard Ver: 2.0.0+)

## Purpose

- Provide the `Animate` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Modules/Animate.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Modules/Animate.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================

Note: Our old official Roblox group was compromised. 
This project is our trademark framework and is not affiliated with any Roblox group.

────────────────────────────────────────────────────
📦 Animate — Version 0.1.7 (Client) (Module — Foundational)
(Made for MAS Framework — Public Standard Ver: 2.0.0+)
────────────────────────────────────────────────────

📌 Description:
This module is a clean, simplified, and optimized replacement for Roblox’s default
`Animate` script. It rewrites the entire animation logic into a modern, readable,
and lightweight system that is easier to edit, customize, and debug.

Roblox’s original Animate script is:
- difficult to read  
- over-engineered  
- tightly coupled to legacy systems  
- slow to modify  
- filled with unnecessary branching  

This XPR Studio version is built to be:
- Simple — Clean state-driven animation flow
- Editable — Easy to customize animation IDs or behavior
- Lightweight — No CoreScript clutter or spaghetti logic
- Understandable — Every line is clear and predictable
- Functional — Includes all essential movement states

🎮 Included Movement States
- Idle
- Walking
- Running
- Jumping
- Falling (with jump-timer grace)
- Swimming + SwimIdle
- Sitting
- Climbing
- PlatformStand (stops all animations cleanly)

🛠 Included Systems
- Tool animations (toolanim system)
- Emotes (wave, dance, point, cheer, laugh)
- Chat emote triggers (/e, /emote)
- Smooth animation transitions (fade-in/out)
- Adjustable speed scaling
- Proper priority handling
- State-based animation blocking (Sit, Swim, PlatformStand)
- Anchored HumanoidRootPart will stop moving animations and play idle

✨ What Makes It Better
All complexity and hidden behavior from the default Roblox Animate script have
been removed. This module uses straightforward Lua and clean state checks,
making it perfect for real game development where reliability matters.

Built for developers who want:
✔ predictable behavior  
✔ clean code  
✔ easy debugging  
✔ safe customization
✔ fully customizable animations  
✔ professional animation quality  

At only a fraction of the complexity of the original Animate script.
