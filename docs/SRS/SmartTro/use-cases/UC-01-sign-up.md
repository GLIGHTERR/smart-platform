# SmartTro — UC-01 Đăng ký

## Trạng thái và phạm vi

| Thuộc tính | Giá trị |
| --- | --- |
| Baseline | **PO_REBASELINE — G0 DOCS**, 2026-10-07 |
| Owner quyết định | PO |
| Flow chuẩn | Email -> OTP -> Thông tin cá nhân -> Mật khẩu -> Sign In |
| Điều kiện mở Dev | PR docs đã merge và PO duyệt baseline |

PO_REBASELINE thay thế toàn bộ PM_DECISION trước đây của GLI-114. Không sửa code hoặc merge/deploy hai PR pre-baseline `smart-tro#31` và `smart-platform-services#18`. Hai PR này phải được đánh giá lại sau G0, không phải bằng chứng cho baseline hiện hành.

Email đã normalize là định danh đăng nhập duy nhất. Số điện thoại là dữ liệu liên hệ tùy chọn, nullable, non-unique; không là login identifier và không nhận OTP. Đăng ký thành công quay về Sign In, không auto-login.

## Quyết định PO bắt buộc

| ID | Quyết định |
| --- | --- |
| SU-G0-01 | Hiển thị label đúng `Họ và tên (bắt buộc)`. Normalize bằng trim đầu/cuối và collapse khoảng trắng lặp; sau normalize không được rỗng. Một từ vẫn hợp lệ. |
| SU-G0-02 | SĐT tùy chọn; chỉ validate khi người dùng nhập, không dùng để login, OTP hoặc uniqueness. |
| SU-G0-03 | Thu thập full name + SĐT tại bước riêng sau OTP. Chỉ tạo/persist account khi chọn `Tạo tài khoản` ở bước Mật khẩu. |
| SU-G0-04 | Home ưu tiên full name; email là fallback cho dữ liệu legacy/missing. |
| SU-G0-05 | Đổi email từ OTP: FE xóa OTP đang nhập, về Email với email cũ prefill; không xóa vật lý challenge/outbox. |
| SU-G0-06 | Chỉ khi email normalized mới khác và request thành công, backend atomically supersede/invalidate challenge cũ và tạo challenge/outbox mới. Email không đổi reuse attempt/cooldown hợp lệ, không resend tự động. |
| SU-G0-07 | Back từ Mật khẩu về Thông tin cá nhân xóa password + confirm password, giữ name/phone. |
| SU-G0-08 | Resend cooldown 60 giây theo absolute backend timestamp; resend thành công vô hiệu OTP cũ; tối đa 5 lần/giờ/email. |
| SU-G0-09 | Button/touch target tối thiểu 48 px, contrast accessible; blue outline chỉ cho focus state thật. |
| SU-G0-10 | Giữ nguyên wording social button hiện tại; social auth không được suy diễn là hoạt động. |

## State machine và dữ liệu

```text
email_input
  -> requesting_otp -> otp_input -> verifying_otp
  -> personal_info_input -> password_input -> creating_account
  -> success -> sign_in
```

- Lỗi quay lại bước hiện tại, không được nhảy cóc hoặc tạo account trước `creating_account` thành công.
- Có thể giữ để resume khi còn hợp lệ: `signupAttemptId`, normalized email, step, `otpExpiresAt`, `resendAvailableAt`; countdown tính từ timestamp tuyệt đối.
- Có thể giữ trong memory flow: full name đã normalize và phone. Chỉ persist chúng vào account sau complete thành công.
- Không persist OTP, password, confirm password, token hoặc dữ liệu nhạy cảm vào storage, route parameter hay log.
- Background/foreground không reset flow chỉ vì mở app email. Nếu attempt hết hạn khi resume, hiển thị rõ và chỉ cho Email/Resend theo policy.
- Close/rời flow xóa dữ liệu nhạy cảm; không xóa vật lý challenge/outbox chỉ bởi hành động UI.

## Hành vi theo bước

### Email

1. Người dùng nhập email và chọn `Gửi OTP`.
2. FE normalize theo contract backend, kiểm tra định dạng cơ bản và chờ response thành công trước khi sang OTP.
3. Backend trả attempt, expiry và `resendAvailableAt`; không trả OTP.
4. Wording social button hiện có được giữ nguyên.

### OTP

- OTP chỉ nhận 6 chữ số và cho paste toàn bộ mã.
- OTP đúng chuyển tới Thông tin cá nhân; không chuyển thẳng Mật khẩu.
- Sai, hết hạn, vượt giới hạn hoặc resend thất bại giữ tại OTP và map lỗi an toàn theo contract.
- `Gửi lại mã` chỉ khả dụng khi `now >= resendAvailableAt`; thành công phải vô hiệu OTP cũ.
- Đổi email xóa OTP UI và về Email với email cũ prefill. Với email normalized không đổi, FE/BE reuse attempt/cooldown hợp lệ và không resend tự động. Với email normalized khác, backend atomically supersede/invalidate challenge cũ, tạo challenge/outbox mới và trả attempt mới.

### Thông tin cá nhân

- Field: `Họ và tên (bắt buộc)` và SĐT tùy chọn.
- Full name: trim + collapse whitespace lặp, sau normalize phải khác rỗng; không yêu cầu hai từ.
- Phone: `null` khi bỏ trống; chỉ validate format khi có giá trị; không kiểm tra unique.
- Tiếp tục chỉ khi full name hợp lệ và phone, nếu có, hợp lệ.

### Mật khẩu

- Mật khẩu và Xác nhận mật khẩu tuân theo policy backend và phải trùng nhau.
- `Tạo tài khoản` gửi payload cuối và là thời điểm duy nhất tạo/persist user, displayName, phone.
- Back về Thông tin cá nhân xóa cả password field, giữ full name/phone.
- Thành công quay về Sign In; có thể prefill email nếu an toàn, không cấp session hoặc auto-login.

## API và challenge lifecycle

### Request OTP / đổi email

`POST /auth/signup/request-otp` nhận email đã normalize ở backend boundary và trả attempt identifier, expiry, absolute `resendAvailableAt`.

| Điều kiện | Hành vi backend |
| --- | --- |
| Email bằng normalized email của attempt còn hợp lệ | Reuse attempt/cooldown, không tạo outbox hoặc resend tự động. |
| Email normalized khác và request hợp lệ | Trong một transaction: supersede/invalidate challenge cũ, tạo challenge mới + durable outbox mới; OTP cũ mất hiệu lực. |
| Request không hợp lệ/rate-limited | Không đổi challenge hợp lệ hiện có; trả error mapping an toàn. |

Challenge/outbox là dữ liệu vận hành/audit; UI không xóa vật lý chúng. OTP plaintext không được lưu hoặc log.

### Hoàn tất đăng ký

`POST /auth/signup/complete` chỉ được gọi sau verified attempt và ở bước Mật khẩu:

```json
{
  "email": "normalized-email@example.com",
  "attemptId": "signup-attempt-id",
  "code": "verified-otp-context",
  "displayName": "Nguyen Van A",
  "phone": "+84901234567",
  "password": "secret"
}
```

- `displayName` bắt buộc; sau trim + collapse whitespace không rỗng.
- `phone` tùy chọn; gửi `null` nếu không nhập; không là credential/OTP/unique key.
- G2 BE phải khóa tên field proof OTP trong OpenAPI; FE không giữ OTP ngoài phạm vi cần thiết.
- Backend tạo user, persist display name/phone và consume verified attempt atomically; không phát access/refresh token.

## Validation, lỗi, bảo mật và compatibility

| Boundary | Yêu cầu |
| --- | --- |
| FE | Chặn email sai, OTP không đủ 6 số, full name rỗng sau normalize, phone đã nhập sai format, password sai policy, confirm mismatch. |
| BE | Lặp lại validation quan trọng; normalize input ở boundary; enforce cooldown 60 giây và 5 resend/giờ/email. |
| Error mapping | UI dùng mã/lỗi đã chốt, không hiện raw backend error hoặc tiết lộ email tồn tại qua public response. |
| Privacy | Không log/persist OTP, password, confirm password hoặc token. Phone/full name chỉ dùng cho account sau complete thành công. |
| Legacy | Account có full name null/blank vẫn hoạt động; Home fallback email. Không migration/backfill trong G0. |
| Rollout | G1 FE dùng mock/review contract đã PO duyệt; G2 BE khóa API/persistence; integration chỉ sau khi hai phần cùng merge theo baseline này. |

## Accessibility và visual boundary

- Touch target/button tối thiểu 48 px, focus order/accessibility label theo step, contrast accessible.
- Blue outline chỉ ở focus state thật, không phải decoration tĩnh.
- G1 phải đưa capture/mockup bước Thông tin cá nhân cho PO review. Không có approved asset mới trong G0 nên không tự tạo visual baseline.

## Acceptance criteria

### AC-01 — Happy path
Given email hợp lệ, OTP đúng, full name hợp lệ và phone hợp lệ hoặc bỏ trống
When người dùng hoàn tất `Tạo tài khoản`
Then account được tạo đúng một lần với displayName đã normalize và phone nullable
And ứng dụng quay về Sign In, không auto-login.

### AC-02 — OTP và resend
Given người dùng ở bước OTP
When OTP sai, hết hạn hoặc chưa đủ 6 số
Then không được vào Thông tin cá nhân và lỗi contract được hiển thị.

Given resend bị cooldown/quota chặn
When người dùng yêu cầu resend
Then FE dùng timestamp backend để chặn đúng 60 giây và backend giới hạn tối đa 5 lần/giờ/email.

Given resend thành công
Then OTP cũ mất hiệu lực.

### AC-03 — Đổi/không đổi email
Given người dùng đang nhập OTP
When đổi email
Then FE xóa OTP và về Email với email cũ prefill.

Given email normalized không đổi
When gửi lại request email
Then attempt/cooldown hợp lệ được reuse và không resend tự động.

Given email normalized khác và request thành công
Then challenge cũ bị supersede/invalidate và challenge/outbox mới được tạo atomically.

### AC-04 — Thông tin cá nhân và back navigation
Given full name null, rỗng hoặc chỉ whitespace sau normalize
When người dùng tiếp tục
Then không thể vào Mật khẩu.

Given full name có whitespace đầu/cuối hoặc lặp
When tiếp tục
Then payload dùng giá trị trim + collapse whitespace.

Given phone bỏ trống
When tạo account
Then phone được persist nullable; phone chỉ validate khi có nhập.

Given người dùng back từ Mật khẩu
Then password/confirm bị xóa, còn full name/phone được giữ.

### AC-05 — Legacy, UX và security
Given account legacy thiếu full name
When Home hiển thị định danh
Then email là fallback.

Then các action đạt 48 px, contrast accessible, không có blue outline giả
And OTP/password/token không xuất hiện trong storage, route parameter hoặc log.

## Traceability và gates

| Gate | Scope | Điều kiện ra |
| --- | --- | --- |
| G0 Docs | Living spec + traceability | PR docs merge, PO duyệt baseline |
| G1 FE | UI/state/mock contract | PO review capture/flow Email -> OTP -> Personal Info -> Password |
| PO review | Quyết định visual/behavior G1 | Approval rõ ràng trước BE |
| G2 BE | API, validation, challenge/outbox lifecycle, persistence | Contract/tests/coverage + deploy evidence |
| G3 Integration | FE + BE cùng baseline | Build đúng merge SHA + integration evidence |
| G4 QA | System/regression | PASS/FAIL/BLOCKED verdict |
| G5 UAT | BA/PO nghiệm thu | PO disposition |

`smart-tro#31` và `smart-platform-services#18` không thỏa flow, fields, lifecycle hoặc gates ở đây. Không merge chúng như implementation của G0; G1/G2 phải re-evaluate hoặc thay thế sau PO approval.

## DoD G0

- File này và `docs/Requirement_List/SmartTro/Requirements.md` phản ánh PO_REBASELINE.
- Không sửa code FE/BE, không merge/deploy PR pre-baseline.
- PR SmartPlatform nêu file cập nhật, validation, impact #31/#18 và ambiguity còn lại.
- Sau handoff, assignee nghiệp vụ trả về PO. Không mở G1 tới khi PR docs merge và PO duyệt baseline.
