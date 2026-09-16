# Board Task Map

## SmartPlatform Project Tasks

| Issue | Prefix | Title | Owner Type | Current Intent |
| --- | --- | --- | --- | --- |
| GLI-10 | SPF | Tech assessment FE/BE architecture | Dev | Validate architecture before implementation. |
| GLI-27 | SPF | Requirement traceability and scope cleanup | PM | Normalize requirements and assumptions. |
| GLI-12 | SPF | Backend foundation and database schema | Dev | Backend modules, database schema and migrations. |
| GLI-11 | SPF | Email identity, OTP activation, OAuth2 and RBAC | Dev | Shared identity/authentication: unique normalized email, 6-digit email OTP for activation, email/password Sign In and safe future provider linking. |
| GLI-14 | SPF | App foundations for SmartTro and SmartChu | Dev | Shared mobile foundations for both apps. |
| GLI-13 | SMA | Web admin foundation | Dev | SmartAdmin base web shell. |
| GLI-16 | SMC | Owner property and room management | Dev | SmartChu owner property/room workflows. |
| GLI-17 | SMT | Renter room discovery and detail | Dev | SmartTro room search/detail/favorite flow. |
| GLI-15 | SPF | Viewing Appointment MVP parent specification/integration | PM/Dev/QA | Multi-room viewing schedule only; no hold, Contract or Payment state. |
| GLI-18 | SPF | Contract lifecycle and e-signature | Dev | Contract workflow and document handling. |
| GLI-20 | SPF | Payment proposed flow and billing ledger | Dev | Payment workflow, ledger and webhook. |
| GLI-22 | SPF | Automatic payment, reminders and notifications | Dev | Scheduled payment and notification behavior. |
| GLI-19 | SPF | Realtime messaging and push infrastructure | Dev | Messaging and push infrastructure. |
| GLI-21 | SPF | Review, ratings and violation reports | Dev/QA | Review and reporting workflow with admin moderation. |
| GLI-24 | SPF | Maintenance incident management | Dev/QA | Incident reporting and owner handling. |
| GLI-25 | SPF | Invoice, expense and revenue reporting | Dev/QA | Renter expense and owner revenue reports. |
| GLI-23 | SPF | File upload, media and document storage | Dev | Images and private contract files. |
| GLI-26 | SPF | QA test plan for MVP flows | QA | Test planning across MVP. |
| GLI-28 | SPF | CI, environment and deployment pipeline | Dev | Local/dev/QAS setup and CI/CD. |

## Recommended Execution Order

1. GLI-10, GLI-27.
2. GLI-12, GLI-11, GLI-14.
3. GLI-43 (Property/Room backend), then GLI-44 and GLI-17 as their contracts become available.
4. GLI-45 (Viewing Appointment backend), then GLI-46 and GLI-47.
5. Post-merge GLI-15 integration/QA; then GLI-18 after its source-appointment requirement is updated.
6. GLI-20, GLI-22 after the Contract/deposit trigger is explicit.
7. GLI-19, GLI-23.
8. GLI-21, GLI-24, GLI-25.
9. GLI-26, GLI-28 should run in parallel once enough implementation detail exists.

## GLI-15 Child Order

1. `GLI-43`: required Property/Room bookability snapshot, ownership policy and room-status event.
2. `GLI-45`: schema migration and Viewing Appointment lifecycle/API.
3. `GLI-46`: renter multi-room viewing UI and per-room decision UI.
4. `GLI-47`: owner review/partial-room handling and notification integration.
5. QA after merged code is deployed to Develop/Staging with the exact merge SHAs.
