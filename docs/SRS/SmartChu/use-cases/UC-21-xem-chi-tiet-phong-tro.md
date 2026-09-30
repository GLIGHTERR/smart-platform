# UC-21: Xem chi tiết phòng trọ

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-21

### Use Case Name

Xem chi tiết phòng trọ

### Description

Cho phép người dùng xem thông tin chi tiết của phòng trọ

### Trigger

Người dùng muốn xem thông tin chi tiết của phòng trọ mình đang sở hữu

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-20, UC-22, UC-23, UC-24

### Precondition

PRE-01. Người dùng đã tạo phòng trọ

### Post-condition

POS-01. Hệ thống hiển thị thông tin chi tiết về phòng trọ đã chọn

### Basic Flow

1. Người dùng chọn nhà trọ có phòng trọ mà người dùng muốn xem thông tin chi tiết
1. Hệ thống hiển thị màn hình “Danh sách phòng” của nhà trọ đã chọn
1. Người dùng chọn phòng trọ muốn xem thông tin chi tiết
1. Hệ thống hiển thị thông tin chi tiết về phòng trọ đã chọn

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
