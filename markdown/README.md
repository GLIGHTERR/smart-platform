# Smart Platform Markdown Mirror

Thư mục này chứa bản Markdown của các tài liệu DOCX/XLSX để agent có thể tìm kiếm, trích dẫn và đọc requirement ổn định hơn. File gốc vẫn được giữ nguyên và là nguồn chính thức về định dạng, công thức và lịch sử chỉnh sửa.

## Quy tắc sử dụng

- Không xóa hoặc thay thế file DOCX/XLSX gốc.
- Khi nội dung nguồn thay đổi, phải đồng bộ lại bản Markdown và cập nhật SHA-256.
- Nếu bản Markdown và file gốc khác nhau, ưu tiên quyết định PO mới nhất rồi tới file gốc đã được cập nhật.
- Ảnh nhúng từ DOCX được trích xuất vào thư mục `assets/` cùng nhóm tài liệu.
- Công thức Excel được giữ dưới dạng văn bản; bản Markdown không thay thế workbook để tính toán.
- Các Change Request lịch sử có thể chứa flow cũ. Với auth SmartTrọ MVP, dùng tài liệu của đúng UC trong `docs/use-cases/smarttro/` làm baseline.
- Các bổ sung trực tiếp trong Markdown sau ngày chuyển đổi phải ghi rõ ngày quyết định PO và liên kết tới UC baseline; không được thay đổi SHA-256 nguồn nếu DOCX/XLSX gốc chưa đổi.
- Với SRS SmartTrọ, `markdown/SRS/use-cases/` là baseline chuyển đổi nguyên trạng từ DOCX; `docs/use-cases/smarttro/` là living implementation spec tổng hợp thêm quyết định PO, Figma, API và test scope. Không coi hai lớp tài liệu này là một.
- Với SmartChủ, DOCX nguồn hiện còn flow số điện thoại/SMS và thiếu precondition phê duyệt hồ sơ kinh doanh ở các UC vận hành. `docs/use-cases/smartchu/` cùng `docs/11-smartchu-business-verification-policy.md` là lớp living spec/amendment hiện hành; không sửa âm thầm nội dung lịch sử của DOCX nguồn.

## Trạng thái chuyển đổi

| Nguồn | Bản Markdown | Đồng bộ | SHA-256 nguồn | Ghi chú |
| --- | --- | --- | --- | --- |
| `SRS/SRS (SmartTrọ).docx` | `SRS/SRS (SmartTrọ).md` + `SRS/use-cases/` | 2026-09-24 | `8cfae5992ace32ba2a206e879ce3ced370a526cf5d96cbb708f6157b94173d34` | Đã sửa lỗi converter bỏ sót bảng lồng trong DOCX: khôi phục danh mục 33 UC và toàn bộ 31 bảng đặc tả thực tế có trong nguồn. UC-01 đến UC-03 living spec vẫn giữ riêng trong `docs/use-cases/smarttro/`. SRS nguồn còn bất nhất số UC và thiếu 2 bảng đặc tả; xem `SRS/use-cases/README.md`. |
| `Requirement_List/Requirements List - SmartTrọ.xlsx` | `Requirement_List/Requirements List - SmartTrọ.md` | 2026-09-16; amended 2026-09-23 | `bbe7698a13132ecf3a3bf1195fd2f9ee8255578aea5da7181d8589ec7a492321` | Mỗi requirement/change request được tách thành record; SM004 được bổ sung theo quyết định PO, source XLSX chưa đổi |
| `User_Stories/User Story - SmartTrọ.xlsx` | `User_Stories/User Story - SmartTrọ.md` | 2026-09-16; amended 2026-09-23 | `d9dfec73abc55b828981b1854723cd7aa516deeda77ba6ded5f7f68aac21ec0f` | Nhóm theo sheet và từng User Story/AC; US 3.0 được bổ sung theo quyết định PO, source XLSX chưa đổi |
| `FRS/FRS - SmartTrọ.docx` | `FRS/FRS - SmartTrọ.md` | 2026-09-16 | `782c1e18ef1dfb5934c0d22177ff45f89a0f3cc029642aa1f4255c30d55caaef` | Toàn bộ đoạn văn, 5 bảng và 16 ảnh nhúng; source hiện chỉ đặc tả chi tiết UC-12, UC-14, UC-15 |
| `SRS/SRS (SmartChủ).docx` | `docs/use-cases/smartchu/` + `docs/11-smartchu-business-verification-policy.md` (living amendments, chưa phải full mirror) | 2026-09-30 | `fc374c30bc5c6777cb4bd7f6d8e48988b9dc801bd6b203d72fbd19b4469b58ab` | Source lịch sử vẫn dùng số điện thoại/SMS. Living specs auth chuyển sang email; policy xác minh kinh doanh đã Approved và bổ sung gate còn thiếu cho UC-10/18/22. Full SRS SmartChủ chưa convert. |
| `FRS/FRS - SmartChủ.docx` | Chưa convert | 2026-09-30 (inventory) | `c45b73e21d9ef7e090ec42b0620b5575792d36a93d21867f4b81947222af4181` | Giữ nguyên nguồn; sẽ convert sau khi scope SmartChủ/auth được PO chốt để tránh tạo hai baseline mâu thuẫn. |

## Thứ tự chuyển đổi tiếp theo

1. PO/BA sửa các bất nhất ID và phần đặc tả còn thiếu trong SRS SmartTrọ nguồn; sau đó chạy lại `scripts/convert_smarttro_srs_use_cases.py`.
2. Đồng bộ lại FRS SmartTrọ sau khi source được bổ sung phần auth có thể truy vết.
3. PO review và chốt `docs/use-cases/smartchu/UC-01..03`; bổ sung capture Figma SmartChủ trước handoff.
4. Convert đầy đủ Requirement List, User Story, SRS và FRS SmartChủ sau khi baseline auth được duyệt; không dùng ba living specs auth để thay thế toàn bộ SRS.
5. BRD, WBS, Questions và file quản lý đầu mục công việc khi các tài liệu trên đã ổn định.
