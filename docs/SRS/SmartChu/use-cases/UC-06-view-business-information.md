# SmartChủ — UC-06 Xem thông tin và trạng thái kinh doanh

## 1. Metadata

| Thuộc tính | Giá trị |
| --- | --- |
| Use Case | `UC-06` — Xem thông tin kinh doanh |
| Actor | Chủ trọ |
| Trạng thái | **Approved** |
| Ngày PO chốt | 2026-09-30 |
| Policy liên quan | [Chính sách xác minh kinh doanh SmartChủ](../../../../archieve/supplemental/Business_Rules/SmartChu/11-smartchu-business-verification-policy.md) |

## 2. Mục tiêu

Cho phép chủ trọ xem thông tin kinh doanh đã khai báo, trạng thái xét duyệt và hướng xử lý tiếp theo mà không cần suy đoán từ việc các chức năng khác có bị khóa hay không.

## 3. Precondition

- Chủ trọ đã đăng nhập thành công.

## 4. Luồng chính

1. Chủ trọ mở `Tài khoản` → tab `Kinh doanh` hoặc chọn CTA xác minh từ Home.
2. Hệ thống tải business profile thuộc đúng tài khoản hiện tại.
3. Hệ thống hiển thị thông tin đã khai báo và một trong bốn trạng thái MVP.
4. UI hiển thị CTA phù hợp:
   - `NOT_SUBMITTED`: `Hoàn thiện hồ sơ`;
   - `PENDING`: không cho gửi trùng, thông báo đang xét duyệt;
   - `REJECTED`: hiển thị lý do và `Cập nhật hồ sơ`;
   - `APPROVED`: hiển thị trạng thái đã xác minh.

## 5. Acceptance Criteria

### AC-SMC-BI-01 — Đúng trạng thái

- **Given** chủ trọ đã đăng nhập
- **When** mở thông tin kinh doanh
- **Then** trạng thái hiển thị khớp dữ liệu backend
- **And** không suy ra trạng thái chỉ từ dữ liệu cache trên client.

### AC-SMC-BI-02 — Lý do từ chối

- **Given** hồ sơ ở trạng thái `REJECTED`
- **When** màn hình tải thành công
- **Then** người dùng thấy lý do từ chối và CTA sửa/gửi lại
- **And** không thấy audit nội bộ không dành cho chủ trọ.

### AC-SMC-BI-03 — Phân quyền dữ liệu

- **Given** hai tài khoản chủ trọ khác nhau
- **When** một tài khoản gọi API xem hồ sơ
- **Then** chỉ hồ sơ thuộc tài khoản đó được trả về.
