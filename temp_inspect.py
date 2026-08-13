import os
import pathlib
from collections import defaultdict

root = pathlib.Path(r'd:/Main Work/XPR Group Corp. All Docs/MAS Framework - Github ver/Plugin/Ref_for_documentation/MAS_Export_13-35-23_02-07-2026_N_A')
bases = [root/'StarterGuiAssets'/'Scripts'/'ClientHandler', root/'ServerScriptServiceAssets'/'ServerHandler']
for base in bases:
    print('===', base.name, '===')
    for path in sorted(base.rglob('*')):
        if path.is_file() and path.suffix in {'.luau', '.lua'}:
            rel = path.relative_to(base)
            try:
                text = path.read_text(encoding='utf-8')
            except Exception as e:
                text = ''
            lines = [line.strip() for line in text.splitlines() if line.strip()]
            preview = ' '.join(lines[:12])[:600]
            print(f'{rel} | {preview}')
    print()
