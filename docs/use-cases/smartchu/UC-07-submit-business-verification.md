# SmartChủ — UC-07 Cập nhật và gửi duyệt thông tin kinh doanh

## 1. Metadata

| Thuộc tính | Giá trị |
| --- | --- |
| Use Case | `UC-07` — Cập nhật thông tin kinh doanh |
| Actor | Chủ trọ |
| Supporting actor | SmartAdmin |
| Trạng thái | **Approved** |
| Ngày PO chốt | 2026-09-30 |
| Policy liên quan | [`../../11-smartchu-business-verification-policy.md`](../../11-smartchu-business-verification-policy.md) |

## 2. Mục tiêu

Chủ trọ khai báo thông tin, tải tài liệu chứng minh theo yêu cầu và gửi một hồ sơ có thể truy vết để Admin phê duyệt trước khi sử dụng các chức năng vận hành cho thuê.

## 3. Dữ liệu nguồn tối thiểu

Baseline lịch sử đề cập mã số thuế/thông tin kinh doanh, giấy tờ khai báo kinh doanh và tài liệu chứng minh quyền sở hữu hoặc quyền sử dụng nhà trọ như sổ đỏ/bản sao công chứng. Danh sách field/file chi tiết phải được cấu hình trong contract của UC này; Dev không tự bổ sung loại giấy tờ pháp lý ngoài tài liệu đã duyệt.

## 4. Luồng chính

1. Chủ trọ mở form từ tab `Kinh doanh` hoặc CTA trên Home.
2. Chủ trọ nhập thông tin và chọn tài liệu hợp lệ.
3. FE validate định dạng/kích thước file trước khi upload.
4. Backend lưu file private và tạo phiên bản hồ sơ xét duyệt.
5. Hệ thống chuyển trạng thái sang `PENDING`.
6. SmartAdmin nhận yêu cầu xét duyệt.
7. Chủ trọ quay về màn trạng thái với thông báo chờ duyệt.

Nếu hồ sơ bị từ chối, chủ trọ sửa theo lý do và gửi lại; phiên bản mới là phiên bản chờ duyệt hiện hành.

## 5. Business Rules

- Hai lần cập nhật liên tiếp cách nhau tối thiểu 1 giờ và tối đa 3 lần mỗi tuần theo baseline SRS cũ, cho tới khi PO thay đổi rule này.
- Không chuyển `APPROVED` chỉ vì upload thành công.
- Trong `PENDING`, người dùng không gửi thêm một yêu cầu giống hệt.
- File phải được quét/validate loại MIME, giới hạn dung lượng và lưu private.
- Chỉ chủ hồ sơ và Admin có quyền phù hợp mới xem được file.
- Sau `REJECTED`, gửi lại tạo version mới nhưng vẫn giữ audit của version cũ.

## 6. Acceptance Criteria

### AC-SMC-BV-01 — Gửi hồ sơ thành công

- **Given** tài khoản đang `NOT_SUBMITTED` hoặc `REJECTED` và dữ liệu hợp lệ
- **When** chủ trọ xác nhận gửi hồ sơ
- **Then** hệ thống lưu đúng một version mới
- **And** trạng thái là `PENDING`
- **And** SmartAdmin nhận được yêu cầu xử lý.

### AC-SMC-BV-02 — Validation tài liệu

- **Given** file sai loại, vượt dung lượng hoặc upload không hoàn tất
- **When** người dùng gửi form
- **Then** hồ sơ không được chuyển sang `PENDING`
- **And** UI chỉ rõ trường/file cần sửa.

### AC-SMC-BV-03 — Gửi lại sau từ chối

- **Given** hồ sơ đang `REJECTED`
- **When** người dùng sửa và gửi lại hợp lệ
- **Then** hệ thống tạo version mới ở `PENDING`
- **And** giữ được quyết định và lý do của version cũ trong audit.

### AC-SMC-BV-04 — Giới hạn tần suất

- **Given** người dùng chưa thỏa thời gian chờ hoặc đã vượt số lần cập nhật tuần
- **When** cố gửi hồ sơ
- **Then** backend từ chối bằng error code nghiệp vụ ổn định
- **And** FE hiển thị thời điểm có thể thử lại nếu backend cung cấp.
