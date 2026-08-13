# Client Apiservice

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `StarterGuiAssets/Scripts/ClientHandler/Services/ClientAPIService.luau`
- Kind: Service
- Runtime: Client
- Module path: `StarterGuiAssets/Scripts/ClientHandler/Services/ClientAPIService`

## Overview

This service is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: (Made for MAS Framework — Public Standard Ver: 2.0.0+)

## Purpose

- Provide the `Client Apiservice` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Services/ClientAPIService.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Services/ClientAPIService.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================

Note: Our old official Roblox group was compromised. 
This project is our trademark framework and is not affiliated with any Roblox group.

────────────────────────────────────────────────────
📦 ClientAPIService — Version 2.4.2 (Client) (Service — Foundational)
(Made for MAS Framework — Public Standard Ver: 2.0.0+)
────────────────────────────────────────────────────

The ClientAPIService is a foundational utility that provides a unified interface
for client-side modules to communicate with the server, shared services,
and other client-side systems in a safe and consistent manner.

Version 2.4.0 Update: introduces logical listener keys, allowing multiple isolated
listeners per RemoteEvent, RemoteFunction, or Bindable without conflict.

────────────────────────────────────────────────────
Benefit
────────────────────────────────────────────────────
- Eliminates duplicated networking and event-handling code across client modules.
- Prevents event stacking and memory leaks caused by repeated connections.
- Supports multiple isolated listeners per remote or bindable via logical keys.
- Enforces predictable duplicate-reset behavior per logical listener key.
- Simplifies both client-server and client-only communication under one service.
- Improves debugging clarity by centralizing remotes and bindables in shared locations.
- Reduces human error scenarios.
- Makes large-scale projects easier to scale, refactor, and maintain.
- Encourages modular, decoupled system design without tight dependencies.

────────────────────────────────────────────────────
Purpose
────────────────────────────────────────────────────
- Provide standardized helper methods (Ex: :Receive, :Send, :Request)
  for client-server communication.
- Provide client-only messaging (Ex: :Bind, :FireBindable)
  via BindableEvents for same-side communication.
- Enforce MAS duplicate-reset rules per logical listener key.
- Allow multiple independent systems to listen to the same remote safely.
- Reduce boilerplate and duplicated networking or event-handling logic.

────────────────────────────────────────────────────
How It Works
────────────────────────────────────────────────────
- Client modules access ClientAPIService through the Services table.
- All networking and client messaging logic is centralized in this service.
- No need to manage Remote references or Bindable lifecycles directly.
- Each listener is identified by a logical key.
- If no key is provided, "__default" is used automatically.
- Rebinding replaces only the listener with the same logical key.
- Different keys do not interfere with each other.

Example (Multi-Listener Support):

ClientAPI:Receive("InventoryModule", "UpdateItem", UpdateUI, "UI")
ClientAPI:Receive("InventoryModule", "UpdateItem", PlayEffect, "FX")

Both listeners remain active and isolated.

────────────────────────────────────────────────────
Intended Use
────────────────────────────────────────────────────
- Any client module that needs to:
  - Communicate with the server
  - Listen for server events
  - Request server-side data
  - Communicate with other client-side modules
- Systems that require multiple independent reactions to the same event.
- Prevents duplicate listeners during respawn, reload, or module reinitialization.
- Improves maintainability and debugging clarity across large projects.

────────────────────────────────────────────────────
Networking Layer
────────────────────────────────────────────────────
- All remotes are stored under "Variables.Remotes", grouped by ModuleFolder.
- Each ModuleFolder must contain:
    - "RE" folder for RemoteEvents
    - "RF" folder for RemoteFunctions

Available methods:

- :Send(ModuleFolder, eventName, ...)
  Fires a RemoteEvent to the server.

- :Request(ModuleFolder, functionName, ...)
  Invokes a RemoteFunction on the server and returns the response.

- :Receive(ModuleFolder, eventName, callback, listenerKey?)
  Listens for a RemoteEvent from the server.
  Automatically disconnects any previous listener using the same logical key.
  If listenerKey is omitted, "__default" is used.

- :ReceiveRequest(ModuleFolder, functionName, callback, listenerKey?)
  Registers a RemoteFunction handler.
  Supports multiple logical keys through internal dispatching.
  If multiple callbacks exist, the last returned value is used.
  If listenerKey is omitted, "__default" is used.

Example:

ClientAPI:Send("InventoryModule", "AddItem", "Sword")
ClientAPI:Request("ProfileModule", "GetProfileData", playerId)

ClientAPI:Receive("CombatModule", "OnHit", UpdateUI, "UI")
ClientAPI:Receive("CombatModule", "OnHit", PlayEffect, "VFX")

────────────────────────────────────────────────────
Client-Side Bindable Messaging
────────────────────────────────────────────────────
ClientAPIService also supports client-only communication using BindableEvents
and BindableFunctions.

- Bindables are stored under "Variables.Bindables", grouped by ModuleFolder.
- All client-created bindables are automatically prefixed with "__Client_"
  for clarity and easy inspection.
- Bindables follow the same logical-key duplicate-reset behavior.

Available methods:

- :GetOrCreateBindable(ModuleFolder, Name)
  Creates or retrieves a client-side BindableEvent.

- :FireBindable(ModuleFolder, Name, ...)
  Fires a client-side BindableEvent.

- :Bind(ModuleFolder, Name, callback, listenerKey?)
  Binds a listener to a BindableEvent.
  Automatically replaces any existing listener using the same logical key.

- :BindFunction(ModuleFolder, Name, callback, listenerKey?)
  Binds a BindableFunction callback with logical key isolation.

This system is intended for:
- Client module to client module communication
- Decoupled gameplay logic
- UI, effects, and local state coordination
- Multi-layer reactions (UI, VFX, Audio, Analytics, etc.)

────────────────────────────────────────────────────
MAS Behavior Guarantees
────────────────────────────────────────────────────
- Only one active listener per logical key.
- Rebinding replaces only the matching logical key.
- Different keys coexist without interference.
- No hidden lifecycle behavior.
- No implicit dependency on character respawn.
- Predictable and explicit event ownership.
- Fully backward compatible with previous versions.
