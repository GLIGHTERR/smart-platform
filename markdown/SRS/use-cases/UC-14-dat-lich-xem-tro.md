# UC-14: Đặt lịch xem trọ

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.15.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-14

### Use Case Name

Đặt lịch xem trọ

### Description

Cho phép người dùng đặt lịch xem trọ

### Actor(s)

Registered Users

### Related Use Case

N/A

### Priority

1

### Trigger

Người dùng muốn đặt lịch xem phòng trọ trước khi thuê

### Precondition

PRE-01. Người dùng đã đăng nhập thành công vào SmartTrọ

### Post-condition

- POS-01. Hệ thống lưu thông tin đặt lịch
- POS-02. Hệ thống thông báo người dùng đặt lịch thành công
- POS-03. Hệ thống thông báo chủ trọ có người tới xem phòng

### Basic Flow

1. Màn hình hiển thị trang “Danh sách phòng”
1. Người dùng bấm chọn 1 phòng trọ
1. Màn hình hiển thị trang “Chi tiết phòng trọ”
1. Người dùng bấm nút “Đặt lịch”
1. Màn hình hiển thị pop-up Calendar
1. Người dùng chọn ngày giờ và bấm nút “Gửi”
1. Hệ thống thông báo người dùng đặt lịch thành công

### Alternative Flow

1. Tại bước 2, người dùng có thể đặt lịch luôn bằng cách
- AL-14.1. Người dùng bấm nút “Đặt lịch”
- AL-14.2. Tiếp tục tại bước 5 của Basic Flow

### Exception Flow

1. Tại bước 7, khi hệ thống phát hiện thời gian người dùng chọn trùng lịch với lịch của chủ trọ
- EX-14.1. Hệ thống gửi thông báo chủ trọ đã có lịch trong khoảng thời gian này

### Business Rules

BR-01. Thời gian chọn phải là tương lai so với thời điểm hiện tại

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
