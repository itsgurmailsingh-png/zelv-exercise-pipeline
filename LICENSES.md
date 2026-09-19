# Licences

Every row below was filled in by reading the actual LICENSE/NOTICE/data
files in `/reference/<repo>`, not the README's marketing copy, per the
project's own rule that READMEs are not licences. Sources quoted inline.

| Repository | Code licence | Data/text licence | Media licence | Can ship in app? | Can redistribute files? | Notes |
|---|---|---|---|---|---|---|
| yuhonas/free-exercise-db | Unlicense (public domain) | Unlicense | Unlicense | **Yes** | **Yes** | `LICENSE.md` at repo root, no carve-out for `exercises/<id>/*.jpg`. README explicitly invites "check the repo out and use the JSON files and images locally." Originally derived from `wrkout/exercises.json` (credited, not license-encumbered). |
| exercemus/exercises | MIT | **Per-exercise, not blanket MIT** | N/A — `images/` dir is empty (`.gitkeep` only) | **Conditional** | **Conditional** | Repo's own README: "All code in this repository is under the MIT License... However, all exercises in this repository have a license associated with them that you must follow." Each record carries a `license`/`license_author` field (wger-specific). Merged from wger.de + exercises.json. **Do not treat as blanket-MIT — must parse and carry the per-record license field if imported.** |
| rthepen/workout-database | MIT | MIT (declared at repo root, no per-record override found) | N/A — no exercise images bundled (only a UI `hero.png`); video is by external URL per its own "multi-video fallback" design | **Yes** | **Yes** | Multi-language, JSON Schema draft-07. No media licensing entanglement since it doesn't bundle exercise media. |
| zohar-ui/open-exercise-db | N/A (no code) | CC BY-SA 4.0 | N/A | **No data exists yet** | N/A | **`LICENSE` confirms CC BY-SA 4.0** (Incendium AI) — but the repo contains only `README.md`, `LICENSE`, `exercise.schema.json`, `ROADMAP.md`. Its own `ROADMAP.md`: "Day 3: Import existing 1,269 exercises as seed data" is **unchecked**. The README's "1,200+ exercises ✅ Seeded" claim is not backed by any committed file — zero JSON records, no releases, one branch (`master`). **This source cannot be imported in Phase 2 because it has nothing to import yet.** If/when it's seeded, share-alike applies: keep in a separate file set so it doesn't force CC BY-SA onto the rest of `/data/`. |
| AssiamahS/opengym3d | MIT | N/A (no independent text data beyond exercise specs, which are its own pipeline input, not a licensable "dataset" per se) | Mixed — see breakdown below | **Reference only, per user instruction** | **No — excluded by explicit instruction regardless of licence** | See "opengym3d asset breakdown" below. |
| squall01337/mixamo-llm-mocap | MIT | N/A | N/A (tool, no bundled character/motion files) | Reference only | N/A | Its own LICENSE footer independently confirms: "Mixamo characters... Adobe Mixamo terms. No character FBX is included and none may be redistributed — download your own from mixamo.com." Third independent confirmation of the Mixamo app-only rule (after opengym3d and Adobe's own FAQ). |
| Larenju-Rai/open-mocap-blender | MIT | N/A | N/A (no bundled assets found) | Reference only | N/A | Blender addon, video→mocap. Studied for approach only. |
| cgtinker/BlendArMocap | **GPLv3** | N/A | N/A | Reference only | **No — copyleft** | If any of its code were copied into our pipeline, our pipeline code would need to become GPLv3 too. We are not copying code, only studying the MediaPipe-in-Blender approach. |
| KevinLTT/video2bvh | MIT | N/A | N/A (one demo `cxk.bvh` sample, same MIT terms, not used by us) | Reference only (permissive if we did want to reuse code) | Yes, but unused | Permissive — safe to actually reuse code/approach if needed later, unlike the GPL/AGPL tools. |
| freemocap/freemocap | **AGPLv3** | N/A | N/A | Reference only | **No — strong copyleft (network-use clause)** | Multi-camera mocap, listed in the spec itself as "reference only." Confirmed AGPLv3 at repo root. |

## The 5 specific questions — answered

**1. free-exercise-db: JSON only, or JSON + images public domain?**
Both. `LICENSE.md` (Unlicense) sits at repo root with no per-directory
override, and the README explicitly tells users to "use the JSON files
and images locally" — the maintainer's own stated intent covers both.

**2. The CC BY-SA progression/rehab/coaching-cue database — found and confirmed, but empty.**
`zohar-ui/open-exercise-db`, licence confirmed CC BY-SA 4.0 in its `LICENSE`
file, built by Incendium AI. **However it has no actual exercise data
committed** — see the ROADMAP finding above. Recommendation: do not block
Phase 2 on this source. Proceed with free-exercise-db (+ rthepen, with
exercemus deprioritized pending per-record license parsing) for the base
layer; revisit open-exercise-db once it actually ships data, or build our
own coaching-cue/contraindication/progression fields from public,
non-copyrightable domain knowledge (the schema in Phase 2 already has
fields for this).

**3. opengym3d: code + character + motion licensing, and the Mixamo claim.**
Code: MIT, confirmed. Characters: MPFB2 (MakeHuman for Blender) — mesh,
targets and skins are CC0, confirmed independently at
`static.makehumancommunity.org/about/license.html` (not just opengym3d's
own claim) — the MPFB2 *add-on* is GPLv3 but that only covers the Blender
tool, not content it generates. Motion: mixed lanes, see breakdown below.
The Mixamo "app-only, not redistributable as files" claim is confirmed
independently three times over: opengym3d's own README, the separate
`mixamo-llm-mocap` repo's LICENSE footer, and Adobe's own Mixamo FAQ
(helpx.adobe.com/creative-cloud/faq/mixamo-faq.html — see Q4).

*A note on "ownership disputed" images*: I could not find any statement in
opengym3d's own docs (`README.md`, `ROADMAP.md`, `RESEARCH.md`,
`docs/FREE_ASSET_RESEARCH.md`) describing its images as disputed — their
own research explicitly treats MPFB2 + Mesh2Motion as clean CC0 and
verified. I'm flagging this discrepancy rather than asserting a dispute I
can't source. Regardless, per your explicit instruction we are not copying
their images either way — we'll reproduce the same pipeline (MPFB2 + CC0
motion + our own video) independently so our output is unambiguously ours,
not "opengym3d's images with a different licence justification."

**opengym3d asset breakdown** (from its own `docs/FREE_ASSET_RESEARCH.md`,
independently spot-checked):
| Asset | Licence | Shippable |
|---|---|---|
| MPFB2 human mesh/rig | CC0 | Yes |
| Mesh2Motion CC0 clips (push-up, jumping jacks, jog, run, walk, bear crawl, meditation) | CC0 | Yes |
| Own phone video → MediaPipe | Yours | Yes |
| Mixamo clips | Adobe terms | App-only, no file redistribution |
| CMU mocap clips | CMU terms | App-only, "may not resell even converted" |
| Z-Anatomy (écorché reference) | CC BY-SA 4.0 | Share-alike, kept behind a flag upstream |

**4. Mixamo's current terms (confirmed 2026-09-19 via Adobe's own FAQ).**
Free for unlimited commercial or non-commercial use, no attribution
required. Restriction: characters/animations cannot be redistributed as
standalone files or an asset pack — they must be incorporated into a
finished project. Baking motion into our own app's GLB output, not
shipping raw Mixamo FBX files, stays compliant.

**5. A CC0 rigged human character with no restrictions — found.**
**MPFB2 (MakeHuman for Blender)** — base mesh, targets and skins are CC0,
confirmed at the MakeHuman Community's own licence page (independent of
opengym3d). The add-on/generator code is GPLv3, but that governs the tool,
not content exported from it. This is our character source for Phase 3.

## Explicitly excluded — do not copy into this repo

- ExerciseDB media
- `hasaneyldrm/exercises-dataset` media (marked © Gym visual — confirmed present on the `github.com/topics/exercise-database` listing)
- opengym3d images (excluded per instruction; see note above — no independent dispute found, excluded regardless)

## Verdict for Phase 2

Use **free-exercise-db** (public domain, JSON + images) as the base layer.
Use **rthepen/workout-database** (MIT) to fill multi-language gaps.
**Defer exercemus/exercises** until per-record license parsing is built —
its data is not blanket-MIT despite the repo's MIT badge.
**Defer open-exercise-db** — it has no data yet; re-check periodically or
build the coaching-cue/contraindication/progression fields ourselves.
