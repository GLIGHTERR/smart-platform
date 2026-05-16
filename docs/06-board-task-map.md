# Board Task Map

## SmartPlatform Project Tasks

| Issue | Prefix | Title | Owner Type | Current Intent |
| --- | --- | --- | --- | --- |
| GLI-10 | SPF | Tech assessment FE/BE architecture | Dev | Validate architecture before implementation. |
| GLI-27 | SPF | Requirement traceability and scope cleanup | PM | Normalize requirements and assumptions. |
| GLI-12 | SPF | Backend foundation and database schema | Dev | Backend modules, database schema and migrations. |
| GLI-11 | SPF | Auth, OAuth2, OTP and RBAC | Dev | Shared authentication and authorization. |
| GLI-14 | SPF | App foundations for SmartTro and SmartChu | Dev | Shared mobile foundations for both apps. |
| GLI-13 | SMA | Web admin foundation | Dev | SmartAdmin base web shell. |
| GLI-16 | SMC | Owner property and room management | Dev | SmartChu owner property/room workflows. |
| GLI-17 | SMT | Renter room discovery and detail | Dev | SmartTro room search/detail/favorite flow. |
| GLI-15 | SPF | Booking room proposed flow | Dev | Cross-system booking workflow. |
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
3. GLI-16, GLI-17.
4. GLI-15, GLI-18.
5. GLI-20, GLI-22.
6. GLI-19, GLI-23.
7. GLI-21, GLI-24, GLI-25.
8. GLI-26, GLI-28 should run in parallel once enough implementation detail exists.

