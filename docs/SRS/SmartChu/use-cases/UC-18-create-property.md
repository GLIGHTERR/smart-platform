# SmartChủ — UC-18 Tạo nhà trọ

## 1. Metadata

| Thuộc tính | Giá trị |
| --- | --- |
| Use Case | `UC-18` — Tạo nhà trọ |
| Actor | Chủ trọ |
| Trạng thái amendment | **Approved** |
| Ngày PO chốt | 2026-09-30 |
| Policy | [Chính sách xác minh kinh doanh SmartChủ](../../../../archieve/supplemental/Business_Rules/SmartChu/11-smartchu-business-verification-policy.md) |

## 2. Mục tiêu

Cho phép chủ trọ đã được xác minh kinh doanh tạo thông tin nhà trọ để quản lý tài sản cho thuê. MVP không cho tạo draft nhà trọ trước khi hồ sơ được duyệt.

## 3. Precondition

- Chủ trọ đã đăng nhập SmartChủ.
- `businessVerificationStatus = APPROVED`.

Các trường bắt buộc lịch sử gồm tên nhà trọ, số tầng, mô tả, địa chỉ, tỉnh/thành phố, phường/xã, giá điện và giá nước; contract field chi tiết phải được duyệt trong tài liệu UC/UI trước khi Dev triển khai.

## 4. Luồng chính

1. Chủ trọ mở danh sách nhà trọ.
2. FE nhận trạng thái `APPROVED` và cho phép chọn `Tạo nhà trọ`.
3. Chủ trọ nhập dữ liệu hợp lệ và xác nhận.
4. Backend kiểm tra lại quyền và trạng thái xác minh.
5. Hệ thống tạo nhà trọ thuộc đúng chủ trọ và trả về chi tiết/danh sách cập nhật.

## 5. Alternative Flow — chưa được duyệt

1. FE hiển thị message theo trạng thái `NOT_SUBMITTED`, `PENDING` hoặc `REJECTED`.
2. Người dùng được dẫn tới thông tin kinh doanh.
3. Không mở form và không tạo draft nhà trọ.

## 6. Acceptance Criteria

### AC-SMC-PR-01 — Tạo nhà trọ khi đã duyệt

- **Given** chủ trọ có trạng thái `APPROVED` và dữ liệu nhà trọ hợp lệ
- **When** xác nhận tạo
- **Then** nhà trọ được tạo đúng một lần và thuộc đúng tài khoản.

### AC-SMC-PR-02 — UI gate

- **Given** trạng thái khác `APPROVED`
- **When** người dùng chọn `Tạo nhà trọ`
- **Then** app không mở form tạo
- **And** hiển thị lý do/CTA xác minh phù hợp.

### AC-SMC-PR-03 — API gate

- **Given** trạng thái khác `APPROVED`
- **When** client gọi trực tiếp API tạo nhà trọ
- **Then** backend trả `BUSINESS_VERIFICATION_REQUIRED` với HTTP `403`
- **And** không ghi dữ liệu nhà trọ hoặc draft.
