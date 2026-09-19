# Licences

Status: **audit in progress (Phase 1)**. Nothing from `/reference/` may be
imported into `/data/`, `/characters/`, or `/pipeline/` until its row below
is filled in from the actual LICENSE/NOTICE/data-licence file — READMEs and
marketing copy are not licences.

| Repository | Code licence | Data/text licence | Media licence | Can ship in app? | Can redistribute files? | Notes |
|---|---|---|---|---|---|---|
| yuhonas/free-exercise-db | TBD | TBD | TBD | TBD | TBD | TBD |
| exercemus/exercises | TBD | TBD | TBD | TBD | TBD | TBD |
| rthepen/workout-database | TBD | TBD | TBD | TBD | TBD | TBD |
| zohar-ui/open-exercise-db | TBD | TBD | TBD | TBD | TBD | TBD |
| AssiamahS/opengym3d | TBD | TBD | TBD | TBD | TBD | TBD |
| squall01337/mixamo-llm-mocap | TBD | TBD | TBD | TBD | TBD | TBD |
| Larenju-Rai/open-mocap-blender | TBD | TBD | TBD | TBD | TBD | TBD |
| cgtinker/BlendArMocap | TBD | TBD | TBD | TBD | TBD | TBD |
| KevinLTT/video2bvh | TBD | TBD | TBD | TBD | TBD | TBD |
| freemocap/freemocap | TBD | TBD | TBD | TBD | TBD | TBD |

## Open questions to resolve in Phase 1

1. free-exercise-db: is public-domain status true for both the JSON *and*
   the images, or JSON only?
2. open-exercise-db (CC BY-SA 4.0): share-alike means any modified version
   of that data must also ship CC BY-SA — keep it in a separate file set
   so it doesn't force a licence on the rest of `/data/`.
3. opengym3d: code licence, and separately the licence of its characters
   and motion clips. Confirm the claim that Mixamo clips are usable inside
   a project but not redistributable as files.
4. Mixamo: confirm current terms for using characters/animations inside
   an app.
5. Find at least one CC0 rigged human character with no restrictions
   (candidates: Quaternius, Kenney, Blender demo files, MakeHuman/MPFB
   exports).

## Explicitly excluded — do not copy into this repo

- ExerciseDB media
- `hasaneyldrm/exercises-dataset` media (marked © Gym visual)
- opengym3d images (ownership disputed)
