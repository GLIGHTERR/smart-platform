# SmartChủ G0 - Decision Package

> **Trạng thái:** IN_REVIEW / PARTIAL_DESIGN_READY - Auth, Home và UC-04 đã có nguồn visual; UC-05/08 và operational states còn chờ.
> **Phạm vi:** G0 PM/docs/decision cho phase đầu SmartChủ. Đây không phải implementation approval và không mở gate FE, BE, integration hoặc QA.
> **Traceability:** GLI-274; Auth docs đã merge tại `90ad491fab398b145c1f9973c7b15b7e07a40652`; đợt cập nhật Home/UC-04 được thực hiện trên branch `codex/smartchu-home-profile-docs`.

## 1. Canonical source và nguyên tắc

- Living specs UC-01, UC-02, UC-03 là nguồn đề xuất email auth; các User Story/Requirement List/FRS có phone/SMS là baseline lịch sử, không phải contract triển khai khi xung đột.
- Chính sách xác minh kinh doanh SmartChủ đã **Approved** là nguồn duy nhất cho trạng thái và quyền vận hành; package này không thay đổi policy đó.
- UC-04, UC-05 và UC-08 là living specs round 2/3; baseline legacy chỉ còn là provenance.
- Không có Figma URL/node SmartChủ canonical trong repo. Auth UC-01/02/03 có editable canvas ngày 2026-11-18; Home và UC-04 có editable canvas ngày 2026-11-20. UC-05, UC-08 và operational states chưa có visual reference canonical.

## 2. Decision matrix - PO action required

| ID | Nhóm / lựa chọn cần chốt | Khuyến nghị dựa trên nguồn hiện có | PO decision | Ảnh hưởng | Blocker nếu chưa chốt |
| --- | --- | --- | --- | --- | --- |
| D01 | Credential auth: email OTP cho Sign Up/Forgot Password; email + password cho Sign In, hoặc quay lại phone/SMS legacy | Chọn email theo UC-01/02/03 draft; phone chỉ là dữ liệu liên hệ nếu sau này được thu thập | **APPROVED (PO round 1)** | UC-01/02/03, US-01/02/03, shared auth API | D04/D05 vẫn chặn implementation |
| D02 | Owner profile: danh sách field, required/optional, mutable/immutable, validation, uniqueness, ownership và API/data mapping | Registration Email -> OTP -> Personal info -> Password; display name required; phone optional/editable/non-unique; avatar display/fallback only; profile tách business domain | **APPROVED (PO round 3)** | UC-01, UC-04/05, profile bootstrap, Home | D05 chặn implementation |
| D03 | Boundary account/profile với business verification: thời điểm thu thập profile, quyền Home và feature vận hành | Giữ policy Approved: account email-verified khác `APPROVED`; chỉ `APPROVED` tạo nhà/phòng/hợp đồng | **APPROVED Option A (PO round 1)**; UC-06/07 full scope pending separately | UC-01, Home, minimal status/CTA dependency | D05 chặn UI handoff |
| D04 | Session/password: policy password, OTP/reset TTL/cooldown/attempts, anti-enumeration, duration/rotation, multi-device, Sign Out current/all, revoke sau reset/change, post-success route | Sign Out current; Forgot Password/Change Password all -> Sign In; keep failure throttle separate; successful Change Password cooldown = 5 minutes. | **APPROVED (PO round 3)** | UC-01/02/03/08, auth/session API, security tests | D05 and later BE implementation gap remain |
| D05 | UI/Figma/canvas: canonical reference cho Sign Up (4 steps), Sign In, Forgot Password (3 steps), Home, UC-04/05/08 và state/loading/error | Dùng editable canvas versioned khi chưa có Figma canonical; từng nhóm màn phải có PO review rõ ràng | **PARTIALLY APPROVED:** Auth UC-01/02/03 có canvas ngày 2026-11-18; Home và UC-04 có canvas ngày 2026-11-20; UC-05/08 và operational states còn pending | Tất cả screen G0 | Chưa mở implementation gate |
| D06 | Sequencing: thứ tự Story và dependency shared auth/API, Home, profile/business verification, mobile delivery | Mobile thuộc phase đầu; sau docs/UI approval thực hiện preflight EAS read-only, rồi exact merge SHA -> Mobile QA -> PO app UAT | **APPROVED (PO rounds 1-3)** | Toàn phase đầu | D05/docs UI approval còn chờ; không build trong G0 |

## 2.1. Three distinct review groups

### A. Missing information / references

- **D05 design evidence:** Auth UC-01/02/03 đã có canvas canonical tại `docs/SRS/SmartChu/assets/auth/smartchu-auth-flow-canvas-2026-11-18.zip`; Home và UC-04 dùng `docs/SRS/SmartChu/assets/home-profile/smartchu-home-profile-canvas-2026-11-20.zip`. PNG capture của từng artboard được lưu cạnh living UC để Dev/QA đọc trực quan. FRS Markdown là mirror legacy có sai lệch/thiếu sót và không phải nơi handoff canonical. Repo vẫn chưa có visual canonical cho màn cập nhật UC-05, màn đổi mật khẩu UC-08 và các operational state chưa được thể hiện trên canvas.
- **D02 profile contract:** behavior/field scope đã chốt; detailed UI validation/masking/copy waits for D05 mockup.
- **D04 shared-auth contract:** policy đã chốt; backend Change Password vẫn là implementation gap và session duration/rotation/multi-device reference must be recorded at later BE gate.

### B. Conflicts between living specs and legacy

| Conflict | Canonical disposition pending PO approval | Impact |
| --- | --- | --- |
| UC-01/02/03 draft dùng email; User Stories, Requirement List và FRS legacy dùng phone/SMS | **D01 approved:** email là canonical; legacy được giữ làm provenance, không là implementation contract | D01, auth UI/API/test data |
| AD UC-05 ghi `Không thay đổi SĐT`; D02 đã chốt phone là contact tùy chọn, editable và non-unique | D02 là contract mới nhất; phải sửa AD/UC-05 bằng một thay đổi được PO duyệt trước FE handoff | profile schema/UI/test |
| UC-08 legacy nêu SHA-256; current backend dùng salted adaptive `scrypt` | Không dùng rule SHA-256 legacy; storage algorithm tách riêng password-composition policy | security acceptance/BE |
| US-02 legacy có phone OTP/lockout 72h; UC-02 canonical không OTP normal sign-in | D01/D04 đã chốt email/password và generic anti-enumeration; không mang lockout/OTP legacy sang email flow | sign-in UX/API |

### C. Proposed defer / out of scope

| Nội dung | Disposition đề xuất | Impact / dependency |
| --- | --- | --- |
| Social sign-up, social-only recovery/linking | Defer - cần UC và policy riêng | Không tự link provider theo email trong UC-01/02/03 |
| Loại giấy tờ pháp lý, re-verification/expiry, thu hồi hồ sơ đã duyệt, draft trước approval | Out of G0/MVP theo business-verification policy | Không thay đổi `APPROVED` gate của UC-10/18/22 |
| Mobile chain Expo exact SHA -> Mobile QA -> PO app UAT | In scope phase đầu; sau docs/UI approval mới EAS identity/config preflight read-only | Không build trong G0; cần exact merge SHA và môi trường trước QA |
| UX exploration bằng Canvas Design | Optional review aid, không phải FE/UI task | PO phải chấp thuận brief/artboards; G0 vẫn đóng implementation gate |

## 2.2. PO review choices: D02-D04

### D02 - Owner registration and personal profile fields

| Question | Option A | Option B | Recommendation and trade-off | PO decision |
| --- | --- | --- | --- | --- |
| D02.1 Initial registration fields | Email -> OTP -> Personal info -> Password | Collect personal profile only after sign-in | **A:** adopted SmartTrọ sequence; Personal info = required display name + optional phone contact. **B:** lower initial friction but is not the PO decision. | **APPROVED A (PO round 2)** |
| D02.2 Personal profile minimum scope | `display name` required; `phone` optional contact/editable/non-unique; verified email read-only; avatar display/fallback only | Avatar image-picker/upload/update | **A:** matches current SmartTrọ behavior and is approved phase-one behavior. **B:** is future scope because S3 upload is not ready. | **APPROVED A (PO round 3)** |
| D02.3 Editability | Email immutable in UC-05; account-email change is a separate UC | Allow email edit in UC-05 | **A:** adopted phase-one behavior. Future UC must define re-auth/current password, new-email OTP, uniqueness, session/audit. | **APPROVED A (PO round 2)** |
| D02.4 Profile/business ownership | Personal profile and business profile are separate tabs/domains; business tab is future-feature placeholder | Include business form/status workflow in phase one | **A:** adopted; full UC-06/07 is out of phase-one scope. **B:** is scope expansion. | **APPROVED A (PO round 2)** |

PO cần trả lời cùng các field cụ thể nếu chọn option có phone hoặc field khác: required/optional, format/validation, uniqueness, editability, privacy/masking và API owner. Không có field nào được tự thêm vào contract.

#### Proposed D02 field contract - PO review required

| Surface | Field | Purpose | Required | Source | Editable | Validation / unique | Privacy / masking | API owner | PO decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Registration | Email | Credential identity | Yes | UC-01 / D01 approved | No in this flow | Normalize; unique identity under shared auth contract | Do not expose existence in public response | Shared auth / `smart-platform-services` | Approved by D01 |
| Registration | Email OTP | Verify control of email | Yes | UC-01 / D01 approved | N/A | TTL/cooldown/attempts per D04 | Never log/store/render after use | Shared auth / `smart-platform-services` | Approved D04 |
| Registration | Display name | Owner-facing identity | Yes | D02 round 2 | N/A in registration; editable later | Validation/length/uniqueness pending | Display/masking pending | Profile API owner pending | Approved core |
| Registration | Phone | Optional contact | No | D02 round 2 | N/A in registration; editable later | Never credential/identity/unique; format pending | Masking/consent pending | Profile API owner pending | Approved core |
| Registration | Password + confirmation | Set credential | Yes | UC-01 | N/A | Composition policy per D04; confirmation must match | Never log/store/render after use | Shared auth / `smart-platform-services` | Approved D04 |
| Personal Profile | Display name | Owner-facing identity | Yes | D02 round 2 | Yes | Validation/length/uniqueness pending | Display/masking pending | Profile API owner pending | Approved core |
| Personal Profile | Avatar | Owner-facing presentation | Optional/display only | SmartTrọ current behavior | No update in phase one | Existing behavior is server avatar + fallback only | No upload/update in phase one; S3 not ready | Profile API owner pending | Approved phase-one behavior |
| Personal Profile | Verified email | Show credential identity | Yes | D01/D02 | No; separate future UC if change needed | Already normalized/unique via auth | Display/masking pending | Shared auth/profile bootstrap pending | Approved read-only |
| Personal Profile | Phone contact | Optional contact | No | D02 round 2 | Yes | Never credential/identity/unique; format pending | Masking/consent pending | Profile API owner pending | Approved core |

**Excluded from SmartChủ contract:** legacy US-04 fields `số phòng` and `tên nhà trọ hiện đang thuê` describe a renter relationship, conflict with the SmartChủ actor, and are explicitly out of the owner personal-profile contract. They must not be carried into an owner API/UI/migration.

### D03 - Account, personal profile and business verification boundary

| Question | Option A | Option B | Recommendation and trade-off | PO decision |
| --- | --- | --- | --- | --- |
| D03.1 Post-registration boundary | Email-verified account được Sign In/Home; business profile bắt đầu `NOT_SUBMITTED`, hoàn thiện ở UC-06/07 | Thu business profile ngay trong registration | **A:** đúng `SMC-BV-D01/D02`, giữ signup ngắn; cần Home CTA. **B:** dữ liệu sớm hơn nhưng mâu thuẫn flow UC-01 hiện tại và tăng friction. | **APPROVED A (PO round 1)** |
| D03.2 Access before approval | Cho login, Home, personal/business profile và read actions được policy cho phép; block create nhà/phòng/hợp đồng | Chặn toàn bộ Home/operational surfaces cho đến `APPROVED` | **A:** khớp policy Approved/UI states. **B:** đơn giản quyền nhưng mâu thuẫn policy hiện hành và không hỗ trợ completion journey. | **APPROVED A (PO round 1)** |
| D03.3 Legal-data review boundary | UC-07 submits an immutable, versioned snapshot of applicable legal fields + documents; later personal-profile edits do not mutate PENDING/APPROVED snapshots | Admin reviews mutable live profile data | **A:** preserves legal-review evidence and isolates personal-profile changes. **B:** breaks auditability and can alter data under review. | **APPROVED A (PO round 3)** |

### D04 - Session and password policy

| Question | Option A | Option B | Recommendation and trade-off | PO decision |
| --- | --- | --- | --- | --- |
| D04.1 Password composition and OTP/reset values | Adopt current UC drafts: password min 8 + upper + digit + special; email OTP/reset TTL 10 min, resend 60 sec, reset max 5 attempts | Adopt an explicit shared-platform policy with different values | **A:** có traceability hiện hữu. **B:** tránh SmartChủ-specific drift nhưng PO phải cung cấp version/value. Password composition is separate from storage algorithm. | **APPROVED (PO rounds 1-3)** |
| D04.2 Anti-enumeration and normal sign-in OTP | Generic public response; no OTP for normal Sign In | Reveal account state and/or require OTP normal Sign In | **A:** khớp UC-02/03 and lower friction. **B:** thay D01/UC and increases UX/service dependency. | **Conditionally approved A (PO round 1)** |
| D04.3 Session lifetime/refresh rotation/multi-device | Adopt documented shared-platform defaults; record exact reference/version | Define SmartChủ-specific duration/rotation/device cap | **A:** avoids divergence; current reference is missing and must be supplied. **B:** supports tailored risk model but creates independent contract/test burden. | **Conditionally approved A (PO round 1)** |
| D04.4 Sign-out and credential-change revocation | Sign Out revokes current session; Forgot Password and Change Password each revoke all sessions/refresh grants | Preserve current session after Change Password | **A:** latest PO decision; consistent containment for password recovery/change. **B:** is current backend behavior only and is now an implementation gap. | **APPROVED A (PO round 2)** |
| D04.5 Success route | Sign Up/Reset -> Sign In with email prefill, no auto-login; Change Password -> Sign In | Auto-login or Change Password -> Profile | **A:** latest PO decision. **B:** current backend returns Profile for Change Password and must be changed at later BE gate. | **APPROVED A (PO round 2)** |
| D04.6 Successful password-change frequency | Cooldown 5 minutes after a successful Change Password | Define another cap/window | Failure throttle remains a separate abuse control; legacy `2/day` is removed. | **APPROVED A (PO round 3)** |

#### D04 implementation reference (not a composition-policy decision)

PO reports current `smart-platform-services` `master` hashes passwords with salted adaptive `scrypt` (`N=16384`, `r=8`, `p=1`, key length `64`) serialized as `scrypt$...`. This supersedes no business rule: storage/hash algorithm is an implementation/security control distinct from D04.1 password composition. The legacy UC-08 SHA-256 statement is not a valid implementation baseline. Current backend behavior reported for `changePasswordForCurrentSession` preserves the current session, revokes other sessions, audits `currentSessionPreserved: true`, and returns `next: profile`; **this conflicts with D04.4/D04.5 approved behavior and is a BE implementation/test/docs gap for a later gate.** Failed-current-password attempts are throttled by current login defaults (`5/user` per `15 minutes`, `20/IP or device`, `15 minute` lock); the separate successful-change cooldown is now five minutes.

## 2.3. D05 design/reference packet

Auth reference hiện có: [`smartchu-auth-flow-canvas-2026-11-18.zip`](assets/auth/smartchu-auth-flow-canvas-2026-11-18.zip). Mapping: UC-02 dùng artboard `01`; UC-01 dùng `02–05`; UC-03 dùng `06–08`. Home/Profile reference: [`smartchu-home-profile-canvas-2026-11-20.zip`](assets/home-profile/smartchu-home-profile-canvas-2026-11-20.zip), gồm artboard `01 - Home` và `02 - Hồ sơ cá nhân`; ảnh capture đã được nhúng trong UC-02 và UC-04. ZIP là editable source, còn PNG trong screen specification là nguồn trực quan cho Dev/QA. Không đặt handoff canonical trong FRS mirror. Hai màn OTP dùng chung destination block `Mã xác thực đã được gửi tới` + email masked ở dòng riêng + `Đổi email`. Canvas chốt happy-path visual direction; loading/error/timeout/accessibility state vẫn phải được đặc tả khi mở FE gate.

FE foundation bắt buộc khi gate được mở: dùng `@ant-design/react-native` qua public contract `src/ui`; product screen không import vendor trực tiếp và không thêm full UI library thứ hai. Dev phải xác nhận đã hiểu visual scope, component/import boundary và BE invariant trước khi code; nếu còn ambiguity phải trả lại PM/PO để chốt, không tự diễn giải.

| Flow / screen | Exact missing state or reference | Current reference | UX question for PO |
| --- | --- | --- | --- |
| Sign Up - Email | format validation, submit loading, neutral duplicate/non-enumeration response, network error | Auth canvas artboard `02`; happy path approved | Define operational copy/state at FE gate without changing fields or CTA order |
| Sign Up - Email OTP | wrong/expired/attempt-limit, resend cooldown/loading, resend error, app return, restart | Auth canvas artboard `03`; destination block approved | Define timer/error/disabled states without exposing sensitive data |
| Sign Up - Personal info | validation/loading/error, back/continue behavior | Auth canvas artboard `04`; display name/optional phone approved | Define validation timing, masking and error placement at FE gate |
| Sign Up - Password | confirm mismatch, submit/loading/error, success -> Sign In prefill | Auth canvas artboard `05`; happy path approved | Define validation/error states; success behavior follows D04 |
| Sign In | field validation, loading, generic invalid credential, unverified-account resume, network error, Sign Out return | Auth canvas artboard `01`; Home/Quản lý happy path canvas `2026-11-20` | Define generic error, loading and session-return states without changing the approved Home/Quản lý layout |
| Forgot Password - Email | validation, neutral sent response, loading/network error | Auth canvas artboard `06`; happy path approved | Define neutral operational copy without changing three-screen flow |
| Forgot Password - OTP | wrong/expired/attempt-limit, resend cooldown/loading/error | Auth canvas artboard `07`; `Đổi email` and destination block approved | Define timer/resend/error hierarchy at FE gate |
| Forgot Password - New Password | policy/mismatch, submit/loading/error, success -> Sign In prefill | Auth canvas artboard `08`; happy path approved | Define completion/error states; navigation follows D04 |
| Home | verification banners/CTAs for four statuses, post-login loading/empty/error | Home happy-path canvas `2026-11-20` approved; route mapping for quick actions and operational states are not defined by the canvas | Define loading/error/empty and CTA destination at FE gate without changing the approved layout |
| Personal Profile view | display name, read-only email, optional phone, avatar display/fallback and account actions | UC-04 canvas `2026-11-20` approved and embedded in the UC | Operational loading/error state remains to be specified at FE gate |
| Personal Profile edit | display name, read-only email, optional editable phone, save/cancel/validation/loading/error | No UC-05 canonical canvas; AD still says phone cannot change, conflicting with approved editable-phone contract | Reconcile AD and provide UC-05 visual reference before FE handoff |
| Business tab placeholder | navigation, future-feature placeholder, loading/error/empty and user-facing copy | SmartTrọ has only a technical `Chữ ký` placeholder pattern; no Business tab/mapping | What non-technical copy/layout is approved? Do not copy SmartTrọ literal. |
| Change Password | current/new/confirm, validation/loading/success/error, other-device/session outcome | UC-08 legacy only; no canonical reference | What D04 revocation behavior and success route are approved? |

D05 is **PARTIALLY APPROVED** for Auth UC-01/02/03, Home và UC-04. UC-05/08 và operational states chưa được canvas mô tả vẫn pending; AD UC-05 còn conflict với quyết định phone editable. Không suy diễn hoặc mở FE/UI implementation gate nếu chưa có lệnh PO riêng. Editable canvas không thay BE/API/business rule.

## 3. Contract/acceptance scope sau khi PO chốt

| Bề mặt | Contract tối thiểu cần được PO duyệt trước handoff Dev/QA |
| --- | --- |
| Email identity | normalization, uniqueness, verified state, public error/message không enumeration, và ownership account |
| Registration/recovery | state transition Email -> OTP -> Password, expiry/cooldown/attempt limits được PO chốt, không lưu hoặc log credential nhạy cảm |
| Session | bootstrap/profile fields, duration/rotation, device scope, sign-out current/all, recovery/change-password revocation và route sau thành công |
| Personal profile | từng field, required/optional, editability, validation, privacy/masking và API ownership; không dùng phone legacy làm identity ngầm định |
| Business verification | `NOT_SUBMITTED`, `PENDING`, `APPROVED`, `REJECTED`; backend enforcement và UX CTA theo policy Approved |
| UI reference | link/node/capture và all screen states; không có reference thì issue phải ghi rõ là gap, không tự suy ra design |

### Testable acceptance criteria (policy-ready, no implementation gate)

| ID | Acceptance criterion |
| --- | --- |
| AC-LEGAL-01 | **Given** a landlord has submitted legal fields/documents for UC-07, **When** Admin reviews the submission, **Then** the system presents the immutable, versioned snapshot submitted for that review, **And** later personal-profile edits do not alter that PENDING or APPROVED snapshot. |
| AC-LEGAL-02 | **Given** a legal-bound field must change after a business snapshot exists, **When** the owner submits the change through the business process, **Then** the system creates a new business draft/version requiring resubmission under policy, **And** preserves the prior reviewed snapshot for traceability. |
| AC-PROFILE-01 | **Given** an authenticated SmartChủ owner edits a personal profile, **When** valid display name and optional phone are saved, **Then** the profile reflects those values, **And** phone remains editable, non-unique and unavailable as a credential. |
| AC-AVATAR-01 | **Given** an owner profile has an avatar value or lacks one, **When** the profile is displayed, **Then** the app shows the backend avatar when available or the fallback icon otherwise, **And** offers no image picker/upload/update in phase one. |
| AC-PASSWORD-01 | **Given** an owner has just completed Change Password successfully, **When** the owner requests another Change Password within five minutes, **Then** the system rejects the request with a clear message, **And** leaves password and session state unchanged. |
| AC-PASSWORD-02 | **Given** five minutes have elapsed since the last successful Change Password and submitted credentials are valid, **When** the owner changes password, **Then** the system processes the change under D04, revokes all sessions/refresh grants and routes the owner to Sign In. |
| AC-PASSWORD-03 | **Given** an owner submits an incorrect current password, **When** the failure threshold is reached, **Then** the existing failed-attempt throttle applies independently of the successful-change cooldown, **And** no password/session change occurs. |

## 4. Dependency and gate map

```text
PO chốt D01-D06 (G0)
  -> cập nhật living specs + field/API contract + canonical Figma reference
  -> FE/UI review
  -> PO review UI/contract
  -> BE/API implementation
  -> integration (shared auth + business-verification enforcement)
  -> QA system/regression
  -> PO UAT
```

- UC-01 -> UC-02/UC-03: dùng cùng email identity và password/session contract.
- UC-02 -> Home: cần post-login route và profile/session bootstrap; Home phải phản ánh business-verification policy.
- UC-04 -> Home: D02 field/sequence/avatar behavior và D05 happy-path canvas đã approved; operational states vẫn cần đặc tả khi mở FE gate.
- UC-05: D02 field contract đã approved nhưng D05 chưa có canvas và AD hiện ghi phone immutable, conflict với quyết định phone editable; phải reconcile trước FE handoff.
- UC-06 = xem thông tin/trạng thái kinh doanh; UC-07 = cập nhật/gửi duyệt hồ sơ kinh doanh. Full UC-06/07 không thuộc feature scope phase đầu nếu chưa có decision mở rộng. Phase đầu chỉ phụ thuộc minimal business-verification status/CTA trên Home/Profile theo D03.
- UC-10 = tạo hợp đồng điện tử; UC-18 = tạo nhà trọ; UC-22 = tạo phòng trọ. Chúng không thuộc feature scope phase đầu; chỉ được nhắc để bảo toàn backend authorization `businessVerificationStatus = APPROVED`, không mở Story/gate implementation.
- UC-08 -> D04: canonical Change Password revokes all sessions/refresh grants and routes to Sign In, with a five-minute successful-change cooldown. Current backend behavior is a later BE gap.
- Mobile thuộc scope phase đầu nhưng không build trong G0: sau docs/UI approval, preflight EAS project identity/config **read-only**, rồi Expo build exact merge SHA -> Mobile QA -> PO app UAT. Không yêu cầu/ghi token hoặc secret.

## 5. Readiness by story

| Story / UC | Readiness | Điều kiện để chuyển gate |
| --- | --- | --- |
| US/UC-01 Sign Up | Conditional | D01/D02/D04 policy và Auth happy-path canvas approved; operational states + explicit FE gate remain |
| US/UC-02 Sign In + Sign Out | Conditional | Auth happy-path canvas approved; operational states, Home route/bootstrap and shared auth reference remain |
| US/UC-03 Forgot Password | Conditional | D01/D04 policy và Auth happy-path canvas approved; operational states + explicit FE gate remain |
| Home | Conditional | Happy-path canvas approved; route mapping cho quick actions và operational states còn phải chốt trước FE handoff |
| UC-04 Personal Profile view | Conditional | Canonical UC/AD/canvas approved; operational states và explicit implementation gate còn lại |
| UC-05 Personal Profile edit | Blocked by docs/design conflict | Chưa có canvas; AD phone immutable phải được reconcile với approved phone editable |
| UC-06/07 Business verification | Minimal dependency only | Policy Approved/D03 giữ nguyên; full UC-06/07 là scope expansion pending, D05 chặn UI handoff |
| UC-08 Change Password | Conditional | D04 behavior/cooldown approved; D05 remains; later BE gap is recorded |
| UC-10/18/22 operational create | Out of phase-one feature scope | Không mở Story/gate; chỉ giữ backend authorization `APPROVED` theo policy |

## 6. Reconciliation record

| Nguồn | Tình trạng | Canonical disposition |
| --- | --- | --- |
| `use-cases/README.md` | Từng ghi sai tên UC-01/02 là phone và trạng thái Draft dù docs/design đã được duyệt | Đã sửa index thành canonical email flow và ghi rõ implementation gate chưa mở |
| `User-Stories.md`, `Requirements.md`, FRS legacy | Còn phone/SMS | Giữ nguyên provenance; các file tự ghi nhận là legacy/mirror và phải defer cho living spec approved |
| UC-01/02/03 | D01/D04 approved; D05 Auth happy-path canvas available, operational states còn review | Không coi canvas là implementation approval; chờ explicit FE gate |
| UC-04 | Canonical UC/AD/Home-Profile canvas thay baseline legacy renter fields | D02 behavior và D05 happy-path visual đã nhất quán; implementation gate vẫn đóng |
| UC-05/08 | Draft living specs round 3 thay baseline legacy phone/SHA-256/cooldown | D02/D04 canonical behavior đã ghi nhận; D05 còn chờ và UC-05 có AD conflict cần reconcile |

## 7. G0 disposition and handoff

**G0 = IN_REVIEW / PARTIAL_DESIGN_READY.** D01-D04 và D06 policy/sequence đã được PO chốt; D05 đã giải quyết happy-path Auth, Home và UC-04. UC-05/08, operational states và conflict AD UC-05 vẫn là blocker trước khi đánh giá G0 PASS. `CHANGE_REQUESTED` chỉ dùng sau khi PO từ chối/yêu cầu sửa proposal cụ thể. Không mở implementation gate nào.

**Next owner:** PO (Nghĩa Nguyễn Tuấn) cung cấp/chốt UC-05, UC-08 và operational states còn thiếu hoặc ra lệnh mở implementation gate; PM cập nhật chính package/task hiện có khi có quyết định. **No polling:** chỉ xử lý event wakeup cho PO comment; không poll trạng thái, PR hoặc hệ thống ngoài. Khi wakeup fire: PM đọc yêu cầu PO, cập nhật cùng G0/PR và ghi next action/wakeup tiếp theo; không tạo task G0 trùng.
