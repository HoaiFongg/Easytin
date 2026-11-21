# 00-requirements.md — Bản đặc tả yêu cầu EasyTin (v0.1)

> **Dự án:** EasyTin — Nền tảng học Tin học phổ thông dạng game Pixel  
> **Cấp độ:** Tiểu học (Lớp 3–5) · THCS (Lớp 6–9) · THPT (Lớp 10–12)  
> **Khung chương trình:** Chương trình GDPT 2018 & 3 bộ sách (KNTT, Cánh Diều, Chân trời sáng tạo)  
> **Ngày phê duyệt v0:** 2026-11-21  

---

## 1. Giải quyết các ô `[...]` trong brief ban đầu

| Mục trong Brief | Giá trị xác định cho EasyTin | Cơ sở quyết định |
|---|---|---|
| **Tên làm việc** | `EasyTin` | Đã chốt chính thức theo yêu cầu dự án. |
| **3 bộ sách** | *Kết nối tri thức với cuộc sống*, *Cánh Diều*, *Chân trời sáng tạo*. | Đạt 100% độ phủ trường học công lập và tư thục tại Việt Nam. |
| **Ba cấp học** | Tiểu học (3–5), THCS (6–9), THPT (10–12 gồm cả Tin học ứng dụng ICT và Khoa học máy tính CS). | Đồng bộ toàn diện khung GDPT 2018 Tin học. |
| **Mô hình triển khai** | **Freemium đạo đức:** Miễn phí 100% toàn bộ nội dung học cơ bản và chế độ Offline cho học sinh cá nhân; gói mở rộng cho Trường học/Phòng GD&ĐT (quản lý tập trung, báo cáo học bạ số). | Đảm bảo tính tiếp cận bình đẳng cho học sinh vùng khó khăn. |
| **Chủ sở hữu & pháp nhân** | Tổ chức giáo dục công nghệ EdTech Việt Nam độc lập hướng cộng đồng. | Đảm bảo tuân thủ Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân. |
| **Ngân sách hạ tầng mốc khởi đầu** | ≤ $15 – $30/tháng (giai đoạn 0–10.000 người dùng hàng tháng MAU). | Kiến trúc Jamstack tĩnh + Local-first (IndexedDB) + CDN Edge miễn phí/rẻ. |
| **Đội ngũ nòng cốt** | 1 Tech Lead/Fullstack Engineer, 1 Content/Pedagogy Lead, 1 Pixel Artist/Technical Designer (hỗ trợ bởi AI asset pipeline). | Đội nhỏ tinh gọn, tự động hóa cao bằng toolchain. |
| **Đồ họa pixel** | AI sinh đặc tả lưới + procedural generation qua toolchain `sprite-forge` + kiểm duyệt thủ công bởi Art Lead. | Tối ưu chi phí, đảm bảo 100% bảng màu khóa và tương phản. |
| **Lưu trữ dữ liệu trong nước** | Client-first (lưu tại máy học sinh qua IndexedDB/LocalStorage). Server sync (nếu có lớp học): Cloudflare Workers KV hoặc máy chủ VPS đặt tại Hà Nội/TP.HCM (Viettel IDC/VNPT). | Tuân thủ triệt để Luật An ninh mạng & Nghị định 13/2023/NĐ-CP. |

---

## 2. Ngân hàng 12 câu hỏi làm rõ (Chặn & Không chặn)

1. **[CHẶN] Q1: Học sinh tiểu học chưa có email thì đăng nhập như thế nào?**  
   *Giả định mặc định:* Không dùng email. Đăng nhập bằng **Mã lớp (6 ký tự) + Biệt danh + Mã PIN 4 số / Hình vẽ pixel 3 ký hiệu**. Chế độ "Khách chơi ngay" không cần đăng nhập, lưu tiến độ cục bộ.
2. **[CHẶN] Q2: Phòng máy trường học cũ (Core 2 Duo, RAM 2-4GB, Windows 7, Chrome cũ) có chạy nổi không?**  
   *Giả định mặc định:* Kiến trúc Canvas 2D nhẹ + CSS pixel tối giản, tổng tải ban đầu ≤ 800KB gzipped, không dùng engine 3D/WebGL nặng, 60 FPS ổn định trên CPU yếu.
3. **[CHẶN] Q3: Bản quyền nội dung từ 3 bộ sách giáo khoa giải quyết ra sao?**  
   *Giả định mặc định:* **Tuyệt đối không sao chép nguyên văn câu chữ, hình ảnh hay bài tập SGK.** Hệ thống chỉ trích xuất *Yêu cầu cần đạt (YCCĐ)* của Bộ GD&ĐT, toàn bộ bối cảnh câu chuyện, nhân vật, bài tập, câu hỏi mini-game được viết mới 100%.
4. **[KHÔNG CHẶN] Q4: Mạng trường học chập chờn hoặc không có internet khi thực hành?**  
   *Giả định mặc định:* Hỗ trợ Progressive Web App (PWA) Offline-first. Sau lần tải đầu tiên, toàn bộ game và bài học của khối lớp chạy ngoại tuyến 100%. Tiến độ tự đồng bộ khi có mạng.
5. **[KHÔNG CHẶN] Q5: Font pixel có bị lỗi dấu tiếng Việt (ă, â, ê, ô, ơ, ư, đ, các dấu thanh) không?**  
   *Giả định mặc định:* Tuyệt đối không rasterize chữ thành ảnh. Dùng font web dễ đọc (Inter / Be Vietnam Pro) cho nội dung bài đọc, và bộ bitmap font pixel tùy biến đã kiểm tra đủ 134 ký tự tiếng Việt có dấu cho tiêu đề và nút bấm.
6. **[KHÔNG CHẶN] Q6: Làm sao tránh áp lực tâm lý (dark patterns) đối với học sinh nhỏ tuổi?**  
   *Giả định mặc định:* Không có đồng hồ đếm ngược sinh lo âu; không có cơ chế mất streak khi nghỉ học; không có loot-box may rủi; không trừ điểm phạt khi làm sai; phản hồi tập trung vào *giải thích nguyên nhân hiểu sai (misconception)*.
7. **[KHÔNG CHẶN] Q7: Học sinh khiếm thị màu hoặc giảm thị lực có tiếp cận được không?**  
   *Giả định mặc định:* Bảng màu đạt tương phản WCAG 2.1 AA (≥ 4.5:1), mọi trạng thái thông tin (đúng/sai, nhóm, loại) đều kết hợp Icon + Nhãn chữ + Màu sắc.
8. **[KHÔNG CHẶN] Q8: Việc thực hành gõ phím tiếng Việt (Telex/VNI) trong game như thế nào?**  
   *Giả định mặc định:* Bộ gõ chuẩn hóa Unicode NFC tự động, game chấp nhận cả xử lý composition string của bàn phím tiếng Việt hệ điều hành (Unikey, EVKey).
9. **[KHÔNG CHẶN] Q9: Lập trình Python ở THPT chạy ra sao trên trình duyệt không có backend?**  
   *Giả định mặc định:* Tải lười (lazy load) Pyodide / Skulpt trong Web Worker, chỉ tải ở bài học có code Python, hiển thị thanh tiến trình rõ ràng.
10. **[KHÔNG CHẶN] Q10: Giáo viên quản lý lớp như thế nào nếu không bắt học sinh tạo tài khoản?**  
    *Giả định mặc định:* Giáo viên tạo lớp -> hệ thống sinh danh sách mã PIN nhanh -> phát cho học sinh hoặc chia sẻ mã lớp.
11. **[KHÔNG CHẶN] Q11: Đo lường mức độ thông thạo kiến thức (Mastery) thế nào?**  
    *Giả định mặc định:* Thuật toán lặp lại ngắt quãng Leitner 4 hộp (hộp 1: 1 ngày, hộp 2: 3 ngày, hộp 3: 7 ngày, hộp 4: 21 ngày). Đạt mastery khi đúng ≥ 80% trên ≥ 2 phiên học khác ngày.
12. **[KHÔNG CHẶN] Q12: Tốc độ cập nhật khi chương trình có điều chỉnh?**  
    *Giả định mặc định:* Tách rời mã nguồn (Engine) và Dữ liệu chương trình (Content JSON Schema v1), cập nhật nội dung qua JSON manifest không cần build lại core app.

---

## 3. Ma trận mâu thuẫn & Phương án giải quyết

| Mâu thuẫn | Phương án A | Phương án B | Phương án chọn & Đánh đổi |
|---|---|---|---|
| **Phong cách Pixel vs. Khả năng đọc tiếng Việt** | Dùng 100% font pixel vẽ tay cho toàn bộ app. | Dùng font hệ thống phẳng (Arial/Roboto) hoàn toàn. | **Phương án C (Lai):** Tiêu đề, số điểm, badge dùng Bitmap Pixel Font tiếng Việt chuẩn hóa; văn bản bài đọc, câu hỏi dùng font sans-serif hình học siêu nét (Be Vietnam Pro / Inter) bọc trong khung 9-slice pixel. |
| **Đồ họa sống động vs. Hiệu năng máy phòng học cũ** | Dùng Phaser 3 / PixiJS đầy đủ hiệu ứng hạt, ánh sáng. | Dùng giao diện HTML/DOM tĩnh không có chuyển động. | **Phương án C (Canvas 2D nhẹ + CSS Sprites):** Khung giao diện dùng HTML/CSS pixelated, màn chơi game dùng HTML5 Canvas 2D thuần được tối ưu hóa vòng lặp drawImage, RAM tiêu thụ < 80MB. |
| **Độ phủ 3 bộ sách vs. Tránh quá tải cho học sinh** | Tạo 3 lộ trình riêng biệt cho 3 bộ sách. | Chỉ chọn 1 bộ sách duy nhất làm chuẩn. | **Phương án C (Hợp nhất cây kiến thức GDPT 2018):** Lấy YCCĐ của Bộ GD&ĐT làm xương sống (nút kiến thức), mỗi nút chỉ ra bài học tương ứng trong KNTT, Cánh Diều, CTST để học sinh sách nào cũng học được bài phù hợp. |

---

## 4. 5 Rủi ro lớn nhất ở mức yêu cầu

1. **RISK-REQ-01: Bản quyền sách giáo khoa và khiếu nại sở hữu trí tuệ.**  
   *Mức độ:* Cao | *Tác động:* Rất cao  
   *Biện pháp:* 100% nội dung học liệu, câu đố, minh họa, cốt truyện do EasyTin tự biên soạn theo chuẩn YCCĐ Thông tư 32/2018/TT-BGDĐT. Giữ bảng đối chiếu chứng minh không sao chép tác phẩm phái sinh.
2. **RISK-REQ-02: Phòng máy trường học chặn Internet hoặc không có trình duyệt hiện đại.**  
   *Mức độ:* Trung bình | *Tác động:* Cao  
   *Biện pháp:* Kiến trúc PWA Service Worker offline hoàn toàn; có bản phân phối tĩnh một thư mục để thầy cô có thể copy qua USB mở trực tiếp bằng trình duyệt không cần internet.
3. **RISK-REQ-03: Trôi phong cách đồ họa (Style drift) và rủi ro bản quyền khi dùng AI sinh asset.**  
   *Mức độ:* Trung bình | *Tác động:* Trung bình  
   *Biện pháp:* Khóa bảng màu 16/32 màu cố định (Endesga 32); AI chỉ sinh mã đặc tả cấu trúc lưới; chạy validator tự động kiểm tra màu ngoài bảng và pixel bán trong suốt; người duyệt trước khi đưa vào git.
4. **RISK-REQ-04: Xâm phạm quyền riêng tư dữ liệu trẻ em theo Nghị định 13/2023/NĐ-CP.**  
   *Mức độ:* Thấp (nếu thiết kế đúng) | *Tác động:* Cực cao  
   *Biện pháp:* Tối thiểu hóa dữ liệu (Data Minimization): Không thu thập họ tên đầy đủ, ngày sinh, số điện thoại, email của học sinh. Lưu tiến độ tại trình duyệt cục bộ.
5. **RISK-REQ-05: Độ phức tạp của monorepo làm chậm tiến độ đội ngũ nhỏ.**  
   *Mức độ:* Trung bình | *Tác động:* Trung bình  
   *Biện pháp:* Áp dụng kiến trúc Clean Architecture mô-đun hóa trong một repo duy nhất (modular monolithic), tách domain và games thành các gói thuần TypeScript không phụ thuộc framework UI.

---

## 5. Bản yêu cầu kỹ thuật & chức năng v0

### 5.1 Yêu cầu chức năng (REQ-F)
- **REQ-F01 (Chọn cấp & Bản đồ thế giới pixel):** Cho phép học sinh chọn khối lớp (3 đến 12), hiển thị bản đồ thế giới dạng pixel với các đảo/vùng kiến thức.
- **REQ-F02 (Vòng lặp học 6 bước):** Mỗi nút kiến thức gồm 6 phần: Mở đầu trực quan -> Khám phá tri thức ngắn -> Game tương tác -> Kiểm tra củng cố -> Thử thách sáng tạo -> Tổng kết.
- **REQ-F03 (8 Khuôn game cốt lõi):**
  1. `sort-drag`: Kéo thả phân loại phần cứng, tệp, thiết bị vào/ra.
  2. `block-maze`: Mê cung ghép lệnh điều khiển nhân vật pixel (tuần tự, lặp, rẽ nhánh).
  3. `logic-puzzle`: Bật tắt công tắc nhị phân và ghép cổng logic AND, OR, NOT.
  4. `type-run`: Đua tốc độ gõ 10 ngón và phím tắt thông dụng.
  5. `match-memory`: Lật thẻ ghi nhớ thuật ngữ và biểu tượng tin học.
  6. `branch-story`: Tình huống rẽ nhánh đạo đức và an toàn trên không gian mạng.
  7. `bug-hunt`: Truy tìm và sửa lỗi trong thuật toán hoặc đoạn mã.
  8. `boss-quiz`: Trận chiến vượt ải đánh boss trả lời câu hỏi tổng kết chủ đề.
- **REQ-F04 (Hệ thống ghi nhận tiến độ & Leitner Box):** Thuật toán 4 hộp ngắt quãng nhắc ôn tập; lưu trữ trạng thái sao và huy hiệu cục bộ.
- **REQ-F05 (Âm thanh Chiptune tổng hợp):** Hiệu ứng âm thanh 8-bit sống động qua Web Audio API không tốn băng thông tải file wav/mp3 nặng; có nút bật/tắt rõ ràng.
- **REQ-F06 (Bảng quản lý Giáo viên tinh gọn):** Tạo mã lớp, cấu hình nhiệm vụ theo chủ đề, xem phân tích lỗ hổng kiến thức của học sinh.

### 5.2 Yêu cầu phi chức năng (REQ-N)
- **REQ-N01 (Tải nhanh & Nhẹ):** Dung lượng tải lần đầu (First Load JS/CSS) < 600 KB gzip. Thời gian tương tác (TTI) < 1.5s trên thiết bị yếu.
- **REQ-N02 (Hoạt động ngoại tuyến):** Khả dụng 100% khi ngắt mạng (PWA Offline Cache).
- **REQ-N03 (Độ nét pixel số nguyên):** Hỗ trợ `image-rendering: pixelated`, tỷ lệ scale số nguyên (1x, 2x, 3x, 4x) không mờ hình ở mọi tỷ lệ màn hình.
- **REQ-N04 (Không phụ thuộc backend cho trải nghiệm người học):** Mọi logic tính toán chấm điểm game chạy hoàn toàn ở Client.

---

## 6. Persona người dùng & Hành trình trải nghiệm

### Persona 1: Bé Bảo An (Lớp 4 — Trường Tiểu học Hòa Bình)
- **Đặc điểm:** Thích chơi game pixel, nhanh chán bài đọc dài, dùng máy tính của mẹ hoặc phòng máy trường màn hình 1366x768.
- **Hành trình:** Vào EasyTin -> Bấm "Chơi ngay" chọn Lớp 4 -> Thấy bản đồ "Thung lũng Số hóa" -> Chọn bài "Thiết bị vào - ra" -> Chơi game `sort-drag` nhặt chuột, bàn phím, màn hình vào đúng thùng -> Nghe tiếng chuông chiptune "ting ting!" -> Đạt 3 sao -> Nhận huy hiệu "Chiến binh Phần cứng".

### Persona 2: Thầy Hoàng Minh (Giáo viên Tin học trường THCS)
- **Đặc điểm:** Phải dạy lớp 40 học sinh trong 45 phút, máy tính phòng thực hành nhiều máy không có kết nối internet ra ngoài.
- **Hành trình:** Tải gói offline EasyTin về máy chủ mạng LAN trường hoặc USB -> Học sinh mở trình duyệt gõ địa chỉ nội bộ -> Thầy tạo mã lớp ngắn -> Học sinh nhập mã và hoàn thành bài tập -> Thầy nhìn màn hình tổng hợp thấy ngay 8 học sinh đang nhầm lẫn giữa RAM và ổ cứng.
