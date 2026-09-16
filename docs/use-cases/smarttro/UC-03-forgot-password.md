# SmartTrọ — UC-03 Quên mật khẩu bằng Email OTP: đề xuất quyết định

## 1. Trạng thái tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | **Pending PO approval** |
| Phạm vi | Quên mật khẩu SmartTrọ bằng email, OTP 6 chữ số và mật khẩu mới |
| Figma | Đã xác minh và xuất capture từ page `SmartTrọ` ngày 2026-09-16 |
| Bàn giao Dev | **Chưa được phép** cho đến khi các quyết định `FORGOT-D01` đến `FORGOT-D15` được chốt và source requirements được cập nhật |

Tài liệu này tách **thiết kế trực quan đã có** khỏi **business/security rule chưa được duyệt**. Figma không tự tạo ra quy tắc expiry, retry, lock, session hoặc anti-abuse.

## 2. Flow đề xuất

1. Người dùng nhập email đã đăng ký.
2. Hệ thống phản hồi trung tính và gửi OTP 6 chữ số nếu tài khoản hợp lệ.
3. Người dùng nhập OTP.
4. Khi OTP hợp lệ, người dùng nhập mật khẩu mới và xác nhận mật khẩu.
5. Hệ thống đổi mật khẩu, thu hồi session theo policy đã chốt và đưa người dùng về Sign In; không auto-login.

## 3. Figma traceability và capture

| Bước | Node | Nội dung đã xác minh |
| --- | --- | --- |
| Nhập email | `2005:3286` — `Forget Password (Input Email) - iPhone` | `Email`, `Gửi OTP` |
| Nhập OTP | `2005:3261` — tên layer còn là `Sign Up (Input OTP) - iPhone` | Heading `Quên mật khẩu`, `Mã OTP`, `Tiếp tục`, `Gửi lại mã OTP` |
| Đặt mật khẩu mới | `2005:3310` — tên layer còn là `Sign Up (Input Password) - iPhone` | Heading `Quên mật khẩu`, mật khẩu, nhập lại mật khẩu, `Xác nhận` |

Tên của hai frame sau còn dùng prefix `Sign Up`; Dev và PM phải dùng node ID + nội dung hiển thị để truy vết, không suy luận flow từ tên layer.

### Capture 1 — Nhập email

![SmartTrọ Quên mật khẩu — nhập email](../../assets/smarttro-auth/forgot-password-email.png)

### Capture 2 — Nhập OTP email

![SmartTrọ Quên mật khẩu — nhập OTP](../../assets/smarttro-auth/forgot-password-otp.png)

### Capture 3 — Đặt mật khẩu mới

![SmartTrọ Quên mật khẩu — đặt mật khẩu mới](../../assets/smarttro-auth/forgot-password-new-password.png)

## 4. Các quyết định cần PO chốt

| ID | Nội dung cần chốt | Đề xuất | Lý do / tác động |
| --- | --- | --- | --- |
| `FORGOT-D01` | Định danh account recovery | Dùng email đã normalize giống Sign Up/Sign In | Không tạo identity rule thứ hai |
| `FORGOT-D02` | Hình thức xác minh | OTP email 6 chữ số; không dùng magic link trong MVP | Tránh deep-link/redirect giữa email app và mobile app |
| `FORGOT-D03` | Thời hạn OTP | 10 phút | Đủ thời gian chuyển app nhưng hạn chế cửa sổ tấn công |
| `FORGOT-D04` | Resend | Cooldown 60 giây; OTP mới làm vô hiệu OTP cũ | Tránh nhiều mã cùng hiệu lực và spam email |
| `FORGOT-D05` | Số lần nhập sai | Tối đa 5 lần/challenge; vượt ngưỡng hủy challenge và yêu cầu gửi mã mới | Có rule rõ để test và chống brute force |
| `FORGOT-D06` | Rate limit | Theo email + IP + device; đề xuất tối đa 5 request/15 phút/email và 20 request/giờ/IP | Không phụ thuộc một tín hiệu duy nhất |
| `FORGOT-D07` | Anti-enumeration | Luôn trả thông báo trung tính, ví dụ “Nếu email tồn tại, mã xác thực đã được gửi” | Không tiết lộ email nào có tài khoản |
| `FORGOT-D08` | Điều kiện sang bước mật khẩu | Server cấp reset token ngắn hạn sau OTP hợp lệ; không dùng OTP trực tiếp để đổi mật khẩu | Tách verify challenge khỏi mutation nhạy cảm |
| `FORGOT-D09` | Thời hạn reset token | 10 phút, one-time-use, bind với account + challenge + device/session context phù hợp | Hạn chế replay |
| `FORGOT-D10` | Password policy | Dùng đúng policy Sign Up; không cho trùng mật khẩu hiện tại nếu backend hỗ trợ kiểm tra an toàn | Tránh rule password lệch giữa đăng ký và recovery |
| `FORGOT-D11` | Session sau khi reset | Thu hồi toàn bộ access/refresh session đang hoạt động của tài khoản | Mật khẩu có thể bị reset vì nghi ngờ lộ tài khoản |
| `FORGOT-D12` | Điều hướng sau thành công | Không auto-login; về Sign In với email được prefill, hiển thị thông báo đổi mật khẩu thành công | Nhất quán với Sign Up và buộc dùng credential mới |
| `FORGOT-D13` | State khi chuyển sang email app | Chỉ persist tạm email normalized, bước hiện tại, challenge ID và expiry; không persist OTP/password/reset token | Giữ UX nhưng không lưu secret |
| `FORGOT-D14` | Account chưa verify / social-only | Không tự tạo account, không tự link provider; hiển thị response trung tính và chuyển sang flow support/linking đã chốt sau | Tránh duplicate hoặc takeover account |
| `FORGOT-D15` | Audit/log | Ghi request/resend/verify/reset/revoke theo immutable user ID; mask email, không log OTP/token/password | Đủ điều tra sự cố mà không lộ PII/secret |

## 5. Quy tắc UI và validation kế thừa

- Email trim + lowercase theo cùng normalization của Sign Up/Sign In.
- Mật khẩu và confirm password dùng cùng rule, component và accessibility của Sign Up.
- OTP chỉ nhận 6 chữ số; hỗ trợ paste; hiển thị countdown resend.
- Loading phải chống double-submit; lỗi network giữ email nhưng không giữ OTP/password.
- Khi app background/foreground, phải khôi phục đúng bước nếu challenge còn hạn; nếu hết hạn thì đưa về bước email với thông báo rõ.
- Không đặt email thô trong analytics key; không truyền OTP/password/reset token qua route parameters.

## 6. Source documents phải cập nhật sau khi PO duyệt

| Nguồn | Mục dự kiến cập nhật |
| --- | --- |
| `Requirement_List/Requirements List - SmartTrọ.xlsx` | `SM004` và change request liên quan |
| `User_Stories/User Story - SmartTrọ.xlsx` | User Story `3.0`, AC Email → OTP → password mới |
| `SRS/SRS (SmartTrọ).docx` | UC Quên mật khẩu, pre/post-condition, exceptions và security rules |
| `FRS/FRS - SmartTrọ.docx` | Bổ sung đặc tả flow/API/state nếu FRS được mở rộng auth |
| `Activity_Diagrams/` | Thay flow phone/SMS bằng email OTP; thêm expiry/resend/attempt/rate-limit branches |
| `docs/use-cases/smarttro/UC-02-sign-in.md` | Cập nhật điều hướng từ Sign In sang UC-03 và contract sau khi đặt lại mật khẩu |
| `markdown/` | Đồng bộ lại mirror và SHA-256 sau khi file nguồn thay đổi |

## 7. Gate bàn giao PM/Dev

PM chỉ giao task implementation sau khi:

1. PO xác nhận hoặc điều chỉnh toàn bộ `FORGOT-D01` đến `FORGOT-D15`.
2. Requirement List, User Story, SRS và Activity Diagram đã cập nhật cùng một rule set.
3. API contract thể hiện challenge ID, expiry, resend, attempt, reset token, generic response và session revocation.
4. QA có test matrix cho happy path, expired/replayed OTP, brute force, enumeration, resend race, app resume và session revocation.
