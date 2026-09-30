# SmartChủ — UC-03 Forgot Password by Email OTP

## 1. Metadata

| Thuộc tính | Giá trị |
| --- | --- |
| Use Case | `UC-03` — Quên mật khẩu bằng Email OTP |
| Actor | Chủ trọ |
| Trạng thái | Draft — chờ PO review |
| Ngày cập nhật | 2026-09-30 |
| Parent task | `GLI-90` |
| Source lịch sử | `SRS/SRS (SmartChủ).docx` |

## 2. Mục tiêu và thay đổi nguồn

Chủ trọ khôi phục mật khẩu qua email OTP 6 chữ số. Đề xuất này thay thế flow số điện thoại/SMS và các thông báo có khả năng làm lộ tài khoản trong SRS cũ.

## 3. Luồng đề xuất

1. Màn Email: người dùng nhập email và yêu cầu mã.
2. Hệ thống luôn trả thông báo trung tính: `Nếu email tồn tại, mã xác thực đã được gửi.`
3. Màn OTP: người dùng nhập OTP 6 chữ số; có gửi lại OTP theo cooldown và có cơ chế nhập email khác theo design được duyệt.
4. Sau OTP hợp lệ, backend cấp reset token một lần.
5. Màn Mật khẩu mới: người dùng nhập mật khẩu và xác nhận.
6. Hệ thống đổi mật khẩu, thu hồi toàn bộ session hiện có và đưa người dùng về Sign In với email prefill; không auto-login.

Ba bước Email → OTP → Mật khẩu mới là ba màn riêng. Không tự thêm input OTP inline vào màn Email.

## 4. Rules

- Response request OTP không xác nhận email tồn tại.
- OTP: 6 chữ số, TTL `10 phút`, cooldown `60 giây`, OTP mới vô hiệu OTP cũ, tối đa 5 lần nhập sai.
- Reset token: dùng một lần, TTL `10 phút`, không lưu/log plaintext ở client.
- Password mới dùng policy của UC-01 và không được bằng credential không hợp lệ theo security policy chung.
- Reset thành công thu hồi mọi session/refresh token của account.
- App background/foreground giữ bước và email không nhạy cảm nếu process/state còn hợp lệ.
- Force-close/restart đưa người dùng về Sign In; người dùng bắt đầu lại Forgot Password nếu cần.
- Account social-only không thuộc phạm vi test UC này; phải được bao phủ trong UC social auth riêng, không tự tạo local password account hoặc tự link provider.

## 5. Acceptance Criteria

### AC-SMC-FP-01 — Request không enumeration

- **Given** người dùng nhập email tồn tại hoặc không tồn tại
- **When** yêu cầu mã khôi phục
- **Then** UI hiển thị cùng một thông báo trung tính
- **And** response public không cho phép suy ra trạng thái tài khoản.

### AC-SMC-FP-02 — OTP hợp lệ

- **Given** OTP hiện hành còn hạn và chưa vượt số lần thử
- **When** người dùng xác minh đúng
- **Then** hệ thống cấp quyền chuyển sang bước tạo mật khẩu mới bằng reset token một lần.

### AC-SMC-FP-03 — Đổi mật khẩu

- **Given** reset token hợp lệ và hai trường mật khẩu đúng policy/khớp nhau
- **When** người dùng xác nhận
- **Then** mật khẩu được thay đổi đúng một lần
- **And** mọi session cũ bị thu hồi
- **And** app trở về Sign In với email prefill, không auto-login.

### AC-SMC-FP-04 — App lifecycle

- **Given** người dùng đang ở OTP hoặc Password và chuyển app để đọc email
- **When** quay lại khi process/state còn hợp lệ
- **Then** bước hiện tại không bị dựng lại vô cớ
- **But when** app bị force-close/restart
- **Then** flow recovery không được phục hồi từ dữ liệu nhạy cảm đã persist.

## 6. Implementation notes

- Tái sử dụng email/OTP/reset infrastructure của `smart-platform-services`, không tạo implementation riêng cho SmartChủ.
- UI phải bám Figma SmartChủ; capture Email/OTP/New Password là gate trước handoff.
- Mọi thay đổi về nút `Nhập email khác`, `Gửi lại OTP` hoặc thứ tự button phải được chốt ở design và cập nhật file này trước khi Dev code.

## 7. Điểm chờ PO review

- Xác nhận toàn bộ policy dùng chung với SmartTrọ UC-03.
- Xác nhận wording và vị trí `Nhập email khác` trong Figma SmartChủ.
- Bổ sung capture Figma/node ID SmartChủ.
