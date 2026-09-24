# UC-18: Xem các báo cáo đã tạo

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.19.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-18

### Use Case Name

Xem các báo cáo đã tạo

### Description

Cho phép người dùng xem lại danh sách các báo cáo đã tạo

### Actor(s)

Registered Users

### Related Use Case

UC-17, UC-19, UC-20, UC-21

### Priority

1

### Trigger

Người dùng có nhu cầu muốn xem lại danh sách các báo cáo hỏng hóc mà mình đã tạo

### Precondition

PRE-01. Người dùng đã đăng nhập SmartTrọ

### Post-condition

POS-01. Người dùng thấy được danh sách báo cáo mà mình đã tạo

### Basic Flow

1. Người dùng truy cập vào màn hình “Báo cáo” từ Trang chủ
1. Người dùng có thể thấy được danh sách báo cáo và trạng thái của báo cáo

### Alternative Flow

N/A

### Exception Flow

1. Tại bước 2, nếu người dùng chưa gửi đi bất kì báo cáo nào:
- EX-18.1. Hệ thống trả về thông báo không có dữ liệu hiển thị

### Business Rules

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
