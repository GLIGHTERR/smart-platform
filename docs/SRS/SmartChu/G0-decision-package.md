# SmartChủ G0 - Decision Package

> **Trạng thái:** IN_REVIEW / AWAITING_PO_DECISIONS - PO đang chốt theo từng decision; không phải `CHANGE_REQUESTED`.
> **Phạm vi:** G0 PM/docs/decision cho phase đầu SmartChủ. Đây không phải implementation approval và không mở gate FE, BE, integration hoặc QA.
> **Traceability:** GLI-274; cập nhật từ snapshot `86d28400717a356bc91c3e5372ecff0dbf746729`.

## 1. Canonical source và nguyên tắc

- Living specs UC-01, UC-02, UC-03 là nguồn đề xuất email auth; các User Story/Requirement List/FRS có phone/SMS là baseline lịch sử, không phải contract triển khai khi xung đột.
- Chính sách xác minh kinh doanh SmartChủ đã **Approved** là nguồn duy nhất cho trạng thái và quyền vận hành; package này không thay đổi policy đó.
- UC-04, UC-05 và UC-08 hiện là baseline legacy, chưa đủ làm contract profile/password cho phase đầu.
- Không có Figma URL/node/capture SmartChủ canonical cho các screen G0 trong repo tại thời điểm lập package. Assets FRS legacy không thay thế design reference được duyệt.

## 2. Decision matrix - PO action required

| ID | Nhóm / lựa chọn cần chốt | Khuyến nghị dựa trên nguồn hiện có | PO decision | Ảnh hưởng | Blocker nếu chưa chốt |
| --- | --- | --- | --- | --- | --- |
| D01 | Credential auth: email OTP cho Sign Up/Forgot Password; email + password cho Sign In, hoặc quay lại phone/SMS legacy | Chọn email theo UC-01/02/03 draft; phone chỉ là dữ liệu liên hệ nếu sau này được thu thập | **APPROVED (PO round 1)** | UC-01/02/03, US-01/02/03, shared auth API | D04/D05 vẫn chặn implementation |
| D02 | Owner profile: danh sách field, required/optional, mutable/immutable, validation, uniqueness, ownership và API/data mapping | Chốt tối thiểu bằng bảng field contract riêng; không suy diễn từ US-04/05 legacy | **Pending** | UC-04/05, profile bootstrap, Home | Profile UI/API và migration không thể mở |
| D03 | Boundary account/profile với business verification: thời điểm thu thập profile, quyền Home và feature vận hành | Giữ policy Approved: account email-verified khác `APPROVED`; chỉ `APPROVED` tạo nhà/phòng/hợp đồng | **APPROVED Option A (PO round 1)**; UC-06/07 full scope pending separately | UC-01, Home, minimal status/CTA dependency | D05 chặn UI handoff |
| D04 | Session/password: policy password, OTP/reset TTL/cooldown/attempts, anti-enumeration, duration/rotation, multi-device, Sign Out current/all, revoke sau reset/change, post-success route | PO chấp thuận có điều kiện D04.1-3, D04.5; D04.4 cần xác nhận nuance backend hiện hành | **CONDITIONAL - awaiting D04.4 PO confirmation** | UC-01/02/03/08, auth/session API, security tests | Không thể chốt change-password acceptance criteria |
| D05 | UI/Figma: canonical URL/node/capture cho Sign Up (3 steps), Sign In, Forgot Password (3 steps), Home, UC-04/05/08 và state/loading/error | PO chỉ định nguồn Figma/capture versioned hoặc quyết định không thuộc phase | **Pending** | Tất cả screen G0 | Không thể handoff FE/UI fidelity |
| D06 | Sequencing: thứ tự Story và dependency shared auth/API, Home, profile/business verification, mobile delivery | Mobile thuộc phase đầu; sau docs/UI approval thực hiện preflight EAS read-only, rồi exact merge SHA -> Mobile QA -> PO app UAT | **PARTIALLY APPROVED (mobile in scope)** | Toàn phase đầu | D02/D04/D05 và docs/UI approval còn chờ; không build trong G0 |

## 2.1. Three distinct review groups

### A. Missing information / references

- **D05 design evidence:** repo có **không** Figma URL, node ID hoặc capture canonical cho auth, Home, personal profile và change-password. `FRS.md` là mirror legacy, không có auth/profile/Home detail dùng được làm design approval. `screens/business-verification-states.md` chỉ là textual UI state reference cho Home/business verification.
- **D02 profile contract:** thiếu inventory field của owner, source-of-truth cho mỗi field, ownership, validation, masking và API/data mapping.
- **D04 shared-auth contract:** session duration, refresh rotation và multi-device vẫn cần reference/version shared-platform; D04.4 đang chờ PO xác nhận nuance Change Password.

### B. Conflicts between living specs and legacy

| Conflict | Canonical disposition pending PO approval | Impact |
| --- | --- | --- |
| UC-01/02/03 draft dùng email; User Stories, Requirement List và FRS legacy dùng phone/SMS | **D01 approved:** email là canonical; legacy được giữ làm provenance, không là implementation contract | D01, auth UI/API/test data |
| UC-05 legacy coi phone immutable; UC-01 draft chỉ coi phone là contact data nếu được thu thập | Không suy diễn phone identity hoặc profile field trước D02 | profile schema/UI |
| UC-08 legacy nêu SHA-256; current backend dùng salted adaptive `scrypt` | Không dùng rule SHA-256 legacy; storage algorithm tách riêng password-composition policy | security acceptance/BE |
| US-02 legacy có phone OTP/lockout 72h; UC-02 draft không OTP normal sign-in | Chờ D01/D04; không tự mang lockout/OTP legacy sang email flow | sign-in UX/API |

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
| D02.1 Initial registration fields | Email + verification + password only; collect profile after sign-in | Collect personal profile fields during registration | **A:** khớp UC-01 flow và giảm registration friction; Home/Profile cần một completion state sau sign-in. **B:** dữ liệu sớm hơn nhưng tăng abandonment và cần design/API mới. | Pending |
| D02.2 Personal profile minimum scope | `display name` required; `avatar` optional; verified email read-only; phone omitted until separately specified | Same, nhưng phone là optional contact field, not credential/not unique identity | **A:** không suy diễn phone legacy. **B:** hỗ trợ liên hệ nhưng bắt buộc chốt validation, masking, editability và consent. | Pending |
| D02.3 Editability | Email immutable trong UC-05; đổi email là flow riêng nếu cần | Cho edit email ngay trong UC-05 | **A:** identity/session/audit đơn giản hơn. **B:** cần re-verification, uniqueness và session handling riêng. | Pending |
| D02.4 Profile/business ownership | Personal profile tách business profile; legal/business fields chỉ ở UC-06/07 | Gộp business fields vào profile registration | **A:** khớp business-verification policy và D03. **B:** tăng friction, đổi sequence policy/UI. | Pending |

PO cần trả lời cùng các field cụ thể nếu chọn option có phone hoặc field khác: required/optional, format/validation, uniqueness, editability, privacy/masking và API owner. Không có field nào được tự thêm vào contract.

#### Proposed D02 field contract - PO review required

| Surface | Field | Purpose | Required | Source | Editable | Validation / unique | Privacy / masking | API owner | PO decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Registration | Email | Credential identity | Yes | UC-01 / D01 approved | No in this flow | Normalize; unique identity under shared auth contract | Do not expose existence in public response | Shared auth / `smart-platform-services` | Approved by D01 |
| Registration | Email OTP | Verify control of email | Yes | UC-01 / D01 approved | N/A | TTL/cooldown/attempts per D04 | Never log/store/render after use | Shared auth / `smart-platform-services` | D04 conditional |
| Registration | Password + confirmation | Set credential | Yes | UC-01 | N/A | Composition policy per D04; confirmation must match | Never log/store/render after use | Shared auth / `smart-platform-services` | D04 conditional |
| Personal Profile | Display name | Owner-facing identity | Proposed yes | D02 proposal | Proposed yes | PO must specify format/length/uniqueness | PO must specify visibility/masking | Profile API owner pending | Pending |
| Personal Profile | Avatar | Owner-facing presentation | Proposed optional | D02 proposal | Proposed yes | PO must specify type/size/storage policy | PO must specify access/retention | Profile API owner pending | Pending |
| Personal Profile | Verified email | Show credential identity | Proposed read-only | D01 | No; change requires separate flow if added | Already normalized/unique via auth | PO to confirm display/masking | Shared auth/profile bootstrap pending | Pending display contract |
| Personal Profile | Phone contact | Optional contact only if PO elects | Pending | No canonical phase-one source | PO to decide | PO must specify format/uniqueness; never credential identity | PO must specify masking/consent | Profile API owner pending | Pending |

**Excluded from SmartChủ contract:** legacy US-04 fields `số phòng` and `tên nhà trọ hiện đang thuê` describe a renter relationship, conflict with the SmartChủ actor, and are explicitly out of the owner personal-profile contract. They must not be carried into an owner API/UI/migration.

### D03 - Account, personal profile and business verification boundary

| Question | Option A | Option B | Recommendation and trade-off | PO decision |
| --- | --- | --- | --- | --- |
| D03.1 Post-registration boundary | Email-verified account được Sign In/Home; business profile bắt đầu `NOT_SUBMITTED`, hoàn thiện ở UC-06/07 | Thu business profile ngay trong registration | **A:** đúng `SMC-BV-D01/D02`, giữ signup ngắn; cần Home CTA. **B:** dữ liệu sớm hơn nhưng mâu thuẫn flow UC-01 hiện tại và tăng friction. | **APPROVED A (PO round 1)** |
| D03.2 Access before approval | Cho login, Home, personal/business profile và read actions được policy cho phép; block create nhà/phòng/hợp đồng | Chặn toàn bộ Home/operational surfaces cho đến `APPROVED` | **A:** khớp policy Approved/UI states. **B:** đơn giản quyền nhưng mâu thuẫn policy hiện hành và không hỗ trợ completion journey. | **APPROVED A (PO round 1)** |

### D04 - Session and password policy

| Question | Option A | Option B | Recommendation and trade-off | PO decision |
| --- | --- | --- | --- | --- |
| D04.1 Password composition and OTP/reset values | Adopt current UC drafts: password min 8 + upper + digit + special; email OTP/reset TTL 10 min, resend 60 sec, reset max 5 attempts | Adopt an explicit shared-platform policy with different values | **A:** có traceability hiện hữu. **B:** tránh SmartChủ-specific drift nhưng PO phải cung cấp version/value. Password composition is separate from storage algorithm. | **Conditionally approved (PO round 1)** |
| D04.2 Anti-enumeration and normal sign-in OTP | Generic public response; no OTP for normal Sign In | Reveal account state and/or require OTP normal Sign In | **A:** khớp UC-02/03 and lower friction. **B:** thay D01/UC and increases UX/service dependency. | **Conditionally approved A (PO round 1)** |
| D04.3 Session lifetime/refresh rotation/multi-device | Adopt documented shared-platform defaults; record exact reference/version | Define SmartChủ-specific duration/rotation/device cap | **A:** avoids divergence; current reference is missing and must be supplied. **B:** supports tailored risk model but creates independent contract/test burden. | **Conditionally approved A (PO round 1)** |
| D04.4 Sign-out and credential-change revocation | Sign Out revokes current session; Forgot Password revokes all sessions and returns to Sign In; Change Password preserves current session, revokes other sessions and routes to Profile | Revoke all sessions for every sign-out/credential-change path | **A:** matches current backend behavior for `changePasswordForCurrentSession` and minimizes disruption; still needs explicit PO confirmation. **B:** stronger containment but disrupts the active user. | **Pending PO confirmation** |
| D04.5 Success route | Sign Up/Reset -> Sign In with email prefill, no auto-login; Change Password -> Profile | Auto-login after one or more flows | **A:** matches UC-01/03 drafts and current Change Password backend next route. **B:** smoother UX but changes session/security acceptance. | **Conditionally approved A (PO round 1)** |

#### D04 implementation reference (not a composition-policy decision)

PO reports current `smart-platform-services` `master` hashes passwords with salted adaptive `scrypt` (`N=16384`, `r=8`, `p=1`, key length `64`) serialized as `scrypt$...`. This supersedes no business rule: storage/hash algorithm is an implementation/security control distinct from D04.1 password composition. The legacy UC-08 SHA-256 statement is not a valid implementation baseline. Current backend behavior reported for `changePasswordForCurrentSession` preserves the current session, revokes other sessions, audits `currentSessionPreserved: true`, and returns `next: profile`; Forgot Password revokes all sessions.

## 2.3. D05 design/reference packet

| Flow / screen | Exact missing state or reference | Current reference | UX question for PO |
| --- | --- | --- | --- |
| Sign Up - Email | default, format validation, submit loading, neutral duplicate/non-enumeration response, network error | UC-01 text flow only; no Figma/capture | What copy, CTA order and recovery path are approved? |
| Sign Up - Email OTP | entry, wrong/expired/attempt-limit, resend cooldown/loading, resend error, app return, restart | UC-01 text rules only; no Figma/capture | How are timer, attempts, resend and restart represented without exposing sensitive data? |
| Sign Up - Password | policy hints, confirm mismatch, submit/loading/error, success -> Sign In prefill | UC-01 text flow only; no Figma/capture | What validation timing and success transition are approved? |
| Sign In | default, field validation, loading, generic invalid credential, unverified-account resume, network error, Sign Out return | UC-02 text flow only; no Figma/capture | What generic error copy, unverified route and Home post-login state are approved? |
| Forgot Password - Email | default, validation, neutral sent response, loading/network error, change-email affordance | UC-03 text flow only; no Figma/capture | What exact neutral copy and placement of `Nhập email khác` are approved? |
| Forgot Password - OTP | entry, wrong/expired/attempt-limit, resend cooldown/loading/error, change email | UC-03 text flow only; no Figma/capture | What timer/resend/error hierarchy is approved? |
| Forgot Password - New Password | policy/mismatch, submit/loading/error, success -> Sign In prefill | UC-03 text flow only; no Figma/capture | What completion copy and navigation are approved? |
| Home | verification banners/CTAs for four statuses, post-login loading/empty/error | `screens/business-verification-states.md` specifies four textual states; no Figma/node/capture | Which Home layout, loading/error/empty states and CTA destination are approved? |
| Personal Profile view/edit | all fields, read/edit/loading/save/error/empty states and privacy/masking | UC-04/05 legacy only; no canonical reference | What D02 field list and visual state set are approved? |
| Change Password | current/new/confirm, validation/loading/success/error, other-device/session outcome | UC-08 legacy only; no canonical reference | What D04 revocation behavior and success route are approved? |

If PO requests UX exploration, the handoff brief is this table plus the current textual references; Canvas Design may be used to review editable artboards side-by-side. It does not authorize a FE/UI task or implementation gate.

## 3. Contract/acceptance scope sau khi PO chốt

| Bề mặt | Contract tối thiểu cần được PO duyệt trước handoff Dev/QA |
| --- | --- |
| Email identity | normalization, uniqueness, verified state, public error/message không enumeration, và ownership account |
| Registration/recovery | state transition Email -> OTP -> Password, expiry/cooldown/attempt limits được PO chốt, không lưu hoặc log credential nhạy cảm |
| Session | bootstrap/profile fields, duration/rotation, device scope, sign-out current/all, recovery/change-password revocation và route sau thành công |
| Personal profile | từng field, required/optional, editability, validation, privacy/masking và API ownership; không dùng phone legacy làm identity ngầm định |
| Business verification | `NOT_SUBMITTED`, `PENDING`, `APPROVED`, `REJECTED`; backend enforcement và UX CTA theo policy Approved |
| UI reference | link/node/capture và all screen states; không có reference thì issue phải ghi rõ là gap, không tự suy ra design |

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
- UC-04/05 -> Home: chờ D02; không được suy diễn field từ user story legacy.
- UC-06 = xem thông tin/trạng thái kinh doanh; UC-07 = cập nhật/gửi duyệt hồ sơ kinh doanh. Full UC-06/07 không thuộc feature scope phase đầu nếu chưa có decision mở rộng. Phase đầu chỉ phụ thuộc minimal business-verification status/CTA trên Home/Profile theo D03.
- UC-10 = tạo hợp đồng điện tử; UC-18 = tạo nhà trọ; UC-22 = tạo phòng trọ. Chúng không thuộc feature scope phase đầu; chỉ được nhắc để bảo toàn backend authorization `businessVerificationStatus = APPROVED`, không mở Story/gate implementation.
- UC-08 -> D04: không dùng SHA-256 legacy; change-password revocation/rotation và route cần PO chốt.
- Mobile thuộc scope phase đầu nhưng không build trong G0: sau docs/UI approval, preflight EAS project identity/config **read-only**, rồi Expo build exact merge SHA -> Mobile QA -> PO app UAT. Không yêu cầu/ghi token hoặc secret.

## 5. Readiness by story

| Story / UC | Readiness | Điều kiện để chuyển gate |
| --- | --- | --- |
| US/UC-01 Sign Up | Conditional | D01 approved; D04.4/D05 và shared auth contract còn chờ |
| US/UC-02 Sign In + Sign Out | Conditional | D01/D03 approved; D04.4/D05, Home route/bootstrap còn chờ |
| US/UC-03 Forgot Password | Conditional | D01 approved; D04.4/D05 còn chờ |
| US/UC-04/05 Personal Profile | Blocked | D02 và D05 được PO chốt; thay baseline legacy bằng living spec/contract |
| UC-06/07 Business verification | Minimal dependency only | Policy Approved/D03 giữ nguyên; full UC-06/07 là scope expansion pending, D05 chặn UI handoff |
| UC-08 Change Password | Blocked | D04.4/D05 chờ PO; storage algorithm legacy đã bị thay thế bởi current implementation reference |
| UC-10/18/22 operational create | Out of phase-one feature scope | Không mở Story/gate; chỉ giữ backend authorization `APPROVED` theo policy |

## 6. Reconciliation record

| Nguồn | Tình trạng | Canonical disposition |
| --- | --- | --- |
| `use-cases/README.md` | Ghi sai tên UC-01/02 là phone dù link tới living spec email | Đã sửa index để chỉ rõ email draft/chờ G0 PO decision |
| `User-Stories.md`, `Requirements.md`, FRS legacy | Còn phone/SMS | Giữ nguyên provenance; các file tự ghi nhận là legacy/mirror và phải defer cho living spec approved |
| UC-01/02/03 | D01 email auth approved; D04/D05 còn review | Không coi là implementation approval trước G0 |
| UC-04/05/08 | Baseline legacy, có phone/SHA-256 rule cũ | Không dùng làm contract phase đầu; cần D02/D04. Legacy renter fields bị loại khỏi owner contract |

## 7. G0 disposition and handoff

**G0 = IN_REVIEW / AWAITING_PO_DECISIONS.** D01 và D03 đã approved; D04 còn chờ xác nhận D04.4; D02, D05 và phần D06 sequencing vẫn chờ decision/reference. `CHANGE_REQUESTED` chỉ dùng sau khi PO từ chối/yêu cầu sửa proposal cụ thể. Không mở implementation gate nào.

**Next owner:** PO (Nghĩa Nguyễn Tuấn) quyết định D01-D06 trên GLI-274; PM cập nhật chính package/PR này khi PO yêu cầu sửa. **No polling:** chỉ xử lý event wakeup do control plane đăng ký cho PO comment; không poll trạng thái, PR hoặc hệ thống ngoài. Khi wakeup fire: PM đọc yêu cầu PO, cập nhật cùng G0/PR, rồi đăng ký wakeup kế tiếp nếu vẫn còn quyết định chờ; không tạo task G0 trùng.
