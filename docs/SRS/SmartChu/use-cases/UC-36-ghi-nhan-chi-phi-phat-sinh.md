# UC-36: Ghi nhận chi phí phát sinh

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-36

### Use Case Name

Ghi nhận chi phí phát sinh

### Description

Cho phép người dùng ghi nhận chi phí phát sinh sau khi sửa chữa

### Trigger

Người dùng muốn ghi lại chi phí phát sinh sau khi sửa chữa sự cố

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-35, UC-27

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ
- PRE-02. Người dùng đã tạo phòng trọ
- PRE-04. Người dùng đang có sự cố “Đã hoàn thành” (đã xem, đã đặt lịch sửa chữa, còn hạn, tiến độ đạt 100%)

### Post-condition

- POS-01. Hệ thống hiển thị thông báo người dùng đã ghi nhận chi phí phát sinh thành công
- POS-02. Hệ thống lưu chi phí phát sinh vào chi tiết sự cố

### Basic Flow

1. Người dùng bấm chọn 1 sự cố trên trang “Danh sách sự cố”, tab “Đã hoàn thiện”
1. Hiển thị chi tiết về sự cố đó trên trang “Chi tiết sự cố”
1. Người dùng bấm nút “Ghi nhận chi phí”
1. Hiển thị modal “Ghi nhận chi phí”
1. Người dùng thực hiện ghi nhận chi phí phát sinh và bấm nút “Lưu”
1. Hệ thống lưu chi phí phát sinh vào chi tiết sự cố, thông báo người dùng đã cập nhật thành công chi phí phát sinh

### Alternative Flow

1. Tại bước 5, nếu người dùng muốn huỷ việc ghi nhận chi phí phát sinh
- AL-36.1. Người dùng bấm nút “Huỷ”
- AL-36.2. Màn hình trở về trang “Chi tiết sự cố”

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
