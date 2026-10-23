#!/usr/bin/env python3
"""Runner delegating to oude-mechanismen audit_coverage.py."""
import sys
from pathlib import Path

core_script = Path(__file__).resolve().parents[3] / "oude-mechanismen" / "scripts" / "audit_coverage.py"
if not core_script.exists():
    core_script = Path("/Users/efsa/Repos/oude-mechanismen/scripts/audit_coverage.py")

if not core_script.exists():
    print(f"Error: {core_script} not found.", file=sys.stderr)
    sys.exit(1)

with open(core_script, "r", encoding="utf-8") as f:
    code = compile(f.read(), str(core_script), "exec")
    exec(code)
