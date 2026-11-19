# Context handoffs

Thư mục này định nghĩa giao thức đồng bộ delta từ task nhánh về task điều phối Smart Platform.

## Vì sao không dùng transcript làm source of truth

Transcript dài làm tăng context không tạo thêm giá trị và trạng thái bên ngoài có thể đã thay đổi. Task nhánh chỉ nhận context liên quan; khi đóng, nó trả lại một delta có cấu trúc.

## Hai loại dữ liệu

- **Quyết định bền vững:** identity rule, API contract, policy, workflow, dependency, source path. Cập nhật vào `CODEX_DESKTOP_HANDOFF.md` hoặc living spec.
- **Trạng thái động:** issue status, PR/build/deploy hiện tại. Chỉ ghi ledger và luôn kiểm tra lại provider; không sao chép dài hạn vào handoff trừ snapshot điều phối cần thiết.

## Tín hiệu đóng task

- Codex task: final answer có `ROOT_SYNC` và gửi về task điều phối nếu có thể.
- Multica task: comment cuối có `ROOT_SYNC`.
- PR/task chưa có `ROOT_SYNC` chưa được xem là đã đồng bộ context, dù code có thể đã merge.

Task điều phối không polling. Nó xử lý delta khi nhận tín hiệu close, blocker hoặc yêu cầu của PO.
