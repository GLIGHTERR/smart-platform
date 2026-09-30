# UC-14: Xóa hợp đồng điện tử

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-14

### Use Case Name

Xóa hợp đồng điện tử

### Description

Cho phép người dùng xóa hợp đồng điện tử của mình

### Trigger

Người dùng muốn xóa những hợp đồng không dùng tới

### Priority

1

### Business Rules

BR-01. Người dùng chỉ được xóa các hợp đồng ở trạng thái Chưa ký và chưa có chữ ký của người thuê hoặc các hợp đồng ở trạng thái Đã ký

### Actor(s)

Registered Users

### Related Use Case

UC-13

### Precondition

PRE-01. Người dùng đã có hợp đồng ở trạng thái Đã ký hoặc ở trạng thái Chưa ký và chưa có chữ ký của người thuê

### Post-condition

- POS-01. Hệ thống hiển thị thông báo người dùng đã xóa hợp đồng thành công
- POS-02. Hệ thống lưu thay đổi vào DB

### Basic Flow

1. Người dùng chọn hợp đồng muốn xóa trên trang “Hợp đồng”, tab “Chưa ký” hoặc “Đã ký”
1. Người dùng bấm nút “Xóa” và chọn “Đồng ý” trên modal hiển thị
1. Hệ thống thông báo người dùng đã xóa hợp đồng thành công và lưu thay đổi vào DB

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
