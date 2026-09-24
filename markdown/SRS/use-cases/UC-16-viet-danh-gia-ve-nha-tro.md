# UC-16: Viết đánh giá về nhà trọ

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.17.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-16

### Use Case Name

Viết đánh giá về nhà trọ

### Description

Cho phép người dùng viết đánh giá về nhà trọ để bày tỏ cảm nhận cá nhân về nhà trọ

### Actor(s)

Registered Users

### Related Use Case

N/A

### Priority

1

### Trigger

Người dùng muốn đánh giá về nhà trọ

### Precondition

- PRE-01. Người dùng đã đăng nhập vào SmartTrọ
- PRE-02. Người dùng đang có hợp đồng với phòng trọ thuộc nhà trọ

### Post-condition

POS-01. Người dùng viết đánh giá thành công

### Basic Flow

1. Người dùng xem thông tin nhà trọ
1. Người dùng viết đánh giá cho nhà trọ

### Alternative Flow

N/A

### Exception Flow

1. Nếu có vấn đề trong việc truy cập màn hình
- EX-16.1. Hệ thống thông báo cho người dùng “Lỗi hệ thống”

### Business Rules

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
