# UC-05: Cập nhật thông tin cá nhân

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-5

### Use Case Name

Cập nhật thông tin cá nhân

### Description

Cho phép người dùng cập nhật thông tin cá nhân

### Trigger

Người dùng muốn thay đổi thông tin cá nhân của tài khoản của mình trên app

### Priority

1

### Business Rules

- BR-01. Không được cập nhật SĐT
- BR-02. 2 lần cập nhật thông tin kế nhau phải cách nhau ít nhất 1h

### Actor(s)

Registered Users

### Related Use Case

UC-4

### Precondition

PRE-01. Người dùng đã đăng nhập thành công

### Post-condition

- POS-01. Hệ thống thông báo người dùng cập nhật thành công thông tin của tài khoản
- POS-02. Hệ thống lưu thông tin cập nhật vào DB

### Basic Flow

1. Màn hình hiển thị trang “Tài khoản”, tab “Cá nhân”
1. Người dùng nhấn nút “Cập nhật”
1. Màn hình hiển thị trang “Cập nhật thông tin cá nhân”
1. Người dùng thay đổi các trường thông tin và bấm nút “Cập nhật”
1. Hệ thống lưu thông tin mới cập nhật, thông báo người dùng cập nhật thành công thông tin tài khoản và chuyển về trang “Tài khoản”, tab “Cá nhân”

### Alternative Flow

1. Tại bước 4, nếu người dùng không muốn lưu các thay đổi của mình
- AL-05.1. Người dùng bấm nút “Huỷ”
- AL-05.2. Màn hình trở về trang “Tài khoản”, tab “Cá nhân”

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
