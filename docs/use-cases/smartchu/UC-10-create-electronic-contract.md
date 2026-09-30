# SmartChủ — UC-10 Tạo hợp đồng điện tử — Business Verification Amendment

## 1. Metadata

| Thuộc tính | Giá trị |
| --- | --- |
| Use Case | `UC-10` — Tạo hợp đồng điện tử |
| Trạng thái amendment | **Approved** |
| Ngày PO chốt | 2026-09-30 |
| Policy | [`../../11-smartchu-business-verification-policy.md`](../../11-smartchu-business-verification-policy.md) |

## 2. Precondition bổ sung

- Chủ trọ đã đăng nhập.
- Hồ sơ kinh doanh của chủ trọ có trạng thái `APPROVED`.
- Các precondition khác về nhà trọ, phòng trọ, người thuê và dữ liệu hợp đồng vẫn được xác định trong UC hợp đồng tương ứng.

## 3. Gate behavior

- Nếu trạng thái khác `APPROVED`, FE không mở form tạo hợp đồng và dẫn tới màn thông tin kinh doanh với message phù hợp.
- Backend phải từ chối gọi API trực tiếp bằng `BUSINESS_VERIFICATION_REQUIRED`/HTTP `403`.
- Danh sách hợp đồng vẫn có thể hiển thị dữ liệu mà tài khoản được phép xem; gate chỉ áp dụng cho hành động tạo theo quyết định MVP này.

## 4. Acceptance Criteria bổ sung

### AC-SMC-CT-BV-01 — Chặn tài khoản chưa duyệt

- **Given** hồ sơ kinh doanh không phải `APPROVED`
- **When** chủ trọ chọn tạo hợp đồng hoặc gọi API tạo hợp đồng
- **Then** hệ thống không tạo draft hay hợp đồng mới
- **And** trả behavior xác minh kinh doanh thống nhất.

### AC-SMC-CT-BV-02 — Cho phép tài khoản đã duyệt

- **Given** hồ sơ kinh doanh là `APPROVED` và các precondition hợp đồng khác hợp lệ
- **When** chủ trọ bắt đầu tạo hợp đồng
- **Then** hệ thống cho phép đi tiếp vào flow UC-10.
