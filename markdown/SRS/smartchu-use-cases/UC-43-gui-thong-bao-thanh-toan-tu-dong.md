# UC-43: Gửi thông báo thanh toán tự động

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-43

### Use Case Name

Gửi thông báo thanh toán tự động

### Description

Cho phép người dùng gửi thông báo thanh toán tiền phòng trọ cho người thuê khi người dùng thiết lập khoản thu

### Trigger

Người dùng muốn gửi thông báo thanh toán tiền phòng trọ cho người thuê

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

POS-01. Hệ thống lưu lựa chọn và lịch gửi thông báo

### Basic Flow

1. Người dùng truy cập trang “Thanh toán”
1. Người dùng gạt switch “Gửi thông báo thanh toán tự động”
1. Hiển thị modal chọn ngày gửi thông báo
1. Người dùng chọn ngày và bấm nút “Lưu”
1. Hệ thống lưu lựa chọn và lịch gửi thông báo

### Alternative Flow

1. Tại bước 4, nếu người dùng muốn huỷ thao tác bật chức năng “Gửi thông báo thanh toán tự động”
- AL-43.1. Người dùng bấm nút “Huỷ”
- AL-43.2. Hệ thống đóng modal và hiển thị trạng thái cũ của switch

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
