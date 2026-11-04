"""Combine the small data files into one model file: build/model.json.

Each material, build-up, building and element group lives in its own file,
so many people can work in parallel. This script puts them together.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "build" / "model.json"
errors = []


def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"{path.relative_to(ROOT)}: JSON syntax error in line {e.lineno}: {e.msg}")
        return None


def load_folder(folder):
    items = []
    for path in sorted((DATA / folder).glob("*.json")):
        item = load(path)
        if item is None:
            continue
        if item.get("id") != path.stem:
            errors.append(f"{path.relative_to(ROOT)}: id must be the file name ('{path.stem}'), found '{item.get('id')}'")
        items.append(item)
    return items


model = {
    "schema_version": "1.0",
    "project": load(DATA / "project.json") or {},
    "materials": load_folder("materials"),
    "buildups": load_folder("buildups"),
    "buildings": load_folder("building"),
}

# Elements are stored per file and inserted into their storey.
storeys = {s["id"]: s for b in model["buildings"] for s in b.get("storeys", [])}
for s in storeys.values():
    s.setdefault("elements", [])
for path in sorted((DATA / "elements").glob("*.json")):
    group = load(path)
    if group is None:
        continue
    storey = storeys.get(group.get("storey"))
    if storey is None:
        errors.append(f"{path.relative_to(ROOT)}: unknown storey '{group.get('storey')}'")
        continue
    storey["elements"].extend(group.get("elements", []))

if errors:
    print("assemble: problems found")
    for err in errors:
        print("  -", err)
    sys.exit(1)

OUT.parent.mkdir(exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(model, f, indent=2, ensure_ascii=False)
n_spaces = sum(len(s.get("spaces", [])) for s in storeys.values())
n_elements = sum(len(s["elements"]) for s in storeys.values())
print(f"assemble: {len(model['materials'])} materials, {len(model['buildups'])} build-ups, "
      f"{len(storeys)} storeys, {n_spaces} spaces, {n_elements} elements -> build/model.json")
