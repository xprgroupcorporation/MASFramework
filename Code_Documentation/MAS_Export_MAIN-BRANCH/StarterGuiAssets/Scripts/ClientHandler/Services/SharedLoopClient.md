# Shared Loop Client

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `StarterGuiAssets/Scripts/ClientHandler/Services/SharedLoopClient.luau`
- Kind: Service
- Runtime: Client
- Module path: `StarterGuiAssets/Scripts/ClientHandler/Services/SharedLoopClient`

## Overview

This service is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: (Made for MAS Framework — Public Standard Ver: 2.0.0+)

## Purpose

- Provide the `Shared Loop Client` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Services/SharedLoopClient.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Services/SharedLoopClient.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================

Note: Our old official Roblox group was compromised. 
This project is our trademark framework and is not affiliated with any Roblox group.

────────────────────────────────────────────────────
📦 SharedLoopModule — Version 0.1.4 (Client) (Service — Foundational)
(Made for MAS Framework — Public Standard Ver: 2.0.0+)
────────────────────────────────────────────────────

For efficiently running multi loop tasks for the Client side.

Note: This feature is necessary for MAS framework and it's add-ons.
Note2: This also can be used independently without MAS Framework 

🔁 How It Works:
- Shares a single "RenderStepped / Heartbeat connection" on the Client, 
rather than creating multiple "RunService" loops.
- Shares a single "while wait(1)" loop" on the Client, 
rather than allowing every script to spin its own loop.
- Scripts that require this module register their callbacks to the shared loop, 
keeping performance optimized.
Note: When insert a functions, we recomended to add string os.clock() along with function name to mark it,
and make it easier to clean up

🔧 Supported 3 Shared Loop:
- RenderStepped
- Heartbeat (Minimun of 20 per frame)
- while wait(1)
Note: Just read the module to understand it. How it work? Functions?

🎯 Purpose:
✅ Prevents the creation of "redundant or duplicate loops" across multiple systems.
✅ "Reduces CPU/memory cost" by centralizing time-based logic.
✅ Scales better across large projects with many systems requiring consistent updates.
✅ Maintains predictable tick behavior for game systems (such as cooldowns, UI updates, status checks, etc.)

📈 Benefits:
- ✨ Dramatically improves performance and responsiveness.
- 🔧 Easier debugging and profiling, track loop behavior from one place.
- 🧩 Cleaner architecture: central management for update logic.
- 🕹️ Client-side UI and visual systems update in sync with RenderStepped.
- 🔒 Client-side loop ticks are consistent and minimize scheduling issues.

⚠️ Limitations / Considerations:
- ❌ Shared timing means you "cannot control independent intervals" in decimal per module (e.g., per 0.5s, but 2s is possible).
- 🧠 Developers must think in terms of "shared update frequency", which may limit ultra-granular control.
- 🚫 May introduce dependency issues if modules require different timing tolerances or are not optimized for shared loops.
- 🔄 Requires manual unsubscribe/removal logic for temporary or destroyed modules to avoid memory leaks.

Recommended for experienced developers building "modular" or "component-based systems" 
who want performance consistency across modules.
