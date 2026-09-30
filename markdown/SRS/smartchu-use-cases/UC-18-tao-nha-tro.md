# UC-18: Tạo nhà trọ

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Amendment / living implementation spec hiện hành

- [Living spec UC-18](../../../docs/use-cases/smartchu/UC-18-create-property.md)
- Nội dung nguồn bên dưới được giữ nguyên để truy vết. Khi triển khai và kiểm thử, quyết định Approved trong living spec được ưu tiên nếu có khác biệt.
- [Chính sách xác minh kinh doanh SmartChủ](../../../docs/11-smartchu-business-verification-policy.md)

## Đặc tả nguồn

### Use Case ID

UC-18

### Use Case Name

Tạo nhà trọ

### Description

Cho phép người dùng tạo nhà trọ trên SmartChủ

### Trigger

Người dùng muốn tạo nhà trọ của mình

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-16, UC-17, UC-19

### Precondition

PRE-01. Người dùng đã đăng nhập vào SmartChủ

### Post-condition

- POS-01. Hệ thống thông báo người dùng đã tạo nhà trọ thành công
- POS-02. Hệ thống lưu thông tin nhà trọ vào DB

### Basic Flow

1. Người dùng bấm nút “Thêm mới” trên trang “Toà nhà”
1. Người dùng điền thông tin cho toà nhà mới và bấm nút “Lưu”
1. Hệ thống thông báo người dùng đã tạo toà nhà thành công và lưu thông tin toà nhà mới tạo vào DB

### Alternative Flow

1. Tại bước 2, nếu người dùng muốn huỷ việc tạo toà nhà
- AL-18.1. Người dùng bấm nút “Huỷ”
- AL-18.2. Màn hình trở về trang “Toà nhà”

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
