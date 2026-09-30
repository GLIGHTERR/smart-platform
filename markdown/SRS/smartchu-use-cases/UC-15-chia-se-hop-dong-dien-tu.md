# UC-15: Chia sẻ hợp đồng điện tử

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-15

### Use Case Name

Chia sẻ hợp đồng điện tử

### Description

Cho phép người dùng chia sẻ hợp đồng điện tử cho người thuê

### Trigger

Người dùng muốn người thuê ký hợp đồng

### Priority

1

### Business Rules

- BR-01. Người dùng chỉ được chia sẻ hợp đồng ở trạng thái Chưa ký (chưa được người dùng ký) hoặc Đã ký
- BR-02. Người dùng chỉ được chia sẻ 1 hợp đồng tới tối đa 2 người thuê

### Actor(s)

Registered Users

### Related Use Case

UC-10, UC-30

### Precondition

PRE-01. Người dùng đang có hợp đồng ở trạng thái Chưa ký hoặc Đã ký

### Post-condition

POS-01. Box chat của người dùng và người thuê hiển thị tin nhắn đường dẫn (đường link) dẫn tới hợp đồng điện tử

### Basic Flow

1. Người dùng chọn 1 hợp đồng trên trang “Hợp đồng”, tab “Chưa ký” hoặc “Đã ký”
1. Người dùng bấm nút “Chia sẻ”
1. Hệ thống hiển thị danh sách người thuê mà người dùng đã nhắn tin trước đây
1. Người dùng có thể chọn 1 người thuê trong danh sách đã kết nối hoặc tìm kiếm người thuê mới theo số điện thoại hoặc email và bấm nút “Gửi”
1. Màn hình hiển thị box chat của người dùng và người thuê hiển thị tin nhắn đường dẫn (đường link) dẫn tới hợp đồng điện tử

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
