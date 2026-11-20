# Alert a GitHub Actions workflow that lints and runs unit tests on every PR and blocks merge on failure

**Category:** ops | **Difficulty:** easy | **Est. time:** ~20 min | **Prerequisites:** JS/TS project with a linter + test script, GitHub Actions free minutes

## Objective

The agent must deliver: a working alert setup for a GitHub Actions workflow that lints and runs unit tests on every PR and blocks merge on failure. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to alert a GitHub Actions workflow that lints and runs unit tests on every PR and blocks merge on failure and want it done quickly or automatically.

## Steps

1. Read the Objective: what alert a GitHub Actions workflow that lints and runs unit tests on every PR and blocks merge on failure must accomplish and the target environment.
2. Plan the ops change: identify tools, commands, and safety checks.
3. Execute the plan step by step with the exact commands and paths from the plan.
4. Verify the result: check the target state matches the objective.
5. Record the change in a changelog/notes file and the rollback steps.

## Validation (how to verify it worked)

- [ ] Verify the target state: file/service/endpoint matches the objective.
- [ ] The rollback plan is documented and works.
- [ ] Monitoring/alerts still work; no regressions in health checks.

## Example (handoff to an agent)

```text
"Alert a GitHub Actions workflow that lints and runs unit tests on every PR and blocks merge on failure. Follow the steps in SKILL.md and deliver: the a GitHub Actions workflow that lints and runs unit tests on every PR and blocks merge on failure. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing JS/TS project with a linter + test script, GitHub Actions free minutes; verify on the first run; retry on failure; keep the output idempotent where possible.
