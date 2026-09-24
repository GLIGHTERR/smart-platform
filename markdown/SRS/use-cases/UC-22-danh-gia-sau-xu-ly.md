# UC-22: Đánh giá sau xử lý

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.23.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-22

### Use Case Name

Đánh giá sau xử lý

### Description

Cho phép người dùng đánh giá kết quả sau khi chủ trọ xử lý sự cố

### Actor(s)

Registered Users

### Related Use Case

N/A

### Priority

1

### Trigger

Người dùng muốn gửi đánh giá cá nhân về kết quả xử lý sự cố cho chủ trọ

### Precondition

- PRE-01. Người dùng đã đăng nhập vào SmartTrọ
- PRE-02. Người dùng đang có hợp đồng với 1 phòng trọ
- PRE-03. Người dùng có báo cáo chưa hết hạn và đã được hoàn thành

### Post-condition

POS-01. Hệ thống lưu đánh giá và gửi thông báo cho chủ trọ

### Basic Flow

1. Người dùng truy cập màn hình “Báo cáo” từ Trang chủ
1. Người dùng điều hướng sang tab “Sự cố”
1. Người dùng chọn mở 1 báo cáo chưa hết hạn và đã hoàn thành
1. Người dùng tiến hành vote theo từng tiêu chí và có thể để lại lời note
1. Người dùng tiến hành gửi đánh giá cho chủ trọ
1. Hệ thống lưu thông tin đánh giá và gửi thông tin cho phía chủ trọ

### Alternative Flow

N/A

### Exception Flow

1. Tại bước 6, nếu hệ thống có vấn đề về việc lưu đánh giá hay gửi thông báo cho chủ trọ
- EX-22.1. Hệ thống thông báo “Lỗi hệ thống”

### Business Rules

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
