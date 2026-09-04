# Architecture Decision Record - Initial MVP Architecture

## Status

Proposed for Dev assessment.

## Context

The product needs two mobile apps, one admin web app and shared backend capabilities:

- SmartTro: renter app.
- SmartChu: owner app.
- SmartAdmin: admin web.
- Shared backend for auth, room/property data, booking, contracts, payments, notifications and files.

The current project resources include four repositories:

- `smart-platform`: documentation, skills and memory.
- `smart-tro`: SmartTro mobile app.
- `smart-chu`: SmartChu mobile app.
- `smart-admin`: SmartAdmin web app.

## Proposed Stack

| Layer | Proposed Technology | Decision |
| --- | --- | --- |
| SmartTro mobile | React Native + Expo | Suitable for MVP mobile delivery and shared mobile patterns. |
| SmartChu mobile | React Native + Expo | Suitable for owner workflows and future code reuse. |
| SmartAdmin web | Next.js + React + Tailwind | Suitable for admin dashboard and operational UI. |
| Backend | NestJS + TypeScript | Suitable for modular backend, REST APIs, WebSocket and typed contracts. |
| API style | REST + WebSocket | REST for core CRUD/workflows; WebSocket for realtime messaging/notifications. |
| Database | PostgreSQL | Source of truth for users, properties, rooms, bookings, contracts, invoices and payments. |
| Redis | Cache, queue, sessions | Use for jobs, retry queues, rate limits and temporary state. |
| Storage | S3 or Cloudinary | Store room images and contract PDFs. |
| Realtime/push | Socket.IO + FCM + SMS provider | Socket.IO for realtime app channels; FCM/SMS for offline notifications. |
| Auth | JWT + OAuth2 + RBAC | Support phone login, social login hooks and role-based access. |

## MVP Architecture Recommendation

Use a modular monolith backend first, not true microservices.

The backend should be a platform services monorepo with separate API entrypoints for renter, owner and admin audiences. It must not be treated as one undifferentiated backend app for all clients.

Recommended NestJS module boundaries:

- `auth`: phone login, OTP, OAuth2, JWT, RBAC.
- `users`: renter, owner, admin profile basics.
- `properties`: owner properties and rooms.
- `booking`: viewing requests and booking state transitions.
- `contracts`: contract lifecycle, signature, cancellation and PDF generation.
- `billing`: invoices, payment requests, payment history and ledger.
- `payment`: payment method linking, gateway redirect, webhook and retry.
- `notifications`: push, SMS, owner/renter notifications.
- `media`: image upload and document storage.
- `admin`: moderation, user/account controls and reporting endpoints.

Detailed module ownership, dependency, CRUD and public interface rules are defined in `docs/07-backend-module-boundaries.md`.

## Rationale

This keeps deployment and local development simple while allowing future module extraction if needed.

Benefits:

- Lower setup cost for MVP.
- Easier transaction handling across booking, contract and payment.
- Easier integration testing.
- Clear boundaries for future services.

Risks:

- Backend can become too large if module boundaries are not enforced.
- Payment and realtime logic need strict ownership to avoid coupling.
- Shared DTO/API contracts must be documented early to avoid FE/BE drift.
- Module boundaries must be enforced with public query, policy, command and event interfaces only. Direct repository/entity/schema imports across modules are forbidden.

## Required Dev Assessment Output

The Dev assessment should confirm or revise:

1. Whether Expo is sufficient for the mobile features, especially file upload, push notification and future e-signature UX.
2. Whether NestJS modular monolith is enough for MVP.
3. Recommended ORM/migration tooling.
4. Payment gateway abstraction and webhook handling strategy.
5. File storage approach for public images vs private contract PDFs.
6. Initial CI/CD and environment strategy.
