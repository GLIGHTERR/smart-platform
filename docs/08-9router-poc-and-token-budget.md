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
- 9Router API catalog exposes `cx/gpt-5.4-mini` and `cx/gpt-5.3-codex-spark`, even when the UI combo list is empty.
- An unprojected minimal agent task pinned to `cx/gpt-5.4-mini` completed successfully with no auth/runtime error.
- No API key or provider secret was committed or posted.

What remains risky:

- Agent task runs can still inject large system/project/skill context.
- A small read-only task through an experimental agent still reported `cx/gpt-5.6-sol` and about 259k input tokens before the agent model was pinned.
- Even after pinning a minimal unprojected agent task to `cx/gpt-5.4-mini`, the run still used about 74.7k input tokens and 41.5k cache-read tokens.
- Skills and project resources can dominate token usage even when the user-facing task is small.
- Runtime metadata may not expose the exact upstream route selected by 9Router.
- The current Codex default model in `~/.codex/config.toml` is `cx/gpt-5.6-sol`; agents with an empty model inherit that default.
- 9Router Combo UI is currently empty, so no UI-level fallback aliases have been configured yet.

## Experimental Agent

Agents:

- `Router PoC Agent`
- `Codex DEV Lite (9Router PoC)`

Rules:

- Use only for local PoC tasks.
- Do not use for production code changes.
- Do not change PM, DEV or QA configuration based on a single successful smoke test.
- Use custom env through stdin/file only.
- Keep max concurrency at `1`.
- Keep model pinned to a low-cost route while measuring small tasks, currently `cx/gpt-5.4-mini`.
- Do not change Codex PM, Codex DEV or Gemini QA until the adoption criteria are met.

## Routing Policy Draft

| Route | Suitable Work | Not Suitable For |
| --- | --- | --- |
| `pm-fast` | Board updates, short status reports, simple summaries, low-risk docs notes. | Architecture decision, scope negotiation, payment/contract/auth decisions. |
| `dev-fast` | Repo inventory, package script review, small lint/config fixes, simple scaffold checks. | Database migrations, auth, payment, contract, cross-module design. |
| `dev-deep` | Backend module boundaries, schema design, complex debugging, data consistency, high-risk refactors. | Routine comments or read-only summaries. |
| `qa-fast` | Test checklist drafts, smoke test notes, simple AC mapping. | Final release decision, security review, payment/contract regression sign-off. |

Recommended model mapping during PoC:

| Profile | Model | Use Now? |
| --- | --- | --- |
| `lite` | `cx/gpt-5.4-mini` | Yes, for controlled PoC agents only. |
| `normal` | `cx/gpt-5.4` or `cx/gpt-5.5` | Not yet; define after lite overhead is reduced. |
| `deep` | `cx/gpt-5.6-sol` | Keep for high-risk work and current defaults. |

Do not use the OpenAI-compatible `gpt/*` path as the primary fallback while its provider connection is reporting quota/backoff errors.

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

Continue the PoC, but change the next objective from "model selection" to "context reduction".

`cx/gpt-5.4-mini` works and is cheaper, but agent overhead remains high. The next useful test is a minimal, non-project-bound agent task with:

- No repository checkout.
- No attachment inspection.
- No document skill loading.
- A pinned low-cost model.
- A final run usage comparison against the direct smoke result.

If the run still starts above roughly 50k input tokens for a trivial task, do not roll out 9Router to PM, DEV or QA. First reduce injected context, default enabled plugins, or skill loading for the low-cost agent profile.
