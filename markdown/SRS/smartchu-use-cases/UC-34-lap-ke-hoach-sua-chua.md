# UC-34: Lập kế hoạch sửa chữa

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-34

### Use Case Name

Lập kế hoạch sửa chữa

### Description

Cho phép người dùng đặt lịch sửa chữa cho các sự cố đã được báo cáo

### Trigger

Người dùng muốn đặt lịch sửa chữa cho các sự cố do có thể hoàn thành sớm

### Priority

1

### Business Rules

- BR-01. Thời gian xử lý sự cố mặc định theo độ ưu tiên (Cao: 3 ngày, Vừa: 5 ngày, Thấp: 7 ngày)
- BR-02. Người dùng chỉ được chọn ngày cập nhật trong khoảng nhỏ hơn số ngày mặc định tính theo độ ưu tiên (Cao: < 3 ngày, Vừa: < 5 ngày, Thấp: < 7 ngày)

### Actor(s)

Registered Users

### Related Use Case

UC-32, UC-33

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ
- PRE-02. Người dùng đã tạo phòng trọ
- PRE-03. Người dùng đang có sự cố “Mới” (chưa xem, chưa đặt lịch sửa chữa và đang còn hạn)

### Post-condition

- POS-01. Hệ thống thông báo người dùng cập nhật lịch thành công
- POS-02. Hệ thống gửi thời gian sửa chữa cho người thuê

### Basic Flow

1. Người dùng bấm chọn 1 sự cố trên trang “Danh sách sự cố”, tab “Mới”
1. Hiển thị chi tiết về sự cố đó trên trang “Chi tiết sự cố”
1. Người dùng bấm nút “Lên lịch sửa chữa”
1. Hiển thị modal “Đặt lịch sửa chữa”
1. Người dùng thực hiện đặt lịch sửa chữa và bấm nút “Lưu”
1. Hệ thống lưu thời gian sửa chữa sự cố mới, trạng thái chuyển thành “Đã tiếp nhận”, thông báo người dùng cập nhật lịch thành công và gửi thời gian sửa chữa mới cho người thuê

### Alternative Flow

1. Tại bước 7, nếu người dùng không muốn cập nhật thời gian sửa chữa
- AL-34.1. Người dùng bấm nút “Huỷ”
- AL-34.2. Màn hình trở về trang “Chi tiết sự cố”

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
