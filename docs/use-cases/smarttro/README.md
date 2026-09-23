# SmartTrọ Use Case Implementation Specifications

Thư mục này chứa tài liệu theo từng Use Case để PM giao việc, Dev triển khai và QA kiểm thử trên cùng một baseline.

## Quy tắc

- Mỗi UC có một file riêng; không gộp nhiều UC vào một tài liệu quyết định tổng hợp.
- Quyết định, câu hỏi mở, UI, validation, technical mapping, test scope và gate bàn giao phải nằm trong UC bị ảnh hưởng.
- Nếu một quyết định ảnh hưởng nhiều UC, ghi rõ liên kết giữa các UC và cập nhật từng tài liệu tương ứng; không dùng một “impact register” thay cho requirement của từng UC.
- PM phải hỏi PO ngay trong task/comment khi UC có conflict, deferred decision hoặc ambiguity chưa được giải quyết.
- Dev và QA chỉ dùng revision của đúng UC được giao; không suy diễn từ một flow auth khác.

## Danh mục hiện tại

| Use Case | Tài liệu | Trạng thái |
| --- | --- | --- |
| UC-01 — Đăng ký bằng email | [`UC-01-sign-up.md`](UC-01-sign-up.md) | Approved; Ready cho FE mock/UI review |
| UC-02 — Đăng nhập bằng email và mật khẩu | [`UC-02-sign-in.md`](UC-02-sign-in.md) | Approved; Ready cho FE mock/UI review |
| UC-03 — Quên mật khẩu bằng Email OTP | [`UC-03-forgot-password.md`](UC-03-forgot-password.md) | Approved; Ready cho FE-first implementation |

Các UC tiếp theo phải được bổ sung vào thư mục này khi được chuẩn bị để triển khai.

Với UC-01, UC-02 và UC-03, thứ tự triển khai là: FE mock → deploy preview/mobile build → PO review/approve → BE → map API → QA → UAT.
