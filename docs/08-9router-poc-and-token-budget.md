# 9Router PoC and Token Budget Control

## Purpose

Evaluate 9Router as a local OpenAI-compatible routing layer before applying it to the main Codex PM, Codex DEV and Gemini QA agents.

The goal is to reduce avoidable token/cost usage for simple tasks without weakening execution quality for high-risk product work.

## Current PoC Status

Date: 2026-08-28

Issue: GLI-29

Current decision: do not apply 9Router to PM, DEV or QA yet.

What has been verified:

- Local 9Router endpoint is reachable at `http://127.0.0.1:20128`.
- `GET /v1/models` with an API key returns HTTP 200.
- Direct `POST /v1/responses` with `cx/gpt-5.4-mini` returns HTTP 200.
- Direct smoke output returned `PONG`.
- Direct smoke usage was about 2.5k total tokens.
- No API key or provider secret was committed or posted.

What remains risky:

- Agent task runs can still inject large system/project/skill context.
- A small read-only task through an experimental agent still reported `cx/gpt-5.6-sol` and about 259k input tokens before the agent model was pinned.
- Skills and project resources can dominate token usage even when the user-facing task is small.
- Runtime metadata may not expose the exact upstream route selected by 9Router.

## Experimental Agent

Agent name: `Router PoC Agent`

Rules:

- Use only for local PoC tasks.
- Do not use for production code changes.
- Do not change PM, DEV or QA configuration based on a single successful smoke test.
- Use custom env through stdin/file only.
- Keep max concurrency at `1`.
- Keep model pinned to a low-cost route while measuring small tasks, currently `cx/gpt-5.4-mini`.

## Routing Policy Draft

| Route | Suitable Work | Not Suitable For |
| --- | --- | --- |
| `pm-fast` | Board updates, short status reports, simple summaries, low-risk docs notes. | Architecture decision, scope negotiation, payment/contract/auth decisions. |
| `dev-fast` | Repo inventory, package script review, small lint/config fixes, simple scaffold checks. | Database migrations, auth, payment, contract, cross-module design. |
| `dev-deep` | Backend module boundaries, schema design, complex debugging, data consistency, high-risk refactors. | Routine comments or read-only summaries. |
| `qa-fast` | Test checklist drafts, smoke test notes, simple AC mapping. | Final release decision, security review, payment/contract regression sign-off. |

## Hard Safety Rules

Always use a strong/deep route for:

- Payment flow, money movement, refund, reconciliation or gateway webhook logic.
- Contract validity, digital signature and legal state changes.
- Authorization, RBAC, identity linking, OTP and session handling.
- Data deletion, irreversible state changes and migrations.
- Production deployment, secrets, environment management and incident response.

## PoC Measurement Template

For each test task, record:

- Issue ID and task type.
- Agent and configured model.
- HTTP/runtime outcome.
- Reported model in run usage, if available.
- Input, output, cache read and cache write tokens.
- Latency if visible.
- Whether the answer was usable, partially usable or not usable.
- Whether context injection or skill loading was unexpectedly large.

## Adoption Criteria

9Router can be applied to PM, DEV or QA only if:

1. Small tasks consistently run on the intended low-cost route.
2. Agent runs do not silently fall back to Sol for routine tasks.
3. Token usage is materially lower than the current default.
4. Output quality remains usable for at least 3 low-risk tasks.
5. There is a manual override path for high-risk work.
6. Secrets stay in provider/router/agent env storage, never in docs, comments or repo files.

## Current Recommendation

Continue the PoC, but narrow the next tests.

The next useful test is not another broad project issue. It should be a minimal, non-project-bound agent task with:

- No repository checkout.
- No attachment inspection.
- No document skill loading.
- A pinned low-cost model.
- A final run usage comparison against the direct smoke result.
