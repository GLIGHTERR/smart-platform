# UC-28: Xem đánh giá và bình luận

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-28

### Use Case Name

Xem đánh giá và bình luận

### Description

Cho phép người dùng xem đánh giá và bình luận về phòng trọ

### Trigger

Người dùng muốn xem đánh giá và bình luận về phòng trọ của mình

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-29

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ
- PRE-02. Người dùng đã tạo phòng trọ

### Post-condition

POS-01. Người dùng thấy được các đánh giá và bình luận của người thuê về phòng trọ của mình

### Basic Flow

1. Người dùng bấm chọn toà nhà có phòng trọ muốn xem đánh giá và bình luận từ trang “Toà nhà”
1. Hệ thống hiển thị trang “Danh sách phòng”
1. Người dùng bấm chọn phòng trọ muốn xem đánh giá và bình luận
1. Hệ thống hiển thị trang “Chi tiết phòng trọ”
1. Người dùng kéo xuống để thấy phần Đánh giá và bình luận

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
