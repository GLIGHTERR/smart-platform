# UC-27: Quản lý lịch hẹn

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-27

### Use Case Name

Quản lý lịch hẹn

### Description

Cho phép người dùng xem lịch hẹn đã duyệt dưới dạng lịch

### Trigger

Người dùng muốn xem những lịch hẹn xem phòng trọ đã duyệt

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-26

### Precondition

PRE-01. Người dùng đã đăng nhập vào SmartChủ

### Post-condition

POS-01. Người dùng thấy các lịch hẹn xem phòng được bố trí dưới dạng lịch

### Basic Flow

1. Người dùng truy cập trang “Lịch xem” từ Trang chủ
1. Người dùng bấm nút “Xem lịch”
1. Hệ thống hiển thị lịch cùng lịch hẹn trong các khung giờ đã đặt

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
