# UC-8: Ký hợp đồng điện tử

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.9.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-8

### Use Case Name

Ký hợp đồng điện tử

### Description

Cho phép người dùng ký hợp đồng điện tử

### Actor(s)

Registered Users

### Related Use Case

UC-7, UC-9

### Priority

1

### Trigger

Người dùng muốn ký hợp đồng điện tử để hoàn tất thủ tục thuê trọ

### Precondition

- PRE-01. Người dùng đã đăng nhập
- PRE-02. Người dùng đang mở “Hợp đồng điện tử” mà chủ trọ tạo
- PRE-03. Người dùng không có hợp đồng nào còn hạn hoặc chưa hủy

### Post-condition

- POS-01. Hệ thống thông báo ký hợp đồng điện tử thành công
- POS-02. Hệ thống lưu thông tin hợp đồng vào DB

### Basic Flow

1. Chủ trọ gửi link trang “Hợp đồng điện tử”
1. Người dùng mở link
1. Màn hình hiển thị trang “Hợp đồng điện tử”
1. Người dùng bấm vào vùng “Ký tại đây” trong hợp đồng
1. Người dùng thực hiện ký hợp đồng và nhấn nút “Lưu”
1. Hệ thống lưu thông tin hợp đồng điện tử vào DB và thông báo người dùng đã ký hợp đồng điện tử thành công

### Alternative Flow

1. Tại bước 3, nếu người dùng muốn ký lại
- AL-8.1. Người dùng bấm nút “Ký lại”
- AL-8.2. Người dùng tiếp tục như bước 3 tại Basic Flow
1. Tại bước 3, nếu người dùng muốn hủy thay đổi đã thực hiện
- AL-8.3. Người dùng bấm nút “Hủy”
- AL-8.4. Màn hình thoát khỏi trang “Hợp đồng điện tử”

### Exception Flow

N/A

### Business Rules

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
