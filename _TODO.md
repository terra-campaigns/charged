# Future Wiki Improvements & Backlog

## Content Stubs to Flesh Out

- [ ] [`campaigns/Anthology/index.md`](file:///Users/efsa/Repos/charged/campaigns/Anthology/index.md): Empty index page; add overview text or framing for anthology adventures.
- [ ] [`directory/index.md`](file:///Users/efsa/Repos/charged/directory/index.md): Empty directory root; add gazetteer introduction or regional directory hub links.
- [ ] [`directory/Caravan1/index.md`](file:///Users/efsa/Repos/charged/directory/Caravan1/index.md): Thin stub (2 lines); add caravan composition, personnel, or history.

## Generator Files & Front Matter

- [ ] [`systems/perchance/`](file:///Users/efsa/Repos/charged/systems/perchance/): The four Perchance tables ([`chargedrpg_lhs.md`](file:///Users/efsa/Repos/charged/systems/perchance/chargedrpg_lhs.md), [`chargedrpg_rhs.md`](file:///Users/efsa/Repos/charged/systems/perchance/chargedrpg_rhs.md), [`chargedrpg-uvg_lhs.md`](file:///Users/efsa/Repos/charged/systems/perchance/chargedrpg-uvg_lhs.md), [`chargedrpg-uvg_rhs.md`](file:///Users/efsa/Repos/charged/systems/perchance/chargedrpg-uvg_rhs.md)) lack Jekyll front matter.
  - Option A: Leave as-is (they function as raw text/code snippets).
  - Option B: Add `exclude: [systems/perchance]` in [`_config.yml`](file:///Users/efsa/Repos/charged/_config.yml) so Jekyll skips them completely during site builds.

## Media Cleanup

- [ ] [`imgs/Screenshot 2025-05-12 at 17.53.24.png`](file:///Users/efsa/Repos/charged/imgs/Screenshot%202025-05-12%20at%2017.53.24.png): Unused screenshot in `imgs/`; verify whether it can be archived or deleted.

## Custom Skills & Environment

- [ ] Reference PDF Paths: Custom skills [`review-style`](file:///Users/efsa/Repos/charged/.agents/skills/review-style/SKILL.md) and [`weave-threads`](file:///Users/efsa/Repos/charged/.agents/skills/weave-threads/SKILL.md) point to `/Users/efsa/Library/CloudStorage/...`. If local directory paths or cloud storage mount points ever change, update the paths in those skill definitions.
