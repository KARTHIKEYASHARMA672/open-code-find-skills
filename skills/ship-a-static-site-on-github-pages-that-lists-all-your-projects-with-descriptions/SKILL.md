# Ship a static site on GitHub Pages that lists all your projects with descriptions

**Category:** ops | **Difficulty:** medium | **Est. time:** ~20 min | **Prerequisites:** GitHub account, a repo with project data

## Objective

The agent must deliver: a working ship setup for a static site on GitHub Pages that lists all your projects with descriptions. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to ship a static site on GitHub Pages that lists all your projects with descriptions and want it done quickly or automatically.

## Steps

1. Read the Objective: what ship a static site on GitHub Pages that lists all your projects with descriptions must accomplish and the target environment.
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
"Ship a static site on GitHub Pages that lists all your projects with descriptions. Follow the steps in SKILL.md and deliver: the a static site on GitHub Pages that lists all your projects with descriptions. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing GitHub account, a repo with project data; verify on the first run; retry on failure; keep the output idempotent where possible.
