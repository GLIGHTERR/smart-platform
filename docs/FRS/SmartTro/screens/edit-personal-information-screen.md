# SmartTro - UC-05 Cap nhat thong tin ca nhan Living Specification

## 1. Document control

| Attribute | Value |
| --- | --- |
| Product | SmartTro |
| Use case | UC-05 - Cap nhat thong tin ca nhan |
| Requirement traceability | SM007, US 5.0, UC-04 edit action |
| Status | PO behavior decisions recorded 2026-10-14; ready for G1 only after this document's PR merges |
| Layout evidence | PO attachment `01a13885-ef99-73cf-b2d1-089a77880e94` on GLI-138; layout only, not a color/token source |
| Review gate | G1 capture -> G2 PO UI review -> G3 BE/API |

This is the canonical requirement for updating the signed-in renter's own
personal information. The legacy UC-05 baseline and prior BR-01 are historical
only: BR-01 is superseded for this MVP.

## 2. Scope and boundaries

### 2.1 In scope

- A signed-in Registered User enters UC-05 only from UC-04's edit action.
- The user can update `Họ và tên` and `Số điện thoại` for the access-token
  subject.
- The screen has editable fields in this order: name, phone, then a masked,
  read-only email. It has `Hủy` on the left and `Lưu` on the right.
- Dirty-form exit handling, validation, saving, retry, authoritative refresh,
  accessibility, and the runtime/security rules in this document.

### 2.2 Out of scope

- Editing email, password, avatar/media, contracts, signatures, social auth,
  phone OTP/ownership verification, object storage, media permissions, or
  image processing.
- Persistent offline updates, client-selected `userId`, persistent PII cache,
  or an implementation/backend task before G2 passes.

UC-04 remains a read-only presentation screen. UC-06 owns password changes.

## 3. PO decision matrix

| Decision | Status | Canonical result |
| --- | --- | --- |
| Editable fields | APPROVED | Only `displayName` and `phone` are editable. |
| Email | APPROVED | Normalized-email login identity is read-only and masked using the UC-04 rule. It is never included in an update request. |
| Legacy BR-01 | SUPERSEDED | Phone can be changed or cleared because it is optional, non-unique contact data and not a login identifier. |
| Name validation | APPROVED | Required; Unicode; maximum 160 characters; trim and collapse repeated whitespace; reject null, empty, or whitespace-only normalized values. Server validation is authoritative. |
| Phone validation/storage | APPROVED | UI accepts domestic Vietnam `^0\\d{9}$`; blank maps to `null`; a supplied value is normalized to canonical E.164 `+84XXXXXXXXX` and must match `^\\+[1-9]\\d{7,14}$`. Opening/reopening converts canonical `+84XXXXXXXXX` back to domestic form. |
| Privacy | APPROVED | Edit form shows raw name/phone only to its subject; email is masked. Do not log raw email, phone, profile payload, or raw backend errors in analytics/UI diagnostics. UC-04 continues to mask phone to its final three digits and email by its existing rule. |
| Avatar/media | N/A | No avatar/media edit affordance or media work is in UC-05. |
| Save and state | APPROVED | `Lưu` is primary. Clean or invalid dirty forms disable it; valid dirty forms enable it; saving disables it and exposes a saving state. A fully reverted form is clean again. |
| Cancel and exit | APPROVED | Screen-level `Hủy` is secondary and non-destructive. Dirty `Hủy`, web back, and device/gesture/hardware back require the approved confirmation dialog; clean exits leave immediately. |
| Discard dialog | APPROVED | Title `Hủy thay đổi?`; body `Các thay đổi chưa lưu sẽ bị mất. Bạn có chắc muốn rời khỏi màn hình này?`; stay action `Tiếp tục chỉnh sửa`; destructive leave action `Bỏ thay đổi`. |
| Visual boundary | APPROVED / DEFERRED | Layout, field/action order, scrolling and keyboard/safe-area behavior are approved. Secondary color/token is deliberately proposed in G1 capture and decided only by PO at G2; the supplied layout image is not color evidence. |
| Success | APPROVED | On authoritative save success, show the approved success confirmation, return to UC-04 Personal, and refetch authoritative data. |

## 4. Field and mock-contract matrix

| Field | Editability | UI representation | Normalize / validate | Request and response rule |
| --- | --- | --- | --- | --- |
| `displayName` | Editable, required | Full value | Trim, collapse whitespace, Unicode, 1-160 characters after normalization | Send normalized value; response is authoritative. |
| `phone` | Editable, optional/nullable | Domestic `0XXXXXXXXX`, not masked | Blank -> `null`; validate domestic `^0\\d{9}$`; domestic -> E.164 `+84XXXXXXXXX` and validate the E.164 rule above | Send canonical E.164 or `null`; response canonical value is converted back to domestic form only in UC-05. |
| `email` | Read-only | UC-04 masked form | No edit or normalization in UC-05 | Never send in update request. |
| `avatar` | N/A | No edit section | N/A | UC-04 fallback remains unchanged. |

G1 may use this mock shape only:

```ts
type EditableProfile = {
  displayName: string;
  phone: string | null; // Canonical E.164 at the contract boundary.
  email: string;        // Read-only, rendered masked.
};
```

## 5. Authorization, API and state boundary

The exact endpoint path/method and final transport DTO are a G3 decision after
G2. They must nevertheless implement this fixed boundary:

- The server derives the subject solely from the access token; it accepts no
  client-selected user ID and cannot update another user's profile.
- An update contains only the two approved editable fields, validates them
  server-side, persists atomically, and returns the authoritative profile or a
  safe mapped error.
- The last valid request accepted by the server is the final profile state.
  The client must not apply a stale response over a later accepted response;
  returning to UC-04 refetches the authoritative subject profile.
- A field-validation response attaches safe feedback to the relevant field.
  Retryable errors retain form values and allow a later retry. No offline queue
  is created. A session expired, revoked, inactive, or subject-mismatch result
  follows the common sign-out/session-expired flow and clears per-user UI data.
- Do not add persistent PII cache. Refetch/invalidate UC-04 after success and
  isolate data across logout or account switch.
- The normal-load server processing target is below two seconds; the UI shows
  saving immediately and prevents double submission until it resolves.

## 6. Presentation and accessibility

- The title is `Cập nhật thông tin cá nhân`; there is no avatar/media section.
- The screen scrolls and its action area remains usable above mobile safe areas,
  keyboards, browser controls, and viewport changes.
- The secondary button's color/token is not approved at G0 and must not be
  inferred from the supplied attachment or legacy colors.
- Inputs have programmatic labels, required/optional/read-only hints, logical
  focus order, keyboard and touch activation, visible focus, accessible
  contrast, and dynamic type-safe layout.
- Validation, saving, success, and retryable errors announce their state without
  exposing raw backend errors or PII.
- The dirty-exit dialog is modal to assistive technology: it announces title and
  body, traps focus while open, restores focus when staying, and prevents a
  repeated back action from opening duplicate dialogs.

## 7. Acceptance criteria

### AC-05-01 - Entry, fields, and privacy

- **Given** a signed-in renter selects edit from UC-04
- **When** UC-05 opens
- **Then** it presents editable name, editable domestic phone, and masked
  read-only email in that order, with `Hủy` then `Lưu`.
- **And** it has no avatar/media editing and does not expose raw PII or backend
  errors to logs, analytics, or UI diagnostics.

### AC-05-02 - Name and phone round trip

- **Given** a renter enters a name with leading, trailing, or repeated
  whitespace and a domestic Vietnam phone
- **When** the form validates and saves
- **Then** the name is trim/collapse normalized, the phone is sent canonically
  as E.164, and the server remains authoritative.
- **Given** the phone is blank
- **When** the renter saves valid changes
- **Then** the request stores `null` and UC-04 shows its approved missing-phone
  presentation.
- **Given** UC-05 receives a canonical E.164 phone
- **When** it opens or reopens
- **Then** it renders domestic `0XXXXXXXXX` for editing while UC-04 still masks
  the displayed phone.

### AC-05-03 - Validation and enablement

- **Given** the initial profile values
- **Then** the form is clean and `Lưu` is disabled.
- **Given** any platform-appropriate input event changes a value
- **When** the values are valid and differ from the originals
- **Then** `Lưu` is enabled.
- **When** a required name is empty/whitespace-only, longer than 160 normalized
  characters, or a supplied phone is not valid canonical Vietnam data
- **Then** client feedback is field-specific, the button remains disabled, and
  server validation still decides the final result.
- **When** all values are restored to their originals
- **Then** the form becomes clean and `Lưu` is disabled again.

### AC-05-04 - Save, error, conflict, and authoritative refresh

- **Given** a valid dirty form
- **When** the renter selects `Lưu`
- **Then** saving is announced immediately, repeated submits are prevented, and
  the request updates only the token subject's approved fields.
- **When** a retryable or validation failure occurs
- **Then** form values are retained, safe field/error feedback is shown, and a
  new submit is possible after a real failure.
- **When** concurrent valid requests occur
- **Then** the last valid request accepted by the server defines the final state
  and a stale client response cannot overwrite later accepted state.
- **When** saving succeeds
- **Then** the approved confirmation appears, navigation returns to UC-04
  Personal, and authoritative profile data is invalidated/refetched.

### AC-05-05 - Dirty exit: screen cancel

- **Given** a dirty form
- **When** the renter selects `Hủy`
- **Then** a single modal presents title `Hủy thay đổi?`, the approved body,
  `Tiếp tục chỉnh sửa`, and dangerous `Bỏ thay đổi`.
- **When** the renter chooses `Tiếp tục chỉnh sửa`
- **Then** the modal closes and preserves the form and focus.
- **When** the renter chooses `Bỏ thay đổi`
- **Then** unsaved changes are discarded and the screen exits.

### AC-05-06 - Dirty exit: web back

- **Given** a dirty form in web runtime
- **When** the renter invokes browser back or equivalent web back navigation
- **Then** the same single dirty-exit modal intercepts the exit and behaves as
  AC-05-05.

### AC-05-07 - Dirty exit: device back

- **Given** a dirty form in mobile runtime
- **When** the renter invokes hardware back, gesture back, or equivalent device
  navigation
- **Then** the same single dirty-exit modal intercepts the exit and behaves as
  AC-05-05.
- **Given** a clean form on any runtime
- **When** the renter uses `Hủy` or a supported back path
- **Then** the screen exits immediately with no modal.

### AC-05-08 - Session, cache, and accessibility regression

- **Given** an expired, revoked, inactive, mismatched, logout, or account-switch
  session
- **When** UC-05 handles it
- **Then** it follows the common sign-out/session-expired flow and never keeps
  or renders another account's profile data.
- **And** the form, dialog, states, and actions meet the accessibility rules in
  section 6 and preserve UC-04/UC-06 boundaries.

## 8. Test data and delivery gates

Use synthetic fixtures only; no real PII, credential, token, or cookie belongs
in captures, logs, or test evidence. Minimum fixtures cover valid name/phone,
blank phone, invalid phone, whitespace/160-character name boundaries,
server-validation, retryable error, session failure, two subject isolation, and
three dirty-exit paths.

1. G1 FE/UI uses the mock contract and provides web/mobile captures, including
   clean/dirty/invalid/saving/error/success and each dirty-exit path.
2. G2 is a PO-only UI review of captures, visual tokens, copy, navigation, and
   responsive/accessibility evidence. G2 may approve or request changes.
3. Only after G2 passes may G3 define and implement the actual API/migration
   work. G4 integration, G5 QA, and G6 UAT remain gated in order.

## 9. Traceability and Definition of Done

| Source | UC-05 interpretation |
| --- | --- |
| SM007 | Current requirement trace; this living spec supersedes legacy behavior conflicts. |
| US 5.0 | Updated to this approved two-field, subject-bound update flow. |
| UC-04 | Read-only entry/return screen; supplies only its approved masking and navigation boundaries. |
| PO_DECISION / PO_DECISION_FINAL on GLI-138 | Terminal business, layout, domestic/canonical phone, action, modal, and gate decisions. |

G0 is complete only when this document and the linked traceability changes merge
to `master`. It neither authorizes G1 before that merge nor creates any
implementation work.
