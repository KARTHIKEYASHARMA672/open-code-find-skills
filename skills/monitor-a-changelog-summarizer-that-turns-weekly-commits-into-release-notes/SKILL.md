# Monitor a changelog summarizer that turns weekly commits into release notes

**Category:** ops | **Difficulty:** easy | **Est. time:** ~15 min | **Prerequisites:** Git repo, AI API

## Objective

The agent must deliver: a working monitor setup for a changelog summarizer that turns weekly commits into release notes. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to monitor a changelog summarizer that turns weekly commits into release notes and want it done quickly or automatically.

## Steps

1. Read the Objective: what monitor a changelog summarizer that turns weekly commits into release notes must accomplish and the target environment.
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
"Monitor a changelog summarizer that turns weekly commits into release notes. Follow the steps in SKILL.md and deliver: the a changelog summarizer that turns weekly commits into release notes. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing Git repo, AI API; verify on the first run; retry on failure; keep the output idempotent where possible.
