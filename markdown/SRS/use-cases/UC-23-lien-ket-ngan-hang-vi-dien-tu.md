# UC-23: Liên kết ngân hàng/ví điện tử

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.24.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-23

### Use Case Name

Liên kết ngân hàng/ví điện tử

### Description

Cho phép người dùng liên kết tài khoản ngân hàng/ví điện tử

### Actor(s)

Registered Users

### Related Use Case

UC-24, UC-25

### Priority

1

### Trigger

Người dùng muốn liên kết ngân hàng/ví điện tử với SmartTrọ

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartTrọ
- PRE-02. Người dùng phải có tài khoản ngân hàng/ví điện tử

### Post-condition

- POS-01. Hệ thống thông báo người dùng liên kết tài khoản ngân hàng/ví điện tử thành công
- POS-02. Hệ thống lưu thông tin liên kết vào DB

### Basic Flow

1. Màn hình hiển thị trang “Thanh toán”
1. Người dùng bấm nút “Liên kết ngân hàng/ví điện tử
1. Màn hình hiển thị trang “Liên kết ngân hàng/ví điện tử”
1. Người dùng bấm nút Thêm phương thức thanh toán
1. Màn hình hiển thị trang “Danh sách các loại ngân hàng/ví điện tử”
1. Người dùng chọn loại ngân hàng/ví điện tử
1. Người dùng nhập thông tin ngân hàng/ví điện tử
1. Hệ thống kiểm tra thông tin, nếu hợp lệ, lưu thông tin ngân hàng/ví điện tử được liên kết

### Alternative Flow

N/A

### Exception Flow

1. Tại bước 8, khi hệ thống phát hiện tài khoản ngân hàng/ví điện tử không hợp lệ
- EX-23.1. Hệ thống gửi thông báo thông tin tài khoản ngân hàng/ví điện tử không hợp lệ

### Business Rules

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
