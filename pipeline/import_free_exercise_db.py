"""Map yuhonas/free-exercise-db (Unlicense, public domain) onto our schema.

Text/data only — free-exercise-db's images are also public domain, but this
repo's own ground rules are text-and-data-only regardless, so images are
dropped on import.
"""
import json
import re
from pathlib import Path

REF = Path(__file__).resolve().parent.parent / "reference" / "free-exercise-db" / "dist" / "exercises.json"
OUT = Path(__file__).resolve().parent.parent / "data" / "free_exercise_db.json"

LEVEL_MAP = {"beginner": "beginner", "intermediate": "intermediate", "expert": "advanced"}
CATEGORY_MAP = {
    "strength": "strength",
    "cardio": "cardio",
    "stretching": "mobility",
    "plyometrics": "strength",
    "powerlifting": "strength",
    "strongman": "strength",
    "olympic weightlifting": "strength",
}
CONTRACTION_MAP = {"plyometrics": "plyometric"}


def slugify(s):
    s = re.sub(r"[^a-zA-Z0-9]+", "_", s).strip("_").lower()
    return re.sub(r"_+", "_", s)


def convert(e):
    equipment = e.get("equipment")
    equipment = [equipment] if isinstance(equipment, str) else (equipment or [])
    return {
        "id": slugify(e["id"]),
        "name": e["name"],
        "aliases": [],
        "category": CATEGORY_MAP.get(e.get("category"), "strength"),
        "primary_muscles": e.get("primaryMuscles", []),
        "secondary_muscles": e.get("secondaryMuscles", []),
        "equipment": equipment,
        "level": LEVEL_MAP.get(e.get("level"), "intermediate"),
        "contraction_type": CONTRACTION_MAP.get(e.get("category")),
        "instructions": e.get("instructions", []),
        "coaching_cues": [],
        "common_mistakes": [],
        "contraindications": [],
        "progression_next": [],
        "regression_prev": [],
        "progression_variables": [],
        "source": "yuhonas/free-exercise-db",
        "licence": {
            "short_name": "Unlicense",
            "full_name": "The Unlicense (public domain)",
            "url": "https://unlicense.org",
            "author": None,
        },
        "animation_id": None,
    }


def main():
    raw = json.loads(REF.read_text())
    records = [convert(e) for e in raw]
    seen_ids = set()
    for r in records:
        if r["id"] in seen_ids:
            raise ValueError(f"duplicate id after slugify: {r['id']}")
        seen_ids.add(r["id"])
    OUT.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {len(records)} records -> {OUT}")


if __name__ == "__main__":
    main()
