"""
MAS Framework Export Companion V1.5
===================================

Companion server for the MAS Framework Super Tool plugin.

This utility receives exported framework data directly from Roblox Studio
and reconstructs it on disk as a clean .luau source tree.

Why this tool exists
--------------------
Roblox places are normally shared as .rbxl/.rbxm files, which are
serialized XML. While perfect for Roblox Studio, this format contains
large amounts of metadata that are unnecessary for AI code analysis.

For example, a simple ModuleScript like:

    return {
        Name = "Test"
    }

is only around 10-20 AI tokens as plain Lua source.

The same module inside a serialized Roblox file becomes something like:

    <Item class="ModuleScript">
        <Property name="Name">Test</Property>
        <Property name="Source"><![CDATA[
        return {
            Name = "Test"
        }
        ]]></Property>
        ...
    </Item>

which can easily consume 100-500+ tokens after serialization.

By exporting the framework as a normal folder structure containing
only .luau files, folders, metadata, and assets, AI models spend their
context window on your code instead of Roblox's XML.

Benefits
--------
• Typically reduces AI token usage by approximately 5x-20x compared to
  serialized Roblox files.
• Produces a clean project structure that AI models understand more
  naturally.
• Easier to inspect, search, version with Git, and share with others.
• Ideal for feeding large Roblox frameworks into ChatGPT, Claude,
  Gemini, and other coding assistants.
• Especially useful for users without access to large-context or
  premium AI coding tools, allowing much more efficient use of limited
  context windows.

The exported project can simply be compressed into a ZIP archive and
uploaded directly to an AI assistant for framework analysis, debugging,
refactoring, documentation, or code generation.

Requirements
------------
Python 3.6+
(No external packages required.)

Usage
-----
1. Open a terminal inside the Plugin/ folder.
2. Run:

       python mas_export_companion.py

3. Open Roblox Studio with your MAS project.
4. Click Export in the MAS Framework Super Tool plugin.
5. The exported project will appear inside Export_Output/.

Workflow
--------
Roblox Studio Plugin
    Collects all framework source files and metadata.
            │
            ▼
    Sends JSON to localhost:7777/export
            │
            ▼
MAS Export Companion
    Receives the payload.
    Creates a timestamped export folder.
    Writes the complete .luau source tree.
    Generates .gitkeep files for empty folders.
    Writes manifest.json containing paths, tags, and attributes
    (without duplicating source code).
            │
            ▼
Export_Output/
    MAS_Export_{HH-MM-SS}_DD-MM-YYYY_{PlaceName}/
        ReplicatedStorageAssets/
        ServerScriptServiceAssets/
        StarterGuiAssets/
        Template_Modules/
        Info_(Read!).luau
        manifest.json

Notes
-----
• Keep this server running while using the export feature.
• Every export creates a new timestamped folder.
• Previous exports are never overwritten.
• Press Ctrl+C to stop the server.
"""

from email import errors
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

PORT = 7777
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "Export_Output")


class ExportHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        pass  # suppress default HTTP noise

    def do_GET(self):
        if self.path == "/ping":
            self._respond(200, "pong")
        else:
            self._respond(404, "not found")

    def do_POST(self):
        if self.path != "/export":
            self._respond(404, "unknown endpoint")
            return

        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            self._respond(400, "empty body")
            return

        raw = self.rfile.read(length)

        try:
            data = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError as e:
            self._respond(400, f"invalid JSON: {e}")
            return

        files = data.get("files", [])
        if not files:
            self._respond(400, "no files in payload")
            return

        place_name = data.get("placeName", "Unknown")
        timestamp  = datetime.now().strftime("%H-%M-%S_%d-%m-%Y")
        folder_name = f"MAS_Export_{timestamp}_{place_name}"
        export_path = os.path.join(OUTPUT_DIR, folder_name)

        written = 0
        errors  = []

        # Create all folders first (including empty ones)
        for folder_entry in data.get("emptyFolders", []):
            if isinstance(folder_entry, dict):
                folder_rel = folder_entry.get("path", "")
            else:
                folder_rel = folder_entry
            folder_rel = folder_rel.replace("\\", "/").lstrip("/")
            if ".." in folder_rel or not folder_rel:
                continue
            try:
                os.makedirs(os.path.join(export_path, folder_rel), exist_ok=True)
            except Exception as e:
                errors.append(f"Failed to create folder {folder_rel}: {e}")

        # Write files
        for entry in files:
            rel_path = entry.get("path", "")
            source   = entry.get("source", "")

            if not rel_path:
                continue

            rel_path = rel_path.replace("\\", "/").lstrip("/")
            if ".." in rel_path:
                errors.append(f"Skipped unsafe path: {rel_path}")
                continue

            full_path = os.path.join(export_path, rel_path)
            folder    = os.path.dirname(full_path)

            try:
                os.makedirs(folder, exist_ok=True)
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write(source)
                written += 1
            except Exception as e:
                errors.append(f"Failed to write {rel_path}: {e}")

        # Add .gitkeep to any folder that has no files in it
        gitkeep_added = 0
        for dirpath, dirnames, filenames in os.walk(export_path):
            # Ignore manifest.json and .gitkeep themselves when checking emptiness
            real_files = [f for f in filenames if f not in ("manifest.json", ".gitkeep")]
            if not real_files and not dirnames:
                gitkeep_path = os.path.join(dirpath, ".gitkeep")
                try:
                    with open(gitkeep_path, "w") as f:
                        pass  # empty file
                    gitkeep_added += 1
                except Exception as e:
                    errors.append(f"Failed to write .gitkeep in {dirpath}: {e}")

        # Write manifest.json — exclude source blobs but keep everything else
        try:
            manifest = {k: v for k, v in data.items() if k != "files"}
            manifest["files"] = [
                {k: v for k, v in entry.items() if k != "source"}
                for entry in files
            ]
            with open(os.path.join(export_path, "manifest.json"), "w", encoding="utf-8") as f:
                json.dump(manifest, f, indent=2)
        except Exception as e:
            errors.append(f"Failed to write manifest: {e}")

        # Summary
        print(f"\n[MAS Export] Export complete!")
        print(f"  Place      : {place_name}")
        print(f"  Files      : {written}")
        print(f"  .gitkeep   : {gitkeep_added} empty folders")
        print(f"  Output     : {os.path.abspath(export_path)}")

        for w in data.get("warnings", []):
            print(f"  [WARN] {w}")
        for e in errors:
            print(f"  [ERROR] {e}")
        print()

        if errors:
            self._respond(500, json.dumps({"written": written, "errors": errors}))
        else:
            self._respond(200, json.dumps({"written": written}))

    def _respond(self, code, body):
        encoded = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    server = HTTPServer(("localhost", PORT), ExportHandler)
    print(f"MAS Export Companion running on localhost:{PORT}")
    print(f"Output: {os.path.abspath(OUTPUT_DIR)}")
    print(f"Format: MAS_Export_HH-MM-SS_DD-MM-YYYY_{{PlaceName}}/")
    print(f"Waiting... (Ctrl+C to stop)\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")