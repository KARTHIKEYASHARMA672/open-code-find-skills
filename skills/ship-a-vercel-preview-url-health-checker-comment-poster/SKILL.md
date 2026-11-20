# Ship a Vercel preview URL health checker + comment poster

**Category:** ops | **Difficulty:** medium | **Est. time:** ~20 min | **Prerequisites:** Vercel, GitHub Actions

## Objective

The agent must deliver: a working ship setup for a Vercel preview URL health checker + comment poster. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to ship a Vercel preview URL health checker + comment poster and want it done quickly or automatically.

## Steps

1. Read the Objective: what ship a Vercel preview URL health checker + comment poster must accomplish and the target environment.
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
"Ship a Vercel preview URL health checker + comment poster. Follow the steps in SKILL.md and deliver: the a Vercel preview URL health checker + comment poster. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing Vercel, GitHub Actions; verify on the first run; retry on failure; keep the output idempotent where possible.
