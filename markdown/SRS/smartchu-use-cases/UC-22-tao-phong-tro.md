# UC-22: Tạo phòng trọ

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Amendment / living implementation spec hiện hành

- [Living spec UC-22](../../../docs/use-cases/smartchu/UC-22-create-room.md)
- Nội dung nguồn bên dưới được giữ nguyên để truy vết. Khi triển khai và kiểm thử, quyết định Approved trong living spec được ưu tiên nếu có khác biệt.
- [Chính sách xác minh kinh doanh SmartChủ](../../../docs/11-smartchu-business-verification-policy.md)

## Đặc tả nguồn

### Use Case ID

UC-22

### Use Case Name

Tạo phòng trọ

### Description

Cho phép người dùng tạo phòng trọ mới trong nhà trọ của mình

### Trigger

Người dùng muốn tạo phòng trọ cho người thuê thuê phòng

### Priority

1

### Business Rules

BR-01. Người dùng chỉ được tạo phòng trong nhà trọ sao cho số tầng có phòng active <= số tầng giới hạn trong nhà trọ

### Actor(s)

Registered Users

### Related Use Case

UC-20, UC-21, UC-23

### Precondition

PRE-01. Người dùng đã tạo nhà trọ

### Post-condition

POS-01. Hệ thống thông báo người dùng đã tạo phòng trọ thành công

### Basic Flow

1. Người dùng bấm nút “Thêm phòng trọ” trên trang “Danh sách phòng” của nhà trọ muốn tạo phòng trọ
1. Hệ thống hiển thị trang “Thêm phòng trọ”
1. Người dùng nhập thông tin phòng trọ mới và bấm nút “Lưu”
1. Hệ thống validate input, thông báo người dùng tạo phòng trọ thành công

### Alternative Flow

1. Tại bước 3, nếu người dùng muốn huỷ việc tạo phòng trọ
- AL-22.1. Người dùng bấm nút “Huỷ”
- AL-22.2. Màn hình trở về trang “Danh sách phòng”

### Exception Flow

1. Tại bước 4, nếu hệ thống kiểm tra số tầng có phòng active vượt quá số tầng cho phép trong nhà trọ
- EX-22.1. Hệ thống hiển thị thông báo lỗi “Số tầng vượt quá số tầng cho phép. Hãy đổi số tầng”

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
