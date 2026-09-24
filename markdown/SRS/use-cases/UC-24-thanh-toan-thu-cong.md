# UC-24: Thanh toán thủ công

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.25.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-24

### Use Case Name

Thanh toán thủ công

### Description

Cho phép người dùng thanh toán tiền thuê trọ, theo dõi và tích hợp ngay trên app

### Actor(s)

Registered Users

### Related Use Case

UC-23

### Priority

1

### Trigger

Người dùng mong muốn thanh toán tiền trọ

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartTrọ
- PRE-02. Người dùng đang có hợp đồng thuê trọ

### Post-condition

- POS-01. Người dùng thanh toán thành công
- POS-02. Chủ trọ đã nhận được tiền

### Basic Flow

1. Người dùng truy cập trang “Thanh toán” từ Trang chủ
1. Người dùng chọn “Thanh toán tiền trọ” và chọn Thanh toán
1. Người dùng chọn phương thức thanh toán
1. Hệ thống lưu thông tin thanh toán và chuyển người dùng sang giao diện thanh toán của phương thức đã chọn
1. Người dùng tiến hành thanh toán
1. Hệ thống lưu webhook gửi lại từ cổng thanh toán
1. Nếu việc thanh toán thành công, hệ thống lưu log thanh toán thành công và redirect về màn hình thông báo thanh toán thành công

### Alternative Flow

1. Nếu người dùng đã đặt lịch nhắc thanh toán thì người dùng có thể:
- AL-24.1. Mở trang Thanh toán thông qua thông báo của điện thoại hoặc qua thông báo trên app
- AL-24.1. Tiếp tục từ bước 2 của Basic Flow

### Exception Flow

1. Tại bước 7, khi hệ thống phát hiện thanh toán không thành công
- EX-24.1. Hệ thống lưu log thanh toán thất bại
- EX-24.2. Hệ thống redirect về màn hình thống báo thanh toán thành công
- EX-24.3. Hệ thống thực hiện rollback tiền về cho tài khoản người dùng

### Business Rules

N/A

### Non-functional Requirement

- NR-01. Thời gian phản hồi < 2 giây
- NR-02. Giao dịch phải được mã hóa bằng SHA-256

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
