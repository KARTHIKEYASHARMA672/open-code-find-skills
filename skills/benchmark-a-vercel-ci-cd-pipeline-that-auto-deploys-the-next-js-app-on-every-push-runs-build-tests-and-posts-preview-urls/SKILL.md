# Benchmark a Vercel CI/CD pipeline that auto-deploys the Next.js app on every push, runs build + tests, and posts preview URLs

**Category:** ops | **Difficulty:** medium | **Est. time:** ~25 min | **Prerequisites:** Next.js repo on GitHub, Vercel account, Node.js 18+

## Objective

The agent must deliver: a working benchmark setup for a Vercel CI/CD pipeline that auto-deploys the Next.js app on every push, runs build + tests, and posts preview URLs. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to benchmark a Vercel CI/CD pipeline that auto-deploys the Next.js app on every push, runs build + tests, and posts preview URLs and want it done quickly or automatically.

## Steps

1. Read the Objective: what benchmark a Vercel CI/CD pipeline that auto-deploys the Next.js app on every push, runs build + tests, and posts preview URLs must accomplish and the target environment.
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
"Benchmark a Vercel CI/CD pipeline that auto-deploys the Next.js app on every push, runs build + tests, and posts preview URLs. Follow the steps in SKILL.md and deliver: the a Vercel CI/CD pipeline that auto-deploys the Next.js app on every push, runs build + tests, and posts preview URLs. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing Next.js repo on GitHub, Vercel account, Node.js 18+; verify on the first run; retry on failure; keep the output idempotent where possible.
