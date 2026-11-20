# Generate an OpenAPI spec validator + docs sanity checker

**Category:** ai | **Difficulty:** medium | **Est. time:** ~30 min | **Prerequisites:** OpenAPI spec

## Objective

The agent must deliver: a working generate setup for an OpenAPI spec validator + docs sanity checker. The result should be complete, verified, and usable without further help.

## When to use this skill

- When you need to generate an OpenAPI spec validator + docs sanity checker and want it done quickly or automatically.

## Steps

1. Read the Objective: the AI task to generate an OpenAPI spec validator + docs sanity checker and its inputs.
2. Configure the AI tool (OpenCode/Claude/Gemini/OpenAI free tier) and set up API access.
3. Implement the AI pipeline: prompts + tool calls with the exact task instructions.
4. Add a verification script that runs the AI task on sample input and checks the output shape/content.
5. Run it; fix issues until the output is correct; document the results.
6. Schedule or wire it to run automatically (cron/endpoint) without manual help.

## Validation (how to verify it worked)

- [ ] Run the AI task once on sample input; verify the output format/content.
- [ ] Run it a second time; check the response and error handling on bad input.
- [ ] The scheduled/continuous run produces a valid report each run.

## Example (handoff to an agent)

```text
"Generate an OpenAPI spec validator + docs sanity checker. Follow the steps in SKILL.md and deliver: the an OpenAPI spec validator + docs sanity checker. Report back when done."
```

## Notes / Edge cases

- Edge cases: handle missing OpenAPI spec; verify on the first run; retry on failure; keep the output idempotent where possible.
