# UC-30: Nhắn tin với người thuê

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-30

### Use Case Name

Nhắn tin với người thuê

### Description

Cho phép người dùng nhắn tin với những người thuê có tài khoản trên SmartTrọ

### Trigger

Người dùng muốn nhắn tin, giao tiếp với người thuê

### Priority

1

### Business Rules

BR-01. Người dùng có thể gửi tin nhắn, hình ảnh, video, file và đường link

### Actor(s)

Registered Users

### Related Use Case

UC-15

### Precondition

PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ

### Post-condition

- POS-01. Người dùng nhận được tin nhắn của người thuê
- POS-02. Người dùng gửi được tin nhắn cho người thuê

### Basic Flow

1. Người dùng bấm nút “Tin nhắn” từ thanh điều hướng bên dưới cùng màn hình
1. Hệ thống hiển thị trang “Tin nhắn”
1. Người dùng tìm chọn liên hệ cần nhắn tin, soạn tin nhắn và bấm nút “Gửi”
1. Hệ thống lưu tin nhắn và gửi cho liên hệ đã chọn

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
