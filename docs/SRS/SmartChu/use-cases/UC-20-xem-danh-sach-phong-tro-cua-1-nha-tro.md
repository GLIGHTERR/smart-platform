# UC-20: Xem danh sách phòng trọ (của 1 nhà trọ)

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-20

### Use Case Name

Xem danh sách phòng trọ (của 1 nhà trọ)

### Description

Cho phép người dùng xem danh sách phòng trọ của 1 nhà trọ

### Trigger

Người dùng muốn xem danh sách phòng trọ thuộc 1 nhà trọ cụ thể của mình

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-18, UC-21, UC-22, UC-23

### Precondition

PRE-01. Người dùng đã tạo toà nhà

### Post-condition

POS-01. Người dùng thấy được danh sách phòng trọ thuộc 1 nhà trọ của mình

### Basic Flow

1. Người dùng chọn 1 nhà trọ trên trang “Toà nhà” để xem danh sách phòng của nhà trọ đó
1. Hệ thống hiển thị danh sách phòng trọ thuộc nhà trọ người dùng vừa chọn

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
