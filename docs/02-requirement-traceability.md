# Requirement Traceability - Working Draft

## Purpose

This document gives Dev and QA a quick map from business artifacts to implementation tasks.

It does not replace the original BRD, Requirement Lists, User Stories, SRS or BPMN. It is a working bridge for implementation planning.

## Core Requirement Groups

| Requirement Group | SmartTro IDs | SmartChu IDs | Board Task |
| --- | --- | --- | --- |
| Auth and profile | SM001-SM009 | SM038-SM046 | `GLI-11`, `GLI-14` |
| Room/property discovery and management | SM013-SM016 | SM053-SM061 | `GLI-16`, `GLI-17` |
| Booking room / viewing schedule | SM017 | SM062-SM064 | `GLI-15` |
| Messaging and interaction | SM018-SM020 | SM065-SM068 | `GLI-19`, `GLI-21` |
| Incident management | SM022-SM026 | SM069-SM076 | `GLI-24` |
| Contract lifecycle | SM010-SM012 | SM047-SM052 | `GLI-18` |
| Payment and billing | SM027-SM033 | SM077-SM082 | `GLI-20`, `GLI-22`, `GLI-25` |
| Reporting/statistics | SM034-SM035 | SM083 | `GLI-25` |
| Admin foundation/moderation | N/A in current SmartTro/SmartChu lists | N/A in current SmartTro/SmartChu lists | `GLI-13`, `GLI-21` |
| QA planning | All groups | All groups | `GLI-26` |

## BPMN Coverage

| Process | Current Artifact | Proposed Artifact | Primary Task | Notes |
| --- | --- | --- | --- | --- |
| Payment | `Business_Processes/BP_Payment_Current.png` | `Business_Processes/BP_Payment_Proposed.png` | `GLI-20` | Proposed flow requires payment method linking, gateway redirect, webhook callback, success/failure handling and notification. |
| Booking Room | `Business_Processes/BP_Booking Room_Current.png` | `Business_Processes/BP_Booking Room_Proposed.png` | `GLI-15`, `GLI-18`, `GLI-20` | Proposed flow combines room discovery, viewing schedule, contract creation/signing and deposit generation. |

## Implementation Trace

| Board Task | Requirement Intent | Dev Output | QA Output |
| --- | --- | --- | --- |
| `GLI-10` | Validate proposed FE/BE architecture before implementation. | Architecture recommendation, risks, implementation order. | QA risk notes for high-risk areas. |
| `GLI-27` | Normalize requirements and assumptions before Dev/QA starts. | Requirement mapping and open questions. | Testability notes for ambiguous requirements. |
| `GLI-12` | Establish backend and database foundation. | NestJS modules, schema, migrations, seed roles. | DB/API smoke test scope. |
| `GLI-11` | Support auth and role access. | Auth APIs, JWT/OAuth2/RBAC, OTP behavior. | Auth happy/negative/security test cases. |
| `GLI-15` | Digitize booking room flow. | Booking APIs, state model, FE hooks/screens. | State transition test cases. |
| `GLI-18` | Support contract lifecycle and signature. | Contract APIs, PDF generation, signature/cancel flow. | Contract state, authorization and document test cases. |
| `GLI-20` | Digitize payment flow. | Payment method, invoice/debt payment, webhook, ledger. | Payment state, webhook idempotency and rollback test cases. |
| `GLI-26` | Create QA test plan. | N/A | Test plan and regression scope. |

## Known Traceability Risks

| Risk | Impact | PM Handling |
| --- | --- | --- |
| Some requirement IDs in previous BRD versions were duplicated or inconsistent. | Dev/QA may reference wrong IDs. | Use latest Requirement Lists as implementation IDs. Keep BRD IDs as business context only if inconsistent. |
| Payment flow has high business risk. | Incorrect payment status may affect money and trust. | Require explicit states: pending, success, failed, expired, refunded/rolled back where applicable. |
| Booking proposed flow combines multiple domains. | Large task may be hard to estimate and test. | Keep `GLI-15` as process/API contract task, then split UI/API subtasks if needed. |
| BPMN is image-only. | Dev cannot diff or edit source BPMN. | Use image as source of behavior; future update should store editable BPMN/drawio if possible. |

