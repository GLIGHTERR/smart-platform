# SmartTrọ - UC-06 Đổi mật khẩu

## 1. Trạng thái tài liệu và nguồn

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái G0 | **HOÀN THÀNH - PO đã chốt quyết định ngày 2026-11-04** |
| Phạm vi | Đổi mật khẩu cục bộ cho người dùng đã xác thực. G0 chưa cho phép triển khai FE/BE; Figma/reference chuẩn ở G1 và PO duyệt giao diện vẫn là cổng bắt buộc. |
| Tài liệu cũ | Mục 3.7 SRS là đường cơ sở tham khảo, không phải phê duyệt. Quy tắc SHA-256 trong tài liệu cũ bị thay thế bởi kết luận ở mục 5 và không được dùng mặc định. |
| Các đầu mã nguồn đã rà soát | `smart-platform@19fa7ff491d5e9f5a3ba4b4a53728eec145d76da`; `smart-tro@ab463c04bc16d55c78448ac29dcb0e8f86bb9f22`; `smart-platform-services@dff03a7a49186e7c8ba82efbac9e21fa16910a6b`. |
| Quyết định PO | `UC06-D01..D10` đã ở trạng thái cuối; `UC06-D07` vẫn yêu cầu Security/BE xác minh implementation trước G2. |

Tài liệu này là đặc tả G0 chuẩn, độc lập cho UC-06. Ma trận quyết định bên dưới đã được chốt theo `PO_APPROVED` ngày 2026-11-04; chỉ G1 Figma/reference và PO duyệt giao diện mới cho phép mở FE/UI. Không ghi giá trị mật khẩu, token, cookie, credential, PII thật hoặc log nhạy cảm trong tài liệu/evidence.

## 2. Mục tiêu, tác nhân và ranh giới

**Tác nhân:** người dùng đã đăng nhập, có tài khoản cục bộ đang hoạt động. Subject luôn lấy từ session đã xác thực; client không gửi ID để chọn tài khoản.

**Kích hoạt:** từ UC-04 Account/Personal, người dùng chọn `Đổi mật khẩu`.

**Tiền điều kiện:** session hiện tại hợp lệ; tài khoản có mật khẩu cục bộ; UI/API đang dùng contract đã được phê duyệt.

**Hậu điều kiện khi thành công:** mật khẩu mới được lưu atomically theo kết luận lưu trữ đã duyệt, toàn bộ session bị thu hồi theo `UC06-D03`, sự kiện bảo mật/audit được ghi không lộ secret, và UI điều hướng theo quyết định đã duyệt.

**Trong phạm vi:** biểu mẫu mật khẩu hiện tại/mới/xác nhận, xác minh, validation, vòng đời session, lỗi an toàn, accessibility, contract API/kiểm thử/bàn giao.

**Ngoài phạm vi G0/UC-06:** đặt mật khẩu cho tài khoản chỉ dùng social, bước MFA/re-authentication mới, liên kết tài khoản, reset/recovery của UC-03, quản lý thiết bị chi tiết và implementation/deploy.

## 3. Truy vết và đối chiếu

| Nguồn | Ràng buộc kế thừa / khoảng trống |
| --- | --- |
| UC-01 Sign Up | Chính sách PO đã kế thừa cho UC-06: 8-128 ký tự, chữ thường, chữ hoa, chữ số, ký tự đặc biệt; xác nhận phải khớp. Mật khẩu giữ nguyên ký tự chính xác, không trim/normalize, không đi vào route, log, analytics hoặc persistent storage. |
| UC-02 Sign In | `SIGNIN-D09` với 5 lần sai/15 phút đã được PO dùng lại theo subject cho UC-06. `SIGNIN-D10` về token rotation là contract Sign In; UC-06 thu hồi toàn bộ session và không cấp session mới theo D03. |
| UC-03 Forgot Password | Reset thu hồi toàn bộ session và không auto-login là tiền lệ mà PO đã chọn cho UC-06; audit không log secret. |
| UC-04 Account/Personal | FRS đã phê duyệt action `Đổi mật khẩu` chỉ để điều hướng sang UC-06. Khi rà soát source, `smart-tro` đang điều hướng đến placeholder `Destination`, chưa có biểu mẫu UC-06. |
| UC-05 Edit Personal | Kế thừa mẫu subject-only, server authoritative và sign-out khi session hết hạn/bị thu hồi/không hoạt động; UC-06 đã chọn thành công về Sign In, không quay UC-04. |
| Mã nguồn dịch vụ hiện tại | Có endpoint/service change-password và password hasher dùng salt/slow hash. Mã nguồn hiện hữu thiếu confirm và cấp session mới sau revoke, vì vậy G2 phải reconcile theo D01/D03/D06; mã nguồn không phải deploy evidence. |

## 4. Luồng chuẩn đã được PO phê duyệt

### 4.1. Luồng chính

1. Từ UC-04, người dùng chọn `Đổi mật khẩu`; hệ thống mở biểu mẫu riêng.
2. Biểu mẫu hiển thị `Mật khẩu hiện tại`, `Mật khẩu mới`, `Xác nhận mật khẩu mới`; không prefill trường nào.
3. Người dùng nhập giá trị và chọn action chính. UI validation phía client theo policy đã duyệt, đối chiếu mật khẩu mới/xác nhận và khóa biểu mẫu khi request đang xử lý.
4. API xác thực subject từ session, revalidate mọi ràng buộc, xác minh mật khẩu hiện tại và thực hiện mutation/session/audit trong transaction hoặc thao tác authoritative.
5. Khi API thành công, UI xóa cả ba trường khỏi memory, xử lý session/điểm đến theo `UC06-D03` và `UC06-D04`, rồi thông báo kết quả an toàn.

### 4.2. Luồng thay thế và ngoại lệ

| Tình huống | Hành vi yêu cầu |
| --- | --- |
| Client validation thất bại / mật khẩu mới-xác nhận không khớp / mật khẩu mới giống mật khẩu hiện tại | Không gọi API nếu có thể xác định cục bộ; hiển thị phản hồi nội dòng an toàn; không làm lộ mật khẩu hiện tại. |
| Mật khẩu hiện tại không đúng | Giữ biểu mẫu, xóa trường mật khẩu hiện tại, thông báo generic an toàn, không phân biệt trạng thái tài khoản hay raw backend message; throttle 5 lần thất bại/15 phút theo subject. |
| Session hết hạn, bị thu hồi, không hoạt động hoặc subject không khớp | Không đổi mật khẩu; xóa trạng thái nhạy cảm; chạy hành vi chung session-expired/sign-out của UC-04/05. |
| Bị rate limited / cooldown | Không mutation; hiển thị action/thời điểm thử lại theo server contract; không suy luận trạng thái tài khoản. |
| Timeout, offline, lỗi `5xx` | Không tự kết luận mutation thất bại và không blind retry. Chỉ retry an toàn sau khi có authoritative outcome/query; các trường mật khẩu không được persist. |
| Double submit / request đồng thời | UI chỉ có một request đang chờ. Server phải xác định final authoritative outcome; response của request sau không được tạo mutation hay session thứ hai. |
| Quay lại, hủy, app xuống nền/khởi động lại | Khi có input, back/cancel phải confirm discard; không save draft. Mọi exit/background/restart đều xóa ba trường và không persist secret. |

## 5. Ma trận quyết định bắt buộc

| ID | Quyết định cuối | Lý do | Chủ sở hữu | Tác động | Trạng thái |
| --- | --- | --- | --- | --- | --- |
| UC06-D01 | Kế thừa UC-01: 8-128, lowercase, uppercase, digit, special; giữ nguyên ký tự chính xác, không trim/normalize; mật khẩu mới khác mật khẩu hiện tại; chưa áp dụng last-N history trong MVP. | Nhất quán UC-01/03 mà không thay đổi secret. | PO + Security | FE validation, DTO, biên kiểm thử. | APPROVED 2026-11-04 |
| UC06-D02 | Mật khẩu hiện tại sai trả generic safe error; throttle 5 failures/15 minutes theo subject; public code/copy ổn định, không trả raw error hay account state. | Chống disclosure và brute force. | PO + Security | Status/code/copy, rate limiter, audit, UX. | APPROVED 2026-11-04 |
| UC06-D03 | Thu hồi toàn bộ session, gồm cả session hiện tại; không auto-login/cấp session mới; người dùng Sign In lại. | Đồng nhất recovery và giảm rủi ro session theft. | PO + Security | Auth response, navigation, regression đa thiết bị. | APPROVED 2026-11-04 |
| UC06-D04 | Hiển thị success feedback an toàn rồi điều hướng Sign In. Back/cancel khi có input phải confirm discard; không save draft; exit/background/restart xóa secret. | UX rõ ràng theo D03, không giữ lại secret. | PO + Design | G1 giao diện, navigation, accessibility, UAT. | APPROVED 2026-11-04 |
| UC06-D05 | Dùng lại throttle D02; immutable audit event chỉ có subject và metadata đã mask; không gửi email/push notification trong MVP. | Audit đủ truy vết nhưng bảo vệ privacy. | PO + Security | Rate limiter, audit event, hỗ trợ/truyền thông. | APPROVED 2026-11-04 |
| UC06-D06 | Idempotency key + authoritative outcome/query; một subject chỉ có một mutation đang xử lý; không blind retry; response cũ không ghi đè final state. | Tránh mutation/session trùng và success sai sau timeout. | PO + BE | API contract, persistence, client retry, kiểm thử. | APPROVED 2026-11-04 |
| UC06-D07 | Giữ salted slow hash hiện hành sau khi Security/BE xác minh implementation; không migration nếu compatible; cấm legacy SHA-256. | Bảo toàn lưu trữ an toàn và dùng evidence trước khi thay đổi. | Security + PO | Rà soát compatibility, migration, kiểm thử. | APPROVED 2026-11-04 |
| UC06-D08 | Không đưa secret vào logs/analytics/routes/persistent storage/clipboard; không có exception trong MVP. | Ràng buộc cross-UC đã được phê duyệt. | PO + Security | FE telemetry, API logging, QA evidence. | APPROVED 2026-11-04 |
| UC06-D09 | Tạo Figma/reference chuẩn mới cho biểu mẫu và các trạng thái error/loading/success/session-expired/keyboard/responsive/accessibility trước PO duyệt giao diện; mock/tài liệu cũ không phải approval. | UC-04 chỉ phê duyệt điểm vào, chưa có giao diện chuẩn UC-06. | PO + Design | Cổng G1, screenshot review, accessibility AC. | APPROVED 2026-11-04 |
| UC06-D10 | Web trước; mobile chỉ kiểm thử thủ công theo build/SHA được PO cho phép; UAT sau QA PASS. | Cổng bàn giao của parent. | PO | Kế hoạch QA, release evidence. | APPROVED 2026-11-04 |

## 6. Yêu cầu UI/UX và accessibility

- Entry route là UC-04 Personal; không được coi placeholder hiện tại là màn UC-06 có thể sử dụng.
- Dùng một biểu mẫu riêng với điều khiển hiện/ẩn secure-entry, nhãn dùng được với screen reader, thứ tự focus rõ ràng, focus hiển thị được, cuộn an toàn khi mở keyboard, vùng chạm tối thiểu 48 px và thông báo lỗi.
- Vô hiệu action chính khi đang gửi; không có request trùng; chỉ giữ trạng thái UI không nhạy cảm cần thiết để hiển thị lỗi.
- Không tự động sao chép mật khẩu vào clipboard. Không prefill hoặc giữ lại mật khẩu sau submit, cancel, background/resume, logout, đổi tài khoản hoặc khởi động lại process.
- G1 phải tạo Figma/reference chuẩn trước PO duyệt giao diện: biểu mẫu, copy, success, error, loading, session-expired, keyboard, responsive và accessibility. Mock/tài liệu cũ không là nguồn giao diện chuẩn.

## 7. Hợp đồng API/session/security cho G2 (yêu cầu đã duyệt, chưa cho phép implementation)

### 7.1. Hợp đồng cơ sở

Service đã rà soát có `POST /auth/password/change`; G2 phải reconcile endpoint này với hợp đồng đã duyệt trước integration. Endpoint chỉ xác thực bearer/session subject. Body chứa trường mật khẩu hiện tại, mới và xác nhận; không có subject ID. Request dùng TLS, `Cache-Control: no-store`, ngăn intermediary cache và không bao giờ echo secret.

Khi thành công, chỉ trả acknowledgement và next-state Sign In; không được trả hoặc cấp session mới. Error mapping dùng mã an toàn, ổn định, không raw server message: validation/confirmation/reuse (`400`); unauthenticated/expired/revoked (`401`); inactive/forbidden subject (`403`); current-password invalid (`400` hoặc `401`, được đóng băng trong hợp đồng API G2); rate limit (`429` kèm retry metadata); conflict/concurrency (`409`); retryable unavailability (`5xx`).

### 7.2. Yêu cầu server

- Chỉ xác thực subject hiện tại; xác minh mật khẩu hiện tại theo hành vi timing-safe/anti-enumeration và revalidate policy ở server.
- Chỉ lưu dạng biểu diễn mật khẩu một chiều đã được phê duyệt. Source hiện tại là evidence của salted slow-hash candidate, không phải xác minh deploy hay phê duyệt migration. Cấm SHA-256-only storage làm mặc định implementation.
- Atomically cập nhật mật khẩu, áp dụng đúng phạm vi thu hồi session đã duyệt, ghi privacy-safe audit event và tạo một authoritative outcome cho concurrency.
- Logs, traces, analytics, error body, audit payload, persistent client store, navigation parameter, screenshot và test fixture phải bỏ mật khẩu/session secret. Không tạo trường telemetry mới chứa secret.

## 8. Tiêu chí chấp nhận

### AC-06-01 - Entry và subject

- **Giả sử** người dùng có mật khẩu cục bộ, đã xác thực và đang ở UC-04 Personal
- **Khi** họ chọn `Đổi mật khẩu`
- **Thì** hệ thống chỉ mở biểu mẫu UC-06 đã được phê duyệt và không bao giờ nhận subject do client chọn.
- **Và** session hết hạn, bị thu hồi, không hoạt động hoặc không khớp phải xóa trường nhạy cảm và dùng hành vi session-expired/sign-out chung.

### AC-06-02 - Validation và xác nhận

- **Giả sử** biểu mẫu đang mở
- **Khi** current/new/confirm bị thiếu, không hợp lệ biên, vi phạm D01, mật khẩu mới bằng mật khẩu hiện tại hoặc xác nhận khác nhau
- **Thì** không có mutation nào được thực hiện, phản hồi có accessibility và an toàn, secret không được giữ lại sau exit/resume.

### AC-06-03 - Xác minh mật khẩu hiện tại và chống lạm dụng

- **Giả sử** subject hợp lệ đã xác thực gửi biểu mẫu hợp lệ về cú pháp
- **Khi** xác minh mật khẩu hiện tại thất bại hoặc server áp dụng bảo vệ D02/D05
- **Thì** mật khẩu không đổi, response/copy không tiết lộ thêm account state và retry/cooldown tuân thủ policy đã duyệt.

### AC-06-04 - Mutation thành công và kết quả session

- **Giả sử** xác minh mật khẩu hiện tại và mọi validation đều đạt
- **Khi** server xử lý đúng một mutation
- **Thì** mật khẩu mới là authoritative, audit bảo vệ privacy, hành vi session tuân thủ D03 và navigation/feedback tuân thủ D04.

### AC-06-05 - Lỗi, timeout và concurrency

- **Giả sử** xảy ra timeout, offline/lỗi `5xx`, double submit hoặc thay đổi đồng thời
- **Khi** request tranh chấp hoặc response chưa chắc chắn
- **Thì** UI không uncontrolled retry hoặc hiển thị thành công chưa được xác minh; server cung cấp một final authoritative state theo D06; không tạo session/mutation trùng.

### AC-06-06 - Privacy và accessibility

- **Giả sử** bất kỳ đường UI/API/test/audit nào của UC-06
- **Khi** đường đó xử lý biểu mẫu hoặc response
- **Thì** không có password/session secret trong route parameter, storage, clipboard, analytics, log, error, screenshot hoặc evidence.
- **Và** secure field, label, focus order, error announcement, contrast, touch target, keyboard behavior, loading và responsive state đáp ứng D09 đã duyệt.

## 9. Ma trận kiểm thử và DoD cho downstream

| Lớp | Trường hợp bắt buộc |
| --- | --- |
| Unit | Biên D01 và validation quan hệ; error mapper; xóa trạng thái no-secret; khóa submit; trạng thái dirty/back; navigation theo D03/D04. |
| API/integration | Subject-only auth; sai mật khẩu hiện tại; policy/reuse/confirm; inactive/expired/revoked; rate limit; lỗi an toàn; cache header; transaction password/session/audit atomic; idempotency/concurrency; không log secret. |
| UI/Web | Entry từ UC-04; loading/double-submit; mọi điểm đến lỗi/thành công; focus/screen-reader/keyboard; bằng chứng kích thước 320/375/390/430 và chiều cao ngắn sau khi D09 được hiện thực. |
| System/regression | Chính sách đăng ký UC-01, sign-in/session rotation/throttle UC-02, reset toàn bộ session UC-03, session expiry/account-switch UC-04/05. |
| Mobile | Chỉ thủ công sau khi PO cho phép build/SHA cụ thể; bao phủ ma trận chức năng/accessibility tương đương khả thi trên thiết bị. |

**DoD:** G1 tạo D09 canonical reference và nhận PO duyệt giao diện; G2 chỉ sau lần duyệt đó, xác minh Security/BE theo D07 và bảng API code/status được đóng băng; G3 dùng API thật đã duyệt, không dùng policy mock; Dev cung cấp unit-test/coverage evidence theo quality gate; QA kiểm thử độc lập trên merge/deploy SHA chính xác; PO UAT chỉ sau QA PASS. `ROOT_SYNC` chỉ ở trạng thái cuối sau PO UAT và không chứa dữ liệu nhạy cảm.

## 10. Bản đồ khoảng trống và tác động bàn giao

| Repository | Phát hiện chỉ đọc | Tác động downstream |
| --- | --- | --- |
| `smart-platform` | Đặc tả chuẩn này trước G0 chỉ là tài liệu cũ; UC-04/05 và FRS có điểm vào nhưng chưa có giao diện UC-06 chuẩn. | Khoảng trống tài liệu/G1 Design; G0 không thay đổi code. |
| `smart-tro` | Action UC-04 hiện đến placeholder; chưa có biểu mẫu UC-06/API integration. | Màn hình/navigation G1; integration G3 với API thật sau các cổng. |
| `smart-platform-services` | Có mã nguồn change-password nhưng khác D01 confirm/D03 không cấp session mới và chưa có deploy proof. | G2 phải reconcile hợp đồng, hoàn tất xác minh D07 Security/BE và thêm kiểm thử session/audit/idempotency; không dùng lại theo giả định. |

## 11. Handoff G0 cuối

G0 **HOÀN THÀNH**: PO đã phê duyệt cuối `UC06-D01..D10` ngày 2026-11-04 và tài liệu chuẩn này phản ánh đúng bundle đó. Hành động kế tiếp là **chỉ G1**: tạo Figma/reference chuẩn theo D09, để PO duyệt các trạng thái giao diện/accessibility và ghi evidence cuối. Không assign, trigger hoặc implementation FE/BE từ handoff G0 này. G2 vẫn bị chặn bởi PO duyệt giao diện ở G1 và xác minh Security/BE theo D07.
