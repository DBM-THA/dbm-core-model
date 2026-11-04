"""Check a building model file: first against schema v1, then the references between parts."""
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

model_file = sys.argv[1] if len(sys.argv) > 1 else str(Path(__file__).resolve().parent.parent / "build" / "model.json")
with open(Path(__file__).resolve().parent.parent / "schema" / "building_schema_v1.json", encoding="utf-8") as f:
    schema = json.load(f)
with open(model_file, encoding="utf-8") as f:
    model = json.load(f)

# 1. Schema: structure, types, allowed values
errors = [f"{' > '.join(map(str, e.absolute_path))}: {e.message}"
          for e in Draft202012Validator(schema).iter_errors(model)]

# 2. References: things a schema cannot check
if not errors:
    materials = {m["id"] for m in model["materials"]}
    buildups = {b["id"] for b in model["buildups"]}
    ids = [x["id"] for x in model["materials"] + model["buildups"]]
    for bu in model["buildups"]:
        for layer in bu["layers"]:
            if layer["material"] not in materials:
                errors.append(f"{bu['id']}: unknown material {layer['material']}")
    for b in model["buildings"]:
        ids.append(b["id"])
        for s in b["storeys"]:
            ids.append(s["id"])
            spaces = {sp["id"] for sp in s["spaces"]}
            ids += [sp["id"] for sp in s["spaces"]]
            for e in s["elements"]:
                ids.append(e["id"])
                if e["buildup"] not in buildups:
                    errors.append(f"{e['id']}: unknown build-up {e['buildup']}")
                for sp in e.get("bounds", []):
                    if sp not in spaces:
                        errors.append(f"{e['id']}: bounds unknown space {sp} on this storey")
    duplicates = {i for i in ids if ids.count(i) > 1}
    errors += [f"duplicate id {i}" for i in sorted(duplicates)]

if errors:
    print(f"validate: {len(errors)} problem(s)")
    for err in errors:
        print("  -", err)
    sys.exit(1)
print(f"validate: {Path(model_file).name} is valid (schema v1 and references)")
