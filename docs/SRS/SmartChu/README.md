# SmartChủ — SRS và Use Case chuẩn

Đây là điểm vào duy nhất cho SRS SmartChủ.

- SRS tổng thể: [`SRS.md`](SRS.md)
- Danh mục và đặc tả từng UC: [`use-cases/`](use-cases/README.md)
- Requirement List: [`../../Requirement_List/SmartChu/Requirements.md`](../../Requirement_List/SmartChu/Requirements.md)
- User Stories: [`../../User_Stories/SmartChu/User-Stories.md`](../../User_Stories/SmartChu/User-Stories.md)
- FRS và mô tả màn hình: [`../../FRS/SmartChu/`](../../FRS/SmartChu/FRS.md)
- Chính sách xác minh hồ sơ kinh doanh: [`../../../archieve/supplemental/Business_Rules/SmartChu/11-smartchu-business-verification-policy.md`](../../../archieve/supplemental/Business_Rules/SmartChu/11-smartchu-business-verification-policy.md)
- UC review phía SmartAdmin: [`../SmartAdmin/use-cases/SMC-BV-ADM-01-review-business-profile.md`](../SmartAdmin/use-cases/SMC-BV-ADM-01-review-business-profile.md)

## Quy tắc canonical

- UC có living specification trong `use-cases/` dùng trực tiếp file đó làm nguồn triển khai.
- UC chưa được chuẩn hóa dùng bản chuyển đổi SRS nguồn trong cùng thư mục.
- Bản chuyển đổi nguyên trạng bị thay thế được lưu ở `archieve/source-derived/`, không tồn tại song song trong khu vực tài liệu hiện hành.
- Không tạo thêm một lớp UC khác ở `docs/use-cases/` hoặc `markdown/`.

## Trạng thái living specification hiện có

| Use Case | Tài liệu | Trạng thái |
| --- | --- | --- |
| UC-01 — Đăng ký bằng email | [`use-cases/UC-01-sign-up.md`](use-cases/UC-01-sign-up.md) | Draft — chờ PO review |
| UC-02 — Đăng nhập bằng email và mật khẩu | [`use-cases/UC-02-sign-in.md`](use-cases/UC-02-sign-in.md) | Draft — chờ PO review |
| UC-03 — Quên mật khẩu bằng Email OTP | [`use-cases/UC-03-forgot-password.md`](use-cases/UC-03-forgot-password.md) | Draft — chờ PO review |
| UC-06 — Xem thông tin kinh doanh | [`use-cases/UC-06-view-business-information.md`](use-cases/UC-06-view-business-information.md) | Approved — 2026-09-30 |
| UC-07 — Cập nhật/gửi duyệt thông tin kinh doanh | [`use-cases/UC-07-submit-business-verification.md`](use-cases/UC-07-submit-business-verification.md) | Approved — 2026-09-30 |
| UC-10 — Tạo hợp đồng điện tử | [`use-cases/UC-10-create-electronic-contract.md`](use-cases/UC-10-create-electronic-contract.md) | Approved amendment — 2026-09-30 |
| UC-18 — Tạo nhà trọ | [`use-cases/UC-18-create-property.md`](use-cases/UC-18-create-property.md) | Approved amendment — 2026-09-30 |
| UC-22 — Tạo phòng trọ | [`use-cases/UC-22-create-room.md`](use-cases/UC-22-create-room.md) | Approved amendment — 2026-09-30 |
