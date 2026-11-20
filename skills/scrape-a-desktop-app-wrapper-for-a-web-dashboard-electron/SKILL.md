# Scrape a desktop app wrapper for a web dashboard (Electron)

**Category:** automation | **Difficulty:** medium | **Est. time:** ~30 min | **Prerequisites:** Electron knowledge, a repo

## Objective

The agent must deliver: a working scrape setup for a desktop app wrapper for a web dashboard (Electron). The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to scrape a desktop app wrapper for a web dashboard (Electron) and want it done quickly or automatically.

## Steps

1. Read the Objective: the automation to scrape a desktop app wrapper for a web dashboard (Electron) and its trigger source.
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
"Scrape a desktop app wrapper for a web dashboard (Electron). Follow the steps in SKILL.md and deliver: the a desktop app wrapper for a web dashboard (Electron). Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing Electron knowledge, a repo; verify on the first run; retry on failure; keep the output idempotent where possible.
