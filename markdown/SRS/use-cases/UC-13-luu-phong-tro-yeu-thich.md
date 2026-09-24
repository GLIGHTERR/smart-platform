# UC-13: Lưu phòng trọ yêu thích

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.14.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-13

### Use Case Name

Lưu phòng trọ yêu thích

### Description

Cho phép người dùng lưu phòng trọ yêu thích

### Actor(s)

Registered Users

### Related Use Case

UC-10, UC-11

### Priority

1

### Trigger

Người dùng muốn lưu phòng trọ mà mình yêu thích vào danh sách yêu thích

### Precondition

PRE-01. Người dùng đã đăng nhập vào app SmartTrọ

### Post-condition

- POS-01. Phòng trọ được lưu vào danh sách yêu thích
- POS-02. Cập nhật của phòng trọ sẽ được thông báo tới người dùng sớm nhất

### Basic Flow

1. Màn hình hiển thị trang “Danh sách phòng”
1. Người dùng bấm chọn 1 phòng trọ
1. Màn hình hiển thị trang “Chi tiết phòng trọ”
1. Người dùng bấm icon “Lưu”

### Alternative Flow

1. Tại bước 2, người dùng có thể lưu bằng cách
- AL-13.1. Người dùng bấm icon “Lưu” trên góc của item phòng trọ

### Exception Flow

N/A

### Business Rules

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
