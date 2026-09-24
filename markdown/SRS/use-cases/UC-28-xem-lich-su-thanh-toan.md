# UC-28: Xem lịch sử thanh toán

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.29.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-28

### Use Case Name

Xem lịch sử thanh toán

### Description

Cho phép người dùng xem lại lịch sử thanh toán của mình

### Actor(s)

Registered Users

### Related Use Case

UC-24, UC-25

### Priority

1

### Trigger

Người dùng muốn xem lịch sử thanh toán của mình

### Precondition

PRE-01. Người dùng đã đăng nhập thành công vào SmartTrọ

### Post-condition

POS-01. Người dùng thấy được danh sách những lần thanh toán của mình

### Basic Flow

1. Màn hình hiển thị trang “Thanh toán”
1. Người dùng bấm nút “Tra cứu giao dịch”
1. Màn hình hiển thị trang “Lịch sử giao dịch” cùng danh sách những lần thanh toán trước đây

### Alternative Flow

N/A

### Exception Flow

N/A

### Business Rules

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
