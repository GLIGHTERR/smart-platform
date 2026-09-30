# UC-01: Đăng ký bằng số điện thoại

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Amendment / living implementation spec hiện hành

- [Living spec UC-01](../../../../../docs/SRS/SmartChu/use-cases/UC-01-sign-up.md)
- Nội dung nguồn bên dưới được giữ nguyên để truy vết. Khi triển khai và kiểm thử, quyết định Approved trong living spec được ưu tiên nếu có khác biệt.

## Đặc tả nguồn

### Use Case ID

UC-1

### Use Case Name

Đăng ký bằng số điện thoại

### Description

Cho phép người dùng đăng ký tài khoản bằng số điện thoại

### Trigger

Người dùng muốn đăng ký tài khoản trên SmartChủ

### Priority

1

### Business Rules

- BR-01. SĐT phải có 10 số
- BR-02. SĐT phải bắt đầu bằng số 03, 05, 07, 08 hoặc 09
- BR-03. Mật khẩu phải có ít nhất 8 ký tự
- BR-04. Mật khẩu phải có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số, 1 ký tự đặc biệt
- BR-05. Mã OTP có hiệu lực trong 5 phút

### Actor(s)

Guest Users

### Related Use Case

UC-2

### Precondition

PRE-01. Thiết bị có kết nối internet hoặc hotspot

### Post-condition

- POS-01. Hệ thống thông báo người dùng đăng ký thành công
- POS-02. Thông tin tài khoản được lưu vào DB

### Basic Flow

1. Người dùng truy cập màn hình Đăng ký từ màn hình Đăng nhập
1. Người dùng nhập số điện thoại và bấm nút “Gửi OTP”
1. Hệ thống kiểm tra số điện thoại đã tồn tại chưa, nếu chưa, gửi mã OTP xác thực tới SĐT vừa được nhập
1. Người dùng nhập mã OTP và bấm nút “Tiếp tục”
1. Hệ thống xác thực mã OTP có hợp lệ không, nếu có thì chuyển sang màn hình nhập mật khẩu
1. Người dùng nhập “Mật khẩu” và “Nhập lại mật khẩu”
1. Hệ thống xác thực 2 mật khẩu trùng khớp không, nếu có, hệ thống sẽ thông báo đăng ký tài khoản thành công và chuyển về màn hình đăng nhập

### Alternative Flow

1. Tại bước 4, khi người dùng muốn lấy mã OTP khác
- AL-01.1. Người dùng bấm nút “Gửi lại mã OTP”
- AL-01.2. Tiếp tục tại bước 4 của Basic Flow

### Exception Flow

1. Tại bước 3, khi hệ thống phát hiện SĐT đã đăng ký trong hệ thống
- EX-01.1. Hệ thống gửi thông báo SĐT đã tồn tại trong hệ thống
1. Tại bước 5, khi mã OTP được nhập không hợp lệ
- EX-01.2. Hệ thống gửi thông báo mã OTP không hợp lệ
1. Tại bước 7, khi 2 mật khẩu được nhập không trùng khớp
- EX-01.3. Hệ thống gửi thông báo mật khẩu không trùng khớp

### Non-functional Requirement

- NR-01. Thời gian phản hồi đăng ký < 2 giây
- NR-02. Password phải được mã hóa bằng SHA-256
