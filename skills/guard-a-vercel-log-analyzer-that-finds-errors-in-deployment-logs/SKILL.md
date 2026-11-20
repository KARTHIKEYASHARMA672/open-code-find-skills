# Guard a Vercel log analyzer that finds errors in deployment logs

**Category:** ops | **Difficulty:** easy | **Est. time:** ~15 min | **Prerequisites:** Vercel CLI or API access

## Objective

The agent must deliver: a working guard setup for a Vercel log analyzer that finds errors in deployment logs. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to guard a Vercel log analyzer that finds errors in deployment logs and want it done quickly or automatically.

## Steps

1. Read the Objective: what guard a Vercel log analyzer that finds errors in deployment logs must accomplish and the target environment.
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
"Guard a Vercel log analyzer that finds errors in deployment logs. Follow the steps in SKILL.md and deliver: the a Vercel log analyzer that finds errors in deployment logs. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing Vercel CLI or API access; verify on the first run; retry on failure; keep the output idempotent where possible.
