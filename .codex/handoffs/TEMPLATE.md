# ROOT_SYNC template

```text
ROOT_SYNC
task: <GLI-xx hoặc Codex task title/id>
status: <done | blocked | cancelled | partial>
scope_completed:
  - <delta thực tế>
repos:
  - <owner/repo>
merged_commits:
  - <full SHA hoặc none>
pull_requests:
  - <PR URL/number hoặc none>
contracts_or_decisions:
  - <quyết định mới/đổi hoặc none>
docs_changed:
  - <canonical path hoặc none>
validation:
  - <test/build/deploy/UAT evidence>
environment_changes:
  - <tên biến/config, không ghi secret; hoặc none>
open_risks_or_followups:
  - <việc còn lại hoặc none>
recommended_next_action: <một hành động cụ thể>
```

Quy tắc:

- Chỉ ghi thay đổi của task này.
- Không ghi OTP, mật khẩu, token, API key, cookie hoặc dữ liệu cá nhân không cần thiết.
- Không ghi “tests pass” nếu không có command/evidence tương ứng.
- Nếu không có code change, ghi rõ `merged_commits: none` và lý do N/A.
