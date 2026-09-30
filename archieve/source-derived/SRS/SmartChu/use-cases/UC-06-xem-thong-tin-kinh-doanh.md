# UC-06: Xem thông tin kinh doanh

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Amendment / living implementation spec hiện hành

- [Living spec UC-06](../../../../../docs/SRS/SmartChu/use-cases/UC-06-view-business-information.md)
- Nội dung nguồn bên dưới được giữ nguyên để truy vết. Khi triển khai và kiểm thử, quyết định Approved trong living spec được ưu tiên nếu có khác biệt.
- [Chính sách xác minh kinh doanh SmartChủ](../../../../supplemental/Business_Rules/SmartChu/11-smartchu-business-verification-policy.md)

## Đặc tả nguồn

### Use Case ID

UC-6

### Use Case Name

Xem thông tin kinh doanh

### Description

Cho phép người dùng xem thông tin kinh doanh cho thuê trọ đối với các nhà trọ đã đăng ký trên hệ thống

### Trigger

Người dùng muốn xem thông tin đăng ký kinh doanh của tài khoản của mình

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-7

### Precondition

PRE-01. Người dùng đã đăng nhập thành công

### Post-condition

POS-01. Người dùng xem được thông tin kinh doanh của tài khoản

### Basic Flow

1. Màn hình hiển thị trang “Tài khoản”, tab “Kinh doanh”
1. Người dùng có thể thấy thông tin kinh doanh của tài khoản của mình tại đây

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
