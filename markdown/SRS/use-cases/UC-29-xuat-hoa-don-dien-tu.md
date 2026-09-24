# UC-29: Xuất hóa đơn điện tử

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.30.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-29

### Use Case Name

Xuất hóa đơn điện tử

### Description

Cho phép người dùng xuất hóa đơn điện tử

### Actor(s)

Registered Users

### Related Use Case

UC-24, UC-25

### Priority

1

### Trigger

Người dùng muốn xuất hoá đơn điện tử cho giao dịch thanh toán tiền trọ mà mình muốn

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartTrọ
- PRE-02. Người dùng đang có hợp đồng thuê trọ
- PRE-03. Người dùng đã có phát sinh giao dịch trước đấy

### Post-condition

POS-01. Người dùng xuất được hóa đơn điện tử

### Basic Flow

1. Màn hình hiển thị trang “Thanh toán”
1. Người dùng bấm nút “Tra cứu giao dịch”
1. Màn hình hiển thị trang “Lịch sử giao dịch” cùng danh sách những lần thanh toán trước đây
1. Người dùng chọn vào 1 giao dịch đã hoàn thành
1. Màn hình hiển thị trang “Chi tiết giao dịch”
1. Người dùng bấm nút “Xuất hóa đơn điện tử”
1. Màn hình hiển thị trang “Xuất hóa đơn”
1. Người dùng nhập các thông tin cần thiết cho hóa đơn điện tử cần xuất
1. Người dùng bấm nút “Hoàn thành”
1. Hệ thống validate các thông tin đã được nhập
1. Màn hình hiển thị pop-up “Lưu hóa đơn điện tử”
1. Người dùng bấm nút “Lưu”
1. Hệ thống thực hiện tải hóa đơn điện tử về thiết bị

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
