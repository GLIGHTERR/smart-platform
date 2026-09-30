# UC-03: Quên mật khẩu

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Amendment / living implementation spec hiện hành

- [Living spec UC-03](../../../docs/use-cases/smartchu/UC-03-forgot-password.md)
- Nội dung nguồn bên dưới được giữ nguyên để truy vết. Khi triển khai và kiểm thử, quyết định Approved trong living spec được ưu tiên nếu có khác biệt.

## Đặc tả nguồn

### Use Case ID

UC-3

### Use Case Name

Quên mật khẩu

### Description

Cho phép người dùng đặt lại mật khẩu nếu quên mật khẩu

### Trigger

Người dùng không nhớ mật khẩu và cần đăng nhập vào app

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

N/A

### Precondition

- PRE-01. Người dùng đã có tài khoản SmartChủ
- PRE-02. Người dùng chưa đăng nhập vào app SmartChủ

### Post-condition

- POS-01. Hệ thống thông báo đặt lại mật khẩu thành công
- POS-02. Người dùng được chuyển về màn hình “Đăng nhập”
- POS-03. Mật khẩu mới đã được hash và lưu trong DB

### Basic Flow

1. Màn hình hiển thị trang “Quên mật khẩu”
1. Người dùng nhập SĐT đã đăng ký tài khoản SmartChủ và nhấn nút “Nhận mã”
1. Hệ thống xác thực SĐT, nếu SĐT đã đăng ký tài khoản, hệ thống gửi mã OTP tới SĐT và chuyển sang màn hình “Xác thực OTP”
1. Người dùng nhập mã OTP và nhấn nút “Xác nhận”
1. Hệ thống xác thực mã OTP, nếu mã OTP hợp lệ, chuyển sang màn hình nhập mật khẩu mới
1. Người dùng nhập mật khẩu mới, xác nhận mật khẩu và nhấn nút “Xác nhận”
1. Hệ thống xác thực xem 2 mật khẩu có trùng nhau không, nếu có thì thông báo người dùng đã đặt lại mật khẩu thành công và chuyển về màn hình đăng nhập

### Alternative Flow

1. Tại bước 4, khi người dùng muốn lấy mã OTP khác
- AL-01.1. Người dùng bấm nút “Gửi lại mã OTP”
- AL-01.2. Tiếp tục tại bước 4 của Basic Flow

### Exception Flow

1. Tại bước 3, khi hệ thống phát hiện SĐT chưa đăng ký trong hệ thống
- EX-03.1. Hệ thống gửi thông báo SĐT chưa đăng ký tài khoản
1. Tại bước 5, khi mã OTP được nhập không hợp lệ
- EX-03.2. Hệ thống gửi thông báo mã OTP không hợp lệ
1. Tại bước 7, khi 2 mật khẩu được nhập không trùng khớp
- EX-03.3. Hệ thống gửi thông báo mật khẩu không trùng khớp

### Non-functional Requirement

NR-01. Password phải được mã hóa bằng SHA-256
