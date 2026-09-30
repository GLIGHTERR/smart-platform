# UC-08: Đổi mật khẩu

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-8

### Use Case Name

Đổi mật khẩu

### Description

Cho phép người dùng đổi mật khẩu

### Trigger

Người dùng muốn thay đổi mật khẩu của mình

### Priority

1

### Business Rules

- BR-01. Mật khẩu phải có ít nhất 8 ký tự
- BR-02. Mật khẩu phải có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số, 1 ký tự đặc biệt
- BR-03. Mật khẩu cũ và mật khẩu mới không được trùng nhau
- BR-04. Mật khẩu mới và xác nhận mật khẩu phải trùng nhau
- BR-05. Mật khẩu được đổi tối đa 2 lần 1 ngày

### Actor(s)

Registered Users

### Related Use Case

UC-2

### Precondition

PRE-01. Người dùng đã đăng nhập vào app SmartChủ thành công

### Post-condition

POS-01. Hệ thống thông báo người dùng đổi mật khẩu thành công

### Basic Flow

1. Màn hình hiển thị trang “Tài khoản”, tab “Cá nhân”
1. Người dùng nhấn nút “Đổi mật khẩu”
1. Màn hình hiển thị trang “Đổi mật khẩu”
1. Người dùng nhập mật khẩu hiện tại, mật khẩu mới, xác nhận mật khẩu và nhấn nút “Lưu”
1. Hệ thống xác nhận các mật khẩu hợp lệ, lưu mật khẩu mới vào DB và thông báo người dùng đã đổi mật khẩu thành công

### Alternative Flow

1. Tại bước 4, nếu người dùng muốn huỷ các thay đổi của mình
- AL-08.1. Người dùng bấm nút “Huỷ”
- AL-08.2. Màn hình trở về trang “Tài khoản”, tab “Cá nhân”

### Exception Flow

1. Tại bước 5, khi hệ thống phát hiện mật khẩu hiện tại sai
- EX-08.1. Hệ thống gửi thông báo mật khẩu hiện tại sai

### Non-functional Requirement

- NR-01. Thời gian phản hồi < 2 giây
- NR-02. Password phải được mã hóa bằng SHA-256
