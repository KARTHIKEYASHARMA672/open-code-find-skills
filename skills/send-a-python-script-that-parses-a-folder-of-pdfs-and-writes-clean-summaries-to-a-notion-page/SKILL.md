# Send a Python script that parses a folder of PDFs and writes clean summaries to a Notion page

**Category:** automation | **Difficulty:** easy | **Est. time:** ~15 min | **Prerequisites:** Python 3.11+, the PDF files, Notion integration token

## Objective

The agent must deliver: a working send setup for a Python script that parses a folder of PDFs and writes clean summaries to a Notion page. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to send a Python script that parses a folder of PDFs and writes clean summaries to a Notion page and want it done quickly or automatically.

## Steps

1. Read the Objective: the automation to send a Python script that parses a folder of PDFs and writes clean summaries to a Notion page and its trigger source.
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
"Send a Python script that parses a folder of PDFs and writes clean summaries to a Notion page. Follow the steps in SKILL.md and deliver: the a Python script that parses a folder of PDFs and writes clean summaries to a Notion page. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing Python 3.11+, the PDF files, Notion integration token; verify on the first run; retry on failure; keep the output idempotent where possible.
