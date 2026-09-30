# UC-42: Gửi nhắc nhở đến hạn thanh toán

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-42

### Use Case Name

Gửi nhắc nhở đến hạn thanh toán

### Description

Cho phép người dùng gửi nhắc nhở đến hạn thanh toán 1 cách tự động

### Trigger

Người dùng muốn gửi thông báo nhắc nhở người thuê khi đến hạn thanh toán

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-41

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ
- PRE-02. Người dùng đã liên kết phương thức thanh toán

### Post-condition

POS-01. Hệ thống lưu lựa chọn, lịch và ghi chú nhắc nhở thanh toán

### Basic Flow

1. Người dùng truy cập trang “Thanh toán”
1. Người dùng gạt switch “Gửi nhắc nhở thanh toán”
1. Hiển thị modal chọn ngày gửi nhắc nhở và ghi chú
1. Người dùng chọn ngày, nhập ghi chú (nếu có) và bấm nút “Lưu”
1. Hệ thống lưu lựa chọn, lịch và ghi chú nhắc nhở thanh toán

### Alternative Flow

1. Tại bước 4, nếu người dùng muốn huỷ việc bật chức năng “Gửi nhắc nhở thanh toán”
- AL-42.1. Người dùng bấm nút “Huỷ”
- AL-42.2. Hệ thống đóng modal và hiển thị trạng thái cũ của switch

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
