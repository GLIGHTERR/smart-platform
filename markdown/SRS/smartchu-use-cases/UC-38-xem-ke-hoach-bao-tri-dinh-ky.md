# UC-38: Xem kế hoạch bảo trì định kỳ

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-38

### Use Case Name

Xem kế hoạch bảo trì định kỳ

### Description

Cho phép người dùng xem kế hoạch bảo trì định kỳ của nhà trọ

### Trigger

Người dùng muốn xem kế hoạch bảo trì định kỳ của nhà trọ

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-39

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ
- PRE-02. Người dùng đã tạo nhà trọ và các phòng trọ
- PRE-03. Người dùng đã cập nhật đầy đủ thông tin kinh doanh

### Post-condition

POS-01. Hệ thống hiển thị kế hoạch bảo trì định kỳ dành cho nhà trọ

### Basic Flow

1. Người dùng truy cập trang “Thống kê”, tab “Sự cố”
1. Hiển thị dropdown các nhà trọ người dùng sở hữu
1. Người dùng bấm chọn nhà trọ muốn xem
1. Hiển thị thống kê về sự cố của nhà trọ
1. Người dùng bấm nút Xem lịch bảo trì
1. Hệ thống hiển thị lịch với thời gian dự tính bảo trì từng phòng trọ của nhà trọ

### Alternative Flow

1. Tại bước 6, nếu người dùng chưa đặt lịch bảo trì bao giờ
- AL-38.1. Hệ thống sử dụng AI và tính toán dựa trên tuổi của nhà trọ để đưa ra 1 kế hoạch bảo trì tiết kiệm mà an toàn
- AL-38.2. Lưu kế hoạch bảo trì vào DB
- AL-38.3. Hệ thống hiển thị lịch với thời gian dự tính bảo trì từng phòng trọ của nhà trọ

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 12 giây
