# UC-31: Thống kê hoạt động

> **Loại tài liệu:** Baseline chuyển đổi nguyên trạng từ SRS SmartChủ lịch sử.
> **Nguồn:** `SRS/SRS (SmartChủ).docx` — SHA-256 `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` — chuyển đổi 2026-09-30.
> **Lưu ý:** Tài liệu này không tự động phản ánh quyết định PO mới nếu file DOCX nguồn chưa được sửa.

## Đặc tả nguồn

### Use Case ID

UC-31

### Use Case Name

Thống kê hoạt động

### Description

Cho phép người dùng thống kê hoạt động

### Trigger

Người dùng muốn thống kê các hoạt động của người thuê với nhà trọ cũng như phòng trọ của mình

### Priority

1

### Business Rules

BR-01. Filter cho key metrics cho phép người dùng đặt filter trong vòng 90 ngày (Khoảng cách từ start date tới end date)

### Actor(s)

Registered Users

### Related Use Case

N/A

### Precondition

PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ

### Post-condition

POS-01. Hệ thống hiển thị trang “Thống kê”, tab “Hoạt động” bao gồm các key metrics và charts về lượt báo cáo, đánh giá, lưu, lượt đặt lịch xem cũng như lượt xem

### Basic Flow

1. Người dùng bấm nút “Thống kê” trên “Trang chủ”
1. Hệ thống hiển thị trang “Thống kê”, mặc định hiển thị tab “Hoạt động”

### Alternative Flow

N/A

### Exception Flow

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây
