# Review a cost-tracker CLI that logs spend per service to a spreadsheet

**Category:** coding | **Difficulty:** medium | **Est. time:** ~30 min | **Prerequisites:** Spreadsheet, manual entry

## Objective

The agent must deliver: a working review setup for a cost-tracker CLI that logs spend per service to a spreadsheet. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to review a cost-tracker CLI that logs spend per service to a spreadsheet and want it done quickly or automatically.

## Steps

1. Read the Objective: the deliverable is review a cost-tracker CLI that logs spend per service to a spreadsheet.
2. Create the project scaffold: directory, package.json/setup.py, and an entry file with the correct config.
3. Implement the core logic for a cost-tracker CLI that logs spend per service to a spreadsheet using the right stack; write the files with real content.
4. Add error handling, input validation, and a smoke-test command that verifies the core path.
5. Run the smoke test; fix any issues until it passes.
6. Write a README with setup + run instructions.

## Validation (how to verify it worked)

- [ ] Run the project (npm run dev / python main.py); it starts without errors.
- [ ] Run the smoke test; expect exit code 0 and the expected output.
- [ ] The README setup steps work on a fresh checkout.

## Example (handoff to an agent)

```text
"Review a cost-tracker CLI that logs spend per service to a spreadsheet. Follow the steps in SKILL.md and deliver: the a cost-tracker CLI that logs spend per service to a spreadsheet. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing Spreadsheet, manual entry; verify on the first run; retry on failure; keep the output idempotent where possible.
