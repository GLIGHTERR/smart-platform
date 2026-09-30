# SmartAdmin — SMC-BV-ADM-01 Xét duyệt hồ sơ kinh doanh SmartChủ

## 1. Metadata

| Thuộc tính | Giá trị |
| --- | --- |
| ID tạm cho living spec | `SMC-BV-ADM-01` |
| Actor | Admin có quyền xét duyệt SmartChủ |
| Trạng thái | **Approved** |
| Ngày PO chốt | 2026-09-30 |
| Policy | [`../../../../archieve/supplemental/Business_Rules/SmartChu/11-smartchu-business-verification-policy.md`](../../../../archieve/supplemental/Business_Rules/SmartChu/11-smartchu-business-verification-policy.md) |

ID này là mã traceability của living spec, không thay thế số UC SmartAdmin lịch sử nếu SRS SmartAdmin sau này bổ sung một ID chính thức.

## 2. Mục tiêu

Admin xem hồ sơ đang chờ, kiểm tra thông tin/tài liệu và đưa ra quyết định có audit trước khi chủ trọ được sử dụng các chức năng vận hành.

## 3. Precondition

- Admin đã đăng nhập và có permission xét duyệt hồ sơ SmartChủ.
- Hồ sơ mục tiêu đang `PENDING`.

## 4. Luồng duyệt

1. Admin mở danh sách hồ sơ `PENDING`.
2. Admin xem thông tin và file private của đúng version đang chờ.
3. Admin chọn `Approve`.
4. Backend kiểm tra version/concurrency và chuyển hồ sơ sang `APPROVED`.
5. Hệ thống lưu audit và gửi notification cho chủ trọ.

## 5. Luồng từ chối

1. Admin chọn `Reject`.
2. Hệ thống bắt buộc nhập lý do.
3. Backend chuyển hồ sơ sang `REJECTED`, lưu audit và lý do.
4. Hệ thống gửi notification; chủ trọ có thể sửa/gửi lại theo UC-07.

## 6. Acceptance Criteria

### AC-ADM-BV-01 — Duyệt có audit

- **Given** hồ sơ `PENDING` và Admin có quyền
- **When** Admin duyệt version hiện hành
- **Then** trạng thái là `APPROVED`
- **And** audit có Admin, thời điểm, action và version hồ sơ.

### AC-ADM-BV-02 — Từ chối có lý do

- **Given** hồ sơ `PENDING`
- **When** Admin chọn từ chối
- **Then** hệ thống không cho hoàn tất nếu thiếu lý do
- **And** sau khi hợp lệ, trạng thái là `REJECTED` và chủ trọ nhận được lý do phù hợp.

### AC-ADM-BV-03 — Concurrency

- **Given** version hồ sơ đã thay đổi hoặc đã được Admin khác xử lý
- **When** một quyết định cũ được gửi lên
- **Then** backend từ chối cập nhật stale
- **And** không ghi đè quyết định hiện hành.

### AC-ADM-BV-04 — Phân quyền file

- **Given** người dùng không có permission xét duyệt
- **When** yêu cầu xem file hồ sơ
- **Then** hệ thống từ chối và không trả URL tải hợp lệ.
