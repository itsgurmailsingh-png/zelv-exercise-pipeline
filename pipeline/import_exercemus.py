"""Map exercemus/exercises onto our schema, respecting per-record licences.

The repo's MIT badge covers code only (its own README says so explicitly).
Each exercise record carries its own licence:
  - `exercises` (872 records): 871 have no licence field (exercemus's own
    curated/original content -> repo-default MIT), 1 has an explicit
    CC-BY-SA-3 override -> kept tagged as such.
  - `exercises_to_merge` (190 records): all wger.de, all CC-BY-SA-3,
    explicitly NOT yet part of exercemus's main list. Written to a
    SEPARATE output file so share-alike never touches the MIT/public-domain
    bulk of the data layer.
"""
import json
import re
from pathlib import Path

REF = Path(__file__).resolve().parent.parent / "reference" / "exercises" / "exercises.json"
OUT_MAIN = Path(__file__).resolve().parent.parent / "data" / "exercemus.json"
OUT_CCBYSA = Path(__file__).resolve().parent.parent / "data" / "exercemus_ccbysa_wger.json"

CATEGORY_MAP = {
    "strength": "strength",
    "stretching": "mobility",
    "plyometrics": "strength",
    "strongman": "strength",
    "cardio": "cardio",
    "olympic weightlifting": "strength",
    "crossfit": "strength",
    "calisthenics": "strength",
}
CONTRACTION_MAP = {"plyometrics": "plyometric"}

MIT_LICENCE = {
    "short_name": "MIT",
    "full_name": "MIT License (exercemus/exercises repo default)",
    "url": "https://github.com/exercemus/exercises/blob/main/LICENSE",
    "author": None,
}


def slugify(s):
    s = re.sub(r"[^a-zA-Z0-9]+", "_", s).strip("_").lower()
    return re.sub(r"_+", "_", s)


def licence_for(e):
    lic = e.get("license")
    if not lic:
        return dict(MIT_LICENCE)
    return {
        "short_name": lic.get("short_name"),
        "full_name": lic.get("full_name"),
        "url": lic.get("url"),
        "author": e.get("license_author"),
    }


def convert(e, source_tag):
    return {
        "id": slugify(e["name"]),
        "name": e["name"],
        "aliases": [],
        "category": CATEGORY_MAP.get(e.get("category"), "strength"),
        "primary_muscles": e.get("primary_muscles", []),
        "secondary_muscles": e.get("secondary_muscles", []),
        "equipment": e.get("equipment", []),
        "level": "intermediate",
        "contraction_type": CONTRACTION_MAP.get(e.get("category")),
        "instructions": e.get("instructions", []) or ([e["description"]] if e.get("description") else []),
        "coaching_cues": e.get("tips", []) or [],
        "common_mistakes": [],
        "contraindications": [],
        "progression_next": [],
        "regression_prev": [],
        "progression_variables": [],
        "source": source_tag,
        "licence": licence_for(e),
        "animation_id": None,
    }


def dedupe_ids(records):
    seen = {}
    for r in records:
        base = r["id"]
        if base not in seen:
            seen[base] = 0
            continue
        seen[base] += 1
        r["id"] = f"{base}_{seen[base]}"
    return records


def main():
    raw = json.loads(REF.read_text())

    main_records = dedupe_ids([convert(e, "exercemus/exercises") for e in raw.get("exercises", [])])
    merge_records = dedupe_ids([convert(e, "exercemus/exercises (exercises_to_merge, wger.de)") for e in raw.get("exercises_to_merge", [])])

    OUT_MAIN.write_text(json.dumps(main_records, indent=2, ensure_ascii=False) + "\n")
    OUT_CCBYSA.write_text(json.dumps(merge_records, indent=2, ensure_ascii=False) + "\n")

    print(f"wrote {len(main_records)} records -> {OUT_MAIN}")
    print(f"wrote {len(merge_records)} CC-BY-SA records -> {OUT_CCBYSA}")


if __name__ == "__main__":
    main()
