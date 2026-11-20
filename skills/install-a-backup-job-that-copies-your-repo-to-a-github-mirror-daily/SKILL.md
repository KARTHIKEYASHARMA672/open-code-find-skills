# Install a backup job that copies your repo to a GitHub mirror daily

**Category:** ops | **Difficulty:** easy | **Est. time:** ~15 min | **Prerequisites:** Two GitHub repos, cron or Actions

## Objective

The agent must deliver: a working install setup for a backup job that copies your repo to a GitHub mirror daily. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to install a backup job that copies your repo to a GitHub mirror daily and want it done quickly or automatically.

## Steps

1. Read the Objective: what install a backup job that copies your repo to a GitHub mirror daily must accomplish and the target environment.
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
"Install a backup job that copies your repo to a GitHub mirror daily. Follow the steps in SKILL.md and deliver: the a backup job that copies your repo to a GitHub mirror daily. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing Two GitHub repos, cron or Actions; verify on the first run; retry on failure; keep the output idempotent where possible.
