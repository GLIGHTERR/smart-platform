# UC-35: Cập nhật tiến độ

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-35

### Use Case Name

Cập nhật tiến độ

### Description

Cho phép người dùng cập nhật tiến độ sửa chữa sự cố

### Trigger

Người dùng muốn cập nhật tiến độ sửa chữa của sự cố

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-33, UC-34

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ
- PRE-02. Người dùng đã tạo phòng trọ
- PRE-03. Người dùng đang có sự cố “Đã tiếp nhận” (đã xem, đã đặt lịch sửa chữa, còn hạn và tiến độ chưa đạt 100%)

### Post-condition

POS-01. Hệ thống thông báo cập nhật tiến độ sửa chữa và gửi thông báo cập nhật tới người thuê

### Basic Flow

1. Người dùng bấm chọn 1 sự cố trên trang “Danh sách sự cố”, tab “Đã tiếp nhận”
1. Hiển thị chi tiết về sự cố đó trên trang “Chi tiết sự cố”
1. Người dùng bấm nút “Cập nhật tiến độ”
1. Hiển thị modal “Cập nhật tiến độ”
1. Người dùng thực hiện cập nhật tiến độ và bấm nút “Lưu”
1. Hệ thống lưu tiến độ sửa chữa, thông báo người dùng cập nhật tiến độ thành công và gửi tiến độ sửa chữa mới cho người thuê

### Alternative Flow

1. Tại bước 5, nếu người dùng muốn huỷ việc cập nhật tiến độ
- AL-35.1. Người dùng bấm nút “Huỷ”
- AL-35.2. Hệ thống trở về trang “Chi tiết sự cố”
1. Tại bước 6, nếu tiến độ cập nhật là 100%
- AL-35.3. Hệ thống lưu tiến độ sửa chữa, chuyển trạng thái báo cáo sự cố thành “Đã hoàn thành”, thông báo người dùng cập nhật tiến độ thành công và gửi tiến độ sửa chữa cho người thuê

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
