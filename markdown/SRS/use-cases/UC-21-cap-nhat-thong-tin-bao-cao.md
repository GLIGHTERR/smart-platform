# UC-21: Cập nhật thông tin báo cáo

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.22.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-21

### Use Case Name

Cập nhật thông tin báo cáo

### Description

Cho phép người dùng cập nhật thông tin báo cáo

### Actor(s)

Registered Users

### Related Use Case

UC-19, UC-20

### Priority

1

### Trigger

Người dùng muốn cập nhật thông tin trong báo cáo sự cố của mình

### Precondition

- PRE-01. Người dùng đã đăng nhập vào SmartTrọ
- PRE-02. Người dùng đang có hợp đồng với 1 phòng trọ
- PRE-03. Người dùng đang có báo cáo chưa được hoàn thành và chưa hết hạn

### Post-condition

POS-01. Hệ thống lưu thông tin báo cáo sau cập nhật, thông báo cho người dùng đã cập nhật và gửi thông báo tới chủ trọ

### Basic Flow

1. Người dùng truy cập màn hình “Báo cáo” từ Trang chủ
1. Người dùng điều hướng sang tab “Sự cố”
1. Người dùng chọn mở 1 báo cáo chưa được hoàn thành và chưa hết hạn
1. Người dùng mở màn hình cập nhật báo cáo
1. Người dùng nhập thông tin cần cho báo cáo
1. Người dùng cập nhật báo cáo
1. Hệ thống lưu, thông báo báo cáo đã được cập nhật và gửi thông báo cho chủ trọ thành công

### Alternative Flow

N/A

### Exception Flow

1. Tại bước 7, nếu hệ thống có vấn đề về việc lưu báo cáo hay gửi thông báo cho chủ trọ
- EX-21.1. Hệ thống thông báo “Lỗi hệ thống”

### Business Rules

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
