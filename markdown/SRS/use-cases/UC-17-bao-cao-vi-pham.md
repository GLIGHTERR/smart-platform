# UC-17: Báo cáo vi phạm

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.18.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-17

### Use Case Name

Báo cáo vi phạm

### Description

Cho phép người dùng báo cáo những vi phạm về tiêu chuẩn cộng đồng của nền tảng tới hệ thống

### Actor(s)

Registered Users

### Related Use Case

N/A

### Priority

1

### Trigger

Người dùng muốn báo cáo bài viết hoặc rating, bình luận sai phạm về tiêu chuẩn cộng đồng

### Precondition

PRE-01. Người dùng đã đăng nhập vào SmartTrọ

### Post-condition

- POS-01. Hệ thống lưu báo cáo vi phạm và gửi lên hệ thống
- POS-02. Hệ thống thông báo cho người dùng là đã tiếp nhận báo cáo

### Basic Flow

1. Người dùng truy cập vào danh sách phòng trọ
1. Người dùng truy cập vào 1 bài đăng phòng trọ nào đó
1. Người dùng report bài đăng
1. Hệ thống tiếp nhận report và lưu thông tin report vào DB
1. Hệ thống gửi thông tin report tới đội ngũ admin và thông báo cho người dùng đã tiếp nhận báo cáo

### Alternative Flow

1. Tại bước 3, nếu người dùng muốn report cả các rating, bình luận:
- AL-17.1. Người dùng tìm tới rating vi phạm mà mình muốn report
- AL-17.2. Người dùng report bài rating
- AL-17.3. Tiếp tục tại bước 4 của Basic Flow

### Exception Flow

1. Tại các bước, nếu có sự ngắt quãng do mất mạng hoặc server có vấn đề
- EX-17.1. Hệ thống thông báo cho người dùng “Lỗi hệ thống”

### Business Rules

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
