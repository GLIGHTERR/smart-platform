# UC-11: Ký hợp đồng điện tử

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-11

### Use Case Name

Ký hợp đồng điện tử

### Description

Cho phép người dùng ký hợp đồng điện tử

### Trigger

Người dùng muốn ký hợp đồng điện tử của mình

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-9, UC-10

### Precondition

PRE-01. Người dùng đang có hợp đồng điện tử chưa được ký

### Post-condition

POS-01. Hệ thống lưu thông tin ký hợp đồng và thông báo người dùng đã ký hợp đồng thành công

### Basic Flow

1. Người dùng truy cập màn hình “Hợp đồng”, tab “Chưa ký”
1. Người dùng chọn hợp đồng muốn ký và bấm nút “Ký hợp đồng”
1. Người dùng thực hiện ký hợp đồng và bấm nút “Lưu”
1. Hệ thống thông báo hợp đồng đã được ký thành công, nếu hợp đồng đã đủ cả 2 chữ ký của 2 bên thì sẽ được chuyển về trạng thái Đã hoàn thành, nếu không thì sẽ chuyển sang trạng thái Đã ký

### Alternative Flow

1. Tại bước 3, nếu người dùng muốn ký lại
- AL-11.1. Người dùng bấm nút “Ký lại”
- AL-11.2. Người dùng tiếp tục như bước 3 tại Basic Flow
1. Tại bước 3, nếu người dùng muốn hủy thay đổi đã thực hiện
- AL-11.3. Người dùng bấm nút “Hủy”
- AL-11.4. Màn hình trở về trang “Hợp đồng”, tab “Chưa ký”

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
