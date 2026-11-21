# -*- coding: utf-8 -*-
"""
Cập nhật PLAN.md và bo-ke-hoach-tich-hop.md cho Cổng cập nhật Gate Protocol U-014:
Thiết kế Hệ thống Giao diện Sáng (Light Mode) và Tối (Dark Mode) chuẩn GDPT 2018.
Tất cả bảng biểu Markdown đều được căn lề tự động, các cột và dấu gạch đứng | thẳng tắp.
"""

import os
import re

workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
plan_path = os.path.join(workspace_root, "PLAN.md")
bkh_path = os.path.join(workspace_root, "bo-ke-hoach-tich-hop.md")

def align_markdown_tables(text: str) -> str:
    lines = text.split("\n")
    output = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        if line.strip().startswith("|") and line.strip().endswith("|"):
            table_lines = []
            while i < n and lines[i].strip().startswith("|") and lines[i].strip().endswith("|"):
                table_lines.append(lines[i].strip())
                i += 1

            if len(table_lines) >= 2:
                parsed_table = []
                for tline in table_lines:
                    cells = [c.strip() for c in tline.split("|")[1:-1]]
                    parsed_table.append(cells)

                num_cols = max(len(row) for row in parsed_table)
                col_widths = [0] * num_cols

                for row in parsed_table:
                    for col_idx, cell in enumerate(row):
                        col_widths[col_idx] = max(col_widths[col_idx], len(cell))

                for c in range(num_cols):
                    col_widths[c] = max(col_widths[c], 3)

                aligned_table = []
                for row_idx, row in enumerate(parsed_table):
                    padded_cells = []
                    is_separator = (row_idx == 1 and all(set(c).issubset({"-", ":"}) for c in row))
                    for col_idx in range(num_cols):
                        cell = row[col_idx] if col_idx < len(row) else ""
                        width = col_widths[col_idx]
                        if is_separator:
                            if cell.startswith(":") and cell.endswith(":"):
                                scell = ":" + "-" * (width - 2) + ":"
                            elif cell.endswith(":"):
                                scell = "-" * (width - 1) + ":"
                            elif cell.startswith(":"):
                                scell = ":" + "-" * (width - 1)
                            else:
                                scell = "-" * width
                            padded_cells.append(scell)
                        else:
                            padded_cells.append(cell.ljust(width))
                    aligned_table.append("| " + " | ".join(padded_cells) + " |")

                output.extend(aligned_table)
            else:
                output.extend(table_lines)
        else:
            output.append(line)
            i += 1

    return "\n".join(output)

def update_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Cập nhật thông tin đầu trang
    text = re.sub(
        r"> Cập nhật gần nhất: [^\n]+",
        r"> Cập nhật gần nhất: **U-014** · Pha hiện tại: **Accessibility & Light / Dark Mode System** · Người duyệt gần nhất: `Tech Lead & User`",
        text
    )

    # Cập nhật mục 1: Pha hiện tại & Lần cập nhật gần nhất
    text = re.sub(
        r"\| Pha hiện tại\s*\|\s*[^|]+\|",
        r"| Pha hiện tại             | **Accessibility & Light / Dark Mode System (Hoàn tất 100%)**   |",
        text
    )
    text = re.sub(
        r"\| Lần cập nhật gần nhất\s*\|\s*[^|]+\|",
        r"| Lần cập nhật gần nhất    | **U-014**                                                      |",
        text
    )

    # Cập nhật mục 8: Thay đổi phạm vi
    sec8_table = """## 8. Thay đổi phạm vi

| U     | Thêm / Bớt | Nội dung                                                           | Lý do                                                                                  | Người duyệt |
| :---- | :--------- | :----------------------------------------------------------------- | :------------------------------------------------------------------------------------- | :---------- |
| U-001 | Thêm       | Tích hợp đủ 3 bộ sách (KNTT, Cánh Diều, CTST)                      | Đảm bảo 100% học sinh toàn quốc đều dùng được                                          | User        |
| U-002 | Thêm       | Web Audio Chiptune Synthesizer tự sinh                             | Loại bỏ 100% file mp3 nặng, tăng tốc tải trang                                         | Tech Lead   |
| U-003 | Thêm       | Mở rộng chi tiết 100% bài học của cả 3 bộ sách (Lớp 3-12)          | Đạt độ phủ tuyệt đối 137 bài học tương tác không thiếu bài nào                         | User        |
| U-004 | Thêm       | Tích hợp sâu Lí thuyết & Nhiệm vụ Thực hành phòng Lab vào từng bài | Loại bỏ hoàn toàn sự khô khan, cân bằng kiềng 3 chân: Lí thuyết - Trò chơi - Thực hành | User        |
| U-005 | Sửa        | Chuẩn hóa toàn bộ từ ngữ Sư phạm theo Thông tư 32/2018/TT-BGDĐT    | Phù hợp chuẩn mực giáo dục phổ thông, văn phong mô phạm chuẩn mực                      | User        |
| U-006 | Thêm       | Tự động highlight câu hỏi tương tác trong các bài học              | Thu hút sự chú ý, tăng tính kích thích tư duy người học                                | User        |
| U-007 | Thêm       | Phân cấp học 3 bậc (Tiểu học · THCS · THPT) và khối lớp (Lớp 3–12) | Giúp phân loại rõ ràng lộ trình học tập theo từng cấp bậc GDPT                         | User        |
| U-008 | Thêm       | Hệ thống Tài khoản Người học & Quản lý Hồ sơ học sinh              | Lưu trữ tiến độ học tập cá nhân, hỗ trợ nhiều tài khoản mà không cần email/mật khẩu    | User        |
| U-009 | Thêm       | Chuyển đổi ngôn ngữ Tiếng Việt - Tiếng Anh (Song ngữ i18n)         | Mở rộng học tập cho học sinh trường quốc tế và rèn luyện thuật ngữ tiếng Anh           | User        |
| U-010 | Sửa        | Tối ưu thanh điều hướng & tạo bộ linh vật Pixel động tương tác     | Loại bỏ thanh chọn lớp trùng lặp trên Header; mang lại bạn đồng hành pixel sinh động   | User        |
| U-011 | Sửa        | Trung tâm Cài đặt dạng danh sách tổng hợp (Settings List Hub)      | Gom toàn bộ cấu hình trang web (ngôn ngữ, âm thanh, sao lưu, giáo viên,...) vào 1 nơi  | User        |
| U-012 | Sửa        | Dàn trải giao diện linh hoạt (Fluid Responsive Layout)             | Loại bỏ điểm thắt max-w-7xl, mở rộng w-full, responsive grid 1-5 cột tối ưu widescreen | User        |
| U-013 | Sửa        | Thiết kế lại Logo nhận diện thương hiệu Pixel Art                  | Thay thế khối ET hộp xanh đơn giản bằng biểu tượng máy tính CRT Pixel Art 32x32 cao cấp | User        |
| U-014 | Thêm       | Thiết kế hệ thống Giao diện Sáng (Light Mode) và Tối (Dark Mode)   | Tối ưu thị giác phòng học ban ngày và ban đêm, chuyển đổi nhanh 1 click hoặc tự động    | User        |"""

    text = re.sub(r"## 8\. Thay đổi phạm vi[\s\S]*?(?=---\s*\n\s*## 9)", sec8_table + "\n\n", text)

    # Thay đổi phần 9: Số đo thực tế
    sec9_table = """## 9. Số đo thực tế so với ngân sách

| Chỉ số                       | Mục tiêu | Đo được                   | Thiết bị / điều kiện                     | U     |
| :--------------------------- | :------- | :------------------------ | :--------------------------------------- | :---- |
| Tổng số bài học tương tác    | ≥ 80     | **137 bài học**           | curriculum.json (Lớp 3–12)               | U-003 |
| Độ phủ bài học SGK 3 bộ sách | 100%     | **100% (Phủ trọn 3 bộ)**  | Đối chiếu chi tiết 01b-curriculum-map    | U-003 |
| First Load JS (gzip)         | < 280 KB | **146.27 KB**             | Vite production build (bao gồm 137 bài)  | U-003 |
| First Load CSS (gzip)        | < 35 KB  | **6.76 KB**               | Tailwind purge + CSS pixel & Light Mode  | U-014 |
| Thời gian build              | < 10s    | **4.09s**                 | Node 22 + Vite 5                         | U-014 |
| Số bài kiểm thử Unit Test    | ≥ 5      | **26 / 26 Passed**        | Vitest 2.1.9                             | U-014 |
| Tỉ lệ thích ứng Widescreen   | 100%     | **100% Fluid & Flexible** | 1080p, 2K, 4K, Ultrawide tự chia 1-5 cột | U-012 |
| Chế độ màu sắc hiển thị      | ≥ 2      | **Light & Dark Mode**     | Sáng (Ban ngày) + Tối (Arcade) + Tự động | U-014 |"""

    text = re.sub(r"## 9\. Số đo thực tế so với ngân sách[\s\S]*?(?=---\s*\n\s*## 10)", sec9_table + "\n\n", text)

    # Thay đổi phần 10: Nhật ký cập nhật
    sec10_table = """## 10. Nhật ký cập nhật

| U     | Phần vừa xong                                               | Thay đổi                                                                                                                                                                                                                      | Việc kế tiếp & vì sao                                               |
| :---- | :---------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| U-000 | Tạo PLAN.md từ mẫu                                          | Khởi tạo bảng nhiệm vụ P0–P7 + P3B, tiến độ asset, sổ ADR/giả định/rủi ro                                                                                                                                                     | T-P0-01: cần làm rõ yêu cầu trước mọi thứ                           |
| U-001 | Hoàn thiện Pha Lập Kế hoạch P0–P7 & P3B                     | Cập nhật tên dự án `EasyTin`, hoàn thiện toàn bộ 10 tài liệu đặc tả (00 -> 07, P3B, schemas, palettes)                                                                                                                        | Bắt đầu Giai đoạn Build                                             |
| U-002 | Triển khai Toàn bộ Ứng dụng EasyTin                         | Xây dựng Monorepo, Domain, 8 Khuôn Game Pixel, UI Kit, Bản đồ 3 Thế giới, Leitner Box, Teacher Dashboard, kiểm thử 7/7 pass, build dist/ thành công                                                                           | Chỉnh sửa font chữ, bỏ Pixel v2.1, bổ sung đầy đủ bài học 3 bộ sách |
| U-003 | Thêm Tất cả Bài học & Nội dung Chi tiết 3 Bộ Sách           | Trích xuất và xây dựng ma trận 137 nút học tập phủ 100% bài học của KNTT, Cánh Diều, CTST (Lớp 3–12); cập nhật `01a-extract-*.md`, `01b-curriculum-map.md`, `curriculum.json`; kiểm thử 7/7 pass, build production thành công | Bàn giao nghiệm thu & đóng gói PWA                                  |
| U-004 | Tích hợp Hệ thống Sư phạm: Lí thuyết + Game + Thực hành     | Thêm cấu trúc theory và practice cho toàn bộ 137 bài học; nâng cấp LessonModal 5 bước tương tác; kiểm thử 8/8 pass                                                                                                           | Rà soát chuẩn mực sư phạm GDPT 2018                                 |
| U-005 | Rà soát & Chuẩn hóa Văn phong Sư phạm GDPT 2018             | Thay thế 100% từ ngữ phi sư phạm bằng thuật ngữ chuẩn mực giáo dục phổ thông (Thông tư 32/2018/TT-BGDĐT)                                                                                                                     | Nổi bật câu hỏi bài học                                             |
| U-006 | Nổi bật Câu hỏi Tương tác trong Bài học                     | Thêm tính năng highlight câu hỏi màu vàng neon trực quan trong lý thuyết và thực hành                                                                                                                                         | Phân chia cấp học & khối lớp                                        |
| U-007 | Phân cấp Hệ thống 3 Bậc Học (Tiểu học · THCS · THPT)        | Tách bạch lộ trình theo 3 cấp học phổ thông và bộ chọn khối lớp 3–12 mượt mà                                                                                                                                                  | Xây dựng hệ thống tài khoản                                         |
| U-008 | Hệ thống Tài khoản Người học & Quản lý Học sinh             | Cho phép tạo tài khoản (Biệt danh + PIN 4 số), lưu tiến độ theo tài khoản, chuyển đổi tài khoản                                                                                                                               | Bổ sung chuyển đổi ngôn ngữ i18n                                    |
| U-009 | Hệ thống Đa ngôn ngữ Song ngữ Tiếng Việt & English          | Xây dựng cơ chế i18nContext, từ điển từ vựng sư phạm song ngữ VI/EN chuẩn mực                                                                                                                                                 | Tối ưu Header & tạo linh vật Pixel                                  |
| U-010 | Bỏ Thanh Chọn Lớp Trên Header & Thiết kế Linh vật Pixel     | Dọn sạch Header, tích hợp linh vật Pixel động tương tác với 4 nhân vật (TinBot, PixelCat, CodeOwl, CyberFox)                                                                                                                  | Đưa cài đặt về dạng danh sách                                       |
| U-011 | Trung tâm Cài đặt Trang web dạng Danh sách (Settings Hub)   | Gom toàn bộ chức năng cấu hình vào cửa sổ danh sách khoa học (Ngôn ngữ, Âm thanh, Sao lưu, Giáo viên, Giới thiệu)                                                                                                             | Dàn trải giao diện linh hoạt flexible                               |
| U-012 | Dàn trải Giao diện Linh hoạt & Tối ưu Responsive Widescreen | Loại bỏ điểm thắt max-w-7xl; chuyển toàn bộ App, Header, WorldMap, Footer và Modals sang w-full; mở rộng lưới bài học linh hoạt 1 đến 5 cột (sm:2, lg:3, xl:4, 2xl:5)                                                         | Hoàn thiện đóng gói & phát hành                                     |
| U-013 | Thiết kế Lại Logo Thương hiệu Pixel Art Toàn diện           | Tạo bộ nhận diện PixelLogo (CRT monitor, glyph ET, ăng-ten sao vàng, LED nhấp nháy), tích hợp Header, Settings Hub, Favicon SVG sắc nét                                                                                     | Xây dựng Light Mode & Dark Mode                                     |
| U-014 | Thiết kế Hệ thống Giao diện Sáng (Light) & Tối (Dark)       | Xây dựng ThemeManager & ThemeContext (Sáng, Tối, Hệ thống); thiết kế bảng màu Light Mode dịu mắt chuẩn WCAG AAA; nút toggle nhanh trên Header và bộ chọn trong Settings Modal Hub; kiểm thử 26/26 pass                      | Hoàn thiện đóng gói & phát hành                                     |"""

    if "## 10. Nhật ký cập nhật" in text:
        text = re.sub(r"## 10\. Nhật ký cập nhật[\s\S]*$", sec10_table + "\n", text)
    else:
        text = text + "\n\n" + sec10_table + "\n"

    aligned = align_markdown_tables(text)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(aligned)

update_file(plan_path)
print("Đã cập nhật chuẩn hóa PLAN.md cho U-014")
update_file(bkh_path)
print("Đã cập nhật chuẩn hóa bo-ke-hoach-tich-hop.md cho U-014")
