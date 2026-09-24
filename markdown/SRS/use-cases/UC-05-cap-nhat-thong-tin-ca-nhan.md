# UC-5: Cập nhật thông tin cá nhân

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.6.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-5

### Use Case Name

Cập nhật thông tin cá nhân

### Description

Cho phép người dùng cập nhật thông tin cá nhân

### Actor(s)

Registered Users

### Related Use Case

UC-4

### Priority

1

### Trigger

Người dùng muốn cập nhật thông tin cá nhân cho tài khoản SmartTrọ của mình

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

N/A

### Exception Flow

N/A

### Business Rules

BR-01. Không được cập nhật SĐT

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
