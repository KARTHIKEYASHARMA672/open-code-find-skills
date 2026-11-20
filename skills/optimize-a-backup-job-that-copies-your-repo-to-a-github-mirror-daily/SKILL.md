# Optimize a backup job that copies your repo to a GitHub mirror daily

**Category:** coding | **Difficulty:** medium | **Est. time:** ~30 min | **Prerequisites:** Two GitHub repos, cron or Actions

## Objective

The agent must deliver: a working optimize setup for a backup job that copies your repo to a GitHub mirror daily. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to optimize a backup job that copies your repo to a GitHub mirror daily and want it done quickly or automatically.

## Steps

1. Read the Objective: the deliverable is optimize a backup job that copies your repo to a GitHub mirror daily.
2. Create the project scaffold: directory, package.json/setup.py, and an entry file with the correct config.
3. Implement the core logic for a backup job that copies your repo to a GitHub mirror daily using the right stack; write the files with real content.
4. Add error handling, input validation, and a smoke-test command that verifies the core path.
5. Run the smoke test; fix any issues until it passes.
6. Write a README with setup + run instructions.

## Validation (how to verify it worked)

- [ ] Run the project (npm run dev / python main.py); it starts without errors.
- [ ] Run the smoke test; expect exit code 0 and the expected output.
- [ ] The README setup steps work on a fresh checkout.

## Example (handoff to an agent)

```text
"Optimize a backup job that copies your repo to a GitHub mirror daily. Follow the steps in SKILL.md and deliver: the a backup job that copies your repo to a GitHub mirror daily. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing Two GitHub repos, cron or Actions; verify on the first run; retry on failure; keep the output idempotent where possible.
