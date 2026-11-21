# 02-adr.md — Sổ quyết định kiến trúc & công nghệ EasyTin (ADR)

> **Dự án:** EasyTin  
> **Người sở hữu:** Technical Lead cấp cao  
> **Nguyên tắc:** Ưu tiên tối thượng sự đơn giản, không khóa nhà cung cấp, bảo vệ trẻ em 100%, chạy mượt trên máy yếu.

---

## Danh mục ADR

| ADR ID | Tiêu đề | Loại quyết định | Trạng thái | Ngày duyệt |
|---|---|---|---|---|
| `ADR-001` | Kiến trúc Frontend SPA Local-First + PWA Offline | Một chiều (One-way) | **ĐÃ DUYỆT** | 2026-11-21 |
| `ADR-002` | Công nghệ Game Canvas 2D Thuần + Web Audio Chiptune | Hai chiều (Two-way) | **ĐÃ DUYỆT** | 2026-11-21 |
| `ADR-003` | Hệ thống Đồ họa Pixel AI Text-Spec + Bảng màu Endesga 32 | Hai chiều (Two-way) | **ĐÃ DUYỆT** | 2026-11-21 |
| `ADR-004` | Xử lý Font chữ: Lai Bitmap Tiêu đề + Sans-serif Nội dung | Hai chiều (Two-way) | **ĐÃ DUYỆT** | 2026-11-21 |
| `ADR-005` | Xác thực Không Email (Mã lớp + Biệt danh + PIN 4 số) | Một chiều (One-way) | **ĐÃ DUYỆT** | 2026-11-21 |
| `ADR-006` | Cấu trúc Monorepo Tách biệt Domain Logic và Framework | Hai chiều (Two-way) | **ĐÃ DUYỆT** | 2026-11-21 |
| `ADR-007` | Thuật toán Ôn tập Lặp lại Ngắt quãng Leitner 4 Hộp | Hai chiều (Two-way) | **ĐÃ DUYỆT** | 2026-11-21 |

---

### ADR-001: Kiến trúc Frontend SPA Local-First + PWA Offline
- **Bối cảnh:** Hàng ngàn phòng máy trường học tại Việt Nam có máy tính cấu hình thấp, đường truyền internet chập chờn hoặc ngắt mạng trong giờ kiểm tra. Chi phí server cho hàng trăm ngàn học sinh truy cập đồng thời giờ cao điểm (thundering herd) sẽ làm vỡ ngân sách nếu xử lý logic trên backend.
- **Quyết định:** Chọn mô hình **Client-centric Local-first**. Toàn bộ logic trò chơi, tính điểm, lưu trữ tiến độ chạy trực tiếp trên trình duyệt sử dụng `localStorage` / `IndexedDB`. Ứng dụng xuất bản dưới dạng Static Web App (Vite + React + TypeScript) tích hợp PWA Service Worker.
- **Hệ quả & Đánh đổi:** 
  - *Ưu điểm:* Chi phí hosting = $0 (Cloudflare Pages / Vercel / GitHub Pages). Tải bài 1 lần, chơi ngoại tuyến vĩnh viễn. Không sợ sập server giờ học.
  - *Nhược điểm:* Học sinh đổi máy tính ở phòng thực hành thì tiến độ cục bộ chưa đồng bộ nếu chưa bấm nút xuất mã tiến độ hoặc chưa có mã lớp sync. Đã giải quyết bằng tính năng "Sao chép mã thẻ tiến độ" 6 chữ cái.

---

### ADR-002: Công nghệ Game Canvas 2D Thuần + Web Audio Chiptune
- **Bối cảnh:** Các engine game lớn như Phaser 3 (~1.2MB bundle) hoặc PixiJS tạo gánh nặng tải trang và tiêu tốn nhiều RAM của máy tính cũ.
- **Quyết định:** Viết **Micro Game Runtime** bằng HTML5 Canvas 2D thuần túy kết hợp React state component. Âm thanh tạo hoàn toàn bằng Web Audio API chiptune (Square/Triangle oscillators) qua code synthesizer, không tải bất kỳ file mp3/wav nào.
- **Hệ quả:** Tiết kiệm 95% dung lượng tài nguyên mạng. Dung lượng toàn bộ runtime game < 30KB. Khởi động tức thì trong 20 miligiây.

---

### ADR-003: Hệ thống Đồ họa Pixel AI Text-Spec + Bảng màu Endesga 32
- **Bối cảnh:** Cần hàng trăm sprite pixel chất lượng cao nhưng đội ngũ nhỏ và muốn tự động hóa, tránh trôi phong cách (style drift) và tránh bản quyền rủi ro.
- **Quyết định:** Áp dụng phương án lai A + B + C (§7.0). AI viết đặc tả lưới mã số màu JSON (`SpriteSpec`). Công cụ `sprite-forge` dựng ra pixel canvas trực tiếp dựa trên bảng màu khóa chuẩn **Endesga 32 (32 màu retro kinh điển)**.
- **Hệ quả:** Mọi asset đều có mã nguồn kiểm tra được trong Git diff, 0 màu lạ ngoài bảng, 0 pixel mờ nhòe bán trong suốt.

---

### ADR-004: Xử lý Font chữ: Lai Bitmap Tiêu đề + Sans-serif Nội dung
- **Bối cảnh:** Font pixel thông thường thiếu dấu tiếng Việt (ă, â, ê, ô, ơ, ư, đ, hỏi, ngã, nặng) hoặc gây mỏi mắt cho học sinh khi đọc câu hỏi dài.
- **Quyết định:** Dùng font pixel sắc nét (Press Start 2P / Silkscreen / Bitmap SVG) cho Tiêu đề, số điểm, nút bấm ngắn. Toàn bộ câu hỏi, hướng dẫn, bài đọc dùng font hệ thống hình học siêu nét (Be Vietnam Pro / Inter) được style theo tông màu retro pixel trong khung 9-slice.
- **Hệ quả:** Vừa giữ trọn hồn hoài niệm pixel của game, vừa đạt điểm tối đa về khả năng tiếp cận và chống cận thị học đường.

---

### ADR-005: Xác thực Không Email (Mã lớp + Biệt danh + PIN 4 số)
- **Bối cảnh:** Trẻ em tiểu học và THCS không có email cá nhân. Quy định pháp lý Nghị định 13/2023/NĐ-CP cấm thu thập dữ liệu cá nhân trẻ em khi chưa có sự đồng ý của cha mẹ.
- **Quyết định:** 
  1. Chế độ Khách (Chơi ngay): 1 click không cần bất kỳ thông tin gì.
  2. Chế độ Học sinh theo lớp: Giáo viên tạo phòng học -> Hệ thống sinh mã lớp 6 chữ cái (ví dụ: `TIN401`). Học sinh chỉ cần nhập Mã lớp + Biệt danh (ví dụ: `SocNhi`) + Mã PIN 4 số.
- **Hệ quả:** Tuân thủ pháp lý 100%, bảo vệ dữ liệu trẻ em tuyệt đối.
