# Smart Platform — Tài liệu hiện hành

`docs/` là **điểm vào duy nhất cho tài liệu Markdown hiện hành**. Không tạo lại thư mục `markdown/` và không đặt tài liệu triển khai ở ngoài cây này.

## Cách tìm tài liệu

| Loại tài liệu | SmartTrọ | SmartChủ | SmartAdmin | Shared |
| --- | --- | --- | --- | --- |
| FRS | [`FRS/SmartTro/`](FRS/SmartTro/) | [`FRS/SmartChu/`](FRS/SmartChu/) | [`FRS/SmartAdmin/`](FRS/SmartAdmin/) — chưa có bản hiện hành | — |
| Requirement List | [`Requirement_List/SmartTro/`](Requirement_List/SmartTro/) | [`Requirement_List/SmartChu/`](Requirement_List/SmartChu/) | [`Requirement_List/SmartAdmin/`](Requirement_List/SmartAdmin/) — chưa có bản hiện hành | — |
| SRS / Use Case | [`SRS/SmartTro/`](SRS/SmartTro/) | [`SRS/SmartChu/`](SRS/SmartChu/) | [`SRS/SmartAdmin/`](SRS/SmartAdmin/) | — |
| User Stories | [`User_Stories/SmartTro/`](User_Stories/SmartTro/) | [`User_Stories/SmartChu/`](User_Stories/SmartChu/) | [`User_Stories/SmartAdmin/`](User_Stories/SmartAdmin/) — chưa có bản hiện hành | — |

Các loại nguồn cũ chưa có bản Markdown chuẩn như BRD, WBS, Questions và Workflow Management được lưu trong [`../archieve/legacy-source/`](../archieve/legacy-source/), không nhân bản sang `docs/` khi chưa chuyển đổi.

## Quy tắc nguồn chuẩn

1. Mỗi tài liệu hiện hành chỉ có một đường dẫn chuẩn trong `docs/`.
2. Với Use Case đã được PO cập nhật/phê duyệt, file living specification là tài liệu chuẩn; bản chuyển đổi nguyên trạng tương ứng được giữ ở `archieve/source-derived/` chỉ để đối chiếu lịch sử.
3. Với Use Case chưa có living specification, file chuyển đổi từ SRS nguồn trong `docs/SRS/<Sản phẩm>/use-cases/` là tài liệu chuẩn tạm thời.
4. File DOCX/XLSX/PNG/PUML nguồn cũ nằm trong `archieve/legacy-source/`; không dùng chúng để ghi đè quyết định mới đã được phê duyệt.
5. Tài liệu dùng chung toàn hệ thống được phân loại là `Shared`, tránh sao chép cùng nội dung vào cả ba ứng dụng.
6. Tài liệu hỗ trợ ngoài các loại nguồn cũ được lưu tại `archieve/supplemental/` và phải được chuyển vào đúng loại trong `docs/` khi được chuẩn hóa.

## Trạng thái chuyển đổi

| Nguồn | Bản Markdown chuẩn | Ngày đồng bộ | SHA-256 nguồn |
| --- | --- | --- | --- |
| `archieve/legacy-source/SRS/SmartTro/SRS (SmartTrọ).docx` | [`SRS/SmartTro/SRS.md`](SRS/SmartTro/SRS.md) và [`SRS/SmartTro/use-cases/`](SRS/SmartTro/use-cases/) | 2026-09-24 | `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34` |
| `archieve/legacy-source/FRS/SmartTro/FRS - SmartTrọ.docx` | [`FRS/SmartTro/FRS.md`](FRS/SmartTro/FRS.md) | 2026-09-16 | `782c1e18ef1dfb5934c0d22177ff45f89a0f3cc029642aa1f4255c30d55caaef` |
| `archieve/legacy-source/Requirement_List/SmartTro/Requirements List - SmartTrọ.xlsx` | [`Requirement_List/SmartTro/Requirements.md`](Requirement_List/SmartTro/Requirements.md) | 2026-09-23 | `8780e7a5b6b984c763f1c07926862cf7db6477f00730988aa00784c2b9ec4464` |
| `archieve/legacy-source/User_Stories/SmartTro/User Story - SmartTrọ.xlsx` | [`User_Stories/SmartTro/User-Stories.md`](User_Stories/SmartTro/User-Stories.md) | 2026-09-23 | `e446d2858803534707114c472306ad2cb125c4fd8b9704b1e317a0e683df412f` |
| `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` | [`SRS/SmartChu/SRS.md`](SRS/SmartChu/SRS.md) và [`SRS/SmartChu/use-cases/`](SRS/SmartChu/use-cases/) | 2026-09-30 | `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` |
| `archieve/legacy-source/FRS/SmartChu/FRS - SmartChủ.docx` | [`FRS/SmartChu/FRS.md`](FRS/SmartChu/FRS.md) | 2026-09-30 | `001b95f8980228b947f9ce6f588b3f0101868c3fb778141d174ea64a760181e0` |
| `archieve/legacy-source/Requirement_List/SmartChu/Requirements List - SmartChủ.xlsx` | [`Requirement_List/SmartChu/Requirements.md`](Requirement_List/SmartChu/Requirements.md) | 2026-09-30 | `04140d67de31bd603db35b2463e50ba42b1b7463032110e9bb3eea75158736c4` |
| `archieve/legacy-source/User_Stories/SmartChu/User Story - SmartChủ.xlsx` | [`User_Stories/SmartChu/User-Stories.md`](User_Stories/SmartChu/User-Stories.md) | 2026-09-30 | `868751605d855388a8d688e2c755d247c7b421ae5f884ab5b03f3864f7083ad2` |

## Quy tắc cho agent

- Bắt đầu từ file README của đúng loại tài liệu và đúng sản phẩm.
- Không lấy `archieve/` làm requirement triển khai nếu đã có tài liệu tương ứng trong `docs/`.
- Khi cập nhật nguồn DOCX/XLSX, chạy lại converter, kiểm tra diff và cập nhật bảng trạng thái này trong cùng PR.
- Khi đổi đường dẫn tài liệu, cập nhật link, script và hướng dẫn agent trong cùng commit.
