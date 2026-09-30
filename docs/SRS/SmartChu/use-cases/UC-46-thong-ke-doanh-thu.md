# UC-46: Thống kê doanh thu

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-46

### Use Case Name

Thống kê doanh thu

### Description

Cho phép người dùng thống kê doanh thu trong khoảng thời gian nhất định

### Trigger

Người dùng muốn thống kê lại doanh thu cho thuê nhà trọ trong 1 khoảng thời gian nhất định

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-44

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ
- PRE-02. Người dùng đã được người thuê thanh toán tiền trọ và giao dịch được hiển thị trên trang “Thanh toán”

### Post-condition

POS-01. Hệ thống hiển thị các key metrics và charts thống kê doanh thu của người dùng trong khoảng thời gian đã lọc

### Basic Flow

1. Người dùng truy cập vào trang “Thống kê”
1. Người dùng bấm chọn tab “Doanh thu”
1. Hệ thống hiển thị các key metrics và charts thống kê doanh thu của người dùng trong khoảng thời gian đã lọc

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
