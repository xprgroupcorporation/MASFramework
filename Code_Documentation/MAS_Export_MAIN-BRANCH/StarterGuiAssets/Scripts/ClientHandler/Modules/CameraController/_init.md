# Camera Controller

- Export: `MAS_Export_MAIN-BRANCH`
- Source: `StarterGuiAssets/Scripts/ClientHandler/Modules/CameraController/_init.luau`
- Kind: Client Module
- Runtime: Client
- Module path: `StarterGuiAssets/Scripts/ClientHandler/Modules/CameraController`

## Overview

This client module is part of the MAS Framework export `MAS_Export_MAIN-BRANCH`. The source header identifies it as: (Made for MAS Framework — Public Standard Ver: 2.0.0+)

## Purpose

- Provide the `Camera Controller` implementation for the MAS Framework runtime.
- Preserve the exported Roblox hierarchy for maintainability.
- Document how this module fits into the generated export structure.

## Integration Notes

- Keep public module APIs stable when other scripts require this file.
- Preserve the original export path when moving or regenerating documentation.
- Review related client/server modules before changing shared behavior.

## Source Reference

- Original file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Modules/CameraController/_init.luau`
- Documentation file: `D:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Code_Documentation/MAS_Export_MAIN-BRANCH/StarterGuiAssets/Scripts/ClientHandler/Modules/CameraController/_init.md`

## Source Comment

============================
|                    XPR Studio™                      
|    Exotic • Passionate • Revolutionize   
|     ©2025-2026 All Rights Reserved.        
============================

Note: Our old official Roblox group was compromised. 
This project is our trademark framework and is not affiliated with any Roblox group.

────────────────────────────────────────────────────
📦 CameraController — Version 0.3.2 (Client) (Module — Foundational)
(Made for MAS Framework — Public Standard Ver: 2.0.0+)
────────────────────────────────────────────────────

────────────────────────────────────────────────────
📌 Overview & Responsibility
────────────────────────────────────────────────────
CameraController is the core client-side camera authority within MAS Framework.
It governs camera stability, control states, and cinematic behavior across
gameplay, character reloads, and cutscenes.

This module ensures the camera never enters an invalid or broken state,
even during character respawn, state transitions, or cinematic playback.
It is a required foundational module and must remain active at all times.

Key responsibilities include:
• Maintaining safe camera state across respawns
• Locking and restoring camera control when required
• Providing a unified cinematic cutscene system
• Acting as the integration point for camera effects and shakes

⚠️ This module must always carry the "ReloadReset" tag.

────────────────────────────────────────────────────
⚙️ Behavior Folder — Settings Used by CameraController
────────────────────────────────────────────────────

These values dynamically control camera behavior at runtime.

• CameraFocus (ObjectValue)
  - If not nil, camera will focus on the given BasePart.
  - Overrides default character-based focus.
  - Sub-values:
    - Offset (Vector3): positional offset from the target
    - Rotation (Vector3): rotation offset in degrees

• Fov (NumberValue)
  - Represents the base camera Field of View.
  - Special behavior:
    - Any NumberValue child modifies the final FOV
      using additive or subtractive operations.

• IsAim (BoolValue)
  - Used internally to adjust camera behavior
    when aiming logic is active.

• StopCamera (BoolValue)
  - When true, freezes camera position and rotation completely.

• ZoomFace (BoolValue)
• ZoomFace1 (BoolValue)
  - Locks camera focus toward a specific close-range point.
  - Used for dialogue, inspection, or cinematic emphasis.
  
────────────────────────────────────────────────────
🧩 Shared Integration
────────────────────────────────────────────────────

• Behavior-driven compatibility
  - Respects camera locks, FOV overrides, focus targets,
    and temporary control suspension.
  - Seamlessly pauses gameplay camera logic during cutscenes.

• Shared services & variables
  - Cutscene modules receive shared Variables and Services.
  - Supports camera shake service, effects, and gameplay hooks
    without unsafe cross-dependencies.

• Standardized structure
  - Includes example cutscenes for both supported systems.
  - Custom cutscenes should follow the same folder layout
    to ensure compatibility and predictability.

────────────────────────────────────────────────────
🎬 Cutscene System — Feature Overview
────────────────────────────────────────────────────

• Dual cutscene pipelines
  - PlayBone (modern, animation-driven)
  - PlayCutscene (legacy, attachment-driven)

• Single-call execution
  - Cutscenes start with one function call.
  - Camera state, locking, and restoration are handled internally.

• Character-attached camera
  - Camera RootPart is Motor6D-attached to the character RootPart.
  - Ensures camera movement remains synced with character motion.

• Safe lifecycle handling
  - Prevents overlapping cutscenes.
  - Locks camera input during playback.
  - Fully restores camera state on completion or interruption.

────────────────────────────────────────────────────
🆕 CameraController.PlayBone (Model)
────────────────────────────────────────────────────

The modern and recommended cutscene system.

• Animation-based camera rig
  - Uses a custom camera rig model with an AnimationController.
  - Camera movement is driven by a single camera animation.
  - Fully compatible with Blender and Roblox Animator workflows.

• Event-marker execution system
  - Animation markers are bound via:
    local function bindMarker(markerName)
  - Marker name determines execution type:
    - Matches a ModuleScript name → executes that module
    - Matches a character animation name → plays it

• Modules & CharAni folders
  - Modules folder:
    - Contains logic units (VFX, SFX, gameplay triggers).
  - CharAni folder:
    - Contains character animations synced to the cutscene.
  - Both share access to Variables, Services,
    and CameraShakeService for coordinated effects.

• Camera animation
  - Only one animation is used for camera motion.
  - Marker timing controls all secondary logic.

• RootPart attachment
  - Camera RootPart is Motor6D-welded to the character RootPart.
  - Allows cinematic movement while following the character.

────────────────────────────────────────────────────
🧱 CameraController.PlayCutscene (Folder) — Legacy
────────────────────────────────────────────────────

An older cutscene system intended for non-animation workflows.

• Attachment-based camera path
  - Camera CFrame is defined using Attachments under RootPart.
  - Suitable when Blender or camera animation is unavailable.

• Attachment markers
  - Each attachment represents a camera point and logic marker.
  - Attachments are processed sequentially.

• Required attachment attributes:
  - Delay (number):
    - Delay before moving to the next camera point.
  - Duration (number):
    - Tween duration to this camera point.
  - EaseStyle (string):
    - TweenService easing style.
  - EaseDirection (string):
    - TweenService easing direction.
  - (Beans shown in examples are visual guides only.)

• Module execution via attachments
  - Attachment name acts as a marker.
  - When matched, the corresponding module executes.

• Character animation
  - Supports one character animation
    for the entire cutscene duration.

• RootPart attachment
  - Camera RootPart is Motor6D-attached to the character RootPart.
  - Ensures camera follows character movement.

────────────────────────────────────────────────────
📌 Notes
────────────────────────────────────────────────────
• Must always include the "ReloadReset" tag.
• Automatically resets camera on character reload or respawn.
• Prevents camera corruption after death or reload.
• Supports R6, R15, and any custom character
  (as long as required camera and character components exist.)
• Includes PlayCutscene helper function.
  (The official guide video for usage soon.)
