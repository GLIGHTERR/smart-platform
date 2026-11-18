# SmartChủ - UC-08 Đổi mật khẩu

> **Trạng thái:** Draft living spec - quyết định PO round 3; chờ D05 mockup/state reference trước handoff implementation.
> **Thay thế:** baseline legacy SHA-256 và successful-change cap `2 lần/ngày`.

## Mục tiêu

Chủ trọ đã xác thực thay mật khẩu của account bằng mật khẩu hiện tại, mật khẩu mới và xác nhận mật khẩu.

## Canonical session behavior

- Normal Sign Out: revoke current session.
- Forgot Password: revoke all sessions/refresh grants, quay về Sign In với email prefill và không auto-login.
- Change Password: revoke all sessions/refresh grants, quay về Sign In; không giữ current session.

Đây là latest PO decision. Backend `smart-platform-services` master hiện còn preserve current session, revoke other sessions và trả `Profile` cho Change Password; đây là implementation gap cần BE gate sau này sửa code/tests/docs, không sửa code trong G0.

## Security and throttling

- Password composition dùng policy shared/auth đã chốt ở D04; storage không dùng SHA-256 thuần.
- Current backend master throttle failed current-password attempts theo login defaults: `5/user` trong `15 phút`; `20/IP hoặc device`; lock `15 phút`.
- Failed-current-password throttle tách khỏi successful password-change frequency. Bỏ legacy rule `2 lần/ngày`; sau mỗi Change Password thành công áp dụng cooldown `5 phút` trước lần thành công tiếp theo.
- Không log, store hoặc đưa password vào navigation/persistent state.

## Luồng

1. Chủ trọ mở `Đổi mật khẩu` từ tab `Cá nhân`.
2. App thu current password, new password và confirmation theo UI reference được duyệt.
3. Backend xác thực, áp dụng failed-attempt throttle khi cần, cập nhật password và revoke sessions theo canonical behavior.
4. App xoá credential cục bộ và điều hướng về Sign In; Back navigation không cho truy cập bề mặt bảo vệ.

## Pending UI

Default/validation/loading/failed-current-password/throttled/success/error states, copy và CTA chờ D05 mockup; không suy diễn design.

## Acceptance criteria

### AC-CP-01 - Cooldown after successful change

- **Given** chủ trọ vừa đổi mật khẩu thành công
- **When** yêu cầu đổi lại trong vòng 5 phút
- **Then** hệ thống từ chối với thông báo rõ ràng
- **And** mật khẩu và session state không thay đổi.

### AC-CP-02 - Change after cooldown

- **Given** đã đủ 5 phút từ lần đổi mật khẩu thành công trước đó và current/new password hợp lệ
- **When** chủ trọ gửi yêu cầu đổi mật khẩu
- **Then** hệ thống xử lý đổi mật khẩu
- **And** revoke toàn bộ session/refresh grants rồi đưa chủ trọ về Sign In.

### AC-CP-03 - Failed-password throttle is independent

- **Given** chủ trọ nhập current password sai vượt failed-attempt threshold
- **When** gửi yêu cầu đổi mật khẩu
- **Then** failure throttle hiện hành được áp dụng độc lập với cooldown 5 phút
- **And** không thay đổi mật khẩu hoặc session state.
