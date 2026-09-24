# UC-25: Thanh toán tự động

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.26.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-25

### Use Case Name

Thanh toán tự động

### Description

Cho phép người dùng đặt lịch thanh toán thường kỳ tự động

### Actor(s)

Registered Users

### Related Use Case

UC-23

### Priority

1

### Trigger

Người dùng muốn thanh toán tiền trọ hàng kỳ tự động

### Precondition

- PRE-01. Người dùng cần đảm bảo còn tiền trong tài khoản
- PRE-02. Người dùng đang có hợp đồng thuê trọ

### Post-condition

POS-01. Người dùng nhận thông báo thanh toán thành công mà không cần mở app lên

### Basic Flow

1. Người dùng truy cập trang “Thanh toán” từ Trang chủ
1. Người dùng truy cập trang “Đặt lịch thanh toán”
1. Người dùng chọn phương thức thanh toán
1. Người dùng chọn ngày thanh toán và vòng lặp (Mỗi tháng, mỗi quý, mỗi năm)
1. Người dùng xác nhận thao tác đặt lịch
1. Hệ thống lưu thông tin đặt lịch vào DB
1. Hệ thống kiểm tra log xem số dư tài khoản vào ngày thanh toán có đủ không, nếu đủ thì tiến hành thanh toán, hệ thống sẽ lưu log thông tin thành toán, lưu log webhook mà cổng thanh toán trả về.

### Alternative Flow

N/A

### Exception Flow

1. Tại bước 8, khi hệ thống phát hiện số dư vào ngày thanh toán không đủ
- EX-25.1. Hệ thống tạm dừng chức năng thanh toán tự động
1. Tại bước 8, khi hệ thống thanh toán gặp vấn đề và thanh toán không thành công
- EX-25.2. Hệ thống lưu thông tin thanh toán thất bại
- EX-25.3. Hệ thống lưu webhook thất bại cổng thanh toán gửi về
- EX-25.4. Hệ thống thực hiện rollback tiền về tài khoản người dùng

### Business Rules

BR-01. Nếu gặp mã lỗi ngân hàng bảo trì thì không phải chạy job thanh toán lại 3 lần

### Non-functional Requirement

- NR-01. Thời gian phản hồi < 2 giây
- NR-02. Giao dịch phải được mã hóa bằng SHA-256

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
