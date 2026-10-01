# Smart Platform — Context Handoff

> **Cập nhật:** 2026-10-01
>
> **Vai trò:** Context hub cô đọng cho task điều phối và các task nhánh.
>
> **Lưu ý:** Trạng thái issue/PR/branch/deployment bên dưới là snapshot, phải kiểm tra lại trước khi hành động.

## 1. Mục tiêu vận hành

Tách công việc sang các task Codex nhỏ để tránh nạp lại toàn bộ hội thoại dài, nhưng vẫn bảo toàn quyết định đã chốt. Context bền vững nằm trong repo; trạng thái động nằm trên Multica, GitHub và các provider triển khai.

Luồng đồng bộ:

```text
Task điều phối gốc
  ├─ giao task nhánh bằng context tối thiểu
  ├─ task nhánh triển khai + kiểm chứng
  ├─ task nhánh phát ROOT_SYNC khi đóng
  └─ task gốc đọc delta + commit đã merge, rồi cập nhật handoff/ledger
```

Không polling tiến độ liên tục. Việc đồng bộ xảy ra khi task đóng, bị block hoặc PO yêu cầu kiểm tra.

## 2. Bản đồ repository

| Repository | Vai trò | Default branch |
| --- | --- | --- |
| `GLIGHTERR/smart-platform` | Tài liệu hiện hành, quyết định xuyên repo và context hub | `master` |
| `GLIGHTERR/smart-tro` | Ứng dụng người thuê SmartTrọ — React Native/Expo, có web review | `master` |
| `GLIGHTERR/smart-chu` | Ứng dụng chủ trọ SmartChủ — React Native/Expo | `master` |
| `GLIGHTERR/smart-platform-services` | Backend dùng chung cho SmartTrọ, SmartChủ và tương lai SmartAdmin | `master` |

Đường dẫn local thông dụng:

- `/home/glighter/Project/smart-platform`
- `/home/glighter/Project/smart-tro`
- `/home/glighter/Project/smart-chu`
- Clone backend có thể có nhiều worktree; phải xác minh remote và branch trước khi sửa.

## 3. Nguồn tài liệu hiện hành

- Điểm vào: [`docs/README.md`](docs/README.md).
- SmartTrọ UC-01: [`docs/SRS/SmartTro/use-cases/UC-01-sign-up.md`](docs/SRS/SmartTro/use-cases/UC-01-sign-up.md).
- SmartTrọ UC-02: [`docs/SRS/SmartTro/use-cases/UC-02-sign-in.md`](docs/SRS/SmartTro/use-cases/UC-02-sign-in.md).
- SmartTrọ UC-03: [`docs/SRS/SmartTro/use-cases/UC-03-forgot-password.md`](docs/SRS/SmartTro/use-cases/UC-03-forgot-password.md).
- SmartTrọ Home: [`docs/FRS/SmartTro/screens/home-screen.md`](docs/FRS/SmartTro/screens/home-screen.md).
- SmartChủ UC index: [`docs/SRS/SmartChu/use-cases/README.md`](docs/SRS/SmartChu/use-cases/README.md).

`archieve/` chỉ dùng để truy vết. Không dùng baseline cũ để ghi đè living spec đã chốt.

## 4. Quyết định sản phẩm và kỹ thuật đã chốt

### 4.1 Identity và authentication

- MVP dùng **email đã normalize** làm định danh đăng nhập unique; số điện thoại là dữ liệu liên hệ, không phải login identifier.
- Đăng ký: Email → OTP email 6 chữ số → tạo mật khẩu.
- Đăng nhập thông thường: Email + mật khẩu. Hiện không tự thêm Login OTP chỉ vì mockup từng có biến thể đó; muốn thay đổi phải chốt lại requirement/docs.
- Quên mật khẩu: Email → OTP email 6 chữ số → mật khẩu mới.
- Nếu recovery bị force-close/process kill, người dùng đi lại từ đầu; không persist OTP, password hoặc reset token.
- Normal response của recovery phải chống account enumeration.
- Social auth/social-only recovery là scope riêng và phải test trong UC đăng ký/đăng nhập social; không trộn vào UC email/password hiện tại.
- Không lưu refresh token vào `localStorage`. Web ưu tiên cookie bảo mật/HttpOnly theo contract; mobile dùng secure storage phù hợp runtime.

### 4.2 Email delivery

- FE vẫn chờ response của BE trước khi chuyển màn; không optimistic navigation.
- BE chỉ xử lý đồng bộ validation/rate limit/cooldown, tạo challenge nghiệp vụ và durable transactional outbox job.
- Dựng nội dung email và gọi Brevo chạy ở worker bất đồng bộ với retry/backoff/audit.
- Không dùng fire-and-forget in-memory vì Render restart/scale-down có thể làm mất email.
- Không lưu/log OTP plaintext trong outbox hoặc audit.
- Outbox consumer phải xử lý đúng result shape của TypeORM raw query; claim job hiện dùng CTE `UPDATE` kèm final `SELECT`, quarantine payload lỗi và giữ polling error boundary để một job lỗi không làm dừng consumer.
- Pattern này áp dụng cho mọi quy trình gửi email sau này; hiện ưu tiên Forgot Password rồi Signup. UC-02 Sign In hiện không có email delivery.

### 4.3 UI/mobile

- Figma là nguồn visual; requirement/living spec là nguồn behavior. Nếu conflict phải hỏi PO.
- Font ứng dụng hiện chốt **Be Vietnam Pro**; phải bundle đúng weights cần dùng, không phụ thuộc glyph fallback gây nét chữ không đồng nhất.
- Social icons dùng managed SVG/PNG assets, không dùng FontAwesome glyph nếu làm sai mockup/runtime.
- App người thuê phải hiển thị tên **SmartTrọ** và dùng bộ icon chính thức/adaptive/monochrome trong source app; đổi display name/icon trên Expo dashboard không thay thế cấu hình native của project.
- Cần kiểm tra cả Android device và web review; web không đại diện đầy đủ cho runtime mobile.
- Runtime error/offline dùng pattern chung: nếu đã có dữ liệu hợp lệ thì giữ UI ổn định, retry cục bộ vùng lỗi và hiển thị non-blocking toast; initial load dùng skeleton vùng động. Không hiển thị raw backend error hoặc dữ liệu nhạy cảm trong toast.
- SmartTrọ Home hỗ trợ 0, 1 hoặc nhiều hợp đồng active; nhiều hợp đồng dùng carousel và ưu tiên card sắp hết hạn gần nhất. Ngày trên card là ngày hết hạn; fallback display name là email một dòng có tail ellipsis.

### 4.4 Quy trình delivery

- Từ các UC mới: tạo task cha theo UC, sau đó tách task con theo vai trò thực tế.
- FE/UI được dựng và PO review trước BE. Sau đó mới BE/BE-GAP, integration, QA và UAT.
- QA ưu tiên web/review environment khi device automation không ổn định hoặc tốn quota; PO test/UAT trên device thật khi cần.
- Chỉ auto-build Expo khi merge/push vào `master`; không build mỗi push lên branch cá nhân của Dev.
- Không merge/deploy tự động nếu task chỉ yêu cầu tạo PR hoặc handoff review.
- Sau merge, xóa branch ngắn hạn. Nếu sau này có `develop`/`staging`, policy sẽ được chốt lại.

## 5. Hạ tầng đã dùng

- Backend review: Render Web Service, free tier có thể cold start.
- Database: Neon Postgres.
- Email transactional: Brevo.
- Mobile build/distribution: Expo/EAS preview APK.
- Backend chạy migration khi startup sau khi biến `DATABASE_RUN_MIGRATIONS_ON_STARTUP` được cấu hình cho môi trường phù hợp.

Không ghi secret hoặc giá trị credential vào handoff. Khi cần kiểm tra cấu hình, đọc trực tiếp provider hoặc environment được ủy quyền.

## 6. Snapshot công việc ngày 2026-10-02

### SmartTrọ UC-03

- Parent `GLI-61` và các child trực tiếp `GLI-62`, `GLI-63`, `GLI-64`, `GLI-65`, `GLI-66`, `GLI-68`, `GLI-97`: `done` theo xác nhận Multica và PO ngày 2026-10-01.
- PO xác nhận luồng Forgot Password hoàn tất và cho phép đóng toàn bộ scope UC-03.
- `GLI-67` branding/icon không thuộc danh sách child trực tiếp đã đóng ở trên; phải kiểm tra lại trạng thái issue/PR/build trước khi xử lý tiếp.

### Email outbox

- `GLI-97` Forgot Password transactional outbox: `done`. PR #14 triển khai foundation đã merge; PR #15 hotfix lỗi claim result đã merge và deploy thành công. Render đang giữ `PASSWORD_RECOVERY_OUTBOX_CONSUMER_ENABLED=true` tại thời điểm xác nhận.
- `GLI-98` Signup transactional outbox: `backlog`; dependency foundation từ GLI-97 đã hoàn tất nhưng chưa được tự động khởi chạy.
- Không mở task tối ưu Login OTP vì UC-02 Sign In hiện không gửi OTP theo living spec.

### Hướng tiếp theo đã chuẩn bị nhưng chưa tự động khởi chạy

- SmartTrọ Home Screen: parent `GLI-69` đang `in_progress`; `GLI-70` đã `done` sau khi PR #8 merge tại `57850e5bfe0854ad934e55304af2670f7fc5563c`; `GLI-71` được mở gate theo lệnh PO ngày 2026-10-02, còn `GLI-72..75` vẫn `backlog`. Home không chứa room discovery; `D.S.Trọ` chỉ điều hướng tới UC-10.
- SmartChủ Auth: parent UC-01 `GLI-76`, UC-02 `GLI-83`, UC-03 `GLI-90`; các task con đang backlog. Phải review/chốt docs và Figma trước khi assign Dev.

## 7. Figma và design handoff

- File: `Smart Platform`, key `rsjbGO3ul8lzKKKTj38r0t`.
- Forgot Password node từng dùng: `2005:3261`.
- Cụm design-system/button inverse từng dùng: `2065:6459`.
- Quyền/MCP Figma có quota theo thời điểm; nếu hết quota thì dùng capture đã được PO xác nhận và ghi rõ giới hạn evidence.

## 8. Quy tắc đồng bộ task gốc

Mọi task nhánh phải kết thúc bằng `ROOT_SYNC`. Task điều phối thực hiện đúng một lần sau close/merge:

1. Đọc `ROOT_SYNC` và issue/PR tương ứng.
2. Xác minh SHA đã merge vào default branch; không chỉ tin branch cá nhân.
3. Xác minh test/build/deploy/UAT theo scope.
4. Cập nhật quyết định bền vững vào file này; không ghi log chi tiết từng command.
5. Thêm một dòng vào [`.codex/handoffs/ledger.md`](.codex/handoffs/ledger.md).
6. Nếu delta chỉ là trạng thái động, ghi ledger nhưng không làm phình handoff.
7. Chỉ tạo task tiếp theo khi dependency/gate đã đạt.

## 9. Những điều task mới phải luôn kiểm tra lại

- Current Multica status/assignee/run/blocker.
- PR đã merge hay mới chỉ được tạo.
- Commit có thật sự ở `origin/master` hay không.
- Render/Expo build đang dùng commit nào.
- Migration/schema đã chạy trên môi trường đích hay mới chỉ có trong source.
- Figma node/capture có phải revision PO vừa duyệt hay không.
