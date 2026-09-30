# SmartChủ — Business Verification and Operational Access Policy

## 1. Metadata

| Thuộc tính | Giá trị |
| --- | --- |
| Phạm vi | SmartChủ, SmartAdmin và shared backend `smart-platform-services` |
| Trạng thái | **Approved** |
| Ngày PO chốt | 2026-09-30 |
| Nguồn lịch sử | `SRS/SRS (SmartChủ).docx`, `FRS/FRS - SmartChủ.docx`, `User_Stories/User Story - SmartChủ.xlsx` |
| Loại tài liệu | Cross-cutting business rule và implementation baseline |

## 2. Vấn đề được chuẩn hóa

Nguồn SmartChủ cũ đã có các nội dung sau:

- lưu giấy tờ khai báo kinh doanh và giấy tờ chứng minh quyền sở hữu/sử dụng nhà trọ;
- cho phép chủ trọ cập nhật thông tin kinh doanh và tải ảnh tài liệu;
- gửi yêu cầu sang SmartAdmin và yêu cầu người dùng chờ phê duyệt;
- mô tả việc hoàn thiện hồ sơ kinh doanh là cơ sở để sử dụng chức năng hợp đồng, quản lý nhà trọ và thanh toán.

Tuy nhiên, precondition của các UC tạo hợp đồng, nhà trọ và phòng trọ chưa ghi rõ trạng thái phê duyệt. Tài liệu này đóng gap đó và là nguồn hiện hành cho mọi UC SmartChủ bị ảnh hưởng.

## 3. Quyết định đã duyệt

| ID | Quyết định |
| --- | --- |
| `SMC-BV-D01` | Đăng ký/xác minh email chỉ tạo tài khoản SmartChủ; không đồng nghĩa tài khoản đã được phép kinh doanh cho thuê trọ. |
| `SMC-BV-D02` | Hồ sơ kinh doanh dùng bốn trạng thái MVP: `NOT_SUBMITTED`, `PENDING`, `APPROVED`, `REJECTED`. |
| `SMC-BV-D03` | Chỉ tài khoản có `businessVerificationStatus = APPROVED` mới được tạo hợp đồng, tạo nhà trọ và tạo phòng trọ. |
| `SMC-BV-D04` | MVP không cho tạo bản nháp hợp đồng/nhà/phòng trước khi hồ sơ được duyệt. |
| `SMC-BV-D05` | Home SmartChủ phải hiển thị trạng thái xác minh và CTA phù hợp khi tài khoản chưa `APPROVED`. |
| `SMC-BV-D06` | Danh sách nhà trọ là bề mặt UI chính để chặn hành động `Tạo nhà trọ`; không đặt quy tắc nguồn chỉ ở màn danh sách hợp đồng. |
| `SMC-BV-D07` | FE gating chỉ là UX. Backend phải kiểm tra lại trạng thái ở mọi API bị giới hạn và từ chối yêu cầu không hợp lệ. |
| `SMC-BV-D08` | SmartAdmin phải lưu quyết định duyệt/từ chối, người xử lý, thời điểm và lý do từ chối để truy vết. |

## 4. Trạng thái và chuyển trạng thái

| Trạng thái | Ý nghĩa | Hành động chính của chủ trọ |
| --- | --- | --- |
| `NOT_SUBMITTED` | Chưa gửi hồ sơ kinh doanh | Xem yêu cầu và gửi hồ sơ |
| `PENDING` | Hồ sơ đang chờ Admin xử lý | Xem trạng thái; chờ kết quả |
| `APPROVED` | Hồ sơ hiện hành đã được chấp thuận | Được sử dụng các chức năng vận hành thuộc phạm vi MVP |
| `REJECTED` | Hồ sơ bị từ chối | Xem lý do, sửa và gửi lại |

Luồng MVP:

```text
NOT_SUBMITTED → PENDING → APPROVED
                        ↘ REJECTED → PENDING
```

Không tự động chuyển sang `APPROVED` dựa trên việc người dùng đã tải file hoặc đã điền đủ trường.

## 5. Ma trận quyền MVP

| Hành động | NOT_SUBMITTED | PENDING | REJECTED | APPROVED |
| --- | --- | --- | --- | --- |
| Đăng nhập/đăng xuất | Có | Có | Có | Có |
| Xem/sửa hồ sơ cá nhân | Có | Có | Có | Có |
| Xem trạng thái hồ sơ kinh doanh | Có | Có | Có | Có |
| Gửi hồ sơ | Có | Không | Gửi lại | Không cần |
| Xem danh sách nhà/phòng/hợp đồng hiện có | Có | Có | Có | Có |
| Tạo nhà trọ | Không | Không | Không | Có |
| Tạo phòng trọ | Không | Không | Không | Có |
| Tạo hợp đồng điện tử | Không | Không | Không | Có |

Các quyền xem không được dùng để suy ra quyền tạo/sửa. Mỗi API ghi dữ liệu phải tự kiểm tra quyền của hành động đó.

## 6. Hành vi UI dùng chung

### 6.1 Home SmartChủ

- `NOT_SUBMITTED`: hiển thị CTA `Hoàn thiện hồ sơ kinh doanh`.
- `PENDING`: hiển thị thông báo `Hồ sơ kinh doanh đang được xét duyệt`.
- `REJECTED`: hiển thị lý do ngắn gọn và CTA `Cập nhật hồ sơ`.
- `APPROVED`: không hiển thị cảnh báo xác minh.

Các shortcut điều hướng vẫn được hiển thị để người dùng hiểu cấu trúc ứng dụng. Nếu người dùng chưa `APPROVED` chọn một hành động bị giới hạn, app phải giải thích nguyên nhân và điều hướng tới thông tin kinh doanh; không để thao tác im lặng hoặc báo lỗi kỹ thuật chung chung.

### 6.2 Danh sách nhà trọ

- Hiển thị danh sách nếu có dữ liệu được phép xem.
- Nút `Tạo nhà trọ` chỉ thực thi flow tạo khi trạng thái là `APPROVED`.
- Với trạng thái khác, hiển thị message theo trạng thái và CTA tới hồ sơ kinh doanh.

### 6.3 Danh sách phòng và hợp đồng

- Có thể hiển thị dữ liệu người dùng được phép xem.
- `Tạo phòng trọ` và `Tạo hợp đồng` áp dụng cùng gate `APPROVED`.
- Màn danh sách hợp đồng chỉ tham chiếu policy này; không phải nguồn định nghĩa policy.

## 7. Backend và API contract

- Trạng thái xác minh thuộc owner/business profile và được trả về trong profile/session bootstrap cần thiết cho UI.
- API bị giới hạn phải trả lỗi nghiệp vụ ổn định khi trạng thái khác `APPROVED`.
- Baseline error code: `BUSINESS_VERIFICATION_REQUIRED` với HTTP `403`.
- Response có thể trả `businessVerificationStatus`; chỉ trả `rejectionReason` cho chính chủ trọ và vai trò Admin được phép xem.
- Không nhận trạng thái do client gửi lên làm căn cứ cấp quyền.
- Tài liệu tải lên là private object; không dùng URL public cố định và không ghi nội dung giấy tờ vào application log.

## 8. Trách nhiệm SmartAdmin

1. Nhận đúng phiên bản hồ sơ đang `PENDING`.
2. Xem thông tin và tài liệu theo quyền Admin.
3. Chọn `Approve` hoặc `Reject`.
4. Khi Reject, bắt buộc nhập lý do đủ để chủ trọ sửa hồ sơ.
5. Lưu audit gồm Admin, hành động, thời điểm, request/version hồ sơ và lý do nếu có.
6. Gửi notification cho chủ trọ sau khi có quyết định.

## 9. QA baseline

- Không thể tạo nhà, phòng hoặc hợp đồng ở ba trạng thái chưa duyệt, kể cả gọi API trực tiếp.
- Sau khi Admin duyệt, cùng tài khoản có thể thực hiện các action mà không cần đăng ký lại.
- Reject hiển thị đúng lý do cho chủ trọ và cho phép đi tới flow sửa/gửi lại.
- Không lộ giấy tờ của chủ trọ A cho chủ trọ B.
- Refresh/relogin không làm mất hoặc tự thay đổi trạng thái.
- FE và BE phải xử lý cùng một error code, không phụ thuộc riêng vào trạng thái nút disabled.

## 10. Ngoài phạm vi quyết định này

- Danh sách giấy tờ pháp lý chi tiết theo từng loại hình kinh doanh.
- Quy trình thu hồi một hồ sơ đã `APPROVED` và ảnh hưởng tới dữ liệu đang vận hành.
- Cho phép tạo draft trước khi duyệt.
- Thời hạn hiệu lực/chu kỳ tái xác minh giấy tờ.

Các nội dung này cần quyết định riêng trước khi mở rộng ngoài MVP.
