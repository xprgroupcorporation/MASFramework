# Server Apiservice

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `ServerScriptServiceAssets/ServerHandler/Services/ServerAPIService.luau`
- Kind: Service
- Runtime: Server
- Module path: `ServerScriptServiceAssets/ServerHandler/Services/ServerAPIService`

## Overview

This service is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: (Made for MAS Framework — Public Standard Ver: 2.0.0+)

## Purpose

- Provide the `Server Apiservice` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/ServerScriptServiceAssets/ServerHandler/Services/ServerAPIService.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/ServerScriptServiceAssets/ServerHandler/Services/ServerAPIService.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================

Note: Our old official Roblox group was compromised. 
This project is our trademark framework and is not affiliated with any Roblox group.

────────────────────────────────────────────────────
📦 ServerAPIService — Version 2.4.0 (Server) (Service — Foundational)
(Made for MAS Framework — Public Standard Ver: 2.0.0+)
────────────────────────────────────────────────────

The ServerAPIService is a foundational utility that provides a unified interface
for server-side modules to communicate with clients, shared systems,
and other server-side modules in a safe and consistent manner.

Version 2.4.0 introduces logical listener keys, allowing multiple isolated
listeners per RemoteEvent, RemoteFunction, or Bindable without conflict.

────────────────────────────────────────────────────
Benefit
────────────────────────────────────────────────────
- Eliminates duplicated networking and event-handling code across server modules.
- Centralizes all RemoteEvent and RemoteFunction management in one place.
- Prevents naming conflicts through strict ModuleFolder namespaces.
- Supports multiple isolated listeners per remote or bindable via logical keys.
- Enforces predictable duplicate-reset behavior per logical listener key.
- Simplifies server-to-client and client-to-server communication patterns.
- Improves debugging clarity by organizing remotes and bindables consistently.
- Encourages clean separation between server logic and networking logic.
- Makes large-scale multiplayer systems easier to scale and maintain.

────────────────────────────────────────────────────
Purpose
────────────────────────────────────────────────────
- Provide standardized helper methods (Ex: :Receive, :Send, :Request)
  for server-client communication.
- Provide server-only messaging (Ex: :Bind, :FireBindable)
  via BindableEvents and BindableFunctions.
- Centralize remote creation, caching, and folder organization.
- Enforce MAS duplicate-reset rules per logical listener key.
- Allow multiple independent systems to react to the same remote safely.

────────────────────────────────────────────────────
How It Works
────────────────────────────────────────────────────
- Server modules access ServerAPIService through the Services table.
- All networking and server-side messaging logic is centralized in this service.
- RemoteEvents and RemoteFunctions are automatically created and cached.
- ModuleFolder acts as a namespace to prevent cross-module conflicts.
- Each listener is identified by a logical key.
- If no key is provided, "__default" is used automatically.
- Rebinding replaces only the listener with the same logical key.
- Different keys do not interfere with each other.

Example (Multi-Listener Support):

ServerAPI:Receive("CombatModule", "Damage", HandleCoreLogic, "Core")
ServerAPI:Receive("CombatModule", "Damage", HandleAnalytics, "Analytics")

Both listeners remain active and isolated.

────────────────────────────────────────────────────
Intended Use
────────────────────────────────────────────────────
- Any server module that needs to:
  - Send events to one or more clients
  - Receive events from clients
  - Request data or responses from clients
  - Communicate with other server-side modules
- Systems requiring multiple independent reactions to the same event.
- Prevents duplicated remote setup and scattered networking logic.
- Improves maintainability and clarity in complex server architectures.

────────────────────────────────────────────────────
Networking Layer
────────────────────────────────────────────────────
- All remotes are stored under "Variables.Remotes", grouped by ModuleFolder.
- Each ModuleFolder must contain:
    - "RE" folder for RemoteEvents
    - "RF" folder for RemoteFunctions

Available methods:

- :Send(ModuleFolder, eventName, target?, ...)
  Fires a RemoteEvent:
  - If target is nil → fires to all clients.
  - If target is a Player → fires only to that player.
  - If target is a Team → fires to all players on that team.

- :Request(ModuleFolder, functionName, targetPlayer, ...)
  Invokes a RemoteFunction on a specific client and returns the response.

- :Receive(ModuleFolder, eventName, callback, listenerKey?)
  Listens for a RemoteEvent fired from clients.
  Automatically replaces any existing listener using the same logical key.
  If listenerKey is omitted, "__default" is used.

- :ReceiveRequest(ModuleFolder, functionName, callback, listenerKey?)
  Registers a RemoteFunction handler.
  Supports multiple logical keys through internal dispatching.
  If multiple callbacks exist, the last returned value is used.
  If listenerKey is omitted, "__default" is used.

Example:

ServerAPI:Send("InventoryModule", "ItemAdded", nil, "Sword")
ServerAPI:Receive("InventoryModule", "DropItem", HandleDrop, "Core")
ServerAPI:Receive("InventoryModule", "DropItem", LogDrop, "Analytics")

────────────────────────────────────────────────────
Server-Side Bindable Messaging
────────────────────────────────────────────────────
ServerAPIService also supports server-only communication using BindableEvents
and BindableFunctions.

- Bindables are stored under "Variables.Bindables", grouped by ModuleFolder.
- All server-created bindables are automatically prefixed with "__Server_"
  for clarity and ownership visibility.
- Bindables follow the same logical-key duplicate-reset behavior.

Available methods:

- :GetOrCreateBindable(ModuleFolder, Name)
  Creates or retrieves a server-side BindableEvent or BindableFunction.

- :FireBindable(ModuleFolder, Name, ...)
  Fires a server-side BindableEvent.

- :Bind(ModuleFolder, Name, callback, listenerKey?)
  Binds a listener to a BindableEvent.
  Automatically replaces any existing listener using the same logical key.

- :BindFunction(ModuleFolder, Name, callback, listenerKey?)
  Binds a BindableFunction callback with logical key isolation.

This system is intended for:
- Server module to server module communication
- Decoupled server logic
- Game state orchestration
- Multi-layer server reactions (Core Logic, AntiCheat, Analytics, Logging, etc.)

────────────────────────────────────────────────────
MAS Behavior Guarantees
────────────────────────────────────────────────────
- Only one active listener per logical key.
- Rebinding replaces only the matching logical key.
- Different keys coexist without interference.
- Clear ownership via "__Server_" and "__Client_" prefixes.
- No accidental cross-side bindable usage.
- No hidden lifecycle behavior.
- Predictable, explicit, and debuggable communication flow.
- Fully backward compatible with previous versions.
