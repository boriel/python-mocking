import csv

from typing import Any


def csv_to_rows(filename: str) -> list[dict[str, Any]]:
    with open(filename, "rt", encoding="utf-8") as f:
        return list(csv.DictReader(f))
