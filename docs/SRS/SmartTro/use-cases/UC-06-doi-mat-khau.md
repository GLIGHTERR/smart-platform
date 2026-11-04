# SmartTro - UC-06 Doi mat khau

## 1. Trang thai tai lieu va nguon

| Thuoc tinh | Gia tri |
| --- | --- |
| Trang thai G0 | **NEEDS_PO_DECISION** |
| Pham vi | Doi mat khau local cho nguoi dung da xac thuc; chua la authorization de FE/BE trien khai. |
| Legacy | SRS muc 3.7 la baseline tham khao, khong phai approval. Quy tac SHA-256 trong baseline bi thay the bang verdict o muc 5 va khong duoc dung mac dinh. |
| Source heads da review | `smart-platform@19fa7ff491d5e9f5a3ba4b4a53728eec145d76da`; `smart-tro@ab463c04bc16d55c78448ac29dcb0e8f86bb9f22`; `smart-platform-services@dff03a7a49186e7c8ba82efbac9e21fa16910a6b`. |
| Owner quyet dinh con mo | PO (Nghia Nguyen Tuan), voi Security/BE cung cap evidence ky thuat. |

Tai lieu nay tu dung va la canonical G0 cho UC-06. `OPEN` khong duoc dien giai thanh business rule, API contract, visual approval, hay license mo gate. Khong ghi gia tri password, token, cookie, credential, PII that, hoac log nhay cam trong tai lieu/evidence.

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
| UC-01 Sign Up | Password policy hien co: 8-128 ky tu, chu thuong, chu hoa, chu so, ky tu dac biet; confirm phai khop. Password khong vao route, log, analytics hoac persistent storage. UC-06 can PO xac nhan rang policy nay ap dung nguyen ven. |
| UC-02 Sign In | `SIGNIN-D09`: 5 lan sai lien tiep throttle 15 phut; `SIGNIN-D10`: access 15 phut, refresh 30 ngay va rotation; `SIGNIN-D11`: logout current-device va reset thu hoi moi session. UC-06 chua co quyet dinh thu hoi session sau change. |
| UC-03 Forgot Password | Reset thanh cong revoke toan bo session, khong auto-login; audit khong log secret. Day la precedent security, khong tu dong phe duyet cho UC-06. |
| UC-04 Account/Personal | FRS da phe duyet action `Doi mat khau` chi dieu huong sang UC-06. Tai source review, `smart-tro` dang dieu huong den placeholder `Destination`, chua co form UC-06. |
| UC-05 Edit Personal | Pattern subject-only, server authoritative, expired/revoked/inactive session thi sign-out, va success quay UC-04 la reference UX; khong thay the decision success cua UC-06. |
| services current source | Co candidate endpoint/service change-password va password hasher co salt/slow hash; candidate hien tai khong co confirm field, co behavior cap session moi sau revoke, va chua la approved UC-06 contract/deploy evidence. |

## 4. Luong canonical de PO phe duyet

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
| Current password khong dung | Giu form, xoa current field theo decision UX, thong bao chung khong phan biet account state; retry/rate-limit theo `UC06-D02`. |
| Session expired, revoked, inactive, subject mismatch | Khong doi password; clear sensitive form state; chay common sign-out/session-expired behavior cua UC-04/05. |
| Rate limited / cooldown | Khong mutate; hien retry action/thoi diem theo server contract; khong suy luan account state. |
| Timeout, offline, 5xx | Khong tu ket luan mutation fail hay retry blind. Hien retry an toan sau khi resolve authoritative state/idempotency decision; password fields khong persist. |
| Double submit / concurrent request | UI chi mot request dang cho. Server phai xac dinh final authoritative outcome; response cho request sau khong duoc tao session/mutation thu hai. |
| Back, cancel, app background/restart | Warning dirty state va hanh vi back/cancel la `UC06-D04`; bat ky exit/resume/restart nao xoa ba field, khong persist secret. |

## 5. Decision matrix bat buoc

| ID | Quyet dinh / options | Recommendation | Rationale | Owner | Impact | Status |
| --- | --- | --- | --- | --- | --- | --- |
| UC06-D01 | Password policy: (A) ke thua UC-01 8-128 + lower/upper/digit/special; (B) policy moi; (C) policy identity service la canonical. Normalization: (A) giu nguyen exact characters; (B) trim/normalize. Reuse history: none / last-N / current-only. | A + giu nguyen exact characters + current-only, cho den khi PO/Security quyet khac. | Nhat quan UC-01/03; trim password co the thay doi secret va history chua co evidence. | PO + Security | FE validation, DTO, migration, test boundary. | OPEN |
| UC06-D02 | Sai current password: (A) generic error + same retry control; (B) field-specific; throttle: (A) reuse SIGNIN-D09; (B) policy rieng; (C) no throttle. | A + reuse 5 fail/15 min chi neu PO xac nhan scope chung. | Can han che disclosure va brute force; precedent Sign In khong tu dong ap dung cho mutation. | PO + Security | Status/code/copy, rate limiter, audit, UX. | OPEN |
| UC06-D03 | Session revocation: (A) revoke all incl current, sign in lai; (B) revoke other sessions, current continues/rotates; (C) revoke all va cap session moi current. | A de dong nhat UC-03 va giam session theft, nhung PO phai chap nhan UX. | UC-03 la all-session/no auto-login; source candidate C la conflict can resolve. | PO + Security | Auth response, token rotation, navigation, device regression. | OPEN |
| UC06-D04 | Success destination: (A) Sign In; (B) UC-04; (C) home. Dirty/back/cancel: discard ngay / confirm discard / save draft. | Neu D03=A, A; neu D03=B/C, B. Confirm discard khi co input. | Destination phu thuoc session decision; khong co Figma canonical form/state. | PO + Design | G1 visual, navigation, accessibility, UAT. | OPEN |
| UC06-D05 | Rate limit/lockout, cooldown, audit/security notification: reuse Sign In / policy rieng / no notification. | Audit immutable subject + masked metadata, no secret; notification va exact limit can PO/Security chot. | Audit precedent UC-03; notification co UX/privacy scope. | PO + Security | API headers, event schema, support/comms. | OPEN |
| UC06-D06 | Timeout/duplicate/concurrency: (A) idempotency key + authoritative query; (B) serializable/versioned mutation; (C) server last-write policy. | A, with server-side one mutation per authenticated subject and no blind retry. | Tranh doi password/session lap va feedback sai khi timeout. | PO + BE | API contract, persistence, client retry, tests. | OPEN |
| UC06-D07 | Hashing/storage migration: (A) keep reviewed salted slow hash; (B) approved migration; (C) legacy SHA-256. | A subject to Security verification; reject C. | Read-only source co per-record salted slow hash; legacy SHA-256 is not an approved safe storage contract. | Security + PO | DB migration, compatibility, incident risk, tests. | OPEN |
| UC06-D08 | Privacy: no secret in logs/analytics/routes/persistent storage/clipboard by default; exceptions only explicit approval. | No exceptions. | Ke thua no-secret constraints UC-01/02/03. | PO + Security | FE telemetry, API logging, QA evidence. | APPROVED (existing cross-UC constraint) |
| UC06-D09 | Figma/reference: (A) new canonical Figma; (B) PO-approved annotated reference; (C) infer from legacy/mock. Responsive/a11y states included/excluded. | A; require form, error, loading, success, session-expired, keyboard and responsive states. | UC-04 approves entry only; no UC-06 canonical visual was found. | PO + Design | G1 gate, screenshot review, accessibility AC. | OPEN |
| UC06-D10 | Evidence: web first; mobile manual only per approved build/SHA; UAT boundary. | Web QA first; mobile only after explicit PO authorization for exact build/SHA. | Parent delivery gate. | PO | QA plan, release evidence. | APPROVED (parent gate) |

## 6. UI/UX va accessibility proposal (non-binding while D04/D09 OPEN)

- Entry route is UC-04 Personal; do not treat the present placeholder as a usable UC-06 screen.
- Use one dedicated form with secure-entry show/hide controls, labels usable by screen readers, clear focus order, visible focus, keyboard-safe scroll, minimum 48 px touch targets, and error announcement.
- Disable the primary action while submission is pending; no duplicate request; preserve only non-sensitive UI state needed to render a failure.
- Do not copy password values to clipboard automatically. Do not prefill or retain any password after submit, cancel, background/resume, logout, account switch, or process restart.
- Canonical Figma/reference, text copy, success feedback, responsive viewport matrix, and dirty-discard interaction are gaps owned by PO/Design. No legacy frame/mock is visual source of truth.

## 7. API/session/security proposal for G2 (not approved, not implementation authorization)

### 7.1 Candidate contract

`POST /auth/password/change` (path/method must be confirmed against gateway convention) with authenticated bearer/session subject only. Body contains current, new, and confirmation password fields; no subject ID. Requests must use TLS, `Cache-Control: no-store`, prevent intermediaries from caching, and never echo secret values.

Success must return only the approved next-state: either an acknowledgement with sign-in destination, or a newly issued current-session representation if `UC06-D03=C`. Error mapping must use stable safe codes, without raw server messages: validation/confirmation/reuse (`400`); unauthenticated/expired/revoked (`401`); inactive/forbidden subject (`403` if approved); current-password invalid (`400` or `401`, per D02); rate limit (`429` plus retry metadata); conflict/concurrency (`409`); retryable unavailability (`5xx`). Exact public code/status table is contingent on D02/D03/D05/D06.

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

**DoD:** G1 only after D04/D09 visual decisions and PO review; G2 only after all security/session/API rows are terminal; G3 uses real approved API, not a policy mock; Dev supplies unit-test/coverage evidence under its quality gate; QA independently tests exact merged/deployed SHA; PO UAT occurs only after QA PASS. `ROOT_SYNC` is terminal only after PO UAT and contains no sensitive data.

## 10. Gap and delivery impact map

| Repository | Read-only finding | Downstream impact |
| --- | --- | --- |
| `smart-platform` | This canonical spec was legacy-only before G0; UC-04/05 baseline and FRS show entry but no canonical UC-06 visual. | Docs/G1 Design gap; no code change in G0. |
| `smart-tro` | UC-04 action currently reaches a destination placeholder; no UC-06 form/API integration. | G1 screen/navigation; G3 real API integration after gates. |
| `smart-platform-services` | Existing source has a change-password candidate but differs from proposed confirm/session choices and lacks G0 approval/deploy proof. | G2 must reconcile contract, security review, migration/session/audit tests; do not reuse by assumption. |

## 11. G0 terminal handoff

G0 has normalized the canonical requirement and surfaced decision owners. It is **not** ready for FE or BE. PO must issue terminal decisions for `UC06-D01` through `UC06-D07` and `UC06-D09`; then PM can revise this document, obtain visual approval at G1 where required, and open downstream gates in order.
