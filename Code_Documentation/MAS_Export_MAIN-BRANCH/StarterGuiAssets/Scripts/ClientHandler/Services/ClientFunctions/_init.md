# Client Functions

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `StarterGuiAssets/Scripts/ClientHandler/Services/ClientFunctions/_init.luau`
- Kind: Service
- Runtime: Client
- Module path: `StarterGuiAssets/Scripts/ClientHandler/Services/ClientFunctions`

## Overview

This service is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: (Made for MAS Framework — Public Standard Ver: 2.0.0+)

## Purpose

- Provide the `Client Functions` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Services/ClientFunctions/_init.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Services/ClientFunctions/_init.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================

Note: Our old official Roblox group was compromised. 
This project is our trademark framework and is not affiliated with any Roblox group.

────────────────────────────────────────────────────
📦 ClientFunctions — Version 0.3.0 (Client) (Service — Foundational)
(Made for MAS Framework — Public Standard Ver: 2.0.0+)
────────────────────────────────────────────────────

ClientFunctions is a foundational utility service that provides
a centralized location for reusable client-side helper functions.

Unlike older versions where all functions were manually written
inside a single module, the modern ClientFunctions service uses
a modular auto-registration system.

Any ModuleScript placed inside the "Custom" folder is automatically:

- Required during initialization
- Optionally initialized through its Init() method
- Registered into the ClientFunctions service
- Exposed globally through Services.ClientFunctions

This allows developers to expand utility functionality simply by
adding new modules without modifying the core service itself.

────────────────────────────────────────────────────
Benefits
────────────────────────────────────────────────────
- Modular and scalable utility architecture.
- Plug-and-play function expansion.
- Minimal edits to framework core files.
- Independent utility initialization.
- Better organization and maintainability.
- Reduced risk of merge conflicts.

────────────────────────────────────────────────────
Purpose
────────────────────────────────────────────────────
- Provide shared client-side helper functions.
- Allow utility modules to self-register automatically.
- Centralize reusable helper logic under one service.
- Support optional utility initialization through Init().
- Create a single access point for utility functionality.

────────────────────────────────────────────────────
How It Works
────────────────────────────────────────────────────

When ClientFunctions initializes:

1. The service searches for the "Custom" folder.
2. Every ModuleScript inside the folder is required.
3. If the module contains an Init() function:

   - Init() is executed automatically.
   - The Services table is passed into the module.
4. Every non-reserved member is copied into
   Services.ClientFunctions.
5. Registered functions become globally accessible
   to all client modules.

This means utility modules can remain completely isolated while
still exposing their functionality through a unified interface.

────────────────────────────────────────────────────
Module Structure
────────────────────────────────────────────────────

Example:

ClientFunctions
├─ Custom
│  ├─ MathFunctions
│  ├─ UIFunctions
│  └─ StringFunctions

Each module can contain any number of helper functions.

Example:

```
local Module = {}

function Module.Round(Number)
return math.round(Number)
end

return Module
```

After initialization: Services.ClientFunctions.Round(5.8)
Returns: 6

────────────────────────────────────────────────────
Module Initialization
────────────────────────────────────────────────────

Utility modules may optionally define:

```
function Module:Init(Services)

This function is automatically executed when the service loads.

Example:

local Module = {}

function Module:Init(Services)
print("MathFunctions Initialized")
end

return Module
```

This is useful for:

- Cached references
- Service dependencies
- One-time setup logic
- Utility configuration

Init() is not registered as a callable utility function.

────────────────────────────────────────────────────
Function Registration Rules
────────────────────────────────────────────────────

All keys found inside a custom module are copied into
Services.ClientFunctions except reserved service members.

Reserved keys:

- Init
- Grab
- Name
- __index
- Connections

These keys are ignored during registration.

Example:

```
local Module = {}

function Module:Init()
end

function Module.Test()
end
```

Only:

```
Services.ClientFunctions.Test()
``

becomes available.

────────────────────────────────────────────────────
Duplicate Protection
────────────────────────────────────────────────────

If multiple modules attempt to register the same key,
the first registered function is preserved.

The duplicate function is skipped and a warning is issued.

Example:

MathFunctions:

- Round()

StringFunctions:

- Round()

Result:

[MathFunctions] Round registered
[StringFunctions] Round skipped

This prevents accidental overrides and ensures predictable behavior.

────────────────────────────────────────────────────
Usage Example
────────────────────────────────────────────────────

Module:
```
local Module = {}

function Module.FormatCoins(Value)
return tostring(Value) .. " Coins"
end

return Module
```

Access:

```
local ClientFunctions = Services.ClientFunctions

print(ClientFunctions.FormatCoins(500))
```
Output:

500 Coins

────────────────────────────────────────────────────
Function Declaration Rules***
────────────────────────────────────────────────────

Due to Luau Limitations***
ClientFunctions is designed for stateless utility functions.

All registered functions should be declared using dot syntax (.).

Supported:

function Module.Round(Number)
	return math.round(Number)
end

Not Supported:

function Module:Round(Number)
	return math.round(Number)
end

Functions declared using colon syntax (:)
depend on a self reference and may not behave
as expected after registration.
Recommended to create new service to use them.

To ensure predictable behavior, all utility
functions registered through ClientFunctions
should use dot syntax (.).

────────────────────────────────────────────────────
MAS Behavior Guarantees
────────────────────────────────────────────────────

- All Custom modules load automatically.
- Init() executes automatically when present.
- Registered functions become available globally.
- Reserved framework keys are protected.
- Duplicate registrations are prevented.
- Utility modules remain fully independent.
- New functionality can be added without editing the service.
- Consistent access through Services.ClientFunctions.
- Scales cleanly with project size.
