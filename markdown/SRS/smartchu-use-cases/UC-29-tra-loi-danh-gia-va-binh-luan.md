# UC-29: Trả lời đánh giá và bình luận

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-29

### Use Case Name

Trả lời đánh giá và bình luận

### Description

Cho phép người dùng trả lời đánh giá và bình luận của người thuê

### Trigger

Người dùng muốn trả lời đánh giá và bình luận của người thuê

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-28

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ
- PRE-02. Người dùng đã tạo phòng trọ
- PRE-03. Người thuê đã đánh giá và bình luận về phòng trọ

### Post-condition

- POS-01. Hệ thống hiển thị câu trả lời của người dùng ngay bên dưới đánh giá và bình luận của người thuê
- POS-02. Hệ thống gửi thông báo cho người thuê rằng “Chủ trọ đã trả lời đánh giá và bình luận của bạn”

### Basic Flow

1. Người dùng bấm chọn toà nhà có phòng trọ muốn xem đánh giá và bình luận từ trang “Toà nhà”
1. Hệ thống hiển thị trang “Danh sách phòng”
1. Người dùng bấm chọn phòng trọ muốn xem đánh giá và bình luận
1. Hệ thống hiển thị trang “Chi tiết phòng trọ”
1. Người dùng kéo xuống để thấy phần Đánh giá và bình luận
1. Người dùng tìm tới đánh giá và bình luận mà mình muốn trả lời và bấm nút “Trả lời” ngay bên dưới đánh giá và bình luận đó
1. Hệ thống hiển thị modal “Trả lời”
1. Người dùng nhập nội dung muốn trả lời vầ bấm nút “Gửi”
1. Hệ thống lưu câu trả lời, hiển thị câu trả lời của người dùng ngay bên dưới đánh giá và bình luận của người thuê, đồng thời gửi thông báo tới cho người thuê về việc người dùng (là chủ trọ) đã trả lời đánh giá

### Alternative Flow

1. Tại bước 8, nếu người dùng muốn huỷ việc trả lời
- AL-29.1. Người dùng bấm nút “Huỷ”
- AL-29.2. Màn hình trở về trang “Chi tiết phòng trọ”

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
