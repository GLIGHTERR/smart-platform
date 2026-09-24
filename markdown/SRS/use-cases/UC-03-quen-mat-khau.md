# UC-3: Quên mật khẩu

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.4.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-3

### Use Case Name

Quên mật khẩu

### Description

Cho phép người dùng đặt lại mật khẩu nếu quên mật khẩu

### Actor(s)

Registered Users

### Related Use Case

N/A

### Priority

1

### Trigger

Người dùng muốn đặt lại mật khẩu do quên mật khẩu

### Precondition

- PRE-01. Người dùng đã có tài khoản SmartTrọ
- PRE-02. Người dùng chưa đăng nhập vào app SmartTrọ

### Post-condition

- POS-01. Hệ thống thông báo đặt lại mật khẩu thành công
- POS-02. Người dùng được chuyển về màn hình “Đăng nhập”
- POS-03. Mật khẩu mới đã được hash và lưu trong DB

### Basic Flow

1. Màn hình hiển thị trang “Quên mật khẩu”
1. Người dùng nhập SĐT đã đăng ký tài khoản SmartTrọ và nhấn nút “Nhận mã”
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

### Business Rules

- BR-01. SĐT phải có 10 số
- BR-02. SĐT phải bắt đầu bằng số 03, 05, 07, 08 hoặc 09
- BR-03. Mật khẩu phải có ít nhất 8 ký tự
- BR-04. Mật khẩu phải có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số, 1 ký tự đặc biệt
- BR-05. Mã OTP có hiệu lực trong 5 phút

### Non-functional Requirement

NR-01. Password phải được mã hóa bằng SHA-256

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.

## Tài liệu triển khai đã được phê duyệt

- [Living implementation specification](../../../docs/use-cases/smarttro/UC-03-forgot-password.md)
- Khi baseline và living spec khác nhau, PM/Dev/QA dùng living spec đã phê duyệt cho implementation và ghi rõ deviation khỏi SRS nguồn.
