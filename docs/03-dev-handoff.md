# Dev Handoff - Smart Platform MVP

## How Dev Should Work

Use this order:

1. Read the task issue and PM comments.
2. Check this `docs/` folder for current assumptions and traceability.
3. Use original artifacts only when deeper detail is needed.
4. Ask PM only if the requirement cannot be inferred from BRD/user stories/BPMN.

## Source of Truth Priority

When documents conflict, apply this priority:

1. PM comment on the issue.
2. Latest Markdown handoff documents in this repo.
3. Requirement List IDs.
4. User Story and Acceptance Criteria.
5. BPMN/Activity/Use Case diagrams.
6. BRD business context.
7. WBS effort estimate.

## Requirement Ambiguity Rule

If a requirement is incomplete:

1. Infer expected behavior from BRD and user story intent.
2. Mark it as an assumption in your comment.
3. Continue assessment/design if the assumption does not block the task.
4. Stop and ask PM if the assumption affects money, contract validity, authorization or irreversible state changes.
5. Mention the QA impact in the same comment.

## Current High-Risk Areas

### Payment

Dev must define:

- Payment request state model.
- Invoice/debt state model.
- Gateway transaction state model.
- Webhook idempotency rule.
- Timeout/pending/failure behavior.
- Refund/rollback behavior.
- Notification timing for renter and owner.

Minimum recommended states:

- `payment_request.created`
- `payment_request.pending_gateway`
- `payment_request.success`
- `payment_request.failed`
- `payment_request.expired`
- `payment_request.refund_pending`
- `payment_request.refunded`

### Booking and Contract

Dev must define:

- Booking request state model.
- Viewing schedule conflict rule.
- Contract creation trigger.
- Contract active/inactive/cancel flow.
- Constraint for existing active contracts.
- Deposit generation trigger.

### Auth and RBAC

Dev must define:

- Roles: `renter`, `owner`, `admin`.
- OTP expiration and retry behavior.
- Failed login lockout behavior.
- JWT refresh/logout behavior.
- Social login linking behavior for Facebook, Google and Apple.

## Repository Responsibilities

| Repository | Responsibility |
| --- | --- |
| `smart-platform` | Documents, skills, memory, project-level artifacts. |
| `smart-tro` | Renter mobile app implementation. |
| `smart-chu` | Owner mobile app implementation. |
| `smart-admin` | Admin web implementation. |

## Branch and Commit Rule

Use the task ID in branch and commit naming.

Branch pattern:

```text
GLI-xx-short_task_name
```

Commit pattern:

```text
[GLI-xx] Short implementation summary
```

## Minimum Definition of Ready for Dev

A task is ready for implementation when it has:

- Scope.
- User role.
- Input/output behavior.
- API or screen expectation.
- State transitions if workflow-based.
- Permission rule.
- Acceptance criteria or testable expected result.

If any of these are missing, Dev should infer from BRD/user stories first, then notify PM if the gap is risky.

