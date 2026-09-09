# Viewing Appointment MVP Rules

## Status

PO-approved baseline as of 2026-09-09 for `GLI-15` and its implementation children
`GLI-45`, `GLI-46` and `GLI-47`.

This document supersedes the original backend-foundation assumption that one `booking` belongs to
one room, can create at most one contract, and becomes `consumed` after contract creation.

## Business Boundary

- A viewing appointment schedules a renter to view one or more rooms in one property.
- It does not hold or reserve a room, collect a deposit, create/sign a contract, or change room
  occupancy.
- One appointment can contain from 1 to 10 rooms, all owned by the same owner and belonging to the
  same property.
- One appointment can later be the source of separate contracts for multiple rooms.
- Contract state is never copied into the appointment state.
- Public/API business naming is `ViewingAppointment`; the old `Booking`/`consumed` model is
  deprecated and must be migrated by `GLI-45`.

## Aggregate and Relationships

Recommended persistence model:

```text
viewing_appointments
  id
  property_id
  renter_id
  owner_id
  viewing_starts_at
  viewing_ends_at
  status
  decision_reason
  decided_by
  decided_at
  created_at
  updated_at

viewing_appointment_rooms
  id
  viewing_appointment_id
  room_id
  decision_status
  unavailable_reason
  created_at
  updated_at
```

Contracts created from the appointment store both:

- `source_viewing_appointment_id`
- `room_id`

Do not store a single `contract_id` on the appointment. Do not keep the foundation constraint
`contracts.booking_id UNIQUE` because it prevents one appointment from producing separate
contracts for several rooms.

## Appointment Lifecycle

| Status | Meaning | Schedule-effective |
| --- | --- | --- |
| `requested` | Renter submitted the appointment and owner has not decided. | Yes, only while `viewing_starts_at > now`. |
| `approved` | Owner approved the appointment and at least one room remains included. | Yes, only while `viewing_ends_at > now`. |
| `rejected` | Owner rejected the whole appointment. | No. |
| `cancelled` | Renter, owner or room-unavailability automation cancelled the appointment. | No. |
| `expired` | Appointment was still `requested` when its start time arrived. | No. |
| `ended` | The approved viewing window ended. This does not prove attendance or rental. | No. |

`consumed` is not a valid appointment status.

Allowed transitions:

| From | Actor | To | Required rules |
| --- | --- | --- | --- |
| new | renter | `requested` | All rooms are bookable, same property/owner, 1-10 rooms, valid future time window, idempotency and duplicate rules pass. |
| `requested` | owner | `approved` | Owner owns all included rooms; approval is before start; bookability and all conflicts are rechecked transactionally; owner may remove unavailable rooms with reason; at least one room remains. |
| `requested` | owner | `rejected` | Required reason, audit and both-party notification. |
| `requested`, `approved` | renter | `cancelled` | Renter owns appointment; required reason, audit and both-party notification. |
| `requested`, `approved` | owner | `cancelled` | Owner owns appointment rooms; required reason, audit and both-party notification. |
| `requested` | system | `expired` | `viewing_starts_at <= now`; reason code `APPROVAL_WINDOW_PASSED`; audit and both-party notification. |
| `approved` | system | `ended` | `viewing_ends_at <= now`; event/reason code `VIEWING_WINDOW_ENDED`; audit and both-party notification. |
| `approved` | system | `cancelled` | Every included room became unavailable; reason code `NO_BOOKABLE_ROOMS_REMAIN`; audit and both-party notification. |

Terminal appointment states are `rejected`, `cancelled`, `expired` and `ended`.

MVP does not track attendance or no-show. Reschedule is cancellation followed by a new request.

## Time Rules

- Store start/end in UTC and render using the client device timezone.
- `viewing_starts_at` must be later than the current server time.
- Duration applies to the whole multi-room appointment: minimum 60 minutes, maximum 180 minutes.
- There is no additional minimum lead time in MVP.
- Owner may approve only while `viewing_starts_at > now`.
- Intervals are half-open: `[start, end)`. Adjacent appointments such as 09:00-10:00 and
  10:00-11:00 do not overlap.
- The lifecycle worker must persist `expired`/`ended` within five minutes of the relevant boundary.
- Authorization, duplicate and conflict checks must use logical time effectiveness and must not rely
  on the worker having already persisted the terminal status.

## Duplicate, Merge and Conflict Rules

### Idempotent create

- Client provides an idempotency key for appointment creation.
- Repeating the same key with the same actor and payload returns the original result without a new
  appointment.
- Reusing the same key with a different payload returns conflict and does not mutate the original
  appointment.

### Effective duplicate

Reject a new room request when the same renter already has the same room in a schedule-effective
`requested` or `approved` appointment whose time interval overlaps.

Return HTTP `409` with code `EFFECTIVE_DUPLICATE_VIEWING_APPOINTMENT` and the conflicting
appointment ID when the actor is authorized to see it.

`rejected`, `cancelled`, `expired` and `ended` appointments do not block a new request.

### Same-property merge

- If the renter submits another room in the same property with exactly the same start and end as an
  existing effective `requested` appointment, add the room to that appointment, subject to the
  ten-room cap and bookability checks.
- If the intervals only overlap but do not match exactly, return conflict and ask the renter to edit
  or replace the existing request. Never silently union or intersect time windows.
- Rooms from different properties cannot be merged into one appointment.
- A room cannot be added after the appointment is `approved`. Create a new appointment instead.

### Approval conflicts

Approval must run transactionally. Excluding the appointment currently being approved, reject the
approval if the interval overlaps any schedule-effective `approved` appointment for:

- the renter, across every property and owner;
- the owner, across every room they own; or
- any room included in the appointment.

Pending appointments may coexist. A multi-room appointment does not conflict with its own rooms.
Cancellation, rejection and expiry release conflict eligibility immediately.

## Room Bookability and Status

Canonical MVP room statuses:

| Room status | Meaning | Owner may set directly | Bookable for viewing |
| --- | --- | --- | --- |
| `available` | Active vacant listing available for viewing/rental consideration. | Yes, subject to active-contract guard. | Yes. |
| `reserved` | Held by a later Contract/Deposit workflow. | No. | No. |
| `occupied` | Has an effective rental contract. | No. | No. |
| `maintenance` | Temporarily unavailable for maintenance. | Yes. | No. |
| `inactive` | Owner removed the room from active listing/use. | Yes. | No. |

No separate room `draft` status is required for MVP. A room-create operation must validate required
data before persistence; an unpublished complete room can use `inactive`.

A room is bookable only when all conditions are true:

```text
property.status = active
room.status = available
property.deleted_at IS NULL
room.deleted_at IS NULL
```

Backend validates bookability on direct API calls even when the client bypasses the listing UI. It
must revalidate at both request creation and owner approval.

Viewing appointment creation or approval never changes room status and never creates a hold.
`reserved` is owned by the later Contract/Deposit workflow; its exact trigger belongs to
`GLI-18`/`GLI-20` and is not implemented by `GLI-45`.

Self-booking is forbidden when the renter is also the owner of the property. Owner availability
calendars and ownership transfer are out of scope for MVP. If ownership changes unexpectedly, the
appointment cannot be approved and requires admin/manual resolution.

## Room Status Changes During an Appointment

### While requested

- Owner approval rechecks every room.
- Owner may remove unavailable rooms before approval, with one reason per removed room.
- If at least one room remains, owner may approve the remainder.
- If no room remains, approval fails; owner should reject the appointment with reason, or the system
  will eventually expire it.
- A soft-deleted property/room cannot be approved, but the appointment can still be cancelled or
  rejected/expired normally.

### After approval but before the viewing ends

When an included room becomes `reserved`, `occupied`, `maintenance`, `inactive`, or soft-deleted:

- mark only its appointment-room entry `unavailable`;
- record the originating room status/change reason;
- audit and notify renter and owner;
- keep the appointment approved if at least one room remains available; and
- cancel the appointment with `NO_BOOKABLE_ROOMS_REMAIN` if none remains.

If the room later becomes `available`, do not restore it automatically. Because an approved
appointment cannot add rooms, the renter must create a new appointment for that room. A room can be
added back only while the original appointment is still `requested` and the normal merge/bookability
rules pass.

Room-status updates and approval/contract checks must use transaction/locking or equivalent
concurrency controls so stale UI data cannot produce partial state.

## Per-Room Rental Decision

Each appointment-room has one decision status:

| Status | Meaning |
| --- | --- |
| `undecided` | Renter has not made a rental decision. |
| `selected` | Renter wants the owner to proceed toward a contract for this room. |
| `declined` | Renter does not want this room. |
| `unavailable` | Room cannot proceed because it became non-bookable. |

The decision is tracked per room, not for the whole appointment. Contract lifecycle/status is read
from the Contract module and is not duplicated in this enum.

For the MVP boundary, an owner may initiate the later Contract flow only for an appointment-room
that is `selected`, whose appointment has ended, whose room is still bookable for contract creation,
and which has no non-terminal contract for the same appointment and room. Exact Contract commands
and signing/deposit rules remain `GLI-18`/`GLI-20` scope.

If a previous contract for the same appointment and room is `cancelled`, `expired` or otherwise
terminal, a new contract may be created. At most one non-terminal contract may exist for the same
`source_viewing_appointment_id + room_id` pair.

## Permission Summary

| Action | Renter | Room owner | System | Contract module |
| --- | --- | --- | --- | --- |
| Create requested appointment | Own request | No | No | No |
| Add room to requested appointment | Own request, merge rules apply | No | No | No |
| Cancel | Own requested/approved appointment | Appointment for owned property | No | No |
| Approve/reject | No | Appointment for owned property | No | No |
| Remove unavailable room | No | Before approval; system event after approval | After room-status change | No |
| Expire/end | No | No | Yes | No |
| Set per-room decision | Own ended appointment | Read only | May set `unavailable` | Read only through boundary |
| Create contract | No | GLI-18 flow only | No | Revalidate selected source and room; never consume appointment |

Every actor decision/cancellation requires a nonblank reason, audit record and relevant
notification. System transitions use the machine reason/event codes specified above.

## API and Error Contract Requirements

`GLI-45` must document exact endpoints and DTOs, including:

- renter create/list/detail/cancel and per-room decision operations;
- owner list/detail/approve/reject/cancel and pre-approval room removal;
- multi-room request payload and room-level results;
- UTC timestamps and device-timezone rendering responsibility;
- idempotency behavior;
- lifecycle worker behavior;
- room-status event handling; and
- authorization failures without cross-tenant data leakage.

Minimum business error codes:

- `EFFECTIVE_DUPLICATE_VIEWING_APPOINTMENT`
- `VIEWING_TIME_CONFLICT`
- `ROOM_NOT_BOOKABLE`
- `PROPERTY_NOT_ACTIVE`
- `APPROVAL_WINDOW_PASSED`
- `INVALID_VIEWING_DURATION`
- `ROOM_LIMIT_EXCEEDED`
- `ROOMS_MUST_SHARE_PROPERTY_AND_OWNER`
- `IDEMPOTENCY_KEY_REUSED`
- `NO_BOOKABLE_ROOMS_REMAIN`
- `SELF_BOOKING_FORBIDDEN`

## Required Test Coverage

Dev must derive a test matrix from this document and cover at least:

- every allowed and forbidden lifecycle transition;
- logical expiry/end before and after the worker persists status;
- worker SLA behavior;
- 60/180-minute boundaries and past-time rejection;
- half-open interval adjacency;
- idempotent retry and key/payload mismatch;
- duplicate same renter/room;
- exact-time same-property merge and non-exact overlap conflict;
- renter, owner and room approval conflicts;
- multi-room partial approval/removal;
- room becoming unavailable before and after approval;
- last available room removal cancelling the appointment;
- soft delete and ownership authorization;
- self-booking denial;
- per-room decision isolation;
- multiple contracts sourced from one appointment;
- at-most-one non-terminal contract per appointment-room; and
- audit/notification hooks and reason validation.

Executable business logic added or changed by implementation must satisfy the project Dev coverage
gate before PR handoff. Post-merge QA must use the deployed merge commit, real API contracts and
upstream-produced room/property data; it must not substitute a detached happy-case environment.

## Implementation Dependencies and Order

1. `GLI-43` must provide the Property/Room query/policy/event boundary used by appointment
   bookability and room-status reactions.
2. `GLI-45` migrates the foundation schema/contracts and implements the Viewing Appointment backend.
3. `GLI-46` and `GLI-47` consume the finalized API contract.
4. After merge and deployment, QA validates API, both clients, multi-room integration and
   Property/Room regression before parent `GLI-15` proceeds to PO UAT.

`GLI-18` and `GLI-20` must be updated to remove the old consume-one-booking assumption and define
the exact `reserved`/deposit/activation trigger, but those downstream decisions do not block
Viewing Appointment implementation.
