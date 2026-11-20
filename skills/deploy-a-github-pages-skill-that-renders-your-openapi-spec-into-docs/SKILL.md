# Deploy a GitHub Pages skill that renders your OpenAPI spec into docs

**Category:** ops | **Difficulty:** medium | **Est. time:** ~25 min | **Prerequisites:** OpenAPI spec, GitHub

## Objective

The agent must deliver: a working deploy setup for a GitHub Pages skill that renders your OpenAPI spec into docs. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to deploy a GitHub Pages skill that renders your OpenAPI spec into docs and want it done quickly or automatically.

## Steps

1. Read the Objective: what deploy a GitHub Pages skill that renders your OpenAPI spec into docs must accomplish and the target environment.
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
"Deploy a GitHub Pages skill that renders your OpenAPI spec into docs. Follow the steps in SKILL.md and deliver: the a GitHub Pages skill that renders your OpenAPI spec into docs. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing OpenAPI spec, GitHub; verify on the first run; retry on failure; keep the output idempotent where possible.
