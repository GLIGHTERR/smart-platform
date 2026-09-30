# UC-23: Cập nhật thông tin phòng trọ

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-23

### Use Case Name

Cập nhật thông tin phòng trọ

### Description

Cho phép người dùng cập nhật thông tin phòng trọ

### Trigger

Người dùng muốn cập nhật thông tin phòng trọ

### Priority

1

### Business Rules

- BR-01. Người dùng chỉ được cập nhật phòng trong nhà trọ sao cho số tầng có phòng active <= số tầng giới hạn trong nhà trọ
- BR-02. Người dùng không được đổi trạng thái phòng thành deactive khi phòng vẫn còn hạn hợp đồng cho thuê

### Actor(s)

Registered Users

### Related Use Case

UC-22

### Precondition

PRE-01. Người dùng đã tạo phòng trọ

### Post-condition

- POS-01. Hệ thống lưu thông tin cập nhật phòng trọ vào DB
- POS-02. Hệ thống thông báo người dùng cập nhật phòng trọ thành công

### Basic Flow

1. Người dùng chọn phòng trọ mà mình muốn cập nhật thông tin trên trang “Danh sách phòng”
1. Người dùng bấm nút “Sửa”
1. Hệ thống hiển thị trang “Cập nhật thông tin phòng trọ”
1. Người dùng nhập thông tin muốn cập nhật cho phòng trọ và bấm nút “Lưu”
1. Hệ thống validate input, lưu thay đổi vào DB và thông báo người dùng đã cập nhật thông tin phòng trọ thành công

### Alternative Flow

1. Tại bước 4, nếu người dùng muốn huỷ thay đổi
- AL-23.1. Người dùng bấm nút “Huỷ”
- AL-23.2. Màn hình trở về trang “Chi tiết phòng trọ”

### Exception Flow

1. Tại bước 5, nếu hệ thống phát hiện số tầng của phòng trọ mới cập nhật khiến nhà trọ có nhiều tầng hơn khai báo
- EX-23.1. Hệ thống thông báo lỗi “Lỗi cập nhật. Số tầng đang hoạt động vượt quá mức cho phép”
1. Tại bước 5, nếu hệ thống phát hiện phòng trọ phòng trọ chuyển trạng thái deactive khi đang có hợp đồng cho thuê
- EX-23.2. Hệ thống thông báo lỗi “Lỗi cập nhật. Phòng vẫn đang được thuê”

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
