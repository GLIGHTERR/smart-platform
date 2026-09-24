# UC-26: Nhận thông báo đến hạn

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.27.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-26

### Use Case Name

Nhận thông báo đến hạn

### Description

Cho phép người dùng nhận thông báo khi đến hạn thanh toán từ chủ trọ

### Actor(s)

Registered Users

### Related Use Case

UC-24, UC-25

### Priority

1

### Trigger

Người dùng muốn được nhận thông báo nhắc nhở thanh toán tiền trọ khi đến hạn thanh toán

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartTrọ
- PRE-02. Người dùng đang có hợp đồng thuê trọ

### Post-condition

POS-01. Người dùng nhận được thông báo thanh toán khi đến ngày deadline thanh toán chủ trọ đặt ra

### Basic Flow

1. Màn hình hiển thị trang “Thanh toán”
1. Người dùng gạt switch “Nhận thông báo đến hạn” để bật chức năng

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
