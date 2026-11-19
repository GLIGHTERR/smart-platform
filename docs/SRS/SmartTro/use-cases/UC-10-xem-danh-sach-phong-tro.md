# UC-10: Xem danh sách phòng trọ

> Loại tài liệu: **SRS baseline chuyển đổi nguyên trạng**; không tự động đồng nghĩa với requirement đã được PO phê duyệt để triển khai.
> Nguồn: `archieve/legacy-source/SRS/SmartTro/SRS (SmartTrọ).docx`, mục `3.11.`; SHA-256 `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.
> Đồng bộ: 2026-09-24.

## Làm rõ của PO ngày 2026-10-02

- `D.S.Trọ` từ Home điều hướng tới màn danh sách các phòng đang available thuộc nhiều nhà trọ.
- Mặc định, khi người dùng chưa chọn bộ lọc, màn hình hiển thị tất cả phòng available.
- Thứ tự mặc định: tên nhà trọ tăng dần; các phòng cùng nhà trọ sắp xếp theo giá tăng dần.
- Bộ lọc của người dùng được áp dụng tại màn danh sách phòng. Chi tiết UI và contract của bộ lọc được chốt khi triển khai UC-10, không thuộc scope Home `GLI-69`.

## Đặc tả use case

### Use Case ID

UC-10

### Use Case Name

Xem danh sách phòng trọ

### Description

Cho phép người dùng xem danh sách các phòng trọ trên hệ thống

### Actor(s)

Registered Users

### Related Use Case

UC-11

### Priority

1

### Trigger

Người dùng muốn xem danh sách phòng trọ đang active trên hệ thống

### Precondition

PRE-01. Người dùng đã đăng nhập vào app SmartTrọ

### Post-condition

POS-01. Người dùng xem được danh sách phòng trọ

### Basic Flow

1. Màn hình hiển thị Trang chủ
1. Người dùng bấm nút “D.S.Trọ”
1. Màn hình hiển thị trang “Danh sách phòng”

### Alternative Flow

N/A

### Exception Flow

N/A

### Business Rules

N/A

### Non-functional Requirement

NR-01. Thời gian phản hồi < 2 giây

## Activity Diagram

> DOCX nguồn có tiêu đề “Activity Diagram” cho mục này nhưng không có nội dung sơ đồ nhúng ngay trong phần tương ứng. Không tạo sơ đồ giả định trong baseline.
