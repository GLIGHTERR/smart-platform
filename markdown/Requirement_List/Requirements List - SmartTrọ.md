# Requirements List SmartTrọ

> Bản Markdown được đồng bộ từ [`Requirements List - SmartTrọ.xlsx`](../../Requirement_List/Requirements%20List%20-%20SmartTro%CC%A3.xlsx) ngày 2026-09-16.
> SHA-256 nguồn: `bbe7698a13132ecf3a3bf1195fd2f9ee8255578aea5da7181d8589ec7a492321`.
> Công thức Excel được giữ ở dạng văn bản. File XLSX gốc vẫn là nguồn dữ liệu và định dạng chính thức.
> Các Change Request cũ có thể nhắc số điện thoại hoặc social login để mô tả lịch sử. Baseline triển khai hiện tại nằm trong tài liệu của đúng UC tại `docs/use-cases/smarttro/`.

## Requirements List

### SM001 — Đăng ký

| Trường | Giá trị |
| --- | --- |
| ID | SM001 |
| Platform | SmartTrọ |
| Requirements/ Functions | Đăng ký |
| Steps/ Process | Đăng ký bằng email và OTP |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | Doing |
| FE | Doing |
| App | Doing |
| Test | Doing |
| Deploy | New |
| Deploy date | 09/06/2025 |
| Code Version | 1 |

### SM002 — Đăng nhập

| Trường | Giá trị |
| --- | --- |
| ID | SM002 |
| Platform | SmartTrọ |
| Requirements/ Functions | Đăng nhập |
| Steps/ Process | Đăng nhập bằng email và mật khẩu |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | Doing |
| FE | Doing |
| App | Doing |
| Test | Doing |
| Deploy | New |
| Deploy date | 09/06/2025 |
| Code Version | 1 |

### SM003 — Đăng xuất

| Trường | Giá trị |
| --- | --- |
| ID | SM003 |
| Platform | SmartTrọ |
| Requirements/ Functions | Đăng xuất |
| Steps/ Process | Đăng xuất |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | Doing |
| FE | Doing |
| App | Doing |
| Test | Doing |
| Deploy | New |
| Deploy date | 09/06/2025 |
| Code Version | 1 |

### SM004 — Quên mật khẩu

| Trường | Giá trị |
| --- | --- |
| ID | SM004 |
| Platform | SmartTrọ |
| Requirements/ Functions | Quên mật khẩu |
| Steps/ Process | Quên mật khẩu |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 2 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | Doing |
| FE | Doing |
| App | Doing |
| Test | Doing |
| Deploy | New |
| Deploy date | 09/06/2025 |
| Code Version | 1 |

**Baseline nghiệp vụ đã duyệt ngày 2026-09-22**

- Identity recovery dùng email đã normalize; không dùng số điện thoại hoặc magic link trong MVP.
- UI gồm ba màn riêng: Email → OTP → Mật khẩu mới. Không chèn input OTP động vào màn Email.
- Request recovery luôn trả message trung tính `Nếu email tồn tại, mã xác thực đã được gửi.`; chỉ account đủ điều kiện mới nhận OTP.
- OTP gồm 6 chữ số, TTL 10 phút, resend cooldown 60 giây; OTP mới vô hiệu OTP cũ; tối đa 5 lần sai/challenge.
- Rate limit: tối đa 5 request/15 phút/email và 20 request/giờ/IP, kết hợp tín hiệu device.
- OTP hợp lệ chỉ cấp reset token one-time-use TTL 10 phút; reset token được bind với account/challenge/context phù hợp.
- Reset thành công phải revoke toàn bộ session, trở về Sign In với email prefill và không auto-login.
- Background/foreground khi process còn sống được giữ bước trong memory nếu còn hạn, nhưng phải xóa password fields khi resume.
- Force-close/process bị kill/app restart phải xóa toàn bộ recovery state, mở Sign In và bắt đầu lại bằng email + OTP mới.
- Thứ tự triển khai: FE + preview/mobile build → PO duyệt UI → BE → map API → QA system/regression → UAT.
- Baseline chi tiết: [`docs/use-cases/smarttro/UC-03-forgot-password.md`](../../docs/use-cases/smarttro/UC-03-forgot-password.md).

### SM005 — Đổi mật khẩu

| Trường | Giá trị |
| --- | --- |
| ID | SM005 |
| Platform | SmartTrọ |
| Requirements/ Functions | Đổi mật khẩu |
| Steps/ Process | Đổi mật khẩu |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 2 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | Doing |
| FE | Doing |
| App | Doing |
| Test | Doing |
| Deploy | New |
| Deploy date | 09/06/2025 |
| Code Version | 1 |

### SM006 — Xem thông tin cá nhân

| Trường | Giá trị |
| --- | --- |
| ID | SM006 |
| Platform | SmartTrọ |
| Requirements/ Functions | Xem thông tin cá nhân |
| Steps/ Process | Xem thông tin cá nhân |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 07/07/2025 |
| Code Version | 1 |

### SM007 — Cập nhật thông tin cá nhân

| Trường | Giá trị |
| --- | --- |
| ID | SM007 |
| Platform | SmartTrọ |
| Requirements/ Functions | Cập nhật thông tin cá nhân |
| Steps/ Process | Cập nhật thông tin cá nhân |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 07/07/2025 |
| Code Version | 1 |

### SM008 — Tạo chữ ký điện tử

| Trường | Giá trị |
| --- | --- |
| ID | SM008 |
| Platform | SmartTrọ |
| Requirements/ Functions | Tạo chữ ký điện tử |
| Steps/ Process | Tạo chữ ký điện tử |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | New |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 29/09/2025 |
| Code Version | 1 |

### SM009 — Cập nhật chữ ký điện tử

| Trường | Giá trị |
| --- | --- |
| ID | SM009 |
| Platform | SmartTrọ |
| Requirements/ Functions | Cập nhật chữ ký điện tử |
| Steps/ Process | Cập nhật chữ ký điện tử |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | New |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 29/09/2025 |
| Code Version | 1 |

### SM010 — Xem hợp đồng điện tử

| Trường | Giá trị |
| --- | --- |
| ID | SM010 |
| Platform | SmartTrọ |
| Requirements/ Functions | Xem hợp đồng điện tử |
| Steps/ Process | Xem hợp đồng điện tử |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | New |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 29/09/2025 |
| Code Version | 1 |

### SM011 — Ký hợp đồng điện tử

| Trường | Giá trị |
| --- | --- |
| ID | SM011 |
| Platform | SmartTrọ |
| Requirements/ Functions | Ký hợp đồng điện tử |
| Steps/ Process | Ký hợp đồng điện tử |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | New |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 29/09/2025 |
| Code Version | 1 |

### SM012 — Hủy hợp đồng điện tử

| Trường | Giá trị |
| --- | --- |
| ID | SM012 |
| Platform | SmartTrọ |
| Requirements/ Functions | Hủy hợp đồng điện tử |
| Steps/ Process | Hủy hợp đồng điện tử |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | New |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 29/09/2025 |
| Code Version | 1 |

### SM013 — Xem danh sách phòng trọ

| Trường | Giá trị |
| --- | --- |
| ID | SM013 |
| Platform | SmartTrọ |
| Requirements/ Functions | Xem danh sách phòng trọ |
| Steps/ Process | Xem danh sách phòng trọ |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 07/07/2025 |
| Code Version | 1 |

### SM014 — Xem thông tin chi tiết phòng trọ

| Trường | Giá trị |
| --- | --- |
| ID | SM014 |
| Platform | SmartTrọ |
| Requirements/ Functions | Xem thông tin chi tiết phòng trọ |
| Steps/ Process | Xem thông tin chi tiết phòng trọ |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 07/07/2025 |
| Code Version | 1 |

### SM015 — Đánh giá và bình luận bài đăng phòng trọ

| Trường | Giá trị |
| --- | --- |
| ID | SM015 |
| Platform | SmartTrọ |
| Requirements/ Functions | Đánh giá và bình luận bài đăng phòng trọ |
| Steps/ Process | Đánh giá và bình luận bài đăng phòng trọ |
| Requested By | BA |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 2 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 01/09/2025 |
| Code Version | 1 |

### SM016 — Lưu và theo dõi phòng trọ

| Trường | Giá trị |
| --- | --- |
| ID | SM016 |
| Platform | SmartTrọ |
| Requirements/ Functions | Lưu và theo dõi phòng trọ |
| Steps/ Process | Lưu và theo dõi phòng trọ |
| Requested By | BA |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 2 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 01/09/2025 |
| Code Version | 1 |

### SM017 — Đặt lịch xem trọ

| Trường | Giá trị |
| --- | --- |
| ID | SM017 |
| Platform | SmartTrọ |
| Requirements/ Functions | Đặt lịch xem trọ |
| Steps/ Process | Đặt lịch xem trọ |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 07/07/2025 |
| Code Version | 1 |

### SM018 — Nhắn tin với chủ trọ

| Trường | Giá trị |
| --- | --- |
| ID | SM018 |
| Platform | SmartTrọ |
| Requirements/ Functions | Nhắn tin với chủ trọ |
| Steps/ Process | Nhắn tin với chủ trọ |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 07/07/2025 |
| Code Version | 1 |

### SM019 — Viết đánh giá về nhà trọ

| Trường | Giá trị |
| --- | --- |
| ID | SM019 |
| Platform | SmartTrọ |
| Requirements/ Functions | Viết đánh giá về nhà trọ |
| Steps/ Process | Viết đánh giá về nhà trọ |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 2 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | New |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 01/09/2025 |
| Code Version | 1 |

### SM020 — Báo cáo vi phạm

| Trường | Giá trị |
| --- | --- |
| ID | SM020 |
| Platform | SmartTrọ |
| Requirements/ Functions | Báo cáo vi phạm |
| Steps/ Process | Báo cáo vi phạm |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 2 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | New |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 04/08/2025 |
| Code Version | 1 |

### SM021 — Theo dõi trạng thái báo cáo

| Trường | Giá trị |
| --- | --- |
| ID | SM021 |
| Platform | SmartTrọ |
| Requirements/ Functions | Theo dõi trạng thái báo cáo |
| Steps/ Process | Theo dõi trạng thái báo cáo |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 2 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | New |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 04/08/2025 |
| Code Version | 1 |

### SM022 — Tạo báo cáo sự cố mới

| Trường | Giá trị |
| --- | --- |
| ID | SM022 |
| Platform | SmartTrọ |
| Requirements/ Functions | Tạo báo cáo sự cố mới |
| Steps/ Process | Tạo báo cáo sự cố mới |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 2 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | New |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 04/08/2025 |
| Code Version | 1 |

### SM023 — Cập nhật thông tin báo cáo

| Trường | Giá trị |
| --- | --- |
| ID | SM023 |
| Platform | SmartTrọ |
| Requirements/ Functions | Cập nhật thông tin báo cáo |
| Steps/ Process | Cập nhật thông tin báo cáo |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 2 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | New |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 04/08/2025 |
| Code Version | 1 |

### SM024 — Theo dõi tiến độ xử lý

| Trường | Giá trị |
| --- | --- |
| ID | SM024 |
| Platform | SmartTrọ |
| Requirements/ Functions | Theo dõi tiến độ xử lý |
| Steps/ Process | Theo dõi tiến độ xử lý |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 3 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | New |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 04/08/2025 |
| Code Version | 1 |

### SM025 — Xem các báo cáo đã tạo

| Trường | Giá trị |
| --- | --- |
| ID | SM025 |
| Platform | SmartTrọ |
| Requirements/ Functions | Xem các báo cáo đã tạo |
| Steps/ Process | Xem các báo cáo đã tạo |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 2 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | New |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 04/08/2025 |
| Code Version | 1 |

### SM026 — Đánh giá sau xử lý

| Trường | Giá trị |
| --- | --- |
| ID | SM026 |
| Platform | SmartTrọ |
| Requirements/ Functions | Đánh giá sau xử lý |
| Steps/ Process | Đánh giá sau xử lý |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 3 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | New |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 04/08/2025 |
| Code Version | 1 |

### SM027 — Liên kết ngân hàng/ví điện tử

| Trường | Giá trị |
| --- | --- |
| ID | SM027 |
| Platform | SmartTrọ |
| Requirements/ Functions | Liên kết ngân hàng/ví điện tử |
| Steps/ Process | Liên kết ngân hàng/ví điện tử |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 15/09/2025 |
| Code Version | 1 |

### SM028 — Thanh toán thủ công

| Trường | Giá trị |
| --- | --- |
| ID | SM028 |
| Platform | SmartTrọ |
| Requirements/ Functions | Thanh toán thủ công |
| Steps/ Process | Thanh toán thủ công |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 15/09/2025 |
| Code Version | 1 |

### SM029 — Thanh toán tự động

| Trường | Giá trị |
| --- | --- |
| ID | SM029 |
| Platform | SmartTrọ |
| Requirements/ Functions | Thanh toán tự động |
| Steps/ Process | Thanh toán tự động |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 15/09/2025 |
| Code Version | 1 |

### SM030 — Nhận thông báo đến hạn

| Trường | Giá trị |
| --- | --- |
| ID | SM030 |
| Platform | SmartTrọ |
| Requirements/ Functions | Nhận thông báo đến hạn |
| Steps/ Process | Nhận thông báo đến hạn |
| Requested By | BA |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 2 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 29/09/2025 |
| Code Version | 1 |

### SM031 — Đặt nhắc nhở thanh toán

| Trường | Giá trị |
| --- | --- |
| ID | SM031 |
| Platform | SmartTrọ |
| Requirements/ Functions | Đặt nhắc nhở thanh toán |
| Steps/ Process | Đặt nhắc nhở thanh toán |
| Requested By | BA |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 2 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 29/09/2025 |
| Code Version | 1 |

### SM032 — Lịch sử thanh toán

| Trường | Giá trị |
| --- | --- |
| ID | SM032 |
| Platform | SmartTrọ |
| Requirements/ Functions | Lịch sử thanh toán |
| Steps/ Process | Lịch sử thanh toán |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 1 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | Done |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 15/09/2025 |
| Code Version | 1 |

### SM033 — Xuất hóa đơn điện tử

| Trường | Giá trị |
| --- | --- |
| ID | SM033 |
| Platform | SmartTrọ |
| Requirements/ Functions | Xuất hóa đơn điện tử |
| Steps/ Process | Xuất hóa đơn điện tử |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 2 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | New |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 13/10/2025 |
| Code Version | 1 |

### SM034 — Thống kê chi phí theo tháng

| Trường | Giá trị |
| --- | --- |
| ID | SM034 |
| Platform | SmartTrọ |
| Requirements/ Functions | Thống kê chi phí theo tháng |
| Steps/ Process | Thống kê chi phí theo tháng |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 3 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | New |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 13/10/2025 |
| Code Version | 1 |

### SM035 — Báo cáo chi tiêu

| Trường | Giá trị |
| --- | --- |
| ID | SM035 |
| Platform | SmartTrọ |
| Requirements/ Functions | Báo cáo chi tiêu |
| Steps/ Process | Báo cáo chi tiêu |
| Requested By | PO |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 29/04/2025 |
| Priority | 3 |
| Type | New |
| SRS (BA) | Done |
| Design UI/UX | New |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 13/10/2025 |
| Code Version | 1 |

### SM036 — Đăng ký

| Trường | Giá trị |
| --- | --- |
| ID | SM036 |
| Platform | SmartTrọ |
| Requirements/ Functions | Đăng ký |
| Steps/ Process | Đăng ký bằng liên kết tài khoản Facebook, Google, Apple |
| Requested By | BA |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 07/06/2025 |
| Priority | 3 |
| Type | Change |
| SRS (BA) | New |
| Design UI/UX | Done |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 27/10/2025 |
| Code Version | 2 |

### SM037 — Đăng nhập

| Trường | Giá trị |
| --- | --- |
| ID | SM037 |
| Platform | SmartTrọ |
| Requirements/ Functions | Đăng nhập |
| Steps/ Process | Đăng nhập bằng liên kết tài khoản Facebook, Google, Apple |
| Requested By | BA |
| Channel | Meeting |
| Requested Date (DD/MM/YYYY) | 07/06/2025 |
| Priority | 3 |
| Type | Change |
| SRS (BA) | New |
| Design UI/UX | Done |
| BE | New |
| FE | New |
| App | New |
| Test | New |
| Deploy | New |
| Deploy date | 27/10/2025 |
| Code Version | 2 |

## Change Requests

### 1 — 07/06/2025

| Trường | Giá trị |
| --- | --- |
| STT | 1 |
| Mã CR | CR01 |
| Ngày | 07/06/2025 |
| Thể hiện | App |
| Hệ thống | SmartTrọ |
| Tính năng | Đăng ký |
| Trước thay đổi | Chỉ đăng ký được bằng SĐT |
| Sau thay đổi | Cho phép đăng ký tài khoản bằng liên kết với tài khoản Facebook, Google, Apple |
| Ưu tiên | 3 |
| Ver SRS | 01/01/2025 |
| BA | New |
| UX | New |
| BE | New |
| FE | New |
| IoS | New |
| Android | New |
| QA verify | New |

### =MAX(A1:A2)+1 — 07/06/2025

| Trường | Giá trị |
| --- | --- |
| STT | =MAX(A1:A2)+1 |
| Mã CR | CR02 |
| Ngày | 07/06/2025 |
| Thể hiện | App |
| Hệ thống | SmartTrọ |
| Tính năng | Đăng nhập |
| Trước thay đổi | Chỉ đăng nhập được bằng SĐT và mật khẩu |
| Sau thay đổi | Cho phép đăng nhập bằng tài khoản liên kết Facebook, Google, Apple |
| Ưu tiên | 3 |
| Ver SRS | 01/01/2025 |
| BA | New |
| UX | New |
| BE | New |
| FE | New |
| IoS | New |
| Android | New |
| QA verify | New |

## CR Đăng ký bằng liên kết tài kh

| Cột 1 | Cột 2 | Cột 3 |
| --- | --- | --- |
| CR01 |  |  |
| STT | Thông tin cơ bản: | Chi tiết |
| 1 | Ngày Yêu cầu: | 07/06/2025 |
| =MAX($A$2:A3)+1 | Tên Người Yêu Cầu: | Nguyễn Tuấn Nghĩa |
| =MAX($A$2:A4)+1 | Dự Án/Tên Sản Phẩm: | SmartTrọ |
| =MAX($A$2:A5)+1 | Phiên Bản Hiện Tại: | 1.1.0 |
| =MAX($A$2:A6)+1 | Mô Tả Ngắn của Yêu Cầu Thay đổi: | Yêu cầu thêm chức năng cho phép người dùng đăng ký tài khoản mới bằng liên kết thông tin với tài khoản Facebook, Google, Apple. |
| =MAX($A$2:A7)+1 | Mục Đích và Lợi Ích: |  |
| =MAX($A$2:A8)+1 | Mục đích của Yêu cầu Thay đổi: | Giúp khách hàng đăng ký nhanh và hỗ trợ khách hàng auto fill thông tin tài khoản. |
| =MAX($A$2:A9)+1 | Lợi ích kỳ vọng sau khi thực hiện thay đổi: | Nhanh gọn, không cần tạo tài khoản và nhập OTP cầu kì. |
| =MAX($A$2:A10)+1 | Phạm Vi Thay đổi: |  |
| =MAX($A$2:A11)+1 | Phạm vi thay đổi (Xác định rõ ràng các phần của dự án/sản phẩm sẽ thay đổi): | Giao diện đăng ký, thông tin người dùng lưu trữ trong DB, logic xử lý đăng ký bằng liên kết tài khoản. |
| =MAX($A$2:A12)+1 | Mô tả Chi Tiết: |  |
| =MAX($A$2:A13)+1 | Mô tả chi tiết về thay đổi được đề xuất: | Thêm 3 nút "Đăng ký bằng tài khoản Facebook", "Đăng ký bằng tài khoản Google", "Đăng ký bằng tài khoản Apple" trên màn hình "Đăng ký". Sau khi người dùng bấm 1 trong 3 nút này, người dùng được chuyển sang loại giao diện tương ứng để xác nhận. |
| =MAX($A$2:A14)+1 | Ước Lượng Tài Nguyên và Thời Gian: |  |
| =MAX($A$2:A15)+1 | Ước lượng Số Giờ/Công để Thực Hiện: | 20h |
| =MAX($A$2:A16)+1 | Ước lượng Thời Gian Cần: | 27/10/2025 |
| =MAX($A$2:A17)+1 | Tác Động Đến Người Dùng và Hệ Thống: |  |
| =MAX($A$2:A18)+1 | Tác động dự kiến đối với người dùng cuối: | Người dùng có 1 cách khác để đăng ký tài khoản SmartTrọ |
| =MAX($A$2:A19)+1 | Tác động đối với hệ thống hiện tại: | Không ảnh hưởng luồng cũ |
| =MAX($A$2:A20)+1 | Kiểm Thử và Xác Nhận: |  |
| =MAX($A$2:A21)+1 | Phương pháp kiểm thử được đề xuất: | Hoạt động ổn định |
| =MAX($A$2:A22)+1 | Kế hoạch xác nhận sau khi triển khai: | Hoàn thành |
| =MAX($A$2:A23)+1 | Người Phê Duyệt: |  |
| =MAX($A$2:A24)+1 | Tên Người Phê Duyệt: | Nguyễn Văn A |
| =MAX($A$2:A25)+1 | Chức vụ: | PO |
| =MAX($A$2:A26)+1 | Ngày Phê Duyệt: | 07/06/2025 |
| =MAX($A$2:A27)+1 | Bước Tiếp Theo: |  |
| =MAX($A$2:A28)+1 | Bước tiếp theo sau khi Yêu cầu Thay đổi được phê duyệt: | Triển khai yêu cầu sau khi sản phẩm version 1.0.0 hoàn thiện |
| =MAX($A$2:A29)+1 | Ghi Chú và Ý Kiến Thêm: |  |
| =MAX($A$2:A30)+1 | Ghi chú hoặc ý kiến thêm về yêu cầu thay đổi (nếu có): |  |

## CR Đăng nhập bằng tài khoản liê

| Cột 1 | Cột 2 | Cột 3 |
| --- | --- | --- |
| CR02 |  |  |
| STT | Thông tin cơ bản: | Chi tiết |
| 1 | Ngày Yêu cầu: | 07/06/2025 |
| =MAX($A$2:A3)+1 | Tên Người Yêu Cầu: | Nguyễn Tuấn Nghĩa |
| =MAX($A$2:A4)+1 | Dự Án/Tên Sản Phẩm: | SmartTrọ |
| =MAX($A$2:A5)+1 | Phiên Bản Hiện Tại: | 1.1.0 |
| =MAX($A$2:A6)+1 | Mô Tả Ngắn của Yêu Cầu Thay đổi: | Yêu cầu thêm chức năng cho phép người dùng đăng nhập hệ thống bằng tài khoản Facebook, Google, Apple. |
| =MAX($A$2:A7)+1 | Mục Đích và Lợi Ích: |  |
| =MAX($A$2:A8)+1 | Mục đích của Yêu cầu Thay đổi: | Giúp khách hàng đã đăng ký bằng liên kết tài khoản không phải đăng nhập bằng SĐT và mật khẩu. |
| =MAX($A$2:A9)+1 | Lợi ích kỳ vọng sau khi thực hiện thay đổi: | Nhanh gọn, dễ hiểu do đã đăng ký tài khoản bằng cách liên kết trước đó. |
| =MAX($A$2:A10)+1 | Phạm Vi Thay đổi: |  |
| =MAX($A$2:A11)+1 | Phạm vi thay đổi (Xác định rõ ràng các phần của dự án/sản phẩm sẽ thay đổi): | Giao diện đăng nhập, logic xử lý đăng nhập bằng liên kết tài khoản. |
| =MAX($A$2:A12)+1 | Mô tả Chi Tiết: |  |
| =MAX($A$2:A13)+1 | Mô tả chi tiết về thay đổi được đề xuất: | Thêm 3 nút "Đăng nhập bằng tài khoản Facebook", "Đăng nhập bằng tài khoản Google", "Đăng nhập bằng tài khoản Apple" trên màn hình "Đăng nhập". Sau khi người dùng bấm 1 trong 3 nút này, người dùng được chuyển sang loại giao diện tương ứng để xác nhận. |
| =MAX($A$2:A14)+1 | Ước Lượng Tài Nguyên và Thời Gian: |  |
| =MAX($A$2:A15)+1 | Ước lượng Số Giờ/Công để Thực Hiện: | 14h |
| =MAX($A$2:A16)+1 | Ước lượng Thời Gian Cần: | 27/10/2025 |
| =MAX($A$2:A17)+1 | Tác Động Đến Người Dùng và Hệ Thống: |  |
| =MAX($A$2:A18)+1 | Tác động dự kiến đối với người dùng cuối: | Người dùng có 1 cách khác để đăng nhập tài khoản SmartTrọ |
| =MAX($A$2:A19)+1 | Tác động đối với hệ thống hiện tại: | Không ảnh hưởng luồng cũ |
| =MAX($A$2:A20)+1 | Kiểm Thử và Xác Nhận: |  |
| =MAX($A$2:A21)+1 | Phương pháp kiểm thử được đề xuất: | Hoạt động ổn định |
| =MAX($A$2:A22)+1 | Kế hoạch xác nhận sau khi triển khai: | Hoàn thành |
| =MAX($A$2:A23)+1 | Người Phê Duyệt: |  |
| =MAX($A$2:A24)+1 | Tên Người Phê Duyệt: | Nguyễn Văn A |
| =MAX($A$2:A25)+1 | Chức vụ: | PO |
| =MAX($A$2:A26)+1 | Ngày Phê Duyệt: | 07/06/2025 |
| =MAX($A$2:A27)+1 | Bước Tiếp Theo: |  |
| =MAX($A$2:A28)+1 | Bước tiếp theo sau khi Yêu cầu Thay đổi được phê duyệt: | Triển khai yêu cầu sau khi sản phẩm version 1.0.0 hoàn thiện |
| =MAX($A$2:A29)+1 | Ghi Chú và Ý Kiến Thêm: |  |
| =MAX($A$2:A30)+1 | Ghi chú hoặc ý kiến thêm về yêu cầu thay đổi (nếu có): |  |
