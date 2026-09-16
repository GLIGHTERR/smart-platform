# SmartTrọ — Sign In and Auth Identity MVP

## 1. Trạng thái quyết định

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | **Approved — requirement baseline** |
| Phạm vi triển khai hiện tại | Sign In SmartTrọ bằng email và mật khẩu |
| Định danh tài khoản MVP | Email normalized, unique toàn hệ thống identity |
| Số điện thoại | Dữ liệu liên hệ tùy chọn; không dùng để login/unique trong MVP |
| Ngày chốt | 2026-09-16 |
| Trạng thái bàn giao Dev | Chưa giao — cần đồng bộ Figma/capture và Activity Diagram |

Tài liệu này là nguồn chuẩn cho Sign In và quyết định định danh tài khoản MVP. Nó đồng thời là “impact gate”: trước khi PM giao một task mới có sử dụng email, số điện thoại, user identity, OTP hoặc account linking, PM phải kiểm tra bảng ảnh hưởng ở mục 8 và cập nhật requirement liên quan trước.

## 2. Quyết định MVP

1. Người dùng đăng ký bằng email, OTP email 6 chữ số và mật khẩu.
2. Người dùng đăng nhập bằng email và mật khẩu.
3. Sign In bình thường không yêu cầu OTP ở mỗi lần đăng nhập.
4. Email normalized là unique login identifier của account.
5. Số điện thoại không unique và không dùng làm credential trong MVP; một số điện thoại có thể xuất hiện ở dữ liệu liên hệ theo rule nghiệp vụ riêng trong tương lai.
6. OTP ở Sign Up chứng minh người dùng kiểm soát mailbox tại thời điểm kích hoạt account; nó không phải chữ ký số hay high-assurance MFA cho hợp đồng/thanh toán.
7. Social login và phone login có thể bổ sung sau, nhưng phải link vào identity hiện có; không được tự tạo account trùng chỉ vì provider/phone khác.

## 3. Sign In flow

### 3.1. Happy path

1. Người dùng mở màn Sign In.
2. Nhập email và mật khẩu.
3. FE trim email, dùng lowercase cho đối chiếu identifier và giữ nguyên mật khẩu.
4. Người dùng chọn `Đăng nhập`.
5. Hệ thống xác thực credential.
6. Nếu thành công, hệ thống tạo session/token theo contract backend và điều hướng vào app.

### 3.2. Không có OTP trong Sign In cơ bản

Activity Diagram cũ “Đăng nhập bằng email” đang gửi OTP sau khi credential hợp lệ. Hành vi đó **không thuộc MVP Sign In đã chốt**. OTP/MFA chỉ được thêm sau qua một quyết định riêng, ví dụ:

- đăng nhập thiết bị mới/rủi ro cao;
- thay đổi email hoặc mật khẩu;
- recovery;
- tác vụ nhạy cảm như ký hợp đồng/thanh toán nếu policy sau này yêu cầu.

Không được suy diễn các trường hợp trên thành scope hiện tại.

## 4. UI requirement tối thiểu

- Field `Email`.
- Field `Mật khẩu` có show/hide.
- Primary action `Đăng nhập`.
- Link `Quên mật khẩu` nhưng luồng recovery chưa đổi trong đợt này.
- Link `Chưa có tài khoản? Đăng ký`.
- Loading state chống submit lặp.
- Generic credential error để tránh tiết lộ email có tồn tại hay không.
- Keyboard, focus order, autofill/content type và accessibility label phù hợp.
- Không log/persist mật khẩu.

Sau Sign Up thành công, Sign In có thể nhận email prefill từ navigation state an toàn; không truyền password hoặc OTP.

## 5. Error và security behavior

| Tình huống | Hành vi |
| --- | --- |
| Email trống/sai định dạng | Lỗi inline; không gửi request |
| Credential sai | Thông báo generic; không xác nhận riêng email tồn tại |
| Submit lặp | Chỉ một request active; button ở loading/disabled |
| Mất mạng/timeout | Giữ email, xóa/không persist password theo lifecycle an toàn, cho retry rõ ràng |
| Account chưa verify | Contract backend trả một trạng thái riêng; hướng dẫn resend OTP/tiếp tục activation, không tạo account mới |
| Account bị khóa/rate limited | Hiển thị thông báo và thời điểm/thao tác tiếp theo theo policy backend |

Policy khóa sau 5 lần sai trong 72 giờ đang có trong User Story cũ nhưng chưa được tái phê duyệt trong quyết định email này. Giữ nó ở trạng thái `Needs confirmation` trước task backend thay vì hard-code ở FE.

## 6. Acceptance Criteria Sign In

- Given người dùng có account đã verify email và credential hợp lệ, when đăng nhập bằng email + mật khẩu, then hệ thống tạo session và điều hướng vào app mà không yêu cầu OTP.
- Given email hoặc mật khẩu sai, when người dùng submit, then hệ thống trả lỗi generic và không tiết lộ email có tồn tại.
- Given request đang xử lý, when người dùng bấm lại, then FE không tạo request đăng nhập trùng.
- Given người dùng vừa đăng ký thành công, when được chuyển về Sign In, then email có thể được prefill nhưng password/OTP không được truyền hoặc lưu.
- Given app bị background/foreground trong lúc nhập Sign In, then email có thể được giữ trong UI state nhưng password không được ghi vào persistent storage/log.

## 7. Traceability hiện tại

| Nguồn | Mục cần dùng | Trạng thái |
| --- | --- | --- |
| Requirement List SmartTrọ | `SM001`, `SM002` | Đã đổi tên requirement sang email |
| User Story SmartTrọ | `1.0`, `2.0` | Đã đổi Sign Up/Sign In sang email; bỏ OTP bắt buộc sau mỗi Sign In |
| SRS SmartTrọ | UC-1, UC-2 | Đã đổi heading/logic trọng yếu sang email |
| FRS SmartTrọ | Không tìm thấy section auth có thể truy vết rõ trong bản hiện tại | Không sửa trong đợt này; khi FRS auth được bổ sung phải theo baseline này |
| Activity Diagram Sign Up by Email | PNG + source `.puml` | Đã cập nhật theo email OTP 6 chữ số |
| Activity Diagram Sign In by Email | PNG + source `.puml` | Đã cập nhật; Sign In thông thường không còn OTP |
| Figma SmartTrọ Sign Up | Nodes `237:1161`, `237:1137`, `237:1185` | Stale copy/capture; layout được giữ |
| Figma SmartTrọ Sign In | Node cần PM/Designer xác định | Chưa kiểm tra/capture trong đợt này |

## 8. MVP auth identity impact register

Đây là danh sách phải được ghi nhớ và kiểm tra dần. Không sửa tất cả ngay khi chưa tới scope; nhưng trước khi PM giao task tương ứng, requirement/docs phải được cập nhật.

| Khu vực tương lai | Ảnh hưởng của email-as-identity | Gate trước bàn giao PM |
| --- | --- | --- |
| Quên mật khẩu / account recovery | Tài liệu hiện dùng OTP qua SĐT | Chốt recovery bằng OTP email, expiry/attempt/rate limit và update `SM004`, US `3.0`, SRS/diagram |
| Đổi email | Email là credential unique, không còn là profile field sửa tự do | Tạo flow re-auth + verify email mới + duplicate check + session/audit policy |
| Cập nhật hồ sơ | SĐT có thể sửa như contact; email phải hiển thị trạng thái verified và không update trực tiếp | Sửa requirement/profile AC trước task Profile |
| SmartChủ auth | Cần cùng identity service và cùng rule unique | Audit `SM038+`, SmartChủ US/SRS/Figma trước foundation auth |
| Social login | Provider email có thể trùng account đã có | Chốt linking, verified-email trust và conflict recovery; không auto-create duplicate |
| Phone login hoặc phone verification về sau | Phone không phải unique trong MVP | Chốt migration/linking và duplicate resolution trước khi bật |
| Messaging/contact | Không dùng email login làm public contact mặc định | Chốt privacy và kênh liên hệ; phone/in-app chat là dữ liệu/chức năng riêng |
| Contract/e-signature | OTP Sign Up không đủ làm bằng chứng ký | Chốt signer verification/audit riêng trong task Contract |
| Payment/high-risk action | Sign In cơ bản không có MFA | Chốt step-up auth/risk policy riêng nếu cần |
| Notification | Email đã verify có thể nhận transactional mail | Chốt template, consent, deliverability, bounce và preference trước task notification |
| Data migration/import | User cũ có thể thiếu hoặc trùng email | Có migration report, conflict queue và không tạo account ngầm |
| Admin/support | Lookup/unlock/resend không được lộ dữ liệu | Chốt permission, audit log và anti-enumeration trước task admin support |
| Analytics/audit | Không dùng email thô làm analytics key | Dùng immutable user ID; mask/redact PII trong log/report |

## 9. Quy tắc bắt buộc cho PM và agent

Trước khi giao một task mới có liên quan đến account/identity:

1. Tìm task trong impact register.
2. Kiểm tra Requirement List, User Story, SRS/FRS, Activity Diagram, Figma và API contract liên quan.
3. Nếu còn phone-as-login, email-editable tự do, OTP-on-every-login hoặc ambiguity, PM phải comment và tag PO để xác nhận.
4. Chỉ sau khi docs được cập nhật và traceability rõ ràng mới giao Dev.
5. Comment bàn giao phải link tới tài liệu này và revision cụ thể.

## 10. Các quyết định còn mở trước backend auth

- OTP expiry thực tế.
- Số lần nhập OTP sai tối đa và thời gian khóa challenge.
- Rate limit theo email/IP/device.
- Anti-enumeration response cho Sign Up/resend.
- Failed-login threshold, lock duration và cơ chế unlock.
- Session/refresh-token lifetime, logout all devices và trusted device.
- Email provider, deliverability, bounce và template.

Các mục này không chặn review UI mock, nhưng chặn việc coi task backend auth là implementation-ready.
