# Smart Platform - Project Overview

## Purpose

Smart Platform is a rental management and room discovery platform connecting renters, property owners and administrators.

The product addresses these business problems:

- Renters currently search rooms through fragmented channels such as social media, bulletin boards, brokers or direct contacts.
- Room information is often incomplete, hard to verify and hard to compare.
- Owners manage properties, rooms, contracts, incidents and payments manually or across separate tools.
- Payment tracking, incident handling and contract management lack transparency and traceability.

## Product Areas

| Area | User Group | Primary Goal |
| --- | --- | --- |
| SmartTro | Renter | Search rooms, book viewing schedules, sign contracts, pay rent, report incidents and track rental history. |
| SmartChu | Owner | Manage properties/rooms, bookings, contracts, tenants, incidents, payments and revenue. |
| SmartAdmin | Admin | Manage users, owners, content, violations and platform reporting. |
| Smart Platform Backend | System | Provide shared authentication, data, workflow, payment, notification and document services. |

## Current Documentation Sources

| Source | Location | Notes |
| --- | --- | --- |
| BRD | `BRD/BRD.xlsx` | Business context, scope, functional and non-functional requirements. |
| WBS | `WBS/WBS.xlsx` | Work breakdown and rough effort estimate. |
| Requirement Lists | `Requirement_List/` | Requirement IDs for SmartTro and SmartChu. |
| User Stories | `User_Stories/` | User story and acceptance criteria by module. |
| SRS | `SRS/` | Existing software requirement documents. |
| FRS | `FRS/` | Existing functional requirement documents. |
| Business Processes | `Business_Processes/` | Current/proposed BPMN images for payment and booking room. |
| Activity Diagrams | `Activity_Diagrams/` | Activity diagrams by feature. |
| Use Case Diagrams | `Use_Case_Diagrams/` | Use case diagrams by feature group. |

## Board Task Prefixes

| Prefix | Meaning |
| --- | --- |
| SPF | Smart Platform or cross-system task. Use when the task affects shared backend, architecture, data model, integrations, or multiple apps. |
| SMT | SmartTro app task. Use for renter-facing mobile app tasks. |
| SMC | SmartChu app task. Use for owner-facing mobile app tasks. |
| SMA | SmartAdmin web task. Use for admin web tasks. |

## MVP Implementation Principle

Start with architecture and requirement traceability before coding feature work.

Recommended first execution sequence:

1. `GLI-10` - Tech assessment FE/BE architecture.
2. `GLI-27` - Requirement traceability and scope cleanup.
3. `GLI-12` - Backend foundation and database schema.
4. `GLI-11` - Auth, OAuth2, OTP and RBAC.
5. `GLI-14` - App foundations for SmartTro and SmartChu.
6. Feature flows: room discovery, owner room management, booking, contract and payment.

