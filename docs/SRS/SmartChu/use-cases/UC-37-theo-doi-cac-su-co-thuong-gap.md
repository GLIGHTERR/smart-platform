# UC-37: Theo dõi các sự cố thường gặp

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `archieve/legacy-source/SRS/SmartChu/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-37

### Use Case Name

Theo dõi các sự cố thường gặp

### Description

Cho phép người dùng theo dõi các sự cố thường gặp nhằm đưa ra biện pháp sửa chữa hiệu quả hơn

### Trigger

Người dùng muốn theo dõi các sự cố thường gặp

### Priority

1

### Business Rules

BR-01.

### Actor(s)

Registered Users

### Related Use Case

UC-32

### Precondition

- PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ
- PRE-02. Người dùng đã tạo nhà trọ và các phòng trọ
- PRE-03. Người dùng và người thuê đã ký ít nhất 1 hợp đồng thuê trọ

### Post-condition

POS-01. Hệ thống hiển thị top sự cố nhà trọ hay gặp nhất

### Basic Flow

1. Người dùng truy cập trang “Thống kê” từ Trang chủ
1. Người dùng bấm chọn tab “Sự cố”
1. Hiển thị dropdown danh sách nhà trọ người dùng sở hữu
1. Người dùng chọn nhà trọ muốn xem top các sự cố hay gặp
1. Hệ thống hiển thị thống kê về sự cố (top 5 sự cố thường gặp, top 5 phòng hay gặp sự cố)

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
