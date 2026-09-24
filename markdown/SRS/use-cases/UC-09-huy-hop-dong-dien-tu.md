# UC-9: Hủy hợp đồng điện tử

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.10.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-9

### Use Case Name

Hủy hợp đồng điện tử

### Description

Cho phép người dùng hủy hợp đồng điện tử

### Actor(s)

Registered Users

### Related Use Case

UC-7, UC-8

### Priority

1

### Trigger

Người dùng muốn huỷ hợp đồng thuê trọ

### Precondition

PRE-01. Người dùng đang có hợp đồng điện tử đang diễn ra

### Post-condition

POS-01. Hệ thống lưu thông tin hủy hợp đồng và thông báo người dùng đã hủy hợp đồng thành công

### Basic Flow

1. Màn hình hiển thị trang “Hợp đồng điện tử của tôi”
1. Người dùng bấm nút “Hủy hợp đồng”
1. Hệ thống hiển thị pop-up confirm
1. Người dùng bấm nút “Xác nhận”
1. Hệ thống gửi yêu cầu hủy hợp đồng tới chủ nhà trọ
1. Nếu chủ nhà đồng ý, hệ thống sẽ lưu thông tin hủy hợp đồng và gửi thông báo tới người dùng,

### Alternative Flow

N/A

### Exception Flow

N/A

### Business Rules

BR-01. Sau khi hủy hợp đồng, người dùng cần đợi tối thiểu 1h trước khi ký 1 hợp đồng khác

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
