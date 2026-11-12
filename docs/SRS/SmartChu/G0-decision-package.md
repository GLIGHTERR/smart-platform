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
