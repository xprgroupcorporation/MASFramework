import os
import re
import shutil
import sys
from pathlib import Path

"""
***BROKEN NOW, I WILL FIX LATER***
"""

MODE = "w"

"""Mode values:
    w: generate/update Markdown docs in Code_Documentation
    rm: remove generated Markdown docs for the selected export
"""

PROJECT_ROOT = Path(__file__).resolve().parent
PLUGIN_ROOT = PROJECT_ROOT / "Plugin"
EXPORT_OUTPUT_ROOT = PLUGIN_ROOT / "Export_Output"
REF_ROOT = PLUGIN_ROOT / "Ref_for_documentation"
DOCS_ROOT = PROJECT_ROOT / "Code_Documentation"
SOURCE_SUFFIXES = {".lua", ".luau"}


def to_title(name: str) -> str:
    name = name.replace("_", " ").replace("-", " ")
    name = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", name)
    return name.strip().title()


def find_export_root() -> Path:
    if not REF_ROOT.exists():
        raise FileNotFoundError(f"Missing folder:\n{REF_ROOT}")

    exports = sorted(
        (
            p for p in REF_ROOT.iterdir()
            if p.is_dir()
            and p.name.lower().startswith("mas_export")
        ),
        key=lambda p: p.name
    )

    if not exports:
        raise FileNotFoundError(
            f"No MAS_Export* folder inside\n{REF_ROOT}"
        )

    export = exports[0]

    print(f"Using export:\n{export}")

    return export

def infer_kind(path: Path, text: str) -> str:
    lower_path = path.as_posix().lower()

    if "/services/" in lower_path or "\\services\\" in lower_path:
        return "Service"
    if "server" in lower_path:
        return "Server Module"
    if "client" in lower_path:
        return "Client Module"
    return "Module"


def infer_runtime(path: Path, text: str) -> str:
    lower_path = path.as_posix().lower()
    lower_text = text.lower()

    if "server" in lower_path:
        return "Server"
    if "client" in lower_path:
        return "Client"
    if "client & server" in lower_text or "client and server" in lower_text:
        return "Client & Server"
    if "server" in lower_text:
        return "Server"
    if "client" in lower_text:
        return "Client"
    return "Roblox Luau"


def extract_header(text: str) -> str:
    for line in text.splitlines()[:80]:
        value = line.strip().strip("-").strip()
        if not value or value in {"[[", "]]", "--[[", "--]]"}:
            continue
        if "Version" in value and "MAS Framework" in value:
            return value
        if "MAS Framework" in value:
            return value
        if value.startswith("[") or value.startswith("@"):
            return value
    return ""


def extract_comment_block(text: str) -> str:
    match = re.search(r"--\[\[(.*?)\]\]", text, flags=re.DOTALL)
    if not match:
        return ""

    return match.group(1).strip()


def module_path_for(rel_path: Path) -> str:
    parts = list(rel_path.with_suffix("").parts)
    if parts and parts[-1] == "_init":
        parts = parts[:-1]
    return "/".join(parts)


def make_doc(export_root: Path, source_path: Path, rel_path: Path, docs_root: Path) -> str:
    text = source_path.read_text(encoding="utf-8", errors="ignore")
    kind = infer_kind(rel_path, text)
    runtime = infer_runtime(rel_path, text)
    header = extract_header(text)
    comment_block = extract_comment_block(text)
    module_name = rel_path.parent.name if source_path.stem == "_init" else source_path.stem
    display_name = to_title(module_name)
    module_path = module_path_for(rel_path)

    lines = [
        f"# {display_name}",
        "",
        f"- Export: `{export_root.name}`",
        f"- Source: `{rel_path.as_posix()}`",
        f"- Kind: {kind}",
        f"- Runtime: {runtime}",
        f"- Module path: `{module_path}`",
        "",
        "## Overview",
        "",
    ]

    if header:
        lines.append(
            f"This {kind.lower()} is part of the MAS Framework export `{export_root.name}`. "
            f"The source header identifies it as: {header}"
        )
    else:
        lines.append(
            f"This {kind.lower()} is part of the MAS Framework export `{export_root.name}`."
        )

    lines.extend(
        [
            "",
            "## Purpose",
            "",
            f"- Provide the `{display_name}` implementation for the MAS Framework runtime.",
            "- Preserve the exported Roblox hierarchy for maintainability.",
            "- Document how this module fits into the generated export structure.",
            "",
            "## Integration Notes",
            "",
            "- Keep public module APIs stable when other scripts require this file.",
            "- Preserve the original export path when moving or regenerating documentation.",
            "- Review related client/server modules before changing shared behavior.",
            "",
            "## Source Reference",
            "",
            f"- Original file: `{source_path.as_posix()}`",
            f"- Documentation file: `{(docs_root / rel_path.with_suffix('.md')).as_posix()}`",
        ]
    )

    if comment_block:
        lines.extend(["", "## Source Comment", "", comment_block])

    return "\n".join(lines) + "\n"


def remove_docs(export_docs_root: Path) -> None:
    if export_docs_root.exists():
        shutil.rmtree(export_docs_root)
        print(f"Deleted {export_docs_root}")
    else:
        print(f"No generated docs found at {export_docs_root}")


def generate_docs(export_root: Path, export_docs_root: Path) -> int:
    count = 0

    for source_path in sorted(export_root.rglob("*")):
        if not source_path.is_file() or source_path.suffix.lower() not in SOURCE_SUFFIXES:
            continue

        rel_path = source_path.relative_to(export_root)
        target_file = export_docs_root / rel_path.with_suffix(".md")
        target_file.parent.mkdir(parents=True, exist_ok=True)
        target_file.write_text(
            make_doc(export_root, source_path, rel_path, export_docs_root),
            encoding="utf-8",
        )
        count += 1
        print(f"Created {target_file}")

    return count


def main() -> int:
    try:
       export_root = find_export_root()
    except FileNotFoundError as exc:
        print(exc)
        return 1

    export_docs_root = DOCS_ROOT / export_root.name
    print(f"Using export source: {export_root}")
    print(f"Using docs output: {export_docs_root}")

    if MODE == "rm":
        remove_docs(export_docs_root)
        return 0

    if MODE != "w":
        print(f"Unsupported MODE: {MODE}")
        return 1

    count = generate_docs(export_root, export_docs_root)
    print(f"Finished {MODE} mode. Generated {count} docs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
