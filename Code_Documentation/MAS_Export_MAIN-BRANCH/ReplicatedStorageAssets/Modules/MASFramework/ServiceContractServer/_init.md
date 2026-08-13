# Service Contract Server

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `ReplicatedStorageAssets/Modules/MASFramework/ServiceContractServer/_init.luau`
- Kind: Server Module
- Runtime: Server
- Module path: `ReplicatedStorageAssets/Modules/MASFramework/ServiceContractServer`

## Overview

This server module is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: 📦 MAS Framework – Public Standard Ver: 2.0.0+ (Server)

## Purpose

- Provide the `Service Contract Server` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/ReplicatedStorageAssets/Modules/MASFramework/ServiceContractServer/_init.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/ReplicatedStorageAssets/Modules/MASFramework/ServiceContractServer/_init.md`

## Source Comment

============================
|  XPR Studio™  
|  Exotic • Passionate • Revolutionize 
| ©2025-2026 All Rights Reserved.  
============================
Note: Our old official Roblox group was compromised. 
This framework is an official XPR Studio project release and is not affiliated with any Roblox group.

📦 MAS Framework – Public Standard Ver: 2.0.0+ (Server)

Purpose:
This module defines the official static service interfaces provided by the MAS Framework.
It exists solely to support editor autocomplete, type checking, and static validation.
This file is not intended to be executed at runtime and must not contain runtime logic.

Scope:
- Includes only foundational services and official add-ons bundled with the framework
- Acts as the single source of truth for available server-side services
- Prevents the need to open service implementations or copy method definitions

Architecture (Modular — v2.0):
- Each service's type definition lives in Foundational/, Addon/, or Private/ folders
- This aggregator composes all contracts into a single Services type
- A runtime validator scans folders and warns if modules are not wired

Why not a for loop?
- Luau type system is static and cannot infer dynamic requires
- GetChildren() based requires return 'any', breaking autocomplete
- Static requires preserve full type inference
- Validator ensures missing wiring is still detected safely

How to Add a New Service:
1. Create ModuleScript in Foundational/, Addon/, or Private/
2. Define: export type MyService = { ... } and return nil
3. Add require() in STEP 1
4. Add type alias in STEP 2
5. Add to Services in STEP 3
6. Add to wired table in STEP 4

Validation:
- Missing modules trigger warnings automatically
- Steps 3–5 are required for type safety and autocomplete

Usage:
Use require() for type-only imports:
require(game.ReplicatedStorage.ReplicatedStorageAssets.Modules.MASFramework.ServiceContractServer)

Important:
This module is strictly for developer tooling support.
Do not depend on it for runtime behavior.
