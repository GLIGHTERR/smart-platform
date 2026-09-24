# UC-12: Đánh giá và bình luận trong bài đăng về phòng trọ

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `SRS/SRS (SmartTrọ).docx`, mục `3.13.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Đặc tả use case

### Use Case ID

UC-12

### Use Case Name

Đánh giá và bình luận trong bài đăng về phòng trọ

### Description

Cho phép người dùng đánh giá và bình luận trong bài đăng về phòng trọ

### Actor(s)

Registered Users

### Related Use Case

UC-11

### Priority

1

### Trigger

Người dùng muốn đánh giá và bình luận về bài đăng phòng trọ

### Precondition

PRE-01. Người dùng đã đăng nhập vào app SmartTrọ

### Post-condition

POS-01. Hệ thống lưu đánh giá và bình luận của người dùng và người dùng cũng xem được đánh giá và bình luận của mình trên trang chi tiết phòng trọ

### Basic Flow

1. Màn hình hiển thị trang “Danh sách phòng”
1. Người dùng bấm chọn 1 phòng trọ
1. Màn hình hiển thị trang “Chi tiết phòng trọ”
1. Người dùng bấm chọn số sao để đánh giá
1. Hiển thị pop-up Đánh giá
1. Người dùng có thể viết bình luận và bấm nút “Gửi”
1. Hệ thống lưu thông tin đánh giá, hiển thị đánh giá trên màn hình chi tiết phòng trọ

### Alternative Flow

N/A

### Exception Flow

N/A

### Business Rules

BR-01. Đánh giá tối thiểu 0.5 sao

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
