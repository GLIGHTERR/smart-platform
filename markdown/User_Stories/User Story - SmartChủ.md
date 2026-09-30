# User Story — SmartChủ

> **Loại tài liệu:** Markdown mirror của workbook nguồn.
> **Nguồn:** `User_Stories/User Story - SmartChủ.xlsx` — SHA-256 `6d061232942652055cb034b0908f7a702274e737574abb79da5f100098f7c374` — chuyển đổi 2026-09-30.
> User story lịch sử về số điện thoại/SMS được giữ nguyên. Living spec Approved trong `docs/` được ưu tiên khi triển khai.

## Đăng kýĐăng nhập

### US-01: Đăng ký bằng số điện thoại

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn đăng ký tài khoản của app qua số điện thoại để có tài khoản sử dụng các dịch vụ của app
- Living spec hiện hành: [UC-01](../../docs/use-cases/smartchu/UC-01-sign-up.md)

**Acceptance Criteria nguồn**

- 1. Số điện thoại người dùng nhập phải hợp lệ
- 2. Sau khi người dùng nhập số điện thoại, hệ thống phải gửi mã OTP qua SĐT trong tối đa 10s
- 3.Mật khẩu phải chứa tối thiểu 8 ký tự, gồm ít nhất 1 chữ hoa, 1 số và 1 ký tự đặc biệt
- 4. Người dùng phải được chuyển đến trang nhập mật khẩu trong vòng 3s sau khi nhập đúng mã OTP
- 5. Người dùng phải được đăng ký thành công và chuyển đến trang đăng nhập trong tối đa 3s sau khi nhập mật khẩu hợp lệ

### US-02: Đăng nhập bằng số điện thoại

- **Priority:** High
- **User Story:** Là một người dùng đã đăng ký tài khoản, tôi muốn đăng nhập vào app để sử dụng các dịch vụ của app
- Living spec hiện hành: [UC-02](../../docs/use-cases/smartchu/UC-02-sign-in.md)

**Acceptance Criteria nguồn**

- 1. Trang đăng nhập phải hiển thị input nhập tên đăng nhập/SĐT, mật khẩu, nút "Đăng nhập" và nút "Quên mật khẩu"
- 2. Người dùng phải được đăng nhập thành công và chuyển đến trang đăng nhập trong tối đa 3 giây sau khi nhập SĐT và mật khẩu trùng khớp
- 3. Hệ thống phải thông báo đến người dùng khi tên đăng nhập hoặc mật khẩu không trùng khớp. Thông báo phải hiển thị cảnh báo khóa tài khoản nếu nhập sai quá 5 lần
- 4. Người dùng được nhập mật khẩu cho cùng một SĐT tối đa 5 lần
- 5. Nếu người dùng nhập sai mật khẩu quá 5 lần, hệ thống sẽ khóa tài khoản của SĐT đó trong 72h
- 5. Hệ thống phải chuyển người dùng đến trang "Quên mật khẩu" trong tối đa 3 giây sau khi người dùng chọn "quên mật khẩu"
- 6. Màn hình nhập mã OTP phải hiển thị input nhập mã OTP, nút "Xác nhận" và nút "Gửi lại OTP"
- 7. Hệ thống phải gửi mã OTP tới SĐT đã đăng ký tài khoản để xác thực yêu cầu đăng nhập trong vòng 5s kể tử khi người dùng bấm nút "Đăng nhập"

### US-03: Quên mật khẩu

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn được cấp lại mật khẩu mới nếu quên mật khẩu để tiếp tục đăng nhập được và sử dụng các dịch vụ của app
- Living spec hiện hành: [UC-03](../../docs/use-cases/smartchu/UC-03-forgot-password.md)

**Acceptance Criteria nguồn**

- 1. Số điện thoại người dùng nhập phải là SĐT đã đăng ký tài khoản
- 2. Sau khi người dùng nhập số điện thoại, hệ thống phải gửi mã OTP qua SĐT trong vòng 3s
- 3.Mật khẩu mới phải chứa tối thiểu 8 ký tự, gồm ít nhất 1 chữ hoa, 1 số và 1 ký tự đặc biệt
- 4. Người dùng phải được chuyển đến trang nhập mật khẩu trong vòng 3s sau khi nhập đúng mã OTP
- 5. Người dùng phải được chuyển đến trang đăng nhập trong tối đa 3s sau khi nhập mật khẩu hợp lệ
- 6. Người dùng chưa vượt quá số lần xin cấp lại mật khẩu tối đa

## Quản lý hồ sơ

### US-04: Xem thông tin cá nhân

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn xem thông tin tài khoản cá nhân của mình trên hệ thống của app

**Acceptance Criteria nguồn**

- 1. Trang "Tài khoản" phải có 2 tabs "Cá nhân" và "Kinh Doanh", trong đó tab "Cá nhân" hiển thị các thông tin như tên người dùng, email, SĐT, avatar, số phòng và tên nhà trọ hiện đang thuê (nếu có), nút "Sửa" và nút "Đổi mật khẩu"
- 2. Thông tin SĐT chỉ được hiển thị 3 số cuối
- 3. Hệ thống phải chuyển người dùng tới trang "Sửa thông tin cá nhân" ngay khi người dùng bấm nút "Sửa" trên trang "Tài khoản", tab "Cá nhân"
- 4. Hệ thống phải chuyển người dùng tới trang "Đổi mật khẩu" ngay khi người dùng bấm nút "Đổi mật khẩu" trên trang "Tài khoản", tab "Cá nhân"
- 5. Hệ thống phải chuyển người dùng tới tab "Kinh Doanh" ngay khi người dùng bấm tab "Kinh Doanh" trên trang "Tài khoản"

### US-05: Cập nhật thông tin cá nhân

- **Priority:** High
- **User Story:** Là một người dùng đã đăng ký tài khoản, tôi muốn cập nhật thông tin tài khoản cá nhân của mình trên hệ thống của app để thuận lợi cho quá trình cho thuê phòng trọ

**Acceptance Criteria nguồn**

- 1. Trang "Sửa thông tin cá nhân" hiển thị các input để người dùng chỉnh sửa các thông tin như tên người dùng, email và image picker cho trường avatar. Trường SĐT không được thay đổi
- 2. Người dùng cần đợi 1h kể từ lần thay đổi thông tin tài khoản cá nhân trước đó để có thể thay đổi tiếp
- 3. Hệ thống phải chuyển người dùng về trang "Tài khoản", tab "Cá nhân" trong vòng 2s sau khi người dùng bấm nút "Xác nhận"

### US-06: Xem thông tin kinh doanh

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn xem thông tin tài khoản kinh doanh của mình trên hệ thống của app
- Living spec hiện hành: [UC-06](../../docs/use-cases/smartchu/UC-06-view-business-information.md)
- Chính sách liên quan: [Xác minh kinh doanh SmartChủ](../../docs/11-smartchu-business-verification-policy.md)

**Acceptance Criteria nguồn**

- 1. Trang "Tài khoản", tab "Kinh Doanh" hiển thị các thông tin chung như mã số thuế, ...
- 2. Hệ thống phải chuyển người dùng tới trang "Sửa thông tin kinh doanh" ngay khi người dùng bấm nút "Sửa" trên trang "Tài khoản", tab "Kinh Doanh"

### US-07: Cập nhật thông tin kinh doanh

- **Priority:** High
- **User Story:** Là một người dùng đã đăng ký tài khoản, tôi muốn cập nhật thông tin tài khoản kinh doanh của mình trên hệ thống của app để thuận lợi cho quá trình cho thuê phòng trọ
- Living spec hiện hành: [UC-07](../../docs/use-cases/smartchu/UC-07-submit-business-verification.md)
- Chính sách liên quan: [Xác minh kinh doanh SmartChủ](../../docs/11-smartchu-business-verification-policy.md)

**Acceptance Criteria nguồn**

- 1. Trang "Sửa thông tin kinh doanh" hiển thị các input để người dùng chỉnh sửa các thông tin như mã số thuế, ... và image picker để gửi lên ảnh tài liệu bản gốc hoặc photo có công chứng (sổ đỏ)
- 2. Người dùng cần đợi 1h kể từ lần thay đổi thông tin tài khoản kinh doanh trước đó để có thể thay đổi tiếp. Mỗi tuần người dùng chỉ có thể thay đổi thông tin kinh doanh của mình 3 lần
- 3. Hệ thống phải chuyển người dùng về trang "Tài khoản", tab "Kinh Doanh" trong vòng 2s sau khi người dùng bấm nút "Xác nhận"

### US-08: Đổi mật khẩu

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn đổi mật khẩu của mình để tăng tính bảo mật

**Acceptance Criteria nguồn**

- 1. Trang "Đổi mật khẩu" bao gồm các input cho mật khẩu hiện tại, mật khẩu mới và xác nhận mật khẩu mới, nút "Lưu" và nút "Huỷ"
- 2.Mật khẩu mới phải chứa tối thiểu 8 ký tự, gồm ít nhất 1 chữ hoa, 1 số và 1 ký tự đặc biệt
- 3. Người dùng chỉ được đổi mật khẩu mỗi ngày 1 lần

## Quản lý hợp đồng điện tử

### US-09: Xem danh sách hợp đồng điện tử

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn xem danh sách hợp đồng cho thuê phòng trọ của tôi (hợp đồng điện tử) để dễ quản lý thông tin người thuê phòng trọ

**Acceptance Criteria nguồn**

- 1. Trang "Hợp đồng" hiển thị danh sách các hợp đồng điện tử của người dùng, được chia theo các tabs Tất Cả, Chưa Ký, Đã Ký, Đã Hoàn Thành, Chờ Huỷ, Đã Huỷ
- 2. Thời gian load ra màn hình "Hợp đồng" theo các tabs giới hạn dưới 2s, có áp dụng lazy loading để đảm bảo hiệu suất

### US-10: Tạo hợp đồng điện tử

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn tạo hợp đồng điện tử để khởi tạo thủ tục cho thuê phòng trọ
- Living spec hiện hành: [UC-10](../../docs/use-cases/smartchu/UC-10-create-electronic-contract.md)
- Chính sách liên quan: [Xác minh kinh doanh SmartChủ](../../docs/11-smartchu-business-verification-policy.md)

**Acceptance Criteria nguồn**

- 1. Sau khi bấm nút "Tạo hợp đồng" trên trang "Hợp đồng", trang "Tạo hợp đồng" phải được hiển thị ngay lập tức
- 2. Tất cả thông tin của bên A, bên B và những điều khoản giữa 2 bên là bắt buộc, không được để trống
- 3. Các phản hồi của hệ thống trong luồng phải được hoàn thành dưới 3s

### US-11: Ký hợp đồng điện tử

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn ký hợp đồng điện tử để hoàn tất thủ tục cho thuê phòng trọ của bên người cho thuê trọ

**Acceptance Criteria nguồn**

- 1. Trang "Hợp đồng điện tử" có đầy đủ thông tin như 1 hợp đồng bản cứng, trong đó các phần để người dùng ký sẽ có nút "Ký tại đây"
- 2. Sau khi người dùng bấm nút "Ký tại đây", hiển thị pop-up "Chữ ký điện tử", người dùng có thể thực hiện ký lại cho tới khi bấm nút "Lưu"
- 3. Mỗi phòng chỉ được thuê cùng lúc bởi tối đa 2 người
- 4. Các phản hồi của hệ thống trong luồng phải được hoàn thành dưới 3s

### US-12: Cập nhật hợp đồng điện tử

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn cập nhật hợp đồng điện tử do có nhu cầu muốn thay đổi nội dung hợp đồng

**Acceptance Criteria nguồn**

- 1. Người dùng chỉ có thể thực hiện cập nhật với các hợp đồng chưa có chữ ký của bên thuê (người thuê)
- 2. Các phản hồi của hệ thống trong luồng phải được hoàn thành dưới 3s

### US-13: Xét duyệt yêu cầu huỷ hợp đồng điện tử

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn xét duyệt các yêu cầu huỷ hợp đồng cho thuê khi người thuê trọ muốn thay đổi phòng trọ

**Acceptance Criteria nguồn**

- 1. Truy cập chức năng xét duyệt bằng cách xem chi tiết các hợp đồng trong tab "Chờ duyệt"
- 2. Các hợp đồng được duyệt sẽ được chuyển về trạng thái "Đã huỷ", các hợp đồng bị từ chối yêu cầu huỷ sẽ được chuyển về trạng thái "Đã hoàn thành"
- 3. Người thuê cần được gửi thông báo về tình trạng của yêu cầu xét duyệt huỷ hợp đồng bất kể tình trạng
- 4. Các phản hồi của hệ thống trong luồng phải được hoàn thành dưới 3s

### US-14: Xoá hợp đồng điện tử

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn xoá nhũng hợp đồng điện tử tạo lỗi hoặc không còn khả năng để dùng (người thuê không thuê, phòng có sự cố bất ngờ cần đưa vào trạng thái bảo trì,...)

**Acceptance Criteria nguồn**

- 1. Chỉ được xoá với các hợp đồng trong trạng thái "Chưa ký" hoặc "Đã ký"
- 2. Người dùng không thể tìm lại các hợp đồng bị xoá
- 3. Các phản hồi của hệ thống trong luồng phải được hoàn thành dưới 3s

### US-15: Chia sẻ hợp đồng điện tử

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn chia sẻ hợp đồng điện tử tới người thuê trọ để giúp họ ký và hoàn tất hợp đồng với bên người thuê trọ

**Acceptance Criteria nguồn**

- 1. Chỉ được chia sẻ các hợp đồng ở trạng thái "Đã ký"
- 2. Các phản hồi của hệ thống trong luồng phải được hoàn thành dưới 2s

## Quản lý nhà trọ

### US-16: Xem danh sách nhà trọ

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn xem danh sách các nhà trọ của mình để có thể quản lý và theo dõi tổng quan tài sản cho thuê

**Acceptance Criteria nguồn**

- 1. Trang "Toà nhà" hiển thị danh sách các nhà trọ người dùng quản lý (Sắp xếp theo lần chỉnh sửa gần nhất theo trạng thái)
- 2. Người dùng có thể tìm kiếm toà nhà theo tên

### US-17: Xem chi tiết nhà trọ

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn xem thông tin chi tiết của từng nhà trọ của mình để nắm rõ tình hình từng tài sản

**Acceptance Criteria nguồn**

- 1. Trang chi tiết nhà trọ hiển thị các thông tin mà người dùng đã lưu cho nhà trọ
- 2. Thời gian load trang chi tiết nhà trọ yêu cầu dưới 1s

### US-18: Tạo nhà trọ

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn tạo thông tin về nhà trọ của mình (tên, địa chỉ, mô tả,...) để có thể quản lý tài sản cho thuê của mình
- Living spec hiện hành: [UC-18](../../docs/use-cases/smartchu/UC-18-create-property.md)
- Chính sách liên quan: [Xác minh kinh doanh SmartChủ](../../docs/11-smartchu-business-verification-policy.md)

**Acceptance Criteria nguồn**

- 1. Một số thông tin bắt buộc người dùng tạo nhà trọ là: Tên nhà trọ, số tầng, mô tả, địa chỉ, tỉnh/thành phố, phường/xã, giá tiền 1 số điện, giá tiền 1 khối nước.
- 2. Thời gian load giữa các thao tác call API yêu cầu dưới 1s

### US-19: Cập nhật thông tin nhà trọ

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn cập nhật thông tin của nhà trọ của mình (tên, địa chỉ, mô tả,...) để sửa lại thông tin và tình trạng của nhà trọ cho đúng với hiện trạng

**Acceptance Criteria nguồn**

- 1. Các tầng phải được deactive trước khi muốn giảm số tầng
- 2. Tất cả các phòng phải được deactive trước khi muốn deactive toà nhà
- 3. Thời gian load giữa các thao tác call API yêu cầu dưới 1s

### US-20: Xem danh sách phòng trọ (Của 1 nhà trọ)

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn xem danh sách các phòng trọ trong một nhà trọ cụ thể để quản lý tình trạng từng phòng

**Acceptance Criteria nguồn**

- 1. Trang danh sách phòng trọ hiển thị danh sách các phòng trọ được chia theo các tầng
- 2. Người dùng có thể tìm kiếm phòng trọ theo tên

### US-21: Xem chi tiết phòng trọ

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn xem thông tin chi tiết của từng phòng (diện tích, giá thuê, tình trạng, thông tin khách thuê hiện tại) để theo dõi và đưa ra quyết định quản lý

**Acceptance Criteria nguồn**

- 1. Trang chi tiết phòng trọ bao gồm 2 tabs "Thông tin chung" và "Người thuê"
- 2. Thời gian load giữa các thao tác call API yêu cầu dưới 1s

### US-22: Tạo phòng trọ

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn thêm các phòng trọ vào nhà trọ đã tạo (số phòng, diện tích, giá thuê) để có thể cho khách thuê
- Living spec hiện hành: [UC-22](../../docs/use-cases/smartchu/UC-22-create-room.md)
- Chính sách liên quan: [Xác minh kinh doanh SmartChủ](../../docs/11-smartchu-business-verification-policy.md)

**Acceptance Criteria nguồn**

- 1. Bắt buộc phải có hình ảnh của phòng trọ đi kèm
- 2. Mỗi nhà trọ có 1 tên phòng duy nhất
- 3. Thời gian load giữa các thao tác call API yêu cầu dưới 2s

### US-23: Cập nhật phòng trọ

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn cập nhật thông tin của phòng trọ thuộc nhà trọ của mình để sửa lại thông tin và tình trạng của phòng trọ cho đúng với hiện trạng

**Acceptance Criteria nguồn**

- 1. Mỗi nhà trọ có 1 tên phòng duy nhất
- 2. Thời gian phản hồi các thao tác trong luồng yêu cầu dưới 2s

### US-24: Xem lịch sử thuê phòng

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn xem lịch sử thuê phòng để đánh giá được tần suất được thuê của một phòng và thị hiếu thuê phòng của người thuê

**Acceptance Criteria nguồn**

- 1. Lịch sử thuê phòng hiển thị trên modal
- 2. Lịch sử thuê phòng hiển thị sắp xếp theo thứ tự hợp đồng mới nhất được ký
- 3. Thời gian phản hồi các thao tác trong luồng yêu cầu dưới 1s

## Tương tác

### US-25: Xem yêu cầu xem trọ

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn xem yêu cầu xem trọ để biết có những ai muốn xem phòng trọ nào và vào thời gian nào

**Acceptance Criteria nguồn**

- 1. Trên trang "Yêu cầu xem phòng", danh sách lịch xem được hiển thị sắp xếp theo thứ tự cũ dần
- 2. Mỗi yêu cầu gồm SĐT, số phòng, tên trọ và 2 lựa chọn (duyệt/từ chối)
- 3. Thời gian xử lý trong các thao tác yêu cầu dưới 1s

### US-26: Phản hồi yêu cầu

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn phản hồi yêu cầu xem trọ của người thuê để thông báo cho họ biết liệu họ có thể tới xem phòng trọ không

**Acceptance Criteria nguồn**

- 1. Các yêu cầu đã được xét duyệt sẽ không hiển thị trên màn hình "Yêu cầu xem phòng"
- 2. Thời gian xử lý trong các thao tác yêu cầu dưới 1s

### US-27: Quản lý lịch hẹn

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn xem các yêu cầu xem trọ được phân bổ trên giao diện lịch để có cái nhìn trực quan về các lịch hẹn và có thể sắp xếp lịch hẹn dễ dàng

**Acceptance Criteria nguồn**

- 1. Trang "Lịch xem phòng" phân bổ các yêu cầu xem trên từng khung giờ
- 2. Có thể xem lịch theo ngày, tuần, tháng
- 3. Thời gian xử lý trong các thao tác yêu cầu dưới 1s

### US-28: Xem đánh giá và bình luận

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn xem các đánh giá và bình luận của người thuê về phòng trọ để biết cảm nhận của người thuê về dịch vụ phòng trọ của mình

**Acceptance Criteria nguồn**

- 1. Người dùng có thể xem đánh giá và bình luận về phòng trọ ngay tại trang "Chi tiết phòng trọ"
- 2. Thời gian xử lý trong các thao tác yêu cầu dưới 1s

### US-29: Trả lời đánh giá và bình luận

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn trả lời các đánh giá và bình luận để cảm ơn người thuê đã quan tâm trọ cũng như giải đáp các thắc mắc hoặc hiểu lầm về trọ

**Acceptance Criteria nguồn**

- 1. Người dùng trả lời đánh giá và bình luận ngay bên dưới bình luận của người thuê
- 2. Người dùng có thể báo cáo bình luận cho quản trị viên nếu đánh giá và bình luận vi phạm quy tắc cộng đồng của nền tảng
- 3. Thời gian xử lý các thao tác yêu cầu dưới 1s

### US-30: Nhắn tin với người thuê

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn nhắn tin riêng với người thuê để dễ dàng trong việc giao tiếp và hỗ trợ người thuê tốt hơn

**Acceptance Criteria nguồn**

- 1. Trang "Tin nhắn" hiển thị danh sách các người thuê mà người dùng đã liên lạc
- 2. Cuộc hội thoại mới sẽ được khởi tạo khi người dùng và người thuê ký hợp đồng lần đầu tiên
- 3. Thời gian xử lý các thao tác yêu cầu dưới dưới 2s (Chưa bao gồm cả việc gửi hình ảnh và video)

### US-31: Thống kê hoạt động

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn xem thống kê các hoạt động, tương tác của người thuê với phòng trọ và nhà trọ của mình, để từ đó đưa ra các chiến lược marketing cần thiết cho nhà trọ của mình

**Acceptance Criteria nguồn**

- 1. Màn hình thống kê có filter theo thời gian trong vòng 90 ngày (Khoảng cách từ ngày bắt đầu đến ngày kết thúc)
- 2. Hiển thị đủ key metrics và charts cho Lượt xem, Lượt đánh giá, Lượt báo cáo, Lượt tương tác, Lượt tiếp cận
- 3. Thời gian xử lý trong các thao tác yêu cầu dưới 2s

## Quản lý sự cố

### US-32: Xem danh sách báo cáo sự cố

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn xem danh sách các báo cáo sự cố về nhà trọ của tôi để nắm được nhà trọ của tôi đang có sự cố gì

**Acceptance Criteria nguồn**

- 1. Danh sách báo cáo sự cố có filter theo loại trang thiết bị và độ nghiêm trọng
- 2. Thời gian xử lý các thao tác trong luồng yêu cầu dưới 1s

### US-33: Chi tiết báo cáo sự cố

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn xem chi tiết báo cáo sự cố để biết thêm những thông tin về sự cố như độ nghiêm trọng cũng như chú thích của người thuê

**Acceptance Criteria nguồn**

- 1. Màn hình "Chi tiết báo cáo sự cố" hiển thị Tên sự cố, Loại trang thiết bị gặp sự cố, Độ nghiêm trọng, Hạn sửa chữa, Tiến độ và Chú thích
- 2. Người dùng có thể mở modal "Cập nhật tiến độ" trên màn hình "Chi tiết báo cáo sự cố"

### US-34: Lập kế hoạch sửa chữa

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn lập kế hoạch sửa chữa để xác định và phân bổ thời gian sửa chữa sự cố sao cho hợp lý

**Acceptance Criteria nguồn**

- 1. Người dùng chỉ được chọn thời hạn sửa chữa trong khoảng thời gian cho phép phụ thuộc vào độ nghiêm trọng
- 2. Thời gian xử lý các thao tác trong luồng yêu cầu dưới 1s

### US-35: Cập nhật tiến độ

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn cập nhật tiến độ sửa chữa để người thuê biết được sự cố của mình đang được sửa chữa tới đâu

**Acceptance Criteria nguồn**

- 1. Khi người dùng cập nhật tiến độ thành 100%, sẽ có thông báo tới người thuê rằng sự cố đã được sửa chữa
- 2. Thời gian xử lý các thao tác trong luồng yêu cầu dưới 1s

### US-36: Ghi nhận chi phí phát sinh

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn ghi nhận chi phí phát sinh với những sự cố do người thuê gây ra để người thuê có thể thanh toán sau trong lần đóng tiền trọ sắp tới

**Acceptance Criteria nguồn**

- 1. Người dùng có thể thêm chi phí phát sinh vào sự cố sau khi hoàn thành sửa chữa (Tiến độ = 100%)
- 2. Thời gian xử lý các thao tác trong luồng yêu cầu dưới 1s

### US-37: Theo dõi các sự cố thường gặp

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn theo dõi các sự cố thường gặp để đưa ra những kế hoạch sửa chữa hợp lý

**Acceptance Criteria nguồn**

- 1. Hệ thống sẽ hiển thị 5 sự cố hay gặp nhất trong nhà trọ
- 2. Thời gian xử lý các thao tác trong luồng yêu cầu dưới 1s

### US-38: Xem kế hoạch bảo trì định kỳ

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn xem kế hoạch bảo trì định kỳ để nắm được lịch bảo trì cho phòng trọ cũng như toàn thể nhà trọ của mình

**Acceptance Criteria nguồn**

- 1. Hệ thống tự tính toán và đưa ra 1 danh sách các phòng cần bảo trì
- 2. Thời gian xử lý các thao tác trong luồng yêu cầu dưới 1s

### US-39: Cập nhật kế hoạch bảo trì định kỳ

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn cập nhật kế hoạch bảo trì định kỳ để đặt lại lịch bảo trì phù hợp với thời gian của bản thân và người thuê

**Acceptance Criteria nguồn**

- 1. Người dùng chỉ có thể thay đổi thời gian bảo trì trong vòng 30 ngày so với ngày ban đầu mà hệ thống tính toán
- 2. Thời gian xử lý các thao tác trong luồng yêu cầu dưới 1s

## Quản lý thanh toán

### US-40: Liên kết ngân hàng/ví điện tử

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn liên kết ngân hàng/ví điện tử vào tài khoản SmartChủ để bước đầu thiết lập công cụ giúp hỗ trợ quản lý nguồn thu hàng tháng từ việc cho thuê trọ

**Acceptance Criteria nguồn**

- 1. Hệ thống có hỗ trợ liên kết với các ngân hàng phổ biến tại Việt Nam, Visa Card, Mastercard, Paypal và ví điện tử MOMO
- 2. Người dùng cần liên kết ngân hàng/ví điện tử trước khi sử dụng bất kì tính năng nào khác trên trang "Thanh toán"
- 3. Hệ thống phải xác thực tài khoản ngân hàng và ví điện tử trước khi hoàn tất việc liên kết
- 4. Hệ thống phải xác thực tài khoản ngân hàng và ví điện tử trong vòng 3s

### US-41: Thiết lập khoản thu

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn thiết lập khoản thu chi phí thuê nhà trọ của người thuê để tiết kiệm thời gian quản lý

**Acceptance Criteria nguồn**

- 1. Hiển thị tổng nợ phí cần được thanh toán tại trang "Thanh toán"
- 2. Hiển thị màn hình danh sách nợ phí theo từng phòng trọ khi bấm vào tổng nợ phí cần được thanh toán
- 3. Người dùng có thể gửi thông báo nhắc nhở thủ công hoặc tự động tới những người thuê này
- 4. Thời gian xử lý các thao tác trong luồng yêu cầu dưới 3s

### US-42: Gửi nhắc nhở tự động

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn đặt lịch gửi nhắc nhở tự động về việc thanh toán để nhắc nhở người thuê về hạn nộp tiền trọ

**Acceptance Criteria nguồn**

- 1. Người dùng chọn lịch gửi nhắc nhở phải là ngày tương lai, không được chọn ngày quá khứ. Người dùng chọn vòng lặp mong muốn (Mỗi tháng, mỗi quý, mỗi 6 tháng, mỗi 1 năm)
- 2. Người dùng cần phải liên kết ngân hàng/ví điện tử trước đó
- 3. Thời gian xử lý các thao tác trong luồng yêu cầu dưới 3s

### US-43: Gửi thông báo thanh toán

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn gửi thông báo thanh toán để nhắc nhở thêm người thuê về thời điểm có thể bắt đầu nộp tiền trọ của tháng

**Acceptance Criteria nguồn**

- 1. Người thuê chưa đóng tiền trọ sẽ nhận được thông báo thanh toán tiền trọ hàng ngày từ lúc chốt số điện nước và lên bill tiền trọ của tháng
- 2. Người dùng có thể chọn tắt tính năng "Gửi thông báo thanh toán" bất cứ lúc nào

### US-44: Xem lịch sử thanh toán

- **Priority:** High
- **User Story:** Là một người dùng, tôi muốn xem lịch sử thanh toán tiền trọ để biết tình trạng các giao dịch với người thuê

**Acceptance Criteria nguồn**

- 1. Trang "Lịch sử thanh toán" hiển thị tất cả các giao dịch tiền trọ của người thuê cho người dùng và được xếp theo thứ tự cũ dần
- 2. Người dùng có thể chọn xem chi tiết giao dịch, trong màn hình "Chi tiết giao dịch" có chức năng "Xuất hoá đơn điện tử"

### US-45: Xuất hóa đơn điện tử

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn xuất hóa đơn điện tử để cung cấp cho người thuê tài liệu thanh toán tuân thủ và hợp lý hoá quy trình kế toán và nộp thuế của bản thân

**Acceptance Criteria nguồn**

- 1. Lịch sử thanh toán của người dùng phải có dữ liệu để xuất được hoá đơn
- 2. Hoá đơn sau khi được xuất phải được gửi trực tiếp đến email của người thuê
- 3. Hoá đơn đáp ứng các tiêu chuẩn định dạng hoá đơn điện tử hợp pháp và có thể được tải lên cổng thông tin của cơ quan thuế mà không cần chỉnh sửa

### US-46: Thống kê doanh thu

- **Priority:** Medium
- **User Story:** Là một người dùng, tôi muốn thống kê doanh thu để nắm được tình trạng dòng tiền vào ví khi kinh doanh cho thuê phòng trọ

**Acceptance Criteria nguồn**

- 1. Doanh thu được thống kê từ dữ liệu thanh toán tiền trọ, sửa chữa sự cố, tiền nước, tiền điện,...
- 2. Các thống kê sẽ có các key metrics kèm theo charts riêng biệt
- 3. Có thể filter dữ liệu theo thời gian (1 tháng, 3 tháng, 6 tháng, 1 năm)
