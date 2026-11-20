# Release a GitHub issue auto-labeler skill (AI-based) that works on PRs

**Category:** ops | **Difficulty:** medium | **Est. time:** ~25 min | **Prerequisites:** GitHub repo, AI API

## Objective

The agent must deliver: a working release setup for a GitHub issue auto-labeler skill (AI-based) that works on PRs. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to release a GitHub issue auto-labeler skill (AI-based) that works on PRs and want it done quickly or automatically.

## Steps

1. Read the Objective: what release a GitHub issue auto-labeler skill (AI-based) that works on PRs must accomplish and the target environment.
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
"Release a GitHub issue auto-labeler skill (AI-based) that works on PRs. Follow the steps in SKILL.md and deliver: the a GitHub issue auto-labeler skill (AI-based) that works on PRs. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing GitHub repo, AI API; verify on the first run; retry on failure; keep the output idempotent where possible.
