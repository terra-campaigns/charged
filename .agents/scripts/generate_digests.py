#!/usr/bin/env python3
"""Runner delegating to oude-mechanismen generate_digests.py."""
import sys
from pathlib import Path

core_script = Path(__file__).resolve().parents[3] / "oude-mechanismen" / "scripts" / "generate_digests.py"
if not core_script.exists():
    core_script = Path("/Users/efsa/repos/oude-mechanismen/scripts/generate_digests.py")

if not core_script.exists():
    print(f"Error: {core_script} not found.", file=sys.stderr)
    sys.exit(1)

with open(core_script, "r", encoding="utf-8") as f:
    code = compile(f.read(), str(core_script), "exec")
    exec(code)
