# UC-10: Tạo hợp đồng điện tử

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Amendment / living implementation spec hiện hành

- [Living spec UC-10](../../../docs/use-cases/smartchu/UC-10-create-electronic-contract.md)
- Nội dung nguồn bên dưới được giữ nguyên để truy vết. Khi triển khai và kiểm thử, quyết định Approved trong living spec được ưu tiên nếu có khác biệt.
- [Chính sách xác minh kinh doanh SmartChủ](../../../docs/11-smartchu-business-verification-policy.md)

## Đặc tả nguồn

### Use Case ID

UC-10

### Use Case Name

Tạo hợp đồng điện tử

### Description

Cho phép người dùng tạo mới hợp đồng điện tử

### Trigger

Người dùng muốn tạo hợp đồng điện tử cho thủ tục cho thuê trọ

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-9, UC-11

### Precondition

- PRE-01. Người dùng đã đăng nhập
- PRE-02. Người dùng đã tạo nhà trọ và phòng trọ để cho thuê

### Post-condition

- POS-01. Hệ thống thông báo tạo hợp đồng điện tử thành công
- POS-02. Hệ thống lưu thông tin hợp đồng vào DB

### Basic Flow

1. Trên trang “Hợp đồng”, người dùng bấm nút “Tạo”
1. Hệ thống hiển thị màn hình “Tạo hợp đồng điện tử”
1. Người dùng chọn “Mẫu có sẵn”, nhập các thông tin cần thiết cho hợp đồng và bấm nút “Tiếp tục”
1. Hệ thống hiển thị màn hình “Thiết lập luồng ký”
1. Người dùng nhập thông tin người ký, setup thứ tự ký, vai trò người tham gia và bấm nút “Lưu”
1. Hệ thống lưu thông tin hợp đồng vừa tạo và thông báo cho người dùng đã tạo hợp đồng thành công

### Alternative Flow

1. Tại bước 5, nếu người dùng không muốn lưu hợp đồng điện tử vừa được tạo
- AL-10.1. Người dùng bấm nút “Hủy”
- AL-10.2. Màn hình trở về trang “Hợp đồng”, tab “Tất cả”

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
