# SmartChủ — Use Case Living Specifications

Thư mục này là lớp tài liệu triển khai hiện hành cho các Use Case SmartChủ. Các file DOCX/XLSX gốc vẫn được giữ nguyên để truy vết lịch sử, nhưng các quyết định kỹ thuật/nghiệp vụ mới phải được phản ánh tại living spec tương ứng trước khi giao PM, Dev hoặc QA.

## Trạng thái

| Use Case | Tài liệu | Trạng thái |
| --- | --- | --- |
| UC-01 — Đăng ký bằng email | [`UC-01-sign-up.md`](UC-01-sign-up.md) | Draft — chờ PO review |
| UC-02 — Đăng nhập bằng email và mật khẩu | [`UC-02-sign-in.md`](UC-02-sign-in.md) | Draft — chờ PO review |
| UC-03 — Quên mật khẩu bằng Email OTP | [`UC-03-forgot-password.md`](UC-03-forgot-password.md) | Draft — chờ PO review |
| UC-06 — Xem thông tin kinh doanh | [`UC-06-view-business-information.md`](UC-06-view-business-information.md) | **Approved — 2026-09-30** |
| UC-07 — Cập nhật/gửi duyệt thông tin kinh doanh | [`UC-07-submit-business-verification.md`](UC-07-submit-business-verification.md) | **Approved — 2026-09-30** |
| UC-10 — Tạo hợp đồng điện tử | [`UC-10-create-electronic-contract.md`](UC-10-create-electronic-contract.md) | **Approved amendment — 2026-09-30** |
| UC-18 — Tạo nhà trọ | [`UC-18-create-property.md`](UC-18-create-property.md) | **Approved amendment — 2026-09-30** |
| UC-22 — Tạo phòng trọ | [`UC-22-create-room.md`](UC-22-create-room.md) | **Approved amendment — 2026-09-30** |

## Quy tắc nguồn

- SRS/FRS SmartChủ nguồn hiện còn mô tả auth bằng số điện thoại. Đây là baseline lịch sử, không phải behavior mục tiêu mới.
- Đề xuất hiện tại đưa SmartChủ về cùng identity platform đang vận hành: email normalized là định danh đăng nhập duy nhất; OTP 6 chữ số gửi qua email.
- Các quyết định được dùng chung với SmartTrọ chỉ có hiệu lực cho SmartChủ sau khi PO duyệt từng UC tại đây.
- Capture Figma SmartChủ phải được bổ sung vào đúng UC trước handoff FE; không dùng capture SmartTrọ thay thế.
- Chưa assign hoặc trigger PM/Dev/QA cho các parent SmartChủ cho tới khi PO review xong living spec.
- Xác minh email chỉ tạo tài khoản. Quyền tạo hợp đồng/nhà/phòng được điều khiển bởi [`../../11-smartchu-business-verification-policy.md`](../../11-smartchu-business-verification-policy.md) và chỉ mở khi hồ sơ kinh doanh là `APPROVED`.
- SmartAdmin review contract hiện được ghi tại [`../smartadmin/SMC-BV-ADM-01-review-business-profile.md`](../smartadmin/SMC-BV-ADM-01-review-business-profile.md).

## Trình tự thực hiện

`Docs/PO approval → FE UI + review build → BE → map API → QA → UAT`

Foundation local đã được đồng bộ từ `GLIGHTERR/smart-chu`. Foundation hiện chỉ là shell email/password; endpoint, UI và behavior phải được đối chiếu lại với living spec và `smart-platform-services` trước khi triển khai.
