# UC-19: Tạo báo cáo sự cố

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.20.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-19

### Use Case Name

Tạo báo cáo sự cố

### Description

Cho phép người dùng tạo báo cáo sự cố hỏng hóc trong phòng trọ

### Actor(s)

Registered Users

### Related Use Case

UC-18, UC-20, UC-21

### Priority

1

### Trigger

Người dùng muốn tạo báo cáo sự cố hỏng hóc của phòng trọ

### Precondition

- PRE-01. Người dùng đã đăng nhập vào SmartTrọ
- PRE-02. Người dùng đang có hợp đồng với 1 phòng trọ

### Post-condition

- POS-01. Hệ thống thông báo đã tạo báo cáo thành công
- POS-02. Người dùng thấy được báo cáo đã tạo trong danh sách báo cáo

### Basic Flow

1. Người dùng truy cập màn hình “Báo cáo” từ Trang chủ
1. Người dùng điều hướng sang tab “Sự cố”
1. Người dùng thực hiện thao tác tạo mới
1. Người dùng nhập thông tin cần cho báo cáo
1. Người dùng tạo báo cáo cho chủ trọ
1. Hệ thống lưu, thông báo báo cáo đã được tạo và gửi cho chủ trọ thành công

### Alternative Flow

N/A

### Exception Flow

1. Tại bước 6, nếu hệ thống có vấn đề về việc lưu báo cáo hay gửi thông báo cho chủ trọ
- EX-19.1. Hệ thống thông báo “Lỗi hệ thống”

### Business Rules

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
