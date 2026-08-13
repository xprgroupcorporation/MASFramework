# Data Archive

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `ServerScriptServiceAssets/ServerHandler/Services/DataArchive.luau`
- Kind: Service
- Runtime: Server
- Module path: `ServerScriptServiceAssets/ServerHandler/Services/DataArchive`

## Overview

This service is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: (Made for MAS Framework — Public Standard Ver: 2.0.0+)

## Purpose

- Provide the `Data Archive` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/ServerScriptServiceAssets/ServerHandler/Services/DataArchive.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/ServerScriptServiceAssets/ServerHandler/Services/DataArchive.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================

Note: Our old official Roblox group was compromised. 
This project is our trademark framework and is not affiliated with any Roblox group.

────────────────────────────────────────────────────
📦 DataArchive — Version 0.1.0 (Client & Server) (Service — Foundational)
(Made for MAS Framework — Public Standard Ver: 2.0.0+)
────────────────────────────────────────────────────
────────────────────────────────────────────────────
📦 Feature Overview
────────────────────────────────────────────────────
• Centralized client data container
  - Stores runtime tables that need to be accessed by multiple modules.
  - Acts as a lightweight in-memory archive for temporary gameplay data.

• Named data slots
  - Data is stored using a string key called a "needle".
  - Each needle points to a table that can contain any structured data.

• Deep table modification
  - DeepSet allows modifying nested table values without rewriting the full table.
  - Automatically creates missing sub-tables along the path.

• Fast data access
  - GetData retrieves stored tables instantly for other modules.
  - Designed for quick shared access across MAS client systems.

• Runtime debugging support
  - PrintData allows developers to inspect stored data quickly.
  - Can print either a specific archive slot or the entire archive.

• Framework integration ready
  - Designed to work with MAS Framework.
  - Enables modules to share runtime state safely without tight coupling.

────────────────────────────────────────────────────
🔁 Deployment & Compatibility
────────────────────────────────────────────────────
• Client and Server compatible
  - DataArchive is designed to run identically on both the client and the server.
  - No code modification is required for either environment.

• Copy-and-use deployment
  - The same module can be copied into client services or server services.
  - No environment flags or conditional logic are needed.

• Independent runtime storage
  - Client and server maintain their own independent DataArchive instances.
  - Data is not automatically replicated between environments.

Example usage locations:
Client: ClientHandler → Services → Client
Server: ServerHandler → Services → Server

Simply place the module in the appropriate service folder and require it normally.

────────────────────────────────────────────────────
⚠ Important Notes
────────────────────────────────────────────────────
• DataArchive does not persist data.
  - All stored data exists only during runtime.

• DataArchive does not replicate data.
  - If client and server synchronization is needed, use the MAS ClientAPI service.

• DataArchive is intended for temporary framework state management,
  not for player saving or persistent storage systems.
  
────────────────────────────────────────────────────
⚙️ Available Methods
────────────────────────────────────────────────────
• :SetData(needle, table)
  Stores a table inside the archive under the specified key.

• :DeepSet(needle, pathTable)
  Updates nested values inside a stored table using a path format.
   Example:
      DeepSet("Inventory", {"Weapons","Sword","Damage",50})

• :GetData(needle)
  Returns the stored table for the specified key.

• :PrintData(needle?)
  Prints the stored data for debugging.
  If no key is provided, the entire archive table is printed.

────────────────────────────────────────────────────
📌 Intended Use
────────────────────────────────────────────────────
• Temporary gameplay state storage
• Shared runtime variables between modules
• Structured nested data editing
• Debugging and development inspection
