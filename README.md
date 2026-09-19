# zelv-exercise-pipeline

Own-licensed exercise data + animation pipeline for the Zelv app.

- `/data/` — exercise records (JSON), validated against `/data/schema/`
- `/mocap/raw/` — source phone videos (git-ignored)
- `/mocap/motion/` — extracted motion files
- `/characters/` — 3D character files, one licence note per file
- `/pipeline/` — Python scripts: pose extraction, retargeting, QA, render
- `/renders/` — output animations
- `/reference/` — cloned reference repositories, git-ignored, studied for
  approach only — nothing in here is vendored or shipped
- `LICENSES.md` — licence verdict per source, required reading before
  touching any data or media in this repo

Rendering runs on GitHub Actions (public repo → unlimited free CI minutes,
CPU only, no GPU required). See `.github/workflows/render.yml`.
