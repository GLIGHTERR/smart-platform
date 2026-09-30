# UC-32: Xem danh sách báo cáo sự cố

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-32

### Use Case Name

Xem danh sách báo cáo sự cố

### Description

Cho phép người dùng xem danh sách báo cáo sự cố mà người thuê đã nêu lên

### Trigger

Người dùng muốn xem danh sách các báo cáo sự cố mà người thuê đã báo cáo

### Priority

1

### Business Rules

BR-01. Màn hình “Danh sách sự cố” có filter theo loại trang thiết bị, trạng thái và độ ưu tiên

### Actor(s)

Registered Users

### Related Use Case

UC-33, UC-34

### Precondition

PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ

### Post-condition

POS-01. Hệ thống hiển thị danh sách các báo cáo sự cố mà người dùng nhận được

### Basic Flow

1. Người dùng bấm nút “Sự cố” trên Trang Chủ
1. Hiển thị trang “Danh sách sự cố”

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
