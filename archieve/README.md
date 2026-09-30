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

## Lưu ý chuẩn hóa UC chữ ký điện tử SmartTrọ

Hai draft sinh từ Activity Diagram từng dùng mã `UC-06`/`UC-07`, trùng với Đổi mật khẩu và Xem hợp đồng điện tử trong phần đặc tả nguồn. PO đã chuẩn hóa chúng thành `UC-32-create-digital-signature.md` và `UC-33-update-digital-signature.md`, đặt cuối danh mục hiện hành. Chúng vẫn là Draft tại `supplemental/Draft_Use_Cases/SmartTro/` cho tới khi nội dung được duyệt, và được lập kế hoạch cùng cụm hợp đồng thuê trọ thay vì theo thứ tự số UC.
