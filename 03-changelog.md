# 03-changelog.md — Nhật ký tiến hóa kiến trúc EasyTin

## Vòng lặp 4-Agent Changelog

### Architect -> Engineer
- **Đề xuất ban đầu:** Tách riêng server API cho mọi bài học.
- **Engineer phản biện & sửa:** Loại bỏ ràng buộc server bắt buộc cho chế độ học tập. Đưa toàn bộ tính điểm và Leitner sang domain client thuần túy để học sinh vùng sâu vùng xa không có mạng vẫn học trơn tru.

### Engineer -> Reviewer
- **Engineer đề xuất:** Dùng thư viện ngoài Howler.js để phát âm thanh.
- **Reviewer phản biện & sửa:** Thư viện Howler.js tốn 35KB và cần nạp file audio ngoài có nguy cơ lỗi MIME-type trên mạng LAN trường. Thay thế bằng Web Audio API synthesizer tự viết, 0 file mp3, 100% tự sinh chiptune waveforms.

### Reviewer -> Optimizer
- **Reviewer đề xuất:** Dùng canvas kích thước 1920x1080 rồi scale xuống.
- **Optimizer phản biện & sửa:** Quá tốn GPU fillrate trên máy yếu! Chốt độ phân giải logic cố định chuẩn retro 320x180 hoặc 480x270, sử dụng integer scaling (2x, 3x, 4x) để tiết kiệm 80% RAM và vẽ cực nhanh.
