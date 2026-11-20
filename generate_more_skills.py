r"""Add 1000 MORE hard, agent-ready skills on top of the existing ones (v3).

Reads the current skill folder, skips already-existing names, and generates the
next 1000 unique hard skills (same structure as v2). Writes the names of the
new skills to C:\Users\karth\new_skill_names2.json for the memory sync.

Run: python L:\nothing\nothing 1\generate_more_skills.py
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, r"L:\nothing\nothing 1")
from generate_hard_skills import make_skill, slug, VERBS, OBJECTS  # noqa: E402

BASE = Path(r"L:\nothing\nothing 1\skills")
NAMES_FILE = r"C:\Users\karth\new_skill_names2.json"


def main():
    existing = {d for d in os.listdir(BASE) if (BASE / d).is_dir()}
    generated = []
    seen = set()
    for verb, cat, diff, time in VERBS:
        for obj, prereq in OBJECTS:
            name = f"{verb} {obj}"
            s = slug(name)
            if s in existing or s in seen:
                continue
            seen.add(s)
            d = BASE / s
            d.mkdir(parents=True, exist_ok=True)
            (d / "SKILL.md").write_text(make_skill(name, cat, diff, time, verb, obj, prereq), encoding="utf-8")
            generated.append(s)
            if len(generated) >= 1000:
                break
        if len(generated) >= 1000:
            break
    assert len(generated) == 1000, len(generated)
    all_names = sorted(existing | set(generated))
    lines = [f"# Skills index ({len(all_names)} skills - v2 + v3)\n"]
    for n in all_names:
        lines.append(f"- [{n}](./{n}/SKILL.md)")
    (BASE / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    with open(NAMES_FILE, "w") as f:
        json.dump(generated, f)
    print(f"Added {len(generated)} new hard skills (total {len(all_names)} in folder)")
    print("First 3 new:", generated[:3])


if __name__ == "__main__":
    main()
