# Write a self-updating docs generator that syncs README from code

**Category:** coding | **Difficulty:** easy | **Est. time:** ~25 min | **Prerequisites:** Git repo, your code

## Objective

The agent must deliver: a working write setup for a self-updating docs generator that syncs README from code. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to write a self-updating docs generator that syncs README from code and want it done quickly or automatically.

## Steps

1. Read the Objective: the deliverable is write a self-updating docs generator that syncs README from code.
2. Create the project scaffold: directory, package.json/setup.py, and an entry file with the correct config.
3. Implement the core logic for a self-updating docs generator that syncs README from code using the right stack; write the files with real content.
4. Add error handling, input validation, and a smoke-test command that verifies the core path.
5. Run the smoke test; fix any issues until it passes.
6. Write a README with setup + run instructions.

## Validation (how to verify it worked)

- [ ] Run the project (npm run dev / python main.py); it starts without errors.
- [ ] Run the smoke test; expect exit code 0 and the expected output.
- [ ] The README setup steps work on a fresh checkout.

## Example (handoff to an agent)

```text
"Write a self-updating docs generator that syncs README from code. Follow the steps in SKILL.md and deliver: the a self-updating docs generator that syncs README from code. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing Git repo, your code; verify on the first run; retry on failure; keep the output idempotent where possible.
