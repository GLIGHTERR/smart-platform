# SmartChủ - UC-04 Xem thông tin cá nhân

> **Trạng thái:** Draft living spec - quyết định PO round 2; chờ D05 mockup/state reference trước handoff implementation.
> **Thay thế:** baseline legacy trong SRS nguồn; source provenance vẫn ở archive.

## Mục tiêu và actor

Chủ trọ đã đăng nhập xem thông tin cá nhân của chính mình trong tab `Cá nhân` của Account. Đây là personal profile, tách khỏi business profile.

## Profile contract hiện hành

| Field | Hiển thị | Quy tắc |
| --- | --- | --- |
| Display name | Có | Personal-profile field bắt buộc theo D02 PO round 2. Validation chi tiết chờ PO/mockup. |
| Verified email | Có | Credential identity; read-only trong phase đầu. Không có authenticated account-email-change flow. |
| Phone | Có nếu đã cung cấp | Optional contact, editable, non-unique và không phải credential/identity. Masking/format chờ PO/mockup. |
| Avatar | Display/fallback pending | SmartTrọ hiện chỉ có server-avatar display + fallback; chưa có profile upload/update. PO phải chọn copy behavior này hoặc chốt image-picker/update requirement. |

Không hiển thị hoặc map `số phòng` hay `tên nhà trọ hiện đang thuê`: đó là renter data, không phù hợp actor Chủ trọ.

## Luồng

1. Chủ trọ mở Account, tab `Cá nhân`.
2. App lấy personal-profile của đúng account và hiển thị các field được phép.
3. Chủ trọ có thể điều hướng tới UC-05 hoặc UC-08.
4. Tab `Kinh doanh` là navigation placeholder cho future feature; không triển khai UC-06/07 form/status workflow trong phase đầu. Copy/layout chờ D05 mockup và PO review.

## Quy tắc

- OTP chỉ thuộc challenge Sign Up/Forgot Password; không là personal-profile field.
- Personal profile và business profile là hai domain/tab riêng.
- Full UC-06/07 không thuộc phase đầu; Home/Profile chỉ giữ minimal navigation/CTA dependency đã được PO chốt.
- Mọi state loading, empty, error, privacy/masking và copy hiển thị chờ canonical UI reference; không suy diễn từ SmartTrọ placeholder kỹ thuật.

## Acceptance direction

- Chỉ chủ account được xem profile của mình.
- Không có renter-only data trong response/UI/contract SmartChủ.
- Email read-only; phone, nếu có, không được dùng để đăng nhập hoặc kiểm tra uniqueness.
- Tab `Kinh doanh` điều hướng được tới future-feature placeholder có copy người dùng phù hợp sau PO review.
