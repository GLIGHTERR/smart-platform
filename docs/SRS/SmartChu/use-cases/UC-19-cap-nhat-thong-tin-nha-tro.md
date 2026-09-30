# UC-19: Cập nhật thông tin nhà trọ

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-19

### Use Case Name

Cập nhật thông tin nhà trọ

### Description

Cho phép người dùng cập nhật thông tin nhà trọ của mình

### Trigger

Người dùng muốn cập nhật lại thông tin nhà trọ của mình cho chính xác với hiện trạng

### Priority

1

### Business Rules

- BR-01. Không được giảm số tầng khi số tầng còn phòng active > số tầng được update
- BR-02. Không được chuyển trạng thái toà nhà sang deactive khi còn phòng active

### Actor(s)

Registered Users

### Related Use Case

UC-18

### Precondition

PRE-01. Người dùng đã tạo nhà trọ trên SmartChủ

### Post-condition

- POS-01. Hệ thống thông báo người dùng đã cập nhật nhà trọ thành công
- POS-02. Hệ thống lưu thay đổi thông tin nhà trọ vào DB

### Basic Flow

1. Người dùng chọn nhà trọ mà mình muốn cập nhật
1. Người dùng bấm nút “Thông tin” để truy cập màn hình “Thông tin toà nhà”
1. Người dùng bấm nút “Cập nhật” để truy cập màn hình “Cập nhật toà nhà”
1. Người dùng nhập thông tin mà muốn cập nhật và bấm nút “Lưu”
1. Hệ thống validate thay đổi, thông báo người dùng cập nhật toà nhà thành công và lưu thông tin vào DB

### Alternative Flow

1. Tại bước 4, nếu người dùng muốn huỷ các thay đổi
- AL-19.1. Người dùng bấm nút “Huỷ”
- AL-19.2. Màn hình trở về trang “Thông tin toà nhà”

### Exception Flow

1. Tại bước 5, nếu người dùng giảm số tầng khi số tầng còn phòng active > số tầng được update
- EX-19.1. Hệ thống hiển thị modal thông báo lỗi “Không thể giảm số tầng. Các phòng còn đang hoạt động”. Khi tắt modal thì quay trở lại trang “Cập nhật toà nhà”
1. Tại bước 5, nếu người dùng chuyển trạng thái toà nhà thành deactive khi vẫn còn phòng active
- EX-19.2. Hệ thống hiển thị modal thông báo lỗi “Không thể tắt trạng thái hoạt động. Vẫn còn phòng đang hoạt động”. Khi tắt modal thì quay trở lại trang “Cập nhật toà nhà”

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
