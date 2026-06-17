"""
MAS Framework Export Companion
================================
Run this script before clicking Export in the MAS Plugin.
It listens on localhost:7777 and writes the exported files to MAS_Export/

Requirements: Python 3.6+ (no pip installs needed, uses stdlib only)

Usage:
    python mas_export_companion.py

The MAS_Export/ folder will be created next to this script.
"""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 7777
OUTPUT_DIR = "MAS_Export"


class ExportHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        # Suppress default HTTP log noise, print our own
        pass

    def do_GET(self):
        if self.path == "/ping":
            self._respond(200, "pong")
        else:
            self._respond(404, "not found")

    def do_POST(self):
        if self.path != "/export":
            self._respond(404, "unknown endpoint")
            return

        # Read body
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

        # Write files
        written = 0
        errors = []

        for entry in files:
            rel_path = entry.get("path", "")
            source = entry.get("source", "")

            if not rel_path:
                continue

            # Sanitize: never allow absolute paths or traversal
            rel_path = rel_path.replace("\\", "/").lstrip("/")
            if ".." in rel_path:
                errors.append(f"Skipped unsafe path: {rel_path}")
                continue

            full_path = os.path.join(OUTPUT_DIR, rel_path)
            folder = os.path.dirname(full_path)

            try:
                os.makedirs(folder, exist_ok=True)
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write(source)
                written += 1
            except Exception as e:
                errors.append(f"Failed to write {rel_path}: {e}")

        # Write manifest.json (without source blobs to keep it readable)
        try:
            manifest = {k: v for k, v in data.items() if k != "files"}
            manifest["files"] = [
                {k: v for k, v in entry.items() if k != "source"}
                for entry in files
            ]
            manifest_path = os.path.join(OUTPUT_DIR, "manifest.json")
            with open(manifest_path, "w", encoding="utf-8") as f:
                json.dump(manifest, f, indent=2)
        except Exception as e:
            errors.append(f"Failed to write manifest: {e}")

        # Summary
        print(f"\n[MAS Export] Export received!")
        print(f"  Files written : {written}")
        print(f"  Output folder : {os.path.abspath(OUTPUT_DIR)}")

        skipped_warnings = data.get("warnings", [])
        if skipped_warnings:
            print("  Plugin warnings:")
            for w in skipped_warnings:
                print(f"    - {w}")

        if errors:
            print("  Write errors:")
            for e in errors:
                print(f"    - {e}")

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
    print(f"Output folder: {os.path.abspath(OUTPUT_DIR)}")
    print(f"Waiting for export from Studio plugin...")
    print(f"Press Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nCompanion stopped.")
