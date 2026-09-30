# UC-26: Phản hồi yêu cầu

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-26

### Use Case Name

Phản hồi yêu cầu

### Description

Cho phép người dùng phản hồi yêu cầu xem trọ của người thuê

### Trigger

Người dùng muốn phản hồi yêu cầu xem trọ cho người thuê

### Priority

1

### Business Rules

N/A

### Actor(s)

Registered Users

### Related Use Case

UC-25

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ
- PRE-02. Người dùng đang có phòng trọ
- PRE-03. Người dùng có yêu cầu xem phòng chưa duyệt

### Post-condition

- POS-01. Hệ thống hiển thị thông báo đã duyệt/từ chối yêu cầu
- POS-02. Người dùng nhận được tin nhắn từ hệ thống là đã duyệt/từ chối yêu cầu xem phòng
- POS-03. Người thuê nhận được tin nhắn từ hệ thống rằng yêu cầu xem phòng đã được duyệt/bị từ chối

### Basic Flow

1. Người dùng truy cập màn hình “Lịch xem” để xem danh sách các yêu cầu xem trọ chưa được duyệt
1. Người dùng tìm tới yêu cầu muốn xét duyệt và bấm nút “Duyệt” để duyệt hoặc nút “Từ chối” để từ chối yêu cầu xem trọ
1. Hệ thống validate, hiển thị thông báo duyệt/từ chối thành công và gửi tin nhắn tới người dùng và người thuê

### Alternative Flow

N/A

### Exception Flow

1. Tại bước 3, nếu người dùng duyệt 2 yêu cầu xem cùng 1 phòng và cùng 1 khung giờ
- EX-26.1. Hệ thống hiển thị thông báo lỗi “Đã có lịch xem trùng giờ”

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
