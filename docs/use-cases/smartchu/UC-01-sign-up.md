# SmartChủ — UC-01 Sign Up Implementation Specification

## 1. Metadata

| Thuộc tính | Giá trị |
| --- | --- |
| Use Case | `UC-01` — Đăng ký bằng email |
| Actor | Chủ trọ |
| Trạng thái | Draft — chờ PO review |
| Ngày cập nhật | 2026-09-30 |
| Parent task | `GLI-76` |
| Source lịch sử | `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` |

## 2. Mục tiêu và thay đổi nguồn

Chủ trọ tạo tài khoản bằng email, xác minh bằng OTP email 6 chữ số và thiết lập mật khẩu. Đề xuất này thay thế flow số điện thoại/SMS trong SRS SmartChủ cũ.

| Nội dung cũ | Baseline đề xuất hiện tại |
| --- | --- |
| Số điện thoại là định danh đăng ký | Email normalized là định danh đăng nhập duy nhất |
| OTP qua SMS | OTP 6 chữ số qua email |
| Mật khẩu xử lý theo mô tả SHA-256 cũ | Mật khẩu tuân theo auth platform hiện hành; không lưu/hash bằng SHA-256 thuần |
| Behavior sau đăng ký chưa thống nhất | Trở về Sign In, prefill email; không auto-login |

Số điện thoại, nếu được thu thập ở flow hồ sơ sau này, chỉ là dữ liệu liên hệ và không phải credential/unique identity.

## 3. Luồng đề xuất

1. Chủ trọ nhập email.
2. FE chuẩn hóa định dạng và gửi yêu cầu OTP.
3. Hệ thống trả response chống enumeration phù hợp và gửi OTP email nếu hợp lệ.
4. Chủ trọ nhập OTP 6 chữ số.
5. Sau khi OTP hợp lệ, chủ trọ nhập mật khẩu và xác nhận mật khẩu.
6. Hệ thống tạo tài khoản SmartChủ đã xác minh email và khởi tạo `businessVerificationStatus = NOT_SUBMITTED`.
7. App trở về Sign In với email được điền sẵn; không giữ OTP hoặc mật khẩu.

## 4. Business và security rules

- Email được trim và normalize theo shared identity contract trước khi kiểm tra unique.
- OTP có TTL `10 phút`; cooldown gửi lại `60 giây`; OTP mới làm OTP cũ mất hiệu lực.
- OTP không được lưu/log dưới dạng đọc được và không được đưa vào navigation params hoặc persistent storage.
- Password policy: tối thiểu 8 ký tự, có ít nhất 1 chữ hoa, 1 số và 1 ký tự đặc biệt, trừ khi PO duyệt policy khác cho toàn platform.
- Khi app chỉ background/foreground và process còn sống, giữ bước hiện tại cùng email không nhạy cảm; không render/reload flow từ đầu nếu state còn hợp lệ.
- Khi app bị force-close/restart, không khôi phục OTP/mật khẩu; người dùng đi lại từ đầu Sign Up.
- Đăng ký social không thuộc UC này và cần UC riêng, bao gồm account social-only dùng cùng email.
- Xác minh email không đồng nghĩa được phép vận hành cho thuê. Quyền tạo nhà, phòng và hợp đồng tuân theo [`../../11-smartchu-business-verification-policy.md`](../../11-smartchu-business-verification-policy.md).

## 5. Acceptance Criteria

### AC-SMC-SU-01 — Đăng ký thành công

- **Given** email chưa gắn với tài khoản SmartChủ và người dùng nhập OTP/mật khẩu hợp lệ
- **When** hoàn tất Sign Up
- **Then** hệ thống tạo đúng một tài khoản với email normalized
- **And** hồ sơ kinh doanh khởi tạo ở `NOT_SUBMITTED`
- **And** tài khoản chưa được phép tạo nhà trọ, phòng trọ hoặc hợp đồng
- **And** điều hướng về Sign In với email prefill
- **And** không auto-login.

### AC-SMC-SU-02 — Email đã tồn tại

- **Given** email normalized đã tồn tại
- **When** người dùng yêu cầu đăng ký
- **Then** response và UI không tiết lộ dữ liệu nhạy cảm ngoài behavior đã được PO duyệt
- **And** không tạo tài khoản trùng.

### AC-SMC-SU-03 — OTP

- **Given** người dùng đang ở bước OTP
- **When** OTP sai, hết hạn, vượt số lần thử hoặc đã bị thay bằng OTP mới
- **Then** hệ thống từ chối xác minh với error code có thể map an toàn sang UI
- **And** không tạo account.

### AC-SMC-SU-04 — App lifecycle

- **Given** người dùng rời app tạm thời để đọc email
- **When** quay lại khi process/state còn hợp lệ
- **Then** app giữ đúng bước và email
- **And** không giữ hoặc hiển thị lại mật khẩu/OTP sau restart.

## 6. Implementation notes

- SmartChủ dùng shared backend `smart-platform-services`; không tạo auth database riêng.
- Endpoint tạm `/owner/auth/register` trong foundation không mặc nhiên là contract cuối cùng.
- FE phải dựng và review trước BE.
- Capture Figma SmartChủ cho ba bước Email → OTP → Password là gate bắt buộc trước handoff FE.

## 7. Điểm chờ PO review

- Xác nhận SmartChủ dùng nguyên password policy, TTL/cooldown và post-registration behavior của SmartTrọ.
- Xác nhận wording chống enumeration và lỗi email đã tồn tại.
- Bổ sung capture Figma/node ID SmartChủ.
