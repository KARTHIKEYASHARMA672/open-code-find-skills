# Configure a test generator that creates unit tests from an existing module

**Category:** ops | **Difficulty:** easy | **Est. time:** ~20 min | **Prerequisites:** JS/TS or Python project with a test runner

## Objective

The agent must deliver: a working configure setup for a test generator that creates unit tests from an existing module. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to configure a test generator that creates unit tests from an existing module and want it done quickly or automatically.

## Steps

1. Read the Objective: what configure a test generator that creates unit tests from an existing module must accomplish and the target environment.
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
"Configure a test generator that creates unit tests from an existing module. Follow the steps in SKILL.md and deliver: the a test generator that creates unit tests from an existing module. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing JS/TS or Python project with a test runner; verify on the first run; retry on failure; keep the output idempotent where possible.
