# Configure a Python script that parses a folder of PDFs and writes clean summaries to a Notion page

**Category:** ops | **Difficulty:** easy | **Est. time:** ~20 min | **Prerequisites:** Python 3.11+, the PDF files, Notion integration token

## Objective

The agent must deliver: a working configure setup for a Python script that parses a folder of PDFs and writes clean summaries to a Notion page. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to configure a Python script that parses a folder of PDFs and writes clean summaries to a Notion page and want it done quickly or automatically.

## Steps

1. Read the Objective: what configure a Python script that parses a folder of PDFs and writes clean summaries to a Notion page must accomplish and the target environment.
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
"Configure a Python script that parses a folder of PDFs and writes clean summaries to a Notion page. Follow the steps in SKILL.md and deliver: the a Python script that parses a folder of PDFs and writes clean summaries to a Notion page. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing Python 3.11+, the PDF files, Notion integration token; verify on the first run; retry on failure; keep the output idempotent where possible.
