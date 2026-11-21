# 04-review.md — Báo cáo rà soát 5 Lăng kính EasyTin

> **Hội đồng rà soát độc lập:** Chuyên gia Bảo mật · Frontend/A11y · Vận hành/Gỡ lỗi · Kiến trúc phần mềm · Cố vấn Sư phạm & An toàn trẻ em.

---

## 1. Lăng kính 1: Bảo mật (Security)
- **Đánh giá:** Chọn kiến trúc Local-First và xác thực không email là quyết định bảo mật xuất sắc nhất, loại trừ 99% bề mặt tấn công PII (Personally Identifiable Information).
- **Điểm lưu ý:** Không lưu mã PIN dạng văn bản thô. Sử dụng hàm băm SHA-256 kèm salt cho mã PIN của học sinh nếu có sync lên lớp học.
- **Phán quyết:** **ĐẠT (PASS)**.

---

## 2. Lăng kính 2: Frontend & Khả năng tiếp cận (A11y)
- **Đánh giá:** Thiết kế pixel retro dễ bị lạm dụng gây mỏi mắt nếu rasterize chữ. Bản đặc tả của EasyTin đã ngăn chặn điều này bằng cách bắt buộc văn bản nội dung là text thật của trình duyệt.
- **Tiêu chuẩn kiểm tra:**
  1. Tương phản màu đạt tỷ lệ ≥ 4.5:1 với chữ thường và ≥ 3:1 với chữ lớn.
  2. Bàn phím điều hướng được 100% các nút và màn chơi qua phím Tab, Enter, Space và phím mũi tên.
  3. Hỗ trợ media query `prefers-reduced-motion: reduce` tự động tắt hiệu ứng rung lắc màn hình và hạt nổ pixel.
- **Phán quyết:** **ĐẠT (PASS)**.

---

## 3. Lăng kính 3: Gỡ lỗi & Vận hành (Debugging & Observability)
- **Đánh giá:** Trò chơi có cơ chế tạo seed ngẫu nhiên (`seed: number`) giúp tái hiện chính xác lỗi của màn chơi khi học sinh báo cáo.
- **Bắt lỗi:** Tích hợp Error Boundary pixelated trên React để khi có lỗi bất ngờ, giao diện hiển thị chú robot TinTin đang cầm cờ lê sửa chữa, kèm nút "Thử lại bài học" mà không làm mất tiến độ các bài trước.
- **Phán quyết:** **ĐẠT (PASS)**.

---

## 4. Lăng kính 4: Khả năng Refactor & Mở rộng
- **Đánh giá:** Cấu trúc phân tách tầng Domain (`packages/domain`) hoàn toàn độc lập với UI React và Engine Canvas giúp dễ dàng viết Unit Test và có thể chuyển đổi UI framework sau 3–5 năm mà không phải viết lại logic tính điểm hay Leitner.
- **Phán quyết:** **ĐẠT (PASS)**.

---

## 5. Lăng kính 5: Sư phạm & An toàn trẻ em
- **Đánh giá:** 
  1. Không có cơ chế trừ điểm phạt hay âm thanh tiếng chuông báo động gây lo âu cho học sinh tiểu học.
  2. Mỗi câu trả lời sai đều đi kèm thẻ giải thích nguyên nhân hiểu nhầm (`misconception`), biến lỗi sai thành cơ hội học tập.
  3. Không có tính năng chat tự do giữa học sinh nhằm triệt tiêu hoàn toàn nguy cơ bắt nạt trên mạng (cyberbullying).
- **Phán quyết:** **XUẤT SẮC (EXCELLENT)**.

---

## 6. Tổng hợp 5 việc phải chuẩn bị khi code
1. Viết bộ kiểm tra schema tự động cho toàn bộ bài học trong thư mục nội dung.
2. Thiết lập Web Audio Synthesizer với bộ lọc âm tần thấp (low-pass filter) để âm thanh 8-bit ấm áp, không bị chói tai.
3. Đảm bảo toàn bộ thẻ ảnh, canvas đều có thuộc tính CSS `image-rendering: pixelated; image-rendering: crisp-edges`.
4. Viết hàm chuẩn hóa chuỗi tiếng Việt (Unicode NFC) cho các trò chơi gõ phím.
5. Cài đặt cờ lưu trữ an toàn (Safe LocalStorage Wrapper) phòng trường hợp trình duyệt bật chế độ Ẩn danh (Incognito) chặn quyền ghi dữ liệu.
