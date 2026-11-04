# dbm-core-model

The shared building model of the course *Computer Science* (Digitaler Baumeister, THA, WS 2026/27).
The whole class builds one reference building here – as small JSON files that are checked automatically.

## Structure

| Folder | Content |
|---|---|
| `schema/` | `building_schema_v1.json` – the rules for our model |
| `data/project.json` | Project name |
| `data/materials/` | One file per material, e.g. `MAT-CONCRETE.json` |
| `data/buildups/` | One file per build-up (layers of materials), e.g. `BU-EXTWALL.json` |
| `data/building/` | The building with its storeys and spaces: `B-REF.json` |
| `data/elements/` | Walls, slabs and roof, grouped per file, e.g. `EG-exterior-walls.json` |
| `tools/` | `check.py` combines all files into `build/model.json` and validates it |
| `docs/` | Data dictionary |

## Rules

- The file name is the ID: `MAT-CONCRETE.json` contains `"id": "MAT-CONCRETE"`.
- IDs use capital letters, digits and hyphens only.
- Units are part of the field names: `density_kg_m3`, `thickness_m`, `area_m2`.
- Layers in a build-up go from outside to inside (walls) or from top to bottom (slabs, roof).

## How to contribute

1. Pick your issue and assign yourself.
2. Create a branch: `issue-<number>-<short-name>` (e.g. `issue-7-concrete`).
3. Make your change. Run the check:
   ```
   pip install jsonschema
   python tools/check.py
   ```
4. Commit, push and open a pull request. The template asks for the Definition of Done.
5. Your partner reviews. When the GitHub check is green and the review is approved: merge.

**Workflow for every issue: plan → implement → test.**
Write the code and data yourself – AI may explain, but not write your contribution.
