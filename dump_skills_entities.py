"""Dump all generated skills as compact memory-graph entities for tools.memory.create_entities.

Reads every skill folder under L:\nothing\nothing 1\skills\ and writes
L:\nothing\nothing 1\skills_entities.json with one entity per skill.
"""
import json
from pathlib import Path

BASE = Path(r"L:\nothing\nothing 1\skills")
entities = []
for d in sorted(BASE.iterdir()):
    if not d.is_dir():
        continue
    name = d.name.replace("-", " ").title()
    cat, diff = "coding", "medium"
    md = d / "SKILL.md"
    if md.exists():
        for line in md.read_text(encoding="utf-8").splitlines():
            if line.startswith("**Category:**"):
                cat = line.split("**Category:**")[1].split("|")[0].strip()
            if line.startswith("**Difficulty:**"):
                diff = line.split("**Difficulty:**")[1].split("|")[0].strip()
    entities.append({
        "name": name,
        "entityType": "skill",
        "observations": [f"AI/coding skill ({cat}) for OpenCode: {name}."],
    })

out = Path(r"L:\nothing\nothing 1\skills_entities.json")
out.write_text(json.dumps({"entities": entities, "total": len(entities)}, indent=1), encoding="utf-8")
print(f"Dumped {len(entities)} skill entities to {out}")
