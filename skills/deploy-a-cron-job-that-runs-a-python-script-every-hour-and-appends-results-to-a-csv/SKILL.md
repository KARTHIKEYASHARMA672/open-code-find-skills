# Deploy a cron job that runs a Python script every hour and appends results to a CSV

**Category:** ops | **Difficulty:** medium | **Est. time:** ~25 min | **Prerequisites:** Cron access, the Python script, the output location

## Objective

The agent must deliver: a working deploy setup for a cron job that runs a Python script every hour and appends results to a CSV. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to deploy a cron job that runs a Python script every hour and appends results to a CSV and want it done quickly or automatically.

## Steps

1. Read the Objective: what deploy a cron job that runs a Python script every hour and appends results to a CSV must accomplish and the target environment.
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
"Deploy a cron job that runs a Python script every hour and appends results to a CSV. Follow the steps in SKILL.md and deliver: the a cron job that runs a Python script every hour and appends results to a CSV. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing Cron access, the Python script, the output location; verify on the first run; retry on failure; keep the output idempotent where possible.
