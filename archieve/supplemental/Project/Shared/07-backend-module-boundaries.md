# Backend Module Boundaries - Smart Platform Services

## Decision

Use a backend platform services repository, not one undifferentiated backend app.

Recommended repository role:

- Repository name: `smart-platform-services` or `smart-services`.
- Runtime style: NestJS modular monorepo.
- API entrypoints: renter API, owner API, admin API and worker.
- Core modules: identity, property, viewing, contract, billing, payment and audit.

`smart-platform` remains the documentation, skills and memory repository. Product runtime code must not be added to `smart-platform` unless PM explicitly changes its role.

## Domain Ownership

| Module | Owns | Does Not Own |
| --- | --- | --- |
| identity | immutable user ID, normalized unique email credential, email verification attempts, roles, sessions, auth, permissions, identity links and actor profile basics | property, viewing appointment, contract, invoice or payment lifecycle |
| property | properties, rooms, room inventory, owner-room ownership, room status | viewing appointment lifecycle, contracts, invoices, payments |
| viewing | multi-room viewing appointment, schedule lifecycle and per-room rental decision | room status, contract lifecycle, invoice/debt, payment transaction |
| contract | rental contract, official renter-owner-room binding, rent/deposit terms | invoice lifecycle, payment transaction, room master data |
| billing | invoices, invoice items, debt/outstanding balance, billing cycle, payment allocation | payment gateway transaction, provider callback, contract terms source |
| payment | payment intent, payment transaction, provider integration, webhook, reconciliation | invoice amount source, debt calculation, contract terms |
| audit | append-only security/business/data-change trail | business lifecycle mutation |

## Dependency Rules

1. API apps can call domain modules.
2. Domain modules cannot call API apps.
3. No module may import another module's repository, entity, schema or table.
4. Cross-module reads must use public query/policy services and return snapshots, not aggregates.
5. Cross-module mutations must use public command services or domain events.
6. Events carry minimal snapshots; consumers mutate only their own data.
7. `identity` is upstream and must not depend on business modules.
8. `audit` is sink-only and must not mutate business state.
9. `payment` must not mutate invoice/debt state directly; it must call billing.
10. `billing` must not mutate gateway/payment transaction state directly; it must call payment.

## CRUD Matrix

### Caller: identity

| Caller | Callee | R | C | U | D |
| --- | --- | --- | --- | --- | --- |
| identity | identity | Internal only | Internal only | Internal only | Internal only |
| identity | property | Forbidden | Forbidden | Forbidden | Forbidden |
| identity | viewing | Forbidden | Forbidden | Forbidden | Forbidden |
| identity | contract | Forbidden | Forbidden | Forbidden | Forbidden |
| identity | billing | Forbidden | Forbidden | Forbidden | Forbidden |
| identity | payment | Forbidden | Forbidden | Forbidden | Forbidden |
| identity | audit | N/A | `AuditLogService.recordSecurityEvent()`; events: `UserRegistered`, `UserRoleChanged`, `LoginSucceeded`, `LoginFailed` | Forbidden | Forbidden |

### Caller: property

| Caller | Callee | R | C | U | D |
| --- | --- | --- | --- | --- | --- |
| property | identity | `IdentityQueryService.getActorSnapshot()`; `IdentityAccessService.assertOwner()`; `IdentityAccessService.assertAdmin()` | Forbidden | Forbidden | Forbidden |
| property | property | Internal only | Internal only | Internal only | Internal only |
| property | viewing | Forbidden | Forbidden | Forbidden | Forbidden |
| property | contract | Forbidden | Forbidden | Forbidden | Forbidden |
| property | billing | Forbidden | Forbidden | Forbidden | Forbidden |
| property | payment | Forbidden | Forbidden | Forbidden | Forbidden |
| property | audit | N/A | `AuditLogService.recordBusinessEvent()`; events: `PropertyCreated`, `RoomCreated`, `RoomStatusChanged` | Forbidden | Forbidden |

### Caller: viewing

| Caller | Callee | R | C | U | D |
| --- | --- | --- | --- | --- | --- |
| viewing | identity | `IdentityQueryService.getActorSnapshot()`; `IdentityAccessService.assertRenter()`; `assertOwner()`; `assertAdmin()` | Forbidden | Forbidden | Forbidden |
| viewing | property | `PropertyQueryService.getRoomsBookableSnapshot()`; `PropertyPolicyService.assertRoomsBookable()`; `assertOwnerOwnsRooms()` | Forbidden | Event subscription only: `RoomStatusChanged`, `RoomDeleted`, `PropertyStatusChanged`, `PropertyDeleted` | Forbidden |
| viewing | viewing | Internal only | Internal only | Internal only | Internal only |
| viewing | contract | Forbidden | Forbidden; appointment does not create or consume Contract state | Forbidden | Forbidden |
| viewing | billing | Forbidden | Forbidden | Forbidden | Forbidden |
| viewing | payment | Forbidden | Forbidden | Forbidden | Forbidden |
| viewing | audit | N/A | `AuditLogService.recordBusinessEvent()`; events: `ViewingAppointmentRequested`, `ViewingAppointmentApproved`, `ViewingAppointmentRejected`, `ViewingAppointmentCancelled`, `ViewingAppointmentExpired`, `ViewingAppointmentEnded`, `ViewingAppointmentRoomUnavailable`, `ViewingAppointmentRoomDecisionChanged` | Forbidden | Forbidden |

### Caller: contract

| Caller | Callee | R | C | U | D |
| --- | --- | --- | --- | --- | --- |
| contract | identity | `IdentityQueryService.getActorSnapshot()`; `IdentityAccessService.assertRenter()`; `assertOwner()`; `assertAdmin()` | Forbidden | Forbidden | Forbidden |
| contract | property | `PropertyQueryService.getRoomContractSnapshot()`; `PropertyPolicyService.assertRoomAssignableToContract()`; `assertOwnerOwnsRoom()` | Forbidden | Event only: `ContractActivatedEvent`, `ContractTerminatedEvent`; property updates room occupancy | Forbidden |
| contract | viewing | `ViewingAppointmentQueryService.getSelectedRoomSource()`; `ViewingAppointmentPolicyService.assertRoomEligibleAsContractSource()` | Forbidden | Forbidden; Contract never mutates/consumes the appointment | Forbidden |
| contract | contract | Internal only | Internal only | Internal only | Internal only |
| contract | billing | Forbidden | Event only: `ContractActivatedEvent` for invoice schedule/first invoice | Event only: `ContractRentChangedEvent`, `ContractTerminatedEvent` | Forbidden |
| contract | payment | Forbidden | Forbidden | Forbidden | Forbidden |
| contract | audit | N/A | `AuditLogService.recordBusinessEvent()`; events: `ContractCreated`, `ContractActivated`, `ContractTerminated`, `ContractRentChanged` | Forbidden | Forbidden |

### Caller: billing

| Caller | Callee | R | C | U | D |
| --- | --- | --- | --- | --- | --- |
| billing | identity | `IdentityQueryService.getActorSnapshot()`; `IdentityAccessService.assertRenter()`; `assertOwner()`; `assertAdmin()` | Forbidden | Forbidden | Forbidden |
| billing | property | `PropertyQueryService.getRoomBillingSnapshot()` | Forbidden | Forbidden | Forbidden |
| billing | viewing | Forbidden | Forbidden | Forbidden | Forbidden |
| billing | contract | `ContractQueryService.getContractBillingTerms()`; `ContractPolicyService.assertContractBillable()` | Forbidden | Forbidden | Forbidden |
| billing | billing | Internal only | Internal only | Internal only | Internal only |
| billing | payment | `PaymentQueryService.getPaymentSnapshot()`; `PaymentQueryService.getPaymentStatus()` | `PaymentIntentService.createForInvoice()` or event `InvoiceIssuedEvent` if using event-driven intent creation | Forbidden | Forbidden |
| billing | audit | N/A | `AuditLogService.recordBusinessEvent()`; events: `InvoiceIssued`, `InvoicePaid`, `InvoicePartiallyPaid`, `InvoiceOverdue`, `DebtAdjusted` | Forbidden | Forbidden |

### Caller: payment

| Caller | Callee | R | C | U | D |
| --- | --- | --- | --- | --- | --- |
| payment | identity | `IdentityQueryService.getActorSnapshot()`; `IdentityAccessService.assertPayer()`; `assertAdmin()` | Forbidden | Forbidden | Forbidden |
| payment | property | Forbidden | Forbidden | Forbidden | Forbidden |
| payment | viewing | Forbidden | Forbidden | Forbidden | Forbidden |
| payment | contract | Forbidden | Forbidden | Forbidden | Forbidden |
| payment | billing | `BillingQueryService.getInvoicePayableSnapshot()`; `BillingPolicyService.assertInvoicePayable()`; `assertActorCanPayInvoice()` | Forbidden | `BillingPaymentService.allocateSuccessfulPayment()`; `BillingPaymentService.markPaymentFailedForInvoice()` | Forbidden |
| payment | payment | Internal only | Internal only | Internal only | Internal only |
| payment | audit | N/A | `AuditLogService.recordBusinessEvent()`; events: `PaymentInitiated`, `PaymentSucceeded`, `PaymentFailed`, `PaymentRefunded`, `PaymentReconciled` | Forbidden | Forbidden |

### Caller: audit

| Caller | Callee | R | C | U | D |
| --- | --- | --- | --- | --- | --- |
| audit | identity | `IdentityQueryService.getActorSnapshot()` only to enrich actor if event lacks snapshot | Forbidden | Forbidden | Forbidden |
| audit | property | Do not read aggregate; consume event snapshot only | Forbidden | Forbidden | Forbidden |
| audit | viewing | Do not read aggregate; consume event snapshot only | Forbidden | Forbidden | Forbidden |
| audit | contract | Do not read aggregate; consume event snapshot only | Forbidden | Forbidden | Forbidden |
| audit | billing | Do not read aggregate; consume event snapshot only | Forbidden | Forbidden | Forbidden |
| audit | payment | Do not read aggregate; consume masked event snapshot only | Forbidden | Forbidden | Forbidden |
| audit | audit | Internal only | Internal append-only | Internal only for metadata correction if required | Forbidden hard delete; retention/archive policy only |

## Public Interface Families

### identity

- Query: `IdentityQueryService.getActorSnapshot()`, `getActorsSnapshot()`
- Policy: `IdentityAccessService.assertRenter()`, `assertOwner()`, `assertAdmin()`, `assertPermission()`
- Commands: request/verify email OTP, create account after verification, authenticate email/password, refresh/logout sessions and link a future external identity without creating a duplicate user.
- Events: `EmailVerificationRequested`, `EmailVerified`, `UserRegistered`, `UserRoleChanged`, `LoginSucceeded`, `LoginFailed`
- MVP invariant: normalized email is the unique login identifier; phone is optional contact data and normal Sign In does not require OTP.

### property

- Query: `PropertyQueryService.getRoomBookableSnapshot()`, `getRoomContractSnapshot()`, `getRoomBillingSnapshot()`
- Policy: `PropertyPolicyService.assertRoomBookable()`, `assertOwnerOwnsRoom()`, `assertRoomAssignableToContract()`
- Commands: `PropertyCommandService.markRoomOccupiedFromContract()`, `markRoomAvailableFromContract()` as internal event handlers
- Events: `PropertyCreated`, `RoomCreated`, `RoomStatusChanged`

### viewing

- Query: `ViewingAppointmentQueryService.getAppointmentSnapshot()`, `getSelectedRoomSource()`
- Policy: `ViewingAppointmentPolicyService.assertScheduleEffective()`, `assertRoomEligibleAsContractSource()`
- Commands: renter/owner lifecycle commands and per-room decision commands only; no consume command
- Events: `ViewingAppointmentRequested`, `ViewingAppointmentApproved`, `ViewingAppointmentRejected`, `ViewingAppointmentCancelled`, `ViewingAppointmentExpired`, `ViewingAppointmentEnded`, `ViewingAppointmentRoomUnavailable`, `ViewingAppointmentRoomDecisionChanged`

### contract

- Query: `ContractQueryService.getActiveContract()`, `getContractBillingTerms()`, `getActiveContractByRoom()`
- Policy: `ContractPolicyService.assertContractBillable()`, `assertActorCanViewContract()`
- Commands: `ContractCommandService.createContractFromSelectedViewingRoom()`, `activateContract()`, `terminateContract()`
- Events: `ContractCreated`, `ContractActivated`, `ContractTerminated`, `ContractRentChanged`

### billing

- Query: `BillingQueryService.getInvoicePayableSnapshot()`, `getInvoiceStatus()`, `getOutstandingBalance()`
- Policy: `BillingPolicyService.assertInvoicePayable()`, `assertActorCanPayInvoice()`
- Commands: `BillingCommandService.issueInvoiceFromContract()`, `adjustDebt()`
- Payment commands: `BillingPaymentService.allocateSuccessfulPayment()`, `markPaymentFailedForInvoice()`
- Events: `InvoiceIssued`, `InvoicePaid`, `InvoicePartiallyPaid`, `InvoiceOverdue`, `DebtAdjusted`

### payment

- Query: `PaymentQueryService.getPaymentSnapshot()`, `getPaymentStatus()`
- Commands: `PaymentIntentService.createForInvoice()`, `PaymentCommandService.confirmManualPayment()`, `handleProviderWebhook()`, `refundPayment()`
- Events: `PaymentInitiated`, `PaymentSucceeded`, `PaymentFailed`, `PaymentRefunded`, `PaymentReconciled`

### audit

- Commands: `AuditLogService.recordSecurityEvent()`, `recordBusinessEvent()`, `recordDataChange()`
- Subscribe to security, business and data-change events
- Audit is append-only and never controls domain lifecycle.
