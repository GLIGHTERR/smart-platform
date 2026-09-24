# UC-6: Đổi mật khẩu

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.7.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-6

### Use Case Name

Đổi mật khẩu

### Description

Cho phép người dùng đổi mật khẩu

### Actor(s)

Registered Users

### Related Use Case

UC-2

### Priority

1

### Trigger

Người dùng muốn đổi mật khẩu để tăng cường bảo mật cho tài khoản SmartTrọ của mình

### Precondition

PRE-01. Người dùng đã đăng nhập vào app SmartTrọ thành công

### Post-condition

POS-01. Hệ thống thông báo người dùng đổi mật khẩu thành công

### Basic Flow

1. Màn hình hiển thị trang “Tài khoản”, tab “Cá nhân”
1. Người dùng nhấn nút “Đổi mật khẩu”
1. Màn hình hiển thị trang “Đổi mật khẩu”
1. Người dùng nhập mật khẩu hiện tại, mật khẩu mới, xác nhận mật khẩu và nhấn nút “Đổi mật khẩu”
1. Hệ thống xác nhận các mật khẩu hợp lệ, lưu mật khẩu mới vào DB và thông báo người dùng đã đổi mật khẩu thành công

### Alternative Flow

N/A

### Exception Flow

1. Tại bước 5, khi hệ thống phát hiện mật khẩu hiện tại sai
- EX-06.1. Hệ thống gửi thông báo mật khẩu hiện tại sai

### Business Rules

- BR-01. Mật khẩu phải có ít nhất 8 ký tự
- BR-02. Mật khẩu phải có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số, 1 ký tự đặc biệt
- BR-03. Mật khẩu cũ và mật khẩu mới không được trùng nhau
- BR-04. Mật khẩu mới và xác nhận mật khẩu phải trùng nhau

### Non-functional Requirement

- NR-01. Thời gian phản hồi < 2 giây
- NR-02. Password phải được mã hóa bằng SHA-256

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
