# -*- coding: utf-8 -*-
"""
Cập nhật PLAN.md và bo-ke-hoach-tich-hop.md cho Cổng cập nhật Gate Protocol U-004:
Nâng cấp Hệ thống Sư phạm Toàn diện: Lí thuyết + Trò chơi + Thực hành (137 bài học Lớp 3–12).
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

# 1. Đọc và cập nhật PLAN.md
with open(plan_path, "r", encoding="utf-8") as f:
    plan_text = f.read()

# Cập nhật thông tin đầu trang
plan_text = re.sub(
    r"> Cập nhật gần nhất: \*\*U-\d+\*\* · Pha hiện tại: [^·]+ · Người duyệt gần nhất: `[^`]+`",
    r"> Cập nhật gần nhất: **U-004** · Pha hiện tại: **Pedagogical Tripartite Flow (Lí thuyết + Game + Thực hành)** · Người duyệt gần nhất: `Tech Lead & User`",
    plan_text
)

# Cập nhật mục 1: Pha hiện tại
plan_text = re.sub(
    r"\| Pha hiện tại \| [^|]+ \|",
    r"| Pha hiện tại | **Pedagogical Tripartite Flow: Lí thuyết + Trò chơi + Thực hành (Hoàn tất 100%)** |",
    plan_text
)

# Cập nhật mục 8: Thay đổi phạm vi
new_scope_row = "| U-004 | Thêm | Tích hợp sâu Lí thuyết & Nhiệm vụ Thực hành phòng Lab vào từng bài | Loại bỏ hoàn toàn sự khô khan, cân bằng kiềng 3 chân: Lí thuyết - Trò chơi - Thực hành | User |"
if "U-004" not in plan_text:
    plan_text = plan_text.replace(
        "| U-003 | Thêm | Mở rộng chi tiết 100% bài học của cả 3 bộ sách (Lớp 3-12) | Đạt độ phủ tuyệt đối 137 bài học tương tác không thiếu bài nào | User |",
        "| U-003 | Thêm | Mở rộng chi tiết 100% bài học của cả 3 bộ sách (Lớp 3-12) | Đạt độ phủ tuyệt đối 137 bài học tương tác không thiếu bài nào | User |\n" + new_scope_row
    )

# Cập nhật mục 9: Số đo thực tế
plan_text = re.sub(
    r"\| Số bài kiểm thử Unit Test\s*\|\s*≥ 5\s*\|\s*\*\*7 / 7 Passed\*\*",
    r"| Số bài kiểm thử Unit Test | ≥ 5 | **8 / 8 Passed**",
    plan_text
)

# Thêm chỉ số sư phạm vào mục 9 nếu chưa có
if "Độ phủ Lí thuyết & Thực hành" not in plan_text:
    plan_text = plan_text.replace(
        "| Tổng số bài học tương tác | ≥ 80 | **137 bài học** | curriculum.json (Lớp 3–12) | U-003 |",
        "| Tổng số bài học tương tác | ≥ 80 | **137 bài học** | curriculum.json (Lớp 3–12) | U-003 |\n| Độ phủ Lí thuyết & Thực hành | 100% | **100% (137/137 bài)** | Đầy đủ Overview, Sections, Ví dụ, Tip, Lab Steps | U-004 |"
    )

# Cập nhật mục 10: Nhật ký cập nhật
new_log_row = "| U-004 | Tích hợp Hệ thống Sư phạm Toàn diện: Lí thuyết + Trò chơi + Thực hành | Thêm cấu trúc `theory` (tổng quan, phân tích, ví dụ đời sống, mẹo nhớ) và `practice` (nhiệm vụ lab từng bước, checklist, thử thách) cho toàn bộ 137 bài học Lớp 3–12; nâng cấp `LessonModal.tsx` 5 bước tương tác; kiểm thử 8/8 pass, build dist thành công | Bàn giao nghiệm thu & đóng gói PWA |"
if "U-004" not in plan_text:
    plan_text = plan_text.replace(
        "| U-003 | Thêm Tất cả Bài học & Nội dung Chi tiết 3 Bộ Sách | Trích xuất và xây dựng ma trận 137 nút học tập phủ 100% bài học của KNTT, Cánh Diều, CTST (Lớp 3–12); cập nhật `01a-extract-*.md`, `01b-curriculum-map.md`, `curriculum.json`; kiểm thử 7/7 pass, build production thành công | Bàn giao nghiệm thu & đóng gói PWA |",
        "| U-003 | Thêm Tất cả Bài học & Nội dung Chi tiết 3 Bộ Sách | Trích xuất và xây dựng ma trận 137 nút học tập phủ 100% bài học của KNTT, Cánh Diều, CTST (Lớp 3–12); cập nhật `01a-extract-*.md`, `01b-curriculum-map.md`, `curriculum.json`; kiểm thử 7/7 pass, build production thành công | Tích hợp Sư phạm: Lí thuyết + Game + Thực hành |\n" + new_log_row
    )

# Căn lề bảng cho PLAN.md
aligned_plan = align_markdown_tables(plan_text)
with open(plan_path, "w", encoding="utf-8") as f:
    f.write(aligned_plan)
print("Đã cập nhật và căn lề thành công PLAN.md!")

# 2. Đọc và cập nhật bo-ke-hoach-tich-hop.md
with open(bkh_path, "r", encoding="utf-8") as f:
    bkh_text = f.read()

# Cập nhật mục 8 trong bo-ke-hoach-tich-hop.md
if "U-004" not in bkh_text:
    bkh_text = bkh_text.replace(
        "| U-003 | Thêm       | Mở rộng chi tiết 100% bài học của cả 3 bộ sách (Lớp 3-12) | Đạt độ phủ tuyệt đối 137 bài học tương tác không thiếu bài nào | User        |",
        "| U-003 | Thêm       | Mở rộng chi tiết 100% bài học của cả 3 bộ sách (Lớp 3-12) | Đạt độ phủ tuyệt đối 137 bài học tương tác không thiếu bài nào | User        |\n"
        "| U-004 | Thêm       | Tích hợp sâu Lí thuyết & Nhiệm vụ Thực hành phòng Lab vào từng bài | Loại bỏ hoàn toàn sự khô khan, cân bằng kiềng 3 chân: Lí thuyết - Trò chơi - Thực hành | User        |"
    )

# Cập nhật mục 9 trong bo-ke-hoach-tich-hop.md
bkh_text = re.sub(
    r"\| Số bài kiểm thử Unit Test\s*\|\s*≥ 5\s*\|\s*\*\*7 / 7 Passed\*\*",
    r"| Số bài kiểm thử Unit Test    | ≥ 5      | **8 / 8 Passed**",
    bkh_text
)

if "Độ phủ Lí thuyết & Thực hành" not in bkh_text:
    bkh_text = bkh_text.replace(
        "| Tổng số bài học tương tác    | ≥ 80     | **137 bài học**          | curriculum.json (Lớp 3–12)              | U-003 |",
        "| Tổng số bài học tương tác    | ≥ 80     | **137 bài học**          | curriculum.json (Lớp 3–12)              | U-003 |\n"
        "| Độ phủ Lí thuyết & Thực hành | 100%     | **100% (137/137 bài)**   | Đầy đủ Overview, Sections, Ví dụ, Tip, Lab Steps | U-004 |"
    )

# Cập nhật mục 10 trong bo-ke-hoach-tich-hop.md
if "U-004" not in bkh_text:
    bkh_text = bkh_text.replace(
        "| U-003 | Thêm Tất cả Bài học & Nội dung Chi tiết 3 Bộ Sách | Trích xuất và xây dựng ma trận 137 nút học tập phủ 100% bài học của KNTT, Cánh Diều, CTST (Lớp 3–12); cập nhật `01a-extract-*.md`, `01b-curriculum-map.md`, `curriculum.json`; kiểm thử 7/7 pass, build production thành công | Bàn giao nghiệm thu & đóng gói PWA                                  |",
        "| U-003 | Thêm Tất cả Bài học & Nội dung Chi tiết 3 Bộ Sách | Trích xuất và xây dựng ma trận 137 nút học tập phủ 100% bài học của KNTT, Cánh Diều, CTST (Lớp 3–12); cập nhật `01a-extract-*.md`, `01b-curriculum-map.md`, `curriculum.json`; kiểm thử 7/7 pass, build production thành công | Tích hợp Sư phạm: Lí thuyết + Game + Thực hành                      |\n"
        "| U-004 | Tích hợp Hệ thống Sư phạm Toàn diện: Lí thuyết + Trò chơi + Thực hành | Thêm cấu trúc `theory` (tổng quan, phân tích, ví dụ đời sống, mẹo nhớ) và `practice` (nhiệm vụ lab từng bước, checklist, thử thách) cho toàn bộ 137 bài học Lớp 3–12; nâng cấp `LessonModal.tsx` 5 bước tương tác; kiểm thử 8/8 pass, build dist thành công | Bàn giao nghiệm thu & đóng gói PWA                                  |"
    )

aligned_bkh = align_markdown_tables(bkh_text)
with open(bkh_path, "w", encoding="utf-8") as f:
    f.write(aligned_bkh)
print("Đã cập nhật và căn lề thành công bo-ke-hoach-tich-hop.md!")
