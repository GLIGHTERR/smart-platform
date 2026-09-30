# UC-13: Xét duyệt yêu cầu hủy hợp đồng

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-13

### Use Case Name

Xét duyệt yêu cầu hủy hợp đồng

### Description

Cho phép người dùng xét duyệt yêu cầu hủy hợp đồng

### Trigger

Người dùng muốn xét duyệt yêu cầu hủy hợp đồng của người thuê

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-12, UC-14

### Precondition

PRE-01. Người dùng đang có yêu cầu hủy hợp đồng cần xét duyệt ở trang “Hợp đồng”, tab “Chờ duyệt”

### Post-condition

- POS-01. Hệ thống thông báo người dùng duyệt hoặc từ chối yêu cầu hủy hợp đồng thành công
- POS-02. Hệ thống lưu thay đổi vào DB
- POS-03. Hệ thống gửi thông báo cho người thuê về tình trạng xét duyệt của yêu cầu

### Basic Flow

1. Người dùng chọn 1 hợp đồng trên trang “Hợp đồng”, tab “Chờ duyệt”
1. Người dùng thực hiện xét duyệt yêu cầu hủy hợp đồng
1. Hệ thống thông báo người dùng đã duyệt/từ chối yêu cầu thành công

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
