"""Run all checks – the same ones that run on GitHub for every pull request.

Usage:  python tools/check.py
"""
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
for script in ("assemble.py", "validate_model.py"):
    result = subprocess.run([sys.executable, str(TOOLS / script)])
    if result.returncode != 0:
        print("\nFAILED - fix the problems above before you open a pull request.")
        sys.exit(1)
print("\nOK - all checks passed.")
