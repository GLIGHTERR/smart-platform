# UC-02: Đăng nhập bằng số điện thoại

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Amendment / living implementation spec hiện hành

- [Living spec UC-02](../../../../../docs/SRS/SmartChu/use-cases/UC-02-sign-in.md)
- Nội dung nguồn bên dưới được giữ nguyên để truy vết. Khi triển khai và kiểm thử, quyết định Approved trong living spec được ưu tiên nếu có khác biệt.

## Đặc tả nguồn

### Use Case ID

UC-2

### Use Case Name

Đăng nhập bằng số điện thoại

### Description

Cho phép người dùng đăng nhập tài khoản bằng số điện thoại và mật khẩu

### Trigger

Người dùng muốn đăng nhập vào app SmartChủ

### Priority

1

### Business Rules

- BR-01. SĐT phải có 10 số
- BR-02. SĐT phải bắt đầu bằng số 03, 05, 07, 08 hoặc 09
- BR-03. Mật khẩu phải có ít nhất 8 ký tự
- BR-04. Mật khẩu phải có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số, 1 ký tự đặc biệt
- BR-05. Mã OTP có hiệu lực trong 5 phút

### Actor(s)

Registered Users

### Related Use Case

UC-1

### Precondition

- PRE-01. Người dùng đã có tài khoản SmartChủ
- PRE-02. Người dùng chưa đăng nhập vào app SmartChủ

### Post-condition

- POS-01. Hệ thống thông báo người dùng đăng nhập thành công
- POS-02. Người dùng được chuyển về màn hình “Trang chủ”

### Basic Flow

1. Màn hình hiển thị trang “Đăng nhập”
1. Người dùng nhập SĐT, mật khẩu và nhấn nút “Đăng nhập”
1. Hệ thống xác thực tài khoản, nếu hợp lệ thì chuyển sang màn hình “Nhập mã OTP”
1. Hệ thống gửi mã OTP tới SĐT của người dùng
1. Người dùng nhập mã OTP và nhấn nút “Xác nhận”
1. Hệ thống xác thực mã OTP, nếu hợp lệ thì thông báo “Đăng nhập thành công” và chuyển về màn hình “Trang chủ”

### Alternative Flow

1. Tại bước 5, khi người dùng muốn lấy mã OTP khác
- AL-02.1. Người dùng bấm nút “Gửi lại mã OTP”
- AL-02.2. Tiếp tục tại bước 5 của Basic Flow

### Exception Flow

1. Tại bước 3, khi hệ thống phát hiện SĐT và mật khẩu chưa khớp trong hệ thống
- EX-02.1. Hệ thống gửi thông báo SĐT hoặc mật khẩu không đúng
1. Tại bước 6, khi mã OTP được nhập không hợp lệ
- EX-02.2. Hệ thống gửi thông báo mã OTP không hợp lệ

### Non-functional Requirement

- NR-01. Thời gian phản hồi đăng nhập < 2 giây
- NR-02. Password phải được mã hóa bằng SHA-256
