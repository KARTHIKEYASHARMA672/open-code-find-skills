# Deploy a PDF changelog generator from commit messages

**Category:** ops | **Difficulty:** medium | **Est. time:** ~25 min | **Prerequisites:** Git repo, git log, Python

## Objective

The agent must deliver: a working deploy setup for a PDF changelog generator from commit messages. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to deploy a PDF changelog generator from commit messages and want it done quickly or automatically.

## Steps

1. Read the Objective: what deploy a PDF changelog generator from commit messages must accomplish and the target environment.
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
"Deploy a PDF changelog generator from commit messages. Follow the steps in SKILL.md and deliver: the a PDF changelog generator from commit messages. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing Git repo, git log, Python; verify on the first run; retry on failure; keep the output idempotent where possible.
