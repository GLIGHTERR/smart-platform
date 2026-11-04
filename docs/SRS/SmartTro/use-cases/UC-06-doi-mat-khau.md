# SmartTro - UC-06 Doi mat khau

## 1. Trang thai tai lieu va nguon

| Thuoc tinh | Gia tri |
| --- | --- |
| Trang thai G0 | **DONE - PO decisions terminal 2026-11-04** |
| Pham vi | Doi mat khau local cho nguoi dung da xac thuc. G0 chua la authorization de FE/BE trien khai; G1 canonical reference va PO visual review van la gate. |
| Legacy | SRS muc 3.7 la baseline tham khao, khong phai approval. Quy tac SHA-256 trong baseline bi thay the bang verdict o muc 5 va khong duoc dung mac dinh. |
| Source heads da review | `smart-platform@19fa7ff491d5e9f5a3ba4b4a53728eec145d76da`; `smart-tro@ab463c04bc16d55c78448ac29dcb0e8f86bb9f22`; `smart-platform-services@dff03a7a49186e7c8ba82efbac9e21fa16910a6b`. |
| Quyet dinh PO | `UC06-D01..D10` terminal; `UC06-D07` van yeu cau Security/BE xac minh implementation truoc G2. |

Tai lieu nay tu dung va la canonical G0 cho UC-06. Cac decision matrix ben duoi la terminal theo `PO_APPROVED` ngay 2026-11-04; chi G1 Figma/reference va PO visual review moi cho phep mo FE/UI. Khong ghi gia tri password, token, cookie, credential, PII that, hoac log nhay cam trong tai lieu/evidence.

## 2. Muc tieu, actor va ranh gioi

**Actor:** nguoi dung da dang nhap, co tai khoan local active. Subject luon lay tu session da xac thuc; client khong gui ID de chon account.

**Trigger:** tu UC-04 Account/Personal, nguoi dung chon `Doi mat khau`.

**Preconditions:** session hien tai hop le; account co local password; UI/API dang dung contract da duoc phe duyet.

**Postcondition khi thanh cong:** password moi duoc luu atomically theo storage verdict da duyet, cac session bi thu hoi theo decision `UC06-D03`, security/audit event duoc ghi khong lo secret, va UI thuc hien destination da duyet.

**In scope:** form current/new/confirm, verification, validation, session lifecycle, errors an toan, accessibility, API/test/delivery contract.

**Out of scope cho G0/UC-06:** password enrollment cho social-only account, MFA/re-authentication step moi, account linking, reset/recovery UC-03, quan ly thiet bi chi tiet, va implementation/deploy.

## 3. Traceability va reconcile

| Nguon | Rang buoc ke thua / gap |
| --- | --- |
| UC-01 Sign Up | Policy da duoc PO ke thua cho UC-06: 8-128 ky tu, chu thuong, chu hoa, chu so, ky tu dac biet; confirm phai khop. Password giu nguyen exact characters, khong trim/normalize, va khong vao route, log, analytics hoac persistent storage. |
| UC-02 Sign In | `SIGNIN-D09` 5 lan sai/15 phut duoc PO reuse theo subject cho UC-06. `SIGNIN-D10` token rotation la contract Sign In; UC-06 revoke toan bo session va khong cap session moi theo D03. |
| UC-03 Forgot Password | Reset revoke toan bo session va khong auto-login la precedent ma PO da chon cho UC-06; audit khong log secret. |
| UC-04 Account/Personal | FRS da phe duyet action `Doi mat khau` chi dieu huong sang UC-06. Tai source review, `smart-tro` dang dieu huong den placeholder `Destination`, chua co form UC-06. |
| UC-05 Edit Personal | Pattern subject-only, server authoritative, expired/revoked/inactive session thi sign-out duoc ke thua; UC-06 da chon success ve Sign In, khong quay UC-04. |
| services current source | Co candidate endpoint/service change-password va password hasher co salt/slow hash. Candidate thieu confirm va cap session moi sau revoke, nen G2 phai reconcile theo D01/D03/D06; source khong phai deploy evidence. |

## 4. Luong canonical da duoc PO phe duyet

### 4.1 Main flow de xuat

1. Tu UC-04, user chon `Doi mat khau`; system mo form rieng.
2. Form hien `Mat khau hien tai`, `Mat khau moi`, `Xac nhan mat khau moi`; khong prefill field nao.
3. User nhap gia tri va chon action chinh. UI validate client-side theo policy da duyet, doi chieu new/confirm, khoa form trong khi request.
4. API xac thuc subject tu session, revalidate tat ca rang buoc, xac minh current password, va thuc hien mutation/session/audit trong transaction/authoritative operation.
5. Khi API thanh cong, UI xoa ca ba field khoi memory, xu ly session/destination theo `UC06-D03` va `UC06-D04`, va thong bao ket qua an toan.

### 4.2 Alternate va exception flows

| Tinh huong | Hanh vi yeu cau |
| --- | --- |
| Client validation fail / new-confirm khong khop / new giong current | Khong goi API neu xac dinh local duoc; hien inline feedback an toan; khong lo current password. |
| Current password khong dung | Giu form, xoa current field, thong bao generic safe, khong phan biet account state hay raw backend message; throttle 5 lan that bai/15 phut theo subject. |
| Session expired, revoked, inactive, subject mismatch | Khong doi password; clear sensitive form state; chay common sign-out/session-expired behavior cua UC-04/05. |
| Rate limited / cooldown | Khong mutate; hien retry action/thoi diem theo server contract; khong suy luan account state. |
| Timeout, offline, 5xx | Khong tu ket luan mutation fail hay retry blind. Hien retry an toan sau khi resolve authoritative state/idempotency decision; password fields khong persist. |
| Double submit / concurrent request | UI chi mot request dang cho. Server phai xac dinh final authoritative outcome; response cho request sau khong duoc tao session/mutation thu hai. |
| Back, cancel, app background/restart | Khi co input, back/cancel phai confirm discard; khong save draft. Bat ky exit/background/restart nao xoa ba field, khong persist secret. |

## 5. Decision matrix bat buoc

| ID | Quyet dinh terminal | Rationale | Owner | Impact | Status |
| --- | --- | --- | --- | --- | --- |
| UC06-D01 | Ke thua UC-01: 8-128, lowercase, uppercase, digit, special; giu nguyen exact characters, khong trim/normalize; new khac current; chua ap dung last-N history MVP. | Nhat quan UC-01/03 ma khong thay doi secret. | PO + Security | FE validation, DTO, test boundary. | APPROVED 2026-11-04 |
| UC06-D02 | Current-password sai tra generic safe error; throttle 5 failures/15 minutes theo subject; public code/copy on dinh, khong raw error hay account state. | Chong disclosure va brute force. | PO + Security | Status/code/copy, rate limiter, audit, UX. | APPROVED 2026-11-04 |
| UC06-D03 | Revoke tat ca session, gom current session; khong auto-login/cap session moi; user Sign In lai. | Dong nhat recovery va giam session-theft risk. | PO + Security | Auth response, navigation, device regression. | APPROVED 2026-11-04 |
| UC06-D04 | Success feedback an toan roi dieu huong Sign In. Back/cancel khi co input confirm discard; khong save draft; exit/background/restart xoa secrets. | UX ro rang phu thuoc D03, khong retain secret. | PO + Design | G1 visual, navigation, accessibility, UAT. | APPROVED 2026-11-04 |
| UC06-D05 | Reuse D02 throttle; immutable audit event chi subject + metadata masked; khong email/push notification trong MVP. | Audit du traceability ma bao ve privacy. | PO + Security | Rate limiter, audit event, support/comms. | APPROVED 2026-11-04 |
| UC06-D06 | Idempotency key + authoritative outcome/query; mot subject chi mot mutation dang xu ly; no blind retry; response cu khong ghi de final state. | Tranh duplicate mutation/session va success sai sau timeout. | PO + BE | API contract, persistence, client retry, tests. | APPROVED 2026-11-04 |
| UC06-D07 | Giu salted slow hash hien hanh sau khi Security/BE xac minh implementation; khong migration neu compatible; cam legacy SHA-256. | Bao toan storage an toan va dung evidence truoc thay doi. | Security + PO | Compatibility review, migration, tests. | APPROVED 2026-11-04 |
| UC06-D08 | No secret trong logs/analytics/routes/persistent storage/clipboard; khong exception MVP. | Rang buoc cross-UC da duoc phe duyet. | PO + Security | FE telemetry, API logging, QA evidence. | APPROVED 2026-11-04 |
| UC06-D09 | Tao canonical Figma/reference moi cho form va error/loading/success/session-expired/keyboard/responsive/accessibility truoc PO visual review; legacy/mock khong phai approval. | UC-04 chi phe duyet entry, khong co UC-06 visual canonical. | PO + Design | G1 gate, screenshot review, accessibility AC. | APPROVED 2026-11-04 |
| UC06-D10 | Web first; mobile manual only theo build/SHA duoc PO cho phep; UAT sau QA PASS. | Parent delivery gate. | PO | QA plan, release evidence. | APPROVED 2026-11-04 |

## 6. UI/UX va accessibility requirements

- Entry route is UC-04 Personal; do not treat the present placeholder as a usable UC-06 screen.
- Use one dedicated form with secure-entry show/hide controls, labels usable by screen readers, clear focus order, visible focus, keyboard-safe scroll, minimum 48 px touch targets, and error announcement.
- Disable the primary action while submission is pending; no duplicate request; preserve only non-sensitive UI state needed to render a failure.
- Do not copy password values to clipboard automatically. Do not prefill or retain any password after submit, cancel, background/resume, logout, account switch, or process restart.
- Canonical Figma/reference phai duoc tao o G1 truoc PO visual review: form, copy, success, error, loading, session-expired, keyboard, responsive va accessibility states. Legacy/mock khong la visual source of truth.

## 7. API/session/security contract for G2 (approved requirement, not implementation authorization)

### 7.1 Contract baseline

The reviewed service exposes `POST /auth/password/change`; G2 must reconcile it to the approved contract before integration. It authenticates bearer/session subject only. The body contains current, new, and confirmation password fields; no subject ID. Requests use TLS, `Cache-Control: no-store`, prevent intermediaries from caching, and never echo secret values.

Success returns only acknowledgement and the Sign In next-state; it must not return or issue a new session. Error mapping uses stable safe codes without raw server messages: validation/confirmation/reuse (`400`); unauthenticated/expired/revoked (`401`); inactive/forbidden subject (`403`); current-password invalid (`400` or `401`, frozen by G2 API contract); rate limit (`429` plus retry metadata); conflict/concurrency (`409`); retryable unavailability (`5xx`).

### 7.2 Server requirements

- Authenticate only current subject; verify current password with timing-safe/anti-enumeration behavior and revalidate policy server-side.
- Store only an approved one-way password representation. Current source review is evidence of a salted slow-hash candidate, not deployment verification or migration approval. SHA-256-only storage is rejected as an implementation default.
- Atomically update password, apply one approved session-revocation scope, record privacy-safe audit event, and produce one authoritative outcome for concurrency.
- Logs, traces, analytics, error bodies, audit payloads, persistent client stores, navigation parameters, screenshots, and test fixtures must omit password/session secrets. Do not create a new secret-bearing telemetry field.

## 8. Acceptance criteria

### AC-06-01 - Entry and subject

- **Given** an active authenticated local-password user is on UC-04 Personal
- **When** they choose `Doi mat khau`
- **Then** the system opens only the approved UC-06 form and never accepts a client-selected subject.
- **And** expired, revoked, inactive, or mismatched sessions clear sensitive fields and use common session-expired/sign-out behavior.

### AC-06-02 - Validation and confirmation

- **Given** the form is open
- **When** current/new/confirm values are missing, boundary-invalid, violate D01, new equals current, or confirmation differs
- **Then** no mutation is made, feedback is accessible and safe, and no secret is retained after exit/resume.

### AC-06-03 - Current verification and abuse

- **Given** a valid authenticated subject submits a syntactically valid form
- **When** current-password verification fails or the server applies D02/D05 protection
- **Then** the password is unchanged, response/copy does not disclose extra account state, and retry/cooldown follows approved policy.

### AC-06-04 - Successful mutation and session result

- **Given** current verification and all validation pass
- **When** the server processes exactly one mutation
- **Then** the new password becomes authoritative, audit is privacy-safe, session revocation/current-session behavior follows D03, and navigation/feedback follows D04.

### AC-06-05 - Failure, timeout and concurrency

- **Given** a timeout, offline/5xx failure, double submit, or concurrent change attempt
- **When** requests race or a response is uncertain
- **Then** UI does not issue an uncontrolled retry or show unverified success; server provides one authoritative final state under D06; no duplicate session/mutation is created.

### AC-06-06 - Privacy and accessibility

- **Given** any UI/API/test/audit path for UC-06
- **When** it handles the form or response
- **Then** no password/session secret appears in route params, storage, clipboard, analytics, logs, errors, screenshots, or evidence.
- **And** secure fields, labels, focus order, error announcement, contrast, touch target, keyboard behavior, loading, and responsive states meet the approved D09 reference.

## 9. Test matrix va DoD for downstream

| Layer | Required cases |
| --- | --- |
| Unit | D01 boundary and relation validation; error mapper; no-secret state clearing; submit lock; dirty/back state; navigation per D03/D04. |
| API/integration | subject-only auth; wrong current; policy/reuse/confirm; inactive/expired/revoked; rate-limit; safe errors; cache headers; atomic password/session/audit transaction; idempotency/concurrency; no secret logging. |
| UI/Web | entry UC-04; loading/double-submit; all error/success destinations; focus/screen-reader/keyboard; 320/375/390/430 width and short-height evidence once D09 is approved. |
| System/regression | UC-01 registration policy, UC-02 sign-in/session rotation/throttle, UC-03 reset all-session behavior, UC-04/05 session expiry/account-switch behavior. |
| Mobile | Manual only after PO authorizes a named build and exact SHA; cover same functional/accessibility matrix feasible on device. |

**DoD:** G1 now creates the D09 canonical reference and obtains PO visual review; G2 only after that review plus Security/BE verification required by D07 and a frozen API code/status table; G3 uses real approved API, not a policy mock; Dev supplies unit-test/coverage evidence under its quality gate; QA independently tests exact merged/deployed SHA; PO UAT occurs only after QA PASS. `ROOT_SYNC` is terminal only after PO UAT and contains no sensitive data.

## 10. Gap and delivery impact map

| Repository | Read-only finding | Downstream impact |
| --- | --- | --- |
| `smart-platform` | This canonical spec was legacy-only before G0; UC-04/05 baseline and FRS show entry but no canonical UC-06 visual. | Docs/G1 Design gap; no code change in G0. |
| `smart-tro` | UC-04 action currently reaches a destination placeholder; no UC-06 form/API integration. | G1 screen/navigation; G3 real API integration after gates. |
| `smart-platform-services` | Existing source has a change-password candidate but differs from D01 confirm/D03 no-new-session behavior and lacks deploy proof. | G2 must reconcile contract, complete D07 Security/BE verification, and add session/audit/idempotency tests; do not reuse by assumption. |

## 11. G0 terminal handoff

G0 is **DONE**: PO terminally approved `UC06-D01..D10` on 2026-11-04 and this canonical document reflects that bundle. The next action is **G1 only**: create the D09 canonical Figma/reference, have PO review the visual/accessibility states, and record terminal evidence. Do not assign, trigger, or implement FE/BE from this G0 handoff. G2 remains gated by G1 visual approval and D07 Security/BE implementation verification.
