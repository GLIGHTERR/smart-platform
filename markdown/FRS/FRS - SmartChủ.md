# FRS SmartChủ

> **Loại tài liệu:** Markdown mirror của tài liệu nguồn; không thay thế file DOCX để kiểm tra định dạng gốc.
> **Nguồn:** `FRS/FRS - SmartChủ.docx` — SHA-256 `c45b73e21d9ef7e090ec42b0620b5575792d36a93d21867f4b81947222af4181` — chuyển đổi 2026-09-30.

SmartChủ

Version: v1.0

Người biên soạn / Creator: Nguyễn Tuấn Nghĩa

Chức danh / Title: Business Analyst

Đơn vị / Department: MindX Technology School

Email: tuannghianguyen1509@gmail.com

Điện thoại/ Phone: 0969066700

Hà Nội, tháng 08 năm 2025

## LỊCH SỬ SỬA ĐỔI VÀ PHÊ DUYỆT

| Ngày | Tác giả | Phiên bản | Tham chiếu lịch sử thay đổi |
| --- | --- | --- | --- |
| 08/08/2025 | Nguyễn Tuấn Nghĩa | 1.0 | Khởi tạo |
| 10/08/2025 | Nguyễn Tuấn Nghĩa | 1.0 | Đặc tả, vẽ activity flow, mô tả màn hình UC-11: Ký hợp đồng điện tử<br>Xây dựng yêu cầu phi chức năng |
| 12/08/2025 | Nguyễn Tuấn Nghĩa | 1.0 | Đặc tả, vẽ activity flow, mô tả màn hình UC-15: Chia sẻ hợp đồng điện tử<br>Xây dựng yêu cầu phi chức năng |
| 14/08/2025 | Nguyễn Tuấn Nghĩa | 1.0 | Đặc tả, vẽ activity flow, mô tả màn hình UC-26: Phản hồi yêu cầu (xem trọ)<br>Xây dựng yêu cầu phi chức năng |
| 16/08/2025 | Nguyễn Tuấn Nghĩa | 1.0 | Đặc tả, vẽ activity flow, mô tả màn hình UC-35: Cập nhật tiến độ (sửa chữa sự cố)<br>Xây dựng yêu cầu phi chức năng |
| 18/08/2025 | Nguyễn Tuấn Nghĩa | 1.0 | Đặc tả, vẽ activity flow, mô tả màn hình UC-38: Xem kế hoạch bảo trì định kỳ<br>Xây dựng yêu cầu phi chức năng |

Mục lục

LỊCH SỬ SỬA ĐỔI VÀ PHÊ DUYỆT	2

- Thông tin chung	4
- Giới thiệu	4
- Mục đích	4
- Viết tắt	4
- Tham khảo  	4
- Tổng quan	5
- Bối cảnh và nguồn gốc dữ liệu	5
- Mô hình Functional Decomposition Diagram	6
- Tóm tắt chức năng chính	7
- Đối tượng người dùng	8
- Môi trường hoạt động của phần mềm	8
- Sơ đồ Use case tổng thể	9
- Sơ đồ Use case chi tiết	9
- Yêu cầu phi chức năng toàn hệ thống	17
- Phân tích các use case và luồng nghiệp vụ	22
- Danh sách các trường hợp sử dụng của hệ thống	22
- UC-11: Ký hợp đồng điện tử	22
- Đặc tả use case	23
- Activity Diagram	23
- Mô tả màn hình 	23
- UC-15: Chia sẻ hợp đồng điện tử	29
- Đặc tả use case	29
- Activity Diagram	30
- Mô tả màn hình 	30
- UC-26: Phản hồi yêu cầu (xem trọ)	31
- Đặc tả use-case	31
- Activity Diagram	32
- Mô tả màn hình	33
- UC-35: Cập nhật tiến độ (sửa chữa sự cố) 	34
- Đặc tả use-case	34
- Activity Diagram	35
- Mô tả màn hình	36
- UC-38: Xem kế hoạch bảo trì định kỳ 	37
- Đặc tả use-case	37
- Activity Diagram	38
- Mô tả màn hình	39
## Thông tin chung

## Giới thiệu

Hiện nay, số lượng người có nhu cầu thuê nhà trọ tăng lên hàng năm, tiêu biểu là các trường đại học và các khu công nghiệp, việc mở rộng ký túc xá không đủ nên phần lớn người thuê phải ở tại các nhà trọ trong khu vực. Tuy nhiên, việc tìm phòng trọ hiện nay rất khó khăn do tình hình quỹ đất hạn hẹp, giá nhà cao và uy tín của chủ nhà trọ không được đảm bảo. Người thuê cần một cộng đồng để cùng nhau đánh giá để tìm được nhà trọ uy tín và chất lượng trong tầm giá của mình, và chủ nhà trọ cũng cần một nơi để quảng bá nhà trọ của mình đến nhiều người thuê hơn.

Do đó việc xây dựng 1 nền tảng giúp cả người thuê và chủ trọ cảm thấy dễ dàng hơn trong việc thuê trọ là cần thiết để giúp chủ trọ quản lý nhà trọ tốt hơn, nâng cao chất lượng phục vụ, tối ưu hóa chiến dịch Marketing và tăng doanh thu. Đồng thời, giúp người thuê có 1 cộng đồng đủ uy tín, minh bạch để tin tưởng trong việc tìm, thuê trọ.

## Mục đích

Tài liệu này xác định rõ các yêu cầu chức năng và phi chức năng cho ứng dụng SmartChủ thuộc nền tảng Smart Platform.

Tài liệu sẽ đóng vai trò hướng dẫn chi tiết cho đội ngũ phát triển và các bên liên quan, đảm bảo hệ thống được xây dựng đáp ứng nhu cầu kinh doanh, tối ưu hóa quy trình làm việc và nâng cao trải nghiệm người dùng. Đồng thời, tài liệu cũng là cơ sở để đánh giá và kiểm thử hệ thống trong các giai đoạn triển khai.

## Viết tắt

| Từ viết tắt | Ý nghĩa |
| --- | --- |
| SRS | System Requirement Specification |
| OTP | One-Time Password |
| API | Application Programming Interface |
| UC | Use case |

## Tham khảo

| STT | Tham khảo | Chi tiết |
| --- | --- | --- |
| 1 | LalaHome | LalaHome Website |
| 2 | Batdongsan | Batdongsan Website |

## Tổng quan

## Bối cảnh và nguồn gốc dữ liệu

Ứng dụng SmartChủ sử dụng một loạt nguồn dữ liệu để hiển thị thông tin về khách hàng, hợp đồng, hồ sơ, bao gồm:

## Mô hình Functional Decomposition Diagram

## Hình 1: Sơ đồ phân rã chức năng của phần mềm

## Tóm tắt chức năng chính

## Đối tượng người dùng

Ứng dụng SmartChủ sẽ chỉ có một loại đối tượng người dùng: Chủ trọ

## Môi trường hoạt động của phần mềm

Ứng dụng SmartChủ hoạt động mượt mà trên điện thoại thông minh, yêu cầu như sau:

### Hệ điều hành được hỗ trợ

- iOS phiên bản tối thiểu từ phiên bản 14.0
- Android phiên bản tối thiểu từ phiên bản 8.0
## Sơ đồ Use case tổng thể

Hình 2: Use Case Diagram tổng thể

## Sơ đồ Use case chi tiết

Hình 2: Use Case Diagram tổng thể

Hình 3: Use Case Diagram đăng nhập/đăng ký

Hình 4: Use Case Diagram quản lý hồ sơ

Hình 5: Use Case Diagram quản lý hợp đồng điện tử

Hình 6: Use Case Diagram quản lý nhà trọ

Hình 7: Use Case Diagram tương tác với người thuê

Hình 8: Use Case Diagram quản lý sự cố

Hình 9: Use Case Diagram thanh toán trực tuyến

## Yêu cầu phi chức năng toàn hệ thống

Hình 2: Use Case Diagram tổng thể

| STT | Mã NFR | Nội dung |
| --- | --- | --- |
| Yêu cầu về hiệu suất | Yêu cầu về hiệu suất | Yêu cầu về hiệu suất |
|  | NFR-01 | Thời gian phản hồi |
| 1 | NFR-01.1 | Thời gian tải trang không quá 2 giây |
| 2 | NFR-01.2 | Thời gian tìm kiếm không quá 3 giây |
| 3 | NFR-01.3 | Thời gian xử lý thanh toán không quá 5 giây |
|  | NFR-02 | Khả năng mở rộng |
| 4 | NFR-02.1 | Hệ thống phải hỗ trợ tối thiểu 10,000 người dùng đồng thời |
| 5 | NFR-02.2 | Cơ sở dữ liệu phải lưu trữ thông tin của ít nhất 100,000 phòng trọ |
| 6 | NFR-02.3 | Hệ thống phải xử lý được tối thiểu 1,000 giao dịch thanh toán mỗi giờ |
| Yêu cầu về bảo mật | Yêu cầu về bảo mật | Yêu cầu về bảo mật |
|  | NFR-03 | Bảo mật dữ liệu |
| 7 | NFR-03.1 | Tuân thủ quy định về bảo vệ dữ liệu cá nhân |
| 8 | NFR-03.2 | Kiểm tra bảo mật định kỳ |
| 9 | NFR-03.3 | Mã hóa dữ liệu người dùng và thông tin thanh toán (Bcrypt, Hash) |
|  | NFR-04 | Xác thực và phân quyền (Authorization & Authentication) |
| 10 | NFR-04.1 | Phân quyền truy cập dựa trên vai trò người dùng |
| 11 | NFR-04.2 | Giới hạn số lần đăng nhập thất bại |
| 12 | NFR-04.3 | Hỗ trợ xác thực hai yếu tố (2FA - 2 factors authentication) |
| Yêu cầu về độ tin cậy | Yêu cầu về độ tin cậy | Yêu cầu về độ tin cậy |
|  | NFR-05 | Tính sẵn sàng |
| 13 | NFR-05.1 | Hệ thống phải hoạt động 24/7 với thời gian ngừng hoạt động không quá 0.1% |
| 14 | NFR-05.2 | Thời gian phục hồi sau sự cố không quá 2 giờ |
| 15 | NFR-05.3 | Sao lưu dữ liệu hàng ngày |
|  | NFR-06 | Khả năng chịu lỗi |
| 16 | NFR-06.1 | Hệ thống phải tiếp tục hoạt động khi có lỗi một phần |
| 17 | NFR-06.2 | Tự động phát hiện và báo lỗi |
| 18 | NFR-06.3 | Tự động khôi phục sau lỗi không nghiêm trọng |
| Yêu cầu về tính sử dụng | Yêu cầu về tính sử dụng | Yêu cầu về tính sử dụng |
|  | NFR-07 | Giao diện người dùng |
| 19 | NFR-07.1 | Thiết kế giao diện thân thiện với người dùng |
| Yêu cầu về tương thích | Yêu cầu về tương thích | Yêu cầu về tương thích |
|  | NFR-08 | Tương thích nền tảng |
| 20 | NFR-08.1 | Hỗ trợ iOS 14.0 trở lên và Android 8.0 trở lên |

## Phân tích các use case và luồng nghiệp vụ

## Danh sách các trường hợp sử dụng của hệ thống

| STT | Mã UC | Tên tính năng |
| --- | --- | --- |
| 1 | UC-11 | Ký hợp đồng điện tử |
| 2 | UC-15 | Chia sẻ hợp đồng điện tử |
| 3 | UC-26 | Phản hồi yêu cầu (Xem trọ) |
| 4 | UC-35 | Cập nhật tiến độ (sửa chữa sự cố) |
| 5 | UC-38 | Xem kế hoạch bảo trì định kỳ |

## UC-11: Ký hợp đồng điện tử

## Đặc tả use case

## Activity Diagram

## Mô tả màn hình

Hình 10: Hiển thị màn hình trước khi bấm nút “Ký hợp đồng”

Hình 11: Hiển thị màn hình sau khi ký hợp đồng xong

Hình 12: Modal hiển thị trên màn hình sau khi bấm nút “Ký hợp đồng”

## UC-15: Chia sẻ hợp đồng điện tử

## Đặc tả use case

## Activity Diagram

## Mô tả màn hình

Hình 13. Modal chia sẻ hợp đồng cho người thuê

## UC-26: Phản hồi yêu cầu (xem trọ)

## Đặc tả use-case

## Activity Diagram

## Mô tả màn hình

Hình 14. Màn hình danh sách yêu cầu xem trọ

## UC-35: Cập nhật tiến độ (sửa chữa sự cố)

## Đặc tả use-case

## Activity Diagram

## Mô tả màn hình

Hình 14. Màn hình chi tiết báo cáo và modal cập nhật tiến độ sửa chữa

## UC-38: Xem kế hoạch bảo trì định kỳ

## Đặc tả use-case

## Activity Diagram

## Mô tả màn hình

Hình 15. Màn hình lịch bảo trì khi đã được khởi tạo và chưa được khởi tạo

## Phụ lục bảng nguồn

> Phụ lục liệt kê toàn bộ bảng trong XML (bao gồm bảng lồng) để tránh bỏ sót nội dung khi converter DOCX chỉ thấy bảng cấp cao nhất.

### Bảng nguồn 1

| Ngày | Tác giả | Phiên bản | Tham chiếu lịch sử thay đổi |
| --- | --- | --- | --- |
| 08/08/2025 | Nguyễn Tuấn Nghĩa | 1.0 | Khởi tạo |
| 10/08/2025 | Nguyễn Tuấn Nghĩa | 1.0 | Đặc tả, vẽ activity flow, mô tả màn hình UC-11: Ký hợp đồng điện tử / Xây dựng yêu cầu phi chức năng |
| 12/08/2025 | Nguyễn Tuấn Nghĩa | 1.0 | Đặc tả, vẽ activity flow, mô tả màn hình UC-15: Chia sẻ hợp đồng điện tử / Xây dựng yêu cầu phi chức năng |
| 14/08/2025 | Nguyễn Tuấn Nghĩa | 1.0 | Đặc tả, vẽ activity flow, mô tả màn hình UC-26: Phản hồi yêu cầu (xem trọ) / Xây dựng yêu cầu phi chức năng |
| 16/08/2025 | Nguyễn Tuấn Nghĩa | 1.0 | Đặc tả, vẽ activity flow, mô tả màn hình UC-35: Cập nhật tiến độ (sửa chữa sự cố) / Xây dựng yêu cầu phi chức năng |
| 18/08/2025 | Nguyễn Tuấn Nghĩa | 1.0 | Đặc tả, vẽ activity flow, mô tả màn hình UC-38: Xem kế hoạch bảo trì định kỳ / Xây dựng yêu cầu phi chức năng |

### Bảng nguồn 2

| Từ viết tắt | Ý nghĩa |
| --- | --- |
| SRS | System Requirement Specification |
| OTP | One-Time Password |
| API | Application Programming Interface |
| UC | Use case |

### Bảng nguồn 3

| STT | Tham khảo | Chi tiết |
| --- | --- | --- |
| 1 | LalaHome | LalaHome Website |
| 2 | Batdongsan | Batdongsan Website |

### Bảng nguồn 4

| STT | Nguồn dữ liệu | Mô tả chi tiết |
| --- | --- | --- |
| 1 | Dữ liệu khách hàng | Email, Số điện thoại, Ngày sinh, Giấy tờ khai báo kinh doanh, Sổ đỏ, Hợp đồng thuê trọ |
| 2 | Dữ liệu giao dịch | Thông tin sử dụng dịch vụ, Số tiền thanh toán, Phương thức thanh toán, Ngày thanh toán, Dịch vụ kèm theo, Lịch sử thanh toán |
| 3 | Dữ liệu hành vi | Lượt xem phòng trọ, Lượt đặt lịch xem phòng, Lượt đánh giá và bình luận về phòng trọ, Lượt báo cáo sự cố |

### Bảng nguồn 5

| Chức năng | Mô tả chi tiết | Lợi ích |
| --- | --- | --- |
| Đăng ký/Đăng nhập | Lưu trữ thông tin tài khoản / Lưu trữ thông tin đăng nhập | Cho phép người dùng đăng nhập và tạo tài khoản trên app |
| Quản lý hồ sơ | Xem và sửa thông tin cá nhân / Xem và sửa thông tin kinh doanh | Giúp người dùng có thể sử dụng các chức năng về hợp đồng, quản lý nhà trọ và thanh toán |
| Quản lý hợp đồng | Xem, tạo, sửa, xoá hợp đồng tuỳ theo BR / Ký và chia sẻ hợp đồng cho người thuê / Cho phép duyệt yêu cầu huỷ hợp đồng của người thuê | Cho phép người dùng làm thủ tục cho thuê phòng trọ |
| Quản lý nhà trọ | Xem, tạo, sửa cho nhà trọ cũng như phòng trọ / Xem lịch sử thuê phòng | Giúp người dùng quản lý tài sản cho thuê của mình tốt hơn |
| Quản lý lịch xem trọ | Xem yêu cầu xem trọ / Phản hồi yêu cầu / Quản lý lịch hẹn | Giúp người dùng sắp xếp lịch xem trọ của người thuê sao cho hợp lý |
| Đánh giá và bình luận | Xem đánh giá và bình luận / Trả lời đánh giá và bình luận | Giúp người dùng biết được đánh giá và cảm nhận khách quan về dịch vụ |
| Nhắn tin với người thuê | Gửi tin nhắn cho người thuê / Nhận tin nhắn từ người thuê | Người dùng dễ dàng trao đổi thông tin và giao tiếp với người thuê |
| Thống kê hoạt động | Thống kê lượt xem, lưu, báo cáo, lượt đặt lịch xem | Người dùng dựa vào số liệu thống kê để đưa ra chiến lược marketing hợp lý |
| Tiếp nhận báo cáo (sự cố) | Xem danh sách và chi tiết báo cáo sự cố | Giúp người dùng nắm được thông tin về việc báo cáo sự cố của người thuê |
| Xử lý sự cố | Lập kế hoạch sửa chữa / Cập nhật tiến độ / Ghi nhận chi phí phát sinh | Giúp người dùng sắp xếp lịch trình sửa chữa sự cố của nhà trọ dưới góc độ trực quan hơn |
| Thống kê và báo cáo (sự cố) | Theo dõi các sự cố thường gặp / Xem kế hoạch bảo trì định kỳ / Cập nhật kế hoạch bảo trì định kỳ | Hỗ trợ việc bảo dưỡng, tu sửa nhà trọ, giúp nhà trọ đảm bảo an toàn |
| Quản lý hoá đơn điện tử | Xem lịch sử thanh toán / Xuất hoá đơn điện tử | Giúp người dùng xem lại lịch sử giao dịch và xuất hoá đơn điện tử với các giao dịch mình muốn |
| Theo dõi thanh toán | Liên kết ngân hàng/ví điện tử / Thiết lập khoản thu / Gửi nhắc nhở tự động / Gửi thông báo thanh toán | Hỗ trợ người dùng nhắc nhở và theo dõi tình trạng thanh toán tiền trọ hàng kỳ |
| Thống kê doanh thu | Thống kê doanh thu về tiền cho thuê phòng trọ, tiền nước, tiền điện, tiền dịch vụ,... | Người dùng có thể dựa vào thống kê để đánh giá độ hợp lý của chi phí dịch vụ hoặc độ tăng trưởng trong việc cho thuê phòng |

### Bảng nguồn 6

| STT | Mã NFR | Nội dung |
| --- | --- | --- |
| Yêu cầu về hiệu suất |  |  |
|  | NFR-01 | Thời gian phản hồi |
| 1 | NFR-01.1 | Thời gian tải trang không quá 2 giây |
| 2 | NFR-01.2 | Thời gian tìm kiếm không quá 3 giây |
| 3 | NFR-01.3 | Thời gian xử lý thanh toán không quá 5 giây |
|  | NFR-02 | Khả năng mở rộng |
| 4 | NFR-02.1 | Hệ thống phải hỗ trợ tối thiểu 10,000 người dùng đồng thời |
| 5 | NFR-02.2 | Cơ sở dữ liệu phải lưu trữ thông tin của ít nhất 100,000 phòng trọ |
| 6 | NFR-02.3 | Hệ thống phải xử lý được tối thiểu 1,000 giao dịch thanh toán mỗi giờ |
| Yêu cầu về bảo mật |  |  |
|  | NFR-03 | Bảo mật dữ liệu |
| 7 | NFR-03.1 | Tuân thủ quy định về bảo vệ dữ liệu cá nhân |
| 8 | NFR-03.2 | Kiểm tra bảo mật định kỳ |
| 9 | NFR-03.3 | Mã hóa dữ liệu người dùng và thông tin thanh toán (Bcrypt, Hash) |
|  | NFR-04 | Xác thực và phân quyền (Authorization & Authentication) |
| 10 | NFR-04.1 | Phân quyền truy cập dựa trên vai trò người dùng |
| 11 | NFR-04.2 | Giới hạn số lần đăng nhập thất bại |
| 12 | NFR-04.3 | Hỗ trợ xác thực hai yếu tố (2FA - 2 factors authentication) |
| Yêu cầu về độ tin cậy |  |  |
|  | NFR-05 | Tính sẵn sàng |
| 13 | NFR-05.1 | Hệ thống phải hoạt động 24/7 với thời gian ngừng hoạt động không quá 0.1% |
| 14 | NFR-05.2 | Thời gian phục hồi sau sự cố không quá 2 giờ |
| 15 | NFR-05.3 | Sao lưu dữ liệu hàng ngày |
|  | NFR-06 | Khả năng chịu lỗi |
| 16 | NFR-06.1 | Hệ thống phải tiếp tục hoạt động khi có lỗi một phần |
| 17 | NFR-06.2 | Tự động phát hiện và báo lỗi |
| 18 | NFR-06.3 | Tự động khôi phục sau lỗi không nghiêm trọng |
| Yêu cầu về tính sử dụng |  |  |
|  | NFR-07 | Giao diện người dùng |
| 19 | NFR-07.1 | Thiết kế giao diện thân thiện với người dùng |
| Yêu cầu về tương thích |  |  |
|  | NFR-08 | Tương thích nền tảng |
| 20 | NFR-08.1 | Hỗ trợ iOS 14.0 trở lên và Android 8.0 trở lên |

### Bảng nguồn 7

| STT | Mã UC | Tên tính năng |
| --- | --- | --- |
| 1 | UC-11 | Ký hợp đồng điện tử |
| 2 | UC-15 | Chia sẻ hợp đồng điện tử |
| 3 | UC-26 | Phản hồi yêu cầu (Xem trọ) |
| 4 | UC-35 | Cập nhật tiến độ (sửa chữa sự cố) |
| 5 | UC-38 | Xem kế hoạch bảo trì định kỳ |

### Bảng nguồn 8

| Nội dung | Mô tả |
| --- | --- |
| Use Case ID | UC-11 |
| Use Case Name | Ký hợp đồng điện tử |
| Description | Cho phép người dùng ký hợp đồng điện tử |
| Actor(s) | Registered Users |
| Related Use Case | UC-9, UC-10 |
| Priority | 1 |
| Trigger | Người dùng muốn ký hợp đồng điện tử của mình |
| Precondition | PRE-01. Người dùng đang có hợp đồng điện tử chưa được ký |
| Post-condition | POS-01. Hệ thống lưu thông tin ký hợp đồng và thông báo người dùng đã ký hợp đồng thành công |
| Basic Flow | Người dùng truy cập màn hình “Hợp đồng”, tab “Chưa ký” / Người dùng chọn hợp đồng muốn ký và bấm nút “Ký hợp đồng” / Người dùng thực hiện ký hợp đồng và bấm nút “Lưu” / Hệ thống thông báo hợp đồng đã được ký thành công, nếu hợp đồng đã đủ cả 2 chữ ký của 2 bên thì sẽ được chuyển về trạng thái Đã hoàn thành, nếu không thì sẽ chuyển sang trạng thái Đã ký |
| Alternative Flow | Tại bước 3, nếu người dùng muốn ký lại / AL-11.1. Trên modal chữ ký, người dùng bấm nút “Ký lại” / AL-11.2. Người dùng tiếp tục như bước 3 tại Basic Flow / Tại bước 3, nếu người dùng muốn hủy thay đổi đã thực hiện / AL-11.3. Người dùng bấm nút “Hủy” / AL-11.4. Màn hình trở về trang “Hợp đồng”, tab “Chưa ký” |
| Exception Flow | N/A |
| Business Rules | N/A |
| Non-functional Requirement | NR-01. Thời gian phản hồi < 2 giây |

### Bảng nguồn 9

| STT | Tên | Trường thông tin | Kiểu dữ liệu | Bắt buộc | Max length | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Header Back Button | btn_back | Button | Có | - | Nút quay lại màn hình trước |
| 2 | Screen Title | screen_title | String | Có | 50 | Tiêu đề màn hình "Hợp đồng" |
| 3 | Header Delete Button | btn_delete | Button | Có | - | Nút xóa hợp đồng |
| 4 | Contract ID | contract_id | String | Có | 20 | Mã định danh hợp đồng |
| 5 | Contract Title | contract_title | String | Có | 100 | Tiêu đề hợp đồng "DIGITAL SERVICE AGREEMENT" |
| 6 | Party A Service Provider | party_a_name | String | Có | 100 | Tên nhà cung cấp dịch vụ |
| 7 | Party A Company | party_a_company | String | Có | 150 | Tên công ty bên A |
| 8 | Party A Address | party_a_address | String | Có | 255 | Địa chỉ bên A |
| 9 | Party A Contact Person | party_a_contact | String | Có | 100 | Người liên hệ bên A |
| 10 | Party A Phone | party_a_phone | String | Có | 15 | Số điện thoại bên A |
| 11 | Party A Email | party_a_email | String | Có | 100 | Email bên A |
| 12 | Party B Client | party_b_name | String | Có | 100 | Tên khách hàng |
| 13 | Party B Company | party_b_company | String | Có | 150 | Tên công ty bên B |
| 14 | Party B Address | party_b_address | String | Có | 255 | Địa chỉ bên B |
| 15 | Party B Contact Person | party_b_contact | String | Có | 100 | Người liên hệ bên B |
| 16 | Party B Phone | party_b_phone | String | Có | 15 | Số điện thoại bên B |
| 17 | Party B Email | party_b_email | String | Có | 100 | Email bên B |
| 18 | Terms Title | terms_title | String | Có | 50 | Tiêu đề "TERMS AND CONDITIONS" |
| 19 | Scope of Services | scope_services | Text | Có | 2000 | Phạm vi dịch vụ cung cấp |
| 20 | Contract Duration | contract_duration | Text | Có | 500 | Thời hạn hợp đồng |
| 21 | Compensation | compensation | Text | Có | 1000 | Thông tin về phí và thanh toán |
| 22 | Deliverables | deliverables | Text | Có | 1500 | Các sản phẩm bàn giao |
| 23 | Confidentiality | confidentiality | Text | Có | 1000 | Điều khoản bảo mật |
| 24 | Termination | termination | Text | Có | 1000 | Điều khoản chấm dứt hợp đồng |
| 25 | Digital Signature Title | digital_signature_title | String | Có | 50 | Tiêu đề “DIGITAL SIGNATURES” |
| 26 | Sign Contract Button | btn_sign_contract | Button | Có | - | Nút bắt đầu quy trình ký hợp đồng |
| 27 | Edit Contract Button | btn_edit_contract | Button | Không | - | Nút chỉnh sửa hợp đồng |
| 28 | Share Contract Button | btn_share_contract | Button | Không | - | Nút chia sẻ hợp đồng |

### Bảng nguồn 10

| STT | Tên | Trường thông tin | Kiểu dữ liệu | Bắt buộc | Max length | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Signature Canvas | signature_canvas | Canvas | Có | - | Nút quay lại màn hình trước |
| 2 | Signature Data | signature_data | Base64 | Không | - | Dữ liệu chữ ký dạng Base64 |
| 3 | Re-Sign Button | btn_re_sign | Button | Có | - | Nút ký lại hợp đồng |
| 4 | Save Button | btn_save | Button | Có | - | Nút lưu chữ ký |

### Bảng nguồn 11

| Nội dung | Mô tả |
| --- | --- |
| Use Case ID | UC-15 |
| Use Case Name | Chia sẻ hợp đồng điện tử |
| Description | Cho phép người dùng chia sẻ hợp đồng điện tử cho người thuê |
| Actor(s) | Registered Users |
| Related Use Case | UC-10, UC-30 |
| Priority | 1 |
| Trigger | Người dùng muốn người thuê ký hợp đồng |
| Precondition | PRE-01. Người dùng đang có hợp đồng ở trạng thái Chưa ký hoặc Đã ký |
| Post-condition | POS-01. Box chat của người dùng và người thuê hiển thị tin nhắn đường dẫn (đường link) dẫn tới hợp đồng điện tử |
| Basic Flow | Người dùng chọn 1 hợp đồng trên trang “Hợp đồng”, tab “Chưa ký” hoặc “Đã ký” / Người dùng bấm nút “Chia sẻ” / Hệ thống hiển thị danh sách người thuê mà người dùng đã nhắn tin trước đây / Người dùng có thể chọn 1 người thuê trong danh sách đã kết nối hoặc tìm kiếm người thuê mới theo số điện thoại hoặc email và bấm nút “Gửi” / Màn hình hiển thị box chat của người dùng và người thuê hiển thị tin nhắn đường dẫn (đường link) dẫn tới hợp đồng điện tử |
| Alternative Flow | N/A |
| Exception Flow | N/A |
| Business Rules | BR-01. Người dùng chỉ được chia sẻ hợp đồng ở trạng thái Chưa ký (chưa được người dùng ký) hoặc Đã ký / BR-02. Người dùng chỉ được chia sẻ 1 hợp đồng tới tối đa 2 người thuê |
| Non-functional Requirement | NR-01. Thời gian phản hồi < 2 giây |

### Bảng nguồn 12

| STT | Tên | Trường thông tin | Kiểu dữ liệu | Bắt buộc | Max length | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Modal Title | modal_title | String | Có | 50 | Tiêu đề modal “Gửi tới” |
| 2 | Input Search | input_search | String | Có | 50 | Thanh tìm kiếm liên hệ theo email hoặc số điện thoại |
| 3 | Search Button | btn_search | Button | Có | - | Nút tìm kiếm |
| 4 | Contact Avatar | contact_avatar | Base64 | Không | - | Avatar của liên hệ, nếu không có để hình mặc định |
| 5 | Contact Name/Email | contact_name | String | Có | 50 | Tên hoặc email của liên hệ |
| 6 | Contact Checkbox | contact_checkbox | - | Có | - | Checkbox chọn liên hệ |
| 7 | Send Button | btn_send | Button | Có | - | Nút gửi |

### Bảng nguồn 13

| Nội dung | Mô tả |
| --- | --- |
| Use Case ID | UC-26 |
| Use Case Name | Phản hồi yêu cầu |
| Description | Cho phép người dùng phản hồi yêu cầu xem trọ của người thuê |
| Actor(s) | Registered Users |
| Related Use Case | UC-25 |
| Priority | 1 |
| Trigger | Người dùng muốn phản hồi yêu cầu xem trọ cho người thuê |
| Precondition | PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ / PRE-02. Người dùng đang có phòng trọ / PRE-03. Người dùng có yêu cầu xem phòng chưa duyệt |
| Post-condition | POS-01. Hệ thống hiển thị thông báo đã duyệt/từ chối yêu cầu / POS-02. Người dùng nhận được tin nhắn từ hệ thống là đã duyệt/từ chối yêu cầu xem phòng / POS-03. Người thuê nhận được tin nhắn từ hệ thống rằng yêu cầu xem phòng đã được duyệt/bị từ chối |
| Basic Flow | Người dùng truy cập màn hình “Lịch xem” để xem danh sách các yêu cầu xem trọ chưa được duyệt / Người dùng tìm tới yêu cầu muốn xét duyệt và bấm nút “Duyệt” để duyệt hoặc nút “Từ chối” để từ chối yêu cầu xem trọ / Hệ thống validate, hiển thị thông báo duyệt/từ chối thành công và gửi tin nhắn tới người dùng và người thuê |
| Alternative Flow | N/A |
| Exception Flow | Tại bước 3, nếu người dùng duyệt 2 yêu cầu xem cùng 1 phòng và cùng 1 khung giờ / EX-26.1. Hệ thống hiển thị thông báo lỗi “Đã có lịch xem trùng giờ” |
| Business Rules | N/A |
| Non-functional Requirement | NR-01. Thời gian phản hồi < 2 giây |

### Bảng nguồn 14

| STT | Tên | Trường thông tin | Kiểu dữ liệu | Bắt buộc | Max length | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Screen Title | screen_title | String | Có | 50 | Tiêu đề màn hình “Lịch xem” |
| 2 | Back Button | btn_back | Button | Có | - | Nút quay lại |
| 3 | Calendar Button | btn_calendar | Button | Có | - | Nút quản lý lịch xem |
| 4 | Input Search | input_search | String | Có | 50 | Thanh tìm kiếm yêu cầu xem trọ theo email hoặc số điện thoại |
| 5 | Search Button | btn_search | Button | Có | - | Nút tìm kiếm |
| 6 | Contact Avatar | contact_avatar | Base64 | Không | - | Avatar của liên hệ, nếu không có để hình mặc định |
| 7 | Contact Email | contact_email | String | Có | 50 | Email của liên hệ |
| 8 | Contact Phone | contact_phone | String | Có | 50 | SĐT của liên hệ |
| 9 | Board House Name | board_house_name | String | Có | 50 | Tên nhà trọ |
| 10 | Room Name | room_name | String | Có | 50 | Tên phòng trọ |
| 11 | Accept Button | btn_accept | Button | Có | - | Nút duyệt |
| 12 | Reject Button | btn_reject | Button | Có | - | Nút từ chối |

### Bảng nguồn 15

| Nội dung | Mô tả |
| --- | --- |
| Use Case ID | UC-35 |
| Use Case Name | Cập nhật tiến độ |
| Description | Cho phép người dùng cập nhật tiến độ sửa chữa sự cố |
| Actor(s) | Registered Users |
| Related Use Case | UC-33, UC-34 |
| Priority | 1 |
| Trigger | Người dùng muốn cập nhật tiến độ sửa chữa của sự cố |
| Precondition | PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ / PRE-02. Người dùng đã tạo phòng trọ / PRE-03. Người dùng đang có sự cố “Đã tiếp nhận” (đã xem, đã đặt lịch sửa chữa, còn hạn và tiến độ chưa đạt 100%) |
| Post-condition | POS-01. Hệ thống thông báo cập nhật tiến độ sửa chữa và gửi thông báo cập nhật tới người thuê |
| Basic Flow | Người dùng bấm chọn 1 sự cố trên trang “Danh sách sự cố”, tab “Đã tiếp nhận” / Hiển thị chi tiết về sự cố đó trên trang “Chi tiết sự cố” / Người dùng bấm nút “Cập nhật tiến độ” / Hiển thị modal “Cập nhật tiến độ” / Người dùng thực hiện cập nhật tiến độ và bấm nút “Lưu” / Hệ thống lưu tiến độ sửa chữa, thông báo người dùng cập nhật tiến độ thành công và gửi tiến độ sửa chữa mới cho người thuê |
| Alternative Flow | Tại bước 5, nếu người dùng muốn huỷ việc cập nhật tiến độ / AL-35.1. Người dùng bấm nút “Huỷ” / AL-35.2. Hệ thống trở về trang “Chi tiết sự cố” / Tại bước 6, nếu tiến độ cập nhật là 100% / AL-35.3. Hệ thống lưu tiến độ sửa chữa, chuyển trạng thái báo cáo sự cố thành “Đã hoàn thành”, thông báo người dùng cập nhật tiến độ thành công và gửi tiến độ sửa chữa cho người thuê |
| Exception Flow | N/A |
| Business Rules | N/A |
| Non-functional Requirement | NR-01. Thời gian phản hồi < 2 giây |

### Bảng nguồn 16

| STT | Tên | Trường thông tin | Kiểu dữ liệu | Bắt buộc | Max length | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Modal Title | modal_title | String | Có | 50 | Tiêu đề modal “Cập nhật tiến độ” |
| 2 | Progress Bar | prg_bar | Button | Có | - | Thanh tiến độ |
| 3 | Note Title | note_title | String | Có | 10 | Tiêu đề “Ghi chú” |
| 4 | Note Area | note_area | Text | Không | 100 | Khu vực nhập ghi chú cho từng lần cập nhật tiến độ |
| 5 | Save Button | btn_save | Button | Có | - | Nút lưu |

### Bảng nguồn 17

| Nội dung | Mô tả |
| --- | --- |
| Use Case ID | UC-38 |
| Use Case Name | Xem kế hoạch bảo trì định kỳ |
| Description | Cho phép người dùng xem kế hoạch bảo trì định kỳ của nhà trọ |
| Actor(s) | Registered Users |
| Related Use Case | UC-39 |
| Priority | 1 |
| Trigger | Người dùng muốn xem kế hoạch bảo trì định kỳ của nhà trọ |
| Precondition | PRE-01. Người dùng đã đăng nhập thành công vào SmartChủ / PRE-02. Người dùng đã tạo nhà trọ và các phòng trọ / PRE-03. Người dùng đã cập nhật đầy đủ thông tin kinh doanh |
| Post-condition | POS-01. Hệ thống hiển thị kế hoạch bảo trì định kỳ dành cho nhà trọ |
| Basic Flow | Người dùng truy cập trang “Thống kê”, tab “Sự cố” / Hiển thị dropdown các nhà trọ người dùng sở hữu / Người dùng bấm chọn nhà trọ muốn xem / Hiển thị thống kê về sự cố của nhà trọ / Người dùng bấm nút Xem lịch bảo trì / Hệ thống hiển thị lịch với thời gian dự tính bảo trì từng phòng trọ của nhà trọ |
| Alternative Flow | Tại bước 6, nếu người dùng chưa đặt lịch bảo trì bao giờ / AL-38.1. Hệ thống sử dụng AI và tính toán dựa trên tuổi của nhà trọ để đưa ra 1 kế hoạch bảo trì tiết kiệm mà an toàn / AL-38.2. Lưu kế hoạch bảo trì vào DB / AL-38.3. Hệ thống hiển thị lịch với thời gian dự tính bảo trì từng phòng trọ của nhà trọ |
| Exception Flow | N/A |
| Business Rules | N/A |
| Non-functional Requirement | NR-01. Thời gian phản hồi < 12 giây |

### Bảng nguồn 18

| STT | Tên | Trường thông tin | Kiểu dữ liệu | Bắt buộc | Max length | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Screen Title | screen_title | String | Có | 50 | Tiêu đề modal “Lịch bảo trì” |
| 2 | Back Button | btn_back | Button | Có | - | Nút quay lại |
| 3 | Option Button | btn_option | Button | Có | - | Nút lựa chọn định dạng xem lịch |
| 4 | Calendar Area | calendar_area | Canvas | Có | - | Khu vực hiển thị phòng cần bảo trì trên lịch |

## Tài sản hình ảnh trích xuất

- [image-01.png](assets/frs-smartchu/image-01.png)
- [image-02.png](assets/frs-smartchu/image-02.png)
- [image-03.png](assets/frs-smartchu/image-03.png)
- [image-04.png](assets/frs-smartchu/image-04.png)
- [image-05.png](assets/frs-smartchu/image-05.png)
- [image-06.png](assets/frs-smartchu/image-06.png)
- [image-07.png](assets/frs-smartchu/image-07.png)
- [image-08.png](assets/frs-smartchu/image-08.png)
- [image-09.png](assets/frs-smartchu/image-09.png)
- [image-10.png](assets/frs-smartchu/image-10.png)
- [image-11.png](assets/frs-smartchu/image-11.png)
- [image-12.png](assets/frs-smartchu/image-12.png)
- [image-13.png](assets/frs-smartchu/image-13.png)
- [image-14.png](assets/frs-smartchu/image-14.png)
- [image-15.png](assets/frs-smartchu/image-15.png)
- [image-16.png](assets/frs-smartchu/image-16.png)
- [image-17.png](assets/frs-smartchu/image-17.png)
