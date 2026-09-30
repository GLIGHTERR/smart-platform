# Smart Platform Documentation

Kho tài liệu của Smart Platform được tổ chức theo hai vùng duy nhất:

- [`docs/`](docs/README.md): tài liệu Markdown **hiện hành**, là điểm vào chuẩn cho PM, Dev, QA và agent.
- [`archieve/`](archieve/README.md): tài liệu nguồn cũ, bản chuyển đổi đã được thay thế và tài liệu bổ trợ/lịch sử.

Không tạo lại thư mục `markdown/` và không đặt tài liệu hiện hành ở thư mục gốc.

## Bắt đầu đọc

1. Mở [`docs/README.md`](docs/README.md).
2. Chọn loại tài liệu: `FRS`, `Requirement_List`, `SRS` hoặc `User_Stories`.
3. Chọn sản phẩm: `SmartTro`, `SmartChu` hoặc `SmartAdmin`.
4. Chỉ dùng tài liệu trong `archieve/` khi cần truy vết nguồn hoặc lịch sử quyết định.

## Quy ước sản phẩm

| Tên | Phạm vi |
| --- | --- |
| SmartTrọ / `SmartTro` | Ứng dụng dành cho người thuê trọ. |
| SmartChủ / `SmartChu` | Ứng dụng dành cho chủ trọ. |
| SmartAdmin | Cổng quản trị hệ thống. |
| `Shared` | Tài liệu dùng chung, không thuộc riêng một sản phẩm. |

## Quy tắc cho agent

- Trước khi triển khai hoặc kiểm thử, phải đọc tài liệu hiện hành trong `docs/`.
- Không suy diễn một file trong `archieve/` là yêu cầu hiện hành nếu chưa có dẫn chiếu rõ ràng từ `docs/`.
- Khi thay đổi đường dẫn tài liệu, phải cập nhật liên kết và script converter trong cùng PR.
- Mỗi mục đích tài liệu chỉ có một bản hiện hành; bản bị thay thế phải chuyển vào `archieve/`.
