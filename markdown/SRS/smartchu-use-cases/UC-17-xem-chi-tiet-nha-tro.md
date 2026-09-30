# UC-17: Xem chi tiết nhà trọ

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-17

### Use Case Name

Xem chi tiết nhà trọ

### Description

Cho phép người dùng xem thông tin chi tiết về nhà trọ của mình

### Trigger

Người dùng muốn xem thông tin chi tiết về nhà trọ của mình

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-16, UC-18, UC-19

### Precondition

PRE-01. Người dùng đã tạo nhà trọ

### Post-condition

POS-01. Người dùng xem được thông tin chi tiết về nhà trọ

### Basic Flow

1. Người dùng chọn 1 nhà trọ mà mình muốn xem thông tin chi tiết trên trang “Tòa nhà”
1. Hệ thống hiển thị trang “Danh sách phòng” của nhà trọ vừa chọn
1. Người dùng bấm nút “Thông tin”
1. Hệ thống hiển thị màn hình chứa thông tin chi tiết của nhà trọ

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
