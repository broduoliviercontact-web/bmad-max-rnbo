#!/usr/bin/env python3
from pathlib import Path
import argparse

TEMPLATE_DIRS = [
    "patches",
    "docs",
    "export/rnbo",
    "web/src",
    "tests",
]

def main():
    parser = argparse.ArgumentParser(description="Scaffold a BMAD-MAX project.")
    parser.add_argument("name", help="Project name, e.g. split-flap-clock")
    args = parser.parse_args()

    root = Path(args.name)
    root.mkdir(exist_ok=True)

    for d in TEMPLATE_DIRS:
        (root / d).mkdir(parents=True, exist_ok=True)

    (root / "README.md").write_text(f"# {args.name}\n\nBMAD-MAX project.\n", encoding="utf-8")
    (root / "docs" / "PROJECT_BRIEF.md").write_text("# Project Brief\n\n", encoding="utf-8")
    (root / "docs" / "PATCH_ARCHITECTURE.md").write_text("# Patch Architecture\n\n", encoding="utf-8")
    (root / "docs" / "RNBO_COMPATIBILITY_MATRIX.md").write_text("# RNBO Compatibility Matrix\n\n", encoding="utf-8")

    print(f"Created {root}")

if __name__ == "__main__":
    main()
