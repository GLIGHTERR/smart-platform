# Smart Platform Documentation Repository

This repository stores project documentation, implementation handoff notes, requirement references and future agent memory/skill material for Smart Platform.

## Start Here

Read these files first:

1. `docs/00-project-overview.md`
2. `docs/01-architecture-decision-record.md`
3. `docs/02-requirement-traceability.md`
4. `docs/03-dev-handoff.md`
5. `docs/04-qa-handoff.md`
6. `docs/05-assumptions-and-open-questions.md`
7. `docs/06-board-task-map.md`
8. `docs/07-backend-module-boundaries.md`

## Source Artifacts

| Folder | Content |
| --- | --- |
| `BRD/` | Business Requirements Document. |
| `WBS/` | Work breakdown structure and estimates. |
| `Requirement_List/` | Requirement management files for SmartTro and SmartChu. |
| `User_Stories/` | User stories and acceptance criteria. |
| `SRS/` | Software Requirements Specifications. |
| `FRS/` | Functional Requirements Specifications. |
| `Business_Processes/` | Current/proposed business process images. |
| `Activity_Diagrams/` | Activity diagrams by feature. |
| `Use_Case_Diagrams/` | Use case diagrams by feature group. |
| `Workflow_Management/` | Delivery/output tracking workbook. |

## Board Prefixes

| Prefix | Meaning |
| --- | --- |
| SPF | Smart Platform / cross-system work. |
| SMT | SmartTro renter app. |
| SMC | SmartChu owner app. |
| SMA | SmartAdmin web. |

## Agent Working Rule

If a requirement is unclear, agents should infer the expected behavior from BRD and user stories first, then document the assumption. Ask PM before implementing or testing high-risk logic such as payment, contract validity, authorization, data deletion or irreversible state transitions.
