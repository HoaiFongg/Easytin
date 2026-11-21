# 07-plan-on-a-page.md — Kế hoạch Tổng kết trên Một Trang EasyTin

> **Tầm nhìn:** Đưa EasyTin trở thành nền tảng thực hành Tin học dạng game Pixel quốc dân cho học sinh phổ thông Việt Nam từ Lớp 3 đến Lớp 12, biến mỗi giờ học Tin học thành một chuyến phiêu lưu kỳ thú.

---

## 1. Kế hoạch Tổng quan (Plan-on-a-Page)

```
====================================================================================================
EASYTIN — NỀN TẢNG HỌC TIN HỌC DẠNG GAME PIXEL CHO HỌC SINH VIỆT NAM (LỚP 3 – 12)
====================================================================================================

[ĐỐI TƯỢNG PHỤC VỤ]
- Học sinh Lớp 3–12 (Tiểu học · THCS · THPT)
- Giáo viên Tin học tại các trường phổ thông trên toàn quốc
- Học sinh vùng sâu vùng xa, phòng máy đời cũ, mạng chập chờn

[GIÁ TRỊ CỐT LÕI]
1. Bám sát Chương trình GDPT 2018 & 3 bộ SGK (KNTT, Cánh Diều, Chân trời sáng tạo).
2. Phong cách Pixel Retro cuốn hút, 100% tôn trọng thị giác và khả năng đọc tiếng Việt.
3. Chạy mượt 100% ngoại tuyến (Offline PWA), dung lượng siêu nhẹ (< 600KB).
4. An toàn trẻ em tuyệt đối: Không bắt buộc email, không quảng cáo, không thu thập dữ liệu cá nhân.
5. Vòng lặp học tập khoa học: Leitner Spaced Repetition 4 hộp + 8 khuôn game trí tuệ.

----------------------------------------------------------------------------------------------------
[KIẾN TRÚC & CÔNG NGHỆ]
- Frontend: Vite + React 18 + TypeScript + Tailwind CSS (Pixel Theme).
- Game Engine: Micro HTML5 Canvas 2D + Web Audio Synthesizer (Chiptune 8-bit).
- Dữ liệu: JSON Schema v1 độc lập mã nguồn + Local-First IndexedDB / LocalStorage.
- Đồ họa: Procedural Pixel Generator + Bảng màu khóa Endesga 32.
- Triển khai: Cloudflare Pages Edge CDN (Hà Nội, TP.HCM) + Bản USB Offline dự phòng.

----------------------------------------------------------------------------------------------------
[3 THẾ GIỚI KIẾN THỨC]
- Thế giới 1 (Lớp 3–5): "Thung lũng Số hóa" — Khám phá máy tính, chuột/phím, thuật toán phiêu lưu.
- Thế giới 2 (Lớp 6–9): "Rừng Mạng & Dữ liệu" — Số nhị phân, định tuyến gói tin, bảng tính, an toàn số.
- Thế giới 3 (Lớp 10–12): "Thành phố Thuật toán" — Lập trình Python, cổng logic, CSDL & Đại chiến Boss AI.

----------------------------------------------------------------------------------------------------
[8 KHUÔN GAME CỐT LÕI]
1. sort-drag (Phần cứng & Vào/Ra)      5. match-memory (Thẻ nhớ thuật ngữ)
2. block-maze (Robot mê cung lệnh)     6. branch-story (Hiệp sĩ an toàn mạng)
3. logic-puzzle (Nhị phân & Logic)     7. bug-hunt (Thợ săn lỗi lập trình)
4. type-run (Đua tốc độ gõ phím)       8. boss-quiz (Trận chiến trùm kiến thức)
====================================================================================================
```

---

## 2. Bảng kiểm Go / No-Go cho Dự án EasyTin

| Tiêu chí | Ngưỡng yêu cầu | Kết quả thẩm định | Trạng thái |
|---|---|---|---|
| **Bản quyền sách giáo khoa** | 100% nội dung viết mới, chỉ bám YCCĐ GDPT 2018 | Đã xác nhận không sao chép nguyên văn | **GO** |
| **Bảo vệ dữ liệu trẻ em** | Không thu thập email, SĐT, họ tên khai sinh | Chế độ Khách + Mã lớp học sinh | **GO** |
| **Khả năng đọc tiếng Việt** | Hiển thị đủ dấu, không lỗi font, tương phản ≥ 4.5:1 | Font hệ thống sắc nét + Bitmap tiêu đề | **GO** |
| **Hiệu năng máy phòng học** | Tải ban đầu < 800KB, chạy mượt trên RAM 2-4GB | Canvas 2D nhẹ + Web Audio Synthesizer | **GO** |
| **Vận hành & Ngân sách** | Chi phí duy trì < $20/tháng | Cloudflare Pages + Local-first | **GO** |
| **Tính khả thi kỹ thuật** | Monorepo module hóa, có sẵn schema & test | Kiến trúc sạch, dễ mở rộng 5 năm | **GO** |

---

## 3. PHÁN QUYẾT CHÍNH THỨC
**CHẤP THUẬN TOÀN BỘ KẾ HOẠCH — CHUYỂN NGAY SANG GIAI ĐOẠN TRIỂN KHAI CODE THỰC TẾ (BUILD PHASE).**
