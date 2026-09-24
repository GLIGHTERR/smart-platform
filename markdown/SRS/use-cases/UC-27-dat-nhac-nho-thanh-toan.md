# UC-27: Đặt nhắc nhở thanh toán

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.28.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-27

### Use Case Name

Đặt nhắc nhở thanh toán

### Description

Cho phép người dùng đặt lịch nhắc nhở thanh toán tiền trọ

### Actor(s)

Registered Users

### Related Use Case

UC-24, UC-25

### Priority

1

### Trigger

Người dùng muốn đặt lịch được hệ thống gửi thông báo nhắc nhở thanh toán tiền trọ khi tới kỳ hạn thanh toán

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartTrọ
- PRE-02. Người dùng đang có hợp đồng thuê trọ

### Post-condition

POS-01. Người dùng nhận được thông báo thanh toán khi đến ngày setup người dùng tự đặt ra

### Basic Flow

1. Màn hình hiển thị trang “Thanh toán”
1. Người dùng bấm vào icon “Đặt nhắc nhở thanh toán” trên trang “Thanh toán”
1. Màn hình hiển thị pop-up Calendar Đặt nhắc nhở thanh toán
1. Người dùng chọn ngày giờ và bấm nút “Xác nhận”

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
