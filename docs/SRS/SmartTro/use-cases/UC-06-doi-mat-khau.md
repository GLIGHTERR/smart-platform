# SmartTrọ - UC-06 Đổi mật khẩu

## 1. Trạng thái tài liệu và nguồn

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | **LIVING SPEC - PO đã chốt logic ngày 2026-11-04; Web và Android app UAT PASS ngày 2026-11-12** |
| Phạm vi | Đổi mật khẩu cục bộ cho người dùng đã xác thực trên SmartTrọ Web và Android Expo/EAS preview. iOS không thuộc delivery baseline này. |
| Tài liệu cũ | Mục 3.7 SRS là đường cơ sở tham khảo, không phải phê duyệt. Quy tắc SHA-256 trong tài liệu cũ bị thay thế bởi kết luận ở mục 5 và không được dùng mặc định. |
| Các đầu mã nguồn đã rà soát | `smart-platform@19fa7ff491d5e9f5a3ba4b4a53728eec145d76da`; `smart-tro@ab463c04bc16d55c78448ac29dcb0e8f86bb9f22`; `smart-platform-services@dff03a7a49186e7c8ba82efbac9e21fa16910a6b`. |
| Baseline đã nghiệm thu | Client `smart-tro@7445acd384ec3402d5a7e7c213252a5691d9d6a2`; backend deploy `smart-platform-services@9d94d0980f4273ae9be3e4ccf9ef40964db8b7dd`; EAS build `46b0c648-746d-4cd8-bd57-6c93741bae29`. |
| Quyết định PO | `UC06-D01..D10` đã ở trạng thái cuối; implementation/session behavior, Web QA/UAT và Mobile QA/app UAT đã được xác minh. |

Tài liệu này là living specification chuẩn, độc lập cho UC-06. Ma trận quyết định được chốt theo `PO_APPROVED` ngày 2026-11-04 và các correction UI/session/delivery được nghiệm thu đến ngày 2026-11-12. Không ghi giá trị mật khẩu, token, cookie, credential, PII thật hoặc log nhạy cảm trong tài liệu/evidence.

## 2. Mục tiêu, tác nhân và ranh giới

**Tác nhân:** người dùng đã đăng nhập, có tài khoản cục bộ đang hoạt động. Subject luôn lấy từ session đã xác thực; client không gửi ID để chọn tài khoản.

**Kích hoạt:** từ UC-04 Account/Personal, người dùng chọn `Đổi mật khẩu`.

**Tiền điều kiện:** session hiện tại hợp lệ; tài khoản có mật khẩu cục bộ; UI/API đang dùng contract đã được phê duyệt.

**Hậu điều kiện khi thành công:** mật khẩu mới được lưu atomically theo kết luận lưu trữ đã duyệt, mọi session khác bị thu hồi, session hiện tại được rotate/reissue hoặc duy trì an toàn để người dùng vẫn đăng nhập, sự kiện bảo mật/audit được ghi không lộ secret, và UI hiển thị thành công rồi trở về UC-04/Profile.

**Trong phạm vi:** biểu mẫu mật khẩu hiện tại/mới/xác nhận, xác minh, validation, vòng đời session, lỗi an toàn, accessibility, contract API/kiểm thử/bàn giao.

**Ngoài phạm vi UC-06:** đặt mật khẩu cho tài khoản chỉ dùng social, bước MFA/re-authentication mới, liên kết tài khoản, reset/recovery của UC-03 và quản lý thiết bị chi tiết.

## 3. Truy vết và đối chiếu

| Nguồn | Ràng buộc kế thừa / khoảng trống |
| --- | --- |
| UC-01 Sign Up | Chính sách PO đã kế thừa cho UC-06: 8-128 ký tự, chữ thường, chữ hoa, chữ số, ký tự đặc biệt; xác nhận phải khớp. Mật khẩu giữ nguyên ký tự chính xác, không trim/normalize, không đi vào route, log, analytics hoặc persistent storage. |
| UC-02 Sign In | `SIGNIN-D09` với 5 lần sai/15 phút đã được PO dùng lại theo subject cho UC-06. `SIGNIN-D10` về token rotation là contract Sign In; UC-06 phải rotate/reissue hoặc duy trì an toàn session hiện tại sau khi thu hồi các session khác. |
| UC-03 Forgot Password | Reset vẫn thu hồi toàn bộ session và yêu cầu Sign In; đây là hành vi riêng của UC-03, không áp dụng cho thành công của UC-06. Audit không log secret. |
| UC-04 Account/Personal | Action `Đổi mật khẩu` là entry chính thức sang biểu mẫu UC-06; success quay lại Account/Profile. |
| UC-05 Edit Personal | Kế thừa mẫu subject-only, server authoritative và sign-out khi session hết hạn/bị thu hồi/không hoạt động; UC-06 thành công quay về UC-04/Profile trong khi vẫn giữ người dùng đăng nhập an toàn. |
| Baseline dịch vụ đã nghiệm thu | Endpoint change-password đã được reconcile theo D01/D03/D06, deploy trên exact SHA ở mục 10 và được kiểm thử giữ session hiện tại, thu hồi session khác, audit/migration và safe error mapping. |

## 4. Luồng chuẩn đã được PO phê duyệt

### 4.1. Luồng chính

1. Từ UC-04, người dùng chọn `Đổi mật khẩu`; hệ thống mở biểu mẫu riêng.
2. Biểu mẫu hiển thị `Mật khẩu hiện tại`, `Mật khẩu mới`, `Xác nhận mật khẩu mới`; không prefill trường nào. Cả ba trường là secure/password input, mặc định che giá trị và có nút mắt hoạt động độc lập để hiện/ẩn.
3. Ban đầu cả ba trường không hiển thị lỗi. Một trường chỉ chuyển sang trạng thái đã tương tác sau lần blur đầu tiên; từ đó lỗi của chính trường được cập nhật khi người dùng tiếp tục gõ. Khi blur: cả ba trường kiểm tra bắt buộc; mật khẩu hiện tại và mật khẩu mới kiểm tra pattern D01; xác nhận mật khẩu mới kiểm tra khớp với mật khẩu mới. Việc mật khẩu hiện tại có đúng trên server chỉ được kiểm tra khi submit.
4. API xác thực subject từ session, revalidate mọi ràng buộc, xác minh mật khẩu hiện tại và thực hiện mutation/session/audit trong transaction hoặc thao tác authoritative.
5. Khi API thành công, UI xóa cả ba trường khỏi memory, thu hồi các session khác, duy trì/rotate an toàn session hiện tại, rồi thông báo thành công và trở về UC-04/Profile. Không điều hướng về Sign In và không làm mất session hiện tại.

### 4.2. Luồng thay thế và ngoại lệ

| Tình huống | Hành vi yêu cầu |
| --- | --- |
| Client validation thất bại / mật khẩu mới-xác nhận không khớp / mật khẩu mới giống mật khẩu hiện tại | Không gọi API nếu có thể xác định cục bộ; hiển thị phản hồi nội dòng an toàn; không làm lộ mật khẩu hiện tại. |
| Mật khẩu hiện tại không đúng | Giữ người dùng tại biểu mẫu và giữ session hiện tại; xóa trường mật khẩu hiện tại nếu implementation cần giảm retention, hiển thị lỗi nội dòng an toàn chỉ sau submit, không phân biệt trạng thái tài khoản hay raw backend message; throttle 5 lần thất bại/15 phút theo subject. |
| Session hết hạn, bị thu hồi, không hoạt động hoặc subject không khớp | Không đổi mật khẩu; xóa trạng thái nhạy cảm; chạy hành vi chung session-expired/sign-out của UC-04/05. |
| Bị rate limited / cooldown | Không mutation; hiển thị action/thời điểm thử lại theo server contract; không suy luận trạng thái tài khoản. |
| Timeout, offline, lỗi `5xx` | Không tự kết luận mutation thất bại và không blind retry. Chỉ retry an toàn sau khi có authoritative outcome/query; các trường mật khẩu không được persist. |
| Double submit / request đồng thời | UI chỉ có một request đang chờ. Server phải xác định final authoritative outcome; response của request sau không được tạo mutation hay session thứ hai. |
| Quay lại, hủy, app xuống nền/khởi động lại | Khi có input, back/cancel phải confirm bằng nội dung theo nghĩa `Thao tác đổi mật khẩu chưa hoàn thiện`; không dùng copy gây hiểu nhầm như mật khẩu tài khoản đã bị xóa hoặc không thể khôi phục. Không save draft. Mọi exit/background/restart đều xóa ba trường và không persist secret. |

## 5. Ma trận quyết định bắt buộc

| ID | Quyết định cuối | Lý do | Chủ sở hữu | Tác động | Trạng thái |
| --- | --- | --- | --- | --- | --- |
| UC06-D01 | Kế thừa UC-01: 8-128, lowercase, uppercase, digit, special; giữ nguyên ký tự chính xác, không trim/normalize; mật khẩu mới khác mật khẩu hiện tại; chưa áp dụng last-N history trong MVP. | Nhất quán UC-01/03 mà không thay đổi secret. | PO + Security | FE validation, DTO, biên kiểm thử. | APPROVED 2026-11-04 |
| UC06-D02 | Mật khẩu hiện tại sai trả generic safe error; throttle 5 failures/15 minutes theo subject; public code/copy ổn định, không trả raw error hay account state. | Chống disclosure và brute force. | PO + Security | Status/code/copy, rate limiter, audit, UX. | APPROVED 2026-11-04 |
| UC06-D03 | Thu hồi mọi session khác; rotate/reissue hoặc duy trì an toàn session hiện tại để người dùng vẫn đăng nhập. Nếu không thể duy trì an toàn, phải ghi rõ blocker kỹ thuật cho PO, không tự chuyển sang logout. | Giảm rủi ro session theft nhưng giữ continuity của phiên hiện tại. | PO + Security | Auth response, session lifecycle, regression đa thiết bị. | APPROVED 2026-11-04 |
| UC06-D04 | Hiển thị success feedback an toàn rồi điều hướng về UC-04/Profile; không điều hướng Sign In sau thành công. Back/cancel khi có input phải confirm discard; không save draft; exit/background/restart xóa secret. | UX continuity theo override PO, không giữ lại secret. | PO + Design | G1 giao diện, navigation, accessibility, UAT. | APPROVED 2026-11-04 |
| UC06-D05 | Dùng lại throttle D02; immutable audit event chỉ có subject và metadata đã mask; không gửi email/push notification trong MVP. | Audit đủ truy vết nhưng bảo vệ privacy. | PO + Security | Rate limiter, audit event, hỗ trợ/truyền thông. | APPROVED 2026-11-04 |
| UC06-D06 | Idempotency key + authoritative outcome/query; một subject chỉ có một mutation đang xử lý; không blind retry; response cũ không ghi đè final state. | Tránh mutation/session trùng và success sai sau timeout. | PO + BE | API contract, persistence, client retry, kiểm thử. | APPROVED 2026-11-04 |
| UC06-D07 | Giữ salted slow hash hiện hành sau khi Security/BE xác minh implementation; không migration nếu compatible; cấm legacy SHA-256. | Bảo toàn lưu trữ an toàn và dùng evidence trước khi thay đổi. | Security + PO | Rà soát compatibility, migration, kiểm thử. | APPROVED 2026-11-04 |
| UC06-D08 | Không đưa secret vào logs/analytics/routes/persistent storage/clipboard; không có exception trong MVP. | Ràng buộc cross-UC đã được phê duyệt. | PO + Security | FE telemetry, API logging, QA evidence. | APPROVED 2026-11-04 |
| UC06-D09 | Tạo Figma/reference chuẩn mới cho biểu mẫu và các trạng thái error/loading/success/session-expired/keyboard/responsive/accessibility trước PO duyệt giao diện; mock/tài liệu cũ không phải approval. | UC-04 chỉ phê duyệt điểm vào, chưa có giao diện chuẩn UC-06. | PO + Design | Cổng G1, screenshot review, accessibility AC. | APPROVED 2026-11-04 |
| UC06-D10 | Web trước; mobile chỉ kiểm thử thủ công theo build/SHA được PO cho phép; UAT sau QA PASS. | Cổng bàn giao của parent. | PO | Kế hoạch QA, release evidence. | APPROVED 2026-11-04 |

## 6. Yêu cầu UI/UX và accessibility

- Entry route là UC-04 Personal/Account; chỉ route tới biểu mẫu UC-06 production đã nghiệm thu.
- Dùng một biểu mẫu riêng với điều khiển hiện/ẩn secure-entry, nhãn dùng được với screen reader, thứ tự focus rõ ràng, focus hiển thị được, cuộn an toàn khi mở keyboard, vùng chạm tối thiểu 48 px và thông báo lỗi.
- Cả ba password field mặc định phải che giá trị; nút mắt của từng trường chỉ đổi visibility của chính trường đó và phải có accessible name/state. Không được để mặc định hiện plaintext hoặc dùng một state chung làm ba nút không hoạt động độc lập.
- Appearance của password field UC-06 giữ visual đã được PO duyệt cho màn đổi mật khẩu. Có thể dùng component riêng hoặc variant riêng; không sửa style/logic của password field dùng tại Sign In, Sign Up và Forgot Password chỉ để phục vụ UC-06. Ngược lại, không được thay UC-06 bằng auth-field appearance nếu PO chỉ duyệt thay đổi logic.
- Validation không hiển thị lỗi ngay lúc màn vừa mở. Sau blur đầu tiên, trường đã touched được validate live khi người dùng sửa: required cho cả ba; pattern cho current/new; match cho confirm. Server-only current-password correctness chỉ xuất hiện sau submit.
- Vô hiệu action chính khi đang gửi; không có request trùng; chỉ giữ trạng thái UI không nhạy cảm cần thiết để hiển thị lỗi.
- Không tự động sao chép mật khẩu vào clipboard. Không prefill hoặc giữ lại mật khẩu sau submit, cancel, background/resume, logout, đổi tài khoản hoặc khởi động lại process.
- Khi sửa giao diện, phải đối chiếu lại reference đã được PO duyệt cho biểu mẫu, copy, success, error, loading, session-expired, keyboard, responsive và accessibility. Mock/tài liệu cũ không thay thế living spec/current approved reference.

## 7. Hợp đồng API/session/security cuối

### 7.1. Hợp đồng cơ sở

Endpoint `POST /auth/password/change` chỉ xác thực bearer/session subject. Body chứa trường mật khẩu hiện tại, mới và xác nhận; không có subject ID. Request dùng TLS, `Cache-Control: no-store`, ngăn intermediary cache và không bao giờ echo secret.

Khi thành công, chỉ trả acknowledgement và next-state UC-04/Profile; không trả credential. Server thu hồi các session khác và rotate/reissue hoặc duy trì an toàn session hiện tại để người dùng vẫn đăng nhập. Error mapping dùng mã an toàn, ổn định, không raw server message: validation/confirmation/reuse (`400`); unauthenticated/expired/revoked (`401`); inactive/forbidden subject (`403`); current-password invalid dùng safe `401` classification và được FE map riêng thành lỗi mật khẩu hiện tại, không map thành session-expired; rate limit (`429` kèm retry metadata); conflict/concurrency (`409`); retryable unavailability (`5xx`).

### 7.2. Yêu cầu server

- Chỉ xác thực subject hiện tại; xác minh mật khẩu hiện tại theo hành vi timing-safe/anti-enumeration và revalidate policy ở server.
- Chỉ lưu dạng biểu diễn mật khẩu một chiều salted slow-hash đã được phê duyệt và xác minh trên baseline triển khai. Cấm SHA-256-only storage làm mặc định implementation.
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
- **Thì** ban đầu không trường nào hiển thị lỗi và cả ba trường đều che mật khẩu theo mặc định.
- **Khi** một trường blur lần đầu hoặc người dùng tiếp tục sửa trường đã touched
- **Thì** required/pattern/match được đánh giá đúng theo loại trường; current-password correctness chưa được kiểm tra trước submit.
- **Và khi** current/new/confirm bị thiếu, không hợp lệ biên, vi phạm D01, mật khẩu mới bằng mật khẩu hiện tại hoặc xác nhận khác nhau
- **Thì** không có mutation nào được thực hiện, phản hồi có accessibility và an toàn, secret không được giữ lại sau exit/resume.

### AC-06-03 - Xác minh mật khẩu hiện tại và chống lạm dụng

- **Giả sử** subject hợp lệ đã xác thực gửi biểu mẫu hợp lệ về cú pháp
- **Khi** xác minh mật khẩu hiện tại thất bại hoặc server áp dụng bảo vệ D02/D05
- **Thì** mật khẩu không đổi, người dùng vẫn ở trong session hiện tại và tại biểu mẫu, response/copy không tiết lộ thêm account state và retry/cooldown tuân thủ policy đã duyệt.

### AC-06-04 - Mutation thành công và kết quả session

- **Giả sử** xác minh mật khẩu hiện tại và mọi validation đều đạt
- **Khi** server xử lý đúng một mutation
- **Thì** mật khẩu mới là authoritative, audit bảo vệ privacy, mọi session khác bị thu hồi, session hiện tại được rotate/reissue hoặc duy trì an toàn, và UI hiển thị success rồi trở về UC-04/Profile.
- **Và** nếu không thể giữ session hiện tại an toàn, implementation phải dừng tại blocker cụ thể để PO quyết định; không tự đổi sang logout/Sign In.

### AC-06-05 - Lỗi, timeout và concurrency

- **Giả sử** xảy ra timeout, offline/lỗi `5xx`, double submit hoặc thay đổi đồng thời
- **Khi** request tranh chấp hoặc response chưa chắc chắn
- **Thì** UI không uncontrolled retry hoặc hiển thị thành công chưa được xác minh; server cung cấp một final authoritative state theo D06; không tạo session/mutation trùng.

### AC-06-06 - Privacy và accessibility

- **Giả sử** bất kỳ đường UI/API/test/audit nào của UC-06
- **Khi** đường đó xử lý biểu mẫu hoặc response
- **Thì** không có password/session secret trong route parameter, storage, clipboard, analytics, log, error, screenshot hoặc evidence; việc duy trì session hiện tại không được làm lộ hoặc tái sử dụng credential không an toàn.
- **Và** secure field, label, focus order, error announcement, contrast, touch target, keyboard behavior, loading và responsive state đáp ứng D09 đã duyệt.
- **Và** ba visibility toggle hoạt động độc lập; implementation UC-06 không làm thay đổi ngoài scope appearance/logic của password field tại Sign In, Sign Up hoặc Forgot Password.

## 9. Ma trận kiểm thử và DoD cho downstream

| Lớp | Trường hợp bắt buộc |
| --- | --- |
| Unit | Biên D01 và validation quan hệ; untouched/blur/touched-live-validation; ba visibility toggle độc lập; error mapper; xóa trạng thái no-secret; khóa submit; trạng thái dirty/back; navigation theo D03/D04; regression bảo đảm auth password fields ngoài UC-06 không đổi. |
| API/integration | Subject-only auth; sai mật khẩu hiện tại; policy/reuse/confirm; inactive/expired/revoked; rate limit; lỗi an toàn; cache header; transaction password/session/audit atomic; idempotency/concurrency; không log secret. |
| UI/Web | Entry từ UC-04; loading/double-submit; mọi điểm đến lỗi/thành công; focus/screen-reader/keyboard; bằng chứng kích thước 320/375/390/430 và chiều cao ngắn sau khi D09 được hiện thực. |
| System/regression | Chính sách đăng ký UC-01, sign-in/session rotation/throttle UC-02, reset toàn bộ session và yêu cầu Sign In của UC-03, session expiry/account-switch UC-04/05, cùng việc giữ session hiện tại an toàn sau UC-06. |
| Mobile | Chỉ build sau khi PO cho phép rõ app, target và exact source SHA. Dev tự trigger Expo/EAS và bàn giao build ID/fingerprint/install URL/terminal evidence. Mobile QA chạy trên đúng artifact; PO app UAT chỉ sau Mobile QA PASS. Web QA/UAT không thay thế nhánh này khi app UAT nằm trong scope. |

**DoD:** canonical reference và UI logic đã được PO duyệt; API/session contract dùng API thật, không dùng policy mock; Dev cung cấp unit-test/coverage, PR/merge/deploy và artifact evidence; QA kiểm thử độc lập trên exact merge/deploy/build SHA; Web UAT và Android app UAT trong scope đều PASS. Story/Delivery Control không được đóng sau Web UAT nếu Expo build, Mobile QA hoặc PO app UAT còn thiếu. `ROOT_SYNC` chỉ chạy sau platform UAT cuối cùng và không chứa dữ liệu nhạy cảm.

## 10. Baseline implementation và evidence đã nghiệm thu

| Thành phần | Evidence cuối |
| --- | --- |
| Living spec | `smart-platform` PR #19 merge `3311956abd6ff845dee6d730ddec0d8831c59679`; session/navigation correction PR #20 merge `0262b446a94c2883c3eaeaac1655e60bf2f83128`. |
| SmartTrọ client | PR #107 merge/deploy SHA `7445acd384ec3402d5a7e7c213252a5691d9d6a2`; Web QA và PO Web UAT PASS. |
| Backend | `smart-platform-services` PR #27 merge/deploy SHA `9d94d0980f4273ae9be3e4ccf9ef40964db8b7dd`; Render live/readiness PASS; migration `PasswordChange1700000007000` có trong deployed ledger. |
| Android | Expo/EAS preview internal build `46b0c648-746d-4cd8-bd57-6c93741bae29`, fingerprint `5554613157122cf3cf218ee1f445fb151adca922`, build từ exact client SHA `7445acd384ec3402d5a7e7c213252a5691d9d6a2`. Mobile QA `GLI-258` PASS và PO app UAT `GLI-260` PASS ngày 2026-11-12. |

Behavior cuối đã nghiệm thu: sai mật khẩu hiện tại không sign out; đổi mật khẩu thành công giữ session hiện tại và thu hồi session khác; success quay về Account/Profile; ba password field che mặc định với toggle độc lập; validation không hiện trước blur đầu tiên; component/variant UC-06 không làm đổi ngoài scope các màn Sign In, Sign Up và Forgot Password.

## 11. Delivery closure và quy tắc tái sử dụng

UC-06 đạt Web UAT và Android app UAT trên baseline ở mục 10. Khi tái triển khai hoặc sửa defect:

1. Không coi Web UAT PASS là đủ nếu mobile/app UAT nằm trong scope.
2. Mobile build cần authorization theo app, target và exact source SHA; sau authorization Dev tự build và handoff artifact.
3. Chuỗi đóng bắt buộc là implementation/merge/deploy → Web QA/UAT → authorized Expo build → Mobile QA → PO app UAT → `ROOT_SYNC`.
4. PM vận hành bằng wakeup theo sự kiện; không polling. PR/artifact phải gắn trực tiếp vào task tương ứng.
5. Chỉ thay đổi session behavior, validation timing hoặc password-field component isolation khi PO cập nhật living spec này.
