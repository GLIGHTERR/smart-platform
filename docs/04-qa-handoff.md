# QA Handoff - Smart Platform MVP

## QA Role

QA should validate that implemented behavior matches:

1. PM issue comments.
2. Markdown handoff docs.
3. Requirement Lists.
4. User Stories and Acceptance Criteria.
5. BPMN/Activity/Use Case diagrams.
6. BRD business goals.

For UI tasks, QA must also follow `docs/10-ui-implementation-and-review-playbook.md` and the exact design node/capture named in the UC/task. A generic frame name or a locally reconstructed happy-case screen is not valid visual evidence.

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
| Auth/RBAC | Email normalization/unique identity, 6-digit email OTP activation, email/password Sign In without OTP on every login, state restore, duplicate-account prevention, negative/security and role access. |
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

## Auth QA Focus

QA must use the exact UC specification in `docs/use-cases/smarttro/` as the current baseline. For UC-01 and UC-02, cover:

- Email trim, lowercase/normalization and duplicate-account prevention.
- Sign Up: request OTP, input exactly 6 digits, invalid/expired/resend behavior and successful transition to password.
- App background/foreground while the user opens the email app: restore attempt, email, step and absolute countdown without persisting OTP/password.
- Registration success returns to Sign In and does not auto-login.
- Sign In uses email + password and does not ask for OTP in the normal flow.
- Generic credential errors do not reveal whether an email exists.
- Unverified account resumes activation rather than creating a duplicate account.
- Password/OTP do not appear in logs, route parameters or persistent storage.
- The environment under test uses the exact merged SHA and actual auth/mock contract, not an isolated happy-case setup.

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

For UI execution after merge, QA must additionally receive:

- Merged PR and exact merge SHA.
- Deployed environment/preview URL running that SHA.
- Exact Figma file/page/node or approved capture.
- Required states and responsive viewport matrix.
- Feature flag/environment contract and real test-data source.
- Known mock/review-only behavior and approved deviations.

QA must compare the deployed build side-by-side with the approved source, verify typography and Vietnamese rendering visually, and capture evidence for each required state/viewport. Do not report backend behavior as passed when the delivered scope is FE mock only.
