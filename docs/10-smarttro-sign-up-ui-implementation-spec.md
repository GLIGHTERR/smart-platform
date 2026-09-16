# SmartTrọ — Sign Up UI Implementation Specification

## 1. Trạng thái tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái nghiệp vụ | **Approved** |
| Trạng thái bàn giao PM | **Ready — đã xác minh Figma và xuất capture email ngày 2026-09-16** |
| Phạm vi | Luồng đăng ký SmartTrọ bằng email, OTP email và mật khẩu |
| Nền tảng | React Native + Expo cho iOS, Android và Expo Web preview |
| Dữ liệu ở giai đoạn UI | Mock trong bộ nhớ; chưa gọi API và chưa gửi email thật |
| Ngày lập | 2026-09-15 |
| Ngày cập nhật quyết định email | 2026-09-16 |
| Phê duyệt | PO đã duyệt `SIGNUP-D01` đến `SIGNUP-D08` |

Tài liệu này là nguồn triển khai trực tiếp cho Sign Up SmartTrọ. Quyết định mới nhất thay thế yêu cầu đăng ký bằng số điện thoại trong các tài liệu cũ: **email là định danh đăng nhập duy nhất của tài khoản MVP; số điện thoại chỉ là dữ liệu liên hệ tùy chọn và không dùng để xác định tài khoản duy nhất**.

Tài liệu và capture hiện đã khớp với luồng email. PM có thể dùng tài liệu này để chuẩn bị task FE Sign Up SmartTrọ; backend OTP production vẫn phải chờ chốt các policy còn mở trong `docs/11-smarttro-sign-in-and-auth-identity-mvp.md`.

## 2. Mục tiêu và kết quả mong đợi

Luồng đăng ký gồm ba bước:

1. Nhập email và yêu cầu mã OTP.
2. Nhập mã OTP 6 chữ số nhận qua email.
3. Tạo mật khẩu, xác nhận mật khẩu và hoàn tất đăng ký.

Sau khi đăng ký thành công, ứng dụng chuyển về Sign In và không tự đăng nhập.

Kết quả cần đạt:

- Email được chuẩn hóa và dùng làm định danh unique của tài khoản MVP.
- Người dùng phải xác minh quyền sở hữu email trước khi đặt mật khẩu.
- Luồng UI giữ nguyên trạng thái không nhạy cảm khi người dùng chuyển sang ứng dụng email rồi quay lại.
- OTP, mật khẩu và xác nhận mật khẩu không được ghi vào persistent storage, route parameters hoặc log.
- UI bám Figma sau khi phần chữ được cập nhật sang email; Dev không chép React/Tailwind do Figma sinh ra.
- Giai đoạn review UI có mock gateway rõ ràng và không tạo business rule ngầm.

## 3. Nguồn và thứ tự ưu tiên

### 3.1. Nguồn thiết kế

Figma file `Smart Platform`, file key `rsjbGO3ul8lzKKKTj38r0t`, page `SmartTrọ`.

| Bước | Figma node hiện có | Trạng thái sử dụng |
| --- | --- | --- |
| Nhập email | `237:1161` — `Sign Up (Input Email) - iPhone` | **Ready** — label `Email`, action `Gửi OTP` |
| Nhập OTP | `237:1137` — `Sign Up (Input OTP) - iPhone` | **Ready** — OTP và resend đã hiển thị |
| Tạo mật khẩu | `237:1185` — `Sign Up (Input Password) - iPhone` | **Ready** — mật khẩu, xác nhận mật khẩu và action đăng ký |

Capture baseline đã xuất từ đúng page `SmartTrọ` ngày 2026-09-16 và đặt tại `docs/assets/smarttro-auth/`:

- `sign-up-email.png`.
- `sign-up-otp.png`.
- `sign-up-password.png`.

Các file cũ trong `docs/assets/smarttro-sign-up/` chỉ là lịch sử và không còn là baseline nội dung.

#### Capture 1 — Nhập email

![SmartTrọ Sign Up — nhập email](assets/smarttro-auth/sign-up-email.png)

#### Capture 2 — Nhập OTP email

![SmartTrọ Sign Up — nhập OTP email](assets/smarttro-auth/sign-up-otp.png)

#### Capture 3 — Tạo mật khẩu

![SmartTrọ Sign Up — tạo mật khẩu](assets/smarttro-auth/sign-up-password.png)

### 3.2. Nguồn requirement

- Quyết định PO ngày 2026-09-16 trong tài liệu này.
- `docs/11-smarttro-sign-in-and-auth-identity-mvp.md`.
- `Requirement_List/Requirements List - SmartTrọ.xlsx`, `SM001`.
- `User_Stories/User Story - SmartTrọ.xlsx`, sheet `Đăng kýĐăng nhập`, User Story `1.0`.
- `SRS/SRS (SmartTrọ).docx`, UC Sign Up sau khi cập nhật.

Hai Activity Diagram email đã được cập nhật cùng source `.puml` trong `Activity_Diagrams/`. Các bản `By Phone` chỉ là lịch sử và không còn là baseline MVP.

### 3.3. Quy tắc khi có mâu thuẫn

1. Quyết định PO mới nhất trong task/comment.
2. `docs/10-smarttro-sign-up-ui-implementation-spec.md` và `docs/11-smarttro-sign-in-and-auth-identity-mvp.md`.
3. Markdown handoff mới nhất trong `docs/`.
4. Requirement List, User Story và SRS đã cập nhật.
5. Figma cho phần trình bày trực quan.
6. Code foundation cho convention kỹ thuật.

Nếu vẫn có conflict, deferred decision hoặc ambiguity mà PM không giải quyết được, PM phải comment vào task và tag PO để chốt trước khi giao Dev.

## 4. Quyết định đã phê duyệt

| ID | Quyết định | Trạng thái |
| --- | --- | --- |
| SIGNUP-D01 | Dùng font Poppins tương thích Expo, có system fallback | Approved |
| SIGNUP-D02 | Dùng palette accessible đã duyệt: primary `#B84D00`, text action `#A84300` | Approved |
| SIGNUP-D03 | Social sign-up chỉ visual-only ở review build; production mặc định ẩn đến khi có task riêng | Approved |
| SIGNUP-D04 | Resend OTP ở UI mock có cooldown 60 giây; backend là nguồn policy thật | Approved |
| SIGNUP-D05 | Đăng ký thành công quay về Sign In; không auto-login | Approved |
| SIGNUP-D06 | Áp dụng toàn bộ sai khác accessibility `UI-D01` đến `UI-D07` | Approved |
| SIGNUP-D07 | Định danh Sign Up MVP đổi từ số điện thoại sang email; email normalized là unique login identifier | Approved |
| SIGNUP-D08 | OTP gồm 6 chữ số và gửi qua email; không dùng verification link trong MVP | Approved |

Các giá trị backend chưa được PO chốt trong lần duyệt này — OTP expiry, số lần verify sai tối đa, rate limit theo email/IP/device và chính sách khóa — phải là config và được PM/PO chốt trước task backend. Dev FE không được hard-code chúng thành business rule, ngoài cooldown review 60 giây đã duyệt.

## 5. Luồng nghiệp vụ chuẩn

### 5.1. Bước Email

1. Người dùng mở Sign Up.
2. Nhập email.
3. Ứng dụng trim khoảng trắng và lowercase phần dùng để so khớp/unique.
4. FE kiểm tra định dạng cơ bản.
5. Người dùng chọn `Gửi mã OTP`.
6. Mock/API tạo một signup attempt và gửi OTP tới email.
7. Ứng dụng chuyển sang bước OTP.

### 5.2. Bước OTP

1. Hiển thị email đã mask để người dùng biết mã được gửi tới đâu.
2. Người dùng nhập đúng 6 chữ số.
3. Người dùng chọn `Tiếp tục`.
4. Nếu OTP hợp lệ, chuyển sang bước tạo mật khẩu.
5. Nếu OTP sai/hết hạn, giữ người dùng ở bước OTP và hiển thị lỗi phù hợp.
6. `Gửi lại mã` chỉ khả dụng sau cooldown; OTP mới làm OTP cũ mất hiệu lực khi backend thật được triển khai.

### 5.3. Bước Mật khẩu

1. Nhập mật khẩu và xác nhận mật khẩu.
2. FE kiểm tra tối thiểu 8 ký tự, ít nhất một chữ hoa, một chữ số và một ký tự đặc biệt theo requirement hiện tại.
3. Hai giá trị phải trùng nhau.
4. Khi hoàn tất thành công, tài khoản được tạo ở trạng thái email đã xác minh.
5. Hiển thị success feedback và chuyển về Sign In, điền sẵn email nếu an toàn nhưng không điền mật khẩu.

## 6. Trạng thái và dữ liệu UI

### 6.1. State machine

```text
email_input
  -> requesting_otp
  -> otp_input
  -> verifying_otp
  -> password_input
  -> creating_account
  -> success
  -> sign_in
```

Các trạng thái lỗi quay lại bước hiện tại; không nhảy cóc bước và không tạo tài khoản trước khi email được xác minh.

### 6.2. Trạng thái được phép khôi phục

Để người dùng chuyển sang ứng dụng email rồi quay lại mà không bị dựng lại từ đầu, có thể persist:

- `signupAttemptId` không chứa secret.
- `normalizedEmail`.
- `currentStep`.
- `otpRequestedAt`.
- `otpExpiresAt` khi backend trả về.
- `resendAvailableAt`.

Không persist:

- OTP.
- Password.
- Confirm password.
- Access/refresh token trước khi tài khoản được tạo thành công.

Countdown phải tính từ timestamp tuyệt đối, không chỉ giảm một biến trong memory. Khi app resume, UI tính lại thời gian còn lại từ `resendAvailableAt`/`otpExpiresAt`.

### 6.3. Back, close và resume

- Back từ Password về OTP: xóa password và confirm password.
- Back từ OTP về Email: xóa OTP; giữ email để sửa.
- Rời flow: xóa toàn bộ dữ liệu nhạy cảm; attempt có thể được resume theo policy backend nếu còn hiệu lực.
- App background/foreground: giữ step và email; không reload/reset UI chỉ vì người dùng mở ứng dụng email.
- Attempt hết hạn khi resume: thông báo rõ và đưa người dùng về bước Email hoặc cho gửi lại mã theo policy.

## 7. UI specification

### 7.1. Cấu trúc chung

- Dùng `SafeAreaView`/safe-area thật; không vẽ status bar hoặc home indicator giả.
- Container chính scroll được khi bàn phím mở và trên màn hình thấp.
- Primary button có chiều cao/vùng chạm tối thiểu 48 px.
- Poppins là font ưu tiên; có system fallback nếu font chưa tải xong.
- Không dùng màu cam cũ có contrast thấp cho text/action.

### 7.2. Bước Email

- Title: `Tạo tài khoản`.
- Label: `Email`.
- Placeholder: `Nhập email của bạn`.
- Keyboard/content type: email address; tắt auto-capitalize; cho phép paste.
- Primary action: `Gửi mã OTP`.
- Link phụ: `Đã có tài khoản? Đăng nhập`.
- Inline error tối thiểu: trống, sai định dạng, email đã tồn tại, lỗi gửi mã.
- Không dùng thông báo khác nhau để tiết lộ email đã tồn tại ở endpoint công khai nếu backend chọn generic anti-enumeration response; contract cụ thể phải được chốt ở task backend.

### 7.3. Bước OTP

- Title: `Xác thực email`.
- Helper: `Nhập mã 6 chữ số đã gửi tới <email đã mask>`.
- OTP chỉ nhận chữ số, tối đa 6 ký tự, cho phép paste toàn bộ mã.
- Primary action: `Tiếp tục` disabled khi chưa đủ 6 số hoặc đang verify.
- Secondary action: `Gửi lại mã` cùng countdown.
- Lỗi tối thiểu: mã sai, mã hết hạn, vượt giới hạn thử, resend thất bại.

### 7.4. Bước Mật khẩu

- Title: `Tạo mật khẩu`.
- Hai field: `Mật khẩu` và `Xác nhận mật khẩu`.
- Có show/hide password và accessibility label.
- Hiển thị rule mật khẩu trước khi submit; không chỉ báo lỗi sau cùng.
- Primary action: `Đăng ký`.
- Không lưu password khi back, close hoặc app bị kill.

## 8. Validation và error contract tối thiểu

| Tình huống | Kết quả UI |
| --- | --- |
| Email trống/sai định dạng | Không gửi request; hiển thị lỗi inline |
| Email đã có tài khoản | Hiển thị thông báo theo contract anti-enumeration được backend chốt; có lối sang Sign In |
| Gửi OTP thất bại | Giữ email và cho retry an toàn |
| OTP chưa đủ 6 số | Disable `Tiếp tục` |
| OTP sai | Xóa/đánh dấu field theo thiết kế; giữ ở bước OTP |
| OTP hết hạn | Cho resend theo policy; không sang Password |
| Password không đạt rule | Hiển thị rule chưa đạt; không submit |
| Confirm password không khớp | Lỗi tại confirm field |
| Tạo tài khoản trùng do race condition | Không tạo user thứ hai; hướng dẫn Sign In/khôi phục tài khoản |
| Mất mạng | Giữ state không nhạy cảm, cho retry, không gửi lặp ngầm |

## 9. Technical mapping cho repository `smart-tro`

Giữ implementation theo foundation hiện có. Nếu tên thư mục khác, Dev phải map theo convention repo, không tạo kiến trúc song song chỉ để khớp spec.

Tách tối thiểu:

- Screen/container cho từng bước hoặc một flow container với step components rõ ràng.
- Validation schema cho email/password.
- `SignUpGateway` interface tách mock khỏi API thật.
- Auth flow state có thể restore phần không nhạy cảm.
- Shared input/button/token từ design foundation.

Mock gateway tối thiểu:

- request OTP thành công.
- invalid/expired OTP.
- duplicate email.
- create account thành công/thất bại.
- resend cooldown 60 giây.

## 10. Accessibility và khác biệt có chủ đích với Figma cũ

| ID | Vấn đề của frame cũ | Quyết định triển khai |
| --- | --- | --- |
| UI-D01 | Button thấp hơn vùng chạm an toàn | Vùng chạm tối thiểu 48 px |
| UI-D02 | Chữ trắng trên cam cũ contrast thấp | Dùng `#B84D00` cho primary background |
| UI-D03 | Text cam cũ trên nền trắng contrast thấp | Dùng `#A84300` cho text/action |
| UI-D04 | OTP không nói mã gửi tới đâu | Hiển thị email đã mask |
| UI-D05 | Thiếu resend/error/loading state | Bổ sung đầy đủ state vận hành |
| UI-D06 | Frame vẽ OS chrome | Dùng OS/safe-area thật |
| UI-D07 | Social button trông như hoạt động | Review visual-only; production ẩn bằng feature flag |

## 11. Kiểm thử bắt buộc trước PR

Dev phải tự lập test cases và chạy unit/component tests cho phần mình thay đổi. Coverage 100% áp dụng cho logic mới của flow Sign Up thuộc phạm vi task; không dùng con số coverage để thay thế test hành vi.

Tối thiểu phải có:

- Email trim/lowercase/format validation.
- OTP trống, ngắn, đủ 6 số, ký tự không phải số, paste 6 số.
- Password rule và confirm mismatch.
- Email → OTP → Password → Success → Sign In.
- Back/resume/background và attempt hết hạn.
- Duplicate email và retry sau network failure.
- Không có OTP/password trong route params, log hoặc storage.
- Accessibility label, focus order, keyboard behavior và vùng chạm.

## 12. Out of scope của task FE Sign Up đầu tiên

- Email provider thật và template email production.
- Backend OTP policy/rate limit/anti-abuse hoàn chỉnh.
- Social/OAuth account linking.
- Đổi email, quên mật khẩu và account recovery.
- Xác thực số điện thoại.
- Auto-login sau đăng ký.

## 13. Definition of Done

- Ba bước hoạt động đúng với mock gateway trên mobile và Expo Web preview.
- UI bám capture Figma mới đã đổi sang email và các khác biệt `UI-D01` đến `UI-D07`.
- State restore không làm lộ hoặc persist OTP/password.
- Unit/component tests cho logic mới đạt 100% coverage và tất cả test pass.
- Lint/typecheck pass.
- PR mô tả test evidence, preview URL/build và các deviation còn lại.
- PM/PO review UI trên build từ code đã merge; QA chỉ test sau khi PR merge và môi trường review/develop dùng đúng merge SHA.

## 14. Gate trước khi bàn giao PM

Chỉ chuyển trạng thái tài liệu thành `Ready for PM` khi đủ:

- [ ] Figma node đầu tiên đổi từ Phone sang Email.
- [ ] OTP helper đổi từ SMS/số điện thoại sang email đã mask.
- [ ] Ba capture mới được xuất cùng một revision Figma và nhúng lại vào tài liệu.
- [x] Requirement List `SM001` dùng email.
- [x] User Story `1.0` dùng email OTP 6 chữ số.
- [x] SRS heading/logic Sign Up dùng email.
- [x] Activity Diagram Sign Up by Email không còn bước/text số điện thoại; có source `.puml`.
- [x] Quyết định identity/Sign In được ghi tại `docs/11-smarttro-sign-in-and-auth-identity-mvp.md`.

Khi chưa đủ gate, PM chỉ được cập nhật knowledge/requirement; chưa enqueue Dev triển khai UI.
