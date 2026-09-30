# UC-45: Xuất hoá đơn điện tử

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-45

### Use Case Name

Xuất hoá đơn điện tử

### Description

Cho phép người dùng xuất hoá đơn điện tử

### Trigger

Người dùng muốn xuất hoá đơn điện tử cho những người thuê có nhu cầu xuất hoá đơn điện tử với các giao dịch thanh toán tiền trọ hàng tháng

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-44

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ
- PRE-02. Người dùng đã được người thuê thanh toán tiền trọ và giao dịch được hiển thị trên trang “Thanh toán”

### Post-condition

- POS-01. Hệ thống cho tải hoá đơn điện tử về thiết bị
- POS-02. Hệ thống lưu hoá đơn điện tử vào DB

### Basic Flow

1. Người dùng bấm chọn 1 giao dịch thành công trên trang “Lịch sử giao dịch” mà mình muốn xuất hoá đơn điện tử
1. Hiển thị trang “Chi tiết giao dịch”
1. Người dùng bấm nút “Xuất hoá đơn”
1. Hiển thị trang “Xuất hoá đơn”
1. Người dùng nhập các thông tin cần thiết cho hoá đơn điện tử và bấm nút “Hoàn thành”
1. Hệ thống validate các thông tin đã được nhập, lưu vào DB và hiển thị pop-up “Lưu hoá đơn điện tử”
1. Người dùng bấm nút “Lưu”
1. Hệ thống tải hoá đơn điện tử về thiết bị

### Alternative Flow

1. Tại bước 7, nếu người dùng muốn kết thúc việc xuất hoá đơn mà không muốn lưu hoá đơn về thiết bị
- AL-45.1. Người dùng bấm nút “Huỷ”
- AL-45.2. Màn hình trở về trang “Xuất hoá đơn”

### Exception Flow

1. Tại bước 6, nếu việc validate các thông tin trong hoá đơn trả về kết quả không hợp lệ
- EX-45.1. Hệ thống hiển thị thông báo lỗi “Các thông tin chưa hợp lệ” và trở về trang “Xuất hoá đơn”

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
