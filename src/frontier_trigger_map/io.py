from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]


def read_csv(relative_path: str) -> list[dict[str, str]]:
    path = ROOT / relative_path
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(relative_path: str, fieldnames: list[str], rows: Iterable[dict[str, str]]) -> Path:
    path = ROOT / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return path
