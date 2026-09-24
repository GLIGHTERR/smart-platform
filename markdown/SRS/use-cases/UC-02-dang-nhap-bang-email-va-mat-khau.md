# UC-2: Đăng nhập bằng email và mật khẩu

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.3.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-2

### Use Case Name

Đăng nhập bằng email và mật khẩu

### Description

Cho phép người dùng đăng nhập tài khoản bằng email và mật khẩu; đăng nhập thông thường không yêu cầu OTP

### Actor(s)

Registered Users

### Related Use Case

UC-1

### Priority

1

### Trigger

Người dùng muốn đăng nhập vào app SmartTrọ

### Precondition

- PRE-01. Người dùng đã có tài khoản SmartTrọ và email đã được xác minh
- PRE-02. Người dùng chưa đăng nhập vào app SmartTrọ

### Post-condition

- POS-01. Hệ thống thông báo người dùng đăng nhập thành công
- POS-02. Người dùng được chuyển về màn hình “Trang chủ”

### Basic Flow

1. Màn hình hiển thị trang “Đăng nhập”
1. Người dùng nhập email, mật khẩu và nhấn nút “Đăng nhập”
1. Hệ thống chuẩn hóa email và xác thực email/mật khẩu; nếu hợp lệ thì tạo phiên đăng nhập
1. Hệ thống trả kết quả đăng nhập thành công; không gửi OTP trong Sign In thông thường
1. Ứng dụng lưu phiên đăng nhập theo contract bảo mật và không lưu mật khẩu
1. Ứng dụng thông báo “Đăng nhập thành công” và chuyển về màn hình “Trang chủ”

### Alternative Flow

1. Tại bước 3, khi tài khoản tồn tại nhưng chưa xác minh email
- AL-02.1. Hệ thống hướng dẫn người dùng tiếp tục hoặc gửi lại OTP của luồng kích hoạt tài khoản
- AL-02.2. Sau khi email được xác minh, người dùng quay lại Sign In

### Exception Flow

1. Tại bước 3, khi email hoặc mật khẩu không khớp
- EX-02.1. Hệ thống gửi thông báo credential không đúng theo cách generic, không tiết lộ email có tồn tại
1. Tại bước 3, khi tài khoản bị khóa hoặc bị giới hạn đăng nhập theo policy backend
- EX-02.2. Hệ thống thông báo hành động tiếp theo theo policy; threshold và thời gian khóa cần được chốt trước task backend

### Business Rules

- BR-01. Email phải đúng định dạng và được trim khoảng trắng trước khi xử lý
- BR-02. Email chuẩn hóa là định danh đăng nhập unique của tài khoản MVP
- BR-03. Mật khẩu phải có ít nhất 8 ký tự
- BR-04. Mật khẩu phải có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số, 1 ký tự đặc biệt
- BR-05. Sign In thông thường không yêu cầu OTP; MFA hoặc risk-based OTP chỉ được bổ sung bằng requirement riêng

### Non-functional Requirement

- NR-01. Thời gian phản hồi đăng nhập < 2 giây
- NR-02. Password phải được băm một chiều bằng thuật toán thích ứng có salt như Argon2id hoặc bcrypt; không dùng SHA-256 đơn thuần

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.

## Tài liệu triển khai đã được phê duyệt

- [Living implementation specification](../../../docs/use-cases/smarttro/UC-02-sign-in.md)
- Khi baseline và living spec khác nhau, PM/Dev/QA dùng living spec đã phê duyệt cho implementation và ghi rõ deviation khỏi SRS nguồn.
