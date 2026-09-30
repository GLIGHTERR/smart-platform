# UC-33: Chi tiết báo cáo sự cố

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-33

### Use Case Name

Chi tiết báo cáo sự cố

### Description

Cho phép người dùng xem chi tiết báo cáo sự cố

### Trigger

Người dùng muốn xem chi tiết báo cáo sự cố mà người thuê tạo

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-32, UC-34

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ
- PRE-02. Người dùng đã tạo phòng trọ
- PRE-03. Người dùng đã nhận báo cáo sự cố từ người thuê

### Post-condition

POS-01. Người dùng thấy được chi tiết báo cáo sự cố

### Basic Flow

1. Người dùng bấm nút “Sự cố” trên Trang Chủ
1. Hiển thị trang “Danh sách sự cố”
1. Người dùng bấm chọn 1 sự cố trên trang “Danh sách sự cố”
1. Hiển thị chi tiết về sự cố đó trên trang “Chi tiết sự cố”

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
