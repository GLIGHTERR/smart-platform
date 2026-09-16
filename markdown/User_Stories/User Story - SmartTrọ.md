# User Stories SmartTrọ

> Bản Markdown được đồng bộ từ [`User Story - SmartTrọ.xlsx`](../../User_Stories/User%20Story%20-%20SmartTro%CC%A3.xlsx) ngày 2026-09-16.
> SHA-256 nguồn: `d9dfec73abc55b828981b1854723cd7aa516deeda77ba6ded5f7f68aac21ec0f`.
> File XLSX gốc vẫn là nguồn dữ liệu và định dạng chính thức; bản này tối ưu cho agent đọc theo từng User Story.
> Tổng số User Story được chuyển đổi: 31.


## Đăng kýĐăng nhập

### US 1.0 — Đăng ký bằng email

Là một người dùng, tôi muốn đăng ký tài khoản bằng email được xác minh để có tài khoản sử dụng các dịch vụ của app.

**Ưu tiên:** High

**Acceptance Criteria**

- 1. Email phải đúng định dạng; hệ thống trim khoảng trắng, dùng email chuẩn hóa để kiểm tra unique và không tạo tài khoản trùng.
- 2. Sau khi email hợp lệ được gửi, hệ thống tạo yêu cầu đăng ký và gửi mã OTP 6 chữ số tới email đó.
- 3. Mật khẩu phải chứa tối thiểu 8 ký tự, gồm ít nhất 1 chữ hoa, 1 số và 1 ký tự đặc biệt.
- 4. Sau khi OTP hợp lệ, người dùng được chuyển sang bước tạo mật khẩu; OTP sai hoặc hết hạn không được chuyển bước.
- 5. Sau khi tạo tài khoản thành công, người dùng được chuyển về trang Đăng nhập với email có thể được điền sẵn; hệ thống không tự đăng nhập và không lưu OTP/mật khẩu.

### US 2.0 — Đăng nhập bằng email và mật khẩu

Là một người dùng đã có tài khoản và đã xác minh email, tôi muốn đăng nhập bằng email và mật khẩu để sử dụng các dịch vụ của app.

**Ưu tiên:** High

**Acceptance Criteria**

- 1. Trang đăng nhập hiển thị input Email, Mật khẩu, nút "Đăng nhập", link "Quên mật khẩu" và link sang "Đăng ký".
- 2. Với email và mật khẩu hợp lệ, người dùng đăng nhập thành công và được chuyển vào trang chính của app.
- 3. Khi email hoặc mật khẩu không khớp, hệ thống hiển thị thông báo generic và không tiết lộ email có tồn tại hay không.
- 4. Khi request đăng nhập đang xử lý, hệ thống không gửi thêm request trùng nếu người dùng bấm lại nút Đăng nhập.
- 5. Nếu tài khoản chưa xác minh email, hệ thống hướng dẫn người dùng tiếp tục/resend bước activation thay vì tạo tài khoản mới.
- 6. Hệ thống chuyển người dùng đến trang "Quên mật khẩu" khi người dùng chọn link tương ứng; flow recovery được chốt ở requirement riêng.
- 7. Đăng nhập thông thường không yêu cầu OTP. MFA hoặc risk-based OTP chỉ được bổ sung bằng requirement/decision riêng.
- 8. Mật khẩu không được ghi vào log, route parameter hoặc persistent storage. Failed-login threshold và lock duration cần được chốt trước task backend auth.

### US 3.0 — Quên mật khẩu

Là một người dùng, tôi muốn được cấp lại mật khẩu mới nếu quên mật khẩu để tiếp tục đăng nhập được và sử dụng các dịch vụ của app

**Ưu tiên:** High

**Acceptance Criteria**

- 1. Số điện thoại người dùng nhập phải là SĐT đã đăng ký tài khoản
- 2. Sau khi người dùng nhập số điện thoại, hệ thống phải gửi mã OTP qua SĐT trong vòng 3s
- 3.Mật khẩu mới phải chứa tối thiểu 8 ký tự, gồm ít nhất 1 chữ hoa, 1 số và 1 ký tự đặc biệt
- 4. Người dùng phải được chuyển đến trang nhập mật khẩu trong vòng 3s sau khi nhập đúng mã OTP
- 5. Người dùng phải được chuyển đến trang đăng nhập trong tối đa 3s sau khi nhập mật khẩu hợp lệ
- 6. Người dùng chưa vượt quá số lần xin cấp lại mật khẩu tối đa

## Quản lý hồ sơ

### US 4.0 — Xem thông tin cá nhân

Là một người dùng, tôi muốn xem thông tin tài khoản cá nhân của mình trên hệ thống của app

**Ưu tiên:** High

**Acceptance Criteria**

- 1. Trang "Tài khoản" hiển thị các thông tin như tên người dùng, email, SĐT, avatar, số phòng và tên nhà trọ hiện đang thuê (nếu có), nút "Sửa" và nút "Đổi mật khẩu"
- 2. Thông tin SĐT chỉ được hiển thị 3 số cuối
- 3. Hệ thống phải chuyển người dùng tới trang "Sửa thông tin cá nhân" ngay khi người dùng bấm nút "Sửa" trên trang "Tài khoản"
- 4. Hệ thống phải chuyển người dùng tới trang "Đổi mật khẩu" ngay khi người dùng bấm nút "Đổi mật khẩu" trên trang "Tài khoản"

### US 5.0 — Cập nhật thông tin cá nhân

Là một người dùng đã đăng ký tài khoản, tôi muốn cập nhật thông tin tài khoản cá nhân của mình trên hệ thống của app để thuận lợi cho quá trình thuê nhà trọ

**Ưu tiên:** High

**Acceptance Criteria**

- 1. Trang "Sửa thông tin cá nhân" hiển thị các input để người dùng chỉnh sửa các thông tin như tên người dùng, email và image picker cho trường avatar. Trường SĐT không được thay đổi
- 2. Người dùng cần đợi 1h kể từ lần thay đổi thông tin tài khoản cá nhân trước đó để có thể thay đổi tiếp
- 3. Hệ thống phải chuyển người dùng về trang "Tài khoản" trong vòng 2s sau khi người dùng bấm nút "Xác nhận"

### US 6.0 — Đổi mật khẩu

Là một người dùng, tôi muốn đổi mật khẩu của mình để tăng tính bảo mật

**Ưu tiên:** Medium

**Acceptance Criteria**

- 1. Trang "Đổi mật khẩu" bao gồm các input cho mật khẩu hiện tại, mật khẩu mới và xác nhận mật khẩu mới, nút "Lưu" và nút "Huỷ"
- 2.Mật khẩu mới phải chứa tối thiểu 8 ký tự, gồm ít nhất 1 chữ hoa, 1 số và 1 ký tự đặc biệt
- 3. Người dùng chỉ được đổi mật khẩu mỗi ngày 1 lần

## Quản lý hợp đồng điện tử

### US 7.0 — Xem hợp đồng điện tử

Là một người dùng, tôi muốn xem thông tin hợp đồng thuê trọ của tôi (hợp đồng điện tử) để kiểm tra lại độ minh bạch của việc thuê trọ nếu cần

**Ưu tiên:** High

**Acceptance Criteria**

- 1. Trang "Hợp đồng điện tử của tôi" hiển thị hợp đồng hiện tại của người dùng và lịch sử các hợp đồng mà người dùng đã ký
- 2. Người dùng bấm vào hợp đồng để xem chi tiết hợp đồng

### US 8.0 — Ký hợp đồng điện tử

Là một người dùng, tôi muốn ký hợp đồng điện tử để hoàn tất thủ tục thuê phòng trọ

**Ưu tiên:** High

**Acceptance Criteria**

- 1. Trang "Hợp đồng điện tử" có đầy đủ thông tin như 1 hợp đồng bản cứng, trong đó các phần để người dùng ký sẽ có nút "Ký tại đây"
- 2. Sau khi người dùng bấm nút "Ký tại đây", hiển thị pop-up "Chữ ký điện tử", người dùng có thể ký lại nhiều lần trước khi bấm nút "Lưu"
- 3. 1 người không được có trên 2 hợp đồng active cùng lúc
- 4. Các phản hồi của hệ thống trong luồng phải được hoàn thành dưới 3s

### US 9.0 — Huỷ hợp đồng điện tử

Là một người dùng, tôi muốn huỷ hợp đồng điện tử để chuyển sang phòng trọ khác

**Ưu tiên:** High

**Acceptance Criteria**

- 1. Trang "Hợp đồng điện tử của tôi" có hiển thị nút "Huỷ hợp đồng"
- 2. Sau khi người dùng bấm nút "Huỷ hợp đồng", hiển thị pop-up confirm "Xác nhận yêu cầu huỷ hợp đồng"
- 3. Sau khi người dùng bấm nút "Xác nhận" trong pop-up confirm, người dùng sẽ đợi chủ trọ phê duyệt yêu cầu trong vòng 7 ngày
- 4. Request huỷ hợp đồng sẽ bị hết hạn sau 7 ngày nếu không có sự phê duyệt của chủ trọ

## Tìm kiếm nhà trọ

### US 10.0 — Xem danh sách phòng trọ

Là một người dùng, tôi muốn xem danh sách các phòng trọ tôi có thể thuê tại thời điểm hiện tại

**Ưu tiên:** High

**Acceptance Criteria**

- 1. Trang "Danh sách phòng" hiển thị danh sách các phòng trọ trên hệ thống và đáp ứng các điều kiệu trong bộ lọc, 1 bộ lọc theo giá, diện tích phòng, vị trí địa lý và tiện ích
- 2. Người dùng bấm vào 1 phòng trên danh sách để xem chi tiết

### US 11.0 — Xem chi tiết phòng trọ

Là một người dùng, tôi muốn xem thông tin chi tiết của phòng trọ được đăng lên hệ thống

**Ưu tiên:** High

**Acceptance Criteria**

- 1. Trang chi tiết phòng trọ hiển thị các trường tên trọ, tên/số phòng, hình ảnh, giá tiền, mô tả chi tiết, nút "Lưu nhà trọ", nút "Đặt lịch", khu vực đánh giá và bình luận
- 2. Thời gian load trang chi tiết phòng trọ yêu cầu dưới 2s

### US 12.0 — Đánh giá và bình luận trong bài đăng về phòng trọ

Là một người dùng, tôi muốn đánh giá và bình luận về bài đăng về phòng trọ của chủ trọ

**Ưu tiên:** Medium

**Acceptance Criteria**

- 1. Trang chi tiết phòng trọ sẽ có phần đánh giá bài đăng theo số sao và phần bình luận
- 2. Phần đánh giá sẽ có tối đa 5 sao. Người dùng có thể chọn đánh giá và bình luận hoặc chỉ đánh giá
- 3. Mỗi bình luận không phải là luồng bình luận nhiều người. Mỗi bình luận chỉ có 1 bình luận kèm đánh giá của người dùng và 1 bình luận trả lời/giải đáp thắc mắc của chủ trọ tới người dùng

### US 13.0 — Lưu phòng trọ yêu thích

Là một người dùng, tôi muốn lưu phòng trọ để nắm bắt thông tin mới nhất về phòng trọ nhanh nhất

**Ưu tiên:** Medium

**Acceptance Criteria**

- 1. Trang chi tiết phòng trọ sẽ có phần lưu phòng trọ yêu thích
- 2. Mỗi người dùng có thể lưu tối đa 5 phòng trọ mà họ yêu thích
- 3. Người dùng đã lưu phòng trọ sẽ nhận được thông báo về những thay đổi public về phòng trọ như trạng thái (đang sử dụng/bảo trì) hay việc còn phòng/hết phòng

## Tương tác

### US 14.0 — Đặt lịch xem trọ

Là một người dùng, tôi muốn đặt lịch xem nhà trọ

**Ưu tiên:** High

**Acceptance Criteria**

- 1. Trên trang "Danh sách phòng" hoặc trang chi tiết phòng trọ, người dùng có thể bấm nút "Đặt lịch". Hệ thống sẽ hiển thị pop-up Calendar đẻ người dùng chọn ngày và giờ đến xem phòng trọ
- 2. Người dùng không thể chọn ngày trong quá khứ, nếu người dùng chọn lịch trùng thời gian xem trọ khác của chủ trọ, hệ thống sẽ thông báo để người dùng chọn ngày giờ khác
- 3. Người dùng sẽ nhận được thông báo khi chủ trọ duyệt yêu cầu xem trọ

### US 15.0 — Nhắn tin với chủ trọ

Là một người dùng, tôi muốn nhắn tin với chủ trọ để dễ dàng trao đổi trong thời gian thuê phòng trọ

**Ưu tiên:** High

**Acceptance Criteria**

- 1. Trang "Tin nhắn" hiển thị danh sách các chủ trọ mà người dùng đã liên lạc
- 2. Cuộc hội thoại mới sẽ được khởi tạo khi người dùng và chủ trọ ký hợp đồng lần đầu tiên
- 3. Hệ thống phải xử lý tin nhắn được gửi trong vòng không quá 10s (Bao gồm cả việc gửi hình ảnh và video)

### US 16.0 — Viết đánh giá về nhà trọ

Là một người dùng, tôi muốn đánh giá về nhà trọ để thể hiện quan điểm và cái nhìn chung về nhà trọ và chủ trọ

**Ưu tiên:** Medium

**Acceptance Criteria**

- 1. Trang "Đánh giá" của nhà trọ hiển thị số sao trung bình của nhà trọ và danh sách các người dùng đã đánh giá
- 2. Phần đánh giá sẽ có tối đa 5 sao. Người dùng có thể chọn đánh giá và bình luận hoặc chỉ đánh giá

### US 17.0 — Báo cáo vi phạm

Là một người dùng, tôi muốn báo cáo tới quản trị viên của hệ thống về những vi phạm của chủ trọ, nhà trọ hoặc chính người dùng khác

**Ưu tiên:** Medium

**Acceptance Criteria**

- 1. Người dùng có thể bấm vào biểu tượng ba chấm dọc để thấy lựa chọn báo cáo vi phạm và chọn báo cáo vi phạm.
- 2. Những nơi người dùng có thể báo cáo vi phạm: Bài đăng phòng trọ, Đánh giá và bình luận trong bài đăng phòng trọ, Đánh giá về nhà trọ
- 3. Người dùng có thể báo cáo các hành vi vi phạm tiêu chuẩn cộng đồng của hệ thống SmartTrọ cho đội ngũ quản trị viên của hệ thống

## Quản lý sự cố

### US 18.0 — Xem các báo cáo đã tạo

Là một người dùng, tôi muốn xem danh sách các báo cáo sự cố tôi đã tạo

**Ưu tiên:** Medium

**Acceptance Criteria**

- 1. Trang "Báo cáo sự cố" hiển thị danh sách các báo cáo sự cố mà người dùng đã tạo cho phòng trọ hiện tại và nút "Tạo báo cáo sự cố"
- 2. Người dùng có thể lọc kết quả theo thời gian, trang thiết bị bị hỏng hóc, độ ưu tiên

### US 19.0 — Tạo báo cáo sự cố mới

Là một người dùng, tôi muốn tạo báo cáo sự cố để thông báo với chủ trọ rằng phòng trọ đang có hỏng hóc

**Ưu tiên:** Medium

**Acceptance Criteria**

- 1. Trang "Báo cáo sự cố" hiển thị danh sách các báo cáo sự cố mà người dùng đã tạo cho phòng trọ hiện tại và nút "Tạo báo cáo sự cố"
- 2. Sau khi người dùng bấm nút "Tạo báo cáo sự cố", hiển thị pop-up "Tạo báo cáo sự cố"
- 3. Pop-up "Tạo báo cáo sự cố" hiển thị các trường để chọn loại trang thiết bị bị hỏng hóc, độ ưu tiên, text area chú thích thêm và button "Gửi"
- 4. Hệ thống phải gửi yêu cầu báo cáo sự cố tới chủ trọ trong vòng 5s

### US 20.0 — Theo dõi tiến độ xử lý

Là một người dùng, tôi muốn theo dõi tiến độ xử lý báo cáo sự cố mà mình đã tạo

**Ưu tiên:** Medium

**Acceptance Criteria**

- 1. Người dùng bấm vào 1 báo cáo sự cố chưa được hoàn thành và chưa hết hạn để xem chi tiết và theo dõi tiến độ
- 2. Trang "Chi tiết sự cố" hiển thị các trường như loại thiết bị bị hỏng hóc, độ ưu tiên, chú thích thêm, thời gian tạo, progress bar thể hiện tiến độ hoàn thành và nút "Cập nhật"

### US 21.0 — Cập nhật thông tin báo cáo

Là một người dùng, tôi muốn cập nhật thông tin báo cáo sự cố mà mình đã tạo

**Ưu tiên:** Medium

**Acceptance Criteria**

- 1. Trang "Cập nhật báo cáo sự cố" hiển thị các input cho các trường trang thiết bị bị hỏng hóc, độ ưu tiên, chú thích và nút "Cập nhật"
- 2. Hệ thống phải hoàn tất thao tác cập nhật trong vòng 3s

### US 22.0 — Đánh giá sau xử lý

Là một người dùng, tôi muốn đánh giá kết quả xử lý sự cố của chủ trọ

**Ưu tiên:** Medium

**Acceptance Criteria**

- 1. Người dùng bấm vào 1 báo cáo sự cố đã được hoàn thành để xem chi tiết và đánh giá
- 2. Người dùng sẽ đánh giá theo các tiêu chí như độ hoàn thiện, tốc độ, thái độ

## Thanh toán trực tuyến

### US 23.0 — Liên kết ngân hàng/ví điện tử

Là một người dùng, tôi muốn liên kết ngân hàng/ví điện tử vào tài khoản SmartTrọ để thực hiện thanh toán các khoản thu như tiền đặt cọc cho trọ hay tiền thuê trọ

**Ưu tiên:** High

**Acceptance Criteria**

- 1. Trên trang "Thanh toán", người dùng bấm nút "Thêm phương thức thanh toán" để liên kết thêm phương thức thanh toán mới cho tài khoản
- 2. Người dùng có thể chọn các phương thức thanh toán hiện tại của Việt Nam như tài khoản ngân hàng và ví điện tử MOMO
- 3. Hệ thống phải xác thực tài khoản ngân hàng và ví điện tử trước khi hoàn tất việc liên kết
- 4. Hệ thống phải xác thực tài khoản ngân hàng và ví điện tử trong vòng 3s

### US 24.0 — Thanh toán thủ công

Là một người dùng, tôi muốn thanh toán tiền trọ

**Ưu tiên:** High

**Acceptance Criteria**

- 1. Trên trang "Thanh toán", người dùng bấm nút "Thanh toán tiền trọ" để tiến hành thanh toán tiền trọ
- 2. Hệ thống phải lưu thông tin giao dịch để đối soát lại về sau
- 3. Hệ thống phải rollback tiền về tài khoản người dùng nếu có sự cố trong việc thanh toán (time out, lỗi ngân hàng ở tài khoản đích)
- 4. Hệ thống phải rollback tiền về tài khoản người dùng trong vòng 24h kể từ khi xảy ra sự cố

### US 25.0 — Thanh toán tự động

Là một người dùng, tôi muốn đặt lịch thanh toán tiền trọ tự động mỗi kỳ hạn để không phải thanh toán thủ công

**Ưu tiên:** High

**Acceptance Criteria**

- 1. Người dùng chọn lịch thanh toán phải là ngày tương lai, không được chọn ngày quá khứ. Người dùng chọn vòng lặp phù hợp với yêu cầu của chủ trọ (Mỗi tháng, mỗi quý, mỗi 6 tháng, mỗi 1 năm)
- 2. Người dùng cần phải liên kết ngân hàng/ví điện tử trước đó
- 3. Hệ thống tự thử lại việc thanh toán nếu có vấn đề phát sinh trong thời gian thực hiện thanh toán
- 4. Giới hạn việc hệ thống thử lại là 3 lần. Sau 3 lần không thành công, người dùng cần vào xem lịch sử giao dịch để thực hiện lại giao dịch thủ công
- 5. Chỉ có việc tài khoản ngân hàng/ví điện tử hết tiền mới tạm dừng chức năng thanh toán. Những vấn đề khác không ảnh hưởng tới lịch trình thanh toán tự động

### US 26.0 — Nhận thông báo đến hạn

Là một người dùng, tôi muốn nhận thông báo khi đến hạn thanh toán tiền trọ để thanh toán tiền trọ kịp lúc

**Ưu tiên:** Medium

**Acceptance Criteria**

- 1. Người dùng sẽ nhận được thông báo thanh toán tiền trọ khi tới ngày mà chủ trọ đặt deadline thanh toán trên trang "Thông báo"
- 2. Người dùng sẽ nhận được thông báo thanh toán tiền trọ khi tới ngày mà chủ trọ đặt deadline thanh toán trong phần thông báo của điện thoại
- 3. Người dùng có thể truy cập trang "Thanh toán" qua những thông báo trên

### US 27.0 — Đặt nhắc nhở thanh toán

Là một người dùng, tôi muốn tự đặt lịch thông báo nhắc nhở thanh toán tiền trọ cho bản thân để tránh việc quên hạn thanh toán

**Ưu tiên:** Medium

**Acceptance Criteria**

- 1. Trên trang "Thanh toán", khi người dùng bấm nút "Đặt lịch nhắc nhở thanh toán" hình cái chuông, hiển thị pop-up Calendar
- 2. Người dùng sẽ chọn ngày mà muốn hệ thống gửi thông báo
- 3. Người dùng sẽ nhận được thông báo thanh toán khi tới ngày đặt thông báo trên trang "Thông báo" của app và trong phần thông báo của điện thoại. Người dùng cũng có thể bấm vào các thông báo trên để tới trang "Thanh toán"

## Quản lý hóa đơn điện tử

### US 28.0 — Xem lịch sử thanh toán

Là một người dùng, tôi muốn xem lịch sử thanh toán tiền trọ

**Ưu tiên:** High

**Acceptance Criteria**

- 1. Trên trang "Thanh toán", người dùng bấm nút "Tra cứu giao dịch" để xem lịch sử các giao dịch trước đây
- 2. Người dùng có thể chọn xem các giao dịch trong vòng 6 tháng, 1 năm hoặc 2 năm
- 3. Người dùng chọn 1 giao dịch để xem chi tiết, có thể đặt lệnh thanh toán lại hoặc xuất hóa đơn điện tử

### US 29.0 — Xuất hóa đơn điện tử

Là một người dùng, tôi muốn xuất hóa đơn điện tử để nhận trợ cấp từ nơi học tập hoặc làm việc

**Ưu tiên:** Medium

**Acceptance Criteria**

- 1. Trên trang "Chi tiết giao dịch", người dùng bấm nút "Xuất hóa đơn" để xuất hóa đơn điện tử
- 2. Người dùng cần phải điền đầy đủ thông tin của hóa đơn
- 3. Người dùng cần có máy in để hoàn thành tác vụ

## Theo dõi chi tiêu

### US 30.0 — Thống kê chi phí theo tháng

Là một người dùng, tôi muốn thống kê chi phí phát sinh theo từng tháng để quản lý chi tiêu chặt chẽ hơn

**Ưu tiên:** Medium

**Acceptance Criteria**

- 1. Trên trang "Theo dõi chi tiêu", người dùng bấm nút "Thống kê chi phí" để xem thống kê
- 2. Người dùng có thể chọn xem thống kê theo tiền trọ, tiền nước, tiền wifi, tiền điện hoặc tiền do các chi phí hỏng hóc phát sinh (Do người dùng gây ra chứ không phải lỗi hỏng hóc từ chất lượng trang thiết bị kém hay trang thiết bị tự hỏng do tới hạn)
- 3. Hiển thị các thông tin về chi phí, tỷ lệ phần trăm mỗi chi phí theo từng tháng, chênh lệch so với tháng trước

### US 31.0 — Báo cáo chi tiêu

Là một người dùng, tôi muốn xem báo cáo chi tiêu

**Ưu tiên:** Medium

**Acceptance Criteria**

- 1. Trên trang "Theo dõi chi tiêu", người dùng bấm nút "Báo cáo chi tiêu" để xem báo cáo
- 2. Báo cáo cần đưa ra đủ từng mục chi tiêu và số tiền cho những mục đó, phân chia từng tháng rõ ràng
- 3. Người dùng có thể xuất file excel cho báo cáo
