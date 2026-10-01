# AGENTS.md — Smart Platform

Tài liệu này áp dụng cho toàn bộ repository `smart-platform`. Đây là repository tài liệu và context hub của hệ sinh thái Smart Platform.

## Bắt đầu một task

1. Đọc [`CODEX_DESKTOP_HANDOFF.md`](CODEX_DESKTOP_HANDOFF.md).
2. Đọc [`docs/README.md`](docs/README.md) và living specification đúng sản phẩm/Use Case.
3. Kiểm tra trạng thái động trên Multica, GitHub và môi trường triển khai khi task cần thông tin đó. Không suy diễn trạng thái hiện tại từ snapshot trong handoff.
4. Chỉ nạp context liên quan trực tiếp tới task; không sao chép toàn bộ lịch sử hội thoại vào prompt.

## Nguồn chuẩn

- `docs/`: tài liệu Markdown hiện hành cho PM, Dev, QA và agent.
- `archieve/`: nguồn cũ, bản bị thay thế hoặc tài liệu truy vết; không được tự động coi là yêu cầu hiện hành.
- `CODEX_DESKTOP_HANDOFF.md`: quyết định xuyên repo, quy trình và snapshot điều phối gần nhất; không thay thế living specification.
- Multica/GitHub/deployment provider: nguồn trạng thái thực thi hiện tại.

## Quy tắc vận hành

- Trao đổi và tài liệu nghiệp vụ dùng tiếng Việt có dấu.
- Mỗi UC dùng một task cha; task con theo chuỗi `DOCS → FE → BE/BE-GAP → INT → QA → UAT` khi các bước đó thực sự cần.
- FE dựng UI và được review trước khi triển khai BE, trừ khi task chỉ sửa defect backend độc lập đã được duyệt.
- Không mở rộng scope hoặc tự thay đổi quyết định nghiệp vụ/Figma.
- Không polling liên tục. Chỉ kiểm tra tiến độ khi người dùng yêu cầu hoặc khi cần một lần xác nhận ngay sau thao tác.
- Không lưu API key, password, OTP, token, cookie hoặc secret vào Git, tài liệu hay comment task.
- Branch ngắn hạn được xóa sau khi merge vào `master`. Build/release chính thức chỉ chạy từ `master`, trừ khi PO yêu cầu preview riêng.

## Tách task để giảm context

- Task điều phối gốc giữ quyết định toàn hệ thống và điều phối thứ tự.
- Task nhánh chỉ nhận: mục tiêu, repo, living spec, quyết định liên quan, acceptance criteria và điều kiện kết thúc.
- Không truyền toàn bộ transcript của task gốc cho task nhánh.
- Nếu cần làm song song trong cùng repo, dùng worktree/branch riêng để tránh đè working tree.

## Bắt buộc đồng bộ ngược khi đóng task

Trước khi một task nhánh được coi là hoàn tất, agent phải phát một khối `ROOT_SYNC` theo mẫu tại [`.codex/handoffs/TEMPLATE.md`](.codex/handoffs/TEMPLATE.md).

- Với task Codex: gửi khối này về task điều phối gốc hoặc để trong final answer để task gốc đọc lại.
- Với task Multica: thêm khối này vào comment cuối của issue.
- Chỉ ghi delta tạo ra bởi task, không kể lại toàn bộ project.
- Task điều phối sau đó kiểm tra commit/PR đã merge, cập nhật `CODEX_DESKTOP_HANDOFF.md` nếu có quyết định bền vững, rồi ghi nhận tại [`.codex/handoffs/ledger.md`](.codex/handoffs/ledger.md).
- Không đóng task với mô tả chung chung như “done”; phải có bằng chứng commit, PR, test/build/deploy hoặc lý do N/A.

## Quy tắc sửa tài liệu

- Một mục đích tài liệu chỉ có một bản hiện hành trong `docs/`.
- Khi living spec thay đổi, cập nhật traceability liên quan trong cùng PR.
- Không tái tạo thư mục `markdown/`.
- Giữ nguyên thay đổi không liên quan của người dùng và agent khác.
- Dùng `apply_patch` cho chỉnh sửa thủ công.
