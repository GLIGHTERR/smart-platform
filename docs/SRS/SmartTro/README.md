# SmartTrọ — SRS và Use Case chuẩn

Đây là điểm vào duy nhất cho SRS SmartTrọ.

- SRS tổng thể: [`SRS.md`](SRS.md)
- Danh mục và đặc tả từng UC: [`use-cases/`](use-cases/README.md)
- Requirement List: [`../../Requirement_List/SmartTro/Requirements.md`](../../Requirement_List/SmartTro/Requirements.md)
- User Stories: [`../../User_Stories/SmartTro/User-Stories.md`](../../User_Stories/SmartTro/User-Stories.md)
- FRS và mô tả màn hình: [`../../FRS/SmartTro/`](../../FRS/SmartTro/FRS.md)

## Quy tắc canonical

- UC-01, UC-02 và UC-03 dùng living specification đã được PO chốt trong `use-cases/`.
- Các UC còn lại dùng bản chuyển đổi SRS nguồn cho tới khi living specification tương ứng được tạo và thay thế trong chính thư mục đó.
- Không tạo thêm một lớp UC khác ở `docs/use-cases/` hoặc `markdown/`.
- Bản chuyển đổi nguyên trạng của UC-01 đến UC-03 đã được chuyển vào `archieve/source-derived/` để đối chiếu, không dùng để giao triển khai.

## Quyết định chuẩn hóa UC chữ ký điện tử

SRS nguồn có bất nhất giữa catalogue và các bảng đặc tả chi tiết. PO đã chốt giữ các UC có bảng đặc tả theo mã `UC-01` đến `UC-31`, sau đó đặt hai UC chữ ký điện tử ở cuối danh mục:

- `UC-32` — Tạo mới chữ ký điện tử.
- `UC-33` — Cập nhật chữ ký điện tử.

Hai tài liệu sinh từ Activity Diagram vẫn là Draft tại `archieve/supplemental/Draft_Use_Cases/SmartTro/` cho tới khi nội dung được duyệt. Chúng thuộc **cụm triển khai hợp đồng thuê trọ** cùng UC-07/UC-08/UC-09; số `32`/`33` không có nghĩa phải chờ triển khai xong UC-31.
