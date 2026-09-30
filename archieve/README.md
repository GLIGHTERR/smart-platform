# Smart Platform — Archieve

Thư mục được đặt tên `archieve/` theo quy ước hiện tại của repository. Đây **không phải điểm vào mặc định** cho PM, Dev hoặc QA; tài liệu triển khai hiện hành nằm tại [`../docs/`](../docs/README.md).

## Phân khu

| Thư mục | Mục đích | Có dùng để triển khai trực tiếp? |
| --- | --- | --- |
| [`legacy-source/`](legacy-source/) | File DOCX, XLSX, PNG và PUML gốc/cũ, chia theo loại tài liệu và SmartTrọ/SmartChủ/SmartAdmin/Shared. | Không, chỉ dùng truy vết lịch sử hoặc chạy converter. |
| [`source-derived/`](source-derived/) | Bản Markdown chuyển đổi nguyên trạng đã được thay thế bởi living specification cùng UC. | Không, chỉ dùng đối chiếu nguồn. |
| [`supplemental/`](supplemental/) | Tài liệu hỗ trợ chưa thuộc các nhóm BRD/FRS/SRS/Requirement List/User Stories/WBS. | Chỉ khi README/tài liệu chuẩn trong `docs/` liên kết rõ. |

## Lưu ý về `Shared`

BRD, WBS, kiến trúc và một số workbook quản lý áp dụng cho toàn Smart Platform. Chúng được đặt trong `Shared` để giữ tính duy nhất; không sao chép cùng một file vào ba ứng dụng.

## Lưu ý xung đột UC SmartTrọ

Hai draft `UC-06-create-digital-signature.md` và `UC-07-update-digital-signature.md` được sinh từ Activity Diagram nhưng trùng mã với hai bảng chi tiết khác trong SRS nguồn. Chúng được giữ tại `supplemental/Draft_Use_Cases/SmartTro/` và không phải requirement triển khai cho đến khi PO/BA chốt lại mã UC.
