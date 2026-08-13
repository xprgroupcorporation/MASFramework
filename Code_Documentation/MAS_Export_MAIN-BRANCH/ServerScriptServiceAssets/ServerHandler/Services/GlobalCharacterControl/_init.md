# Global Character Control

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `ServerScriptServiceAssets/ServerHandler/Services/GlobalCharacterControl/_init.luau`
- Kind: Service
- Runtime: Server
- Module path: `ServerScriptServiceAssets/ServerHandler/Services/GlobalCharacterControl`

## Overview

This service is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: (Made for MAS Framework — Public Standard Ver: 2.0.0+)

## Purpose

- Provide the `Global Character Control` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/ServerScriptServiceAssets/ServerHandler/Services/GlobalCharacterControl/_init.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/ServerScriptServiceAssets/ServerHandler/Services/GlobalCharacterControl/_init.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================

Note: Our old official Roblox group was compromised. 
This project is our trademark framework and is not affiliated with any Roblox group.

────────────────────────────────────────────────────
📦 GlobalCharacterControl — Version 1.1.5 (Server) (Service — Foundational)
(Made for MAS Framework — Public Standard Ver: 2.0.0+)
Formerly: CustomCharacterSystem
────────────────────────────────────────────────────

────────────────────────────────────────────────────
🌟 Overview:
────────────────────────────────────────────────────
GlobalCharacterControl fully replaces Roblox's default character loading
pipeline with a controlled, server-authoritative character lifecycle.
It is registered as a MAS SERVICE (not a private module) so any other
server module can call it directly — spawning custom rigs, shapeshifting,
transform abilities, or round/match based spawning:

	Services.GlobalCharacterControl:SpawnFor(player)
	Services.GlobalCharacterControl:SpawnCustomRig(player, rig, settings)
	Services.GlobalCharacterControl:SetCanSpawn(false)  -- round hasn't started

The system is split into a thin orchestrator (this file) and a set of
swappable Core/ modules that own specific responsibilities:
  • Core/LifeHandler   — stat system, death, corpse
  • Core/RagdollSystem — all ragdoll / stun physics
  • Core/RespawnSystem — respawn queue, cooldowns, round/match control

Plus Custom/OnSpawnOrDeath/ — game-specific hooks that fire on every
spawn or death (overhead UI, data wipe, kill streak resets, etc.).
The spawn effect is now also handled here — drop a module with
InitSpawn to customize it per-game.

────────────────────────────────────────────────────
⚙️ How to Setup (Required)
────────────────────────────────────────────────────
1) Set:
   Players.CharacterAutoLoads = false (handled automatically in Init)

2) Place this "GlobalCharacterControl" ModuleScript inside your
   Services folder (wherever Framework.AddServices() points), so
   the framework's loader registers it correctly.

3) Place the matching "GlobalCharacterControl" DATA folder inside:
   ReplicatedStorageAssets
   (Settings / RespawnQueue / Models.StarterCharacter.Rig / CharacterScript / Save)

4) The framework will call Init(self) automatically at startup,
   followed by Grab(self, Services) once all services are loaded.

────────────────────────────────────────────────────
🧩 Core Responsibilities
────────────────────────────────────────────────────
• Disable Roblox default character loading
• Spawn and respawn custom character rigs (incl. custom rigs for shapeshift/transform)
• Handle custom HP, multiple lives, and revive logic
• Apply ragdoll physics for stun and death states
• Manage death remnants and corpse behavior
• Reinitialize PlayerGui safely on respawn
• Support optional Roblox web accessory + clothing transfer (via HumanoidDescription, no LoadCharacterAsync)
• Expose server-side events for death and respawn hooks
• Provide a public respawn queue (visible in RepStorage) for round/match systems
• Provide a runtime-editable Settings folder, readable/writable by any script

────────────────────────────────────────────────────
🔧 Settings (RepStorage.GlobalCharacterControl.Settings)
────────────────────────────────────────────────────

📁 Character/
  • AllowWebAccessories   (Bool) — transfer ALL accessories from player's avatar to custom rig.
                                   Uses HumanoidDescription — never calls LoadCharacterAsync.
                                   Cached in MainFolder.Save per-player; refreshed each respawn,
                                   falls back to cached copy if the web fetch fails.
                                   Dev is responsible for filtering/removing unwanted accessories.
  • UseCustomRigDefault   (Bool) — true: always use StarterCharacter.Rig (custom rig).
                                   false: use StarterCharacter.Rig as the gameplay rig but apply
                                   the player's Roblox avatar appearance (HumanoidDescription)
                                   on top of it. The custom rig is ALWAYS the character model;
                                   this only controls whether appearance is applied from the web.
  • UseRobloxClothing     (Bool) — when true, applies the player's Roblox 2D shirt/pants/graphic
                                   to the custom rig via HumanoidDescription (no LoadCharacterAsync).

📁 Respawn/
  • BodyDespawnTime       (Int)  — seconds before a corpse is cleaned up via Debris
  • CanSpawn              (Bool) — global spawn lock, used for round/match gating
  • RagdollDeath          (Bool) — true: full ragdoll physics on death. false: classic death pose
  • RespawnTime           (Int)  — default respawn delay in seconds

📁 Stat/
  • ApplyCustomMASStatSys (Bool) — enable the custom HP/LifeLeft death pipeline
  • ShouldTag             (Bool) — tag spawned characters with "IsHuman"

These are read/written via :GetSetting() / :SetSetting(), or read directly
by any script via :GetSettingsFolder() — no API linking needed.

────────────────────────────────────────────────────
📌 Notes
────────────────────────────────────────────────────
• This system assumes full ownership of the character lifecycle
• Default Roblox respawn behavior is intentionally bypassed
• AltInit is provided for testing or reverting to default behavior
• Spawn effect logic has been moved to Custom/OnSpawnOrDeath/ — dev can
  add a SpawnEffect module there to customize it per-game
• AllowWebAccessories / UseRobloxClothing / UseCustomRigDefault=false all use
  GetHumanoidDescriptionFromUserId — they never call LoadCharacterAsync, so
  plr.Character is never clobbered mid-spawn
• Customization + save systems are intentionally NOT included — build
  your own on top using Custom/OnStart or Custom/Forever
• Intended for experienced developers and modular MAS projects
