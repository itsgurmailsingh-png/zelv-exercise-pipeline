"""Validate every record in data/*.json against data/schema/exercise.schema.json."""
import json
import sys
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((ROOT / "data" / "schema" / "exercise.schema.json").read_text())
validator = jsonschema.Draft7Validator(SCHEMA)

DATA_FILES = [
    "data/free_exercise_db.json",
    "data/exercemus.json",
    "data/exercemus_ccbysa_wger.json",
]


def main():
    total = 0
    failures = 0
    for rel in DATA_FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        records = json.loads(path.read_text())
        for r in records:
            total += 1
            errors = sorted(validator.iter_errors(r), key=lambda e: e.path)
            if errors:
                failures += 1
                print(f"[{rel}] id={r.get('id')!r}:")
                for e in errors:
                    print(f"    {'.'.join(str(p) for p in e.path)}: {e.message}")
    print(f"\n{total} records checked, {failures} failed")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
