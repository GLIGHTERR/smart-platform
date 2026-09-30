# UC-44: Xem lịch sử thanh toán

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-44

### Use Case Name

Xem lịch sử thanh toán

### Description

Cho phép người dùng xem lịch sử thanh toán tiền trọ theo khoảng thời gian

### Trigger

Người dùng muốn xem lịch sử thanh toán tiền trọ theo khoảng thời gian

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-45

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ
- PRE-02. Người dùng đã liên kết phương thức thanh toán

### Post-condition

POS-01. Hệ thống hiển thị lịch sử thanh toán tiền trọ của những người thuê trọ của người dùng

### Basic Flow

1. Người dùng truy cập trang “Thanh toán”
1. Người dùng bấm nút “Tra cứu giao dịch”
1. Hệ thống hiển thị lịch sử thanh toán tiền trọ của những người thuê trọ của người dùng trên trang “Lịch sử giao dịch”

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
