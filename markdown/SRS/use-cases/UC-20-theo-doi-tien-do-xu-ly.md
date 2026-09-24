# UC-20: Theo dõi tiến độ xử lý

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.21.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-20

### Use Case Name

Theo dõi tiến độ xử lý

### Description

Cho phép người dùng theo dõi tiến độ xử lý sự cố

### Actor(s)

Registered Users

### Related Use Case

UC-19, UC-21

### Priority

1

### Trigger

Người dùng muốn biết tiến độ xử lý sự cố của chủ trọ

### Precondition

- PRE-01. Người dùng đã đăng nhập vào SmartTrọ
- PRE-02. Người dùng đang có hợp đồng với 1 phòng trọ
- PRE-03. Người dùng đang có báo cáo sự cố chưa hoàn thành và chưa hết hạn

### Post-condition

POS-01. Người dùng thấy được tiết độ xử lý sự cố của chủ trọ

### Basic Flow

1. Người dùng truy cập màn hình “Báo cáo” từ Trang chủ
1. Người dùng điều hướng sang tab “Sự cố”
1. Người dùng chọn mở 1 báo cáo chưa hoàn thành và chưa hết hạn
1. Người dùng thấy được tiến độ xử lý của sự cố trong màn hình chi tiết báo cáo sự cố

### Alternative Flow

N/A

### Exception Flow

1. Nếu có sự cố trong lúc thao tác Basic Flow:
- EX-20.1. Hệ thống thông báo “Lỗi hệ thống”

### Business Rules

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
