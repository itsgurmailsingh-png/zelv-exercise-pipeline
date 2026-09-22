"""Split schema-invalid records out of the main data files into
data/needs_review.json, so the main files validate cleanly. Nothing is
deleted — these are upstream data-quality gaps (e.g. a wger record with no
muscle tagged, a free-exercise-db entry that's image-only with no written
instructions), kept for manual fix-up rather than fabricated over.
"""
import json
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
    quarantined = []
    for rel in DATA_FILES:
        path = ROOT / rel
        records = json.loads(path.read_text())
        keep, drop = [], []
        for r in records:
            errors = list(validator.iter_errors(r))
            if errors:
                r["_validation_errors"] = [
                    f"{'.'.join(str(p) for p in e.path)}: {e.message}" for e in errors
                ]
                drop.append(r)
            else:
                keep.append(r)
        path.write_text(json.dumps(keep, indent=2, ensure_ascii=False) + "\n")
        quarantined.extend(drop)
        print(f"{rel}: {len(keep)} kept, {len(drop)} quarantined")

    out = ROOT / "data" / "needs_review.json"
    out.write_text(json.dumps(quarantined, indent=2, ensure_ascii=False) + "\n")
    print(f"\n{len(quarantined)} records -> {out}")


if __name__ == "__main__":
    main()
