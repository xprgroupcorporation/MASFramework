# Data Store

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `ServerScriptServiceAssets/ServerHandler/Modules/DataStore/_init.luau`
- Kind: Server Module
- Runtime: Server
- Module path: `ServerScriptServiceAssets/ServerHandler/Modules/DataStore`

## Overview

This server module is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: (Made for MAS Framework — Public Standard Ver: 2.0.0+)

## Purpose

- Provide the `Data Store` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/ServerScriptServiceAssets/ServerHandler/Modules/DataStore/_init.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/ServerScriptServiceAssets/ServerHandler/Modules/DataStore/_init.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================

Note: Our old official Roblox group was compromised. 
This project is our trademark framework and is not affiliated with any Roblox group.

────────────────────────────────────────────────────
📦 DataStore — Version 1.2.0 (Server) (Module — Foundational)
(Made for MAS Framework — Public Standard Ver: 2.0.0+)
────────────────────────────────────────────────────

────────────────────────────────────────────────────
🌟 Overview & Purpose
────────────────────────────────────────────────────
DataStore is the centralized server-authoritative persistence system
for MAS Framework. It manages player data loading, validation,
normalization, runtime access, and saving through a single controlled
pipeline.

The module supports both object-based and table-based saves, save slots,
global data, and live schema evolution without breaking existing data.

────────────────────────────────────────────────────
🧩 Problems This Module Solves
────────────────────────────────────────────────────
• Eliminates scattered DataStoreService usage
• Prevents corrupted or partial player saves
• Handles backward compatibility automatically
• Avoids type mismatch and missing-key errors
• Centralizes save-slot and cross-save logic
• Reduces complexity when updating data schemas

────────────────────────────────────────────────────
🔗 Data Ownership & Access Model
────────────────────────────────────────────────────
• Server-authoritative only
• Clients never write persistent data directly
• Runtime access via ProfileLibraryService
• External access gated through ServerAPI
• Player lifecycle bound to PlayerAdded / PlayerRemoving

────────────────────────────────────────────────────
📦 Save Architecture
────────────────────────────────────────────────────
• SaveSlot system for multiple progress states
• SlotSave: progression tied to a specific slot
• CrossSave: account-wide shared progression
• GlobalData: server-wide persistent state
• Prefix-based key system for expansion and versioning

────────────────────────────────────────────────────
🧠 Template, Normalization & Validation
────────────────────────────────────────────────────
• Deep template normalization on load
• Automatic restoration of missing keys
• Recursive type validation
• Invalid or mismatched data reset safely
• Extra keys filtered out before saving
• Backward-compatible by design

────────────────────────────────────────────────────
🧱 Middleware & Custom Behavior
────────────────────────────────────────────────────
• Middleware hooks for load, insert, and removal
• CustomBehavior modules inject dynamic data
• Supports live progression updates (levels, stats)
• Extend save logic without editing core module

────────────────────────────────────────────────────
🔄 ServerAPI Integration
────────────────────────────────────────────────────
• Uses GetOrCreateRemote pattern
• Controlled RemoteEvent / RemoteFunction exposure
• Global data edit, fetch, and save endpoints
• Prevents uncontrolled remote usage

────────────────────────────────────────────────────
🛡️ Security & Safety
────────────────────────────────────────────────────
• No client-side persistence authority
• No blind overwrites of stored data
• Save operations filtered to known schemas
• Attribute-based load/save state locking
• Safe retries on data load failures

────────────────────────────────────────────────────
🎯 Typical Use Cases
────────────────────────────────────────────────────
• RPG and progression-driven games
• Multi-slot character systems
• Persistent inventories and stats
• Live-service games with frequent updates
• Projects requiring long-term data stability
• Global data saving (ex: all player shared value)

────────────────────────────────────────────────────
✅ MAS Framework Best Practices
────────────────────────────────────────────────────
• Never call DataStoreService directly
• Treat templates as the single source of truth
• Use middleware for expansion and migration
• Access player data only via ProfileLibraryService
• Let DataStore handle validation and version safety
────────────────────────────────────────────────────
