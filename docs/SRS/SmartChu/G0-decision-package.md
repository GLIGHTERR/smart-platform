# SmartChủ G0 - Decision Package

> **Trạng thái:** CHANGE_REQUESTED - chờ PO chốt các quyết định D01-D06.
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
| D01 | Credential auth: email OTP cho Sign Up/Forgot Password; email + password cho Sign In, hoặc quay lại phone/SMS legacy | Chọn email theo UC-01/02/03 draft; phone chỉ là dữ liệu liên hệ nếu sau này được thu thập | **Pending** | UC-01/02/03, US-01/02/03, shared auth API | Auth UI/API/test contract không thể freeze |
| D02 | Owner profile: danh sách field, required/optional, mutable/immutable, validation, uniqueness, ownership và API/data mapping | Chốt tối thiểu bằng bảng field contract riêng; không suy diễn từ US-04/05 legacy | **Pending** | UC-04/05, profile bootstrap, Home | Profile UI/API và migration không thể mở |
| D03 | Boundary account/profile với business verification: thời điểm thu thập profile, quyền Home và feature vận hành | Giữ policy Approved: account email-verified khác `APPROVED`; chỉ `APPROVED` tạo nhà/phòng/hợp đồng | **Pending confirmation of phase scope** | UC-01, UC-06/07, UC-10/18/22, Home | Route/gating và response bootstrap chưa đủ contract |
| D04 | Session/password: policy password, OTP/reset TTL/cooldown/attempts, anti-enumeration, duration/rotation, multi-device, Sign Out current/all, revoke sau reset/change, post-success route | PO xác nhận hoặc sửa các giá trị/proposal trong UC-01/02/03; UC-08 legacy (kể cả SHA-256) không được dùng làm baseline | **Pending** | UC-01/02/03/08, auth/session API, security tests | Không thể chốt security acceptance criteria |
| D05 | UI/Figma: canonical URL/node/capture cho Sign Up (3 steps), Sign In, Forgot Password (3 steps), Home, UC-04/05/08 và state/loading/error | PO chỉ định nguồn Figma/capture versioned hoặc quyết định không thuộc phase | **Pending** | Tất cả screen G0 | Không thể handoff FE/UI fidelity |
| D06 | Sequencing: thứ tự Story và dependency shared auth/API, Home, profile/business verification, mobile delivery | Dùng map ở mục 4; chỉ mở gate kế tiếp sau PO approval hiển thị của D01-D06 liên quan | **Pending** | Toàn phase đầu | Không mở implementation gate |

## 2.1. Three distinct review groups

### A. Missing information / references

- **D05 design evidence:** repo có **không** Figma URL, node ID hoặc capture canonical cho auth, Home, personal profile và change-password. `FRS.md` là mirror legacy, không có auth/profile/Home detail dùng được làm design approval. `screens/business-verification-states.md` chỉ là textual UI state reference cho Home/business verification.
- **D02 profile contract:** thiếu inventory field của owner, source-of-truth cho mỗi field, ownership, validation, masking và API/data mapping.
- **D04 shared-auth contract:** chưa có quyết định platform-visible cho session duration, refresh rotation, multi-device, normal sign-out scope và change-password revocation.

### B. Conflicts between living specs and legacy

| Conflict | Canonical disposition pending PO approval | Impact |
| --- | --- | --- |
| UC-01/02/03 draft dùng email; User Stories, Requirement List và FRS legacy dùng phone/SMS | Living specs là proposal hiện hành; legacy được giữ làm provenance, không là implementation contract | D01, auth UI/API/test data |
| UC-05 legacy coi phone immutable; UC-01 draft chỉ coi phone là contact data nếu được thu thập | Không suy diễn phone identity hoặc profile field trước D02 | profile schema/UI |
| UC-08 legacy nêu SHA-256; UC-01 draft loại trừ SHA-256 thuần | Không dùng rule SHA-256 legacy; chờ D04 xác nhận shared password policy | security acceptance/BE |
| US-02 legacy có phone OTP/lockout 72h; UC-02 draft không OTP normal sign-in | Chờ D01/D04; không tự mang lockout/OTP legacy sang email flow | sign-in UX/API |

### C. Proposed defer / out of scope

| Nội dung | Disposition đề xuất | Impact / dependency |
| --- | --- | --- |
| Social sign-up, social-only recovery/linking | Defer - cần UC và policy riêng | Không tự link provider theo email trong UC-01/02/03 |
| Loại giấy tờ pháp lý, re-verification/expiry, thu hồi hồ sơ đã duyệt, draft trước approval | Out of G0/MVP theo business-verification policy | Không thay đổi `APPROVED` gate của UC-10/18/22 |
| Mobile chain Expo exact SHA -> Mobile QA -> PO app UAT | Conditional; chỉ áp dụng nếu PO đưa mobile vào phase | Cần target/merge SHA và môi trường trước QA |
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

### D03 - Account, personal profile and business verification boundary

| Question | Option A | Option B | Recommendation and trade-off | PO decision |
| --- | --- | --- | --- | --- |
| D03.1 Post-registration boundary | Email-verified account được Sign In/Home; business profile bắt đầu `NOT_SUBMITTED`, hoàn thiện ở UC-06/07 | Thu business profile ngay trong registration | **A:** đúng `SMC-BV-D01/D02`, giữ signup ngắn; cần Home CTA. **B:** dữ liệu sớm hơn nhưng mâu thuẫn flow UC-01 hiện tại và tăng friction. | Pending |
| D03.2 Access before approval | Cho login, Home, personal/business profile và read actions được policy cho phép; block create nhà/phòng/hợp đồng | Chặn toàn bộ Home/operational surfaces cho đến `APPROVED` | **A:** khớp policy Approved/UI states. **B:** đơn giản quyền nhưng mâu thuẫn policy hiện hành và không hỗ trợ completion journey. | Pending |

### D04 - Session and password policy

| Question | Option A | Option B | Recommendation and trade-off | PO decision |
| --- | --- | --- | --- | --- |
| D04.1 Password + OTP/reset values | Adopt current UC drafts: password min 8 + upper + digit + special; email OTP/reset TTL 10 min, resend 60 sec, reset max 5 attempts | Adopt an explicit shared-platform policy with different values | **A:** có traceability hiện hữu. **B:** tránh SmartChủ-specific drift nhưng PO phải cung cấp version/value. | Pending |
| D04.2 Anti-enumeration and normal sign-in OTP | Generic public response; no OTP for normal Sign In | Reveal account state and/or require OTP normal Sign In | **A:** khớp UC-02/03 and lower friction. **B:** thay D01/UC and increases UX/service dependency. | Pending |
| D04.3 Session lifetime/refresh rotation/multi-device | Adopt documented shared-platform defaults; record exact reference/version | Define SmartChủ-specific duration/rotation/device cap | **A:** avoids divergence; current reference is missing and must be supplied. **B:** supports tailored risk model but creates independent contract/test burden. | Pending |
| D04.4 Sign-out and credential-change revocation | Normal Sign Out = current session; Forgot Password and Change Password = revoke all sessions/refresh grants | Sign Out/credential changes revoke all sessions | **A:** matches UC-03 reset behavior and minimizes surprise on normal exit; Change Password still needs explicit approval. **B:** stronger containment but disrupts other devices. | Pending |
| D04.5 Success route | Sign Up/Reset -> Sign In with email prefill, no auto-login; Change Password route explicitly selected by PO | Auto-login after one or more flows | **A:** matches UC-01/03 drafts. **B:** smoother UX but changes session/security acceptance. | Pending |

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
- UC-06/07 -> UC-10/18/22: policy Approved đã chặn action vận hành, nhưng bootstrap/gating UI vẫn phụ thuộc D03 và D05.
- UC-08 -> D04: không dùng SHA-256 legacy; change-password revocation/rotation và route cần PO chốt.
- Nếu mobile thuộc scope: Expo exact merge SHA -> Mobile QA -> PO app UAT. Chưa có SHA/target hay quyết định scope nên không kích hoạt chain này.

## 5. Readiness by story

| Story / UC | Readiness | Điều kiện để chuyển gate |
| --- | --- | --- |
| US/UC-01 Sign Up | Conditional | D01, D04, D05 được PO chốt; shared auth contract được ghi lại |
| US/UC-02 Sign In + Sign Out | Conditional | D01, D03, D04, D05 được PO chốt; Home route/bootstrap rõ |
| US/UC-03 Forgot Password | Conditional | D01, D04, D05 được PO chốt |
| US/UC-04/05 Personal Profile | Blocked | D02 và D05 được PO chốt; thay baseline legacy bằng living spec/contract |
| UC-06/07 Business verification | Docs-ready, phase-scope pending | Policy Approved giữ nguyên; D03/D05 và scope phase phải rõ trước UI/API handoff |
| UC-08 Change Password | Blocked | D04/D05 được PO chốt; thay password storage rule legacy |
| UC-10/18/22 operational create | Dependency-held | Không mở trong G0; giữ gate `APPROVED` theo policy, chờ sequencing D06 |

## 6. Reconciliation record

| Nguồn | Tình trạng | Canonical disposition |
| --- | --- | --- |
| `use-cases/README.md` | Ghi sai tên UC-01/02 là phone dù link tới living spec email | Đã sửa index để chỉ rõ email draft/chờ G0 PO decision |
| `User-Stories.md`, `Requirements.md`, FRS legacy | Còn phone/SMS | Giữ nguyên provenance; các file tự ghi nhận là legacy/mirror và phải defer cho living spec approved |
| UC-01/02/03 | Email proposal nhưng còn PO review | Không coi là Approved cho implementation trước G0 |
| UC-04/05/08 | Baseline legacy, có phone/SHA-256 rule cũ | Không dùng làm contract phase đầu; cần D02/D04 |

## 7. G0 disposition and handoff

**G0 = CHANGE_REQUESTED.** Không có PO decision hiển thị cho D01-D06, do đó không mở implementation gate nào.

**Next owner:** PO (Nghĩa Nguyễn Tuấn) quyết định D01-D06 trên GLI-274; PM cập nhật chính package/PR này khi PO yêu cầu sửa. **No polling:** chỉ xử lý event wakeup do control plane đăng ký cho PO comment; không poll trạng thái, PR hoặc hệ thống ngoài. Khi wakeup fire: PM đọc yêu cầu PO, cập nhật cùng G0/PR, rồi đăng ký wakeup kế tiếp nếu vẫn còn quyết định chờ; không tạo task G0 trùng.
