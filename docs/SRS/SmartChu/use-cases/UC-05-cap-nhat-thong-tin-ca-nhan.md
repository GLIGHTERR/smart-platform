# SmartChủ - UC-05 Cập nhật thông tin cá nhân

> **Trạng thái:** Draft living spec - quyết định PO round 2; chờ D05 mockup/state reference trước handoff implementation.
> **Thay thế:** baseline legacy, gồm rule phone immutable và cooldown profile 1 giờ.

## Phạm vi

Chủ trọ cập nhật personal profile của chính mình. Phase đầu không có authenticated account-email-change flow và không gồm business-profile/legal-document workflow.

## Field behavior

| Field | Phase-one behavior | Pending detail |
| --- | --- | --- |
| Display name | Required; editable | Format/length/uniqueness và UI state chờ PO/mockup. |
| Phone | Optional contact; editable; non-unique; không credential/identity | Format, masking, consent và API response chờ PO/mockup. |
| Verified email | Read-only | Đổi email account là UC riêng sau này: re-auth/current password, new-email OTP, uniqueness, session/audit behavior. |
| Avatar | Chưa chốt update | SmartTrọ hiện display server avatar + fallback only; profile PATCH chưa update avatar. PO phải chọn copy current behavior hoặc chốt image-picker/upload/update. |

## Rules and boundaries

- Không dùng cooldown chung 1 giờ cho personal profile. Rule legacy không giải quyết độc lập API abuse, business submission/resubmission hoặc legal consistency.
- Rate limits là ba concern tách biệt: API abuse/failure throttle; business submission/resubmission cooldown; legal snapshot/versioning.
- Khi UC-07 được submit, kiến trúc đề xuất để PO review là tạo immutable/versioned verification snapshot của đúng legal fields + documents để Admin review. Personal profile có thể sửa độc lập. Nếu legal-bound field đổi, tạo business draft/version mới và yêu cầu resubmit theo policy; không dựa vào profile cooldown.
- Full UC-06/07 và snapshot implementation không thuộc phase đầu; đây là decision/dependency record, không là implementation gate.
- OTP không xuất hiện trong personal-profile contract.

## Luồng

1. Chủ trọ mở UC-05 từ tab `Cá nhân`.
2. App hiển thị các personal-profile field được phép sửa.
3. Chủ trọ lưu thay đổi; app hiển thị outcome theo canonical mockup rồi về UC-04.
4. Nếu đổi email account được yêu cầu sau phase đầu, điều hướng sang UC riêng, không mở rộng UC-05 ngầm định.

## Acceptance direction

- Phone nếu có có thể cập nhật và không được dùng làm identity/credential/unique key.
- Email không editable trong phase đầu.
- Không có rule successful-profile-update cooldown cho đến khi PO quyết định policy theo đúng concern.
- Các field legal/business không bị cập nhật qua UC-05.
