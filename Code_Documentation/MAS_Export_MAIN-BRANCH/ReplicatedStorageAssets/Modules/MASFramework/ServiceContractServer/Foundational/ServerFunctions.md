# Server Functions

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `ReplicatedStorageAssets/Modules/MASFramework/ServiceContractServer/Foundational/ServerFunctions.luau`
- Kind: Server Module
- Runtime: Server
- Module path: `ReplicatedStorageAssets/Modules/MASFramework/ServiceContractServer/Foundational/ServerFunctions`

## Overview

This server module is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: 📦 MAS Framework – Public Standard Ver: 2.0.0+ (Server)

## Purpose

- Provide the `Server Functions` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/ReplicatedStorageAssets/Modules/MASFramework/ServiceContractServer/Foundational/ServerFunctions.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/ReplicatedStorageAssets/Modules/MASFramework/ServiceContractServer/Foundational/ServerFunctions.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================
Note: Our old official Roblox group was compromised. 
This framework is an official XPR Studio project release and is not affiliated with any Roblox group.

📦 MAS Framework – Public Standard Ver: 2.0.0+ (Server)

Purpose:
This module defines the static service interface for ServerFunctions.
It exists solely to support editor autocomplete, type checking, and static validation.
This file is not intended to be executed at runtime and must not contain runtime logic.

Usage:
Each service contract module is auto-required by ServiceContractServer.
Do not require this module directly in consumer scripts — use ServiceContractServer instead.

Important:
This module is strictly for developer tooling support.
Do not depend on it for runtime behavior.
