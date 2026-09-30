# UC-12: Cập nhật hợp đồng điện tử

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-12

### Use Case Name

Cập nhật hợp đồng điện tử

### Description

Cho phép người dùng cập nhật nội dung hợp đồng điện tử của mình

### Trigger

Người dùng muốn cập nhật nội dung hợp đồng của mình

### Priority

1

### Business Rules

BR-01. Chỉ được cập nhật các hợp đồng ở trạng thái Đã ký hoặc Chưa ký và chưa có chữ ký nào

### Actor(s)

Registered Users

### Related Use Case

UC-13

### Precondition

PRE-01. Người dùng đang sở hữu hợp đồng ở trạng thái Chưa ký và chưa có chữ ký nào trong hợp đồng hoặc hợp đồng ở trạng thái Đã ký

### Post-condition

- POS-01. Hệ thống thông báo người dùng cập nhật hợp đồng thành công
- POS-02. Hệ thống lưu thay đổi vào DB

### Basic Flow

1. Người dùng chọn 1 hợp đồng trên trang “Hợp đồng”, tab “Chưa ký” hoặc tab “Đã ký”
1. Người dùng bấm nút “Sửa”
1. Người dùng thực hiện cập nhật những thông tin trong hợp đồng và bấm nút “Lưu”
1. Hệ thống thông báo cập nhật hợp đồng thành công và trở về trang “Hợp đồng”, tab hiển thị hợp đồng

### Alternative Flow

1. Tại bước 3, nếu người dùng muốn hủy những thay đổi đã thực hiện
- AL-12.1. Người dùng bấm nút “Hủy”
- AL-12.2. Màn hình trở về trang “Hợp đồng”, tab hiển thị hợp đồng

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
