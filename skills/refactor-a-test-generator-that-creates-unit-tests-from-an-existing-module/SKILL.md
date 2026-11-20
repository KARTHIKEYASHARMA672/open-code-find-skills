# Refactor a test generator that creates unit tests from an existing module

**Category:** coding | **Difficulty:** medium | **Est. time:** ~30 min | **Prerequisites:** JS/TS or Python project with a test runner

## Objective

The agent must deliver: a working refactor setup for a test generator that creates unit tests from an existing module. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to refactor a test generator that creates unit tests from an existing module and want it done quickly or automatically.

## Steps

1. Read the Objective: the deliverable is refactor a test generator that creates unit tests from an existing module.
2. Create the project scaffold: directory, package.json/setup.py, and an entry file with the correct config.
3. Implement the core logic for a test generator that creates unit tests from an existing module using the right stack; write the files with real content.
4. Add error handling, input validation, and a smoke-test command that verifies the core path.
5. Run the smoke test; fix any issues until it passes.
6. Write a README with setup + run instructions.

## Validation (how to verify it worked)

- [ ] Run the project (npm run dev / python main.py); it starts without errors.
- [ ] Run the smoke test; expect exit code 0 and the expected output.
- [ ] The README setup steps work on a fresh checkout.

## Example (handoff to an agent)

```text
"Refactor a test generator that creates unit tests from an existing module. Follow the steps in SKILL.md and deliver: the a test generator that creates unit tests from an existing module. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing JS/TS or Python project with a test runner; verify on the first run; retry on failure; keep the output idempotent where possible.
