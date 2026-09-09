# QA Handoff - Smart Platform MVP

## QA Role

QA should validate that implemented behavior matches:

1. PM issue comments.
2. Markdown handoff docs.
3. Requirement Lists.
4. User Stories and Acceptance Criteria.
5. BPMN/Activity/Use Case diagrams.
6. BRD business goals.

## Test Planning Priority

Prioritize tests by business risk:

1. Payment and billing.
2. Contract lifecycle and e-signature.
3. Booking room flow.
4. Auth/RBAC.
5. Room/property management.
6. Incident management.
7. Messaging/notifications.
8. Reports and admin moderation.

## Required Test Types

| Area | Required Test Types |
| --- | --- |
| Auth/RBAC | Functional, negative, security, role access. |
| Viewing Appointment | State transition, expiry/end worker, duplicate/merge/conflict, multi-room, room-status reaction, notification and Property/Room regression. |
| Contract | State transition, permission, document access, cancellation. |
| Payment | API, webhook, idempotency, rollback/refund, notification, regression. |
| Room/property | Functional, validation, image/media, permission. |
| Incident | Functional, status transition, notification. |
| Admin | Functional, authorization, moderation workflow. |

## Payment QA Focus

QA must cover:

- Payment method linking succeeds.
- Payment method linking fails.
- Manual payment success.
- Manual payment failure.
- Gateway timeout/pending.
- Duplicate webhook callback.
- Webhook callback with invalid signature.
- Payment success updates invoice/debt status exactly once.
- Payment failure does not mark invoice as paid.
- Rollback/refund rule is testable and logged.
- Renter and owner receive the correct notifications.

## Viewing Appointment QA Focus

QA must cover:

- Renter can view available rooms.
- Renter can view room detail.
- Renter can request a 1-10 room viewing appointment for one property.
- Renter cannot select invalid/past time.
- Effective duplicate, exact-time merge and half-open schedule conflict behavior.
- Owner approval checks renter, owner and every room transactionally.
- Room-status changes remove only affected rooms and cancel only when none remains.
- `requested` expires and `approved` ends within the worker SLA; no `consumed` state exists.
- Owner receives booking/viewing notification.
- Per-room renter decisions remain isolated; one appointment may source several contracts.
- Contract creation never changes the appointment lifecycle.
- Existing active contract behavior is handled.
- Deposit generation occurs only after valid contract/signing trigger.

## Contract QA Focus

QA must cover:

- Owner can create contract.
- Renter can view contract.
- Renter can sign contract.
- Owner can sign contract.
- Contract PDF access is protected.
- Contract cancellation request can be approved/rejected.
- Cancellation request expiration behavior.
- User cannot have invalid concurrent active contracts.

## Requirement Ambiguity Rule for QA

If expected result is unclear:

1. Infer expected behavior from BRD and the business goal.
2. Mark test case as assumption-based.
3. Ask PM before finalizing pass/fail if the behavior affects money, contract validity, authorization or data deletion.
4. Do not silently pass ambiguous behavior.

## Minimum Definition of Ready for QA

A task is ready for QA test case design when it has:

- User story or requirement ID.
- Clear acceptance criteria or expected result.
- State transitions if applicable.
- Test data requirements.
- Role/permission rule.
- Known out-of-scope items.
