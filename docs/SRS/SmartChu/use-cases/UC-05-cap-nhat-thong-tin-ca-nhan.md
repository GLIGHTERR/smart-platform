# SmartChủ - UC-05 Cập nhật thông tin cá nhân

> **Trạng thái:** Draft living spec - quyết định PO round 3; chờ D05 mockup/state reference trước handoff implementation.
> **Thay thế:** baseline legacy, gồm rule phone immutable và cooldown profile 1 giờ.

## Phạm vi

Chủ trọ cập nhật personal profile của chính mình. Phase đầu không có authenticated account-email-change flow và không gồm business-profile/legal-document workflow.

## Field behavior

| Field | Phase-one behavior | Pending detail |
| --- | --- | --- |
| Display name | Required; editable | Format/length/uniqueness và UI state chờ PO/mockup. |
| Phone | Optional contact; editable; non-unique; không credential/identity | Format, masking, consent và API response chờ PO/mockup. |
| Verified email | Read-only | Đổi email account là UC riêng sau này: re-auth/current password, new-email OTP, uniqueness, session/audit behavior. |
| Avatar | Display/fallback only | Không có image picker/upload/update phase đầu vì S3 upload chưa sẵn sàng; future scope. |

## Rules and boundaries

- Không dùng cooldown chung 1 giờ cho personal profile. Rule legacy không giải quyết độc lập API abuse, business submission/resubmission hoặc legal consistency.
- Rate limits là ba concern tách biệt: API abuse/failure throttle; business submission/resubmission cooldown; legal snapshot/versioning.
- Khi UC-07 được submit, hệ thống tạo immutable/versioned verification snapshot của đúng legal fields + documents để Admin review. Personal profile có thể sửa độc lập và không làm thay đổi snapshot PENDING/APPROVED. Nếu legal-bound field đổi, tạo business draft/version mới và yêu cầu resubmit theo policy; không dựa vào profile cooldown.
- Full UC-06/07 và snapshot implementation không thuộc phase đầu; đây là decision/dependency record, không là implementation gate.
- OTP không xuất hiện trong personal-profile contract.

## Luồng

1. Chủ trọ mở UC-05 từ tab `Cá nhân`.
2. App hiển thị các personal-profile field được phép sửa.
3. Chủ trọ lưu thay đổi; app hiển thị outcome theo canonical mockup rồi về UC-04.
4. Nếu đổi email account được yêu cầu sau phase đầu, điều hướng sang UC riêng, không mở rộng UC-05 ngầm định.

## Acceptance direction

### AC-PP-01 - Personal profile update

- **Given** chủ trọ đã đăng nhập và nhập display name hợp lệ cùng phone contact tùy chọn
- **When** lưu UC-05
- **Then** personal profile được cập nhật
- **And** phone vẫn editable, non-unique, không là identity/credential.

### AC-PP-02 - Legal review isolation

- **Given** chủ trọ có hồ sơ pháp lý `PENDING` hoặc `APPROVED`
- **When** chủ trọ cập nhật UC-05
- **Then** snapshot legal đang review/đã review không thay đổi
- **And** không tạo submission business mới chỉ do personal-profile update.

### AC-PP-03 - Legal-field amendment

- **Given** legal-bound field của business profile cần đổi sau khi snapshot đã tồn tại
- **When** chủ trọ gửi thay đổi qua business process
- **Then** hệ thống tạo business draft/version mới cần resubmit
- **And** giữ snapshot trước đó để audit/review.
