# Phase 1 report — License audit

## Done

- Read the actual LICENSE/NOTICE file (not README) for all 10 reference
  repos. Full table in `LICENSES.md`.
- Answered all 5 specific questions from the brief. Two answers were
  independently cross-checked outside the reference repos themselves
  (MPFB2's CC0 status via the MakeHuman Community's own licence page;
  Mixamo's terms via Adobe's own FAQ) rather than trusting a single
  source's claim.
- Identified a CC0 rigged human character (MPFB2) to use in Phase 3.
- Confirmed the Mixamo "app-only, no file redistribution" rule three
  independent ways.

## What failed / diverged from the brief

1. **`open-exercise-db` (the CC BY-SA progression/rehab database) has no
   data.** Found it, confirmed the licence, but its own `ROADMAP.md` shows
   the data-seeding step as not done — the repo is schema + roadmap only,
   despite the README's "✅ Seeded, 1,200+ exercises" claim. Nothing to
   import from it right now.
2. **`exercemus/exercises` is not blanket-MIT.** Its own README overrides
   the repo-wide MIT badge for data: each exercise record carries its own
   `license`/`license_author` field (inherited from wger.de), and the
   maintainer explicitly says those must be individually respected. Using
   this source means parsing and carrying per-record licences, not a bulk
   import.
3. **Could not source the "openGym images (ownership disputed)" claim.**
   Read opengym3d's own README, ROADMAP, RESEARCH.md, and
   `docs/FREE_ASSET_RESEARCH.md` — their own research treats MPFB2 (CC0)
   and Mesh2Motion (CC0) as clean and verified, no dispute language
   anywhere. I'm not overriding your instruction — opengym3d images stay
   excluded either way — but I can't independently confirm *why* they're
   disputed. If you have a specific source for that claim, it'd help to
   know it in case it points to a licensing issue in MPFB2/Mesh2Motion
   themselves that I should re-check.

## Needs your decision before Phase 2

- **Exercemus**: skip it for now (simplest, matches "free-exercise-db as
  base layer" already being 800+ exercises), or build the per-record
  license parser so we can use its wger-derived entries too?
- **open-exercise-db being empty**: build the coaching-cue /
  contraindication / progression-ladder fields ourselves from public
  domain training knowledge (the schema already has the fields for it —
  this is real authoring work, not a data import), skip that content for
  now and ship without it, or wait and re-check the repo periodically for
  when it's actually seeded?
- **The "ownership disputed" opengym3d claim**: any source you have for
  it, in case it's a caution I should fold into how we treat MPFB2 too.

Proposed default if you'd rather I just pick: skip exercemus, build a
small first-party set of coaching cues/contraindications/progressions for
the initial exercise list ourselves (not a licensing shortcut — it's
domain knowledge, not copyrighted text, as long as we don't copy specific
phrasing from a paywalled source), and proceed to Phase 2 on that basis.
