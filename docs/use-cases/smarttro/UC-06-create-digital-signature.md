# SmartTrọ — UC-06 Tạo mới chữ ký điện tử

## 1. Trạng thái tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | **Draft — chờ PO review/chốt các câu hỏi mở** |
| Ngày lập | 2026-09-24 |
| Nguồn chính | `Activity_Diagrams/AD_Profile Management (Create Digital Signature).png` |
| Phạm vi | Tạo và lưu mẫu chữ ký điện tử của người thuê trong khu vực Tài khoản |
| Bàn giao | **Chưa Ready cho PM/Dev/QA** cho tới khi các quyết định tại mục 8 được chốt |

Tài liệu này được suy ra trực tiếp từ Activity Diagram đã có. Các bước và nhánh được diagram thể hiện được coi là bằng chứng nguồn; nội dung tại mục 8 chỉ là câu hỏi/đề xuất, chưa phải requirement đã duyệt.

## 2. Mục tiêu và giá trị nghiệp vụ

Là **người thuê đã có tài khoản SmartTrọ**, tôi muốn tạo và lưu mẫu chữ ký điện tử của mình để có thể sử dụng mẫu chữ ký đó trong các nghiệp vụ điện tử được hệ thống hỗ trợ sau này.

UC này chỉ tạo mẫu chữ ký trong hồ sơ người dùng. Việc áp chữ ký vào hợp đồng, xác nhận ý chí ký hợp đồng và giá trị pháp lý của chữ ký thuộc UC ký hợp đồng hoặc requirement pháp lý riêng; không được tự động thực hiện khi UC-06 hoàn tất.

## 3. Nguồn và traceability

### 3.1. Activity Diagram

![UC-06 — Tạo chữ ký điện tử](../../../Activity_Diagrams/AD_Profile%20Management%20%28Create%20Digital%20Signature%29.png)

Diagram xác nhận các hành vi sau:

- Người dùng có thể bắt đầu khi đã đăng nhập hoặc được yêu cầu đăng nhập trước.
- Luồng điều hướng: `Trang chủ` → `Tài khoản` → tab `Chữ ký điện tử` → `Tạo chữ ký điện tử`.
- Hệ thống hiển thị pop-up/khu vực ký.
- Người dùng có thể chọn `Ký lại` để xóa/thay bản ký nháp và thực hiện lại.
- Chữ ký chỉ được lưu khi người dùng chọn `Lưu`.

### 3.2. Quan hệ với SRS

- Catalogue trong SRS gốc có `UC-6 — Tạo mới chữ ký điện tử` nhưng không có bảng đặc tả tương ứng.
- File này là living draft bổ sung từ diagram, không phải nội dung đã tồn tại trong DOCX nguồn.
- Sau khi PO duyệt, BA cần đưa đặc tả đã chốt trở lại SRS nguồn và chạy lại bộ chuyển đổi Markdown.

## 4. Đặc tả Use Case

| Nội dung | Mô tả |
| --- | --- |
| Use Case ID | UC-06 |
| Use Case Name | Tạo mới chữ ký điện tử |
| Description | Cho phép người thuê tạo và lưu mẫu chữ ký điện tử trong hồ sơ SmartTrọ. |
| Actor(s) | Người thuê (Renter) |
| Related Use Case | UC-02 — Đăng nhập; UC-07 — Cập nhật chữ ký điện tử; UC ký hợp đồng điện tử theo catalogue SRS |
| Priority | Chưa được xác định trong diagram/SRS; cần PO chốt |
| Trigger | Người dùng chọn `Tạo chữ ký điện tử` trong tab `Chữ ký điện tử` của màn Tài khoản. |
| Precondition | Thiết bị có thể truy cập SmartTrọ; người dùng có tài khoản và đăng nhập thành công trước khi tạo chữ ký. |
| Post-condition thành công | Mẫu chữ ký được lưu và liên kết với đúng tài khoản người thuê. |
| Post-condition không thành công | Không tạo hoặc ghi đè mẫu chữ ký khi người dùng chưa chọn `Lưu` hoặc thao tác lưu thất bại. |

## 5. Luồng nghiệp vụ

### 5.1. Basic Flow

1. Người dùng mở ứng dụng SmartTrọ.
2. Hệ thống kiểm tra trạng thái đăng nhập.
3. Nếu người dùng chưa đăng nhập, người dùng thực hiện đăng nhập; sau khi thành công, hệ thống hiển thị màn Trang chủ.
4. Người dùng chọn `Tài khoản`.
5. Hệ thống hiển thị màn Tài khoản.
6. Người dùng chọn tab `Chữ ký điện tử`.
7. Hệ thống hiển thị màn Chữ ký điện tử.
8. Người dùng chọn `Tạo chữ ký điện tử`.
9. Hệ thống hiển thị pop-up/khu vực ký chữ ký điện tử.
10. Người dùng ký trong khu vực ký.
11. Người dùng chọn `Lưu`.
12. Hệ thống lưu thông tin mẫu chữ ký điện tử vừa tạo vào đúng tài khoản người dùng.
13. Use Case kết thúc thành công.

### 5.2. Alternative Flow

#### AF-06-01 — Đăng nhập trước khi tạo chữ ký

1. Tại bước 2, nếu người dùng chưa đăng nhập, hệ thống điều hướng tới luồng đăng nhập.
2. Người dùng đăng nhập thành công.
3. Luồng tiếp tục tại bước 3 của Basic Flow.

#### AF-06-02 — Ký lại trước khi lưu

1. Sau bước 10, người dùng chọn `Ký lại` thay vì `Lưu`.
2. Hệ thống đưa người dùng trở lại khu vực ký để thực hiện một mẫu chữ ký mới.
3. Luồng tiếp tục tại bước 10 của Basic Flow; bản ký nháp trước đó không được lưu làm mẫu chính thức.

### 5.3. Exception Flow

Activity Diagram chưa mô tả các nhánh chữ ký rỗng, mất mạng, lưu thất bại, hết phiên đăng nhập hoặc lỗi đồng bộ. PM không được giao Dev tự quyết các behavior này; cần chốt tại mục 8 trước khi triển khai.

## 6. Business Rules xác nhận được từ diagram

| ID | Business Rule | Nguồn |
| --- | --- | --- |
| `SIG-CREATE-BR01` | Chỉ tài khoản đã đăng nhập mới được lưu mẫu chữ ký. | Nhánh kiểm tra đăng nhập |
| `SIG-CREATE-BR02` | Mẫu chữ ký được tạo bằng thao tác ký trong khu vực ký do hệ thống hiển thị. | Bước ký trong pop-up |
| `SIG-CREATE-BR03` | Người dùng có thể ký lại nhiều lần trước khi chọn mẫu cuối cùng để lưu. | Nhánh `Ký lại` |
| `SIG-CREATE-BR04` | Hệ thống chỉ ghi nhận mẫu chữ ký khi người dùng chủ động chọn `Lưu`; không auto-save bản ký nháp. | Nhánh `Lưu` |
| `SIG-CREATE-BR05` | Hoàn tất UC-06 không đồng nghĩa với việc ký một hợp đồng cụ thể. | Phạm vi diagram chỉ lưu chữ ký vào tài khoản |

## 7. Acceptance Criteria từ diagram

### AC-06-01 — Mở khu vực tạo chữ ký

- **Given** người thuê đã đăng nhập
- **When** người thuê mở `Tài khoản`, chọn tab `Chữ ký điện tử` và chọn `Tạo chữ ký điện tử`
- **Then** hệ thống hiển thị khu vực cho phép người dùng vẽ/ký mẫu chữ ký.

### AC-06-02 — Ký lại

- **Given** người dùng đã vẽ một bản ký nháp nhưng chưa lưu
- **When** người dùng chọn `Ký lại`
- **Then** hệ thống cho phép thực hiện lại chữ ký
- **And** bản ký nháp trước không được lưu làm mẫu chữ ký chính thức.

### AC-06-03 — Lưu mẫu chữ ký

- **Given** người dùng đã ký trong khu vực ký
- **When** người dùng chọn `Lưu`
- **Then** hệ thống lưu mẫu chữ ký vào đúng tài khoản người dùng
- **And** lần mở lại màn Chữ ký điện tử phải đọc được mẫu chữ ký đã lưu.

### AC-06-04 — Yêu cầu đăng nhập

- **Given** người dùng chưa đăng nhập
- **When** người dùng bắt đầu hành trình tạo chữ ký
- **Then** hệ thống yêu cầu hoàn tất đăng nhập trước khi cho phép lưu mẫu chữ ký.

## 8. Quyết định cần PO chốt trước khi bàn giao

| ID | Câu hỏi cần chốt | Đề xuất ban đầu | Trạng thái |
| --- | --- | --- | --- |
| `SIG-COMMON-D01` | Đây là mẫu chữ ký vẽ tay lưu trong app hay chữ ký số có chứng thư số/CA và giá trị pháp lý độc lập? | MVP coi đây là **mẫu chữ ký điện tử vẽ tay**, không gọi là chữ ký số PKI/CA và không tuyên bố giá trị pháp lý ngoài luồng ký hợp đồng được duyệt. | Pending |
| `SIG-COMMON-D02` | Có cho phép lưu khi khu vực ký đang trống hoặc chỉ có một nét/chấm không? | Không cho lưu chữ ký rỗng; ngưỡng hợp lệ tối thiểu cần Dev/QA có contract đo được. | Pending |
| `SIG-CREATE-D03` | Mỗi người dùng được có bao nhiêu mẫu chữ ký? | MVP chỉ có một mẫu hiện hành cho mỗi tài khoản; tạo mới chỉ khả dụng khi chưa có mẫu. | Pending |
| `SIG-CREATE-D04` | Định dạng, kích thước, nền và giới hạn dữ liệu chữ ký là gì? | Chuẩn hóa thành asset nền trong suốt, giới hạn kích thước và dung lượng ở backend; không lưu raw stroke vô hạn. | Pending |
| `SIG-CREATE-D05` | Khi lưu lỗi/mất mạng, UI xử lý thế nào? | Không báo thành công; giữ bản nháp trong memory của màn hiện tại để retry, không persist qua app restart. | Pending |
| `SIG-CREATE-D06` | Có cần audit và bảo vệ dữ liệu chữ ký không? | Ghi audit create/update/status change; mã hóa khi truyền và lưu; không đưa asset chữ ký vào log/analytics. | Pending |

## 9. Gate bàn giao

- PO duyệt `SIG-COMMON-D01`, `SIG-COMMON-D02` và `SIG-CREATE-D03` đến `SIG-CREATE-D06`.
- Figma có màn/tab Chữ ký điện tử, trạng thái chưa có chữ ký, pop-up/khu vực ký, loading/error/success và hành vi `Ký lại`.
- PM tạo task cha theo UC; FE dựng UI và deploy preview trước, sau đó mới triển khai BE, map API, QA và UAT.
- QA phải có bằng chứng cho navigation, login gate, ký lại, save success, save failure và không tự ký hợp đồng.
