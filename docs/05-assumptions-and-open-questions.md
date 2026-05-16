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

