# UC-41: Thiết lập khoản thu

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-41

### Use Case Name

Thiết lập khoản thu

### Description

Cho phép người dùng thiết lập khoản thu cho từng phòng trong nhà trọ

### Trigger

Người dùng muốn thiết lập khoản thu cho từng phòng trong nhà trọ của mình

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-42, UC-43

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ
- PRE-02. Người dùng đang có hợp đồng active với người thuê
- PRE-03. Người dùng đã liên kết phương thức thanh toán

### Post-condition

POS-01. Hệ thống lưu thông tin khoản thu vào DB và thông báo người dùng thiết lập khoản thu thành công

### Basic Flow

1. Người dùng truy cập trang “Thanh toán” từ Trang chủ
1. Người dùng bấm nút “Thiết lập khoản thu”
1. Hiển thị màn hình “Thiết lập khoản thu”
1. Người dùng bấm chọn nhà trọ và phòng trọ muốn thiết lập khoản thu
1. Hiển thị modal “Thiết lập khoản thu”
1. Nhập số điện, số nước, phụ thu và chú thích (nếu có) và bấm nút “Lưu”
1. Hệ thống lưu thông tin khoản thu vào DB và thông báo người dùng đã thiết lập khoản thu thành công

### Alternative Flow

1. Tại bước 6, nếu người dùng muốn huỷ việc thiết lập
- AL-41.1. Người dùng bấm nút “Huỷ”
- AL-41.2. Màn hình trở về trang “Thiết lập khoản thu”
1. Tại bước 7, nếu người dùng đã bật chức năng “Gửi thông báo thanh toán”
- AL-41.3. Hệ thống gửi thông tin khoản thu tới người thuê khi tới hạn

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
