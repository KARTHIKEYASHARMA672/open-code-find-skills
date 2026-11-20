"""Generate 500 unique AI/coding/automation skills for the opencode skills folder.

Each skill is a folder containing SKILL.md, written in Notion-style documentation
(headings, sections, bullets). Run: python L:\nothing\nothing 1\generate_skills.py
"""
from pathlib import Path

BASE = Path(r"L:\nothing\nothing 1\skills")
BASE.mkdir(parents=True, exist_ok=True)

# verb -> category
VERBS = [
    ("Automate", "automation", "advanced"), ("Build", "coding", "advanced"),
    ("Create", "coding", "medium"), ("Deploy", "ops", "medium"),
    ("Set up", "ops", "easy"), ("Configure", "ops", "easy"),
    ("Script", "automation", "medium"), ("Generate with AI", "ai", "advanced"),
    ("Migrate", "coding", "medium"), ("Refactor", "coding", "medium"),
    ("Scaffold", "coding", "easy"), ("Integrate", "coding", "medium"),
    ("Monitor", "ops", "easy"), ("Parse", "automation", "easy"),
    ("Convert", "docs", "easy"), ("Summarize", "docs", "easy"),
    ("Document", "docs", "easy"), ("Test", "coding", "easy"),
    ("Package", "ops", "easy"), ("Release", "ops", "medium"),
    ("Roll back", "ops", "medium"), ("Upgrade", "ops", "medium"),
    ("Cache", "ops", "medium"), ("Queue", "automation", "medium"),
    ("Poll", "automation", "easy"), ("Schedule", "automation", "easy"),
    ("Backup", "ops", "easy"), ("Restore", "ops", "easy"), ("Alert", "ops", "easy"),
    ("Scrape", "automation", "medium"), ("Crawl", "automation", "medium"),
    ("Index", "docs", "easy"), ("Benchmark", "ops", "medium"),
    ("Profile", "ops", "medium"), ("Tune", "ops", "advanced"),
    ("Guard", "ops", "easy"), ("Lint", "coding", "easy"),
    ("Optimize", "coding", "medium"), ("Visualize", "docs", "easy"),
    ("Extract", "automation", "easy"),
]

OBJECTS = [
    "a Vite SPA", "a React dashboard", "a Python scraper", "a PDF generator",
    "a webhook server", "a Python data pipeline", "an OpenCode skill",
    "an AI agent", "an MCP server", "a GitHub Actions CI pipeline",
    "a Node CLI tool", "a FastAPI endpoint", "a Vercel deployment",
    "a Next.js app", "a CI/CD pipeline", "a data-collection bot",
    "a report builder", "a portfolio site", "an error logger", "a cron job",
    "a Dockerized API", "a static site", "a TypeScript utility",
    "a chrome extension", "a data-migration script", "a chatbot",
    "a Slack bot", "a Telegram bot", "a Notion integration", "a SaaS auth flow",
    "a Redis cache layer", "a search indexer", "a test generator",
    "an auto-tagger", "a log parser", "a monitoring dashboard",
    "a code review bot", "an auto-deploy pipeline", "a daily report script",
    "a resume generator", "a Readme generator", "a webhook-based alert bot",
    "a TypeScript microservice", "a Fastify server", "a Postgres migration tool",
]

# 40 x 42 = 1680 combos; we take the first 500 in deterministic order.
def generate_skills():
    out, seen = [], set()
    for verb, cat, diff in VERBS:
        for obj in OBJECTS:
            name = f"{verb} {obj}"
            if name in seen:
                continue
            seen.add(name)
            out.append((name, cat, diff))
            if len(out) == 1000:
                return out
    return out

def slug(name):
    return name.lower().replace(" ", "-").replace("/", "-")

def skill_doc(name, cat, diff):
    steps = [
        "Set up the prerequisites and accounts.",
        "Plan the structure and key files.",
        "Implement the main " + name.split(" ", 1)[0].lower() + " logic step by step.",
        "Add tests or a quick smoke check.",
        "Deploy or run the result and verify it works.",
        "Document the steps and share the output.",
    ]
    steps_md = "\n".join(f"{i+1}. {s}" for i, s in enumerate(steps))
    return f"""# {name}

**Category:** {cat} | **Difficulty:** {diff} | **Time:** ~10 min | **Skill type:** coding/automation

## Description

A step-by-step skill to {name.lower()}. Written in Notion-style documentation with
sections for when to use it, the steps, and notes.

## When to use

- You want a reusable, repeatable way to {name.lower()}.
- The task keeps coming up, so having the steps saved here saves time.

## Steps

{steps_md}

## Notes

- Review the steps once to adapt them to your exact setup.
- Reuse the folder from `L:\\nothing\\nothing 1\\skills\\` as your template.
"""

skills = generate_skills()
assert len(skills) == 1000, len(skills)

for name, cat, diff in skills:
    d = BASE / slug(name)
    d.mkdir(parents=True, exist_ok=True)
    (d / "SKILL.md").write_text(skill_doc(name, cat, diff), encoding="utf-8")

# Index file listing all skills
lines = [f"# Skills index ({len(skills)} skills)\n"]
for name, cat, diff in skills:
    lines.append(f"- [{name}](./{slug(name)}/SKILL.md) — {cat}")
(BASE / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

print(f"Generated {len(skills)} skills in {BASE}")
