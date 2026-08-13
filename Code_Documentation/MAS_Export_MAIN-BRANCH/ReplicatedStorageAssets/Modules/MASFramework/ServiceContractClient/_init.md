# Service Contract Client

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `ReplicatedStorageAssets/Modules/MASFramework/ServiceContractClient/_init.luau`
- Kind: Client Module
- Runtime: Client
- Module path: `ReplicatedStorageAssets/Modules/MASFramework/ServiceContractClient`

## Overview

This client module is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: 📦 MAS Framework – Public Standard Ver: 2.0.0+ (Client)

## Purpose

- Provide the `Service Contract Client` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/ReplicatedStorageAssets/Modules/MASFramework/ServiceContractClient/_init.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/ReplicatedStorageAssets/Modules/MASFramework/ServiceContractClient/_init.md`

## Source Comment

============================
|  XPR Studio™  
|  Exotic • Passionate • Revolutionize 
| ©2025-2026 All Rights Reserved.  
============================
Note: Our old official Roblox group was compromised. 
This framework is an official XPR Studio project release and is not affiliated with any Roblox group.

📦 MAS Framework – Public Standard Ver: 2.0.0+ (Client)

Purpose:
This module defines the official static service interfaces provided by the MAS Framework.
It exists solely to support editor autocomplete, type checking, and static validation.
This file is not intended to be executed at runtime and must not contain runtime logic.

Scope:
- Includes only foundational services and official add-ons bundled with the framework
- Acts as the single source of truth for available client-side services
- Prevents the need to open service implementations or copy method definitions

Architecture (Modular — v2.0):
- Each service's type definition lives in its own ModuleScript under Foundational/, Addon/, or Private/ folders
- This aggregator module requires each contract module and composes them into the final Services type
- A runtime validator auto-scans all folders and warns if any module is not wired up below
- This gives you plugin-like safety: drop a module in a folder, and if you forget to wire it, you get warned

Why not a for loop?
- Luau's type checker is STATIC — it cannot resolve types from dynamic requires in a loop
- require(child) where child comes from GetChildren() returns type 'any' — autocomplete breaks
- Static require() calls are the ONLY way to preserve full autocomplete in Luau
- The validator below catches anything you forget to wire up, giving you plugin-like safety

How to Add a New Service (Required Process)
1. Create a ModuleScript inside one of the following:
   - Foundational/ (core framework services)
   - Addon/ (optional extensions)
   - Private/ (internal or restricted systems)

2. Define the contract inside the module:
   export type MyService = { ... }
   return nil

3. Register the module in STEP 1:
   - Add a static require() in the correct folder section

4. Register the type in STEP 2:
   - Create a local type alias from the contract export

5. Expose it in STEP 3:
   - Add it to the Services export type

6. Register it in STEP 4:
   - Add it to the wired table for validation safety

Validation:
- The runtime validator will detect missing wiring
- However, Steps 3–5 are required for full type safety and autocomplete support

Usage:
Use require() to access the type definitions for annotation purposes only.
Example:
	require(game.ReplicatedStorage.ReplicatedStorageAssets.Modules.MASFramework.ServiceContractClient)

*Versioning:
Each service contract module includes a version comment indicating the supported API surface.
When a service gains new methods or behavior changes, 
its version and definitions must be updated in its own contract module accordingly.

Important:
This module is strictly for developer tooling support.
Do not depend on it for runtime behavior.
