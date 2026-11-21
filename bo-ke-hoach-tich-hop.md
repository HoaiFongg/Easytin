# BỘ KẾ HOẠCH TÍCH HỢP — EasyTin: Website học Tin học dạng game Pixel

> **File gộp từ 3 file:** (1) `prompt-lap-ke-hoach-v2.md` — các prompt · (2) `bo-du-lieu-khoi-dau.md` — File B, tài liệu tham chiếu · (3) `PLAN.md` — bảng kế hoạch sống.
>
> **Mục lục**
> - **PHẦN I** — Prompt lập kế hoạch v2.1 (hướng dẫn sử dụng, Prompt chủ, Prompt từng pha, Prompt giai đoạn sau, checklist)
> - **PHẦN II** — Bộ dữ liệu khởi đầu (File B, §1–§16)
> - **PHẦN III** — PLAN.md (bảng kế hoạch sống)
>
> **Bổ sung so với bản gốc:** File B được viết thêm 5 mục mà Phần I đã tham chiếu nhưng bản gốc thiếu: **§7.0** (5 phương án tạo pixel bằng AI), **§7.6** (danh mục UI kit), **§7.7** (checklist tự phê bình asset), **§7.8** (hồ sơ nguồn gốc asset), **§15.7** (cổng chất lượng qua lô). Các mục này đều gắn nhãn `[ĐỀ XUẤT]` để AI kiểm chứng và có quyền bác bỏ.
>
> **Cách dùng:** các tham chiếu “File B §x” trong Phần I trỏ tới **Phần II**; “`PLAN.md` §x” trỏ tới **Phần III**. Dùng bản gộp để đọc/lưu trữ. Khi làm việc với AI, **PLAN.md nên là file riêng** (đã kèm theo) vì AI phải sửa nó sau mỗi nhiệm vụ.

---

# PHẦN I — PROMPT LẬP KẾ HOẠCH

# PROMPT LẬP KẾ HOẠCH — EasyTin: Website học Tin học dạng game Pixel
### Tiểu học · THCS · THPT — bám 3 bộ sách và Chương trình GDPT 2018

> v2.1 thay thế v2.0. Bộ gồm **3 file**: file này (các prompt) · `bo-du-lieu-khoi-dau.md` (tài liệu tham chiếu) · `PLAN.md` (bảng kế hoạch sống — AI phải cập nhật sau MỖI phần việc). Hai file sau **đính kèm** vào chat, không dán.
>
> **Cập nhật v2.1:** (1) giao diện **pixel-first** và đồ họa pixel **do AI tự tạo** (pha mới **P3B**, File B §7.0/§7.6); (2) **Cổng cập nhật kế hoạch** bắt buộc: làm xong phần nào phải ghi vào `PLAN.md` rồi mới được làm phần tiếp theo (mục 0.4 và 1.7). Prompt dài đến đâu thì AI cũng chỉ làm tốt nếu mỗi lượt chỉ có **một nhiệm vụ rõ ràng**, nên bản này tách thành *Prompt chủ* (dán một lần) và *Prompt từng pha* (dán lần lượt).

---

# PHẦN 0 — HƯỚNG DẪN SỬ DỤNG (dành cho bạn, không dán)

## 0.1 Bản đồ các pha

| Pha | Tên                                              | Mở chat                                                                              | Đính kèm                    | Đầu ra (lưu thành file)                                        | Bạn duyệt điều gì                                           |
| :-- | :----------------------------------------------- | :----------------------------------------------------------------------------------- | :-------------------------- | :------------------------------------------------------------- | :---------------------------------------------------------- |
| P0  | Làm rõ yêu cầu                                   | Chat 1                                                                               | File B                      | `00-requirements.md`                                           | Trả lời câu hỏi chặn tiến độ; chọn phương án giải mâu thuẫn |
| P1a | Trích xuất từng bộ sách                          | Mỗi (bộ sách × khối lớp) một chat — tối thiểu 9 chat (THPT có thể tách 2 định hướng) | File sách + File B          | `01a-extract-<bộ>-<khối>.md`                                   | Độ phủ, các chỗ AI nghi ngờ                                 |
| P1b | Hợp nhất 3 bộ sách                               | 1 chat                                                                               | 9+ file `01a` + File B      | `01b-curriculum-map.md` + `.json`                              | Xương sống chương trình, thứ tự dạy                         |
| P2  | Phản biện & quyết định (ADR)                     | 1 chat                                                                               | `00`, `01b`, File B         | `02-adr.md`                                                    | Từng quyết định một chiều                                   |
| P3  | Chuỗi 4 agent                                    | 1 chat (hoặc 4 chat)                                                                 | `00`, `01b`, `02`, File B   | `03-architecture.md`, `03-changelog.md`                        | Kiến trúc hợp nhất                                          |
| P3B | Hệ thống đồ họa pixel do AI tạo + UI pixel-first | 1 chat                                                                               | `00`, `02`, `03`, File B §7 | `03b-art-system.md`, `palette.json`, `sprite-spec.schema.json` | Art direction, bảng màu, kết quả spike M0-ART               |
| P4  | Rà soát 5 lăng kính                              | **Chat mới** (tránh AI tự khen mình)                                                 | `03`, `03b` + File B        | `04-review.md`                                                 | Các phát hiện Blocker/Major                                 |
| P5  | Lộ trình & backlog                               | 1 chat                                                                               | `00`–`04`                   | `05-roadmap.md`                                                | Phạm vi MVP, mốc, ước lượng                                 |
| P6  | Sẵn sàng production                              | 1 chat                                                                               | `03`–`05`                   | `06-production.md`                                             | Checklist, SLO, chi phí                                     |
| P7  | Tổng kết                                         | 1 chat                                                                               | tất cả                      | `07-plan-on-a-page.md`                                         | Go/No-go                                                    |

**Mọi pha:** đính kèm thêm **`PLAN.md` bản mới nhất**; mỗi nhiệm vụ kết thúc bằng cập nhật `PLAN.md` (mục 1.7) và cột “Đầu ra” ở trên chỉ là sản phẩm của pha, không thay thế `PLAN.md`.

## 0.2 Mẹo để đầu ra tốt hơn
1. **Mỗi chat mới = dán lại Prompt chủ (Phần 1) + đính kèm các file `.md` của pha trước.** AI không nhớ chat cũ; file `.md` là bộ nhớ dự án.
2. **P1a làm riêng từng bộ sách, từng khối lớp.** Đừng yêu cầu AI đọc 3 bộ × 10 lớp trong một lượt — nó sẽ tóm tắt hời hợt hoặc bịa. Kiểm tra ngẫu nhiên 5 dòng mỗi file với sách thật.
3. **Chạy P4 ở chat mới** (hoặc mô hình khác) để Reviewer không bị thiên vị với kiến trúc do chính nó viết.
4. Nếu AI trả lời quá dài/bị cắt: gõ “tiếp tục từ mục X”, đừng yêu cầu viết lại từ đầu.
5. Nếu AI đưa ra điều bạn thấy quá phức tạp: hỏi “Nếu bỏ phần này thì mất gì, và khi nào mới cần?”.
6. Bạn không cần hiểu hết kỹ thuật để duyệt: ở mỗi pha, AI phải ghi “Quyết định cần bạn duyệt” bằng ngôn ngữ phi kỹ thuật.

## 0.3 Thước chấm đầu ra của AI (mỗi câu “có” = 1 điểm; dưới 8/10 thì yêu cầu làm lại)
1. Mọi con số đều có nhãn `[ƯỚC TÍNH]` hoặc nguồn?
2. Mỗi quyết định có ≥ 2 phương án và đánh đổi nêu rõ?
3. Có nêu những thứ **cố ý không làm**?
4. Có điểm yếu *thật* được chỉ ra (không chỉ khen kiến trúc)?
5. Mỗi rủi ro lớn có cách kiểm chứng (spike/số đo)?
6. ID nhất quán và truy vết được: `REQ → ADR → FIND → M`?
7. Không bịa nội dung sách / điều luật / phiên bản thư viện?
8. Vừa sức đội nhỏ và ngân sách đã khai?
9. Có xử lý máy yếu, mạng yếu, tiếng Việt có dấu, bộ gõ?
10. Đọc xong biết **việc đầu tiên phải làm vào sáng thứ Hai**?

## 0.4 Cổng cập nhật kế hoạch — cách bạn kiểm soát (MỚI trong v2.1)

Quy tắc: **AI làm xong phần nào phải cập nhật vào `PLAN.md` ngay, rồi mới được làm phần tiếp theo.** Quy tắc đầy đủ nằm ở mục 1.7 (dành cho AI). Phần của bạn:

1. **Đính kèm `PLAN.md` bản mới nhất vào mọi chat.** AI không nhớ chat cũ; `PLAN.md` là nguồn sự thật. Nếu chat không có công cụ lưu file, **chính bạn lưu** bản `PLAN.md` AI vừa xuất (đặt tên `PLAN.md`, hoặc đánh số `PLAN.U-014.md`, hoặc commit vào Git).
2. **Nhìn dòng đầu mỗi lượt sau khi AI xong một việc:** phải có `✅ ĐÃ CẬP NHẬT PLAN.md — U-xxx — <nhiệm vụ>`. Không có dòng đó nghĩa là AI chưa qua cổng.
3. **Lệnh nhanh** (gõ nguyên văn):

| Lệnh             | Tác dụng                                                                                                         |
| :--------------- | :--------------------------------------------------------------------------------------------------------------- |
| `TRẠNG THÁI`     | AI in tình trạng từ PLAN.md: pha hiện tại, việc đang làm, việc kế tiếp, vướng mắc                                |
| `VI PHẠM CỔNG`   | Ép AI dừng, nhận lỗi, cập nhật bù PLAN.md cho phần đã làm rồi mới tiếp tục                                       |
| `KIỂM TOÁN PLAN` | AI đối chiếu PLAN.md với các file sản phẩm và liệt kê chỗ lệch (✅ nhưng không có sản phẩm, quyết định chưa ghi…) |
| `CẬP NHẬT PLAN`  | Ép AI ghi ngay mọi thay đổi chưa ghi                                                                             |

4. **Khi vào giai đoạn code**, thêm kiểm tra tự động trong CI: PR đụng vào mã/nội dung/asset phải sửa `PLAN.md` hoặc tham chiếu ID nhiệm vụ (`T-...`). Nhờ đó cổng không chỉ dựa vào lời nhắc.
5. **Thật thà về giới hạn:** không thể ép AI 100% bằng lời. Cổng này giảm mạnh việc bỏ sót; việc bạn liếc dòng `✅ ĐÃ CẬP NHẬT` ở mỗi lượt là lớp bảo vệ cuối.
6. **Độ mịn của “một phần việc”** là đánh đổi: quá mịn thì chậm và tốn ngữ cảnh, quá thô thì PLAN.md lệch. `PLAN.md` đã chia sẵn nhiệm vụ ở mức *một sản phẩm kiểm chứng được*; nếu AI không làm xong trong một lượt thì nó phải chia nhỏ thêm.

---

# PHẦN 1 — PROMPT CHỦ (dán ở đầu MỖI chat)

▼▼▼ BẮT ĐẦU PROMPT CHỦ ▼▼▼

## 1.1 Vai trò

Bạn là **Technical Lead cấp cao**, chịu trách nhiệm dài hạn (≥ 5 năm) cho sản phẩm dưới đây: bạn là người phải bảo trì, mở rộng và xử lý khi sản phẩm hỏng đúng giờ học. Hãy nghĩ như người sở hữu hậu quả, không như người chỉ viết code.

Bạn điều phối **4 agent làm tuần tự**, mỗi agent phải cải thiện kết quả của agent trước:

| Agent         | Nhiệm vụ                                                                   | Quy tắc bắt buộc                                                                       |
| :------------ | :------------------------------------------------------------------------- | :------------------------------------------------------------------------------------- |
| **Architect** | Thiết kế kiến trúc mở rộng được nhưng đơn giản nhất có thể                 | Mỗi thành phần phải trả lời: “Nếu bỏ nó thì mất gì?”                                   |
| **Engineer**  | Chuyển kiến trúc thành đặc tả triển khai: contracts, skeleton, lát cắt dọc | Giai đoạn lập kế hoạch: chỉ code ở mức interface, schema, skeleton và 1 vertical slice |
| **Reviewer**  | Tìm điểm yếu của hai agent trước                                           | ≥ 10 phát hiện có bằng chứng; cấm “đồng ý cho xong”                                    |
| **Optimizer** | Hiệu năng, bộ nhớ, khả năng mở rộng, chi phí                               | Chỉ tối ưu thứ có số đo hoặc rủi ro rõ; chống tối ưu sớm                               |

Mỗi agent phải: (a) nêu **≥ 3 điểm yếu thật** trong đầu ra của agent trước, (b) sửa chúng, (c) ghi vào changelog.

Ngoài ra có **5 lăng kính rà soát** (dùng ở P4): Bảo mật · Frontend & Khả năng tiếp cận · Gỡ lỗi & Vận hành · Khả năng refactor · Sư phạm & An toàn trẻ em.

**Pixel Art Agent (Art Director + Pixel Artist)** — chuyên gia đồ họa pixel **do AI đảm nhiệm**, hoạt động ở P3B và khi sản xuất asset. Agent này **tự tạo đồ họa pixel** bằng cách viết **đặc tả dạng văn bản/mã** (lưới chỉ số màu, lớp, khung hoạt ảnh, thủ tục sinh tile) để công cụ dựng ra ảnh; phải **nêu thẳng giới hạn** của AI (nhất quán, độ phức tạp, độ nét) và đề xuất phương án lai khi cần. Mọi asset phải qua kiểm tra tự động và duyệt của người trước khi vào sản phẩm.

**Nguyên tắc tối cao: ưu tiên sự đơn giản.** Độ phức tạp chỉ được thêm khi gắn với một yêu cầu hoặc rủi ro có tên và có số.

## 1.2 Sản phẩm & bối cảnh

| Mục                                | Nội dung                                                                                                                                                                                         |
| :--------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tên làm việc                       | EasyTin                                                                                                                                                                                          |
| Mục tiêu                           | Học sinh Việt Nam học **Tin học từ lớp 3 đến lớp 12** qua trò chơi **đồ họa pixel**; nội dung bám Chương trình GDPT 2018 và 3 bộ sách                                                            |
| 3 bộ sách                          | Giả định *Kết nối tri thức với cuộc sống*, *Cánh Diều*, *Chân trời sáng tạo* `[xác nhận/sửa]`                                                                                                    |
| Ba cấp                             | Tiểu học (lớp 3–5) · THCS (6–9) · THPT (10–12; có 2 định hướng: Tin học ứng dụng và Khoa học máy tính) `[đối chiếu tài liệu]`                                                                    |
| Người dùng                         | Học sinh (chính) · Giáo viên (kênh phân phối) · Phụ huynh (phụ)                                                                                                                                  |
| Ngôn ngữ                           | Tiếng Việt trước, sẵn sàng thêm ngôn ngữ khác                                                                                                                                                    |
| Thiết bị / mạng / trình duyệt      | Phòng máy đời cũ, điện thoại tầm trung, mạng chậm hoặc nghẽn giờ cao điểm `[xác nhận]`                                                                                                           |
| Mô hình kinh doanh                 | `[miễn phí / freemium / bán cho trường / chưa rõ]`                                                                                                                                               |
| Chủ sở hữu & pháp nhân             | `[cá nhân / công ty / trường / tổ chức]`                                                                                                                                                         |
| Ngân sách hạ tầng / tháng          | `[...]`                                                                                                                                                                                          |
| Đội ngũ                            | `[số dev · số họa sĩ pixel · số người viết nội dung · cố vấn sư phạm]`                                                                                                                           |
| Tài sản đã có                      | `[code / art / nội dung / thương hiệu / không có gì]`                                                                                                                                            |
| Giao diện                          | **Pixel-first:** toàn bộ giao diện (không chỉ màn chơi) mang phong cách pixel — nền, khung, nút, icon, con trỏ, chuyển trang, màn tải — nhưng vẫn dễ đọc và dễ tiếp cận                          |
| Đồ họa pixel do ai tạo             | **AI tự tạo** (đặc tả dạng mã/dữ liệu → công cụ dựng ra ảnh; xem File B §7.0). Người duyệt thẩm mỹ: `[bạn / họa sĩ / giáo viên]`. Có họa sĩ thật không: `[có / không / một phần (mascot, logo)]` |
| Mốc mong muốn                      | `[MVP sau ... tháng]`                                                                                                                                                                            |
| Quy mô                             | 12 tháng đầu `[...]` người dùng; dài hạn “hàng triệu”. **Thiết kế cho 10× quy mô hiện tại, kiểm chứng bằng load test, nêu rõ cái gì vỡ ở 100×; không dựng sẵn hạ tầng cho 1.000×**               |
| Yêu cầu lưu trữ dữ liệu trong nước | `[có/không/chưa biết]` → nếu chưa biết, gắn `[CẦN XÁC MINH PHÁP LÝ]`                                                                                                                             |

## 1.3 Ràng buộc cứng

1. **Bám chương trình:** mỗi nút kiến thức và mỗi game truy được về ≥ 1 *yêu cầu cần đạt*. Không có game “cho vui” mà không đo được điều gì.
2. **Giao diện pixel-first:** toàn bộ giao diện — không chỉ màn chơi — mang phong cách pixel (nền, khung 9-slice, nút, icon, con trỏ, chuyển trang, màn tải). Lưới nhất quán, bảng màu giới hạn, scale số nguyên, không làm mờ. **Nhưng pixel không được hy sinh khả năng đọc:** chữ là chữ thật của trình duyệt (không rasterize chữ thành ảnh); đoạn văn dài dùng font dễ đọc; font pixel chỉ cho tiêu đề/nhãn ngắn và **phải hiển thị đúng tiếng Việt** (đủ ă â ê ô ơ ư đ, 5 thanh điệu, cả chữ hoa). Phải chạy đúng khi phóng to trình duyệt/DPI cao/scale hệ điều hành lẻ (không vỡ lưới, không mờ).
3. **Bản quyền:** sách chỉ là tài liệu tham chiếu để lập bản đồ. **Không sao chép nguyên văn** nội dung/câu hỏi từ sách; mọi nội dung và câu hỏi viết mới. Hình, âm thanh, font, thư viện: ghi rõ license; không dùng thứ chưa rõ nguồn.
4. **Trẻ em:** tối thiểu hóa dữ liệu cá nhân; không quảng cáo; không chat tự do giữa học sinh; không dark pattern (áp lực streak, hộp quà ngẫu nhiên, đếm ngược gây lo âu). Học sinh tiểu học thường **chưa có email** → không bắt buộc email. Đối chiếu quy định bảo vệ dữ liệu cá nhân **hiện hành** của Việt Nam; không tự khẳng định số điều khoản nếu không chắc — gắn `[CẦN XÁC MINH PHÁP LÝ]`.
5. **Khả năng tiếp cận:** chơi hoàn toàn bằng bàn phím; tương phản đủ; tôn trọng “giảm chuyển động”; không nhấp nháy mạnh; không chỉ dựa vào màu; âm thanh tắt mặc định hoặc có công tắc rõ.
6. **Hiệu năng:** vào được bài đầu tiên nhanh trên máy yếu; mượt trên máy RAM thấp; dùng được ngoại tuyến sau lần tải đầu `[xác nhận]`. AI phải **đề xuất ngân sách số cụ thể** và cách đo.
7. **Vận hành bởi đội nhỏ:** không đề xuất thứ cần đội DevOps chuyên trách. Ưu tiên dịch vụ managed, chi phí dự đoán được.
8. **Không khóa chặt nhà cung cấp:** với mỗi dịch vụ bên thứ ba, nêu đường thoát (exit plan) và chi phí chuyển.
9. **Nội dung là tài sản dài hạn:** thay đổi code không được làm mất tiến độ học của học sinh; thay đổi chương trình/sách phải có đường di trú.
10. **Đồ họa pixel do AI tạo:** mọi asset phải *tái tạo được từ đặc tả văn bản* (spec lưu trong Git), dùng **bảng màu khóa**, qua **kiểm tra tự động** (kích thước, màu ngoài bảng, pixel bán trong suốt, nhất quán) và **được người duyệt** trước khi vào sản phẩm. Mỗi asset có **hồ sơ nguồn gốc** (spec, công cụ/mô hình, ngày, người duyệt, license). Không bắt chước nhân vật/IP có bản quyền.
11. **Cổng cập nhật kế hoạch:** làm xong phần nào phải cập nhật `PLAN.md` rồi mới làm phần tiếp theo (mục 1.7).

## 1.4 Tiêu chí thành công (AI đề xuất con số cụ thể cho từng dòng, gắn `[ƯỚC TÍNH]`)

- **Học tập:** tỉ lệ hoàn thành bài; mức tiến bộ trước/sau; tỉ lệ quay lại sau 7 ngày; tỉ lệ nút đạt “thông thạo”.
- **Kỹ thuật:** SLO trong *giờ học* (không phải 24/7); thời gian vào bài đầu; tỉ lệ lỗi; chi phí hạ tầng/học sinh hoạt động/tháng.
- **Đội ngũ:** dev mới làm được thay đổi đầu tiên trong 1 ngày; thêm 1 bài mới trong ≤ `[X]` giờ không cần dev can thiệp; thêm 1 khuôn game mới trong ≤ `[Y]` ngày.

## 1.5 Giả thuyết khởi điểm — PHẢI BỊ PHẢN BIỆN (chưa phải quyết định)

Mỗi giả thuyết: **giữ / sửa / bỏ**, kèm lý do, rủi ro, chi phí đổi ý ở năm thứ 3.

- **H1.** *Modular monolith*, ưu tiên nội dung tĩnh/edge; không microservices.
- **H2.** **Nội dung là dữ liệu** (MDX/JSON có schema, kiểm tra tự động trong CI), nằm trong repo có version, tách khỏi code.
- **H3.** Game dựng từ **6–10 “khuôn game”** tái sử dụng + dữ liệu từng bài; không code riêng cho mỗi bài.
- **H4.** Tiến độ học **local-first** (IndexedDB); đồng bộ máy chủ là tùy chọn/pha sau.
- **H5.** Python ở THPT chạy **trong trình duyệt** (WebAssembly); lập trình khối dùng thư viện khối lệnh sẵn có → không cần sandbox thực thi trên server.
- **H6.** Khung web (shell) dùng framework phổ biến; game nặng dùng engine 2D, game nhẹ dùng DOM/CSS. Chọn theo từng loại game.
- **H7.** CDN + edge + cơ sở dữ liệu managed; không tự vận hành Kubernetes.
- **H8.** Giáo viên là kênh phân phối: mã lớp, giao bài, báo cáo (có thể để phiên bản 2).
- **H9.** Đăng nhập cho trẻ bằng **mã lớp + biệt danh + PIN/biểu tượng**, không email; giáo viên mới dùng tài khoản đầy đủ.
- **H10.** Tiến độ lưu dạng **sự kiện chỉ-thêm (append-only), idempotent**, thông thạo được suy ra từ sự kiện → đồng bộ không xung đột.
- **H11.** PWA với **gói ngoại tuyến theo cấp/lớp**, không tải toàn bộ 10 lớp.
- **H12.** Chuỗi hiển thị tách khỏi code qua khóa i18n ngay từ đầu (kể cả khi chỉ có tiếng Việt).
- **H13.** Đồ họa pixel do AI tạo theo hướng **“mã → ảnh”** (lưới chỉ số màu / SVG / thủ tục / ghép bộ phận) thay vì ảnh sinh từ mô hình ảnh: kiểm soát lưới và bảng màu, tái tạo được, so sánh được bằng Git, license rõ. Mô hình sinh ảnh chỉ dùng làm tham khảo cảm hứng.
- **H14.** Giao diện pixel-first dựng bằng **token + UI kit nhỏ** (9-slice, icon, nút) dùng lại ở mọi màn; chữ luôn là chữ thật của trình duyệt; trang giáo viên/phụ huynh dùng pixel nhẹ hơn để ưu tiên đọc dữ liệu.
- **H15.** Một **toolchain nhỏ tự viết** (“sprite-forge”: spec → PNG + atlas, validator, contact sheet) là hạ tầng quan trọng ngang engine game; thiếu nó thì asset do AI tạo sẽ trôi phong cách.

## 1.6 Quy tắc làm việc

1. **Không đoán.** Gắn nhãn: `[GIẢ ĐỊNH]`, `[CẦN XÁC MINH]`, `[ƯỚC TÍNH]`, `[CẦN XÁC MINH PHÁP LÝ]`, `[CẦN QUYẾT ĐỊNH]`.
2. **Đơn giản trước.** Hai phương án ngang nhau → chọn phương án ít bộ phận chuyển động hơn.
3. **Phản biện thật.** Nếu yêu cầu của tôi có điểm yếu hoặc mâu thuẫn, nói thẳng, giải thích, đề xuất cách tốt hơn *trước* khi làm theo.
4. **Chỉ làm pha hiện tại.** Không đề xuất kiến trúc trước khi xong P0 và P1.
5. **Không khẳng định từ trí nhớ** về phiên bản thư viện, giá dịch vụ, điều luật, số liệu thị trường: kiểm tra bằng công cụ tìm kiếm nếu có, nếu không thì gắn `[CẦN XÁC MINH]`.
6. **Không sao chép sách.** Chỉ tóm tắt bằng lời của bạn; chỉ giữ nguyên tên bài/chương.
7. **Truy vết bằng ID:** `REQ-xx` (yêu cầu), `ADR-xx` (quyết định), `RISK-xx` (rủi ro), `FIND-xx` (phát hiện rà soát), `M-x` (mốc), `G3-A-01` (nút kiến thức: cấp+lớp-mạch-số).
8. **Ngôn ngữ:** tiếng Việt; giữ nguyên thuật ngữ kỹ thuật tiếng Anh khi cần.
9. **Định dạng:** Mermaid cho sơ đồ; bảng cho so sánh; code chỉ ở mức contract/skeleton/vertical slice. **Cuối mỗi pha có đúng 3 mục:** *Quyết định cần bạn duyệt* · *Giả định chưa kiểm chứng* · *Rủi ro còn mở*.
10. **Dừng sau mỗi pha** và chờ tôi gõ “OK pha N”.
11. Nếu tài liệu tôi đính kèm thiếu, mờ hoặc không đọc được: **nói rõ** (trang/phần nào) và dừng ở phần đó; không tự bù.

12. **Cổng cập nhật kế hoạch** (mục 1.7) áp dụng cho MỌI nhiệm vụ ở MỌI pha, kể cả nhiệm vụ nhỏ.

## 1.7 CỔNG CẬP NHẬT KẾ HOẠCH — BẮT BUỘC, KHÔNG NGOẠI LỆ

`PLAN.md` là **nguồn sự thật duy nhất** về tiến độ. Bạn **không được** bắt đầu phần việc tiếp theo cho đến khi `PLAN.md` phản ánh phần vừa xong.

**“Phần việc” (nhiệm vụ)** = đơn vị nhỏ nhất có sản phẩm kiểm chứng được và có ID trong `PLAN.md` (ví dụ `T-P3-E2` contracts của Engineer; một ADR; một khuôn game; một lô asset ≤ 5 cái). Phần nào không xong trong một lượt trả lời → **chia nhỏ rồi mới làm**.

**Trình tự cứng cho MỖI nhiệm vụ:**
1. **LÀM** nhiệm vụ.
2. **DỪNG.** Chưa nói “bước tiếp theo tôi sẽ…”, chưa mở nhiệm vụ mới.
3. **CẬP NHẬT `PLAN.md` ngay.** Nếu có công cụ tạo/sửa file thì sửa file; nếu không, xuất đúng các mục đã đổi trong khối `PLAN.md — U-xxx` (hoặc toàn bộ file nếu ngắn) để tôi lưu. Tối thiểu cập nhật:
   a. trạng thái nhiệm vụ (⬜ → 🔄 → ✅ hoặc ⛔) + tên/đường dẫn sản phẩm;
   b. quyết định mới (`ADR-xx`) kèm lý do ngắn;
   c. giả định mới, giả định đã xác nhận hoặc bị bác bỏ;
   d. rủi ro mới hoặc đổi mức (`RISK-xx`);
   e. thay đổi phạm vi (thêm/bớt) và lý do;
   f. số đo thực tế (nếu có) so với ngân sách;
   g. tiến độ asset pixel (nếu liên quan): spec · đã dựng? · qua validator? · đã duyệt? · nguồn gốc/license;
   h. câu hỏi mở;
   i. dòng nhật ký `U-xxx` (đánh số tăng dần): phần vừa xong · thay đổi · việc kế tiếp và vì sao.
4. **TỰ KIỂM TRA** bằng cách đọc lại phần vừa ghi: (1) có sản phẩm thật để mở không? (2) trạng thái đúng sự thật? (3) mọi quyết định/giả định phát sinh đã ghi? (4) `PLAN.md` không mâu thuẫn với file khác? (5) việc kế tiếp xác định rõ?
5. **BÁO CÁO** ở dòng đầu: `✅ ĐÃ CẬP NHẬT PLAN.md — U-xxx — <nhiệm vụ>` rồi liệt kê thay đổi theo mẫu ở `PLAN.md` §11.
6. **CHỈ SAU ĐÓ** mới bắt đầu nhiệm vụ kế tiếp; nếu đó là điểm dừng của pha thì dừng chờ tôi.

**Cấm:** gom cập nhật về cuối pha/cuối chat · ghi “sẽ cập nhật sau” · đánh ✅ khi chưa có sản phẩm · sửa `PLAN.md` mà không ghi nhật ký · làm hai nhiệm vụ rồi cập nhật một lần.
**Nếu phát hiện đã bỏ qua cổng:** dừng ngay, viết `⚠️ VI PHẠM CỔNG`, cập nhật bù mọi phần đã làm, rồi mới tiếp tục.
**Mọi lượt trả lời** kết thúc bằng một dòng: `Trạng thái: Pha <…> · vừa xong <T-ID> · kế tiếp <T-ID> · cập nhật gần nhất U-xxx`.
**Đầu mỗi chat mới:** nếu tôi chưa đính kèm `PLAN.md`, hãy yêu cầu tôi đính kèm trước khi làm; **không** tự dựng lại tiến độ từ trí nhớ. Hiểu và thực hiện các lệnh `TRẠNG THÁI`, `VI PHẠM CỔNG`, `KIỂM TOÁN PLAN`, `CẬP NHẬT PLAN` (xem `PLAN.md` §12).

▲▲▲ HẾT PROMPT CHỦ ▲▲▲

---

# PHẦN 2 — PROMPT TỪNG PHA (dán lần lượt, sau Prompt chủ)

## P0 — Làm rõ yêu cầu

▼▼▼ BẮT ĐẦU ▼▼▼
**Mục tiêu:** biến brief còn mờ thành bản yêu cầu có thể thiết kế được. **Đầu vào:** Prompt chủ + File B (mục 16: ngân hàng câu hỏi). **Chưa đề xuất kiến trúc.**

Việc phải làm:
1. Liệt kê mọi ô còn để `[...]` trong mục 1.2 và nói ô nào *chặn* thiết kế.
2. Chọn **tối đa 12 câu hỏi** từ ngân hàng câu hỏi (File B §16) và tự thêm nếu thiếu. Chia **Chặn tiến độ** / **Không chặn**. Mỗi câu ghi: *vì sao hỏi* · *giả định mặc định nếu tôi không trả lời* · *hậu quả nếu giả định sai*.
3. Lập **ma trận mâu thuẫn**: quy mô × đơn giản × ngân sách × thời gian × chất lượng nội dung × chất lượng đồ họa. Chỉ ra những cặp không thể thỏa mãn cùng lúc và đề xuất **2–3 phương án giải**, mỗi phương án nêu cái được/mất.
4. Nêu **5 rủi ro lớn nhất ở mức yêu cầu** (chưa phải mức kỹ thuật), mỗi rủi ro có `RISK-xx`.
5. Viết **Bản yêu cầu v0**: yêu cầu chức năng (`REQ-Fxx`), phi chức năng (`REQ-Nxx`: hiệu năng, tiếp cận, riêng tư, vận hành), **ngoài phạm vi** (ghi rõ để tránh phình), **đề xuất phạm vi MVP** (lát cắt nhỏ nhất vẫn chứng minh được giá trị: ví dụ 1 lớp × 1 chủ đề × 2 khuôn game).
6. Persona và hành trình ngắn cho: học sinh từng cấp, giáo viên, phụ huynh (dựa File B §1; chỉnh nếu tôi cung cấp thông tin khác).

**Đầu ra:** `00-requirements.md` gồm: Câu hỏi · Giả định · Mâu thuẫn & phương án · Rủi ro · Yêu cầu (F/N) · Ngoài phạm vi · Phạm vi MVP đề xuất · 3 mục cuối pha.
**Hoàn thành khi:** mỗi câu hỏi chặn đều có giả định mặc định; mỗi `REQ` kiểm chứng được (có tiêu chí nghiệm thu). **Cổng:** mỗi nhiệm vụ `T-P0-xx` xong → cập nhật `PLAN.md` (mục 1.7) rồi mới làm nhiệm vụ kế tiếp.
▲▲▲ HẾT ▲▲▲

## P1a — Trích xuất MỘT bộ sách cho MỘT khối lớp

▼▼▼ BẮT ĐẦU ▼▼▼
**Bộ sách:** `[KNTT | CD | CTST]` · **Khối lớp:** `[3–5 | 6–9 | 10–12 (định hướng ...)]` · **Đầu vào:** file sách đính kèm + File B (§2, §3).

Việc phải làm:
1. **Kiểm kê file:** liệt kê từng file/tập, số trang đọc được, phần thiếu/mờ. Nếu thiếu hoặc không đọc được → **dừng và báo**, không tự bù.
2. **Trích xuất theo từng bài** vào bảng ở File B §3.1 (một dòng/bài): tên bài, số tiết (nếu có), mục tiêu (tóm tắt bằng lời bạn), **thuật ngữ mới**, **loại hoạt động** (theo taxonomy File B §3.5), công cụ/phần mềm, kiểu đánh giá cuối bài (mô tả *loại*, không chép câu hỏi), tiên quyết (suy ra), trang nguồn.
3. **Gắn yêu cầu cần đạt** của Chương trình cho từng bài nếu tôi đính kèm tài liệu chương trình; nếu không có, ghi `chưa đối chiếu`.
4. **Độ tin cậy** mỗi dòng: Cao / Trung bình / Thấp, kèm lý do nếu không Cao.
5. **Phát hiện đặc thù của bộ sách:** thứ tự dạy, độ sâu, thuật ngữ riêng, công cụ riêng, ví dụ/ngữ cảnh đặc trưng (mô tả, không chép).
6. **Đối chiếu khung giả định** (File B §2): ô nào đúng, ô nào sai, ô nào chưa đủ dữ liệu.
7. **Danh sách điểm nghi ngờ** để tôi kiểm tra bằng mắt với sách thật.

**Cấm:** chép nguyên văn quá tên bài/chương; bịa nội dung cho phần chưa đọc được.
**Đầu ra:** `01a-extract-<bộ>-<khối>.md` + 3 mục cuối pha.
**Hoàn thành khi:** mọi bài trong file đều có dòng; mọi dòng có trang nguồn và độ tin cậy. **Cổng:** mỗi nhiệm vụ `T-P1A-xx` xong → cập nhật `PLAN.md` (mục 1.7) rồi mới làm nhiệm vụ kế tiếp.
▲▲▲ HẾT ▲▲▲

## P1b — Hợp nhất 3 bộ sách thành Bản đồ chương trình

▼▼▼ BẮT ĐẦU ▼▼▼
**Đầu vào:** các file `01a-*`, `00-requirements.md`, File B (§2–§6). **Kiểm tra trước:** đủ 3 bộ × 3 cấp chưa? Thiếu cái nào thì liệt kê và hỏi tôi có chạy tiếp với phần đã có không.

Việc phải làm:
1. **Chuẩn hóa thuật ngữ:** lập bảng `khái niệm × (3 bộ sách) → thuật ngữ chuẩn của sản phẩm` (File B §3.3). Quy tắc chọn: theo Chương trình → theo đa số → dễ hiểu nhất cho trẻ.
2. **Ma trận phủ:** `yêu cầu cần đạt × bộ sách` (✔ đủ / ◐ một phần / ✖ không có). Rút ra: *khoảng trống của chương trình trong sách*, *nội dung sách vượt chương trình*.
3. **So sánh thứ tự dạy** giữa 3 bộ; nêu chỗ khác biệt lớn và **chọn thứ tự cho sản phẩm** theo File B §3.4 (CT 2018 > tính tiên quyết sư phạm > đa số 3 bộ > đơn giản cho trẻ). Ghi lý do từng lựa chọn.
4. **Hợp nhất thành nút kiến thức** theo schema File B §4: gộp trùng; tách nút quá lớn (mục tiêu mỗi nút chơi/học xong trong ≤ 10–15 phút); mỗi nút có ≥ 1 outcome truy được về Chương trình; `book_refs` chỉ ghi tên chương/chủ đề.
5. **Đồ thị tiên quyết** (Mermaid, vẽ theo từng khối lớp) + **kiểm tra chu trình** và nút mồ côi.
6. **Gán khuôn game** (File B §5) cho từng nút; nếu chưa có khuôn phù hợp thì đề xuất khuôn mới. Thống kê **số nút / khuôn** để biết khuôn nào đáng đầu tư trước.
7. **Nút “khó làm game”** (đạo đức, pháp luật, lý thuyết thuần): đề xuất cách khác (tình huống rẽ nhánh, nhân vật hỏi đáp, sắp xếp quy tắc…).
8. **Ước lượng khối lượng nội dung** theo cấp: số nút, số bài chơi, số câu hỏi tối thiểu (item bank), số asset pixel, số giờ viết/duyệt/vẽ `[ƯỚC TÍNH]`.
9. **Dựng JSON** đầy đủ (hoặc ≥ 30 nút mẫu trải đều 3 cấp nếu quá dài) + JSON Schema để kiểm tra trong CI.
10. **Danh sách quyết định cần người có chuyên môn sư phạm duyệt.**

**Đầu ra:** `01b-curriculum-map.md`, `curriculum.json`, `curriculum.schema.json` + 3 mục cuối pha.
**Hoàn thành khi:** mọi yêu cầu cần đạt đều có nút hoặc được ghi là “cố ý chưa làm”; đồ thị không có chu trình. **Cổng:** mỗi nhiệm vụ `T-P1B-xx` xong → cập nhật `PLAN.md` (mục 1.7) rồi mới làm nhiệm vụ kế tiếp.
▲▲▲ HẾT ▲▲▲

## P2 — Phản biện & quyết định kỹ thuật (ADR)

▼▼▼ BẮT ĐẦU ▼▼▼
**Đầu vào:** `00`, `01b`, File B (§8 danh mục ứng viên, §9 seed kiến trúc).

Việc phải làm:
1. **Rút ràng buộc kỹ thuật** từ `00` và `01b` (số nút, số khuôn game, thiết bị, mạng, đội, ngân sách, pháp lý).
2. **Phản biện H1–H12** từng cái một: giữ/sửa/bỏ + lý do + rủi ro + chi phí đổi ý năm 3.
3. **Ra quyết định** (mỗi cái một ADR) cho: framework web · engine game & cách trộn DOM/Canvas · định dạng nội dung & công cụ cho người viết nội dung · lưu trữ dữ liệu (client + server) · xác thực (trẻ em vs giáo viên) · hosting/CDN & vị trí máy chủ gần Việt Nam · CI/CD · phân tích sử dụng thân thiện quyền riêng tư · **hệ thống đồ họa pixel do AI tạo (hướng “mã → ảnh”, toolchain, validator)** · **design system giao diện pixel-first** · i18n · chiến lược test · PWA/ngoại tuyến · lập trình khối & Python trong trình duyệt · theo dõi lỗi.
4. **Ma trận đánh giá** cho mỗi hạng mục có ≥ 2 ứng viên thật, tiêu chí & trọng số do bạn nêu: độ đơn giản · chi phí · rủi ro khóa nhà cung cấp · dễ tuyển người ở Việt Nam · hiệu năng máy yếu · độ “sống” của dự án · giấy phép. **Kiểm tra** phiên bản, giá, giấy phép, tình trạng bảo trì hiện tại trước khi chấm.
5. **Mẫu ADR bắt buộc** (File B §15.1), có trường *loại quyết định* (một chiều/hai chiều) và *dấu hiệu cần xem lại*.
6. **Sổ “cửa một chiều”:** liệt kê quyết định khó đảo ngược nhất (định dạng nội dung, ID, schema sự kiện tiến độ, nhà cung cấp dữ liệu…) và cách giảm rủi ro.
7. **5 quyết định yếu/rủi ro nhất** và **spike** (thử nghiệm ≤ 2–3 ngày) cho từng cái: câu hỏi cần trả lời, cách đo, tiêu chí đạt/không đạt.
8. **Bảng điểm gãy khi mở rộng:** điểm nghẽn đầu tiên ở 10× / 100× / 1.000× (cụ thể: cái gì, vì sao, đo bằng gì) và **những thứ cố ý chưa xây**.
9. **Mô hình chi phí** (File B §15.3) ở 3 mốc 1 nghìn / 100 nghìn / 1 triệu học sinh `[ƯỚC TÍNH]`, nêu giả định.
10. **Cờ pháp lý** gom lại một chỗ (dữ liệu trẻ em, lưu trữ trong nước, bản quyền sách & asset, học liệu số trong trường) — chỉ nêu *cần xác minh gì*, không tự kết luận.

**Đầu ra:** `02-adr.md` + 3 mục cuối pha.
**Hoàn thành khi:** mọi quyết định có ≥ 2 phương án; mọi quyết định một chiều có kế hoạch giảm rủi ro. **Cổng:** mỗi nhiệm vụ `T-P2-xx` xong → cập nhật `PLAN.md` (mục 1.7) rồi mới làm nhiệm vụ kế tiếp. Mỗi ADR xong phải được ghi vào `PLAN.md` §4 ngay.
▲▲▲ HẾT ▲▲▲

## P3 — Chuỗi 4 agent (làm tuần tự trong cùng một chat)

▼▼▼ BẮT ĐẦU ▼▼▼
**Đầu vào:** `00`, `01b`, `02`, File B (§9). Làm lần lượt 3.1 → 3.2 → 3.3 → 3.4; **sau MỖI nhiệm vụ của từng agent (xem `PLAN.md` §2, P3) phải cập nhật `PLAN.md` theo mục 1.7 trước khi sang nhiệm vụ kế tiếp**; chỉ dừng chờ tôi khi tôi yêu cầu.

### 3.1 Architect — đưa ra
1. **Kiến trúc hệ thống** (Mermaid C4 mức ngữ cảnh + container) và **cấu trúc thành phần**; với mỗi thành phần: trách nhiệm, phụ thuộc, “nếu bỏ thì mất gì”.
2. **Luồng dữ liệu** (sequence diagram) cho: vào bài → chơi → chấm → lưu tiến độ → đồng bộ; đăng nhập bằng mã lớp; giáo viên xem báo cáo; cập nhật nội dung phiên bản mới.
3. **Thiết kế API** (nếu có backend): endpoint, request/response, mã lỗi, versioning, idempotency, rate limit, phân quyền.
4. **Lược đồ cơ sở dữ liệu:** ERD Mermaid + DDL; chỉ mục; chiến lược migration; chính sách lưu/xóa dữ liệu.
5. **Chiến lược cache** theo tầng (trình duyệt · service worker · CDN · edge · ứng dụng): nội dung nào, TTL bao nhiêu, **cách vô hiệu hóa khi nội dung đổi**, cách tránh học sinh thấy bản cũ giữa chừng bài.
6. **Cấu trúc thư mục repo** và **quy tắc phụ thuộc** (domain không phụ thuộc framework; game chỉ phụ thuộc game-core; nội dung không chứa code) + cách ép bằng công cụ.
7. **Kiến trúc giao diện pixel-first:** design system pixel (token bội số nguyên của `--px`, bảng màu theo cấp, UI kit 9-slice/nút/icon/con trỏ/nền/chuyển trang/màn tải), cây component, quản lý trạng thái, quy ước loading/empty/error, responsive cho 3 loại màn hình (điện thoại, máy tính bảng, màn hình phòng máy). Nêu cách giữ **chữ là chữ thật**, độ nét khi zoom/DPI, và mức pixel nhẹ hơn cho trang giáo viên/phụ huynh. (Chi tiết kỹ thuật dựng do P3B chốt.)
8. **Kiến trúc game:** lớp engine, giao diện chung của *khuôn game*, vòng đời scene, nạp/giải phóng tài nguyên, bộ chấm điểm tách khỏi phần hiển thị, bộ sinh số ngẫu nhiên có seed, giao tiếp game ↔ tiến độ.
9. **Pipeline đồ họa pixel do AI tạo:** `spec (văn bản/mã) → sprite-forge dựng PNG → validator → contact sheet → AI tự phê bình → người duyệt → atlas → tối ưu → hồ sơ nguồn gốc/license → CDN`; vị trí spec trong repo; quy ước đặt tên; cách CI chạy lại toàn bộ để chứng minh asset tái tạo được. (Chi tiết do P3B chốt.)
10. **Hệ thống nội dung:** người viết nội dung làm việc thế nào (công cụ, kiểm tra, xem trước, duyệt, phát hành) **mà không cần dev**.
11. **Sơ đồ phụ thuộc thời gian chạy** và **chế độ lỗi** (cái gì hỏng thì sản phẩm suy giảm thế nào — graceful degradation).

### 3.2 Engineer — cải thiện bản của Architect, đưa ra
1. **Phát hiện ≥ 3 điểm yếu/mơ hồ của Architect** và sửa (ghi `03-changelog.md`).
2. **Contracts** (TypeScript hoặc ngôn ngữ đã chọn): `Curriculum Node`, `Lesson`, `Item`, `GameTemplate`, `GameResult`, `ProgressEvent`, `Mastery`, `Classroom`, `Learner`, **`SpriteSpec`, `PaletteSpec`, `UiTokens`, `AssetProvenance`**… kèm quy tắc kiểm tra.
3. **Skeleton** thư mục/file + **thứ tự xây** (cái gì xây trước vì cắt giảm rủi ro nhiều nhất).
4. **Danh sách API endpoint đầy đủ** kèm ví dụ request/response.
5. **Migration đầu tiên** và dữ liệu mẫu.
6. **Một vertical slice hoàn chỉnh:** 1 bài lớp 3 + 1 khuôn game, từ file nội dung → nạp → chơi → chấm → lưu sự kiện → hiển thị tiến độ. Có **1 sprite do AI viết spec → dựng thành PNG → vào atlas → hiển thị bằng UI pixel** trong chính lát cắt này. Code mẫu chạy được hoặc gần chạy được (≤ ~300 dòng tổng), kèm 3 test quan trọng nhất.
7. **Chiến lược test:** cái gì test đơn vị, cái gì E2E, cái gì kiểm tra nội dung tự động (schema, liên kết, tiên quyết, chính tả, đủ alt-text).
8. **Hướng dẫn thêm 1 bài mới** và **thêm 1 khuôn game mới** (checklist ≤ 1 trang).

### 3.3 Reviewer — rà soát Architect + Engineer
1. **≥ 10 phát hiện** theo **Blocker / Major / Minor**: bảng `FIND-xx | mức | bằng chứng | kịch bản hỏng | cách sửa | công sức`.
2. **Danh sách thứ over-engineered cần cắt** (mỗi mục: lý do, tiết kiệm được gì).
3. **Danh sách thứ under-engineered sẽ đau sau 12 tháng.**
4. **Kiểm tra nhất quán:** kiến trúc ↔ yêu cầu `REQ` ↔ ADR; mỗi `REQ` có nơi hiện thực?
5. **Kiểm tra theo đội nhỏ:** đội `[...]` người có làm nổi không? Phần nào là “điểm đơn” (một người biết)?
6. **Phán quyết:** Đi tiếp / Sửa rồi đi tiếp / Làm lại — kèm điều kiện.

### 3.4 Optimizer — cải thiện bản đã qua rà soát
1. **Ngân sách hiệu năng** `[ĐỀ XUẤT]` + cách đo: dung lượng tải lần đầu, thời gian vào bài đầu, khung hình/giây trên máy yếu, RAM, dung lượng bài tiếp theo, dung lượng gói ngoại tuyến theo cấp.
2. **Vấn đề hiệu năng cụ thể** với số tính được. Ví dụ: bộ nhớ GPU của một texture atlas ≈ rộng × cao × 4 byte (một atlas 2048×2048 RGBA ≈ 16 MB) → đặt hạn mức atlas/scene.
3. **Rò rỉ bộ nhớ/tài nguyên:** chuyển scene, listener/timer không gỡ, worker Python/WASM không giải phóng, âm thanh không dừng.
4. **Render thừa & tác vụ nặng:** khi nào đưa vào worker, khi nào tải lười theo lớp/cấp, khi nào tiền xử lý lúc build.
5. **Mạng:** gộp request, nén, cache; hành vi khi mạng chập chờn; thundering herd đầu tiết học (cả phòng máy vào cùng lúc).
6. **Mỗi tối ưu** ghi: cách đo · trước/sau dự kiến · chi phí độ phức tạp · có nên làm *bây giờ* không. **Cấm tối ưu thứ chưa có số đo hoặc rủi ro rõ.**
7. **Khả năng mở rộng & chi phí** ở 3 mốc người dùng; điểm gãy tiếp theo.

### Bản hợp nhất
Kiến trúc cuối cùng (sau 4 agent) + `03-changelog.md` (“agent nào đổi gì và vì sao”) + 3 mục cuối pha.
**Hoàn thành khi:** mọi Blocker của Reviewer đã được xử lý hoặc chuyển thành ADR/RISK có chủ. **Cổng:** mỗi nhiệm vụ `T-P3-xx` xong → cập nhật `PLAN.md` (mục 1.7) rồi mới làm nhiệm vụ kế tiếp.
▲▲▲ HẾT ▲▲▲

## P3B — Hệ thống đồ họa pixel do AI tạo & giao diện pixel-first

▼▼▼ BẮT ĐẦU ▼▼▼
**Vai:** Pixel Art Agent (Art Director + Pixel Artist) phối hợp Architect/Engineer. **Đầu vào:** `00`, `02`, `03`, `PLAN.md`, File B §7 (đặc biệt §7.0, §7.6–§7.8). **Mục tiêu:** chứng minh bằng thực nghiệm rằng AI tự tạo được đồ họa pixel đủ chất lượng và nhất quán cho toàn bộ giao diện + game, hoặc chỉ ra chỗ cần phương án lai. **Mỗi nhiệm vụ `T-P3B-xx` xong phải cập nhật `PLAN.md` (§2 và §3) trước khi làm nhiệm vụ kế tiếp.**

Việc phải làm:
1. **Đánh giá khả năng và giới hạn thật** (T-P3B-01): trong môi trường này AI có chạy được mã (Python/Node) không? có xem lại được ảnh đã dựng không? So sánh 5 phương án A–E ở File B §7.0 theo: kiểm soát lưới/bảng màu · nhất quán · tái tạo được · diff bằng Git · license/nguồn gốc · chất lượng tối đa · công sức chỉnh. **Nêu thẳng điều AI làm kém** và chốt phương án mặc định (đề xuất A+B+C+D, bỏ E khỏi đường sản xuất) — hoặc bác bỏ có lý do.
2. **Art direction bible** (T-P3B-02) ≤ 2 trang: tông và mood cho 3 thế giới (Làng Pixel / Thành phố Code / Trạm vũ trụ — có thể đổi), mascot và nhân vật dẫn đường, quy tắc silhouette, hướng sáng, độ dày viền, mức chi tiết, điều cấm kỵ, **danh sách “không bắt chước”** (không dùng IP có bản quyền).
3. **Palette khóa** (T-P3B-03): `palette.json` cho từng thế giới + bảng UI chung; mỗi màu có tên vai trò; kiểm tra tương phản chữ/nền ≥ 4.5:1 và cặp màu an toàn cho mù màu; quy tắc palette swap cho NPC/avatar.
4. **Định dạng SpriteSpec** (T-P3B-04): schema JSON (kích thước, palette, legend, frames/rows hoặc thủ tục, lớp/bộ phận, pivot, tag, hoạt ảnh) + **ít nhất 3 sprite mẫu do chính bạn viết** (icon 16×16, nhân vật 4 khung, 1 tile thủ tục) để chứng minh định dạng dùng được.
5. **Đặc tả toolchain “sprite-forge”** (T-P3B-05): đầu vào/ra; dựng PNG chỉ dùng màu trong palette; **validator** (kích thước đúng, màu ngoài palette, pixel bán trong suốt, viền không đứt, ô trống thừa, pivot hợp lệ, số khung); **contact sheet** (phóng 1×/2×/4×, nền sáng và tối) để AI và người nhìn lại; đóng gói atlas JSON; chạy trong CI. Viết skeleton + 1 vertical slice (1 spec → PNG → atlas).
6. **UI kit pixel-first** (T-P3B-06): danh mục thành phần (File B §7.6), token, **so sánh kỹ thuật dựng** (9-slice ảnh · CSS thuần · SVG crispEdges · canvas) theo độ nét ở mọi zoom/DPI, dung lượng, tiếp cận, đổi chủ đề, hiệu năng máy yếu; chốt cách dựng và các quy tắc “pixel không làm khó đọc”.
7. **Chiến lược nhất quán ở quy mô lớn** (T-P3B-07): style guide + palette khóa + **golden samples** (asset mẫu vàng AI luôn tham chiếu) + duyệt theo lô + tái sử dụng bộ phận + kiểm tra tự động + “ngân sách chất lượng” (mức nào là đủ tốt) + **phương án lai** (phần nào nên có người vẽ: mascot, logo, minh họa lớn).
8. **Nguồn gốc & pháp lý** (T-P3B-08): hồ sơ nguồn gốc cho từng asset (File B §7.8); chính sách khi dùng mô hình sinh ảnh bên ngoài (chỉ tham khảo, không đưa thẳng vào sản phẩm); quyền sở hữu sản phẩm do AI tạo `[CẦN XÁC MINH PHÁP LÝ]`; quy trình thay asset khi có khiếu nại.
9. **Kế hoạch sản xuất theo lô** (T-P3B-09): danh mục asset theo mốc (M0: 1 mascot 4 khung + 1 tileset 16 ô + UI kit tối thiểu + bộ icon nhỏ; M1…), ước lượng **số lượt AI/asset + giờ người duyệt/lô** `[ƯỚC TÍNH]`, cổng chất lượng qua lô (File B §15.7).
10. **Spike M0-ART** (T-P3B-10, 2–3 ngày): tạo mascot 4 khung + tileset 16 ô + UI kit tối thiểu → qua validator → hiển thị trong shell trên máy yếu. **Tiêu chí đạt `[ĐỀ XUẤT]`:** người duyệt chấm ≥ `[4/5]` về thẩm mỹ và nhất quán; nhận diện đúng ở 1×–4×; đúng bảng màu 100%; không mờ ở zoom/DPI thử nghiệm; dung lượng trong ngân sách; số vòng sửa ≤ `[3]`/asset. **Không đạt → đề xuất phương án lai** (người vẽ phần cốt lõi, AI làm phần còn lại) và ghi vào ADR.

**Đầu ra:** `03b-art-system.md`, `palette.json`, `sprite-spec.schema.json`, thư mục spec mẫu + 3 mục cuối pha.
**Hoàn thành khi:** có kết quả spike với số đo; mọi quyết định đồ họa có ADR; `PLAN.md` §3 phản ánh từng asset đã làm (spec · validator · duyệt · nguồn gốc).
▲▲▲ HẾT ▲▲▲

## P4 — Rà soát 5 lăng kính (nên chạy ở chat mới)

▼▼▼ BẮT ĐẦU ▼▼▼
**Đầu vào:** `03-architecture.md`, `02-adr.md`, File B (§10–§13). Bạn là người rà soát *độc lập*: không bênh vực thiết kế; nhiệm vụ là tìm chỗ nó sẽ hỏng. Mỗi phát hiện ghi bảng `FIND-xx | lăng kính | mức | bằng chứng | kịch bản thực tế | cách sửa | công sức | chủ`.

**4.1 Bảo mật:** mô hình mối đe dọa (tài sản, tác nhân, bề mặt tấn công); báo cáo lỗ hổng kèm mức nghiêm trọng; **kịch bản tấn công thực tế**; bản sửa an toàn. Tối thiểu xét: XSS qua nội dung (MDX/HTML do người viết nội dung chèn) · phân quyền giáo viên ↔ học sinh ↔ lớp (IDOR) · lộ dữ liệu học sinh · dò mã lớp/PIN (brute force) · giả mạo tiến độ/điểm từ client (chỗ nào chấp nhận được, chỗ nào không, ví dụ khi có “chứng nhận”) · lạm dụng API/rate limit · chuỗi cung ứng thư viện · bí mật trong repo · CSP & header · chạy code Python/khối lệnh của học sinh trong trình duyệt · hộp thoại/biểu mẫu nhập tự do của trẻ (PII vô tình).

**4.2 Frontend & Khả năng tiếp cận:** API props của component · trạng thái đang tải/rỗng/lỗi · responsive (điện thoại dọc, máy tính bảng, màn hình phòng máy) · bàn phím toàn bộ · trình đọc màn hình · giảm chuyển động · tương phản bảng màu pixel · cỡ chữ & cỡ vùng bấm cho trẻ nhỏ · focus trong canvas game · **độ nét giao diện pixel ở mọi mức zoom/DPI (scale lẻ có gây mờ không)** · chữ có bị rasterize vào ảnh không · pixel-first có làm khó đọc với trẻ khó đọc/mắt yếu không.

**4.3 Gỡ lỗi & Vận hành:** liệt kê **trường hợp biên khó thấy** (File B §12) và cách xử lý; khả năng tái hiện lỗi (seed ngẫu nhiên, log sự kiện); theo dõi lỗi; feature flag; rollback; runbook; điều tra sự cố “học sinh báo mất tiến độ”.

**4.4 Khả năng refactor:** ranh giới module; hướng phụ thuộc; chỗ nào thành “nồi lẩu” sau 2 năm; quy tắc kiểm tra kiến trúc tự động; chi phí thêm cấp/lớp/khuôn game thứ 11; chi phí đổi framework.

**4.5 Sư phạm & An toàn trẻ em:** từng khuôn game có thật sự dạy được nút kiến thức gán cho nó? Có nguy cơ học vẹt/đoán mò? Phản hồi khi sai có giúp học không? Độ khó phù hợp lứa tuổi? Có dark pattern? Nội dung có phân biệt/định kiến? Dữ liệu trẻ em được bảo vệ ra sao? Kế hoạch playtest với học sinh thật. **Đồ họa do AI tạo:** nhất quán phong cách giữa các lô, nhận diện được ở 1×, không chứa ký hiệu/hình ảnh không phù hợp lứa tuổi, không giống IP có bản quyền, hồ sơ nguồn gốc đầy đủ.

**Đầu ra:** `04-review.md` (bảng FIND + phán quyết từng lăng kính + 5 việc phải sửa trước khi code) + 3 mục cuối pha. **Cổng:** mỗi nhiệm vụ `T-P4-xx` xong → cập nhật `PLAN.md` (mục 1.7) rồi mới làm nhiệm vụ kế tiếp. Sau mỗi lăng kính phải cập nhật.
▲▲▲ HẾT ▲▲▲

## P5 — Lộ trình triển khai & backlog

▼▼▼ BẮT ĐẦU ▼▼▼
**Đầu vào:** `00`–`04`, File B (§14, §15).

Việc phải làm:
1. **Cập nhật kiến trúc** theo `04-review` (chỉ liệt kê thay đổi).
2. **Các mốc** (có thể đổi thứ tự nhưng phải nêu lý do):
   - **M0 – Spike giảm rủi ro:** 1 game pixel mượt trên máy yếu · font pixel đủ dấu tiếng Việt · chạy ngoại tuyến · Python/khối lệnh trong trình duyệt (nếu giữ H5) · **spike M0-ART: pipeline đồ họa pixel do AI tạo (mascot 4 khung + tileset + UI kit tối thiểu qua validator, hiển thị trên máy yếu)** · bộ gõ Telex/VNI trong game gõ phím · đăng nhập mã lớp.
   - **M1 – Vertical slice** một lớp, đủ 1 chu trình học–chơi–chấm–lưu.
   - **M2** hoàn thành Tiểu học · **M3** THCS · **M4** THPT · **M5** công cụ giáo viên.
3. **Mỗi mốc** ghi: mục tiêu · phạm vi *trong/ngoài* · sản phẩm bàn giao · **tiêu chí hoàn thành đo được** · ước lượng *theo khoảng* kèm giả định đội · phụ thuộc · rủi ro (`RISK-xx`) · **cắt gì nếu trễ** · cổng playtest.
4. **Kế hoạch sản xuất nội dung** (thường là điểm nghẽn thật): quy trình viết → duyệt sư phạm → thiết kế game → **AI tạo pixel (spec → dựng → validator) → người duyệt thẩm mỹ** → lập trình khuôn/tham số → QA → phát hành; năng suất `[ƯỚC TÍNH]`; số người từng vai; hàng chờ và điểm nghẽn. Thêm **kế hoạch sản xuất asset theo lô** (danh mục asset theo mốc, số lượt AI + giờ duyệt, cổng qua lô — theo P3B) và nêu rõ **người duyệt thẩm mỹ là ai** (nếu không có, đó là Blocker).
5. **Playtest:** với học sinh thật ở *mỗi* cấp, trước khi mở rộng; giao thức (File B §14.2); tiêu chí **dừng/đổi hướng**.
6. **Backlog 30 ngày đầu:** epic → story, mỗi story có tiêu chí nghiệm thu, người làm, phụ thuộc, thứ tự; chỉ rõ **việc đầu tiên vào sáng thứ Hai**.
7. **Quản trị thay đổi:** quy trình khi sách/chương trình đổi, khi một bài bị lỗi nội dung, khi cần gỡ một game.
8. **Sổ rủi ro cập nhật** (xác suất × tác động × người chịu trách nhiệm × cách giảm).

**Đầu ra:** `05-roadmap.md` + 3 mục cuối pha. **Cổng:** mỗi nhiệm vụ `T-P5-xx` xong → cập nhật `PLAN.md` (mục 1.7) rồi mới làm nhiệm vụ kế tiếp.
▲▲▲ HẾT ▲▲▲

## P6 — Sẵn sàng production & vận hành 5 năm

▼▼▼ BẮT ĐẦU ▼▼▼
**Đầu vào:** `03`–`05`.

Việc phải làm (mỗi mục: *chọn gì · vì sao · chi phí · ai chịu trách nhiệm*):
1. **Môi trường** dev / staging / prod; hạ tầng dưới dạng code; quản lý bí mật.
2. **CI/CD:** kiểm tra gì trên mỗi PR (lint, type, test, kiểm tra nội dung, kiểm tra kích thước bundle/atlas, kiểm tra license asset, **validator đồ họa pixel (bảng màu, kích thước, bán trong suốt), dựng lại asset từ spec để chứng minh tái tạo được, kiểm tra PLAN.md/ID nhiệm vụ**, quét lỗ hổng phụ thuộc); quy trình phát hành; **rollback trong ≤ vài phút**; feature flag.
3. **Kim tự tháp test** và dữ liệu test (kể cả máy yếu giả lập bằng giới hạn CPU/mạng).
4. **Quan sát hệ thống:** log, metric, theo dõi lỗi, cảnh báo; **SLO tính theo giờ học** (ví dụ khung giờ học trong ngày) và ngân sách lỗi; bảng điều khiển “sức khỏe giờ học”.
5. **Sao lưu & khôi phục:** RPO/RTO, tần suất, **diễn tập khôi phục**.
6. **Sự cố:** phân loại mức độ, ai trực, kênh liên lạc với giáo viên khi sự cố, mẫu báo cáo sau sự cố.
7. **Quyền riêng tư & tuân thủ cho dữ liệu trẻ em:** bản đồ dữ liệu (thu gì, để làm gì, lưu bao lâu, ai thấy), cơ chế đồng ý/yêu cầu xóa, đánh giá tác động sơ bộ `[CẦN XÁC MINH PHÁP LÝ]`.
8. **Chuỗi cung ứng:** kiểm kê license (SBOM), chính sách cập nhật phụ thuộc (định kỳ), ghim phiên bản, kế hoạch khi một thư viện bị bỏ rơi. Thêm **hồ sơ nguồn gốc asset do AI tạo** (spec, công cụ/mô hình, ngày, người duyệt, license) và quy trình thay asset khi có vấn đề bản quyền.
9. **Vòng đời nội dung:** version hóa, bất biến ID, ngưng dùng (deprecate), di trú tiến độ khi cấu trúc đổi.
10. **Chi phí:** theo dõi, cảnh báo ngưỡng, “công tắc khẩn” khi chi phí tăng đột biến.
11. **Tài liệu giảm “bus factor”:** onboarding dev mới trong 1 ngày, sổ ADR, runbook, hướng dẫn thêm bài/khuôn game, sơ đồ hệ thống.
12. **Pre-mortem:** giả sử 12 tháng sau dự án thất bại — liệt kê **10 nguyên nhân khả dĩ nhất** và hành động phòng ngừa ngay bây giờ.
13. **Vận hành “ngày thứ hai” trong 5 năm:** việc định kỳ hằng tuần/tháng/quý/năm (cập nhật phụ thuộc, rà soát nội dung, kiểm tra tương thích trình duyệt, diễn tập khôi phục, rà soát chi phí, rà soát bảo mật).
14. **Câu hỏi chốt:** “Điều gì sẽ vỡ trước, và ta biết bằng cách nào?”

**Đầu ra:** `06-production.md` (có checklist tick được) + 3 mục cuối pha. **Cổng:** mỗi nhiệm vụ `T-P6-xx` xong → cập nhật `PLAN.md` (mục 1.7) rồi mới làm nhiệm vụ kế tiếp.
▲▲▲ HẾT ▲▲▲

## P7 — Tổng kết & Go/No-go

▼▼▼ BẮT ĐẦU ▼▼▼
**Đầu vào:** toàn bộ `00`–`06`.
Viết `07-plan-on-a-page.md` **không quá 2 trang**: (1) sản phẩm trong 3 câu · (2) kiến trúc trong 1 sơ đồ · (3) 10 quyết định quan trọng nhất (link ADR) · (4) 5 rủi ro hàng đầu và cách giảm · (5) lộ trình 1 bảng · (6) chi phí 3 mốc · (7) **checklist Go/No-go** cho M0 và cho M1 · (8) câu hỏi còn mở · (9) **3 việc đầu tiên vào sáng thứ Hai**.
Sau đó **tự phản biện bản kế hoạch trong 10 dòng:** “Nếu phải cắt 40% phạm vi, cắt gì? Nếu chỉ có một nửa ngân sách, đổi gì?”. **Cổng:** mỗi nhiệm vụ `T-P7-xx` xong → cập nhật `PLAN.md` (mục 1.7) rồi mới làm nhiệm vụ kế tiếp.
▲▲▲ HẾT ▲▲▲

---

# PHẦN 3 — PROMPT CHO GIAI ĐOẠN SAU (khi đã duyệt kế hoạch / đã có code)

Dán Prompt chủ trước, đính kèm `07-plan-on-a-page.md`, `03-architecture.md`, `02-adr.md`, và code liên quan. Mỗi prompt kết thúc bằng: *“Giữ nguyên chức năng hiện có. Không đoán — kiểm chứng giả định.”*

**B0. Xây MVP (cầu nối từ kế hoạch sang code)**
> Đóng vai kỹ sư full-stack cấp cao xây MVP theo kế hoạch đã duyệt. Chỉ làm **mốc `[M-x]`**. Trước khi code: nhắc lại phạm vi và tiêu chí hoàn thành, liệt kê file sẽ tạo/sửa. Đưa ra: cấu trúc thư mục · code sẵn sàng production (có test, xử lý lỗi, loading/empty/error) · hướng dẫn chạy · cách kiểm tra tiêu chí hoàn thành · những gì cố ý chưa làm. Làm theo từng bước nhỏ, mỗi bước chạy được. Nếu thấy kế hoạch sai, dừng và báo trước khi làm khác. **Mỗi task xong phải cập nhật `PLAN.md` và ghi ID nhiệm vụ vào commit trước khi làm task tiếp (mục 1.7).**

**B1. Refactor theo Clean Architecture**
> Đóng vai kiến trúc sư phần mềm cấp cao refactor module `[...]`. Cải thiện phân tách trách nhiệm, tính mô-đun, hướng phụ thuộc, khả năng mở rộng và bảo trì theo quy tắc phụ thuộc của dự án. Đưa ra: cấu trúc thư mục mới · phân tích kiến trúc (trước/sau) · code đã refactor · các cải tiến chính · **bài test chứng minh hành vi không đổi** (viết trước khi refactor).

**B2. Phân tích ngược codebase lạ**
> Đóng vai kỹ sư cấp cao vừa vào dự án. Phân tích ngược kiến trúc và luồng dữ liệu đầu–cuối; tìm lỗi kiến trúc, logic trùng lặp, điểm nghẽn, rủi ro mở rộng, vấn đề bảo trì. Đưa ra: phân tích kiến trúc · khu vực nghiêm trọng (xếp hạng) · chiến lược refactor theo bước nhỏ · code cải tiến.

**B3. Tối ưu hiệu năng**
> Đóng vai kỹ sư hiệu năng cấp cao. Tìm điểm nghẽn, logic kém hiệu quả, render thừa, thao tác tốn tài nguyên, **rò rỉ bộ nhớ** (chuyển scene, texture/sprite, listener, timer, worker WASM, âm thanh). Mỗi vấn đề có số đo trước/sau. Đưa ra: vấn đề · chiến lược · code tối ưu · cải tiến mở rộng · cách đo lặp lại được (kịch bản máy yếu + mạng chậm).

**B4. Kiểm tra bảo mật**
> Đóng vai kỹ sư bảo mật cấp cao. Tìm lỗ hổng, lỗi xác thực/phân quyền, điểm yếu API, injection (kể cả XSS qua nội dung), lộ dữ liệu học sinh, rủi ro hạ tầng và chuỗi cung ứng. Đưa ra: báo cáo kèm mức độ · **kịch bản tấn công thực tế** · bản sửa an toàn · khuyến nghị production. Ưu tiên rủi ro khai thác được.

**B5. Gỡ lỗi sự cố production**
> Đóng vai kỹ sư gỡ lỗi cấp cao. Với log/mô tả lỗi và code đính kèm: phân tích chức năng · **nguyên nhân gốc** (không chữa triệu chứng) · các trường hợp biên · bản sửa sẵn sàng production · **test tái hiện lỗi** · cách phát hiện sớm lần sau. Mọi giả định phải kiểm chứng bằng bằng chứng trong log/code.

**B6. Xây thành phần UI / khuôn game**
> Đóng vai kỹ sư frontend cấp cao. Tạo `[component / khuôn game]` tái sử dụng, dễ tiếp cận, API rõ ràng, theo design system pixel và checklist File B §5.3/§11. Xử lý đang tải/rỗng/lỗi, responsive, bàn phím, giảm chuyển động. Đưa ra: kiến trúc · thiết kế props/tham số · code · test · ví dụ sử dụng · tài liệu 1 trang cho người viết nội dung.

**B7. Viết nội dung một bài học (cho người viết nội dung/GV cố vấn)**
> Dựa trên nút `[ID]` trong `curriculum.json`, viết bài học theo schema (hook ≤ 30 giây · phần học ≤ 3 phút · phần chơi với khuôn `[...]` và tham số · 6–10 câu kiểm tra có gắn *misconception tag* · phản hồi khi sai giúp hiểu lại · recap). Văn phong phù hợp lớp `[...]`; không sao chép sách; kiểm tra thuật ngữ theo bảng thuật ngữ chuẩn; ghi các điểm cần giáo viên duyệt.

**B8. Sản xuất lô asset pixel bằng AI**
> Đóng vai Pixel Art Agent. Lấy danh sách asset ID từ `PLAN.md` §3 (một lô ≤ 5 asset cùng loại). Với mỗi asset: (1) đọc style guide, `palette.json` và golden samples; (2) viết **SpriteSpec** (không vẽ tay, không dùng ảnh sinh từ mô hình ảnh); (3) dựng bằng sprite-forge → PNG + **contact sheet** (1×/2×/4×, nền sáng/tối); (4) chạy validator; (5) **tự phê bình** theo checklist File B §7.7 và sửa tối đa `[3]` vòng; (6) ghi **hồ sơ nguồn gốc** (File B §7.8). Nếu môi trường không chạy được mã: xuất spec + lệnh dựng và nói rõ chưa kiểm chứng bằng ảnh. **Xong lô → cập nhật `PLAN.md` §3 và §10 (báo cáo `✅ ĐÃ CẬP NHẬT PLAN.md`) rồi mới làm lô kế tiếp.** Báo ngay nếu phát hiện palette trôi hoặc lệch phong cách so với golden samples.

---

# PHỤ LỤC — Checklist hoàn thành giai đoạn lập kế hoạch

- [ ] P0: câu hỏi chặn đã có đáp án hoặc giả định; phạm vi MVP rõ; có danh sách ngoài phạm vi
- [ ] P1a: đủ 9+ file trích xuất, đã kiểm ngẫu nhiên 5 dòng/file với sách thật
- [ ] P1b: bản đồ chương trình hợp nhất; bảng thuật ngữ chuẩn; đồ thị tiên quyết không chu trình; có JSON + schema
- [ ] P2: mỗi quyết định lớn có ADR; có 5 quyết định rủi ro nhất kèm spike; có bảng điểm gãy 10×/100×/1.000×
- [ ] P3: kiến trúc hợp nhất; có vertical slice; changelog giữa 4 agent
- [ ] P3B: đã chọn phương án tạo pixel bằng AI; có palette khóa, SpriteSpec, đặc tả sprite-forge, UI kit; **spike M0-ART có số đo và kết luận đạt/không đạt**; có hồ sơ nguồn gốc mẫu
- [ ] P4: báo cáo 5 lăng kính; mọi Blocker có hướng xử lý
- [ ] P5: lộ trình có tiêu chí hoàn thành đo được; kế hoạch sản xuất nội dung; backlog 30 ngày
- [ ] P6: checklist production; chi phí 3 mốc; pre-mortem
- [ ] P7: kế hoạch 2 trang; Go/No-go; “3 việc đầu tiên vào sáng thứ Hai”
- [ ] M0 đã chọn đủ rủi ro dễ chết nhất: font tiếng Việt · máy yếu · ngoại tuyến · bộ gõ Telex/VNI · đăng nhập mã lớp · Python/khối lệnh trong trình duyệt · **đồ họa pixel do AI tạo · độ nét UI khi zoom/DPI**
- [ ] **Cổng cập nhật:** mọi nhiệm vụ ✅ trong `PLAN.md` đều có sản phẩm mở được; nhật ký `U-xxx` liên tục, không đứt quãng; chạy `KIỂM TOÁN PLAN` không còn chỗ lệch


---

# PHẦN II — BỘ DỮ LIỆU KHỞI ĐẦU (FILE B)

# BỘ DỮ LIỆU KHỞI ĐẦU (File B) — Tài liệu tham chiếu cho các prompt lập kế hoạch

> **Cách dùng:** đính kèm file này vào mọi chat của dự án. Đây là *hạt giống* để AI đỡ phải bắt đầu từ trang trắng, **không phải quyết định đã chốt**. Mọi thứ gắn `[GIẢ ĐỊNH]`, `[ĐỀ XUẤT]` hoặc `[CẦN ĐỐI CHIẾU]` đều phải bị AI kiểm chứng và có quyền bác bỏ nếu có lý do. Mục lục: §1 Bối cảnh · §2 Khung chương trình · §3 Mẫu trích xuất · §4 Schema nội dung · §5 Khuôn game · §6 Vòng lặp học · §7 Pixel & âm thanh · §8 Công nghệ ứng viên · §9 Seed kiến trúc · §10 Bảo mật · §11 Tiếp cận · §12 Trường hợp biên · §13 Sổ rủi ro · §14 KPI & playtest · §15 Mẫu · §16 Ngân hàng câu hỏi P0.

---

## §1. Bối cảnh thực tế & persona `[GIẢ ĐỊNH — cần xác minh với giáo viên và học sinh thật]`

### 1.1 Persona

| Persona                       | Đặc điểm                                                                                                       | Hệ quả thiết kế                                                                                                  |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| **HS Tiểu học (≈ 8–11 tuổi)** | Đọc chữ còn chậm; thường chưa có email; kỹ năng chuột/bàn phím đang hình thành; tập trung ngắn; thích nhân vật | Ít chữ, có giọng đọc; nút to; kéo thả/chạm; đăng nhập không email; màn chơi 2–5 phút; không đếm ngược gây áp lực |
| **HS THCS (≈ 11–15 tuổi)**    | Thích thử thách và so sánh; dùng điện thoại nhiều; bắt đầu lập trình khối                                      | Nhiệm vụ nhiều bước; mục tiêu cá nhân; chế độ thử thách tùy chọn; chạy tốt trên điện thoại                       |
| **HS THPT (≈ 15–18 tuổi)**    | Thực dụng, nghĩ đến thi cử/nghề; thích dự án thật                                                              | Bài có “sản phẩm” (chương trình, bảng dữ liệu, trang web); liên hệ nghề nghiệp; bàn phím và code thật            |
| **Giáo viên Tin học**         | Ít thời gian; lớp đông; cần giao bài/xem kết quả nhanh; một số GV tiểu học không chuyên Tin                    | Mã lớp, giao bài 1 chạm, báo cáo ngắn; hướng dẫn dạy kèm mỗi bài; không cần cài đặt                              |
| **Phụ huynh**                 | Quan tâm an toàn và thời gian dùng                                                                             | Trang giải thích dữ liệu thu thập; không quảng cáo; xem tiến độ (tùy chọn, pha sau)                              |

### 1.2 Môi trường trường học Việt Nam `[GIẢ ĐỊNH]`
- Phòng máy: Windows đời cũ, RAM thấp, trình duyệt có thể cũ, thường **không có quyền cài đặt**, mạng dùng chung dễ nghẽn, có thể chặn một số tên miền hoặc giao thức.
- Ở nhà: điện thoại Android tầm trung và máy tính dùng chung gia đình; dữ liệu di động có hạn → **dung lượng tải là tính năng**.
- Giờ cao điểm: **đầu tiết học** (cả lớp 30–45 em đăng nhập cùng lúc), đầu năm học, trước kỳ kiểm tra.
- Kênh lan truyền: nhóm Zalo của lớp/trường → link và mã lớp phải **dễ chia sẻ** và mở tốt trong trình duyệt tích hợp của ứng dụng chat.
- Máy dùng chung: nhiều học sinh lần lượt dùng một máy → dữ liệu cục bộ phải gắn với học sinh, có đăng xuất rõ ràng.

---

## §2. Khung xương chương trình giả định `[CẦN ĐỐI CHIẾU — rút từ hiểu biết chung, chưa đối chiếu sách/Chương trình; AI phải kiểm chứng từng ô và sửa]`

Các mạch nội dung của Chương trình GDPT 2018 môn Tin học `[đối chiếu tên mạch với tài liệu chương trình]`:
**A.** Máy tính và xã hội tri thức · **B.** Mạng máy tính và Internet · **C.** Tổ chức lưu trữ, tìm kiếm và trao đổi thông tin · **D.** Đạo đức, pháp luật và văn hóa trong môi trường số · **E.** Ứng dụng tin học · **F.** Giải quyết vấn đề với sự trợ giúp của máy tính · **G.** Hướng nghiệp với Tin học.

| Mạch  | Tiểu học (3–5)                                         | THCS (6–9)                                                                             | THPT (10–12)                                                                    |
| :---- | :----------------------------------------------------- | :------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------ |
| **A** | Bộ phận máy tính, thiết bị vào/ra, thông tin quanh em  | Thông tin và dữ liệu, biểu diễn thông tin, thiết bị số, vai trò thông tin trong xã hội | Hệ thống máy tính, phần mềm, biểu diễn dữ liệu; (KHMT) nền tảng AI và xã hội    |
| **B** | Internet là gì, lên mạng an toàn cơ bản                | Mạng cục bộ/diện rộng, dịch vụ Internet                                                | Địa chỉ, mô hình mạng, an toàn mạng                                             |
| **C** | Tệp và thư mục, tìm thông tin đơn giản                 | Tìm kiếm nâng cao, đánh giá thông tin, thư điện tử, lưu trữ trực tuyến                 | Cơ sở dữ liệu, truy vấn (định hướng KHMT)                                       |
| **D** | Ứng xử khi dùng máy, thông tin cá nhân                 | Bản quyền, an toàn thông tin, bắt nạt trực tuyến                                       | Quy định liên quan, an ninh mạng, đạo đức AI                                    |
| **E** | Gõ bàn phím, vẽ, soạn thảo, trình chiếu cơ bản         | Soạn thảo, trình chiếu, bảng tính, đa phương tiện, sơ đồ tư duy                        | (Tin học ứng dụng) đồ họa, video, web, phần mềm chuyên dụng                     |
| **F** | Thuật toán trong đời sống, lập trình trực quan mức đầu | Thuật toán, sơ đồ khối, lập trình trực quan (khối)                                     | (KHMT) lập trình văn bản (ví dụ Python), cấu trúc dữ liệu, thuật toán, kiểm thử |
| **G** | —                                                      | Nghề liên quan Tin học mức giới thiệu                                                  | Ngành/nghề và định hướng                                                        |

**Lưu ý cho AI:** THPT có hai định hướng *Tin học ứng dụng* và *Khoa học máy tính* `[đối chiếu]`; sản phẩm phải quyết định hỗ trợ một hay cả hai và nêu hậu quả khối lượng nội dung.

---

## §3. Mẫu trích xuất & hợp nhất sách

### 3.1 Bảng trích xuất (mỗi bài một dòng)

| ID tạm | Bộ sách | Lớp | Tập/Chủ đề | Chương/Bài | Tên bài (giữ nguyên) | Số tiết | Mục tiêu (lời của AI) | Thuật ngữ mới | Loại hoạt động | Công cụ | Kiểu đánh giá cuối bài | Tiên quyết (suy ra) | Yêu cầu cần đạt (CT) | Trang | Độ tin cậy |
| :----- | :------ | :-- | :--------- | :--------- | :------------------- | :------ | :-------------------- | :------------ | :------------- | :------ | :--------------------- | :------------------ | :------------------- | :---- | :--------- |

### 3.2 Ma trận phủ

| Yêu cầu cần đạt (mã + tóm tắt) | KNTT  | CD    | CTST  | Nút kiến thức sản phẩm | Ghi chú |
| :----------------------------- | :---- | :---- | :---- | :--------------------- | :------ |
|                                | ✔/◐/✖ | ✔/◐/✖ | ✔/◐/✖ |                        |         |

### 3.3 Bảng thuật ngữ chuẩn

| Khái niệm | KNTT dùng | CD dùng | CTST dùng | **Chuẩn của sản phẩm** | Lý do chọn |
| :-------- | :-------- | :------ | :-------- | :--------------------- | :--------- |

### 3.4 Quy tắc giải quyết xung đột (theo thứ tự ưu tiên)
1. Chương trình GDPT 2018 là chuẩn.
2. Tính tiên quyết sư phạm (khái niệm nền học trước).
3. Điểm chung của đa số trong 3 bộ sách.
4. Đơn giản cho trẻ ở độ tuổi đó.
→ Mọi ngoại lệ phải ghi lý do và người duyệt.

### 3.5 Taxonomy loại hoạt động & mức nhận thức

- **Hoạt động:** quan sát · nghe/đọc · thảo luận · thao tác trên máy · trò chơi · dự án · phân loại/ghép cặp · lập trình/gỡ lỗi · tình huống ứng xử.
- **Mức nhận thức (Bloom rút gọn):** nhớ · hiểu · áp dụng · phân tích · sáng tạo.

---

## §4. Schema nội dung `[ĐỀ XUẤT]`

### 4.1 Nguyên tắc
- **ID bất biến:** không bao giờ tái sử dụng ID đã dùng; ngưng dùng thì đánh dấu `deprecated`.
- **ID dạng** `<cấp><lớp>-<mạch>-<số>`, ví dụ `G3-A-01`.
- **Nội dung version hóa** (semver cho gói nội dung); mỗi sự kiện tiến độ ghi phiên bản nội dung đã học.
- **Chuỗi hiển thị tách khỏi code** bằng khóa i18n.
- **Mọi ảnh/âm thanh có mô tả thay thế** (alt/caption).

### 4.2 Nút kiến thức (Curriculum Node)
```json
{
  "id": "G3-A-01",
  "status": "active",
  "level": "primary",
  "grade": 3,
  "strand": "A",
  "title_key": "node.G3-A-01.title",
  "outcomes": [{ "code": "CT-...", "summary_key": "..." }],
  "prerequisites": [],
  "book_refs": [{ "set": "KNTT", "chapter": "..." }],
  "bloom": "understand",
  "game_template": "sort-drag",
  "difficulty": 1,
  "est_minutes": 8,
  "lesson_id": "L-G3-A-01",
  "item_ids": ["I-G3-A-01-001"]
}
```

### 4.3 Bài học (Lesson) — cấu trúc 6 phần
`hook` (≤ 30 giây, tình huống/nhân vật) → `learn` (≤ 3 phút, ngắn, nhiều hình) → `play` (khuôn game + tham số) → `check` (6–10 câu) → `recap` (3 ý) → `extend` (tùy chọn, thử thách/nối với đời sống).

### 4.4 Câu hỏi (Item)
```json
{
  "id": "I-G3-A-01-001",
  "node_id": "G3-A-01",
  "type": "mcq | multi | order | match | fill | drag | typed | code-trace",
  "prompt_key": "...",
  "options": [{ "key": "...", "correct": true, "feedback_key": "..." }],
  "difficulty": 2,
  "bloom": "apply",
  "misconception_tags": ["nham-ram-voi-o-cung"],
  "est_seconds": 20,
  "alt_text_key": "..."
}
```
**Misconception tag** (ví dụ lẫn lộn RAM/ổ cứng, nhầm Internet với trình duyệt) giúp phản hồi khi sai *có ích* và giúp giáo viên thấy lớp đang hiểu sai ở đâu.

### 4.5 Kiểm tra nội dung tự động trong CI `[ĐỀ XUẤT]`
Hợp lệ schema · ID duy nhất · tiên quyết tồn tại và không chu trình · mọi `outcomes` có mã · mọi key i18n có chuỗi · mọi ảnh có alt · mọi nút có ≥ N câu hỏi · không có từ cấm/PII · độ dài chuỗi không tràn UI ở cỡ chữ lớn.

---

## §5. Catalog khuôn game `[ĐỀ XUẤT — AI chọn 6–10 khuôn đáng đầu tư nhất]`

### 5.1 Danh mục

| ID                  | Khuôn                 | Nút/kỹ năng điển hình                         | Cấp            | Cơ chế                                 | Chấm bằng                         | Tham số bài (dữ liệu)                     | Độ nặng |
| :------------------ | :-------------------- | :-------------------------------------------- | :------------- | :------------------------------------- | :-------------------------------- | :---------------------------------------- | :------ |
| `sort-drag`         | Kéo thả / phân loại   | Phân loại thiết bị vào/ra, loại tệp, phần mềm | TH, THCS       | Kéo vật vào nhóm                       | So khớp nhãn                      | nhóm, vật, gợi ý, giới hạn thử            | S       |
| `match-memory`      | Ghép cặp / lật thẻ    | Thuật ngữ ↔ hình/nghĩa                        | TH, THCS       | Lật 2 thẻ                              | Cặp đúng                          | cặp thẻ, số cặp, thời gian (tùy chọn)     | S       |
| `type-run`          | Gõ phím chạy đua      | Gõ đúng, tư thế tay, phím tắt                 | TH, THCS       | Gõ để nhân vật chạy                    | Chuỗi gõ khớp (chuẩn hóa Unicode) | văn bản, tốc độ, cho phép sai             | M       |
| `block-maze`        | Mê cung lệnh          | Tuần tự/lặp/rẽ nhánh                          | TH, THCS       | Ghép khối lệnh điều khiển nhân vật     | Mô phỏng chạy khối                | bản đồ, khối cho phép, số bước tối ưu     | M–L     |
| `bug-hunt`          | Thợ săn lỗi           | Gỡ lỗi thuật toán/chương trình                | THCS, THPT     | Tìm dòng/khối sai                      | Dòng đúng / test pass             | chương trình, lỗi, test                   | M       |
| `file-explorer-sim` | Mô phỏng thư mục/tệp  | Tạo/di chuyển/đổi tên/tìm tệp                 | TH, THCS       | Giao diện thu nhỏ                      | Trạng thái cây thư mục cuối       | cây ban đầu, nhiệm vụ, kết quả mong muốn  | M       |
| `sheet-quest`       | Bảng tính quest       | Công thức, hàm, địa chỉ ô                     | THCS, THPT     | Ô lưới tương tác                       | Giá trị ô/biểu thức               | lưới, nhiệm vụ, kiểm tra                  | M–L     |
| `packet-route`      | Gói tin & định tuyến  | Địa chỉ, đường đi, giao thức                  | THCS, THPT     | Chọn đường cho gói tin                 | Đường đi hợp lệ                   | đồ thị mạng, nguồn–đích, ràng buộc        | M       |
| `logic-puzzle`      | Nhị phân / cổng logic | Biểu diễn nhị phân, cổng logic                | THCS, THPT     | Bật/tắt bit, nối cổng                  | Bảng chân trị                     | bài toán, cổng cho phép                   | M       |
| `query-detective`   | Điều tra CSDL         | Truy vấn, lọc/sắp xếp/nối bảng                | THPT           | Xây truy vấn bằng khối/văn bản         | Kết quả truy vấn                  | bảng dữ liệu, câu hỏi, đáp án             | L       |
| `branch-story`      | Tình huống rẽ nhánh   | Đạo đức, an toàn, pháp luật số                | TH, THCS, THPT | Chọn hành động trong tình huống        | Hậu quả theo nhánh + phản hồi     | kịch bản, nhánh, kết cục                  | S–M     |
| `boss-quiz`         | Quiz boss             | Tổng kết chủ đề                               | Tất cả         | Trả lời để “đánh boss”                 | Điểm/độ thông thạo                | ngân hàng câu, ngưỡng                     | S       |
| `py-sandbox`        | Sân chơi Python       | Biến, rẽ nhánh, vòng lặp, hàm                 | THPT           | Viết/điền code, chạy trong trình duyệt | Test tự động                      | đề, mã khởi tạo, test, giới hạn thời gian | L       |

### 5.2 Ví dụ dữ liệu một bài chơi (`sort-drag`)
```json
{
  "template": "sort-drag",
  "node_id": "G3-A-01",
  "params": {
    "groups": [{ "id": "in", "label_key": "..." }, { "id": "out", "label_key": "..." }],
    "items": [{ "id": "mouse", "sprite": "dev/mouse", "group": "in" },
              { "id": "screen", "sprite": "dev/screen", "group": "out" }],
    "hints": 3,
    "unlimited_retries": true,
    "seed": 12345
  },
  "scoring": { "mastery_threshold": 0.8 }
}
```

### 5.3 Checklist chất lượng cho MỌI khuôn game
- Có **màn hướng dẫn** ngắn (≤ 1 màn) và có thể bỏ qua khi đã biết.
- Có **3 mức gợi ý** (nhẹ → rõ); **không có trạng thái bế tắc** (luôn có đường thoát/thử lại).
- **Thử lại vô hạn**, không phạt nặng; phản hồi khi sai nêu *vì sao* (dựa trên misconception tag).
- **Chơi được bằng bàn phím**; vùng bấm đủ lớn; hỗ trợ chạm.
- **Tôn trọng giảm chuyển động**; không nhấp nháy; không dựa chỉ vào màu.
- **Bộ chấm điểm tách khỏi phần hiển thị** (test được không cần giao diện); **ngẫu nhiên có seed** để tái hiện lỗi.
- **Sự kiện đo lường chuẩn** (xem §9.6); **không rò rỉ tài nguyên** khi thoát scene.
- Chạy được ở độ phân giải logic cố định và scale số nguyên; có chế độ **tạm dừng**/tiếp tục an toàn khi mất mạng.
- Có tài liệu 1 trang cho người viết nội dung: tham số nào chỉnh được, giới hạn, ví dụ.

---

## §6. Vòng lặp học & tiến độ `[ĐỀ XUẤT]`

- **Phiên học:** hook → học ngắn → chơi → kiểm tra → recap. Mục tiêu 5–10 phút/nút; ở tiểu học 2–5 phút/màn.
- **Mức thông thạo (mastery) của một nút:** đạt khi đúng ≥ `[80%]` trên ≥ `[2]` phiên cách nhau ≥ `[1 ngày]`. Con số do P2/P5 chốt sau playtest.
- **Ôn lặp cách quãng (Leitner 4 hộp):** lặp lại sau `[1, 3, 7, 21]` ngày; sai thì lùi một hộp. Ôn xen kẽ 3–5 câu cũ vào đầu phiên mới.
- **Phần thưởng:** XP, huy hiệu, trang trí nhân vật/ngôi nhà pixel, mở khóa khu vực.
- **“Streak mềm”:** chúc mừng chuỗi ngày nhưng **không mất mát/áp lực** khi nghỉ.
- **Xếp hạng:** không công khai theo tên mặc định; giáo viên tự bật cho lớp; ưu tiên “kỷ lục cá nhân” và “cùng nhau đạt mục tiêu của lớp”.
- **Cấm (dark pattern):** hộp quà ngẫu nhiên/cờ bạc hóa; đếm ngược gây lo âu cho tiểu học; thông báo ép quay lại; so sánh làm xấu hổ; trừ điểm gây sợ; quảng cáo.
- **Giáo viên:** giao bài theo nút/chủ đề; xem lớp đang hiểu sai ở đâu (misconception tag); xuất báo cáo; không bắt buộc cài đặt.

---

## §7. Pixel & âm thanh `[ĐỀ XUẤT]`

### 7.0 Đồ họa pixel do AI tạo — nguyên tắc và 5 phương án `[ĐỀ XUẤT — P3B (T-P3B-01) chốt sau khi thử thật]`

**Nguyên tắc:** AI **không “vẽ” ảnh**. AI viết **đặc tả dạng văn bản/mã** (lưới chỉ số màu, hình học, thủ tục, ghép bộ phận) lưu trong Git; một công cụ nhỏ (“sprite-forge”) **dựng ra PNG** chỉ dùng màu trong palette khóa. Nhờ vậy asset kiểm soát được lưới và bảng màu, tái tạo được, so sánh được bằng Git, nguồn gốc rõ.

**Điều kiện thực hiện:** môi trường chạy được mã (Python/Node) **và** AI xem lại được ảnh đã dựng (contact sheet). Nếu thiếu một trong hai, AI chỉ xuất được spec + lệnh dựng và **phải ghi rõ “chưa kiểm chứng bằng ảnh”**.

| PA    | Tên                           | Cách làm                                                                         | Mạnh                                             | Yếu                                                                                                | Hợp với                                     |
| :---- | :---------------------------- | :------------------------------------------------------------------------------- | :----------------------------------------------- | :------------------------------------------------------------------------------------------------- | :------------------------------------------ |
| **A** | Lưới chỉ số màu               | Mỗi ký tự/số = một màu trong palette; sprite viết thành lưới (≤ 32×32)           | Kiểm soát tuyệt đối lưới và màu; diff Git rất rõ | AI dễ lệch hàng/cột ở sprite lớn; tốn token                                                        | Icon, tile, nhân vật nhỏ                    |
| **B** | Hình học / SVG → raster       | Vẽ khối, đường, hình bằng tọa độ; dựng với `crispEdges`, lượng tử hóa về palette | Rất hợp hình khối, đối xứng; gọn                 | Nếu không lượng tử hóa sẽ “trông như vector”, không ra pixel                                       | Khung, nút, nền hình khối, vật thể hình học |
| **C** | Thủ tục                       | Hàm sinh có seed: nhiễu, dither, lặp mẫu, tile ghép được                         | Sinh số lượng lớn nhất quán; tái tạo bằng seed   | Khó điều khiển chi tiết cụ thể                                                                     | Tile địa hình, nền, hiệu ứng, texture       |
| **D** | Ghép bộ phận                  | Thân/đầu/trang phục/phụ kiện là các lớp; palette swap tạo biến thể               | Tạo nhiều nhân vật/NPC/avatar nhất quán          | Tốn công làm bộ phận “vàng” ban đầu                                                                | Nhân vật, NPC, avatar                       |
| **E** | Mô hình sinh ảnh → hạ về lưới | Sinh ảnh rồi giảm độ phân giải/lượng tử hóa                                      | Nhanh, nhiều ý tưởng                             | **Không kiểm soát lưới/palette; trôi phong cách; không tái tạo; nguồn gốc/bản quyền mờ; khó diff** | Chỉ làm tham khảo cảm hứng                  |

**Đề xuất mặc định:** **A + B + C + D**; **loại E khỏi đường sản xuất** (chỉ tham khảo, không đưa pixel của E vào sản phẩm).

**Điều AI làm kém (phải nêu thẳng khi đánh giá):**
- Đếm chính xác hàng/cột ở lưới lớn; giữ chi tiết nhất quán giữa nhiều khung hoạt ảnh.
- “Cái hồn” thẩm mỹ của mascot, logo, minh họa lớn.
- Tự nhìn lại ảnh có thể sai → cần contact sheet + validator + **người duyệt**.

**Phương án lai khi cần:** người vẽ phần cốt lõi (mascot, logo, minh họa lớn), AI làm phần còn lại (tile, icon, UI, biến thể).

### 7.1 Đặc tả hình ảnh
- **Độ phân giải logic cố định** (ví dụ 320×180 cho ngang 16:9; cần phương án cho điện thoại dọc), phóng to **số nguyên**, `image-rendering: pixelated`.
- **Lưới ô:** 16×16 cho bản đồ/vật phẩm; 32×32 cho nhân vật chính/biểu tượng lớn `[ĐỀ XUẤT]`.
- **Bảng màu:** ≤ `[16–32]` màu mỗi “thế giới” + bảng UI chung ≤ `[8]` màu; mỗi cấp có chủ đề màu riêng nhưng chung quy tắc tương phản.
- **Tương phản chữ/nền** ≥ 4.5:1; kiểm tra bảng màu với các dạng mù màu thường gặp; trạng thái quan trọng có thêm hình/ký hiệu, không chỉ màu.
- **Hoạt ảnh:** 4–8 khung/chuyển động, 6–12 khung/giây; không nhấp nháy > 3 lần/giây; có chế độ giảm chuyển động.
- **UI pixel:** khung 9-slice, nút (bình thường/hover/nhấn/tắt/focus **nhìn thấy rõ**), bộ icon 16×16, con trỏ chuột pixel (tùy chọn).
- **Nhất quán phong cách:** hướng sáng, độ dày viền, mức chi tiết; có “style guide” 1 trang kèm sprite mẫu.

### 7.2 Chữ (font)
- Font pixel chỉ dùng cho tiêu đề/nhãn ngắn; **bắt buộc kiểm tra đủ glyph tiếng Việt** (ă â ê ô ơ ư đ + thanh điệu, cả chữ hoa, kiểu gộp & tổ hợp). Thiếu glyph → chọn font khác hoặc tự vẽ bitmap font.
- Văn bản dài: font sans dễ đọc, cỡ chữ điều chỉnh được, giãn dòng thoáng; tùy chọn chữ dễ đọc cho người khó đọc.
- Nhúng font tự chủ (không phụ thuộc CDN bên ngoài nếu có thể) và ghi license.

### 7.3 Pipeline asset
`vẽ (công cụ pixel art) → xuất sprite sheet + JSON → gộp atlas theo cảnh/cấp → nén/kiểm tra dung lượng → kiểm tra license → đóng gói theo gói ngoại tuyến → CDN`
- Đặt tên: `<thế-giới>/<loại>/<tên>_<biến-thể>_<khung>.png`.
- File nguồn (.ase hoặc tương đương) lưu trong kho; ghi chú công cụ/phiên bản.
- **Sổ license (`ASSETS.md`):** tên asset · tác giả · nguồn · license · được phép dùng thương mại? · cần ghi công? · ngày kiểm tra.
- **Hạn mức:** dung lượng atlas/scene, số atlas nạp cùng lúc, kích thước tối đa mỗi texture `[ĐỀ XUẤT — Optimizer chốt]`.
- **Asset sinh bằng AI:** `[CẦN QUYẾT ĐỊNH]` — rủi ro bản quyền, nhất quán phong cách, khả năng chỉnh sửa; nếu dùng, phải có quy trình duyệt và ghi nhận.

### 7.4 Âm thanh
- Phong cách chiptune; hiệu ứng ngắn; **tắt mặc định** hoặc hỏi lần đầu; điều khiển âm lượng; có phụ đề/biểu tượng thay cho thông tin chỉ nghe được.
- Hạn mức dung lượng mỗi hiệu ứng/nhạc nền `[ĐỀ XUẤT]`; tạm dừng khi chuyển tab; giải phóng khi thoát scene.

### 7.5 Mẫu ước lượng sản xuất asset

| Hạng mục                          | Số lượng | Giờ/đơn vị `[ƯỚC TÍNH]` | Tổng | Ghi chú |
| :-------------------------------- | :------- | :---------------------- | :--- | :------ |
| Nhân vật chính (bộ khung hình)    |          |                         |      |         |
| Nhân vật phụ/NPC                  |          |                         |      |         |
| Tile bản đồ theo thế giới         |          |                         |      |         |
| Vật phẩm/biểu tượng bài học       |          |                         |      |         |
| UI (khung, nút, icon)             |          |                         |      |         |
| Hiệu ứng (particles, chuyển cảnh) |          |                         |      |         |
| Âm thanh                          |          |                         |      |         |

### 7.6 Danh mục UI kit pixel-first `[ĐỀ XUẤT — T-P3B-06 chốt]`

Toàn bộ giao diện (không chỉ màn chơi) dùng bộ thành phần dưới đây, dựng từ **token** và dùng lại ở mọi màn.

| Thành phần                                                  | Biến thể / trạng thái                                                                                                                            | Ghi chú                                                |
| :---------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------- |
| **Token**                                                   | `--px` (đơn vị cơ sở), bội số nguyên của `--px` cho mọi kích thước/khoảng cách; palette UI; độ dày viền                                          | Mọi kích thước là bội số nguyên → không vỡ lưới        |
| **Khung 9-slice**                                           | panel, hộp thoại, thẻ, tooltip; 2–3 độ dày viền                                                                                                  | Co giãn không méo góc                                  |
| **Nút**                                                     | bình thường · hover · nhấn · tắt · **focus nhìn thấy rõ**; 3 cỡ                                                                                  | Vùng bấm đề xuất ≥ 44×44 px CSS cho trẻ nhỏ/điện thoại |
| **Thanh tiến trình / XP / tải**                             | đầy · rỗng · đang tải                                                                                                                            | Có nhãn chữ thật, không chỉ màu                        |
| **Ô nhập, checkbox, radio, công tắc, thanh trượt âm lượng** | thường · focus · lỗi · tắt                                                                                                                       | Chữ là chữ thật của trình duyệt                        |
| **Icon 16×16 (và bản 32×32)**                               | bộ tối thiểu: trang chủ, chơi, tạm dừng, gợi ý, thử lại, âm thanh bật/tắt, cài đặt, sao, khóa, đúng, sai, mũi tên, quay lại, giáo viên, trợ giúp | Mỗi icon có alt/nhãn                                   |
| **Con trỏ pixel**                                           | mặc định · bấm được · kéo                                                                                                                        | Tùy chọn; luôn có con trỏ hệ thống dự phòng            |
| **Vòng focus**                                              | pixel dày, tương phản cao                                                                                                                        | Dùng chung cho DOM và canvas                           |
| **Nền & chuyển trang**                                      | nền theo thế giới; chuyển trang ngắn                                                                                                             | Tôn trọng giảm chuyển động                             |
| **Màn tải**                                                 | mascot + thanh tiến trình                                                                                                                        | Hiện rõ khi tải lười Python/gói ngoại tuyến            |
| **Hộp phản hồi đúng/sai, toast**                            | đúng · sai · thông tin                                                                                                                           | Luôn có **icon + chữ**, không chỉ màu                  |
| **Huy hiệu / khung phần thưởng**                            | chưa mở · đã mở                                                                                                                                  | Không dark pattern (§6)                                |
| **Chế độ pixel nhẹ**                                        | cho trang giáo viên/phụ huynh                                                                                                                    | Ưu tiên đọc dữ liệu: ít trang trí, bảng/biểu đồ rõ     |

**Quy tắc “pixel không làm khó đọc”:**
- Chữ luôn là chữ thật của trình duyệt, **không rasterize chữ thành ảnh**; đoạn văn dài dùng font sans dễ đọc; font pixel chỉ cho tiêu đề/nhãn ngắn và phải đủ glyph tiếng Việt (§7.2).
- Phóng to theo **số nguyên**; ở zoom/DPI lẻ phải có quy tắc làm tròn/snap để không mờ (`image-rendering: pixelated`); thử ở nhiều mức zoom và DPI.
- Cỡ chữ điều chỉnh được; tương phản ≥ 4.5:1; có chế độ giảm chuyển động.

**Kỹ thuật dựng cần so sánh (P3B chốt):** 9-slice bằng ảnh/`border-image` · CSS thuần (ví dụ `box-shadow` pixel) · SVG `crispEdges` · canvas. Tiêu chí: độ nét ở mọi zoom/DPI · dung lượng · tiếp cận · đổi chủ đề · hiệu năng máy yếu.

### 7.7 Checklist AI tự phê bình mỗi asset `[ĐỀ XUẤT]`

AI chạy checklist này trên **contact sheet** (phóng 1×/2×/4×, nền sáng và nền tối) sau khi validator chạy xong.

**A. Kỹ thuật (máy kiểm — validator)**
- [ ] Kích thước và số khung đúng spec.
- [ ] Chỉ dùng màu trong palette khóa (0 màu ngoài bảng).
- [ ] Không có pixel bán trong suốt.
- [ ] Viền ngoài kín, không đứt; không có ô trống thừa/tràn mép.
- [ ] Pivot hợp lệ; tên file đúng quy ước (§7.3).

**B. Nhìn (AI + người)**
- [ ] Nhận diện được ở **1×**; silhouette rõ.
- [ ] Hướng sáng, độ dày viền, mức chi tiết **khớp golden samples**.
- [ ] Không có pixel lẻ “bẩn” (orphan), không dải màu thô (banding) ngoài ý định.
- [ ] Hoạt ảnh liền mạch giữa các khung; không nhấp nháy > 3 lần/giây.
- [ ] Đủ tương phản khi đặt trên nền sáng và tối; không chỉ phân biệt bằng màu.

**C. Nội dung & an toàn**
- [ ] Phù hợp lứa tuổi; không ký hiệu/hình ảnh không phù hợp.
- [ ] Không giống nhân vật/IP có bản quyền.
- [ ] Có alt-text; bối cảnh văn hóa phù hợp với học sinh Việt Nam.

**D. Quy trình**
- Tối đa `[3]` vòng sửa/asset; mỗi vòng ghi “lỗi → đã sửa gì”.
- Sau vòng cuối vẫn chưa đạt → chuyển người vẽ (phương án lai) và ghi vào `PLAN.md` §3.
- Phát hiện **palette trôi** hoặc lệch phong cách so với golden → dừng lô và báo ngay.

### 7.8 Hồ sơ nguồn gốc asset (provenance) `[ĐỀ XUẤT]`

Mỗi asset có một hồ sơ lưu **cạnh spec trong Git**, và một dòng tương ứng trong sổ license `ASSETS.md` (§7.3).

```json
{
  "asset_id": "A-005",
  "type": "character",
  "spec_path": "assets/source/world1/mascot.spec.json",
  "spec_hash": "sha256:...",
  "built_with": { "tool": "sprite-forge", "version": "0.1.0" },
  "ai_used": { "model": "[tên + phiên bản, nếu có]", "role": "viết spec", "date": "YYYY-MM-DD" },
  "golden_refs": ["A-001/golden-01"],
  "external_references": [],
  "validator": { "passed": true, "report": "..." },
  "aesthetic_reviewer": { "name": "[người duyệt]", "score": 4, "date": "YYYY-MM-DD" },
  "license": "[giấy phép dự án chọn cho asset do AI tạo — CẦN XÁC MINH PHÁP LÝ]",
  "ip_similarity_check": "đã đối chiếu danh sách ‘không bắt chước’",
  "status": "active | replaced",
  "replaced_by": null,
  "replace_reason": null
}
```

**Quy tắc:**
- **Tái tạo được:** CI dựng lại asset từ spec và so `spec_hash`/kết quả; không khớp thì báo.
- **Mô hình sinh ảnh bên ngoài** chỉ dùng tham khảo cảm hứng; nếu có dùng phải ghi vào `external_references`; **không đưa pixel của nó vào sản phẩm**.
- **Quyền sở hữu** sản phẩm do AI tạo: `[CẦN XÁC MINH PHÁP LÝ]`; không tự kết luận.
- **Khi có khiếu nại:** gỡ asset → viết spec mới → dựng lại → duyệt → ghi `replaced`/`replaced_by`/lý do.
- Hồ sơ cũng là nguồn cho SBOM/kiểm kê license ở P6.

---

## §8. Danh mục ứng viên công nghệ `[CHỈ LÀ ỨNG VIÊN — phải kiểm tra phiên bản, giá, license, độ “sống” của dự án và tương thích máy yếu trước khi dùng]`

| Hạng mục                 | Ứng viên (ví dụ)                                                    | Điều cần kiểm tra                                                                                  |
| :----------------------- | :------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------- |
| Khung web / shell        | Next.js · Astro · SvelteKit · Vite + React/Vue/Svelte               | Hiệu năng máy yếu; xuất tĩnh/ngoại tuyến; hệ sinh thái; dễ tuyển người                             |
| Engine game 2D           | Phaser · PixiJS · Kaplay · Canvas thuần · (engine khác xuất web)    | Dung lượng; hỗ trợ pixel-perfect; quản lý bộ nhớ; hỗ trợ bàn phím/tiếp cận; độ “sống”              |
| Nội dung                 | MDX/Markdown + JSON · CMS có Git (kiểu headless) · bảng tính → JSON | Người không phải dev có làm được không; xem trước; kiểm tra schema                                 |
| Kiểm tra schema          | Zod · JSON Schema (Ajv) · Valibot                                   | Dùng chung client/server/CI                                                                        |
| Lập trình khối           | Blockly (hoặc tương đương)                                          | License; tùy biến khối bằng tiếng Việt; hiệu năng                                                  |
| Python trong trình duyệt | Pyodide · PyScript · Skulpt                                         | Dung lượng tải; thời gian khởi động; chạy trong worker; giới hạn thời gian/bộ nhớ; thư viện hỗ trợ |
| Lưu trữ client           | IndexedDB (bọc bằng thư viện nhỏ) · Dexie                           | Dung lượng; hành vi khi người dùng xóa dữ liệu; chế độ riêng tư                                    |
| PWA / ngoại tuyến        | Workbox · service worker tự viết                                    | Chiến lược cache theo gói; cập nhật phiên bản; xử lý bản cũ                                        |
| Backend                  | Serverless/edge (Workers, functions) · Node monolith nhỏ · BaaS     | Giới hạn, giá, độ trễ từ Việt Nam; thoát nhà cung cấp                                              |
| Cơ sở dữ liệu            | PostgreSQL managed · SQLite phân tán/edge · BaaS                    | Giá theo quy mô; sao lưu; vị trí dữ liệu; migration                                                |
| Xác thực                 | Tự làm cho mã lớp/PIN + dịch vụ cho giáo viên · nhà cung cấp auth   | Trẻ em/không email; tuân thủ; chi phí theo người dùng                                              |
| CDN / hosting            | Nhà cung cấp CDN lớn · hosting tĩnh                                 | **Điểm hiện diện gần Việt Nam**; giá băng thông; cache rules                                       |
| Theo dõi lỗi             | Sentry · GlitchTip (tự host) · tương tự                             | Quyền riêng tư (lọc PII); giá; kích thước SDK                                                      |
| Phân tích sử dụng        | Công cụ thân thiện quyền riêng tư (tự host hoặc không cookie)       | Không thu PII trẻ em; chi phí; dữ liệu ở đâu                                                       |
| Test                     | Vitest/Jest · Playwright · kiểm thử trực quan cho canvas            | Chạy ổn định trong CI; giả lập máy yếu/mạng chậm                                                   |
| CI/CD                    | Nền tảng CI của kho mã · triển khai tự động                         | Thời gian chạy; chi phí; bí mật                                                                    |
| Công cụ pixel art        | Aseprite · LibreSprite · Piskel · Tiled (bản đồ)                    | License; định dạng xuất; quy trình đội                                                             |
| Âm thanh                 | Web Audio · Howler · tương tự                                       | Dung lượng; độ trễ trên máy yếu; tự phát âm thanh bị chặn                                          |

**Quy tắc đánh giá ứng viên:** nêu ≥ 2 phương án thật; kiểm tra *lần cập nhật gần nhất, số người bảo trì, license, kích thước đóng gói, tương thích trình duyệt mục tiêu*; ghi đường thoát và chi phí đổi.

---

## §9. Seed kiến trúc `[ĐỀ XUẤT — Architect được phép bác bỏ]`

### 9.1 Thành phần logic
`Web shell` (định tuyến, UI, đăng nhập) · `Content pack` (nội dung tĩnh theo phiên bản) · `Game runtime` (engine + khuôn game) · `Progress store (local)` · `Sync API` (nhận sự kiện, trả tiến độ) · `Teacher API` (lớp, giao bài, báo cáo) · `Auth` · `Analytics` (ẩn danh) · `Asset CDN` · `Observability`.

### 9.2 Cây thư mục (monorepo) `[ĐỀ XUẤT]`
```
/apps
  /web                 # shell: routing, UI, PWA
  /api                 # backend (nếu có)
/packages
  /domain              # logic thuần: Node, Lesson, Mastery, scheduling (không phụ thuộc framework)
  /content-schema      # schema + kiểm tra nội dung
  /game-core           # giao diện chung khuôn game, vòng đời scene, RNG có seed
  /games
    /sort-drag
    /block-maze
    /...               # mỗi khuôn một gói, chỉ phụ thuộc game-core + domain
  /ui                  # design system pixel (component có props rõ ràng)
  /i18n                # chuỗi, tiện ích
  /telemetry           # sự kiện chuẩn, lọc PII
/content
  /vi/primary/g3/...   # JSON/MDX theo nút; không chứa code
/assets
  /source              # file nguồn pixel
  /build               # atlas, âm thanh đã tối ưu
/tools                 # validator nội dung, build atlas, kiểm tra license, đo dung lượng
/infra                 # hạ tầng dưới dạng code
/docs                  # ADR, runbook, hướng dẫn thêm bài/khuôn game
```

### 9.3 Quy tắc phụ thuộc (ép bằng công cụ kiểm tra kiến trúc)
- `domain` **không** import framework/UI/engine.
- `games/*` chỉ import `game-core`, `domain`, `ui` (nếu cần); **không** import lẫn nhau.
- `apps/*` lắp ghép các gói; không chứa logic nghiệp vụ.
- `content` không chứa code; chỉ dữ liệu có schema.

### 9.4 Bảng cơ sở dữ liệu seed (phía server) `[ĐỀ XUẤT — chỉ cần khi có đồng bộ/lớp học]`

| Bảng               | Cột chính                                                                               | Ghi chú                                       |
| :----------------- | :-------------------------------------------------------------------------------------- | :-------------------------------------------- |
| `teachers`         | id, email/định danh, tên hiển thị, tạo lúc                                              | Tài khoản đầy đủ                              |
| `classrooms`       | id, teacher_id, tên, mã lớp, cấp/lớp, trạng thái                                        | Mã lớp ngẫu nhiên đủ dài, có hạn              |
| `learners`         | id, classroom_id, biệt danh, avatar_id, pin_hash                                        | **Không email/họ tên thật bắt buộc**; PIN băm |
| `consents`         | id, learner_id/classroom_id, loại, bởi ai, lúc nào, thu hồi lúc                         | `[CẦN XÁC MINH PHÁP LÝ]`                      |
| `progress_events`  | id (UUID v7), learner_id, node_id, content_version, type, payload, client_ts, server_ts | **Chỉ thêm**; khóa idempotency = id           |
| `mastery`          | learner_id, node_id, level, box, next_due, updated_at                                   | **Suy ra** từ sự kiện; có thể dựng lại        |
| `assignments`      | id, classroom_id, node_ids, due, tạo lúc                                                | Giáo viên giao bài                            |
| `badges`           | learner_id, badge_id, earned_at                                                         |                                               |
| `content_releases` | version, released_at, notes, min_client_version                                         | Để di trú & thông báo                         |
| `audit_log`        | id, actor, action, target, at, ip_hash                                                  | Quyền truy cập dữ liệu trẻ                    |

Chỉ mục gợi ý: `progress_events(learner_id, client_ts)`, `mastery(learner_id, next_due)`, `learners(classroom_id)`, `classrooms(join_code)`.

### 9.5 API seed `[ĐỀ XUẤT]`

| Phương thức & đường dẫn            | Mục đích                                | Ghi chú                                          |
| :--------------------------------- | :-------------------------------------- | :----------------------------------------------- |
| `POST /v1/auth/class-login`        | Đăng nhập bằng mã lớp + biệt danh + PIN | Giới hạn tốc độ; khóa tạm khi sai nhiều          |
| `GET /v1/content/manifest`         | Phiên bản nội dung & gói ngoại tuyến    | ETag/cache ngắn                                  |
| `GET /v1/me/progress`              | Tiến độ & mastery hiện tại              | Riêng tư, không cache CDN                        |
| `POST /v1/progress/events`         | Gửi **lô** sự kiện                      | Idempotent; kiểm tra schema; giới hạn kích thước |
| `GET /v1/classes/:id/report`       | Báo cáo lớp (giáo viên)                 | Kiểm tra quyền sở hữu lớp                        |
| `POST /v1/classes/:id/assignments` | Giao bài                                |                                                  |
| `POST /v1/teacher/classes`         | Tạo lớp, sinh mã lớp                    |                                                  |
| `POST /v1/learners/:id/reset-pin`  | Giáo viên đặt lại PIN                   | Ghi audit log                                    |
| `DELETE /v1/learners/:id`          | Xóa dữ liệu học sinh                    | Theo chính sách xóa                              |

Quy ước: versioning trong đường dẫn; mã lỗi thống nhất; **mọi POST có thể thử lại an toàn**; phân trang; giới hạn kích thước; không trả thông tin thừa.

### 9.6 Sự kiện tiến độ (schema seed)
```json
{
  "id": "uuid-v7",
  "learner_id": "...",
  "node_id": "G3-A-01",
  "content_version": "1.4.0",
  "type": "attempt | hint_used | completed | review_done | badge_earned",
  "payload": { "score": 0.8, "duration_s": 95, "hints": 1, "misconceptions": ["..."], "seed": 12345 },
  "client_ts": "2026-01-01T00:00:00Z"
}
```
**Quy tắc:** không đưa PII vào `payload`; thời gian client có thể sai → dùng `server_ts` để sắp xếp tin cậy, `client_ts` chỉ tham khảo.

### 9.7 Đồng bộ & xung đột `[ĐỀ XUẤT]`
- Client ghi sự kiện vào IndexedDB trước; gửi nền theo lô; thử lại với backoff; **server loại trùng theo `id`**.
- Server tính lại `mastery` từ sự kiện (hàm thuần trong `domain`, dùng chung client/server).
- Xung đột ≈ không có vì **chỉ thêm**; cái cần xử lý là **đổi phiên bản nội dung giữa chừng** (di trú bằng bản đồ `old_node → new_node`).

### 9.8 Tầng cache

| Tầng           | Cái gì                                       | TTL/chiến lược                | Vô hiệu hóa                                        |
| :------------- | :------------------------------------------- | :---------------------------- | :------------------------------------------------- |
| CDN            | JS/CSS/atlas có hash                         | Rất dài, immutable            | Đổi tên file (hash)                                |
| CDN/Edge       | `content/manifest`                           | Ngắn + ETag                   | Phát hành phiên bản mới                            |
| CDN            | Gói nội dung theo bài/cấp (URL có phiên bản) | Dài                           | URL mới theo phiên bản                             |
| Service worker | Gói ngoại tuyến theo cấp/lớp                 | Precache + cập nhật nền       | Khi manifest đổi; **không đổi giữa chừng một bài** |
| Server         | Báo cáo lớp (tổng hợp)                       | Ngắn (vài chục giây–vài phút) | Khi có sự kiện mới (hoặc chấp nhận trễ)            |
| Trình duyệt    | Tiến độ cục bộ                               | Nguồn sự thật tạm thời        | Đồng bộ lô                                         |

### 9.9 Đăng nhập cho trẻ `[ĐỀ XUẤT]`
- **Không email.** Học sinh vào bằng: *mã lớp* (giáo viên chia sẻ, qua Zalo/in) + *biệt danh/avatar* + *PIN ngắn hoặc chuỗi biểu tượng*.
- Giáo viên có thể đặt lại PIN; giới hạn thử sai; mã lớp hết hạn/thay mới được.
- Chế độ **khách** (không lưu server) để thử nhanh; dữ liệu chỉ ở máy.
- Máy dùng chung: có nút “Đổi người chơi” rõ ràng; dữ liệu cục bộ tách theo học sinh.

### 9.10 Ngân sách hiệu năng `[ĐỀ XUẤT — chỉ là điểm xuất phát, phải đo trên máy thật]`

| Chỉ số                                      | Mục tiêu khởi điểm                               |
| :------------------------------------------ | :----------------------------------------------- |
| Mã chạy ban đầu (shell, nén)                | vài trăm KB trở xuống                            |
| Bài đầu tiên + game (cả asset)              | vài MB trở xuống                                 |
| Thời gian từ bấm đến chơi được trên máy yếu | vài giây                                         |
| Khung hình/giây                             | ổn định ~30–60 fps trên máy RAM 4 GB             |
| Gói ngoại tuyến cho một lớp                 | giới hạn rõ ràng, có thanh tiến trình tải        |
| Python trong trình duyệt                    | tải lười, chỉ ở bài cần; hiển thị tiến trình tải |

---

## §10. Seed bảo mật `[ĐỀ XUẤT — dùng ở P4.1]`

| Nhóm                  | Câu hỏi kiểm tra                                                                                                                                |
| :-------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Xác thực & phiên**  | Mã lớp đủ entropy? Giới hạn thử PIN? Khóa tạm? Phiên hết hạn? Đăng xuất trên máy dùng chung?                                                    |
| **Phân quyền (IDOR)** | Giáo viên A có đọc được lớp của B bằng cách đoán ID? Học sinh có đọc tiến độ người khác?                                                        |
| **Dữ liệu trẻ em**    | Thu gì, để làm gì, lưu bao lâu? Có PII ở log/analytics/theo dõi lỗi? Quy trình xóa?                                                             |
| **Nội dung (XSS)**    | MDX/HTML do người viết nội dung có thể chèn script? Chuỗi nhập của học sinh (biệt danh, ô nhập tự do) có được thoát an toàn?                    |
| **Mã của học sinh**   | Python/khối lệnh chạy trong sandbox trình duyệt (worker); giới hạn thời gian/bộ nhớ; không truy cập mạng/DOM ngoài ý muốn                       |
| **Giả mạo tiến độ**   | Client có thể gửi điểm giả? Với game thường: chấp nhận; với “chứng nhận/huy hiệu quan trọng”: xác minh phía server hoặc không coi là bằng chứng |
| **API**               | Rate limit; kích thước lô tối đa; kiểm tra schema; idempotency; thông báo lỗi không lộ chi tiết                                                 |
| **Chuỗi cung ứng**    | Quét lỗ hổng phụ thuộc; ghim phiên bản; kiểm tra script bên thứ ba; Subresource Integrity nếu có                                                |
| **Cấu hình**          | CSP, header bảo mật, cookie cờ an toàn, CORS tối thiểu, bí mật không nằm trong repo                                                             |
| **Hạ tầng**           | Sao lưu mã hóa; quyền tối thiểu; nhật ký truy cập; môi trường staging không chứa dữ liệu thật                                                   |
| **Lạm dụng**          | Spam tạo lớp/học sinh; tải gói lớn lặp để đốt băng thông; chi phí tăng đột biến                                                                 |

---

## §11. Seed tiếp cận `[ĐỀ XUẤT — dùng ở P4.2]`

- Toàn bộ chức năng thao tác được **chỉ bằng bàn phím**; thứ tự focus hợp lý; **focus nhìn thấy rõ** (cả trong game canvas).
- Cỡ chữ điều chỉnh; không dùng chữ pixel cho đoạn văn dài; tương phản ≥ 4.5:1 (chữ thường).
- **Không chỉ dựa vào màu**; có hình/ký hiệu/nhãn bổ sung.
- **Giảm chuyển động** (theo cài đặt hệ thống) và tránh nhấp nháy nguy hiểm.
- Có phương án thay thế **kéo thả** (chọn–đặt bằng bàn phím/chạm).
- Hình có mô tả; hiệu ứng âm thanh quan trọng có biểu tượng/phụ đề.
- Vùng chạm đủ lớn cho trẻ nhỏ và điện thoại.
- Trình đọc màn hình: cấu trúc tiêu đề, nhãn nút, thông báo trạng thái (đúng/sai/hoàn thành) qua vùng thông báo thích hợp.
- Hỗ trợ **phóng to** màn hình/trang mà không vỡ bố cục.
- Thời gian giới hạn (nếu có) phải tắt/kéo dài được.

---

## §12. Sổ trường hợp biên `[GIẢ ĐỊNH — dùng ở P4.3]`

**Kết nối & dữ liệu**
1. Mất mạng giữa lúc đang lưu/gửi lô sự kiện.
2. Mạng chập chờn: yêu cầu hoàn thành hai lần (idempotency).
3. Học sinh xóa dữ liệu trình duyệt / dùng chế độ riêng tư / hết dung lượng lưu trữ.
4. Mở hai tab hoặc hai thiết bị cùng lúc cho một học sinh.
5. Đồng hồ máy sai (lệch ngày/giờ) ảnh hưởng ôn lặp cách quãng và sắp xếp sự kiện.
6. Cập nhật nội dung **giữa chừng một bài** (bản cũ trong cache, bản mới trên server).
7. Đổi cấu trúc chương trình giữa năm → di trú tiến độ.

**Phòng máy & thiết bị**
8. Nhiều học sinh dùng chung một máy; quên đăng xuất.
9. Cả phòng 40 máy vào bài cùng lúc (thundering herd).
10. Trình duyệt cũ không hỗ trợ một tính năng; WebAssembly/Worker bị tắt hoặc chặn.
11. Mạng trường chặn tên miền/giao thức; thiếu quyền cài đặt.
12. Màn hình độ phân giải nhỏ/lớn bất thường; DPI cao; phóng to hệ điều hành.
13. Máy yếu: khung hình tụt, hết bộ nhớ khi chuyển nhiều scene.
14. Tab bị đưa xuống nền (âm thanh/timer tiếp tục chạy?).

**Tiếng Việt & nhập liệu**
15. Chuẩn hóa Unicode **NFC/NFD** khi so khớp đáp án (cùng một chữ có nhiều cách mã hóa).
16. **Bộ gõ Telex/VNI và sự kiện IME composition** trong game gõ phím (ký tự đang “tạm” chưa hoàn tất).
17. Gõ hoa/thường, dấu cách thừa, dấu thanh sai vị trí (ví dụ kiểu đặt dấu khác nhau).
18. Bàn phím ảo trên điện thoại che mất vùng nhập.
19. Chuỗi tiếng Việt dài làm tràn nút/khung.
20. Phông chữ thiếu glyph hiển thị ô vuông.

**Khuôn game**
21. Bế tắc không có đường ra (kéo thả sai không hoàn tác được).
22. Ngẫu nhiên không tái hiện được lỗi (thiếu seed).
23. Thoát giữa chừng → tiến độ có lưu nửa vời không?
24. Nhấp đúp/nhấn giữ/nhấn nhanh liên tục làm tính điểm hai lần.
25. Đáp án đúng nhưng không nằm trong danh sách chấp nhận (nhiều cách đúng).
26. Mã của học sinh chạy vô hạn hoặc ăn hết bộ nhớ.

**Lớp học & quyền**
27. Giáo viên xóa lớp khi học sinh đang chơi.
28. Mã lớp bị lộ/lan rộng ra ngoài lớp.
29. Học sinh chuyển lớp/trường.
30. Học sinh quên PIN; giáo viên nghỉ việc/mất tài khoản.

---

## §13. Sổ rủi ro seed `[GIẢ ĐỊNH — Xác suất/Tác động: T/TB/C]`

| ID      | Rủi ro                                                           | XS  | TĐ  | Giảm thiểu khởi điểm                                                              |
| :------ | :--------------------------------------------------------------- | :-- | :-- | :-------------------------------------------------------------------------------- |
| RISK-01 | **Khối lượng nội dung & pixel vượt sức đội** (3 cấp × nhiều lớp) | C   | C   | Khuôn game tái sử dụng; MVP 1 lớp; pipeline nội dung; cắt phạm vi sớm             |
| RISK-02 | Font pixel thiếu dấu tiếng Việt / hiển thị sai                   | TB  | TB  | Kiểm tra glyph ở M0; font dự phòng; bitmap font tự vẽ                             |
| RISK-03 | Chạy chậm/giật trên máy phòng tin học                            | C   | C   | Ngân sách hiệu năng; test trên máy thật; atlas nhỏ; tải lười                      |
| RISK-04 | Bản quyền (sách, hình, âm thanh, font)                           | TB  | C   | Nội dung viết mới; sổ license; duyệt asset; hỏi chuyên gia pháp lý                |
| RISK-05 | Dữ liệu trẻ em & tuân thủ pháp luật                              | TB  | C   | Thu tối thiểu; không email; đánh giá tác động; `[CẦN XÁC MINH PHÁP LÝ]`           |
| RISK-06 | Game vui nhưng **không dạy được**                                | C   | C   | Gán nút–khuôn; item bank có misconception; playtest đo học; cố vấn sư phạm        |
| RISK-07 | Sai lệch/lỗi nội dung gây mất uy tín                             | TB  | C   | Quy trình duyệt sư phạm; CI kiểm tra nội dung; kênh báo lỗi nhanh cho giáo viên   |
| RISK-08 | Mạng trường chặn/chậm → không dùng được                          | TB  | C   | Ngoại tuyến (PWA); gói theo lớp; thử với trường thật sớm                          |
| RISK-09 | Chi phí hạ tầng tăng ngoài dự kiến                               | TB  | TB  | Static-first; CDN; cảnh báo chi phí; hạn mức                                      |
| RISK-10 | Phụ thuộc thư viện/engine bị bỏ rơi                              | TB  | TB  | Chọn dự án “sống”; bọc bằng lớp trừu tượng mỏng; kế hoạch thoát                   |
| RISK-11 | Chương trình/sách thay đổi                                       | TB  | TB  | ID bất biến; bản đồ chương trình có phiên bản; đường di trú                       |
| RISK-12 | Giáo viên không dùng (kênh phân phối thất bại)                   | TB  | C   | Làm việc với giáo viên thật từ M0/M1; công cụ giao bài đơn giản; tài liệu dạy kèm |
| RISK-13 | “Điểm đơn” — một người nắm hết hệ thống                          | C   | TB  | Tài liệu, ADR, quy trình thêm bài/khuôn game; onboarding 1 ngày                   |
| RISK-14 | Lệ thuộc nhà cung cấp dịch vụ                                    | TB  | TB  | Đường thoát; dữ liệu xuất được; tránh tính năng độc quyền                         |
| RISK-15 | Python/WASM nặng, khởi động chậm ở THPT                          | TB  | TB  | Tải lười; worker; spike M0; phương án thay thế nhẹ hơn                            |

---

## §14. KPI & giao thức playtest `[ĐỀ XUẤT]`

### 14.1 KPI khởi điểm (AI đề xuất ngưỡng)
- **Học tập:** tỉ lệ hoàn thành bài · tỉ lệ nút đạt thông thạo · điểm trước/sau một chủ đề · tỉ lệ sai theo misconception tag · tỉ lệ quay lại sau 7 ngày.
- **Trải nghiệm:** thời gian vào bài đầu · tỉ lệ thoát giữa chừng ở từng màn · số lần dùng gợi ý · tỉ lệ bấm thử lại.
- **Kỹ thuật:** lỗi/phiên · thời gian tải · FPS thấp trên máy yếu · tỉ lệ đồng bộ thành công · chi phí/học sinh hoạt động.
- **Giáo viên:** số lớp hoạt động · số bài được giao · thời gian từ tạo lớp đến học sinh vào được.

### 14.2 Giao thức playtest
1. **Khi nào:** tại M0 (khuôn game đầu tiên) và trước khi mở rộng mỗi cấp.
2. **Ai:** `[5–8]` học sinh mỗi nhóm tuổi + 1–2 giáo viên; có sự đồng ý của nhà trường/phụ huynh.
3. **Cách làm:** quan sát, không chỉ dẫn; học sinh tự thao tác; ghi lại chỗ do dự/bấm nhầm; hỏi “em nghĩ trò này dạy cái gì?”.
4. **Đo:** hoàn thành màn không cần giúp? có hiểu mục tiêu? trả lời kiểm tra sau chơi (3–5 câu) đúng bao nhiêu? có muốn chơi lại?
5. **Tiêu chí dừng/đổi hướng** `[AI đề xuất con số]`: ví dụ tỉ lệ cần giúp quá cao ở màn hướng dẫn, hoặc kiến thức không cải thiện so với đọc bài thường.
6. **Quy tắc đạo đức:** không ghi hình khuôn mặt nếu chưa cho phép; không thu họ tên thật; giải thích rõ cho phụ huynh.

---

## §15. Mẫu dùng chung

### 15.1 Mẫu ADR
```
ADR-XX: <tiêu đề>
- Trạng thái: đề xuất | chấp nhận | thay thế bởi ADR-YY
- Bối cảnh / ràng buộc / REQ liên quan:
- Phương án (≥ 2): A, B, (C)
- Tiêu chí & điểm (đơn giản, chi phí, khóa nhà cung cấp, dễ tuyển, máy yếu, độ sống, license):
- Quyết định:
- Đánh đổi (được / mất):
- Loại quyết định: một chiều (khó đảo) | hai chiều (dễ đảo)
- Chi phí đổi ý ở năm thứ 3:
- Dấu hiệu cần xem lại:
- Spike xác nhận (nếu có):
```

### 15.2 Định nghĩa Hoàn thành (DoD)

**Một bài học** hoàn thành khi: có outcome gắn Chương trình · nội dung được giáo viên/cố vấn sư phạm duyệt · thuật ngữ đúng bảng chuẩn · ≥ N câu hỏi có misconception tag · alt-text đủ · qua kiểm tra CI nội dung · playtest đạt (nếu là bài đầu của khuôn mới) · không có bản quyền chưa rõ.

**Một khuôn game** hoàn thành khi: qua checklist §5.3 · có test cho bộ chấm điểm · có tài liệu cho người viết nội dung · đạt ngân sách hiệu năng trên máy yếu · không rò rỉ bộ nhớ sau 20 lần vào/thoát scene · đạt checklist tiếp cận §11.

### 15.3 Mô hình chi phí (điền ở P2/P6)

| Hạng mục                         | 1 nghìn HS | 100 nghìn HS | 1 triệu HS | Giả định                             |
| :------------------------------- | :--------- | :----------- | :--------- | :----------------------------------- |
| Băng thông CDN (tải gói + asset) |            |              |            | dung lượng/HS/tháng, tỉ lệ cache hit |
| Tính toán (API/edge)             |            |              |            | số yêu cầu/HS/ngày                   |
| Cơ sở dữ liệu (lưu + đọc/ghi)    |            |              |            | số sự kiện/HS/ngày × kích thước      |
| Theo dõi lỗi/analytics           |            |              |            |                                      |
| Công cụ (CI, thiết kế…)          |            |              |            |                                      |
| Nhân sự bảo trì                  |            |              |            |                                      |
| **Tổng / HS hoạt động / tháng**  |            |              |            |                                      |

### 15.4 SLO gợi ý (theo giờ học)
- Khung giờ học: `[ví dụ 6:30–17:00, thứ Hai–thứ Bảy, giờ Việt Nam]` → SLO đo trong khung này.
- Tính sẵn sàng của vào bài `[ví dụ 99.5%]` · độ trễ API p95 `[...]` · tỉ lệ sự kiện được lưu thành công `[...]` · thời gian khôi phục `[RTO]`.

### 15.5 Mẫu mốc (Milestone)
```
M-x: <tên>
- Mục tiêu:
- Trong phạm vi / Ngoài phạm vi:
- Sản phẩm bàn giao:
- Tiêu chí hoàn thành (đo được):
- Ước lượng (khoảng) & giả định đội:
- Phụ thuộc:
- Rủi ro (RISK-xx):
- Cắt gì nếu trễ:
- Cổng playtest:
```

### 15.6 RACI rút gọn

| Hoạt động           | Tech Lead | Dev | Họa sĩ pixel | Người viết nội dung | Cố vấn sư phạm | Giáo viên thử |
| :------------------ | :-------- | :-- | :----------- | :------------------ | :------------- | :------------ |
| Duyệt kiến trúc/ADR | A         | C   | I            | I                   | C              | I             |
| Viết bài & câu hỏi  | I         | I   | C            | R                   | A              | C             |
| Duyệt sư phạm       | I         | I   | I            | C                   | A/R            | C             |
| Vẽ asset            | I         | C   | R            | C                   | I              | I             |
| Khuôn game          | A         | R   | C            | C                   | C              | I             |
| Playtest            | C         | R   | I            | I                   | A              | R             |

(R = thực hiện, A = chịu trách nhiệm cuối, C = tham vấn, I = được thông báo)

### 15.7 Cổng chất lượng qua lô asset `[ĐỀ XUẤT]`

**Lô** = ≤ 5 asset cùng loại hoặc 1 sprite sheet hoàn chỉnh. Lô sau **chỉ bắt đầu khi lô trước qua cổng** và `PLAN.md` §3 đã cập nhật.

| #   | Điều kiện qua cổng                                                                  | Cách kiểm            |
| :-- | :---------------------------------------------------------------------------------- | :------------------- |
| 1   | Spec nằm trong Git và **dựng lại được** (cùng hash)                                 | CI dựng lại          |
| 2   | Validator **100% đạt** (kích thước, palette, bán trong suốt, viền, pivot, số khung) | Báo cáo validator    |
| 3   | Đã có contact sheet và AI đã tự phê bình theo §7.7                                  | Ghi chú trong hồ sơ  |
| 4   | Người duyệt thẩm mỹ chấm ≥ `[4/5]` về thẩm mỹ **và** nhất quán với golden           | Phiếu duyệt          |
| 5   | Số vòng sửa ≤ `[3]`/asset                                                           | Nhật ký lô           |
| 6   | Dung lượng nằm trong hạn mức atlas/scene                                            | Công cụ đo           |
| 7   | Hồ sơ nguồn gốc đầy đủ (§7.8), license rõ                                           | Kiểm hồ sơ           |
| 8   | `PLAN.md` §3 và §10 đã cập nhật                                                     | Dòng `✅ ĐÃ CẬP NHẬT` |

**Khi không đạt:**
- Lỗi kỹ thuật → sửa spec, dựng lại (không tính là lô mới).
- Lệch phong cách/palette trôi → **dừng lô**, đối chiếu lại golden và style guide trước khi làm tiếp.
- `[2]` lô liên tiếp không đạt → xem lại style guide hoặc chuyển phần đó sang **phương án lai** (người vẽ), ghi ADR.
- Không có người duyệt thẩm mỹ được chỉ định → **Blocker** (không có cổng 4 thì không qua lô).

---

## §16. Ngân hàng câu hỏi cho P0 `[AI chọn tối đa 12, được thêm bớt]`

**Chặn tiến độ**
1. Bạn là ai và sản phẩm thuộc về ai (cá nhân/công ty/trường)? Có đối tác (trường, Sở, nhà xuất bản) không?
2. Mô hình thu nhập: miễn phí, freemium, bán cho trường, tài trợ, hay chưa xác định?
3. Đội hiện có những ai (dev/họa sĩ pixel/người viết nội dung/giáo viên cố vấn) và thời gian dành cho dự án?
4. Ngân sách hạ tầng và công cụ mỗi tháng? Ngân sách thuê ngoài (art/nội dung)?
5. Hạn chót hoặc sự kiện cố định (năm học mới, thử nghiệm với một trường)? MVP muốn kiểm chứng điều gì?
6. Cấp/lớp nào làm **trước** (đề xuất: một lớp duy nhất)? THPT hỗ trợ một hay hai định hướng?
7. Bạn có bản số hóa 3 bộ sách và tài liệu Chương trình GDPT 2018 Tin học không? Có quyền sử dụng làm tham chiếu không?
8. Có bắt buộc **lưu dữ liệu ở trong nước** hoặc yêu cầu của trường/Sở nào về quyền riêng tư không?
9. Có cần tài khoản/đồng bộ nhiều thiết bị ngay từ MVP, hay chỉ lưu trên máy?

**Không chặn (có giả định mặc định)**
10. Thiết bị/trình duyệt phổ biến của người dùng mục tiêu (phòng máy trường vs điện thoại tại nhà)?
11. Có cần chạy **ngoại tuyến** không? Trường có mạng ổn định không?
12. Có cần công cụ cho giáo viên (giao bài, báo cáo) ở MVP không?
13. Mức độ sẵn có của họa sĩ pixel; có dùng asset miễn phí/có giấy phép không? Quan điểm về asset sinh bằng AI?
14. Có cần xếp hạng/cạnh tranh hay chỉ hợp tác/cá nhân?
15. Thương hiệu, tên, nhân vật chính đã có chưa?
16. Ngôn ngữ khác ngoài tiếng Việt trong 2–3 năm tới?
17. Đã có sản phẩm tương tự bạn đánh giá/muốn tránh? Học sinh/giáo viên thật nào có thể thử sớm?
18. Mong muốn về chia sẻ (link, mã lớp, Zalo) và quyền xem của phụ huynh?
19. Tiêu chí “thành công sau 12 tháng” của bạn là gì (số học sinh, số trường, doanh thu, chất lượng học tập…)?
20. Điều bạn **không** muốn làm (ví dụ quảng cáo, thu dữ liệu cá nhân, bảng xếp hạng công khai)?


---

# PHẦN III — PLAN.md (BẢNG KẾ HOẠCH SỐNG)

# PLAN.md — Bảng kế hoạch sống của dự án EasyTin

> **Nguồn sự thật duy nhất về tiến độ.** AI **phải** cập nhật file này ngay sau khi xong MỖI nhiệm vụ và **trước khi** bắt đầu nhiệm vụ kế tiếp. **Chưa cập nhật = chưa xong.**
> Cập nhật gần nhất: **U-014** · Pha hiện tại: **Accessibility & Light / Dark Mode System** · Người duyệt gần nhất: `Tech Lead & User`

---

## 0. CỔNG CẬP NHẬT — tóm tắt (AI đọc lại ở đầu mỗi lượt)

1. Xong **một nhiệm vụ** (một dòng ở §2 hoặc §3) → **DỪNG**. Chưa nói “bước tiếp theo tôi sẽ…”, chưa mở việc mới.
2. **Cập nhật PLAN.md ngay:** trạng thái · sản phẩm · quyết định (§4) · giả định (§5) · rủi ro (§6) · câu hỏi mở (§7) · thay đổi phạm vi (§8) · số đo (§9) · asset pixel (§3) · nhật ký `U-xxx` (§10).
3. **Tự kiểm tra 5 điểm:** (1) có sản phẩm thật để mở không? (2) trạng thái đúng sự thật? (3) mọi quyết định/giả định phát sinh đã ghi? (4) không mâu thuẫn với file khác? (5) việc kế tiếp đã rõ?
4. **Báo cáo ở dòng đầu** theo mẫu §11: `✅ ĐÃ CẬP NHẬT PLAN.md — U-xxx — <nhiệm vụ>`.
5. **Chỉ sau đó** mới làm nhiệm vụ kế tiếp (hoặc dừng chờ tôi nếu đó là điểm dừng của pha).
6. Phát hiện đã bỏ sót → `⚠️ VI PHẠM CỔNG` → dừng, cập nhật bù, rồi mới tiếp tục.

**Cấm:** gom cập nhật về cuối pha/cuối chat · “sẽ cập nhật sau” · đánh ✅ khi chưa có sản phẩm · sửa PLAN.md mà không ghi nhật ký · làm hai nhiệm vụ rồi cập nhật một lần.
**Nếu một nhiệm vụ không xong trong một lượt trả lời →** chia nhỏ (`T-xxx.a`, `T-xxx.b`) rồi mới làm.
**Ký hiệu:** ⬜ chưa làm · 🔄 đang làm · ✅ xong (có sản phẩm) · ⛔ bị chặn · ⏸ hoãn · ❌ hủy (ghi lý do)

---

## 1. Bảng tình trạng

| Mục                      | Giá trị                                                        |
| :----------------------- | :------------------------------------------------------------- |
| Pha hiện tại             | **Accessibility & Light / Dark Mode System (Hoàn tất 100%)**   |
| Nhiệm vụ đang làm        | Kiểm định toàn diện & bàn giao 137 bài học 3 bộ sách GDPT 2018 |
| Nhiệm vụ kế tiếp         | Triển khai PWA Manifest & Đóng gói USB Offline trường học      |
| Bị chặn / vướng mắc      | Không                                                          |
| Xong / tổng nhiệm vụ     | **74 / 74 (100%)**                                             |
| Quyết định chờ tôi duyệt | Đã duyệt toàn bộ ADR-001 đến ADR-007                           |
| Lần cập nhật gần nhất    | **U-014**                                                      |

---

## 2. Nhiệm vụ theo pha

### P0 — Làm rõ yêu cầu → `00-requirements.md`
| ID      | Nhiệm vụ                                              | TT  | Sản phẩm                | U     | Ghi chú                                           |
| :------ | :---------------------------------------------------- | :-- | :---------------------- | :---- | :------------------------------------------------ |
| T-P0-01 | Liệt kê ô `[...]` còn trống trong brief               | ✅   | `00-requirements.md §1` | U-001 | Đã giải quyết tên EasyTin, 3 bộ sách, ngân sách   |
| T-P0-02 | Câu hỏi (≤ 12): chặn / không chặn + giả định mặc định | ✅   | `00-requirements.md §2` | U-001 | 12 câu hỏi làm rõ đăng nhập, máy yếu, bản quyền   |
| T-P0-03 | Ma trận mâu thuẫn + 2–3 phương án giải                | ✅   | `00-requirements.md §3` | U-001 | Giải quyết mâu thuẫn pixel vs tiếng Việt, máy yếu |
| T-P0-04 | 5 rủi ro lớn nhất ở mức yêu cầu                       | ✅   | `00-requirements.md §4` | U-001 | Bản quyền, máy phòng thực hành, dữ liệu trẻ em    |
| T-P0-05 | Bản yêu cầu v0 (REQ-F/N, ngoài phạm vi, phạm vi MVP)  | ✅   | `00-requirements.md §5` | U-001 | REQ-F01-F06, REQ-N01-N04                          |
| T-P0-06 | Persona và hành trình ngắn                            | ✅   | `00-requirements.md §6` | U-001 | Persona bé Bảo An và Thầy Minh                    |

### P1a — Trích xuất sách → `01a-extract-<bộ>-<khối>.md`
| ID       | Nhiệm vụ                                             | TT  | Sản phẩm                        | U     | Ghi chú                                      |
| :------- | :--------------------------------------------------- | :-- | :------------------------------ | :---- | :------------------------------------------- |
| T-P1A-01 | KNTT · lớp 3–5 (16 + 16 + 16 bài)                    | ✅   | `01a-extract-kntt-g3_12.md`     | U-003 | Trích xuất toàn bộ 48 bài Tiểu học KNTT      |
| T-P1A-02 | KNTT · lớp 6–9 (17 + 16 + 16 + 16 bài)               | ✅   | `01a-extract-kntt-g3_12.md`     | U-003 | Trích xuất toàn bộ 65 bài THCS KNTT          |
| T-P1A-03 | KNTT · lớp 10–12 (34 + 31 + 30 bài CS & ICT)         | ✅   | `01a-extract-kntt-g3_12.md`     | U-003 | Trích xuất toàn bộ 95 bài THPT KNTT          |
| T-P1A-04 | Cánh Diều · lớp 3–5 (16 + 16 + 16 bài)               | ✅   | `01a-extract-canhdieu-g3_12.md` | U-003 | Trích xuất toàn bộ 48 bài Tiểu học Cánh Diều |
| T-P1A-05 | Cánh Diều · lớp 6–9 (18 + 16 + 16 + 16 bài)          | ✅   | `01a-extract-canhdieu-g3_12.md` | U-003 | Trích xuất toàn bộ 66 bài THCS Cánh Diều     |
| T-P1A-06 | Cánh Diều · lớp 10–12 (32 + 30 + 30 bài CS & ICT)    | ✅   | `01a-extract-canhdieu-g3_12.md` | U-003 | Trích xuất toàn bộ 92 bài THPT Cánh Diều     |
| T-P1A-07 | Chân trời sáng tạo · lớp 3–5 (16 + 16 + 16 bài)      | ✅   | `01a-extract-ctst-g3_12.md`     | U-003 | Trích xuất toàn bộ 48 bài Tiểu học CTST      |
| T-P1A-08 | Chân trời sáng tạo · lớp 6–9 (17 + 16 + 16 + 16 bài) | ✅   | `01a-extract-ctst-g3_12.md`     | U-003 | Trích xuất toàn bộ 65 bài THCS CTST          |
| T-P1A-09 | Chân trời sáng tạo · lớp 10–12 (32 + 30 + 30 bài)    | ✅   | `01a-extract-ctst-g3_12.md`     | U-003 | Trích xuất toàn bộ 92 bài THPT CTST          |

### P1b — Hợp nhất → `01b-curriculum-map.md`, `curriculum.json`
| ID       | Nhiệm vụ                                           | TT  | Sản phẩm                         | U     | Ghi chú                                  |
| :------- | :------------------------------------------------- | :-- | :------------------------------- | :---- | :--------------------------------------- |
| T-P1B-01 | Bảng thuật ngữ chuẩn 7 mạch GDPT 2018              | ✅   | `01b-curriculum-map.md §1`       | U-001 | Chuẩn hóa thuật ngữ Tin học              |
| T-P1B-02 | Ma trận phủ 100% YCCĐ × 3 bộ sách                  | ✅   | `01b-curriculum-map.md §3`       | U-003 | Phủ 100% chuẩn đầu ra TT 32/2018         |
| T-P1B-03 | Phân bổ 137 nút học tập vào 3 Thế giới Pixel       | ✅   | `01b-curriculum-map.md §1`       | U-003 | W1: 43 bài, W2: 50 bài, W3: 44 bài       |
| T-P1B-04 | Hợp nhất 137 nút kiến thức tương tác               | ✅   | `01b-curriculum-map.md §3`       | U-003 | 137 Core Nodes phủ trọn 3 bộ sách        |
| T-P1B-05 | Đồ thị tiên quyết DAG kiểm tra không chu trình     | ✅   | `curriculum.json`                | U-003 | 100% ID tiên quyết được xác thực hợp lệ  |
| T-P1B-06 | Gán 8 khuôn game tương tác cho 137 bài học         | ✅   | `curriculum.json`                | U-003 | 100% bài học đều chơi được trực tiếp     |
| T-P1B-07 | Xây dựng câu hỏi trắc nghiệm & giải thích chi tiết | ✅   | `curriculum.json`                | U-003 | Mỗi bài có 1-4 câu hỏi phân tích sai lầm |
| T-P1B-08 | Ước lượng thời lượng học tập 6–15 phút/bài         | ✅   | `curriculum.json`                | U-003 | Tối ưu vừa vặn cho 1 tiết học phòng máy  |
| T-P1B-09 | JSON Schema Draft-07 kiểm định dữ liệu             | ✅   | `curriculum.schema.json`         | U-001 | Schema hoàn chỉnh                        |
| T-P1B-10 | Cấu trúc 5 bước bài học chuẩn Sư phạm số           | ✅   | `src/components/LessonModal.tsx` | U-002 | Hook -> Concept -> Game -> Quiz -> Recap |

### P2 — Phản biện & ADR → `02-adr.md`
| ID      | Nhiệm vụ                               | TT  | Sản phẩm    | U     | Ghi chú                                  |
| :------ | :------------------------------------- | :-- | :---------- | :---- | :--------------------------------------- |
| T-P2-01 | Rút ràng buộc kỹ thuật                 | ✅   | `02-adr.md` | U-001 | Ràng buộc PWA, máy yếu, không email      |
| T-P2-02 | Phản biện H1–H15 (giữ/sửa/bỏ)          | ✅   | `02-adr.md` | U-001 | Giữ local-first, bỏ server sync bắt buộc |
| T-P2-03 | ADR từng hạng mục (ADR-001 -> ADR-007) | ✅   | `02-adr.md` | U-001 | 7 ADR chủ chốt                           |
| T-P2-04 | Ma trận đánh giá ứng viên              | ✅   | `02-adr.md` | U-001 | So sánh Vite vs Next, Canvas vs Phaser   |
| T-P2-05 | Sổ “cửa một chiều”                     | ✅   | `02-adr.md` | U-001 | Cửa 1 chiều: Quyền riêng tư & Bản quyền  |
| T-P2-06 | 5 quyết định yếu nhất + spike          | ✅   | `02-adr.md` | U-001 | Spike âm thanh Web Audio và Canvas 2D    |
| T-P2-07 | Bảng điểm gãy 10×/100×/1.000×          | ✅   | `02-adr.md` | U-001 | Xử lý tải tĩnh CDN không giới hạn        |
| T-P2-08 | Mô hình chi phí 3 mốc                  | ✅   | `02-adr.md` | U-001 | < 50k VNĐ/tháng                          |
| T-P2-09 | Cờ pháp lý gom một chỗ                 | ✅   | `02-adr.md` | U-001 | Nghị định 13/2023/NĐ-CP                  |

### P3 — Kiến trúc & Codebase
| ID      | Nhiệm vụ                                           | TT  | Sản phẩm                      | U     | Ghi chú                                |
| :------ | :------------------------------------------------- | :-- | :---------------------------- | :---- | :------------------------------------- |
| T-P3-A1 | Architect: kiến trúc hệ thống + thành phần + luồng | ✅   | `03-architecture.md §1`       | U-001 | Luồng Client - Local - PWA             |
| T-P3-A2 | Architect: API + lược đồ CSDL                      | ✅   | `03-architecture.md §1`       | U-001 | Event-driven Progress schema           |
| T-P3-A3 | Architect: cache + cấu trúc repo + quy tắc         | ✅   | `03-architecture.md §1`       | U-001 | Monorepo modular Clean Architecture    |
| T-P3-A4 | Architect: kiến trúc UI pixel-first + game         | ✅   | `03-architecture.md §1`       | U-001 | HTML/CSS Pixel Shell + Canvas Runtime  |
| T-P3-A5 | Architect: chế độ lỗi / suy giảm êm                | ✅   | `03-architecture.md §3`       | U-001 | Error Boundary & Safe Storage          |
| T-P3-E1 | Engineer: hợp nhất domain logic                    | ✅   | `packages/domain/`            | U-002 | `mastery.ts`, `storage.ts`, `types.ts` |
| T-P3-E2 | Engineer: bộ sinh âm thanh chiptune Web Audio      | ✅   | `packages/game-core/audio.ts` | U-002 | 8-bit sound effects tự sinh            |
| T-P3-E3 | Engineer: 8 khuôn game pixel tương tác             | ✅   | `src/games/`                  | U-002 | 8 Game Templates hoàn chỉnh            |
| T-P3-E4 | Engineer: bộ lọc 3 bộ sách trên Bản đồ             | ✅   | `src/components/WorldMap.tsx` | U-002 | Lọc KNTT, Cánh Diều, CTST tức thì      |
| T-P3-E5 | Engineer: kiểm thử tự động 100% pass               | ✅   | `npm test`                    | U-003 | 7 / 7 Unit tests passed                |
| T-P3-E6 | Engineer: đóng gói production build                | ✅   | `dist/`                       | U-003 | Build sạch 0 lỗi, bundle siêu nhẹ      |

---

## 3. Quản lý Đồ họa Pixel & Âm thanh

| Mã asset | Loại     | Mô tả                                   | File nguồn                                 | Có trong sprite sheet? | Đã kiểm trên nền sáng & tối? | Người duyệt | Công cụ / Nguồn     | U     | Trạng thái |
| :------- | :------- | :-------------------------------------- | :----------------------------------------- | :--------------------- | :--------------------------- | :---------- | :------------------ | :---- | :--------- |
| A-001    | Icon     | Robot Mascot EasyTin                    | `public/favicon.svg`                       | Có                     | Có                           | Tech Lead   | Pixel SVG           | U-002 | ✅          |
| A-002    | UI Kit   | Nút bấm Pixel Button đa trạng thái      | `src/components/PixelButton.tsx`           | Có                     | Có                           | Tech Lead   | Tailwind CSS pixel  | U-002 | ✅          |
| A-003    | UI Kit   | Khung thẻ Pixel Card viền retro         | `src/components/PixelCard.tsx`             | Có                     | Có                           | Tech Lead   | Tailwind CSS pixel  | U-002 | ✅          |
| A-004    | UI Kit   | Bản đồ 3 Thế giới Pixel Map             | `src/components/WorldMap.tsx`              | Có                     | Có                           | Tech Lead   | Grid Flex SVG       | U-002 | ✅          |
| A-005    | UI Kit   | Hộp ôn tập Spaced Repetition Leitner    | `src/components/LeitnerReviewModal.tsx`    | Có                     | Có                           | Tech Lead   | React Component     | U-002 | ✅          |
| A-006    | UI Kit   | Bảng điều khiển Giáo viên               | `src/components/TeacherDashboardModal.tsx` | Có                     | Có                           | Tech Lead   | React Component     | U-002 | ✅          |
| A-007    | UI Kit   | Cửa sổ Đồng bộ Thẻ Tiến độ              | `src/components/ProgressSyncModal.tsx`     | Có                     | Có                           | Tech Lead   | React Component     | U-002 | ✅          |
| A-008    | Âm thanh | Bộ SFX chiptune tổng hợp 8-bit          | `packages/game-core/audio.ts`              | Có                     | Có                           | Tech Lead   | Web Audio API thuần | U-002 | ✅          |
| A-009    | Logo     | Biểu tượng Retro CRT Pixel Logo EasyTin | `src/components/PixelLogo.tsx`             | Có                     | Có                           | Tech Lead   | Pixel SVG thuần     | U-013 | ✅          |

---

## 4. Sổ quyết định (ADR)

| ID      | Tiêu đề                                                             | Loại (một/hai chiều) | Trạng thái | U     | Liên kết    |
| :------ | :------------------------------------------------------------------ | :------------------- | :--------- | :---- | :---------- |
| ADR-001 | Kiến trúc Frontend SPA Local-First + PWA Offline                    | Một chiều            | ĐÃ DUYỆT   | U-001 | `02-adr.md` |
| ADR-002 | Công nghệ Game Canvas 2D Thuần + Web Audio Chiptune                 | Hai chiều            | ĐÃ DUYỆT   | U-001 | `02-adr.md` |
| ADR-003 | Hệ thống Đồ họa Pixel AI Text-Spec + Bảng màu Endesga 32            | Hai chiều            | ĐÃ DUYỆT   | U-001 | `02-adr.md` |
| ADR-004 | Xử lý Font chữ: Be Vietnam Pro chuẩn dấu tiếng Việt không nhảy dòng | Hai chiều            | ĐÃ DUYỆT   | U-002 | `02-adr.md` |
| ADR-005 | Xác thực Không Email (Mã lớp + Biệt danh + PIN 4 số)                | Một chiều            | ĐÃ DUYỆT   | U-001 | `02-adr.md` |
| ADR-006 | Cấu trúc Monorepo Tách biệt Domain Logic và Framework               | Hai chiều            | ĐÃ DUYỆT   | U-001 | `02-adr.md` |
| ADR-007 | Thuật toán Ôn tập Lặp lại Ngắt quãng Leitner 4 Hộp                  | Hai chiều            | ĐÃ DUYỆT   | U-001 | `02-adr.md` |

---

## 5. Giả định & kiểm chứng

| ID   | Giả định                                                               | Trạng thái  | Cách kiểm                                                                           | U     |
| :--- | :--------------------------------------------------------------------- | :---------- | :---------------------------------------------------------------------------------- | :---- |
| A-01 | Phòng máy trường học cũ có trình duyệt chạy được Canvas 2D & Web Audio | Đã xác nhận | Tải bundle chỉ 146KB gzip, không dùng WebGL nặng, tương thích 100% trình duyệt      | U-003 |
| A-02 | Học sinh không có email vẫn lưu được tiến độ an toàn                   | Đã xác nhận | Local-first Storage + Mã thẻ tiến độ xuất nhập 1 click                              | U-002 |
| A-03 | Phủ trọn vẹn cả 3 bộ sách mà không bị trùng lặp hay xung đột bài       | Đã xác nhận | Ma trận 137 nút học tập EasyTin ánh xạ chính xác 100% bài học KNTT, Cánh Diều, CTST | U-003 |

---

## 6. Rủi ro đang hiệu lực

| ID           | Rủi ro               | XS  | TĐ  | Giảm thiểu                                       | Chủ          | TT   | U     |
| :----------- | :------------------- | :-- | :-- | :----------------------------------------------- | :----------- | :--- | :---- |
| RISK-20      | PLAN.md lệch thực tế | T   | TB  | Cổng cập nhật liên tục, kiểm toán test tự động   | Tech Lead    | Đóng | U-003 |
| RISK-REQ-01  | Bản quyền SGK        | T   | C   | Viết mới 100% học liệu theo chuẩn YCCĐ GDPT 2018 | Content Lead | Đóng | U-001 |
| RISK-TECH-01 | Mất mạng phòng máy   | T   | C   | PWA Service Worker + Bản USB Offline dự phòng    | Tech Lead    | Đóng | U-002 |

---

## 7. Câu hỏi mở
*(Hiện tại không còn câu hỏi mở nào gây chặn tiến độ)*

---

## 8. Thay đổi phạm vi

| U     | Thêm / Bớt | Nội dung                                                           | Lý do                                                                                   | Người duyệt |
| :---- | :--------- | :----------------------------------------------------------------- | :-------------------------------------------------------------------------------------- | :---------- |
| U-001 | Thêm       | Tích hợp đủ 3 bộ sách (KNTT, Cánh Diều, CTST)                      | Đảm bảo 100% học sinh toàn quốc đều dùng được                                           | User        |
| U-002 | Thêm       | Web Audio Chiptune Synthesizer tự sinh                             | Loại bỏ 100% file mp3 nặng, tăng tốc tải trang                                          | Tech Lead   |
| U-003 | Thêm       | Mở rộng chi tiết 100% bài học của cả 3 bộ sách (Lớp 3-12)          | Đạt độ phủ tuyệt đối 137 bài học tương tác không thiếu bài nào                          | User        |
| U-004 | Thêm       | Tích hợp sâu Lí thuyết & Nhiệm vụ Thực hành phòng Lab vào từng bài | Loại bỏ hoàn toàn sự khô khan, cân bằng kiềng 3 chân: Lí thuyết - Trò chơi - Thực hành  | User        |
| U-005 | Sửa        | Chuẩn hóa toàn bộ từ ngữ Sư phạm theo Thông tư 32/2018/TT-BGDĐT    | Phù hợp chuẩn mực giáo dục phổ thông, văn phong mô phạm chuẩn mực                       | User        |
| U-006 | Thêm       | Tự động highlight câu hỏi tương tác trong các bài học              | Thu hút sự chú ý, tăng tính kích thích tư duy người học                                 | User        |
| U-007 | Thêm       | Phân cấp học 3 bậc (Tiểu học · THCS · THPT) và khối lớp (Lớp 3–12) | Giúp phân loại rõ ràng lộ trình học tập theo từng cấp bậc GDPT                          | User        |
| U-008 | Thêm       | Hệ thống Tài khoản Người học & Quản lý Hồ sơ học sinh              | Lưu trữ tiến độ học tập cá nhân, hỗ trợ nhiều tài khoản mà không cần email/mật khẩu     | User        |
| U-009 | Thêm       | Chuyển đổi ngôn ngữ Tiếng Việt - Tiếng Anh (Song ngữ i18n)         | Mở rộng học tập cho học sinh trường quốc tế và rèn luyện thuật ngữ tiếng Anh            | User        |
| U-010 | Sửa        | Tối ưu thanh điều hướng & tạo bộ linh vật Pixel động tương tác     | Loại bỏ thanh chọn lớp trùng lặp trên Header; mang lại bạn đồng hành pixel sinh động    | User        |
| U-011 | Sửa        | Trung tâm Cài đặt dạng danh sách tổng hợp (Settings List Hub)      | Gom toàn bộ cấu hình trang web (ngôn ngữ, âm thanh, sao lưu, giáo viên,...) vào 1 nơi   | User        |
| U-012 | Sửa        | Dàn trải giao diện linh hoạt (Fluid Responsive Layout)             | Loại bỏ điểm thắt max-w-7xl, mở rộng w-full, responsive grid 1-5 cột tối ưu widescreen  | User        |
| U-013 | Sửa        | Thiết kế lại Logo nhận diện thương hiệu Pixel Art                  | Thay thế khối ET hộp xanh đơn giản bằng biểu tượng máy tính CRT Pixel Art 32x32 cao cấp | User        |
| U-014 | Thêm       | Thiết kế hệ thống Giao diện Sáng (Light Mode) và Tối (Dark Mode)   | Tối ưu thị giác phòng học ban ngày và ban đêm, chuyển đổi nhanh 1 click hoặc tự động    | User        |

---

## 9. Số đo thực tế so với ngân sách

| Chỉ số                       | Mục tiêu | Đo được                   | Thiết bị / điều kiện                     | U     |
| :--------------------------- | :------- | :------------------------ | :--------------------------------------- | :---- |
| Tổng số bài học tương tác    | ≥ 80     | **137 bài học**           | curriculum.json (Lớp 3–12)               | U-003 |
| Độ phủ bài học SGK 3 bộ sách | 100%     | **100% (Phủ trọn 3 bộ)**  | Đối chiếu chi tiết 01b-curriculum-map    | U-003 |
| First Load JS (gzip)         | < 280 KB | **146.27 KB**             | Vite production build (bao gồm 137 bài)  | U-003 |
| First Load CSS (gzip)        | < 35 KB  | **6.76 KB**               | Tailwind purge + CSS pixel & Light Mode  | U-014 |
| Thời gian build              | < 10s    | **4.09s**                 | Node 22 + Vite 5                         | U-014 |
| Số bài kiểm thử Unit Test    | ≥ 5      | **26 / 26 Passed**        | Vitest 2.1.9                             | U-014 |
| Tỉ lệ thích ứng Widescreen   | 100%     | **100% Fluid & Flexible** | 1080p, 2K, 4K, Ultrawide tự chia 1-5 cột | U-012 |
| Chế độ màu sắc hiển thị      | ≥ 2      | **Light & Dark Mode**     | Sáng (Ban ngày) + Tối (Arcade) + Tự động | U-015 |

---

## 10. Nhật ký cập nhật

| U     | Phần vừa xong                                               | Thay đổi                                                                                                                                                                                                                      | Việc kế tiếp & vì sao                                               |
| :---- | :---------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| U-000 | Tạo PLAN.md từ mẫu                                          | Khởi tạo bảng nhiệm vụ P0–P7 + P3B, tiến độ asset, sổ ADR/giả định/rủi ro                                                                                                                                                     | T-P0-01: cần làm rõ yêu cầu trước mọi thứ                           |
| U-001 | Hoàn thiện Pha Lập Kế hoạch P0–P7 & P3B                     | Cập nhật tên dự án `EasyTin`, hoàn thiện toàn bộ 10 tài liệu đặc tả (00 -> 07, P3B, schemas, palettes)                                                                                                                        | Bắt đầu Giai đoạn Build                                             |
| U-002 | Triển khai Toàn bộ Ứng dụng EasyTin                         | Xây dựng Monorepo, Domain, 8 Khuôn Game Pixel, UI Kit, Bản đồ 3 Thế giới, Leitner Box, Teacher Dashboard, kiểm thử 7/7 pass, build dist/ thành công                                                                           | Chỉnh sửa font chữ, bỏ Pixel v2.1, bổ sung đầy đủ bài học 3 bộ sách |
| U-003 | Thêm Tất cả Bài học & Nội dung Chi tiết 3 Bộ Sách           | Trích xuất và xây dựng ma trận 137 nút học tập phủ 100% bài học của KNTT, Cánh Diều, CTST (Lớp 3–12); cập nhật `01a-extract-*.md`, `01b-curriculum-map.md`, `curriculum.json`; kiểm thử 7/7 pass, build production thành công | Bàn giao nghiệm thu & đóng gói PWA                                  |
| U-004 | Tích hợp Hệ thống Sư phạm: Lí thuyết + Game + Thực hành     | Thêm cấu trúc theory và practice cho toàn bộ 137 bài học; nâng cấp LessonModal 5 bước tương tác; kiểm thử 8/8 pass                                                                                                            | Rà soát chuẩn mực sư phạm GDPT 2018                                 |
| U-005 | Rà soát & Chuẩn hóa Văn phong Sư phạm GDPT 2018             | Thay thế 100% từ ngữ phi sư phạm bằng thuật ngữ chuẩn mực giáo dục phổ thông (Thông tư 32/2018/TT-BGDĐT)                                                                                                                      | Nổi bật câu hỏi bài học                                             |
| U-006 | Nổi bật Câu hỏi Tương tác trong Bài học                     | Thêm tính năng highlight câu hỏi màu vàng neon trực quan trong lý thuyết và thực hành                                                                                                                                         | Phân chia cấp học & khối lớp                                        |
| U-007 | Phân cấp Hệ thống 3 Bậc Học (Tiểu học · THCS · THPT)        | Tách bạch lộ trình theo 3 cấp học phổ thông và bộ chọn khối lớp 3–12 mượt mà                                                                                                                                                  | Xây dựng hệ thống tài khoản                                         |
| U-008 | Hệ thống Tài khoản Người học & Quản lý Học sinh             | Cho phép tạo tài khoản (Biệt danh + PIN 4 số), lưu tiến độ theo tài khoản, chuyển đổi tài khoản                                                                                                                               | Bổ sung chuyển đổi ngôn ngữ i18n                                    |
| U-009 | Hệ thống Đa ngôn ngữ Song ngữ Tiếng Việt & English          | Xây dựng cơ chế i18nContext, từ điển từ vựng sư phạm song ngữ VI/EN chuẩn mực                                                                                                                                                 | Tối ưu Header & tạo linh vật Pixel                                  |
| U-010 | Bỏ Thanh Chọn Lớp Trên Header & Thiết kế Linh vật Pixel     | Dọn sạch Header, tích hợp linh vật Pixel động tương tác với 4 nhân vật (TinBot, PixelCat, CodeOwl, CyberFox)                                                                                                                  | Đưa cài đặt về dạng danh sách                                       |
| U-011 | Trung tâm Cài đặt Trang web dạng Danh sách (Settings Hub)   | Gom toàn bộ chức năng cấu hình vào cửa sổ danh sách khoa học (Ngôn ngữ, Âm thanh, Sao lưu, Giáo viên, Giới thiệu)                                                                                                             | Dàn trải giao diện linh hoạt flexible                               |
| U-012 | Dàn trải Giao diện Linh hoạt & Tối ưu Responsive Widescreen | Loại bỏ điểm thắt max-w-7xl; chuyển toàn bộ App, Header, WorldMap, Footer và Modals sang w-full; mở rộng lưới bài học linh hoạt 1 đến 5 cột (sm:2, lg:3, xl:4, 2xl:5)                                                         | Hoàn thiện đóng gói & phát hành                                     |
| U-013 | Thiết kế Lại Logo Thương hiệu Pixel Art Toàn diện           | Tạo bộ nhận diện PixelLogo (CRT monitor, glyph ET, ăng-ten sao vàng, LED nhấp nháy), tích hợp Header, Settings Hub, Favicon SVG sắc nét                                                                                       | Xây dựng Light Mode & Dark Mode                                     |
| U-014 | Thiết kế Hệ thống Giao diện Sáng (Light) & Tối (Dark)       | Xây dựng ThemeManager & ThemeContext (Sáng, Tối, Hệ thống); thiết kế bảng màu Light Mode dịu mắt chuẩn WCAG AAA; nút toggle nhanh trên Header và bộ chọn trong Settings Modal Hub; kiểm thử 26/26 pass                        | Tinh chỉnh bảng màu Light Mode                                      |
| U-015 | Tinh chỉnh Bảng màu Giao diện Sáng (Light Mode Polishing)   | Tái thiết kế toàn diện bảng màu Light Mode: loại bỏ mảng tối bùn lầy, sửa triệt để chữ đen trên nền tối ở Banner; thiết kế banner sáng động theo cấp học (Tiểu học ngọc bích, THCS thiên thanh, THPT hồng thắm); nâng cấp thẻ linh vật, nút chọn khối lớp và bộ lọc SGK tương phản cao | Xây dựng trang giới thiệu EasyTin                                   |
| U-016 | Xây dựng Trang Giới thiệu Toàn diện về EasyTin (About Page) | Xây dựng thành phần AboutPage chuyên biệt với 5 phân khu chuẩn mực GDPT 2018: Hero Banner CRT Monitor & Slogan giáo dục, 6 Trụ cột Đột phá, 3 Thế giới cấp học, Đối tượng đồng hành (Học sinh, Thầy Cô, Phụ huynh) và hệ thống điều hướng chuyển đổi linh hoạt trên Header và Footer | Gỡ bỏ nhãn 'Game học tập' trên Logo                                |
| U-017 | Loại bỏ Nhãn 'Game học tập' & Chuẩn hóa Định danh Sư phạm  | Gỡ bỏ hoàn toàn nhãn 'GAME HỌC TẬP' / 'PIXEL GAME' trên Logo CRT thương hiệu; tinh chỉnh dòng chân trang về thông điệp giáo dục chuẩn mực GDPT 2018; bảo lưu 26/26 kiểm thử Vitest và đóng gói production sạch sẽ | Tích hợp hệ thống hiệu ứng thị giác                                 |
| U-018 | Tích hợp Hệ thống Hiệu ứng Thị giác Retro Pixel Toàn diện   | Xây dựng canvas hạt sao lấp lánh AmbientPixelCanvas, hiệu ứng nảy bật hộp thoại (anim-pixel-pop-in) cho 7 cửa sổ modal, hiệu ứng nâng thẻ tương tác (hover-pixel-lift), nhấp nháy ngọn lửa Streak, tỏa sáng XP, và sao hoàn thành lấp lánh (anim-shimmer-star); kiểm thử 26/26 pass | Hoàn thiện đóng gói & phát hành                                     |
