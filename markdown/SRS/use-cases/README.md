# SmartTrọ SRS Use Case Baseline

> Chuyển đổi ngày 2026-09-24 từ `SRS/SRS (SmartTrọ).docx`.
> SHA-256 nguồn: `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34`.

Thư mục này là bản đối chiếu đầy đủ những gì **đang tồn tại trong SRS DOCX**. Nó khác với `docs/use-cases/smarttro/`, nơi chứa living spec đã được PO chốt và dùng để triển khai code.

## Phạm vi chuyển đổi

- Danh mục nguồn: **33 UC**.
- Bảng đặc tả chi tiết thực tế trong DOCX: **31 UC**.
- Mỗi bảng đặc tả được xuất thành một file riêng để agent có thể đọc ổn định và truy vết về đúng mục trong SRS.
- Nội dung không được tự suy diễn để lấp các UC thiếu hoặc sửa lệch số trong file nguồn.

## Các bất nhất cần PO/BA xử lý ở SRS nguồn

- Catalogue có `UC-6 — Tạo mới chữ ký điện tử` và `UC-7 — Cập nhật chữ ký điện tử`, nhưng phần phân tích chi tiết không có hai UC này.
- Từ chức năng Đổi mật khẩu tới Thống kê chi phí theo tháng, số UC trong catalogue và phần phân tích chi tiết lệch nhau hai đơn vị; không được tự động coi hai ID là tương đương.
- Mục chi tiết cuối có tiêu đề `UC-31: Báo cáo chi tiêu`, nhưng bảng bên trong ghi `Use Case ID = UC-32`; catalogue lại ghi `UC-33 — Báo cáo chi tiết`.
- Catalogue có 33 UC nhưng DOCX chỉ có 31 bảng đặc tả chi tiết. Các khoảng trống này phải được PO/BA sửa ở nguồn trước khi dùng làm requirement triển khai.

## Danh mục UC trong SRS nguồn

| STT | Mã UC | Tên UC |
| ---: | --- | --- |
| 1 | UC-1 | Đăng ký bằng email |
| 2 | UC-2 | Đăng nhập bằng email và mật khẩu |
| 3 | UC-3 | Quên mật khẩu |
| 4 | UC-4 | Xem thông tin cá nhân |
| 5 | UC-5 | Cập nhật thông tin cá nhân |
| 6 | UC-6 | Tạo mới chữ ký điện tử |
| 7 | UC-7 | Cập nhật chữ ký điện tử |
| 8 | UC-8 | Đổi mật khẩu |
| 9 | UC-9 | Xem hợp đồng điện tử |
| 10 | UC-10 | Ký hợp đồng điện tử |
| 11 | UC-11 | Hủy hợp đồng điện tử |
| 12 | UC-12 | Xem danh sách phòng trọ |
| 13 | UC-13 | Xem chi tiết phòng trọ |
| 14 | UC-14 | Đánh giá và bình luận trong bài đăng về phòng trọ |
| 15 | UC-15 | Lưu phòng trọ yêu thích |
| 16 | UC-16 | Đặt lịch xem trọ |
| 17 | UC-17 | Nhắn tin với chủ trọ |
| 18 | UC-18 | Viết đánh giá về nhà trọ |
| 19 | UC-19 | Báo cáo vi phạm |
| 20 | UC-20 | Xem các báo cáo đã tạo |
| 21 | UC-21 | Tạo báo cáo sự cố mới |
| 22 | UC-22 | Theo dõi tiến độ xử lý |
| 23 | UC-23 | Cập nhật thông tin báo cáo |
| 24 | UC-24 | Đánh giá sau xử lý |
| 25 | UC-25 | Liên kết ngân hàng/ví điện tử |
| 26 | UC-26 | Thanh toán thủ công |
| 27 | UC-27 | Thanh toán tự động |
| 28 | UC-28 | Nhận thông báo đến hạn |
| 29 | UC-29 | Đặt nhắc nhở thanh toán |
| 30 | UC-30 | Xem lịch sử thanh toán |
| 31 | UC-31 | Xuất hóa đơn điện tử |
| 32 | UC-32 | Thống kê chi phí theo tháng |
| 33 | UC-33 | Báo cáo chi tiết |

## Phân tích chi tiết thực tế trong SRS nguồn

| Mục SRS | Tiêu đề mục | ID trong bảng | Tên trong bảng | Baseline | Đối chiếu |
| --- | --- | --- | --- | --- | --- |
| 3.2. | UC-1: Đăng ký bằng email | UC-1 | Đăng ký bằng email | [`UC-01-dang-ky-bang-email.md`](UC-01-dang-ky-bang-email.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.3. | UC-2: Đăng nhập bằng email và mật khẩu | UC-2 | Đăng nhập bằng email và mật khẩu | [`UC-02-dang-nhap-bang-email-va-mat-khau.md`](UC-02-dang-nhap-bang-email-va-mat-khau.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.4. | UC-3: Quên mật khẩu | UC-3 | Quên mật khẩu | [`UC-03-quen-mat-khau.md`](UC-03-quen-mat-khau.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.5. | UC-4: Xem thông tin cá nhân | UC-4 | Xem thông tin cá nhân | [`UC-04-xem-thong-tin-ca-nhan.md`](UC-04-xem-thong-tin-ca-nhan.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.6. | UC-5: Cập nhật thông tin cá nhân | UC-5 | Cập nhật thông tin cá nhân | [`UC-05-cap-nhat-thong-tin-ca-nhan.md`](UC-05-cap-nhat-thong-tin-ca-nhan.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.7. | UC-6: Đổi mật khẩu | UC-6 | Đổi mật khẩu | [`UC-06-doi-mat-khau.md`](UC-06-doi-mat-khau.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.8. | UC-7: Xem hợp đồng điện tử | UC-7 | Xem hợp đồng điện tử | [`UC-07-xem-hop-dong-dien-tu.md`](UC-07-xem-hop-dong-dien-tu.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.9. | UC-8: Ký hợp đồng điện tử | UC-8 | Ký hợp đồng điện tử | [`UC-08-ky-hop-dong-dien-tu.md`](UC-08-ky-hop-dong-dien-tu.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.10. | UC-9: Hủy hợp đồng điện tử | UC-9 | Hủy hợp đồng điện tử | [`UC-09-huy-hop-dong-dien-tu.md`](UC-09-huy-hop-dong-dien-tu.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.11. | UC-10: Xem danh sách phòng trọ | UC-10 | Xem danh sách phòng trọ | [`UC-10-xem-danh-sach-phong-tro.md`](UC-10-xem-danh-sach-phong-tro.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.12. | UC-11: Xem chi tiết phòng trọ | UC-11 | Xem chi tiết phòng trọ | [`UC-11-xem-chi-tiet-phong-tro.md`](UC-11-xem-chi-tiet-phong-tro.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.13. | UC-12: Đánh giá và bình luận trong bài đăng về phòng trọ | UC-12 | Đánh giá và bình luận trong bài đăng về phòng trọ | [`UC-12-danh-gia-va-binh-luan-trong-bai-dang-ve-phong-tro.md`](UC-12-danh-gia-va-binh-luan-trong-bai-dang-ve-phong-tro.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.14. | UC-13: Lưu phòng trọ yêu thích | UC-13 | Lưu phòng trọ yêu thích | [`UC-13-luu-phong-tro-yeu-thich.md`](UC-13-luu-phong-tro-yeu-thich.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.15. | UC-14: Đặt lịch xem trọ | UC-14 | Đặt lịch xem trọ | [`UC-14-dat-lich-xem-tro.md`](UC-14-dat-lich-xem-tro.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.16. | UC-15: Nhắn tin với chủ trọ | UC-15 | Nhắn tin với chủ trọ | [`UC-15-nhan-tin-voi-chu-tro.md`](UC-15-nhan-tin-voi-chu-tro.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.17. | UC-16: Viết đánh giá về nhà trọ | UC-16 | Viết đánh giá về nhà trọ | [`UC-16-viet-danh-gia-ve-nha-tro.md`](UC-16-viet-danh-gia-ve-nha-tro.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.18. | UC-17: Báo cáo vi phạm | UC-17 | Báo cáo vi phạm | [`UC-17-bao-cao-vi-pham.md`](UC-17-bao-cao-vi-pham.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.19. | UC-18: Xem các báo cáo đã tạo | UC-18 | Xem các báo cáo đã tạo | [`UC-18-xem-cac-bao-cao-da-tao.md`](UC-18-xem-cac-bao-cao-da-tao.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.20. | UC-19: Tạo báo cáo sự cố | UC-19 | Tạo báo cáo sự cố | [`UC-19-tao-bao-cao-su-co.md`](UC-19-tao-bao-cao-su-co.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.21. | UC-20: Theo dõi tiến độ xử lý | UC-20 | Theo dõi tiến độ xử lý | [`UC-20-theo-doi-tien-do-xu-ly.md`](UC-20-theo-doi-tien-do-xu-ly.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.22. | UC-21: Cập nhật thông tin báo cáo | UC-21 | Cập nhật thông tin báo cáo | [`UC-21-cap-nhat-thong-tin-bao-cao.md`](UC-21-cap-nhat-thong-tin-bao-cao.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.23. | UC-22: Đánh giá sau xử lý | UC-22 | Đánh giá sau xử lý | [`UC-22-danh-gia-sau-xu-ly.md`](UC-22-danh-gia-sau-xu-ly.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.24. | UC-23: Liên kết ngân hàng/ví điện tử | UC-23 | Liên kết ngân hàng/ví điện tử | [`UC-23-lien-ket-ngan-hang-vi-dien-tu.md`](UC-23-lien-ket-ngan-hang-vi-dien-tu.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.25. | UC-24: Thanh toán thủ công | UC-24 | Thanh toán thủ công | [`UC-24-thanh-toan-thu-cong.md`](UC-24-thanh-toan-thu-cong.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.26. | UC-25: Thanh toán tự động | UC-25 | Thanh toán tự động | [`UC-25-thanh-toan-tu-dong.md`](UC-25-thanh-toan-tu-dong.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.27. | UC-26: Nhận thông báo đến hạn | UC-26 | Nhận thông báo đến hạn | [`UC-26-nhan-thong-bao-den-han.md`](UC-26-nhan-thong-bao-den-han.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.28. | UC-27: Đặt nhắc nhở thanh toán | UC-27 | Đặt nhắc nhở thanh toán | [`UC-27-dat-nhac-nho-thanh-toan.md`](UC-27-dat-nhac-nho-thanh-toan.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.29. | UC-28: Xem lịch sử thanh toán | UC-28 | Xem lịch sử thanh toán | [`UC-28-xem-lich-su-thanh-toan.md`](UC-28-xem-lich-su-thanh-toan.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.30. | UC-29: Xuất hóa đơn điện tử | UC-29 | Xuất hóa đơn điện tử | [`UC-29-xuat-hoa-don-dien-tu.md`](UC-29-xuat-hoa-don-dien-tu.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.31. | UC-30: Thống kê chi phí theo tháng | UC-30 | Thống kê chi phí theo tháng | [`UC-30-thong-ke-chi-phi-theo-thang.md`](UC-30-thong-ke-chi-phi-theo-thang.md) | Khớp giữa tiêu đề và bảng đặc tả. |
| 3.32. | UC-31: Báo cáo chi tiêu | UC-32 | Báo cáo chi tiêu | [`UC-31-bao-cao-chi-tieu.md`](UC-31-bao-cao-chi-tieu.md) | Tiêu đề `UC-31` nhưng bảng ghi `UC-32`. |

## Quan hệ với tài liệu triển khai

- UC-01, UC-02 và UC-03 đã có living spec được PO phê duyệt trong [`docs/use-cases/smarttro/`](../../../docs/use-cases/smarttro/README.md); giữ nguyên các file đó.
- Hai UC chữ ký điện tử không có bảng đặc tả trong DOCX nguồn, nhưng đã có Activity Diagram. Vì vậy chúng được soạn thành **living spec Draft bổ sung**, không được coi là nội dung trích xuất từ DOCX:
  - UC-6 — Tạo mới chữ ký điện tử: [`UC-06-create-digital-signature.md`](../../../docs/use-cases/smarttro/UC-06-create-digital-signature.md)
  - UC-7 — Cập nhật chữ ký điện tử: [`UC-07-update-digital-signature.md`](../../../docs/use-cases/smarttro/UC-07-update-digital-signature.md)
- Khi chuẩn bị UC mới, PM phải bắt đầu từ baseline tương ứng tại đây, sau đó ghi rõ quyết định PO, deviation, UI, API, test scope và gate triển khai trong living spec riêng.
- Không dùng việc “chưa tạo living spec” để kết luận SRS không có UC; baseline của toàn bộ SRS phải luôn được tạo trước và độc lập với tiến độ coding.
