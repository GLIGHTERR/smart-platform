# UC-09: Xem hợp đồng điện tử

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-9

### Use Case Name

Xem hợp đồng điện tử

### Description

Cho phép người dùng xem danh sách hợp đồng điện tử của mình

### Trigger

Người dùng muốn xem danh sách các hợp đồng điện tử của mình

### Priority

1

### Business Rules

BR-01. Khi truy cập trang, người dùng mặc định được điều hướng tới tab “Tất cả”

### Actor(s)

Registered Users

### Related Use Case

UC-10, UC-11

### Precondition

PRE-01. Người dùng đã đăng nhập thành công

### Post-condition

POS-01. Người dùng thấy được danh sách những hợp đồng điện tử của mình

### Basic Flow

1. Người dùng nhấn nút “Hợp đồng” trên thanh điều hướng bên dưới cùng màn hình
1. Màn hình hiển thị trang “Hợp đồng”

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
