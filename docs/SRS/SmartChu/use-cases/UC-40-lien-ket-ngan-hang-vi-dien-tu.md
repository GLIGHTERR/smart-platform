# UC-40: Liên kết ngân hàng/ví điện tử

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-40

### Use Case Name

Liên kết ngân hàng/ví điện tử

### Description

Cho phép người dùng liên kết ngân hàng/ví điện tử với SmartChủ

### Trigger

Người dùng muốn liên kết ngân hàng/ví điện tử với SmartChủ để thuận tiện cho việc thanh toán tiền trọ

### Priority

1

### Business Rules

BR-01. Nếu người dùng chưa liên kết phương thức thanh toán nào, người dùng phải thực hiện liên kết trước khi muốn sử dụng các chức năng khác trong trang “Thanh toán”

### Actor(s)

Registered Users

### Related Use Case

UC-44, UC-45, UC-46

### Precondition

PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ

### Post-condition

POS-01. Hệ thống thông báo người dùng liên kết ngân hàng/ví điện tử thành công

### Basic Flow

1. Người dùng bấm nút “Thanh toán” trên Trang chủ
1. Hiển thị trang “Thanh toán”
1. Người dùng bấm nút “Liên kết ngân hàng/ví điện tử”
1. Hiển thị màn hình “Liên kết ngân hàng/ví điện tử”
1. Người dùng thực hiện thêm  phương thức thanh toán, nhập thông tin cần thiết và bấm nút “Liên kết”
1. Hệ thống validate thông tin liên kết, lưu thông tin liên kết và hiển thị trang “Thanh toán”

### Alternative Flow

1. Tại bước 5, nếu người dùng muốn huỷ việc liên kết
- AL-40.1. Người dùng bấm nút “Huỷ”
- AL-40.2. Màn hình trở về trang “Thanh toán”

### Exception Flow

1. Tại bước 6, nếu thông tin liên kết không hợp lệ
- EX-40.1. Hệ thống hiển thị pop-up báo thông tin không hợp lệ, nếu đóng pop-up, màn hình trở về “Liên kết ngân hàng/ví điện tử”

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
