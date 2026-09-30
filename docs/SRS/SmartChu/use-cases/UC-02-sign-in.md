# SmartChủ — UC-02 Sign In Implementation Specification

## 1. Metadata

| Thuộc tính | Giá trị |
| --- | --- |
| Use Case | `UC-02` — Đăng nhập bằng email và mật khẩu |
| Actor | Chủ trọ |
| Trạng thái | Draft — chờ PO review |
| Ngày cập nhật | 2026-09-30 |
| Parent task | `GLI-83` |
| Source lịch sử | `SRS/SRS (SmartChủ).docx` |

## 2. Mục tiêu và thay đổi nguồn

Chủ trọ đăng nhập bằng email và mật khẩu. Flow đăng nhập thông thường **không yêu cầu OTP**. Đề xuất này thay thế SRS cũ dùng số điện thoại và yêu cầu OTP sau credential.

## 3. Luồng đề xuất

1. Chủ trọ nhập email và mật khẩu.
2. FE validate định dạng tối thiểu và gửi request một lần.
3. Backend xác thực email normalized, mật khẩu và trạng thái tài khoản.
4. Nếu hợp lệ, backend tạo session/token theo shared auth contract.
5. App lưu session bằng secure storage phù hợp nền tảng và điều hướng vào Home SmartChủ.

## 4. Rules

- Không dùng số điện thoại làm credential.
- Không gửi OTP trong Sign In bình thường.
- Sai email hoặc mật khẩu dùng thông báo chung, không xác nhận tài khoản có tồn tại.
- Account chưa xác minh trả error code riêng cho FE và resume bước OTP của UC-01 với email prefill; không tạo account mới.
- Access token/refresh token không được lưu plaintext trong `localStorage`; mobile dùng secure storage, web dùng cơ chế cookie/token đã được platform duyệt.
- Chặn double-submit và trả UI về trạng thái thao tác được sau timeout/lỗi mạng.
- Sign Out thu hồi/đóng session theo contract, xóa credential cục bộ và trở về Sign In.
- Không tự link/unlink social provider dựa trên email trong UC này.

## 5. Acceptance Criteria

### AC-SMC-SI-01 — Đăng nhập thành công

- **Given** tài khoản email/password đã xác minh và đang active
- **When** người dùng nhập credential đúng
- **Then** hệ thống tạo session hợp lệ
- **And** app điều hướng vào Home SmartChủ.

### AC-SMC-SI-02 — Credential không hợp lệ

- **Given** email hoặc mật khẩu không đúng
- **When** người dùng đăng nhập
- **Then** UI hiển thị thông báo chung
- **And** không tiết lộ email có tồn tại hay không.

### AC-SMC-SI-03 — Account chưa xác minh

- **Given** email/password đúng nhưng account chưa hoàn tất email OTP
- **When** đăng nhập
- **Then** app điều hướng tới bước OTP của UC-01 với email prefill
- **And** không tạo tài khoản hoặc session trùng.

### AC-SMC-SI-04 — Sign Out

- **Given** người dùng đã đăng nhập
- **When** chọn Sign Out
- **Then** session cục bộ bị xóa và backend xử lý refresh/session theo contract
- **And** người dùng trở về Sign In, không xem được dữ liệu bảo vệ bằng Back navigation.

## 6. Implementation notes

- Foundation local đã có email/password validation và SecureStore, nhưng endpoint `/owner/auth/login` và payload hiện tại chỉ là adapter ban đầu, chưa phải contract được duyệt.
- FE phải dựng đúng Figma SmartChủ trước khi map API thật.
- Capture Figma SmartChủ Sign In và các validation/loading/error state phải được bổ sung trước handoff.

## 7. Điểm chờ PO review

- Xác nhận post-login route/Home state của SmartChủ.
- Xác nhận session duration, multi-device và sign-out-current/all behavior dùng chung toàn platform.
- Bổ sung capture Figma/node ID SmartChủ.
