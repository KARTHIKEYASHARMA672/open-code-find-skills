# Publish an API rate-limiter and circuit-breaker wrapper

**Category:** automation | **Difficulty:** easy | **Est. time:** ~20 min | **Prerequisites:** Node/Python, your APIs

## Objective

The agent must deliver: a working publish setup for an API rate-limiter and circuit-breaker wrapper. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to publish an API rate-limiter and circuit-breaker wrapper and want it done quickly or automatically.

## Steps

1. Read the Objective: the automation to publish an API rate-limiter and circuit-breaker wrapper and its trigger source.
2. Set up the automation framework: create the script/workflow file with the trigger (cron/webhook/event).
3. Implement the automation logic: read input, transform/send, write the output artifact.
4. Make it safe to re-run: add idempotency checks and retries with backoff.
5. Test the automation with sample data; verify the output artifact appears.
6. Document how the automation triggers and what it outputs.

## Validation (how to verify it worked)

- [ ] Run the automation once; confirm the expected output exists (file/email/message).
- [ ] Run it twice; confirm no duplicates or corrupt data.
- [ ] The trigger (cron/webhook/event) fires and the job completes without errors.

## Example (handoff to an agent)

```text
"Publish an API rate-limiter and circuit-breaker wrapper. Follow the steps in SKILL.md and deliver: the an API rate-limiter and circuit-breaker wrapper. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing Node/Python, your APIs; verify on the first run; retry on failure; keep the output idempotent where possible.
