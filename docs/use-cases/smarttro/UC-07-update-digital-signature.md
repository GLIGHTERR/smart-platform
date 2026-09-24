# SmartTrọ — UC-07 Cập nhật chữ ký điện tử

## 1. Trạng thái tài liệu

| Thuộc tính | Giá trị |
| --- | --- |
| Trạng thái | **Draft — chờ PO review/chốt các câu hỏi mở** |
| Ngày lập | 2026-09-24 |
| Nguồn chính | `Activity_Diagrams/AD_Profile Management (Update Digital Signature).png` |
| Phạm vi | Cập nhật mẫu chữ ký và/hoặc trạng thái của chữ ký điện tử đã có |
| Bàn giao | **Chưa Ready cho PM/Dev/QA** cho tới khi các quyết định tại mục 8 được chốt |

Tài liệu này được suy ra trực tiếp từ Activity Diagram đã có. Diagram cho phép thay đổi trạng thái và ký lại theo hai nhánh độc lập trước khi cập nhật; các behavior không xuất hiện trong diagram được giữ ở dạng câu hỏi mở.

## 2. Mục tiêu và giá trị nghiệp vụ

Là **người thuê đã có mẫu chữ ký điện tử**, tôi muốn cập nhật mẫu chữ ký hoặc trạng thái sử dụng của chữ ký để thông tin chữ ký trong tài khoản phản ánh lựa chọn hiện tại của tôi.

UC này không tự động thay đổi nội dung hoặc hiệu lực của các hợp đồng đã ký trước đó. Tác động của việc vô hiệu hóa/thay mẫu chữ ký tới hợp đồng cũ và hợp đồng mới phải được chốt riêng tại mục 8.

## 3. Nguồn và traceability

### 3.1. Activity Diagram

![UC-07 — Cập nhật chữ ký điện tử](../../../Activity_Diagrams/AD_Profile%20Management%20%28Update%20Digital%20Signature%29.png)

Diagram xác nhận các hành vi sau:

- Người dùng phải đăng nhập trước khi cập nhật.
- Luồng điều hướng: `Trang chủ` → `Tài khoản` → tab `Chữ ký điện tử`.
- Hệ thống kiểm tra người dùng đã có chữ ký hay chưa; nếu chưa có, luồng cập nhật kết thúc.
- Khi đã có chữ ký, người dùng chọn `Chỉnh sửa` và hệ thống hiển thị pop-up Chữ ký điện tử.
- Người dùng có thể thay đổi trạng thái, ký lại, thực hiện cả hai hoặc không thay đổi từng nhánh.
- Hệ thống chỉ lưu phiên bản cập nhật khi người dùng chọn `Cập nhật`.

### 3.2. Quan hệ với SRS

- Catalogue trong SRS gốc có `UC-7 — Cập nhật chữ ký điện tử` nhưng không có bảng đặc tả tương ứng.
- File này là living draft bổ sung từ diagram, không phải nội dung đã tồn tại trong DOCX nguồn.
- Sau khi PO duyệt, BA cần đưa đặc tả đã chốt trở lại SRS nguồn và chạy lại bộ chuyển đổi Markdown.

## 4. Đặc tả Use Case

| Nội dung | Mô tả |
| --- | --- |
| Use Case ID | UC-07 |
| Use Case Name | Cập nhật chữ ký điện tử |
| Description | Cho phép người thuê cập nhật mẫu chữ ký điện tử và/hoặc trạng thái sử dụng của chữ ký đã lưu. |
| Actor(s) | Người thuê (Renter) |
| Related Use Case | UC-02 — Đăng nhập; UC-06 — Tạo mới chữ ký điện tử; UC ký hợp đồng điện tử theo catalogue SRS |
| Priority | Chưa được xác định trong diagram/SRS; cần PO chốt |
| Trigger | Người dùng chọn `Chỉnh sửa` tại màn Chữ ký điện tử. |
| Precondition | Người dùng đăng nhập thành công; tài khoản có mẫu chữ ký điện tử đã lưu để cập nhật. |
| Post-condition thành công | Hệ thống lưu mẫu chữ ký và trạng thái mới nhất của đúng tài khoản; dữ liệu cũ chỉ bị thay thế sau khi cập nhật thành công. |
| Post-condition không thành công | Mẫu chữ ký và trạng thái hiện hành không thay đổi nếu người dùng chưa chọn `Cập nhật` hoặc thao tác lưu thất bại. |

## 5. Luồng nghiệp vụ

### 5.1. Basic Flow

1. Người dùng mở ứng dụng SmartTrọ.
2. Hệ thống kiểm tra trạng thái đăng nhập.
3. Nếu người dùng chưa đăng nhập, người dùng thực hiện đăng nhập; sau khi thành công, hệ thống hiển thị màn Trang chủ.
4. Người dùng chọn `Tài khoản`.
5. Hệ thống hiển thị màn Tài khoản.
6. Người dùng chọn tab `Chữ ký điện tử`.
7. Hệ thống hiển thị màn Chữ ký điện tử và kiểm tra tài khoản đã có mẫu chữ ký hay chưa.
8. Khi đã có chữ ký, người dùng chọn `Chỉnh sửa`.
9. Hệ thống hiển thị pop-up Chữ ký điện tử cùng mẫu và trạng thái hiện tại.
10. Người dùng thay đổi trạng thái, ký lại mẫu chữ ký hoặc thực hiện cả hai thao tác.
11. Người dùng chọn `Cập nhật`.
12. Hệ thống lưu mẫu chữ ký và trạng thái mới nhất của tài khoản.
13. Use Case kết thúc thành công.

### 5.2. Alternative Flow

#### AF-07-01 — Tài khoản chưa có chữ ký

1. Tại bước 7, hệ thống xác định tài khoản chưa có chữ ký.
2. Luồng cập nhật kết thúc theo đúng Activity Diagram.
3. Diagram chưa quy định có hiển thị CTA chuyển sang UC-06 hay không; behavior này chờ PO chốt.

#### AF-07-02 — Không thay đổi trạng thái

1. Tại bước 10, người dùng giữ nguyên trạng thái hiện tại.
2. Hệ thống không thay đổi trường trạng thái và tiếp tục xử lý nhánh chữ ký.

#### AF-07-03 — Không ký lại

1. Tại bước 10, người dùng giữ nguyên mẫu chữ ký hiện tại.
2. Hệ thống không thay đổi asset chữ ký và tiếp tục xử lý nhánh trạng thái.

#### AF-07-04 — Ký lại

1. Tại bước 10, người dùng chọn ký lại và ký trong khu vực ký.
2. Nếu người dùng tiếp tục chọn `Ký lại`, hệ thống đưa về khu vực ký để tạo bản nháp mới.
3. Khi người dùng chấp nhận bản ký mới, luồng tiếp tục tại bước 11 của Basic Flow.

#### AF-07-05 — Đăng nhập trước khi cập nhật

1. Tại bước 2, nếu người dùng chưa đăng nhập, hệ thống điều hướng tới luồng đăng nhập.
2. Người dùng đăng nhập thành công.
3. Luồng tiếp tục tại bước 3 của Basic Flow.

### 5.3. Exception Flow

Activity Diagram chưa mô tả các nhánh chữ ký mới không hợp lệ, cập nhật không có thay đổi, mất mạng, xung đột phiên bản, lưu thất bại hoặc hết phiên đăng nhập. Các behavior này phải được chốt tại mục 8 trước khi triển khai.

## 6. Business Rules xác nhận được từ diagram

| ID | Business Rule | Nguồn |
| --- | --- | --- |
| `SIG-UPDATE-BR01` | Chỉ tài khoản đã đăng nhập và đã có mẫu chữ ký mới đi vào luồng cập nhật. | Login gate + nhánh `Đã có chữ ký` |
| `SIG-UPDATE-BR02` | Thay đổi trạng thái và ký lại là hai lựa chọn độc lập trong cùng phiên chỉnh sửa. | Hai nhánh song song trong diagram |
| `SIG-UPDATE-BR03` | Người dùng có thể giữ nguyên một nhánh và chỉ cập nhật nhánh còn lại. | Nhánh `Không thay đổi trạng thái` / `Không ký lại` |
| `SIG-UPDATE-BR04` | Người dùng có thể ký lại nhiều lần trước khi chọn bản cuối. | Vòng lặp `Ký lại` |
| `SIG-UPDATE-BR05` | Dữ liệu chỉ được ghi nhận khi người dùng chọn `Cập nhật`; mở pop-up hoặc tạo bản nháp không tự ghi đè dữ liệu hiện hành. | Bước `Cập nhật` → lưu dữ liệu |

## 7. Acceptance Criteria từ diagram

### AC-07-01 — Chỉ sửa chữ ký đã tồn tại

- **Given** người thuê đã đăng nhập và có mẫu chữ ký
- **When** người thuê mở tab `Chữ ký điện tử` và chọn `Chỉnh sửa`
- **Then** hệ thống hiển thị mẫu chữ ký và trạng thái hiện tại trong giao diện chỉnh sửa.

### AC-07-02 — Cập nhật trạng thái độc lập

- **Given** giao diện chỉnh sửa đang hiển thị chữ ký hiện tại
- **When** người dùng chỉ thay đổi trạng thái rồi chọn `Cập nhật`
- **Then** hệ thống lưu trạng thái mới
- **And** giữ nguyên asset chữ ký hiện tại.

### AC-07-03 — Ký lại độc lập

- **Given** giao diện chỉnh sửa đang hiển thị chữ ký hiện tại
- **When** người dùng ký lại, giữ nguyên trạng thái và chọn `Cập nhật`
- **Then** hệ thống lưu mẫu chữ ký mới
- **And** giữ nguyên trạng thái hiện tại.

### AC-07-04 — Cập nhật đồng thời

- **Given** giao diện chỉnh sửa đang hiển thị chữ ký hiện tại
- **When** người dùng vừa thay đổi trạng thái vừa ký lại rồi chọn `Cập nhật`
- **Then** hệ thống lưu cả trạng thái và mẫu chữ ký mới trong cùng một kết quả cập nhật.

### AC-07-05 — Tài khoản chưa có chữ ký

- **Given** người dùng đã đăng nhập nhưng chưa có mẫu chữ ký
- **When** người dùng mở tab `Chữ ký điện tử`
- **Then** hệ thống không cho phép thực hiện thao tác cập nhật
- **And** không tự tạo một mẫu chữ ký rỗng.

## 8. Quyết định cần PO chốt trước khi bàn giao

| ID | Câu hỏi cần chốt | Đề xuất ban đầu | Trạng thái |
| --- | --- | --- | --- |
| `SIG-COMMON-D01` | Đây là mẫu chữ ký vẽ tay lưu trong app hay chữ ký số có chứng thư số/CA và giá trị pháp lý độc lập? | MVP coi đây là **mẫu chữ ký điện tử vẽ tay**, không gọi là chữ ký số PKI/CA và không tuyên bố giá trị pháp lý ngoài luồng ký hợp đồng được duyệt. | Pending |
| `SIG-COMMON-D02` | Có cho phép cập nhật bằng chữ ký rỗng hoặc bản ký chỉ có một nét/chấm không? | Không cho lưu chữ ký rỗng; dùng cùng validation đã chốt cho UC-06. | Pending |
| `SIG-UPDATE-D03` | “Trạng thái” gồm những giá trị nào, mặc định là gì và tác động thế nào? | MVP dùng `active/inactive`; chỉ chữ ký active được đề xuất trong luồng ký mới. | Pending |
| `SIG-UPDATE-D04` | Vô hiệu hóa hoặc thay mẫu chữ ký có ảnh hưởng hợp đồng đã ký không? | Không làm thay đổi hợp đồng/chữ ký snapshot đã hoàn tất; chỉ ảnh hưởng giao dịch ký mới. | Pending |
| `SIG-UPDATE-D05` | Khi tài khoản chưa có chữ ký, chỉ kết thúc như diagram hay hiển thị CTA sang UC-06? | Hiển thị empty state và CTA `Tạo chữ ký điện tử` dẫn sang UC-06. | Pending |
| `SIG-UPDATE-D06` | Nếu người dùng không đổi trạng thái lẫn chữ ký rồi bấm `Cập nhật`, hệ thống làm gì? | Disable `Cập nhật` khi không có thay đổi; không gửi request no-op. | Pending |
| `SIG-UPDATE-D07` | Cập nhật lỗi/mất mạng hoặc có xung đột phiên bản xử lý thế nào? | Không ghi đè dữ liệu hiện hành; giữ bản nháp trong memory để retry và dùng version/checksum chống lost update. | Pending |
| `SIG-UPDATE-D08` | Có cần audit và bảo vệ asset chữ ký không? | Audit create/update/status change, không log asset; mã hóa khi truyền/lưu và kiểm soát quyền đọc. | Pending |

## 9. Gate bàn giao

- PO duyệt các quyết định dùng chung `SIG-COMMON-D01`, `SIG-COMMON-D02` và các quyết định cập nhật `SIG-UPDATE-D03` đến `SIG-UPDATE-D08`.
- Figma có trạng thái đã có/chưa có chữ ký, edit popup, active/inactive, ký lại, no-change, loading/error/success.
- PM tạo task cha theo UC; FE dựng UI và deploy preview trước, sau đó mới triển khai BE, map API, QA và UAT.
- QA phải test riêng thay trạng thái, ký lại, cập nhật đồng thời, không có chữ ký, save failure và ảnh hưởng tới hợp đồng cũ/mới theo quyết định PO.
