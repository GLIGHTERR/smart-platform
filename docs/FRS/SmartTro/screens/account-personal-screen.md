# SmartTro - UC-04 Account / Personal Living Specification

## 1. Document control

| Attribute | Value |
| --- | --- |
| Product | SmartTro |
| Use case | UC-04 - Xem thong tin ca nhan |
| Requirement traceability | SM006, US 4.0, Home action `Tai khoan` |
| Status | PO visual/profile decisions recorded 2026-10-06; API/data decisions remain explicitly deferred |
| Canonical visual evidence | Three PO-approved captures attached to GLI-106: 0 active contracts, 1 active contract, 2 active contracts |
| Review viewport | Mobile portrait 375 x 812 |

This document is the living specification for viewing the signed-in renter's own
account details. It does not implement UC-05 (edit profile), UC-06 (change
password), profile persistence, or a backend profile endpoint.

## 2. Scope and boundaries

### 2.1 In scope

- A signed-in renter opens UC-04 from Home action `Tai khoan`.
- Account header, persistent `Ca nhan` and `Chu ky` tabs, personal-information
  card, and the approved rental-summary variants.
- Navigation-only edit action to UC-05, navigation-only `Doi mat khau` action
  to UC-06, and the existing sign-out flow.
- Display masking, avatar fallback, loading/error/session safety, accessibility,
  and responsive scrolling behavior described here.

### 2.2 Out of scope

- Editing profile data, changing a password, changing a contract, or rendering
  signature content.
- Defining a new backend endpoint, ownership model, cache policy, or database
  migration.
- Any field not listed as approved for display in the decision matrix.

## 3. PO decision matrix

| Decision | PO decision | Result / impact |
| --- | --- | --- |
| Tabs | APPROVED | `Ca nhan` and `Chu ky` are always visible, regardless of active-contract count. |
| Layout | APPROVED | The full screen scrolls; bottom actions belong to the scroll-safe layout and must not be obscured by safe areas. |
| Phone | APPROVED | Display only the last three digits. |
| Email mask | APPROVED | Keep the domain. For local part length >= 3: first character + `***` + last character. For length 2: first character + `*`. For length 1: `*`. Do not log raw email or pre-mask values in analytics/UI diagnostics. |
| Avatar | APPROVED | Nullable. For null, empty value, or image-load error, use a white circular placeholder with the installed Ant Design React Native outline `user` glyph; an empty white circle is the last fallback. Do not log avatar URL. |
| Rental states | APPROVED | 0 active: hide `Dang thue`; 1 active: `Dang thue . 1` and one summary card without pagination; 2+: `Dang thue . N`, horizontally swipeable carousel, one card per page, and accessible actual-count indicator. |
| Rental card | APPROVED | Show only `Phong`, `Nha tro`, and `Het han`; no contract-edit content. |
| Multi-contract order | APPROVED | Sort by `signedAt` ascending; tie-break by `contractId` ascending. Do not sort UC-04 by expiry date. |
| Active contract | APPROVED | Reuse Home meaning: still in term and not deactivated by backend/owner, unless a later PO decision supersedes it. |
| Visual source | APPROVED | The three GLI-106 captures are canonical visual evidence for 0, 1, and 2 active contracts; no separate Figma file/node is required for G0. |
| Edit/change-password/sign-out | APPROVED | Edit icon navigates only to UC-05; `Doi mat khau` navigates only to UC-06; `Dang xuat` uses the existing sign-out flow. |
| MVP field set and source ownership | OPEN / deferred | No FE/BE implementation may infer additional display fields from legacy SRS or database schema. |
| Profile API, field nullability/defaults | OPEN / deferred | Backend profile response remains a G3 contract decision; current actor/session endpoints are insufficient. |
| Address/emergency-contact privacy and cache policy | OPEN / deferred | Do not render, log, analyse, or cache these fields until an explicit decision exists. |

## 4. Information presentation

### 4.1 Personal information card

The canonical captures show display name, masked phone, masked email, and avatar
placement. They establish presentation only; the approved API field set and
source ownership are deferred. Every displayed value must be sourced from the
authenticated subject only.

For visual parity, the avatar fallback has an accessible label that identifies it
as the account avatar placeholder. The account's name, masked phone, and masked
email must each remain programmatically available to assistive technology without
exposing unmasked contact values.

### 4.2 Rental region

The rental region is separate from the personal-information card.

| Active contracts | Expected presentation |
| --- | --- |
| 0 | Do not render `Dang thue` or a rental card. |
| 1 | Render `Dang thue . 1` and one stable-height card. Do not render pagination. |
| 2+ | Render `Dang thue . N`, a horizontally swipeable, stable-height carousel, and an accessible page/count indicator. |

Each summary card displays `Phong`, `Nha tro`, and `Het han`. For 2+ records,
the list is ordered by `signedAt` ascending and then `contractId` ascending.

## 5. Runtime and security states

| State | Expected UX | Safety requirement |
| --- | --- | --- |
| Initial loading | Preserve layout with an accessible loading state. | Do not show prior subject's data. |
| Ready / partial | Render only approved fields with approved masks/fallbacks. | Do not treat missing JSON/object data as displayable content. |
| Empty rental | Omit the rental region. | Distinguish no active contracts from an unavailable profile response. |
| Retryable error / timeout | Provide a retryable, non-sensitive error state. | Do not surface raw backend errors or PII. |
| Offline / failed refresh | Exact cache/stale policy is deferred. | Do not introduce PII cache behavior before its contract is approved. |
| Session expired, revoked, inactive, or subject mismatch | Run the common session-expired/sign-out behavior. | Clear per-user profile/rental state; never retain or render another user's data. |

## 6. Acceptance criteria

### AC-04-01 - Entry and subject authorization

- **Given** a signed-in renter is on Home
- **When** the renter selects `Tai khoan`
- **Then** the app opens UC-04 for the access-token subject only
- **And** no client-controlled user identifier may select another profile.

### AC-04-02 - Account chrome and scroll safety

- **Given** UC-04 renders at an approved viewport
- **When** content exceeds the viewport height
- **Then** the screen scrolls without clipping or fixed-height assumptions
- **And** `Ca nhan`, `Chu ky`, edit, `Doi mat khau`, and `Dang xuat` remain reachable without being hidden by a safe area.

### AC-04-03 - Contact masking and avatar fallback

- **Given** UC-04 renders approved contact fields
- **When** email local part has length 1, 2, or at least 3
- **Then** it is masked using the approved rule and keeps its domain
- **And** phone shows only its last three digits.
- **Given** avatar is null, empty, or fails to load
- **Then** the accessible `user`-glyph placeholder is rendered
- **And** no raw email or avatar URL is written to analytics/UI diagnostics.

### AC-04-04 - Rental variants

- **Given** the authenticated renter has zero active contracts
- **When** UC-04 is ready
- **Then** `Dang thue` is absent.
- **Given** exactly one active contract
- **Then** `Dang thue . 1` and one rental card are shown without pagination.
- **Given** two or more active contracts
- **Then** cards are swipeable one at a time, have stable height, and expose the actual count/page accessibly
- **And** records are ordered by `signedAt`, then `contractId`, ascending.

### AC-04-05 - Navigation boundaries

- **Given** the renter activates the edit icon, `Doi mat khau`, or `Dang xuat`
- **When** the action succeeds
- **Then** it respectively navigates to UC-05, navigates to UC-06, or invokes the existing sign-out flow
- **And** UC-04 performs no edit, password-change, or contract-edit business logic.

### AC-04-06 - Error and session isolation

- **Given** loading, refresh, offline, expired/revoked/inactive session, or a profile subject mismatch occurs
- **When** UC-04 handles it
- **Then** it follows the runtime-state matrix without raw error/PII disclosure
- **And** it never keeps profile or rental data from a previous user/session.

## 7. Deferred API proposal for G3 review

After G2, backend may review an authenticated profile-read contract (path/name
not approved). It must derive the subject from the access token, never accept a
client-selected user ID, define each approved field's source owner and
nullability, define active-rental semantics and `signedAt`/`contractId`, and
specify error/session/cache headers. `/auth/me` and `/session/me` currently
return actor/session data only and must not be treated as an approved UC-04
profile response.

## 8. Implementation gate and Definition of Done

G1 FE/UI may be created only after this document is merged and G0 is marked
done. It must use mock data only for fields and states explicitly approved in
this document, produce web and mobile evidence for the three canonical visual
states plus loading/error/session states, and keep UC-05/UC-06 implementation
out of scope. G3 backend review remains blocked until G2 visual review approves
the FE evidence.
