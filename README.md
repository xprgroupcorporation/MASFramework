<h2>
   <p align="center">
    <b>MAS Framework</b>
  </p>
  <p align="center">
    <b>Modular Architecture Standard</b>
  </p>
  <p align="center">
    <i>A production-ready framework for scalable Roblox development.</i>
  </p>
</h2>

<div align="center">

![Platform](https://img.shields.io/badge/Platform-Roblox-AFA9EC?style=flat-square&labelColor=3C3489)
![Status](https://img.shields.io/badge/Status-Production_Ready-AFA9EC?style=flat-square&labelColor=3C3489)
![Framework Engine Version](https://img.shields.io/badge/Framework_Engine-v2.0.0-534AB7?style=flat-square&labelColor=3C3489)
![Plugin Tool Version](https://img.shields.io/badge/Plugin_Tool%2B-v0.8.6-534AB7?style=flat-square&labelColor=3C3489)

![Architecture](https://img.shields.io/badge/Architecture-Component--Oriented-7F77DD?style=flat-square&labelColor=26215C)
![Multi--Place](https://img.shields.io/badge/Multi--Place-Supported-7F77DD?style=flat-square&labelColor=26215C)
![Foundation_Modules](https://img.shields.io/badge/Foundation_Modules%2FServices-Included-534AB7?style=flat-square&labelColor=3C3489)
![Add--on_Modules](https://img.shields.io/badge/Add--on_Modules%2FServices-Included-534AB7?style=flat-square&labelColor=3C3489)

</div>

MAS Framework is a modular Roblox development framework built to keep projects **organized, scalable, and maintainable** as they grow.

It provides a consistent architecture for building everything from small experiences to large **multi-place games**, with structured client/server separation and integrated Roblox Studio tooling.

> **Build systems. Not spaghetti.**

## 💡 What is MAS?

**MAS — Modular Architecture Standard** is an architecture framework designed around the idea that Roblox projects should remain understandable even as their codebase grows.

MAS gives developers conventions and systems for organizing:

* 🧩 **Modular game systems**
* 🔀 **Client / Server separation**
* 🌐 **Multi-place experiences**
* ⚙️ **Service-based architecture**
* 🔗 **Shared systems and dependencies**
* 🛠️ **Roblox Studio tooling**

Instead of every project developing its own way of organizing systems, MAS provides a common structure that developers can build upon.

## ⭐ Why MAS?

Roblox development is easy to start. Keeping a large Roblox project organized is not.  
As a project grows, scripts multiply, dependencies become harder to track, client and server responsibilities become mixed, and maintaining the same architecture across multiple places becomes increasingly difficult.
MAS is designed to solve that problem.

### 🧩 Modular by Design

Break large systems into smaller, independent modules that can be developed, maintained, and replaced without restructuring the entire project.

### 🔒 Clear Client / Server Architecture

Keep client-side and server-side responsibilities separated while providing structured communication between them.

### 🌐 Multi-Place Ready

Designed for Roblox experiences that contain multiple places, allowing projects to maintain a consistent framework structure across different environments.

### ⚙️ Structured Services

MAS provides a standardized service lifecycle, including methods such as `Init` and `Grab`, allowing systems to initialize and access dependencies predictably.

### 🛠️ Built-in Studio Tooling

MAS is accompanied by **MAS Super Tool+**, a Roblox Studio plugin designed to simplify framework installation, project management, exporting, synchronization, and development workflows.

### 🤖 AI-Friendly Development

MAS projects can be exported into a structured source format designed to make the framework easier to inspect, document, and work with using modern AI development tools.

## 🏗️ Architecture

MAS follows a modular architecture where systems are separated according to their responsibility rather than being placed into one large collection of scripts.

A typical project can contain:

```text
MAS
├── Client
│   ├── Services
│   └── Modules
│
├── Server
│   ├── Services
│   └── Modules
│
├── ServerStorageAssets
│   └── Sharred
│
└── UniqueServerSettings ← Setting your project, more in the handbook
    ├── MapType
    └── PlaceName
```

The exact structure can be adapted to the needs of the project while maintaining the principles of MAS.

## 🛠️ MAS Super Tool+

**MAS Super Tool+** is the official Roblox Studio plugin for MAS Framework.

It extends the framework beyond runtime code and provides development tooling for managing MAS projects.

### Current tooling includes:

![Install](https://img.shields.io/badge/-Framework_Installation-534AB7?style=flat-square&labelColor=3C3489)
![Sync](https://img.shields.io/badge/-Project_Synchronization-534AB7?style=flat-square&labelColor=3C3489)
![Export](https://img.shields.io/badge/-Source_Export-534AB7?style=flat-square&labelColor=3C3489)
![Templates](https://img.shields.io/badge/-Module_%26_Service_Templates/Insert-534AB7?style=flat-square&labelColor=3C3489)
![Assets](https://img.shields.io/badge/-Asset_%26_Tag_Management-534AB7?style=flat-square&labelColor=3C3489)
![Commands](https://img.shields.io/badge/-Project_Commands-534AB7?style=flat-square&labelColor=3C3489)

The plugin is intended to make MAS easier to install, maintain, and develop with directly inside Roblox Studio.

## 📦 Getting Started

[![Download](https://img.shields.io/badge/MAS_Framework-Download_Latest_Release-534AB7?style=for-the-badge&labelColor=3C3489)](https://github.com/xprgroupcorporation/MASFramework/releases/latest)

### Setup Steps

**1. Download the Framework**
Grab the latest `MAS_Framework.rbxm` from the [Releases](https://github.com/xprgroupcorporation/MASFramework/releases/latest) page.

**2. Install the Plugin**
If you don't already have **MAS Super Tool+** installed, download the `.rbxmx` from the same release and place it in your local Roblox `Plugins` folder, then restart Studio.

> 💡 **Tip:** Bind a keyboard shortcut to toggle the plugin widget via Studio's *Customize Shortcuts* menu. Recommended: `Right Alt + ,`

**3. Insert & Install**
Drag `MAS_Framework.rbxm` into `Workspace`, open the **MAS Super Tool+** widget, and use the **Install** option to unpack the framework into your project.

For more instructions and framework concepts, see the **MAS Handbook**.

### 📖 Documentation (!!!REMAKE IN PROGRESS!!!)

**[MAS Handbook](https://canva.link/y5f98pi02r9isz0)** (!!!FOLLOW GITHUB FOR NOW!!!)

The handbook contains information about installation, architecture, services, modules, APIs, and framework usage.

### 💬 Community

**[XPR Studio Discord](https://discord.gg/YqbkxwRKgW)**

Ask questions, discuss development, report issues, and share projects using MAS.

## 🔄 Version Compatibility

**Current Release: `v2.0.0`**

MAS v2.0.0 introduces the current framework architecture.

> ⚠️ **v2.0.0 is not compatible with MAS v1.8.1–v1.9.9.**

Projects using previous MAS versions should follow the migration guidance before upgrading.

## 🚀 Project Status

![Status](https://img.shields.io/badge/Status-Production_Ready-7F77DD?style=flat-square\&labelColor=26215C)
![Release](https://img.shields.io/badge/Release-Public-534AB7?style=flat-square\&labelColor=3C3489)

MAS Framework is **publicly available for development use**.

The framework is actively maintained and will continue to evolve through improvements to its architecture, tooling, documentation, and developer experience.

The goal is not to make MAS the only way to build Roblox games.

The goal is to provide developers with a **strong foundation when they want one**.

## 🧠 Design Philosophy

MAS is built around a few simple principles:

| Principle           | Purpose                                                               |
| ------------------- | --------------------------------------------------------------------- |
| **Modularity**      | Keep systems independent and manageable.                              |
| **Separation**      | Clearly define responsibilities between systems.                      |
| **Scalability**     | Allow projects to grow without collapsing under their own complexity. |
| **Consistency**     | Give teams a predictable development structure.                       |
| **Flexibility**     | Provide structure without unnecessarily restricting developers.       |
| **Maintainability** | Make existing systems easier to understand and modify.                |

> **Good architecture should disappear into the workflow — not become the workflow.**

## 🏢 About

MAS Framework is developed by **XPR Studio™**, part of **XPR Group Corporation™**.

## 📫 Links

| Type            | Link                                                             |
| --------------- | ---------------------------------------------------------------- |
| 📖 Handbook     | [MAS Handbook](https://canva.link/y5f98pi02r9isz0)      (!!!REMAKE IN PROGRESS!!!)         |
| 💬 Discord      | [XPR Studio Discord](https://discord.gg/YqbkxwRKgW)              |
| 🏢 Github | [XPR Group Corporation™](https://github.com/xprgroupcorporation) |

---

<div align="center">

### **Build modular. Build scalable. Build with MAS.**

**MAS Framework — Modular Architecture Standard**

</div>

---

<h2>
  <p align="center">
    XPR Group Corporation™
  </p>
  <p align="center">
    <b>Exotic • Passionate • Revolutionize</b>
  </p>
</h2>
