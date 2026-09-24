# SmartTrọ Use Case Implementation Specifications

Thư mục này chứa **living implementation specification** theo từng Use Case để PM giao việc, Dev triển khai và QA kiểm thử trên cùng một baseline đã được PO chốt. Đây không phải bản convert nguyên trạng từ SRS DOCX.

Bản đối chiếu đầy đủ nội dung UC thực tế có trong SRS nguồn nằm tại [`markdown/SRS/use-cases/`](../../../markdown/SRS/use-cases/README.md). Baseline SRS và living spec phải được giữ tách biệt để vừa bảo toàn bằng chứng nguồn, vừa thể hiện được các quyết định PO/Figma/API phát sinh trong quá trình triển khai.

## Quy tắc

- Mỗi UC có một file riêng; không gộp nhiều UC vào một tài liệu quyết định tổng hợp.
- Khi bắt đầu chuẩn bị một UC, phải đọc file baseline tương ứng trong `markdown/SRS/use-cases/`, sau đó ghi rõ các điểm giữ nguyên, thay đổi hoặc chưa rõ trong living spec.
- Quyết định, câu hỏi mở, UI, validation, technical mapping, test scope và gate bàn giao phải nằm trong UC bị ảnh hưởng.
- Nếu một quyết định ảnh hưởng nhiều UC, ghi rõ liên kết giữa các UC và cập nhật từng tài liệu tương ứng; không dùng một “impact register” thay cho requirement của từng UC.
- PM phải hỏi PO ngay trong task/comment khi UC có conflict, deferred decision hoặc ambiguity chưa được giải quyết.
- Dev và QA chỉ dùng revision của đúng UC được giao; không suy diễn từ một flow auth khác.
- Không chờ tới khi coding một UC mới tạo bản chuyển đổi SRS. Toàn bộ baseline có sẵn phải được convert trước; living spec mới được mở dần theo tiến độ triển khai.

## Danh mục hiện tại

| Use Case | Tài liệu | Trạng thái |
| --- | --- | --- |
| UC-01 — Đăng ký bằng email | [`UC-01-sign-up.md`](UC-01-sign-up.md) | Approved; Ready cho FE mock/UI review |
| UC-02 — Đăng nhập bằng email và mật khẩu | [`UC-02-sign-in.md`](UC-02-sign-in.md) | Approved; Ready cho FE mock/UI review |
| UC-03 — Quên mật khẩu bằng Email OTP | [`UC-03-forgot-password.md`](UC-03-forgot-password.md) | Approved; Ready cho FE-first implementation |
| UC-06 — Tạo mới chữ ký điện tử | [`UC-06-create-digital-signature.md`](UC-06-create-digital-signature.md) | Draft từ Activity Diagram; chờ PO chốt nhóm `SIG-COMMON` và `SIG-CREATE` |
| UC-07 — Cập nhật chữ ký điện tử | [`UC-07-update-digital-signature.md`](UC-07-update-digital-signature.md) | Draft từ Activity Diagram; chờ PO chốt nhóm `SIG-COMMON` và `SIG-UPDATE` |

Các UC tiếp theo được bổ sung vào **thư mục living spec này** khi được chuẩn bị để triển khai. Việc đó không ảnh hưởng tới baseline SRS đã được chuyển đổi trước cho toàn bộ danh mục.

Với UC-01, UC-02 và UC-03, thứ tự triển khai là: FE mock → deploy preview/mobile build → PO review/approve → BE → map API → QA → UAT.
