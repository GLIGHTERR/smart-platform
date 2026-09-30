# UC-24: Xem lịch sử thuê phòng

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-24

### Use Case Name

Xem lịch sử thuê phòng

### Description

Cho phép người dùng xem lịch sử cho thuê của phòng trọ

### Trigger

Người dùng muốn xem lịch sử cho thuê của phòng trọ của mình

### Priority

1

### Business Rules

- BR-01. Danh sách thông tin người thuê sắp xếp theo thứ tự cũ dần
- BR-02. Thông tin người thuê bao gồm thông tin cơ bản và hợp đồng mà họ đã ký để thuê phòng

### Actor(s)

Registered Users

### Related Use Case

UC-22

### Precondition

PRE-01. Người dùng đã tạo phòng trọ

### Post-condition

POS-01. Hệ thống hiển thị danh sách thông tin người thuê cùng với hợp đồng mà họ ký để thuê phòng, sắp xếp theo thứ tự cũ dần

### Basic Flow

1. Người dùng chọn phòng trọ mà mình muốn xem lịch sử cho thuê
1. Người dùng chọn tab “Người thuê”, bấm nút “Lịch sử thuê phòng”
1. Hệ thống hiển thị màn hình “Lịch sử thuê phòng”

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
