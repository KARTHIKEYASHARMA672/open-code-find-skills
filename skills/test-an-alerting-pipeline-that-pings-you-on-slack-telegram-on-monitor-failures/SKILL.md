# Test an alerting pipeline that pings you on Slack/Telegram on monitor failures

**Category:** coding | **Difficulty:** easy | **Est. time:** ~20 min | **Prerequisites:** Slack/Telegram bot, uptime service

## Objective

The agent must deliver: a working test setup for an alerting pipeline that pings you on Slack/Telegram on monitor failures. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to test an alerting pipeline that pings you on Slack/Telegram on monitor failures and want it done quickly or automatically.

## Steps

1. Read the Objective: the deliverable is test an alerting pipeline that pings you on Slack/Telegram on monitor failures.
2. Create the project scaffold: directory, package.json/setup.py, and an entry file with the correct config.
3. Implement the core logic for an alerting pipeline that pings you on Slack/Telegram on monitor failures using the right stack; write the files with real content.
4. Add error handling, input validation, and a smoke-test command that verifies the core path.
5. Run the smoke test; fix any issues until it passes.
6. Write a README with setup + run instructions.

## Validation (how to verify it worked)

- [ ] Run the project (npm run dev / python main.py); it starts without errors.
- [ ] Run the smoke test; expect exit code 0 and the expected output.
- [ ] The README setup steps work on a fresh checkout.

## Example (handoff to an agent)

```text
"Test an alerting pipeline that pings you on Slack/Telegram on monitor failures. Follow the steps in SKILL.md and deliver: the an alerting pipeline that pings you on Slack/Telegram on monitor failures. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing Slack/Telegram bot, uptime service; verify on the first run; retry on failure; keep the output idempotent where possible.
