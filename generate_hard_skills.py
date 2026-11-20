"""Generate 1000 HARD, agent-ready skills for OpenCode (v2).

Unlike the first batch (v1), these skills are "hard": each SKILL.md is a
self-contained workflow for an agent to complete the task autonomously:
- Objective (what the agent must deliver)
- When to use it (triggers)
- Steps (concrete, with placeholders for real inputs)
- Validation (checklist to verify it worked)
- Example handoff (the prompt to give an agent)
- Notes / Edge cases

Run: python L:\nothing\nothing 1\generate_hard_skills.py
"""
import re
import shutil
from pathlib import Path

BASE = Path(r"L:\nothing\nothing 1\skills")

# (verb, category, difficulty, est. time)
VERBS = [
    ("Automate", "automation", "hard", "30 min"),
    ("Build", "coding", "medium", "30 min"),
    ("Deploy", "ops", "medium", "25 min"),
    ("Set up", "ops", "easy", "20 min"),
    ("Configure", "ops", "easy", "20 min"),
    ("Create", "coding", "medium", "30 min"),
    ("Fix", "ops", "medium", "25 min"),
    ("Refactor", "coding", "medium", "30 min"),
    ("Optimize", "coding", "medium", "30 min"),
    ("Integrate", "coding", "medium", "35 min"),
    ("Extract", "automation", "easy", "20 min"),
    ("Generate", "ai", "medium", "30 min"),
    ("Monitor", "ops", "easy", "15 min"),
    ("Alert", "ops", "easy", "20 min"),
    ("Backup", "ops", "easy", "15 min"),
    ("Test", "coding", "easy", "20 min"),
    ("Write", "coding", "easy", "25 min"),
    ("Send", "automation", "easy", "15 min"),
    ("Publish", "automation", "easy", "20 min"),
    ("Migrate", "coding", "hard", "40 min"),
    ("Patch", "ops", "easy", "15 min"),
    ("Harden", "ops", "medium", "30 min"),
    ("Install", "ops", "easy", "15 min"),
    ("Release", "ops", "medium", "25 min"),
    ("Scrape", "automation", "medium", "30 min"),
    ("Index", "docs", "easy", "20 min"),
    ("Benchmark", "ops", "medium", "25 min"),
    ("Tune", "ops", "medium", "25 min"),
    ("Verify", "coding", "easy", "15 min"),
    ("Ship", "ops", "medium", "20 min"),
    ("Review", "coding", "medium", "30 min"),
    ("Guard", "ops", "easy", "15 min"),
    ("Lint", "coding", "easy", "15 min"),
    ("Trace", "automation", "medium", "25 min"),
    ("Debug", "ops", "medium", "30 min"),
    ("Wrap", "coding", "easy", "20 min"),
    ("Inject", "docs", "easy", "15 min"),
    ("Instrument", "automation", "medium", "25 min"),
]

# (object description, prerequisites)
OBJECTS = [
    ("a Vercel CI/CD pipeline that auto-deploys the Next.js app on every push, runs build + tests, and posts preview URLs",
     "Next.js repo on GitHub, Vercel account, Node.js 18+"),
    ("a GitHub Actions workflow that lints and runs unit tests on every PR and blocks merge on failure",
     "JS/TS project with a linter + test script, GitHub Actions free minutes"),
    ("a Slack/Telegram webhook bot that forwards GitHub issues and PRs to chat with AI summaries",
     "Slack/Telegram bot token, GitHub repo, free-tier AI API key (Gemini/Groq/OpenAI)"),
    ("a Python script that parses a folder of PDFs and writes clean summaries to a Notion page",
     "Python 3.11+, the PDF files, Notion integration token"),
    ("a Node CLI tool that reads a JSON file and outputs formatted tables or CSV",
     "Node.js 18+, the JSON file"),
    ("a FastAPI endpoint that exposes a SQLite database over HTTP with auth",
     "Python 3.11+, the SQLite file"),
    ("a static site on GitHub Pages that lists all your projects with descriptions",
     "GitHub account, a repo with project data"),
    ("an MCP server that exposes your docs to OpenCode",
     "Node.js or Python, your docs"),
    ("a cron job that runs a Python script every hour and appends results to a CSV",
     "Cron access, the Python script, the output location"),
    ("a Chrome extension that summarizes the current article via a free-tier AI",
     "Browser, Chrome extension build steps"),
    ("a PostgreSQL migration tool that validates data before applying changes",
     "PostgreSQL, the migration files"),
    ("a Sentry-style error logger that captures and emails runtime errors",
     "Email account, the error source"),
    ("a data pipeline (Python/pandas) that reads a raw file, cleans it, and writes the final CSV",
     "Python 3.11+, the raw file"),
    ("a monitoring dashboard with alerts for a Vercel production app",
     "Vercel account, uptime service, a dashboard"),
    ("a backup job that copies your repo to a GitHub mirror daily",
     "Two GitHub repos, cron or Actions"),
    ("a test generator that creates unit tests from an existing module",
     "JS/TS or Python project with a test runner"),
    ("a search indexer that makes your docs searchable",
     "Docs source, hosting (Vercel/GitHub Pages)"),
    ("a dockerized Fastify API with health endpoints and graceful shutdown",
     "Node.js, Docker, a docker-compose file"),
    ("a PDF changelog generator from commit messages",
     "Git repo, git log, Python"),
    ("a Vercel log analyzer that finds errors in deployment logs",
     "Vercel CLI or API access"),
    ("a GitHub-to-Notion sync for issues and PRs",
     "Notion integration, GitHub repo"),
    ("a long-tail video render script using ffmpeg for your project videos",
     "ffmpeg installed, the video files"),
    ("a spreadsheet (TSV) export pipeline for data analysis",
     "Python + pandas, a CSV input"),
    ("a background job queue (Redis-based) for slow tasks",
     "Redis instance, a Python or Node worker"),
    ("a unit-test coverage dashboard for your CI",
     "jest/pytest + coverage tools"),
    ("an alerting pipeline that pings you on Slack/Telegram on monitor failures",
     "Slack/Telegram bot, uptime service"),
    ("a TypeScript utility for parsing and validating complex configs",
     "TypeScript, your configs"),
    ("a performance profiler for Node/Python endpoints",
     "Node.js or Python, the service"),
    ("a weekly research digest script using a search API",
     "Search API key (free tier), email"),
    ("a website Uptime/status page with page-specific checks",
     "Any hosting, health endpoints"),
    ("a GitHub Pages skill that renders your OpenAPI spec into docs",
     "OpenAPI spec, GitHub"),
    ("a desktop app wrapper for a web dashboard (Electron)",
     "Electron knowledge, a repo"),
    ("a robust API error handler that retries with exponential backoff",
     "Python/Node, the API"),
    ("a PDF merger/splitter utility for contract docs",
     "PDFs, pdfmerge tools"),
    ("a TypeScript CLI that uploads files to your Vercel Blob store",
     "Vercel account, the files"),
    ("a GitHub-to-Zod validation generator for your API schemas",
     "Your API spec"),
    ("a private n8n workflow module for the workflow you build often",
     "n8n installed"),
    ("a PR description generator that fills descriptions from the diff",
     "GitHub, your repo"),
    ("a GitHub Actions runner script that caches npm/pip installs",
     "CI setup"),
    ("a time-tracking CLI that logs task durations in a local JSONL",
     "Any project"),
    ("a log rotation + compaction script for your app logs",
     "Log files, storage"),
    ("an accessibility checker script that audits pages for issues",
     "Pages, axe rules"),
    ("a data model migrator with rollback + verification checks",
     "DB, migrations"),
    ("a CLI that generates test fixtures for your API from an OpenAPI spec",
     "OpenAPI spec"),
    ("a CLI help/README generator for your project",
     "Your project"),
    ("a Vercel speed-test script that compares deploy URLs",
     "Vercel accounts"),
    ("an API rate-limiter and circuit-breaker wrapper",
     "Node/Python, your APIs"),
    ("a Notion database that tracks your tasks + AI summarization skill",
     "Notion"),
    ("a GitHub Actions monthly spend analyzer",
     "GitHub Actions usage"),
    ("a CI cache warmer for your monorepo",
     "Monorepo, CI"),
    ("a PDF password remover/re-encryptor",
     "PDFs"),
    ("a broken-link checker that scans your docs",
     "Docs, tools"),
    ("a bug-triage assistant that summarizes issues by severity",
     "GitHub Issues, AI API"),
    ("a changelog summarizer that turns weekly commits into release notes",
     "Git repo, AI API"),
    ("a cost-tracker CLI that logs spend per service to a spreadsheet",
     "Spreadsheet, manual entry"),
    ("a data-quality checker for your raw datasets",
     "Datasets, pandas"),
    ("a migration verifier that compares pre/post data snapshots",
     "DBs"),
    ("an OpenAPI spec validator + docs sanity checker",
     "OpenAPI spec"),
    ("a Vercel preview URL health checker + comment poster",
     "Vercel, GitHub Actions"),
    ("a release drafter that creates release notes from merged PRs",
     "GitHub, git log"),
    ("a GitHub issue auto-labeler skill (AI-based) that works on PRs",
     "GitHub repo, AI API"),
    ("a retry + circuit-breaker pattern for resilient background jobs",
     "Python/Node, the job"),
    ("a self-updating docs generator that syncs README from code",
     "Git repo, your code"),
]

STEPS = {
    "coding": [
        "Read the Objective: the deliverable is {verb} {obj}.",
        "Create the project scaffold: directory, package.json/setup.py, and an entry file with the correct config.",
        "Implement the core logic for {obj} using the right stack; write the files with real content.",
        "Add error handling, input validation, and a smoke-test command that verifies the core path.",
        "Run the smoke test; fix any issues until it passes.",
        "Write a README with setup + run instructions.",
    ],
    "automation": [
        "Read the Objective: the automation to {verb} {obj} and its trigger source.",
        "Set up the automation framework: create the script/workflow file with the trigger (cron/webhook/event).",
        "Implement the automation logic: read input, transform/send, write the output artifact.",
        "Make it safe to re-run: add idempotency checks and retries with backoff.",
        "Test the automation with sample data; verify the output artifact appears.",
        "Document how the automation triggers and what it outputs.",
    ],
    "ai": [
        "Read the Objective: the AI task to {verb} {obj} and its inputs.",
        "Configure the AI tool (OpenCode/Claude/Gemini/OpenAI free tier) and set up API access.",
        "Implement the AI pipeline: prompts + tool calls with the exact task instructions.",
        "Add a verification script that runs the AI task on sample input and checks the output shape/content.",
        "Run it; fix issues until the output is correct; document the results.",
        "Schedule or wire it to run automatically (cron/endpoint) without manual help.",
    ],
    "ops": [
        "Read the Objective: what {verb} {obj} must accomplish and the target environment.",
        "Plan the ops change: identify tools, commands, and safety checks.",
        "Execute the plan step by step with the exact commands and paths from the plan.",
        "Verify the result: check the target state matches the objective.",
        "Record the change in a changelog/notes file and the rollback steps.",
    ],
    "devops": [
        "Read the Objective: what {verb} {obj} means and the environment.",
        "Configure the tooling (GitHub Actions/Vercel/Docker/CI) per best practice.",
        "Run the automation/deploy; check build, logs, and exit codes.",
        "Fix failures until the run is green.",
        "Verify a cold start works and artifacts are archived.",
        "Document the setup + how to re-run.",
    ],
    "docs": [
        "Read the Objective: the deliverable is {verb} {obj}.",
        "Set up the tooling (Docusaurus/Mintlify/GitHub Pages) per best practice.",
        "Write the docs content for {obj} with real, useful information.",
        "Add search + navigation; make sure pages are reachable.",
        "Deploy and verify the published docs work.",
        "Document how to update the docs in the future.",
    ],
}

VALID = {
    "coding": [
        "Run the project (npm run dev / python main.py); it starts without errors.",
        "Run the smoke test; expect exit code 0 and the expected output.",
        "The README setup steps work on a fresh checkout.",
    ],
    "automation": [
        "Run the automation once; confirm the expected output exists (file/email/message).",
        "Run it twice; confirm no duplicates or corrupt data.",
        "The trigger (cron/webhook/event) fires and the job completes without errors.",
    ],
    "ai": [
        "Run the AI task once on sample input; verify the output format/content.",
        "Run it a second time; check the response and error handling on bad input.",
        "The scheduled/continuous run produces a valid report each run.",
    ],
    "ops": [
        "Verify the target state: file/service/endpoint matches the objective.",
        "The rollback plan is documented and works.",
        "Monitoring/alerts still work; no regressions in health checks.",
    ],
    "devops": [
        "Trigger the CI/deploy; confirm green build + deploy + preview URL.",
        "Verify on a fresh run: re-run from scratch.",
        "Check notifications/artifacts are sent and present.",
    ],
    "docs": [
        "Open the published docs; all pages render without errors.",
        "The new docs appear in search results and navigation.",
        "Docs instructions are clear; the project owner can follow them.",
    ],
}


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def make_skill(name: str, cat: str, diff: str, time: str, verb: str, obj: str, prereq: str) -> str:
    v = verb.lower()
    steps = "\n".join(f"{i + 1}. " + s.format(verb=v, obj=obj, prereq=prereq) for i, s in enumerate(STEPS[cat]))
    valid = "\n".join(f"- [ ] {x.format(verb=v, obj=obj, prereq=prereq)}" for x in VALID[cat])
    artifact = f"the {obj}"
    return f"""# {name}

**Category:** {cat} | **Difficulty:** {diff} | **Est. time:** ~{time} | **Prerequisites:** {prereq}

## Objective

The agent must deliver: a working {v} setup for {obj}. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to {v} {obj} and want it done quickly or automatically.

## Steps

{steps}

## Validation (how to verify it worked)

{valid}

## Example (handoff to an agent)

```text
"{name}. Follow the steps in SKILL.md and deliver: {artifact}. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing {prereq}; verify on the first run; retry on failure; keep the output idempotent where possible.
"""


def main():
    shutil.rmtree(BASE, ignore_errors=True)
    BASE.mkdir(parents=True, exist_ok=True)
    skills = []
    seen = set()
    for verb, cat, diff, time in VERBS:
        for obj, prereq in OBJECTS:
            name = f"{verb} {obj}"
            if name in seen:
                continue
            seen.add(name)
            skills.append((name, cat, diff, time, verb, obj, prereq))
            if len(skills) >= 1000:
                break
        if len(skills) >= 1000:
            break
    assert len(skills) == 1000, len(skills)
    for name, cat, diff, time, verb, obj, prereq in skills:
        d = BASE / slug(name)
        d.mkdir(parents=True, exist_ok=True)
        (d / "SKILL.md").write_text(make_skill(name, cat, diff, time, verb, obj, prereq), encoding="utf-8")
    lines = [f"# Skills index ({len(skills)} skills, v2 - hard, agent-ready)\n"]
    for name, cat, diff, time, verb, obj, prereq in skills:
        lines.append(f"- [{name}](./{slug(name)}/SKILL.md) — {cat}")
    (BASE / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated {len(skills)} hard skills in {BASE}")
    for n, *_ in skills[:8]:
        print("  -", n)


if __name__ == "__main__":
    main()
