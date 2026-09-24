# UC-15: Nhắn tin với chủ trọ

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.16.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-15

### Use Case Name

Nhắn tin với chủ trọ

### Description

Cho phép người dùng nhắn tin với chủ trọ

### Actor(s)

Registered Users

### Related Use Case

N/A

### Priority

1

### Trigger

Người dùng muốn nhắn tin, liên lạc với chủ trọ dễ dàng hơn trên SmartTrọ

### Precondition

PRE-01. Người dùng đã đăng nhập thành công vào SmartTrọ

### Post-condition

- POS-01. Người dùng nhận được tin nhắn của chủ trọ
- POS-02. Người dùng gửi tin nhắn được cho chủ trọ

### Basic Flow

1. Màn hình hiển thị Trang chủ
1. Người dùng bấm nút “Tin nhắn”
1. Màn hình hiển thị trang “Tin nhắn”
1. Người dùng chọn chủ trọ, soạn tin nhắn và bấm nút “Gửi”
1. Hệ thống gửi tin nhắn tới cho chủ trọ

### Alternative Flow

N/A

### Exception Flow

N/A

### Business Rules

BR-01. Tin nhắn trong vòng 1024 kí tự

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
