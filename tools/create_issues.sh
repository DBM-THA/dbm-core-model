#!/usr/bin/env bash
# Creates labels and all issues in the current GitHub repository.
# Needs the GitHub CLI (gh) and a login: gh auth login
set -e
gh label create round-1 --color 0E8A16 --description "Independent tasks" --force
gh label create round-2 --color D93F0B --description "Depends on round 1" --force
gh issue create --title "R1-01 Material: Reinforced concrete" --label round-1 --body-file issues/R1-01.md
gh issue create --title "R1-02 Material: Sand-lime brick" --label round-1 --body-file issues/R1-02.md
gh issue create --title "R1-03 Material: Mineral wool" --label round-1 --body-file issues/R1-03.md
gh issue create --title "R1-04 Material: Gypsum plaster" --label round-1 --body-file issues/R1-04.md
gh issue create --title "R1-05 Material: Cement screed" --label round-1 --body-file issues/R1-05.md
gh issue create --title "R1-06 Material: EPS insulation" --label round-1 --body-file issues/R1-06.md
gh issue create --title "R1-07 Material: Softwood timber" --label round-1 --body-file issues/R1-07.md
gh issue create --title "R1-08 Material: Gypsum board" --label round-1 --body-file issues/R1-08.md
gh issue create --title "R1-09 Data dictionary: building, storey, space" --label round-1 --body-file issues/R1-09.md
gh issue create --title "R1-10 Data dictionary: element, build-up, material" --label round-1 --body-file issues/R1-10.md
gh issue create --title "R2-01 Build-up: Exterior wall" --label round-2 --body-file issues/R2-01.md
gh issue create --title "R2-02 Build-up: Interior wall" --label round-2 --body-file issues/R2-02.md
gh issue create --title "R2-03 Build-up: Floor slab" --label round-2 --body-file issues/R2-03.md
gh issue create --title "R2-04 Build-up: Flat roof" --label round-2 --body-file issues/R2-04.md
gh issue create --title "R2-05 Spaces: ground floor" --label round-2 --body-file issues/R2-05.md
gh issue create --title "R2-06 Spaces: first floor" --label round-2 --body-file issues/R2-06.md
gh issue create --title "R2-07 Elements: EG exterior walls" --label round-2 --body-file issues/R2-07.md
gh issue create --title "R2-08 Elements: EG slab interior walls" --label round-2 --body-file issues/R2-08.md
gh issue create --title "R2-09 Elements: OG exterior walls" --label round-2 --body-file issues/R2-09.md
gh issue create --title "R2-10 Elements: OG slab roof interior walls" --label round-2 --body-file issues/R2-10.md
