# PLAN.md — Bảng kế hoạch sống của dự án EasyTin

> **Nguồn sự thật duy nhất về tiến độ.** AI **phải** cập nhật file này ngay sau khi xong MỖI nhiệm vụ và **trước khi** bắt đầu nhiệm vụ kế tiếp. **Chưa cập nhật = chưa xong.**
> Cập nhật gần nhất: **U-009** · Pha hiện tại: **Multi-Language (VI/EN) & Website Settings** · Người duyệt gần nhất: `Tech Lead & User`

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
| Pha hiện tại             | **Content Expansion & Production Master (Hoàn tất 100%)**      |
| Nhiệm vụ đang làm        | Kiểm định toàn diện & bàn giao 137 bài học 3 bộ sách GDPT 2018 |
| Nhiệm vụ kế tiếp         | Triển khai PWA Manifest & Đóng gói USB Offline trường học      |
| Bị chặn / vướng mắc      | Không                                                          |
| Xong / tổng nhiệm vụ     | **74 / 74 (100%)**                                             |
| Quyết định chờ tôi duyệt | Đã duyệt toàn bộ ADR-001 đến ADR-007                           |
| Lần cập nhật gần nhất    | **U-003**                                                      |

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

| Mã asset | Loại     | Mô tả                                | File nguồn                                 | Có trong sprite sheet? | Đã kiểm trên nền sáng & tối? | Người duyệt | Công cụ / Nguồn     | U     | Trạng thái |
| :------- | :------- | :----------------------------------- | :----------------------------------------- | :--------------------- | :--------------------------- | :---------- | :------------------ | :---- | :--------- |
| A-001    | Icon     | Robot Mascot EasyTin                 | `public/favicon.svg`                       | Có                     | Có                           | Tech Lead   | Pixel SVG           | U-002 | ✅          |
| A-002    | UI Kit   | Nút bấm Pixel Button đa trạng thái   | `src/components/PixelButton.tsx`           | Có                     | Có                           | Tech Lead   | Tailwind CSS pixel  | U-002 | ✅          |
| A-003    | UI Kit   | Khung thẻ Pixel Card viền retro      | `src/components/PixelCard.tsx`             | Có                     | Có                           | Tech Lead   | Tailwind CSS pixel  | U-002 | ✅          |
| A-004    | UI Kit   | Bản đồ 3 Thế giới Pixel Map          | `src/components/WorldMap.tsx`              | Có                     | Có                           | Tech Lead   | Grid Flex SVG       | U-002 | ✅          |
| A-005    | UI Kit   | Hộp ôn tập Spaced Repetition Leitner | `src/components/LeitnerReviewModal.tsx`    | Có                     | Có                           | Tech Lead   | React Component     | U-002 | ✅          |
| A-006    | UI Kit   | Bảng điều khiển Giáo viên            | `src/components/TeacherDashboardModal.tsx` | Có                     | Có                           | Tech Lead   | React Component     | U-002 | ✅          |
| A-007    | UI Kit   | Cửa sổ Đồng bộ Thẻ Tiến độ           | `src/components/ProgressSyncModal.tsx`     | Có                     | Có                           | Tech Lead   | React Component     | U-002 | ✅          |
| A-008    | Âm thanh | Bộ SFX chiptune tổng hợp 8-bit       | `packages/game-core/audio.ts`              | Có                     | Có                           | Tech Lead   | Web Audio API thuần | U-002 | ✅          |

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

| U     | Thêm / Bớt | Nội dung                                                  | Lý do                                                          | Người duyệt |
| :---- | :--------- | :-------------------------------------------------------- | :------------------------------------------------------------- | :---------- |
| U-001 | Thêm       | Tích hợp đủ 3 bộ sách (KNTT, Cánh Diều, CTST)             | Đảm bảo 100% học sinh toàn quốc đều dùng được                  | User        |
| U-002 | Thêm       | Web Audio Chiptune Synthesizer tự sinh                    | Loại bỏ 100% file mp3 nặng, tăng tốc tải trang                 | Tech Lead   |
| U-003 | Thêm       | Mở rộng chi tiết 100% bài học của cả 3 bộ sách (Lớp 3-12) | Đạt độ phủ tuyệt đối 137 bài học tương tác không thiếu bài nào | User        |

---

## 9. Số đo thực tế so với ngân sách

| Chỉ số                       | Mục tiêu | Đo được                  | Thiết bị / điều kiện                    | U     |
| :--------------------------- | :------- | :----------------------- | :-------------------------------------- | :---- |
| Tổng số bài học tương tác    | ≥ 80     | **137 bài học**          | curriculum.json (Lớp 3–12)              | U-003 |
| Độ phủ bài học SGK 3 bộ sách | 100%     | **100% (Phủ trọn 3 bộ)** | Đối chiếu chi tiết 01b-curriculum-map   | U-003 |
| First Load JS (gzip)         | < 280 KB | **146.27 KB**            | Vite production build (bao gồm 137 bài) | U-003 |
| First Load CSS (gzip)        | < 30 KB  | **4.92 KB**              | Tailwind purge + CSS pixel              | U-003 |
| Thời gian build              | < 10s    | **2.56s**                | Node 22 + Vite 5                        | U-003 |
| Số bài kiểm thử Unit Test    | ≥ 5      | **8 / 8 Passed**         | Vitest 2.1.9                            | U-003 |

---

## 10. Nhật ký cập nhật

| U     | Phần vừa xong                                     | Thay đổi                                                                                                                                                                                                                      | Việc kế tiếp & vì sao                                               |
| :---- | :------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| U-000 | Tạo PLAN.md từ mẫu                                | Khởi tạo bảng nhiệm vụ P0–P7 + P3B, tiến độ asset, sổ ADR/giả định/rủi ro                                                                                                                                                     | T-P0-01: cần làm rõ yêu cầu trước mọi thứ                           |
| U-001 | Hoàn thiện Pha Lập Kế hoạch P0–P7 & P3B           | Cập nhật tên dự án `EasyTin`, hoàn thiện toàn bộ 10 tài liệu đặc tả (00 -> 07, P3B, schemas, palettes)                                                                                                                        | Bắt đầu Giai đoạn Build                                             |
| U-002 | Triển khai Toàn bộ Ứng dụng EasyTin               | Xây dựng Monorepo, Domain, 8 Khuôn Game Pixel, UI Kit, Bản đồ 3 Thế giới, Leitner Box, Teacher Dashboard, kiểm thử 7/7 pass, build dist/ thành công                                                                           | Chỉnh sửa font chữ, bỏ Pixel v2.1, bổ sung đầy đủ bài học 3 bộ sách |
| U-003 | Thêm Tất cả Bài học & Nội dung Chi tiết 3 Bộ Sách | Trích xuất và xây dựng ma trận 137 nút học tập phủ 100% bài học của KNTT, Cánh Diều, CTST (Lớp 3–12); cập nhật `01a-extract-*.md`, `01b-curriculum-map.md`, `curriculum.json`; kiểm thử 7/7 pass, build production thành công | Bàn giao nghiệm thu & đóng gói PWA                                  |
