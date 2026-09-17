# UI Implementation and Review Playbook

## 1. Mục đích

Tài liệu này chuẩn hóa cách PM viết task, Dev triển khai và QA kiểm thử UI cho Smart Platform. Playbook được rút ra từ chuỗi triển khai và sửa lỗi của `GLI-48`, nơi một màn hình auth phải qua nhiều vòng sửa vì implementation đầu tiên chưa có đủ nguồn thiết kế, bằng chứng visual, quy tắc typography, responsive và điều kiện preview/deploy.

Mục tiêu không phải yêu cầu mọi pixel giống ảnh tĩnh bất chấp nền tảng. Mục tiêu là:

- bám đúng ngôn ngữ thị giác đã được PO duyệt;
- phát hiện sai hướng ngay ở một màn/state mẫu, trước khi nhân rộng;
- dùng đúng stack, component, asset và convention của repository;
- review được trên đúng build và đúng commit;
- tách rõ UI mock/review khỏi behavior production chưa được triển khai;
- giảm các vòng sửa lại toàn màn hình, giảm rework và quota agent.

Áp dụng cho `smart-tro`, `smart-chu`, `smart-admin` và các UI repository được bổ sung sau này. Quyết định riêng trong tài liệu UC/task luôn được ưu tiên hơn giá trị mặc định của playbook.

## 2. Bài học bắt buộc từ GLI-48

| Vấn đề đã gặp | Nguyên nhân gốc | Quy tắc phòng ngừa |
| --- | --- | --- |
| UI triển khai đầu tiên khác rõ Figma | Task mô tả flow nhưng chưa khóa exact frame/capture và visual invariants | Task UI phải có Figma file/page/node hoặc capture đã duyệt cho đúng app, đúng state |
| Frame SmartTrọ và SmartChủ có tên tương tự, asset export khó phân biệt | Dùng tên frame thay vì node ID và tên file có namespace | Mọi nguồn thiết kế phải ghi app, UC, state, node ID; file capture dùng prefix app/UC/state |
| Font tiếng Việt có nét và weight không đồng đều | Font/fallback/weight chưa được khóa và chưa kiểm tra computed font | Chỉ dùng font/weight được duyệt, load trước khi render và chụp evidence có dấu tiếng Việt |
| Social icon hiển thị không ổn định | Dùng glyph/icon thay thế thay cho brand asset quản lý trong repo | Dùng SVG/PNG/package asset đã kiểm tra; không dùng emoji hoặc ký tự gần giống |
| Khoảng cách input, title và component lệch ở nhiều viewport | Chỉ review một kích thước và thiếu screenshot matrix | Chốt baseline và chạy đủ responsive matrix trước PR |
| Web preview trắng sau deploy | Expo export chưa cấu hình đúng base path của GitHub Pages | Deployment task phải ghi hosting path; smoke test asset/route trên URL production |
| Web preview lỗi do storage native | Dùng `SecureStore` trực tiếp trên web | Mọi native dependency phải có platform adapter/fallback được test trên preview target |
| Local và preview hiển thị khác nhau | Feature flag review không được khai báo nhất quán | Task phải ghi flag, giá trị cho local/review/production và cập nhật `.env.example` |
| PR được mở nhưng PO chưa có bằng chứng so sánh | Screenshot/evidence bị coi là tùy chọn | Screenshot matrix, source capture và deviation note là gate bắt buộc trước review |
| Sửa font nhiều vòng | Chỉ kiểm tra tên package, chưa kiểm tra cảm nhận thị giác và fallback thực tế | QA/PO phải kiểm tra bằng hình ảnh; Dev phải cung cấp font-family/weight thực tế trên runtime |

## 3. Nguồn chuẩn và cách xử lý mâu thuẫn

### 3.1. Thứ tự nguồn chuẩn

1. Quyết định PO mới nhất trong task/comment.
2. Tài liệu UC đã phê duyệt trong `docs/use-cases/`.
3. Playbook này và handoff hiện hành.
4. Figma exact node/capture đã được ghi trong UC hoặc task.
5. Design tokens, typography và managed assets đang được phê duyệt trong code.
6. Component/foundation convention của repository.
7. Các source artifact cũ hơn như SRS, FRS, User Story, Requirement List.

Figma là nguồn chuẩn cho bố cục, màu, typography, hierarchy, thứ tự thành phần, độ bo và cảm nhận thị giác. Code foundation là nguồn chuẩn cho convention kỹ thuật, accessibility primitive và khả năng tái sử dụng. Không được dùng một component foundation khác phong cách chỉ vì component đó đã tồn tại; hãy thêm variant/token phù hợp thay vì bỏ qua visual baseline.

### 3.2. Không suy đoán từ tên frame

Tên như `Sign In`, `Sign Up`, `Forgot Password` có thể xuất hiện ở nhiều app hoặc nhiều state. PM/Dev/QA không được chọn frame chỉ bằng tên. Mỗi task phải ghi tối thiểu:

- tên sản phẩm/app;
- Figma file key hoặc URL;
- page;
- exact node ID;
- tên UC/screen;
- state của screen;
- đường dẫn capture đã duyệt nếu có.

Quy ước tên capture:

```text
<app>-<uc>-<screen>-<state>-<viewport>.<ext>
```

Ví dụ:

```text
smarttro-uc02-sign-in-default-375x812.png
smarttro-uc01-sign-up-otp-error-320x568.png
```

### 3.3. Điều kiện phải dừng và hỏi PO

PM phải comment và tag PO, không tự suy đoán, nếu xảy ra một trong các trường hợp:

- Figma và UC mô tả khác nhau về field, action hoặc flow;
- không xác định được frame/node thuộc app nào;
- requirement yêu cầu behavior chưa có contract hoặc chưa được duyệt;
- font, icon, màu hoặc component chủ đạo chưa có quyết định;
- khác biệt responsive có thể làm thay đổi composition, không chỉ co giãn;
- cần thêm/bớt thành phần so với happy-path capture;
- mock/review behavior có nguy cơ bị hiểu nhầm là production behavior;
- deployment yêu cầu public/private access, secret, domain hoặc native distribution chưa được phê duyệt.

## 4. Definition of Ready cho task UI

PM chỉ giao Dev khi task có đủ các trường sau.

### 4.1. Phạm vi và hành vi

- Task ID, UC/requirement ID và repository đích.
- Screen/state nằm trong scope; screen/state nằm ngoài scope.
- Route/entry point để review.
- Happy path, error, loading, disabled, empty và retry state áp dụng.
- Behavior là mock, review-only hay production.
- Những behavior phải giữ nguyên, đặc biệt khi task chỉ sửa visual.

### 4.2. Nguồn thiết kế

- Figma file/page/exact node hoặc capture đã duyệt.
- Danh sách visual invariants: hierarchy, thứ tự component, palette, typography, radius, alignment và asset.
- Baseline viewport và responsive matrix.
- Khác biệt accessibility đã duyệt so với frame tĩnh.
- Deviation đã biết và người phê duyệt deviation.

### 4.3. Ràng buộc kỹ thuật

- Framework/runtime và các library/component hiện hành của repo.
- Font family, weight mapping và cách load.
- Asset nào phải dùng từ repo/package; không để Dev tự chọn asset gần giống.
- Feature flags và giá trị ở local/review/production.
- Preview target, base path, route và environment contract.
- Test/lint/typecheck/export command cần pass.

### 4.4. Evidence bắt buộc

- Screenshot cho từng state được thay đổi ở baseline viewport.
- Screenshot responsive matrix cho happy path.
- So sánh cạnh nhau với source capture.
- PR ghi commit SHA, preview URL, commands đã chạy và deviation còn lại.

Nếu thiếu source thiết kế chính xác hoặc behavior boundary, task chưa Ready. Không giao Dev với mô tả chung như “làm giống mockup” hoặc “follow Figma”.

## 5. Quy trình triển khai của Dev

### 5.1. Trước khi sửa code

1. Đọc task, UC, playbook và exact Figma node/capture.
2. Xác nhận repository, branch, framework, component library, token và font hiện có.
3. Lập inventory của screen states, assets, flags, navigation và platform dependencies.
4. Ghi rõ behavior nào được giữ nguyên và behavior nào nằm ngoài scope.
5. Nếu task chỉ sửa visual, không thay mock/API/session/validation contract ngoài yêu cầu.

### 5.2. Triển khai theo lát cắt nhỏ

1. Hoàn thiện một happy-path screen ở baseline viewport.
2. Chụp và so sánh với source capture.
3. Sửa hierarchy, typography, spacing, alignment, radius và asset trước.
4. Chỉ sau khi baseline đạt mới mở rộng error/loading/disabled và responsive states.
5. Chạy test và preview sau mỗi thay đổi có ảnh hưởng layout/platform đáng kể.

Không xây hàng loạt screen dựa trên một interpretation chưa được PO review.

### 5.3. Typography

Đối với SmartTrọ, typography đã được chốt sau `GLI-48`:

| Vai trò | Font |
| --- | --- |
| Input, placeholder, body, helper, notice, error | `BeVietnamPro_400Regular` |
| Screen title, primary action, link, separator, social label | `BeVietnamPro_600SemiBold` |

Quy tắc bắt buộc:

- chỉ import các weight thực sự dùng;
- không trộn Poppins/system font tùy ý trong application content;
- chờ font load trước khi render evidence hoặc có loading gate rõ ràng;
- kiểm tra chuỗi tiếng Việt có dấu ở cả regular và semibold;
- kiểm tra runtime/computed `fontFamily` và `fontWeight`, không chỉ kiểm tra package đã cài;
- không dùng synthetic bold nếu weight thật đã có;
- OS status-bar chrome và brand logo/icon không bị ép theo application font.

SmartChủ hoặc SmartAdmin chỉ kế thừa mapping này khi tài liệu UC/design system của app đó đã phê duyệt. Không tự suy rộng quyết định SmartTrọ sang app khác.

### 5.4. Asset và icon

- Dùng asset SVG/PNG hoặc package được quản lý trong repo.
- Không dùng emoji, Unicode symbol hoặc icon gần giống để thay brand mark.
- Asset phải có tên theo app/feature, tránh export ra các file `(1)`, `(2)` không truy vết được.
- Kiểm tra kích thước, aspect ratio, màu, nền trong suốt và khả năng hiển thị trên Web/iOS/Android.
- Social control review-only phải hiển thị đúng asset nhưng không giả lập OAuth/session thành công.

### 5.5. Responsive và accessibility

Mặc định cho mobile Auth SmartTrọ:

| Viewport | Mục đích |
| --- | --- |
| `375 × 812` | Baseline visual comparison |
| `320 × 568` | Màn nhỏ/chiều cao thấp |
| `390 × 844` | Mobile phổ biến |
| `430 × 932` | Mobile rộng/cao |

Yêu cầu:

- không clip title, input, CTA, link hoặc error;
- không horizontal scroll;
- giữ khoảng cách rõ giữa các input và giữa các nhóm chức năng;
- xử lý safe area, keyboard và font scaling;
- vùng chạm tối thiểu theo UC/accessibility requirement;
- Expo Web trên viewport lớn chỉ render mobile canvas tối đa `430 px` nếu task không yêu cầu desktop composition;
- không hard-code OS status bar/home indicator từ ảnh Figma.

Giá trị matrix trên là baseline của Auth SmartTrọ, không phải quy tắc toàn hệ thống. Task cho layout khác phải ghi matrix phù hợp.

### 5.6. Platform và preview

- Expo Web/GitHub Pages phải cấu hình đúng base path của repository.
- Mọi route và static asset phải smoke test trực tiếp trên production preview URL.
- Native-only dependency như secure storage phải có platform adapter hoặc implementation `.web` riêng.
- Không đưa secret vào biến `EXPO_PUBLIC_*`.
- `.env.example` phải phản ánh các public flag cần để reviewer thấy đúng UI.
- Feature review-only phải có giá trị rõ cho local, preview và production; không dựa vào flag ngầm trong session agent.
- Preview phải được build từ commit đã merge. Ghi exact SHA; nếu dùng cache-busting query thì query chỉ giúp nhận diện build, không thay thế SHA evidence.

## 6. Visual acceptance gate trước PR

Dev phải tự kiểm tra trước khi mở PR:

- đúng app, UC, node và state;
- component order và hierarchy khớp source capture;
- font family/weight thực tế đúng, ký tự tiếng Việt không mỏng/dày bất thường;
- title, input, button, separator, social controls và links có spacing/alignment hợp lý;
- color, border, radius, width và icon đúng baseline;
- không có placeholder asset, emoji hoặc glyph tạm;
- baseline và responsive matrix không clip/overflow;
- keyboard/safe area không che action quan trọng;
- local và deployed preview hiển thị cùng feature set;
- behavior nằm ngoài scope không bị thay đổi.

Với Auth SmartTrọ, sai lệch alignment/spacing/radius ở happy path không vượt quá `4 px`, trừ safe area, OS chrome hoặc accessibility deviation đã ghi rõ trong UC.

Evidence tối thiểu trong PR:

```text
- Figma/source: <file/page/node hoặc capture path>
- Scope/states: <danh sách>
- Baseline screenshot: <375x812>
- Responsive screenshots: <320x568, 390x844, 430x932>
- Preview URL: <URL>
- Merge candidate SHA: <full SHA>
- Commands: <lint/typecheck/test/export>
- Deviations: <none hoặc danh sách + lý do + approval>
```

Không dùng câu “đã làm giống Figma” thay cho evidence.

## 7. Definition of Done cho Dev

- Functional behavior trong scope pass và behavior ngoài scope được giữ nguyên.
- Lint, typecheck, unit/component tests và platform export liên quan pass.
- Logic mới trong phạm vi task có coverage theo UC/task; coverage không thay thế visual test.
- Screenshot/evidence đầy đủ theo mục 6.
- PR mô tả source, states, flags, preview target, SHA và deviation.
- PR merge xong mới deploy build review chính thức.
- Preview chính thức chạy đúng merge SHA và URL mở được trên target browser/device.

## 8. Quy trình QA sau merge

QA chỉ bắt đầu execution sau khi:

- PR đã merge;
- preview/develop đã deploy đúng merge SHA;
- PM giao đúng UC, source capture, test data và environment contract;
- flags trên môi trường khớp review scope.

QA không tự dựng một happy-case environment tách rời. Test phải dùng route, navigation, config và integration hiện có của môi trường được chỉ định.

Visual QA phải:

1. Xác nhận build SHA và URL.
2. So sánh side-by-side với exact source capture.
3. Chạy đủ baseline/responsive matrix được ghi trong UC/task.
4. Kiểm tra font bằng nhận định hình ảnh và runtime/computed evidence khi có dấu hiệu fallback/synthetic weight.
5. Kiểm tra asset, spacing, alignment, overflow, keyboard, safe area và accessibility.
6. Chạy state transition từ output thực của bước trước, không tự nhập một bộ dữ liệu chỉ để happy path pass.
7. Ghi rõ behavior đang là mock/review-only; không kết luận backend production đã hoạt động nếu task chỉ có FE mock.

Defect phải có:

- screen/state/viewport;
- bước tái hiện;
- expected source/capture;
- actual screenshot;
- build SHA và environment;
- severity và ảnh hưởng;
- mỗi defect là một vấn đề tách biệt, không gộp nhiều lỗi không cùng nguyên nhân.

## 9. Mẫu nội dung PM giao Dev

```markdown
### UI implementation scope

- Task / UC: <GLI-xx / UC-xx>
- Repository: <repo>
- Route/entry: <route>
- In scope: <screen + states>
- Out of scope: <behavior/screens>
- Behavior boundary: <mock/review-only/production; behavior phải giữ nguyên>

### Design source

- Product/page: <SmartTrọ|SmartChủ|SmartAdmin / page>
- Figma file key: <key>
- Exact node IDs: <id + state>
- Approved captures: <repo paths>
- Baseline viewport: <width x height>
- Responsive matrix: <sizes>
- Approved accessibility deviations: <list>

### Technical constraints

- Framework/runtime: <current repo stack>
- Components/tokens: <paths/names>
- Typography: <family + exact weights + mapping>
- Managed assets: <paths/packages>
- Feature flags: <local/review/production values>
- Preview/deploy target and base path: <target>

### Acceptance and evidence

- Functional AC: <list>
- Visual invariants: <list>
- Required tests/commands: <list>
- Required screenshots: <states x viewports>
- PR must include: source, preview URL, full SHA, evidence and deviations.

Nếu source hoặc requirement mâu thuẫn/không rõ, dừng phần bị ảnh hưởng, comment và tag PO; không tự chọn interpretation.
```

## 10. Mẫu nội dung PM giao QA

```markdown
### QA execution handoff

- Task / UC: <GLI-xx / UC-xx>
- Merged PR: <URL>
- Merge SHA: <full SHA>
- Environment / preview URL: <URL>
- Exact design source: <file/page/node/capture>
- States and responsive matrix: <list>
- Feature flags/environment contract: <list>
- Test data source: <actual setup/data; không tự dựng happy-case riêng>
- Known mock/review-only behavior: <list>
- Known approved deviations: <list>

QA phải test deployed merge SHA, ghi evidence từng viewport/state và tạo defect riêng cho từng vấn đề độc lập.
```

## 11. Checklist ngắn cho PM

Trước khi bấm giao task UI, PM tự kiểm tra:

- [ ] Exact repo/app/UC/screen/state đã rõ.
- [ ] Exact Figma node hoặc capture đã có.
- [ ] Font/weight, asset và visual invariants đã khóa.
- [ ] Behavior boundary và out-of-scope đã ghi.
- [ ] Baseline/responsive matrix đã ghi.
- [ ] Feature flags và preview target đã ghi.
- [ ] Evidence/DoD đã ghi.
- [ ] Có quy tắc stop-and-ask khi mâu thuẫn.
- [ ] QA handoff sau merge/deploy đã chuẩn bị.

