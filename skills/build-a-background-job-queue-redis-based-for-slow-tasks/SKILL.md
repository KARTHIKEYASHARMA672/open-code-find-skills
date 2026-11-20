# Build a background job queue (Redis-based) for slow tasks

**Category:** coding | **Difficulty:** medium | **Est. time:** ~30 min | **Prerequisites:** Redis instance, a Python or Node worker

## Objective

The agent must deliver: a working build setup for a background job queue (Redis-based) for slow tasks. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to build a background job queue (Redis-based) for slow tasks and want it done quickly or automatically.

## Steps

1. Read the Objective: the deliverable is build a background job queue (Redis-based) for slow tasks.
2. Create the project scaffold: directory, package.json/setup.py, and an entry file with the correct config.
3. Implement the core logic for a background job queue (Redis-based) for slow tasks using the right stack; write the files with real content.
4. Add error handling, input validation, and a smoke-test command that verifies the core path.
5. Run the smoke test; fix any issues until it passes.
6. Write a README with setup + run instructions.

## Validation (how to verify it worked)

- [ ] Run the project (npm run dev / python main.py); it starts without errors.
- [ ] Run the smoke test; expect exit code 0 and the expected output.
- [ ] The README setup steps work on a fresh checkout.

## Example (handoff to an agent)

```text
"Build a background job queue (Redis-based) for slow tasks. Follow the steps in SKILL.md and deliver: the a background job queue (Redis-based) for slow tasks. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing Redis instance, a Python or Node worker; verify on the first run; retry on failure; keep the output idempotent where possible.
