# UC-07: Cập nhật thông tin kinh doanh

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Amendment / living implementation spec hiện hành

- [Living spec UC-07](../../../docs/use-cases/smartchu/UC-07-submit-business-verification.md)
- Nội dung nguồn bên dưới được giữ nguyên để truy vết. Khi triển khai và kiểm thử, quyết định Approved trong living spec được ưu tiên nếu có khác biệt.
- [Chính sách xác minh kinh doanh SmartChủ](../../../docs/11-smartchu-business-verification-policy.md)

## Đặc tả nguồn

### Use Case ID

UC-7

### Use Case Name

Cập nhật thông tin kinh doanh

### Description

Cho phép người dùng cập nhật thông tin kinh doanh của mình

### Trigger

Người dùng muốn cập nhật thông tin kinh doanh của tài khoản của mình

### Priority

1

### Business Rules

- BR-01. 2 lần cập nhật thông tin kế nhau phải cách nhau tối thiểu 1h
- BR-02. Mỗi tuần người dùng chỉ được cập nhật thông tin tối đa 3 lần

### Actor(s)

Registered Users

### Related Use Case

UC-6

### Precondition

PRE-01. Người dùng đã đăng nhập thành công

### Post-condition

- POS-01. Hệ thống thông báo người dùng chờ duyệt thông tin
- POS-02. Hệ thống lưu thông tin yêu cầu cập nhật thông tin kinh doanh
- POS-03. Hệ thống gửi thông báo yêu cầu cập nhật thông tin kinh doanh cho đội admin trên SmartAdmin

### Basic Flow

1. Màn hình hiển thị trang “Tài khoản”, tab “Kinh doanh”
1. Người dùng nhấn nút “Sửa”
1. Hệ thống hiển thị trang “Sửa thông tin kinh doanh”
1. Người dùng thay đổi các trường thông tin và bấm nút “Lưu”
1. Hệ thống lưu thông tin mới cập nhật, thông báo người dùng gửi yêu cầu cập nhật thông tin kinh doanh thành công và chuyển về trang “Tài khoản”, tab “Kinh doanh”

### Alternative Flow

1. Tại bước 4, nếu người dùng muốn huỷ các thay đổi
- AL-07.1. Người dùng bấm nút “Huỷ”
- AL-07.2. Màn hình trở lại trang “Tài khoản”, tab “Kinh doanh”

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
