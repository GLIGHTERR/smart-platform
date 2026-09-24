# UC-1: Đăng ký bằng email

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.2.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-1

### Use Case Name

Đăng ký bằng email

### Description

Cho phép người dùng đăng ký tài khoản bằng email, xác minh bằng OTP email 6 chữ số và tạo mật khẩu

### Actor(s)

Guest Users

### Related Use Case

UC-2

### Priority

1

### Trigger

Người dùng muốn đăng ký tài khoản trên SmartTrọ

### Precondition

PRE-01. Thiết bị có kết nối internet hoặc hotspot

### Post-condition

- POS-01. Hệ thống thông báo người dùng đăng ký thành công
- POS-02. Thông tin tài khoản được lưu vào DB

### Basic Flow

1. Người dùng truy cập màn hình Đăng ký từ màn hình Đăng nhập
1. Người dùng nhập email và bấm nút “Gửi OTP”
1. Hệ thống chuẩn hóa email, kiểm tra unique và gửi mã OTP 6 chữ số tới email hợp lệ
1. Người dùng nhập mã OTP và bấm nút “Tiếp tục”
1. Hệ thống xác thực mã OTP có hợp lệ không, nếu có thì chuyển sang màn hình nhập mật khẩu
1. Người dùng nhập “Mật khẩu” và “Nhập lại mật khẩu”
1. Hệ thống xác thực 2 mật khẩu trùng khớp không, nếu có, hệ thống sẽ thông báo đăng ký tài khoản thành công và chuyển về màn hình đăng nhập

### Alternative Flow

1. Tại bước 4, khi người dùng muốn lấy mã OTP khác
- AL-01.1. Người dùng bấm nút “Gửi lại mã OTP”
- AL-01.2. Tiếp tục tại bước 4 của Basic Flow

### Exception Flow

1. Tại bước 3, khi hệ thống phát hiện email chuẩn hóa đã được dùng cho tài khoản khác
- EX-01.1. Hệ thống không tạo tài khoản trùng và hướng dẫn người dùng đăng nhập hoặc khôi phục tài khoản theo contract anti-enumeration
1. Tại bước 5, khi mã OTP được nhập không hợp lệ
- EX-01.2. Hệ thống gửi thông báo mã OTP không hợp lệ
1. Tại bước 7, khi 2 mật khẩu được nhập không trùng khớp
- EX-01.3. Hệ thống gửi thông báo mật khẩu không trùng khớp

### Business Rules

- BR-01. Email phải đúng định dạng và được trim khoảng trắng trước khi xử lý
- BR-02. Email chuẩn hóa là định danh đăng nhập unique của tài khoản MVP
- BR-03. Mật khẩu phải có ít nhất 8 ký tự
- BR-04. Mật khẩu phải có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số, 1 ký tự đặc biệt
- BR-05. Thời gian hiệu lực OTP là cấu hình backend; UI dùng thời điểm hết hạn do API trả về

### Non-functional Requirement

- NR-01. Thời gian phản hồi đăng ký < 2 giây
- NR-02. Password phải được băm một chiều bằng thuật toán thích ứng có salt như Argon2id hoặc bcrypt; không dùng SHA-256 đơn thuần

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.

## Tài liệu triển khai đã được phê duyệt

- [Living implementation specification](../../../docs/use-cases/smarttro/UC-01-sign-up.md)
- Khi baseline và living spec khác nhau, PM/Dev/QA dùng living spec đã phê duyệt cho implementation và ghi rõ deviation khỏi SRS nguồn.
