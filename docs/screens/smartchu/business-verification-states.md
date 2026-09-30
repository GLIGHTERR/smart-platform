# SmartChủ — Business Verification UI States

## 1. Mục tiêu

Tài liệu này mô tả cách các bề mặt SmartChủ truyền đạt trạng thái xác minh kinh doanh. Đây không phải nguồn định nghĩa quyền; nguồn policy là [`../../11-smartchu-business-verification-policy.md`](../../11-smartchu-business-verification-policy.md).

## 2. Home state

| Trạng thái | Nội dung | CTA |
| --- | --- | --- |
| `NOT_SUBMITTED` | `Hoàn thiện hồ sơ kinh doanh để bắt đầu quản lý nhà trọ.` | `Hoàn thiện hồ sơ` |
| `PENDING` | `Hồ sơ kinh doanh đang được xét duyệt.` | `Xem hồ sơ` |
| `REJECTED` | `Hồ sơ kinh doanh cần được cập nhật.` + lý do ngắn gọn | `Cập nhật hồ sơ` |
| `APPROVED` | Không hiển thị cảnh báo xác minh | Không có |

- Không hiển thị giấy tờ hoặc dữ liệu nhạy cảm trên Home.
- Không dùng toast tạm thời làm nơi duy nhất thông báo trạng thái.
- Shortcut/module vẫn hiển thị; action bị giới hạn phải giải thích và dẫn tới hồ sơ kinh doanh.

## 3. Property List state

| Trạng thái | Nút `Tạo nhà trọ` |
| --- | --- |
| `APPROVED` | Enabled, mở UC-18 |
| Khác `APPROVED` | Không mở form; hiển thị block/empty-state và CTA xác minh |

Không dùng nút disabled không có giải thích. Nếu hiển thị disabled về mặt thị giác, phải có text/CTA cho biết bước cần làm tiếp theo.

## 4. Room và Contract state

- `Tạo phòng trọ` và `Tạo hợp đồng` áp dụng cùng pattern.
- Danh sách hiện có vẫn có thể đọc nếu authorization của bản ghi cho phép.
- Error từ backend `BUSINESS_VERIFICATION_REQUIRED` phải map về cùng message/CTA, không hiển thị nguyên error kỹ thuật.

## 5. Accessibility và responsive

- Trạng thái không được phân biệt chỉ bằng màu.
- CTA có label rõ và vùng chạm mobile phù hợp.
- Banner/card không đẩy hành động chính ra khỏi viewport ở màn hình nhỏ.
- Lý do từ chối dài phải truncate có chủ đích hoặc mở trang chi tiết; không làm vỡ layout Home.
