# SmartChủ — UC-22 Tạo phòng trọ

## 1. Metadata

| Thuộc tính | Giá trị |
| --- | --- |
| Use Case | `UC-22` — Tạo phòng trọ |
| Actor | Chủ trọ |
| Trạng thái amendment | **Approved** |
| Ngày PO chốt | 2026-09-30 |
| Policy | [`../../11-smartchu-business-verification-policy.md`](../../11-smartchu-business-verification-policy.md) |

## 2. Mục tiêu

Cho phép chủ trọ đã được xác minh thêm phòng vào một nhà trọ thuộc quyền quản lý. MVP không cho tạo draft phòng trước khi hồ sơ kinh doanh được duyệt.

## 3. Precondition

- Chủ trọ đã đăng nhập.
- `businessVerificationStatus = APPROVED`.
- Nhà trọ đích đã tồn tại và thuộc quyền quản lý của chủ trọ.

Baseline lịch sử yêu cầu phòng trọ có hình ảnh đi kèm; các field chi tiết tiếp tục theo UC-22/UI được duyệt.

## 4. Luồng chính

1. Chủ trọ mở danh sách phòng của một nhà trọ.
2. FE cho phép chọn `Tạo phòng trọ` khi trạng thái xác minh là `APPROVED`.
3. Chủ trọ nhập thông tin, tải ảnh và xác nhận.
4. Backend kiểm tra lại trạng thái xác minh và quyền sở hữu nhà trọ.
5. Hệ thống tạo phòng đúng một lần trong đúng nhà trọ.

## 5. Acceptance Criteria

### AC-SMC-RM-01 — Tạo phòng hợp lệ

- **Given** tài khoản `APPROVED`, nhà trọ thuộc tài khoản và dữ liệu phòng hợp lệ
- **When** người dùng xác nhận
- **Then** phòng được tạo trong đúng nhà trọ.

### AC-SMC-RM-02 — Chặn chưa xác minh

- **Given** trạng thái khác `APPROVED`
- **When** người dùng chọn tạo phòng hoặc gọi API trực tiếp
- **Then** hệ thống không tạo phòng/draft
- **And** API trả `BUSINESS_VERIFICATION_REQUIRED` với HTTP `403`.

### AC-SMC-RM-03 — Chặn sai quyền sở hữu

- **Given** tài khoản `APPROVED` nhưng nhà trọ không thuộc tài khoản
- **When** gọi API tạo phòng
- **Then** backend từ chối theo authorization policy
- **And** không tiết lộ dữ liệu riêng của chủ trọ khác.
