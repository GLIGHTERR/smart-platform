# UC-16: Xem danh sách nhà trọ

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-16

### Use Case Name

Xem danh sách nhà trọ

### Description

Cho phép người dùng xem danh sách nhà trọ của mình

### Trigger

Người dùng muốn xem danh sách nhà trọ mà mình sở hữu

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-17, UC-18

### Precondition

PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ

### Post-condition

POS-01. Hệ thống hiển thị danh sách nhà trọ mà người dùng sở hữu

### Basic Flow

1. Người dùng bấm nút “Tòa nhà” trên thanh điều hướng bên dưới cùng màn hình
1. Hệ thống hiển thị trang “Tòa nhà” cùng danh sách các nhà trọ mà người dùng sở hữu

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
