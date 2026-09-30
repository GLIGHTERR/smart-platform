# UC-39: Cập nhật kế hoạch bảo trì

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-39

### Use Case Name

Cập nhật kế hoạch bảo trì

### Description

Cho phép người dùng cập nhật lại kế hoạch bảo trì của nhà trọ

### Trigger

Người dùng muốn cập nhật lại lịch bảo trì nhà trọ nếu khung thời gian hiện tại đang bận

### Priority

1

### Business Rules

BR-01. Thời gian cập nhật phải trong vòng 30 ngày từ ngày tự động đặt lịch

### Actor(s)

Registered Users

### Related Use Case

UC-38

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ
- PRE-02. Người dùng đã tạo nhà trọ và các phòng trọ
- PRE-03. Người dùng đã cập nhật đầy đủ thông tin kinh doanh
- PRE-04. Người dùng đã đặt lịch bảo trì nhà trọ trước đây

### Post-condition

POS-01. Hệ thống thông báo cập nhật lịch bảo trì thành công

### Basic Flow

1. Người dùng truy cập trang “Lịch bảo trì”
1. Người dùng bấm chọn 1 ngày muốn xem chi tiết lịch
1. Hiển thị pop-up các kế hoạch bảo trì của ngày đã chọn
1. Người dùng bấm chọn 1 kế hoạch bảo trì để xem chi tiết
1. Hiển thị pop-up kế hoạch bảo trì
1. Người dùng chọn ngày thực hiện kế hoạch bảo trì mới và bấm nút “Lưu”
1. Hệ thống lưu thời gian mới cho kế hoạch bảo trì và thông báo người dùng cập nhật lịch bảo trì thành công

### Alternative Flow

1. Tại bước 6, nếu người dùng muốn huỷ việc cập nhật
- AL-39.1. Người dùng bấm nút “Huỷ”
- AL-39.2. Màn hình trở về pop-up kế hoạch bảo trì

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
