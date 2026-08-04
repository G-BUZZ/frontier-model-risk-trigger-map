from __future__ import annotations

import argparse
import sys

from .build import build_outputs
from .validate import validate_repository


def main() -> None:
    parser = argparse.ArgumentParser(description="Frontier Model Risk Trigger Map")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="Validate repository data")
    sub.add_parser("build", help="Build trigger-map outputs")
    args = parser.parse_args()

    issues = validate_repository()
    if issues:
        for issue in issues:
            print(f"ERROR [{issue.table}:{issue.row}] {issue.message}", file=sys.stderr)
        raise SystemExit(1)

    if args.command == "validate":
        print("Validation passed.")
    elif args.command == "build":
        csv_path, md_path = build_outputs()
        print(f"Built {csv_path}")
        print(f"Built {md_path}")


if __name__ == "__main__":
    main()
