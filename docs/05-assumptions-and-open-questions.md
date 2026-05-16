# Assumptions and Open Questions

## Active Assumptions

| ID | Assumption | Impact | Owner |
| --- | --- | --- | --- |
| ASM-001 | `smart-platform` is a documentation, skills and memory repository, not a runtime app. | Dev should not put product code here unless it is documentation tooling. | PM |
| ASM-002 | SmartTro and SmartChu are separate mobile apps but should share backend API contracts and UX patterns where possible. | FE foundations should align on auth, API client and validation patterns. | Dev |
| ASM-003 | The backend should start as a NestJS modular monolith for MVP. | Simplifies deployment and cross-domain transactions. | Dev |
| ASM-004 | Payment, booking and contract are cross-system SPF workflows first. | Split into SMT/SMC/SMA subtasks after API/state contract is stable. | PM |
| ASM-005 | BPMN images are valid behavior sources even without editable BPMN files. | Dev/QA should read the image behavior and PM will translate if needed. | PM |
| ASM-006 | Latest Requirement Lists are the implementation ID source when BRD IDs conflict. | Prevents duplicate/legacy BRD IDs from blocking task execution. | PM |

## Open Questions

| ID | Question | Why It Matters | Suggested Default |
| --- | --- | --- | --- |
| OQ-001 | Which payment gateway/provider will be used for MVP? | Determines API integration, webhook signature, test sandbox and refund behavior. | Abstract payment provider behind backend interface until provider is selected. |
| OQ-002 | What is the exact rollback/refund rule when payment times out or gateway fails? | Money movement requires precise expected result. | Mark transaction failed/pending first; do not mark invoice paid until verified success webhook. |
| OQ-003 | Does deposit payment happen before or after both parties sign the electronic contract? | Booking proposed BPMN combines contract and deposit. | Generate deposit request after contract is valid for signing; finalize room booking after required payment success. |
| OQ-004 | What is the exact rule for a renter who already has an active contract? | Booking proposed BPMN checks existing active contract. | Allow new contract only after current contract cancellation is approved or old contract is inactive. |
| OQ-005 | Are social login CRs included in MVP or later release? | Affects auth scope and app store configuration. | Treat as priority 3 unless PM promotes it. |
| OQ-006 | Does SmartAdmin need full MVP implementation now or only foundation/moderation support? | Affects scope and timeline. | Start with foundation and moderation/reporting needed by SmartTro/SmartChu flows. |

## PM Analysis of Dev-Flagged Requirement Gaps

| Gap | PM Decision for MVP | Dev Impact | QA Impact |
| --- | --- | --- | --- |
| Legal level of electronic signature is unclear. | Treat MVP e-signature as in-app electronic consent with signature image, timestamp, signer identity, IP/device metadata and audit trail. Do not claim certified digital signature unless a certified provider is selected. | Build contract signature as an auditable platform workflow, not a government-grade digital signature integration. Keep provider abstraction open. | Test signature capture, signer identity, audit trail, immutable signed snapshot and permission access. Do not test legal certificate validation unless provider is added. |
| Payment gateway is not selected. | Use a payment provider abstraction for MVP. Payment business state must not depend on a specific gateway. | Define provider interface: create payment, verify webhook, query transaction, refund/rollback request. Implement mock/sandbox adapter first if needed. | Test against provider-independent state transitions and webhook contract; provider-specific test cases can be added later. |
| Payment retry/timeout/reconciliation is unclear. | Invoice/debt is paid only after verified success. Timeout should become pending or failed based on provider response; duplicate webhook must be idempotent. Refund/rollback must be explicitly logged. | Implement payment state machine and idempotency key before UI polish. | Required tests: duplicate callback, invalid callback, timeout, pending, success, failed, refund/rollback log. |
| RBAC matrix is not detailed. | Use minimum role matrix first: renter, owner, admin. Owner can manage only owned properties/rooms/contracts/payments. Renter can access only own bookings/contracts/payments/incidents. Admin can moderate and view platform data according to admin module scope. | Add policy layer/guards early; do not rely only on frontend route guards. | Test horizontal access control and role mismatch for every sensitive endpoint. |
| NFR/SLA is too broad. | Use BRD NFR as target, but MVP acceptance should focus on measurable baseline: page/API response, payment webhook reliability, daily backup, secure private documents. | Define logs, healthcheck and basic monitoring hooks early. Advanced load targets can be later. | Add smoke/performance checks for critical flows; full load testing waits until environment is ready. |
| SmartAdmin scope lacks detailed Requirement List. | For MVP, SmartAdmin starts with foundation, auth, user/content/report moderation support needed by SmartTro/SmartChu. Dashboard analytics can be phased later. | Build admin shell and moderation APIs only where they unblock reports/violations/accounts. | QA should test admin access, moderation workflow and auditability; not full analytics unless scoped. |

## Requirement Clarification Protocol

When Dev or QA finds unclear requirements:

1. Check BRD business goal.
2. Check Requirement List and User Story AC.
3. Check BPMN/Activity/Use Case diagrams.
4. Infer a default behavior if low-risk.
5. Comment the assumption on the task.
6. Ask PM before implementing/testing high-risk logic.

High-risk logic includes:

- Payment or refund.
- Contract signing or cancellation.
- Authorization and data privacy.
- Deleting data.
- State transitions that cannot be easily reversed.
