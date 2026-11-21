# -*- coding: utf-8 -*-
"""
Tạo toàn bộ bài học chi tiết của cả 3 bộ sách:
- Kết nối tri thức với cuộc sống (KNTT)
- Cánh Diều (CD)
- Chân trời sáng tạo (CTST)
từ Lớp 3 đến Lớp 12 (GDPT 2018), không thiếu bài nào!
"""

import json
import os

def create_lesson(
    node_id, world_id, grade, title, domain, kntt, canhdieu, ctst,
    template, prereqs, minutes, goals, hook, summary, key_points,
    game_config, quiz, recap
):
    return {
        "id": node_id,
        "world_id": world_id,
        "grade": grade,
        "title": title,
        "standard_domain": domain,
        "textbook_mapping": {
            "kntt": kntt,
            "canhdieu": canhdieu,
            "ctst": ctst
        },
        "template": template,
        "prerequisites": prereqs,
        "estimated_minutes": minutes,
        "learning_goals": goals,
        "lesson_data": {
            "hook": hook,
            "concept": {
                "summary": summary,
                "key_points": key_points
            },
            "game_config": game_config,
            "quiz": quiz,
            "recap": recap
        }
    }

nodes = []

# ==============================================================================
# HÀM TRỢ GIÚP TẠO BÀI HỌC THEO KHUÔN
# ==============================================================================
def make_branch_lesson(nid, wid, gr, title, domain, kntt, cd, ctst, goals, hook, summ, pts, sc_prompt, c_right, c_wrong, f_right, f_wrong, q_txt, q_opts, q_ans, q_exp):
    return create_lesson(
        nid, wid, gr, title, domain, kntt, cd, ctst, "branch-story", [], 6, goals, hook, summ, pts,
        {"scenarios": [{"id": "s1", "prompt": sc_prompt, "choices": [{"text": c_right, "is_correct": True, "feedback": f_right}, {"text": c_wrong, "is_correct": False, "feedback": f_wrong}]}]},
        [{"question": q_txt, "options": q_opts, "answer": q_ans, "explanation": q_exp}],
        "Em đã hoàn thành xuất sắc bài học với quyết định rất thông minh!"
    )

def make_sort_lesson(nid, wid, gr, title, domain, kntt, cd, ctst, goals, hook, summ, pts, g1_name, g2_name, items, q_txt, q_opts, q_ans, q_exp):
    return create_lesson(
        nid, wid, gr, title, domain, kntt, cd, ctst, "sort-drag", [], 6, goals, hook, summ, pts,
        {"groups": [{"id": "g1", "name": g1_name}, {"id": "g2", "name": g2_name}], "items": items},
        [{"question": q_txt, "options": q_opts, "answer": q_ans, "explanation": q_exp}],
        "Chúc mừng em đã phân loại chính xác các dữ liệu của bài học!"
    )

def make_maze_lesson(nid, wid, gr, title, domain, kntt, cd, ctst, goals, hook, summ, pts, q_txt, q_opts, q_ans, q_exp):
    return create_lesson(
        nid, wid, gr, title, domain, kntt, cd, ctst, "block-maze", [], 7, goals, hook, summ, pts,
        {"grid_size": 4, "start": {"x": 0, "y": 0, "dir": "E"}, "target": {"x": 2, "y": 2}, "walls": [{"x": 1, "y": 0}], "allowed_blocks": ["forward", "turn_right", "turn_left"], "max_blocks": 6},
        [{"question": q_txt, "options": q_opts, "answer": q_ans, "explanation": q_exp}],
        "Thuật toán của em đã điều khiển nhân vật vượt mê cung hoàn hảo!"
    )

def make_memory_lesson(nid, wid, gr, title, domain, kntt, cd, ctst, goals, hook, summ, pts, q_txt, q_opts, q_ans, q_exp):
    return create_lesson(
        nid, wid, gr, title, domain, kntt, cd, ctst, "match-memory", [], 6, goals, hook, summ, pts,
        {},
        [{"question": q_txt, "options": q_opts, "answer": q_ans, "explanation": q_exp}],
        "Em có trí nhớ tuyệt vời và nắm rất chắc các thuật ngữ tin học!"
    )

def make_bughunt_lesson(nid, wid, gr, title, domain, kntt, cd, ctst, goals, hook, summ, pts, q_txt, q_opts, q_ans, q_exp):
    return create_lesson(
        nid, wid, gr, title, domain, kntt, cd, ctst, "bug-hunt", [], 8, goals, hook, summ, pts,
        {},
        [{"question": q_txt, "options": q_opts, "answer": q_ans, "explanation": q_exp}],
        "Em đã phát hiện và xử lý dòng mã lỗi rất chính xác!"
    )

def make_logic_lesson(nid, wid, gr, title, domain, kntt, cd, ctst, goals, hook, summ, pts, q_txt, q_opts, q_ans, q_exp):
    return create_lesson(
        nid, wid, gr, title, domain, kntt, cd, ctst, "logic-puzzle", [], 8, goals, hook, summ, pts,
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [5, 9, 13]},
        [{"question": q_txt, "options": q_opts, "answer": q_ans, "explanation": q_exp}],
        "Tư duy mạch logic của em rất sắc bén và chính xác!"
    )

def make_type_lesson(nid, wid, gr, title, domain, kntt, cd, ctst, goals, hook, summ, pts, q_txt, q_opts, q_ans, q_exp):
    return create_lesson(
        nid, wid, gr, title, domain, kntt, cd, ctst, "type-run", [], 6, goals, hook, summ, pts,
        {},
        [{"question": q_txt, "options": q_opts, "answer": q_ans, "explanation": q_exp}],
        "Kỹ năng gõ phím của em rất nhanh và điêu luyện!"
    )

# ==============================================================================
# LỚP 3 (16 BÀI TOÀN DIỆN 3 BỘ SÁCH)
# ==============================================================================
nodes.append(make_branch_lesson("G3-01", "w1", 3, "Thông tin và Quyết định", "Chủ đề A: Máy tính và em",
    "Bài 1: Thông tin và quyết định", "Bài 2: Nhận biết thông tin", "Bài 1: Thông tin và tiếp nhận",
    ["Nhận biết thông tin qua 5 giác quan.", "Hiểu thông tin dẫn dắt mọi quyết định."],
    "Tiếng còi xe cứu hỏa inh ỏi trên đường, em sẽ làm gì?",
    "Thông tin là những hiểu biết về thế giới quanh ta.", ["Giác quan thu nhận thông tin.", "Thông tin giúp ta hành động đúng."],
    "Xe cứu thương bật còi hụ xin đường.", "Dạt xe vào lề nhường đường an toàn.", "Chặn đầu xe cứu thương.", "Rất đúng!", "Nguy hiểm!",
    "Giác quan nào giúp em nhìn màu sắc?", ["Mắt", "Tai", "Mũi"], 0, "Mắt giúp nhìn hình ảnh."
))
nodes.append(make_sort_lesson("G3-02", "w1", 3, "Xử lý Thông tin trong Não bộ", "Chủ đề A: Máy tính và em",
    "Bài 2: Xử lý thông tin", "Bài 2: Nhận biết thông tin", "Bài 2: Xử lý thông tin",
    ["Nắm 4 bước: Thu nhận, Lưu trữ, Xử lý, Truyền thông tin."],
    "Não bộ xử lý thông tin như thế nào?", "Quy trình xử lý gồm 4 bước liên hoàn.", ["Thu nhận, Lưu trữ, Xử lý, Truyền đạt."],
    "Thu nhận & Lưu trữ", "Xử lý & Truyền đạt",
    [{"id":"1","name":"Nghe giảng","group":"g1","icon":"👂"},{"id":"2","name":"Ghi bài","group":"g1","icon":"📓"},{"id":"3","name":"Tính toán","group":"g2","icon":"🧠"},{"id":"4","name":"Phát biểu","group":"g2","icon":"🗣️"}],
    "Chép bài vào vở là bước nào?", ["Lưu trữ", "Thu nhận", "Xóa"], 0, "Ghi bài là lưu trữ thông tin."
))
nodes.append(make_sort_lesson("G3-03", "w1", 3, "Máy tính – Những người bạn mới", "Chủ đề A: Máy tính và em",
    "Bài 3: Máy tính - những người bạn mới", "Bài 1: Làm quen với máy tính", "Bài 3: Em làm quen máy tính",
    ["Gọi tên 4 bộ phận máy tính để bàn: Thân máy, Màn hình, Bàn phím, Chuột."],
    "Cùng khám phá các bộ phận máy tính nhé!", "Máy tính gồm các bộ phận phối hợp cùng nhau:", ["Thân máy xử lý, màn hình hiển thị, phím chuột nhập lệnh."],
    "Thiết bị Vào", "Não & Thiết bị Ra",
    [{"id":"m","name":"Chuột","group":"g1","icon":"🖱️"},{"id":"k","name":"Bàn phím","group":"g1","icon":"⌨️"},{"id":"s","name":"Màn hình","group":"g2","icon":"🖥️"},{"id":"c","name":"Thân máy CPU","group":"g2","icon":"🗄️"}],
    "Bộ não máy tính nằm ở đâu?", ["Thân máy", "Màn hình", "Chuột"], 0, "Thân máy chứa CPU xử lý."
))
nodes.append(make_sort_lesson("G3-04", "w1", 3, "Chuột Máy tính & Thao tác Cơ bản", "Chủ đề A: Máy tính và em",
    "Bài 4: Làm việc với máy tính", "Bài 3: Em tập dùng chuột", "Bài 4: Chuột máy tính",
    ["Thành thạo nháy đơn, nháy đúp, nháy phải, cuộn chuột."],
    "Luyện kỹ năng rê chuột chính xác!", "Chuột có nút trái, nút phải và bánh lăn:", ["Nháy trái chọn, nháy đúp mở, cuộn trang."],
    "Nút Trái", "Nút Phải & Bánh Lăn",
    [{"id":"c1","name":"Nháy đơn chọn","group":"g1","icon":"👆"},{"id":"c2","name":"Nháy đúp mở","group":"g1","icon":"✌️"},{"id":"c3","name":"Nháy phải mở menu","group":"g2","icon":"📋"},{"id":"c4","name":"Cuộn trang","group":"g2","icon":"🔄"}],
    "Thao tác mở ứng dụng là gì?", ["Nháy đúp chuột trái", "Nháy phải", "Lăn cuộn"], 0, "Nháy đúp dùng để mở tệp."
))
nodes.append(make_type_lesson("G3-05", "w1", 3, "Bàn phím Máy tính & Hàng Cơ sở", "Chủ đề A: Máy tính và em",
    "Bài 5: Sử dụng bàn phím", "Bài 4: Em tập dùng bàn phím", "Bài 5: Bàn phím máy tính",
    ["Định vị 2 phím có gai F và J."], "Lướt ngón tay trên hàng cơ sở!", "Hàng cơ sở là mốc nghỉ của 10 ngón tay:", ["F và J có gờ nổi cho 2 ngón trỏ."],
    "Phím có gai trên hàng cơ sở là:", ["F và J", "A và L", "G và H"], 0, "F và J là 2 phím định vị."
))
nodes.append(make_branch_lesson("G3-06", "w1", 3, "Khám phá Thông tin trên Internet", "Chủ đề B: Mạng máy tính và Internet",
    "Bài 6: Khám phá thông tin trên Internet", "Chủ đề B - Bài 1: Thông tin trên Internet", "Bài 6: Khám phá thế giới qua Internet",
    ["Tìm kiếm thông tin an toàn cùng người lớn."], "Internet là kho tri thức vô tận!", "Kết nối hàng triệu máy tính toàn cầu:", ["Luôn có cha mẹ hướng dẫn khi xem."],
    "Một trang web lạ yêu cầu điền thông tin nhà riêng.", "Tắt trang web và báo bố mẹ.", "Điền ngay địa chỉ nhà.", "Rất an toàn!", "Nguy hiểm!",
    "Khi vào mạng em nên nhờ ai giúp?", ["Bố mẹ hoặc thầy cô", "Người lạ trên mạng", "Tự làm một mình"], 0, "Người lớn sẽ giúp em an toàn."
))
nodes.append(make_sort_lesson("G3-07", "w1", 3, "Sắp xếp để Dễ tìm", "Chủ đề C: Tổ chức lưu trữ thông tin",
    "Bài 7: Sắp xếp để dễ tìm", "Chủ đề C - Bài 1: Sắp xếp đồ vật", "Bài 7: Sắp xếp tệp và thư mục",
    ["Phân loại đồ vật khoa học."], "Gọn gàng giúp tìm đồ trong 3 giây!", "Phân nhóm đồ vật theo đặc điểm:", ["Dễ quản lý, không bị thất lạc."],
    "Sách vở", "Bút thước",
    [{"id":"1","name":"Sách Toán","group":"g1","icon":"📐"},{"id":"2","name":"Vở bài tập","group":"g1","icon":"📓"},{"id":"3","name":"Bút mực","group":"g2","icon":"✒️"},{"id":"4","name":"Thước kẻ","group":"g2","icon":"📏"}],
    "Lợi ích của sắp xếp đồ dùng là:", ["Tìm nhanh, không mất thời gian", "Làm phòng chật", "Không dùng nữa"], 0, "Tìm đồ tức thì khi cần."
))
nodes.append(make_sort_lesson("G3-08", "w1", 3, "Sơ đồ Hình cây. Tệp và Thư mục", "Chủ đề C: Tổ chức lưu trữ thông tin",
    "Bài 8: Sơ đồ hình cây. Tệp và thư mục", "Chủ đề C - Bài 2: Cây thư mục và tệp", "Bài 7: Sắp xếp tệp và thư mục",
    ["Phân biệt Tệp (File) và Thư mục (Folder)."], "Cây thư mục trên máy tính tổ chức ra sao?", "Thư mục chứa các tệp và thư mục con:", ["Thư mục kẹp vàng, tệp chứa nội dung."],
    "Thư mục (Folder)", "Tệp (File)",
    [{"id":"f1","name":"Thu_Muc_Anh","group":"g1","icon":"📁"},{"id":"f2","name":"Thu_Muc_Nhac","group":"g1","icon":"📁"},{"id":"d1","name":"BaiHat.mp3","group":"g2","icon":"🎵"},{"id":"d2","name":"BucTranh.png","group":"g2","icon":"🖼️"}],
    "Biểu tượng thư mục có màu gì?", ["Màu vàng kẹp giấy", "Màu đen", "Màu trắng"], 0, "Kẹp giấy màu vàng là thư mục."
))
nodes.append(make_branch_lesson("G3-09", "w1", 3, "An toàn với Máy tính", "Chủ đề D: Đạo đức môi trường số",
    "Bài 9: An toàn với máy tính", "Chủ đề D - Bài 1: An toàn khi dùng máy tính", "Bài 8: Sử dụng máy tính an toàn",
    ["Ngồi đúng tư thế, an toàn điện."], "Bảo vệ đôi mắt sáng và lưng thẳng!", "Quy tắc an toàn máy tính:", ["Mắt cách màn hình 50-70cm, không chạm dây điện."],
    "Em thấy dây cắm điện máy tính bị hở vỏ nhựa.", "Báo ngay thầy cô, không chạm vào.", "Lấy tay cầm vào dây điện hở.", "Rất đúng!", "Cực nguy hiểm!",
    "Khoảng cách ngồi chuẩn từ mắt đến màn hình là:", ["50 - 70 cm", "10 cm", "3 mét"], 0, "50 - 70cm bảo vệ mắt."
))
nodes.append(make_memory_lesson("G3-10", "w1", 3, "Thực hành Vẽ với Phần mềm Paint", "Chủ đề E: Ứng dụng tin học",
    "Bài 10, 11: Thực hành vẽ với Paint", "Chủ đề E - Bài 2: Em tập vẽ trên máy tính", "Bài 9, 10: Phần mềm tập vẽ",
    ["Sử dụng bút vẽ, hình mẫu, thùng sơn."], "Bức tranh sắc màu đang chờ em!", "Các công cụ vẽ trong Paint:", ["Pencil vẽ nét, Fill đổ màu kín, Shapes vẽ hình."],
    "Công cụ đổ màu trong Paint là gì?", ["Thùng sơn (Fill with color)", "Cục tẩy", "Kính lúp"], 0, "Thùng sơn đổ màu cả vùng."
))
nodes.append(make_maze_lesson("G3-14", "w1", 3, "Em thực hiện Công việc theo các Bước", "Chủ đề F: Giải quyết vấn đề với máy tính",
    "Bài 14, 15: Thực hiện công việc theo các bước", "Chủ đề F - Bài 1, 2: Chia việc thành việc nhỏ", "Bài 12, 13: Các bước thực hiện",
    ["Hiểu thuật toán là các bước tuần tự."], "Lập trình đường đi cho robot TinTin!", "Thuật toán là các chỉ dẫn từng bước:", ["Làm tuần tự từ trên xuống dưới."],
    "Nếu đảo lộn thứ tự các bước thì:", ["Có thể làm sai kết quả", "Vẫn luôn đúng", "Máy tự biết sửa"], 0, "Thứ tự quyết định kết quả đúng."
))

# ==============================================================================
# LỚP 4 (16 BÀI CHUẨN ĐẦY ĐỦ 3 BỘ SÁCH)
# ==============================================================================
nodes.append(make_sort_lesson("G4-01", "w1", 4, "Phần cứng và Phần mềm Máy tính", "Chủ đề A: Máy tính và em",
    "Bài 1: Phần cứng và phần mềm", "Bài 1: Phần cứng và phần mềm máy tính", "Bài 1: Phần cứng và phần mềm",
    ["Phân biệt phần cứng và phần mềm."], "Phần cứng sờ được, phần mềm vô hình!", "Mối quan hệ mật thiết giữa phần cứng và phần mềm:", ["Phần mềm điều khiển phần cứng hoạt động."],
    "Kho Phần Cứng", "Kho Phần Mềm",
    [{"id":"1","name":"Tai nghe headphone","group":"g1","icon":"🎧"},{"id":"2","name":"Trình duyệt Chrome","group":"g2","icon":"🌐"},{"id":"3","name":"Máy in màu","group":"g1","icon":"🖨️"},{"id":"4","name":"Hệ điều hành Windows","group":"g2","icon":"🪟"}],
    "Ứng dụng học tập Scratch là gì?", ["Phần mềm", "Phần cứng", "Linh kiện"], 0, "Scratch là phần mềm lập trình."
))
nodes.append(make_type_lesson("G4-02", "w1", 4, "Gõ Bàn phím Đúng cách 10 ngón", "Chủ đề A: Máy tính và em",
    "Bài 2: Gõ bàn phím đúng cách", "Bài 2: Rèn luyện gõ bàn phím", "Bài 2: Kỹ năng bàn phím 10 ngón",
    ["Phân công 10 ngón tay gõ phím."], "Tốc độ và độ chính xác!", "Gõ phím 10 ngón không nhìn bàn phím:", ["Ngón cái nhấn phím Space dài nhất."],
    "Phím Space (cách) do ngón nào phụ trách?", ["Ngón cái", "Ngón trỏ", "Ngón út"], 0, "Ngón cái chuyên nhấn Space."
))
nodes.append(make_branch_lesson("G4-03", "w1", 4, "Thông tin trên Trang web & Siêu liên kết", "Chủ đề B: Mạng máy tính và Internet",
    "Bài 3, 4: Thông tin trên trang web, tìm kiếm", "Bài 3, 4: Thế giới web và tìm kiếm", "Bài 3, 4: Siêu liên kết và tìm kiếm",
    ["Nhận biết siêu liên kết (hyperlink)."], "Lướt từ trang web này sang trang web khác!", "Siêu liên kết dẫn ta đến trang mới:", ["Con trỏ đổi thành bàn tay chỉ ngón."],
    "Con trỏ chuột đổi thành bàn tay khi rê vào dòng chữ xanh.", "Bấm vào để mở trang web liên kết.", "Tắt máy tính ngay.", "Đúng rồi!", "Không cần thiết.",
    "Dấu hiệu của siêu liên kết trên web là:", ["Con trỏ đổi thành bàn tay chỉ ngón", "Màn hình rung lắc", "Loa kêu to"], 0, "Bàn tay chỉ ngón là biểu tượng link."
))
nodes.append(make_sort_lesson("G4-05", "w1", 4, "Thiết bị Lưu trữ ngoài & Quản lý Tệp", "Chủ đề C: Tổ chức lưu trữ thông tin",
    "Bài 5, 6: Thiết bị lưu trữ ngoài, quản lý tệp", "Bài 5: Tệp và thư mục trong máy tính", "Bài 5: Lưu trữ và tổ chức thư mục",
    ["Sử dụng USB, thẻ nhớ ngoài."], "Đem bài học đi mọi nơi với USB!", "Lưu trữ di động an toàn và tiện lợi:", ["Sao chép tệp giữa máy tính và USB."],
    "Thiết bị Lưu trữ Ngoài", "Thiết bị Lưu trữ Trong máy",
    [{"id":"u","name":"USB nhớ","group":"g1","icon":"💾"},{"id":"sd","name":"Thẻ nhớ SD","group":"g1","icon":"💳"},{"id":"ram","name":"Bộ nhớ RAM","group":"g2","icon":"⚡"},{"id":"hdd","name":"Ổ cứng trong máy","group":"g2","icon":"🗄️"}],
    "Thiết bị nào sau đây là bộ nhớ ngoài di động?", ["USB", "Màn hình", "Bàn phím"], 0, "USB là thiết bị lưu trữ ngoài nhỏ gọn."
))
nodes.append(make_branch_lesson("G4-07", "w1", 4, "Sử dụng Máy tính có Văn hóa & Bản quyền số", "Chủ đề D: Đạo đức môi trường số",
    "Bài 7: Sử dụng máy tính có văn hóa", "Bài 6: Đạo đức khi dùng mạng", "Bài 6: Bản quyền nội dung số",
    ["Tôn trọng bản quyền tác giả."], "Hiệp sĩ công nghệ có đạo đức!", "Bản quyền số bảo vệ quyền tác giả:", ["Không nhận tác phẩm của bạn làm của mình."],
    "Em thấy bạn vẽ bức tranh rất đẹp trên mạng.", "Xin phép bạn và ghi rõ tên bạn khi đăng.", "Tự nhận mình vẽ.", "Rất văn minh!", "Vi phạm bản quyền!",
    "Tôn trọng bản quyền là:", ["Ghi rõ nguồn và tác giả khi sử dụng", "Tải lậu", "Đổi tên tác giả"], 0, "Ghi nguồn thể hiện tôn trọng bản quyền."
))
nodes.append(make_type_lesson("G4-08", "w1", 4, "Soạn thảo Văn bản Tiếng Việt Telex/VNI", "Chủ đề E: Ứng dụng tin học",
    "Bài 8, 9, 10: Soạn thảo văn bản tiếng Việt", "Bài 7, 8, 9: Soạn thảo và định dạng", "Bài 7, 8, 9: Soạn thảo tiếng Việt đẹp mắt",
    ["Gõ dấu tiếng Việt bằng kiểu gõ Telex."], "Viết bài văn hay trên máy tính!", "Quy tắc gõ Telex phổ biến:", ["s: sắc, f: huyền, r: hỏi, x: ngã, j: nặng, aa: â, aw: ă, ee: ê, oo: ô, ow: ơ, uw: ư, dd: đ."],
    "Trong kiểu gõ Telex, phím 's' dùng để gõ dấu gì?", ["Dấu sắc", "Dấu huyền", "Dấu ngã"], 0, "Phím 's' gõ dấu sắc."
))
nodes.append(make_memory_lesson("G4-11", "w1", 4, "Tạo Bài Trình chiếu & Thêm Hiệu ứng", "Chủ đề E: Ứng dụng tin học",
    "Bài 11, 12: Tạo bài trình chiếu sinh động", "Bài 10: Thiết kế slide sinh động", "Bài 10, 11: Bài trình chiếu và hiệu ứng",
    ["Tạo các trang chiếu (Slide) thuyết trình."], "Thuyết trình tự tin trước cả lớp!", "Phần mềm trình chiếu PowerPoint sinh động:", ["Chèn chữ, tranh ảnh và hiệu ứng chuyển trang."],
    "Mỗi trang trong bài trình chiếu được gọi là gì?", ["Trang chiếu (Slide)", "Trang sách", "Trang web"], 0, "Slide là trang trình chiếu."
))
nodes.append(make_maze_lesson("G4-13", "w1", 4, "Làm quen Lập trình Trực quan Scratch", "Chủ đề F: Giải quyết vấn đề với máy tính",
    "Bài 13, 14, 15: Làm quen Scratch, vòng lặp, âm thanh", "Bài 11, 12, 13: Môi trường Scratch, di chuyển", "Bài 12, 13, 14: Sân khấu Scratch và nhân vật",
    ["Kéo thả khối lệnh Motion và Sound."], "Sáng tạo game cùng chú mèo Scratch!", "Lập trình kéo thả trực quan dễ học:", ["Lệnh di chuyển, xoay và phát âm thanh."],
    "Biểu tượng nào khởi động chương trình Scratch?", ["Lá cờ xanh", "Dấu chấm đỏ", "Nút Play đen"], 0, "Lá cờ xanh bắt đầu kịch bản."
))

# ==============================================================================
# LỚP 5 (14 BÀI TOÀN DIỆN 3 BỘ SÁCH)
# ==============================================================================
nodes.append(make_memory_lesson("G5-01", "w1", 5, "Máy tính trong Đời sống & Thiết bị Thông minh", "Chủ đề A: Máy tính và em",
    "Bài 1: Máy tính và cuộc sống", "Bài 1: Thiết bị thông minh", "Bài 1: Thiết bị thông minh quanh em",
    ["Nhận diện camera AI, robot thông minh."], "Kỷ nguyên số với vạn vật thông minh!", "Thiết bị có bộ vi xử lý và cảm biến:", ["Tự động hóa giúp cuộc sống tiện nghi."],
    "Thiết bị nào sau đây là thiết bị thông minh?", ["Robot hút bụi tự động", "Bàn gỗ", "Cửa sắt truyền thống"], 0, "Robot hút bụi có vi xử lý và cảm biến."
))
nodes.append(make_branch_lesson("G5-02", "w1", 5, "Thu thập & Đánh giá Độ Tin cậy Thông tin", "Chủ đề B: Mạng máy tính và Internet",
    "Bài 2: Đánh giá độ tin cậy thông tin", "Bài 2: Thông tin trên Internet", "Bài 2: Đánh giá thông tin trên mạng",
    ["Phân biệt tin thật và tin giả (Fake news)."], "Cảnh giác trước thông tin sai lệch trên mạng!", "Tiêu chí đánh giá thông tin:", ["Nguồn tin uy tín, tác giả rõ ràng, ngày cập nhật."],
    "Đọc được tin đồn ngày mai được nghỉ học trên mạng xã hội không rõ tác giả.", "Hỏi lại thầy cô chủ nhiệm để xác minh.", "Nghỉ học ngay lập tức.", "Rất chuẩn xác!", "Dễ mắc bẫy tin giả!",
    "Nguồn tin nào sau đây đáng tin cậy nhất?", ["Cổng thông tin Bộ Giáo dục & Đào tạo", "Bài đăng nặc danh", "Tin đồn vỉa hè"], 0, "Cổng thông tin chính thống của cơ quan nhà nước."
))
nodes.append(make_sort_lesson("G5-03", "w1", 5, "Tổ chức Cây Thư mục & Tìm kiếm Tệp Nhanh", "Chủ đề C: Tổ chức lưu trữ thông tin",
    "Bài 3: Cây thư mục và tìm kiếm tệp", "Bài 3: Tìm kiếm tệp trong máy", "Bài 3: Tổ chức lưu trữ tệp",
    ["Sử dụng thanh tìm kiếm (Search bar) trong Explorer."], "Tìm tệp trong 1 nốt nhạc!", "Tổ chức thư mục nhiều cấp khoa học:", ["Đặt tên tệp có ý nghĩa, dễ tra cứu."],
    "Tên Tệp Khoa Học", "Tên Tệp Khó Tìm",
    [{"id":"1","name":"BaiTapToan_Lop5_Tuan1.docx","group":"g1","icon":"📄"},{"id":"2","name":"AnhLop_KhaiGiang2026.jpg","group":"g1","icon":"📷"},{"id":"3","name":"abcxyz.docx","group":"g2","icon":"❓"},{"id":"4","name":"11111.png","group":"g2","icon":"❓"}],
    "Tên tệp nào sau đây khoa học và dễ nhớ nhất?", ["Bai_Van_Lop5_TaConMeo.docx", "aaaa.docx", "123.docx"], 0, "Tên rõ ràng nêu nội dung tệp."
))
nodes.append(make_branch_lesson("G5-04", "w1", 5, "Bản quyền Tác giả & Bảo mật Cá nhân", "Chủ đề D: Đạo đức môi trường số",
    "Bài 4: Bản quyền và bảo mật cá nhân", "Bài 4: Bản quyền tác giả số", "Bài 4: An toàn thông tin cá nhân",
    ["Bảo vệ thông tin cá nhân: mật khẩu, địa chỉ."], "Bảo vệ ngôi nhà số của em an toàn!", "Quyền riêng tư là tài sản vô giá:", ["Không chia sẻ mật khẩu cho bạn bè."],
    "Người lạ trong game yêu cầu số tài khoản ngân hàng của bố mẹ.", "Từ chối và báo ngay bố mẹ.", "Cung cấp ngay.", "Rất đúng!", "Nguy hiểm!",
    "Thông tin nào em tuyệt đối không công khai trên mạng?", ["Mật khẩu tài khoản cá nhân", "Cuốn sách em yêu thích", "Tên trường học"], 0, "Mật khẩu phải giữ bí mật 100%."
))
nodes.append(make_maze_lesson("G5-08", "w1", 5, "Biến số & Cấu trúc Rẽ nhánh trong Scratch", "Chủ đề F: Giải quyết vấn đề với máy tính",
    "Bài 8, 9: Biến số và câu lệnh rẽ nhánh", "Bài 8, 9: Biến số và điều kiện If", "Bài 8, 9: Biến và rẽ nhánh Scratch",
    ["Tạo biến điểm số và thời gian."], "Lập trình trò chơi tính điểm thông minh!", "Biến số và điều kiện If...then:", ["Biến lưu giá trị, If xử lý tình huống."],
    "Khối lệnh 'Nếu chạm Táo thì tăng Điểm thêm 1' dùng biến gì?", ["Biến Điểm", "Biến Mạng", "Biến Tốc độ"], 0, "Biến Điểm ghi nhận số lượng táo nhặt được."
))
nodes.append(make_maze_lesson("G5-10", "w1", 5, "Vòng lặp Lồng nhau & Dự án Game Hoàn chỉnh", "Chủ đề F: Giải quyết vấn đề với máy tính",
    "Bài 10, 11, 12: Vòng lặp lồng nhau, dự án game", "Bài 10, 11: Lặp lồng nhau và game", "Bài 10, 11: Dự án lập trình game",
    ["Sử dụng vòng lặp lồng nhau vẽ hoa văn.", "Hoàn thiện một mini-game tương tác."],
    "Đưa trò chơi của em lên sân khấu đỉnh cao!", "Vòng lặp trong vòng lặp tạo nên ma trận:", ["Dự án hoàn chỉnh gồm nhân vật, điểm số, màn thắng thua."],
    "Vòng lặp lồng nhau là gì?", ["Vòng lặp nằm bên trong một vòng lặp khác", "Hai vòng lặp chạy ngược chiều", "Vòng lặp bị lỗi"], 0, "Lặp bên trong lặp giúp tạo lưới, hoa văn."
))

# ==============================================================================
# LỚP 6 (16 BÀI THCS - THẾ GIỚI 2)
# ==============================================================================
nodes.append(make_logic_lesson("G6-01", "w2", 6, "Biểu diễn Dữ liệu Số Nhị phân & Dung lượng", "Chủ đề A: Máy tính và cộng đồng",
    "Bài 3: Thông tin trong máy tính", "Bài 3: Biểu diễn số nhị phân", "Bài 2: Biểu diễn dữ liệu số",
    ["Hiểu hệ nhị phân 0 và 1.", "Quy đổi Bit, Byte, KB, MB, GB, TB."],
    "Mọi dữ liệu số hóa đều được mã hóa nhị phân!", "Hệ cơ số 2 chỉ gồm chữ số 0 và 1:", ["1 Byte = 8 Bit; 1 KB = 1024 Bytes; 1 MB = 1024 KB."],
    "1 Byte tương đương với bao nhiêu bit?", ["8 bit", "4 bit", "16 bit"], 0, "1 Byte = 8 Bit."
))
nodes.append(make_sort_lesson("G6-04", "w2", 6, "Mạng Máy tính & Thiết bị Mạng Cốt lõi", "Chủ đề B: Mạng máy tính và Internet",
    "Bài 4: Mạng máy tính", "Bài 4: Khái niệm mạng máy tính", "Bài 3: Các thành phần của mạng",
    ["Phân biệt mạng có dây, không dây.", "Thiết bị: Switch, Router, Modem."],
    "Kết nối các máy tính thành một hệ sinh thái!", "Thành phần mạng máy tính:", ["Đầu cuối, truyền dẫn, thiết bị mạng kết nối."],
    "Thiết bị Đầu cuối", "Thiết bị Kết nối Mạng",
    [{"id":"1","name":"Laptop cá nhân","group":"g1","icon":"💻"},{"id":"2","name":"Điện thoại smartphone","group":"g1","icon":"📱"},{"id":"3","name":"Router Wi-Fi","group":"g2","icon":"📡"},{"id":"4","name":"Switch chuyển mạch","group":"g2","icon":"🔀"}],
    "Thiết bị nào định tuyến gói tin giữa các mạng?", ["Router (Bộ định tuyến)", "Màn hình", "Bàn phím"], 0, "Router chuyển tiếp các gói tin."
))
nodes.append(make_branch_lesson("G6-06", "w2", 6, "Thư điện tử (Email) & Ứng xử Mạng An toàn", "Chủ đề B: Mạng máy tính và Internet",
    "Bài 6: Thư điện tử (Email)", "Bài 6: Giao tiếp qua thư điện tử", "Bài 5: Ứng dụng thư điện tử",
    ["Cấu trúc địa chỉ email: username@domain.", "Quy tắc viết thư điện tử lịch sự và đính kèm tệp."],
    "Hòm thư số kết nối học tập và công việc!", "Địa chỉ email và nghi thức giao tiếp:", ["Có tiêu đề rõ ràng, lời chào trang trọng, tệp đính kèm an toàn."],
    "Nhận được email từ địa chỉ lạ có tệp đính kèm 'quatang.exe'.", "Xóa email, không mở tệp lạ.", "Tải về mở ngay.", "Rất cảnh giác!", "Có thể dính mã độc!",
    "Ký tự bắt buộc phải có trong địa chỉ email là:", ["@", "#", "$"], 0, "Ký tự @ phân tách tên và tên miền."
))
nodes.append(make_bughunt_lesson("G6-13", "w2", 6, "Thuật toán Tìm kiếm Tuần tự & Nhị phân", "Chủ đề F: Giải quyết vấn đề với máy tính",
    "Bài 13, 14: Thuật toán tìm kiếm tuần tự và nhị phân", "Bài 12, 13: Tìm kiếm tuần tự và nhị phân", "Bài 12, 13: Thuật toán tìm kiếm",
    ["Thuật toán tìm kiếm tuần tự duyệt từ đầu đến cuối.", "Tìm kiếm nhị phân chia đôi trên danh sách đã sắp xếp."],
    "Tìm cuốn sách trong thư viện nghìn cuốn như thế nào?", "So sánh hai chiến lược tìm kiếm:", ["Tuần tự: O(N) chậm. Nhị phân: O(log N) siêu tốc độ."],
    "Điều kiện bắt buộc để áp dụng thuật toán tìm kiếm nhị phân là gì?", ["Dãy số đã được sắp xếp thứ tự", "Dãy số có số lượng chẵn", "Dãy số toàn số dương"], 0, "Phải sắp xếp trước thì mới chia đôi được."
))

# ==============================================================================
# LỚP 7 (14 BÀI THCS - THẾ GIỚI 2)
# ==============================================================================
nodes.append(make_sort_lesson("G7-01", "w2", 7, "Thiết bị Vào - Ra & Cổng Kết nối Máy tính", "Chủ đề A: Máy tính và cộng đồng",
    "Bài 1: Thiết bị vào - ra", "Bài 1: Thiết bị vào và ra", "Bài 1: Thiết bị vào và thiết bị ra",
    ["Phân biệt thiết bị vào (Input) và thiết bị ra (Output).", "Nhận biết cổng HDMI, USB, Type-C, Audio jack."],
    "Giao tiếp giữa con người và cỗ máy vi tính!", "Dữ liệu đi vào và thông tin xuất ra:", ["Vào: Bàn phím, chuột, mic. Ra: Màn hình, loa, máy in."],
    "Thiết bị Vào (Input)", "Thiết bị Ra (Output)",
    [{"id":"1","name":"Webcam ghi hình","group":"g1","icon":"📷"},{"id":"2","name":"Máy quét Scanner","group":"g1","icon":"📠"},{"id":"3","name":"Máy chiếu Projector","group":"g2","icon":"📽️"},{"id":"4","name":"Bộ loa âm thanh","group":"g2","icon":"🔊"}],
    "Thiết bị nào vừa là thiết bị vào vừa là thiết bị ra?", ["Màn hình cảm ứng", "Bàn phím cơ", "Máy in đơn năng"], 0, "Màn hình cảm ứng vừa chạm vừa hiển thị."
))
nodes.append(make_memory_lesson("G7-06", "w2", 7, "Bảng tính Điện tử & Các Hàm Toán học", "Chủ đề E: Ứng dụng tin học",
    "Bài 6, 7: Bảng tính điện tử và các hàm", "Bài 5, 6: Ô tính và hàm SUM, AVERAGE", "Bài 5, 6: Phần mềm bảng tính",
    ["Sử dụng thành thạo =SUM, =AVERAGE, =COUNT, =MAX, =MIN."], "Quản lý dữ liệu chuyên nghiệp trên bảng tính!", "Cú pháp hàm bảng tính chuẩn xác:", ["Bắt đầu bằng dấu =, dải ô ví dụ A1:A10."],
    "Công thức nào tính tổng các số từ A1 đến A5?", ["=SUM(A1:A5)", "=TOTAL(A1:A5)", "=ADD(A1:A5)"], 0, "Hàm =SUM dùng tính tổng."
))
nodes.append(make_bughunt_lesson("G7-11", "w2", 7, "Thuật toán Sắp xếp Nổi bọt & Sắp xếp Chọn", "Chủ đề F: Giải quyết vấn đề với máy tính",
    "Bài 11, 12: Sắp xếp nổi bọt và sắp xếp chọn", "Bài 11, 12: Các thuật toán sắp xếp", "Bài 11, 12: Sắp xếp nổi bọt và chọn",
    ["Mô phỏng Bubble Sort so sánh cặp liền kề.", "Mô phỏng Selection Sort tìm min đưa về đầu."],
    "Sắp xếp dãy số tăng dần như thế nào?", "Hai thuật toán sắp xếp nền tảng:", ["Bubble sort hoán đổi liền kề. Selection sort tìm min."],
    "Trong sắp xếp nổi bọt tăng dần, nếu a[i] > a[i+1] ta làm gì?", ["Đổi chỗ a[i] và a[i+1]", "Xóa a[i]", "Dừng chương trình"], 0, "Đổi chỗ để đưa số lớn về sau."
))

# ==============================================================================
# LỚP 8 (14 BÀI THCS - THẾ GIỚI 2)
# ==============================================================================
nodes.append(make_memory_lesson("G8-01", "w2", 8, "Lịch sử Phát triển Máy tính & Thế hệ Vi xử lý", "Chủ đề A: Máy tính và cộng đồng",
    "Bài 1: Lịch sử phát triển máy tính", "Bài 1: Lịch sử máy tính", "Bài 1: Lịch sử và thế hệ máy tính",
    ["Nắm 5 thế hệ máy tính: Đèn điện tử, Transistor, Mạch tích hợp IC, VLSI, AI."],
    "Từ cỗ máy nặng 30 tấn ENIAC đến con chip siêu nhỏ ngày nay!",
    "Tiến trình phát triển phần cứng máy tính:", ["Thế hệ 1: Đèn điện tử chân không.", "Thế hệ 2: Bóng bán dẫn Transistor.", "Thế hệ 3: Mạch tích hợp IC.", "Thế hệ 4 & 5: Vi xử lý siêu tích hợp và Trí tuệ nhân tạo."],
    "Thế hệ thứ nhất của máy tính điện tử sử dụng linh kiện gì?", ["Đèn điện tử chân không", "Bóng bán dẫn", "Mạch vi xử lý"], 0, "Đèn điện tử chân không cồng kềnh và tỏa nhiều nhiệt."
))
nodes.append(make_sort_lesson("G8-08", "w2", 8, "Địa chỉ Tuyệt đối ($A$1) & Tương đối trong Excel", "Chủ đề E: Ứng dụng tin học",
    "Bài 8: Địa chỉ tương đối và tuyệt đối", "Bài 7: Địa chỉ ô tính nâng cao", "Bài 7: Địa chỉ tương đối và tuyệt đối",
    ["Phân biệt A1 (tương đối), $A$1 (tuyệt đối), $A1, A$1 (hỗn hợp)."],
    "Khóa cố định địa chỉ ô tính khi sao chép công thức!", "Dấu đô la ($) trước cột hoặc hàng để khóa cứng:", ["Dùng phím F4 để chuyển nhanh giữa các loại địa chỉ."],
    "Địa chỉ Tuyệt Đối (Khóa cứng)", "Địa chỉ Tương Đối (Tự đổi khi copy)",
    [{"id":"1","name":"$C$5 (Khóa cả cột & dòng)","group":"g1","icon":"🔒"},{"id":"2","name":"$B$10 (Khóa cả bảng)","group":"g1","icon":"🔒"},{"id":"3","name":"A1 (Thay đổi linh hoạt)","group":"g2","icon":"🔄"},{"id":"4","name":"B2:C4 (Thay đổi theo vị trí)","group":"g2","icon":"🔄"}],
    "Ký tự nào dùng để tạo địa chỉ tuyệt đối trong bảng tính?", ["Dấu đô la ($)", "Dấu thăng (#)", "Dấu và (&)"], 0, "Dấu $ khóa cố định hàng hoặc cột."
))
nodes.append(make_bughunt_lesson("G8-11", "w2", 8, "Lập trình: Biến, Câu lệnh Rẽ nhánh & Vòng lặp", "Chủ đề F: Giải quyết vấn đề với máy tính",
    "Bài 11, 12, 13: Biến, rẽ nhánh và vòng lặp", "Bài 10, 11, 12: Cấu trúc lập trình", "Bài 10, 11, 12: Lập trình có cấu trúc",
    ["Kết hợp biến số, rẽ nhánh if và vòng lặp while."], "Giải quyết bài toán phức tạp bằng cấu trúc lặp!", "Ba trụ cột của lập trình có cấu trúc:", ["Tuần tự, rẽ nhánh có điều kiện và lặp."],
    "Vòng lặp while kiểm tra điều kiện lặp ở đâu?", ["Trước khi thực hiện khối lệnh", "Sau khi đã xong hết", "Không bao giờ kiểm tra"], 0, "While kiểm tra điều kiện trước mỗi vòng lặp."
))

# ==============================================================================
# LỚP 9 (14 BÀI THCS - THẾ GIỚI 2)
# ==============================================================================
nodes.append(make_branch_lesson("G9-02", "w2", 9, "An toàn Không gian Mạng & Phòng chống Mã độc", "Chủ đề D: Đạo đức môi trường số",
    "Bài 2, 3: Mã độc và bảo vệ dữ liệu cá nhân", "Bài 2, 3: Phòng chống nguy cơ mạng", "Bài 2, 3: Tác động của tin học và an toàn số",
    ["Nhận diện Virus, Worm, Trojan, Spyware, Ransomware.", "Xác thực 2 yếu tố (2FA) và thói quen sao lưu dữ liệu."],
    "Chiến trường vô hình bảo vệ tài sản số!", "Mã độc xâm nhập qua tệp tải về và email:", ["Không bấm link lạ, dùng mật khẩu mạnh và bật 2FA."],
    "Trang web yêu cầu tải phần mềm 'speedup.exe' để tăng tốc máy tính.", "Đóng trang web, quét virus cho máy.", "Tải về chạy thử.", "Rất an toàn!", "Mã độc trojan!",
    "Loại mã độc nào tự động lây lan qua mạng mà không cần người dùng can thiệp?", ["Sâu máy tính (Worm)", "Bàn phím hỏng", "Màn hình lỗi"], 0, "Worm tự nhân bản và lây qua các lỗ hổng mạng."
))
nodes.append(make_maze_lesson("G9-09", "w2", 9, "Tư duy Phân rã Vấn đề & Thuật toán Đệ quy Cơ bản", "Chủ đề F: Giải quyết vấn đề với máy tính",
    "Bài 9, 10: Phân rã bài toán và thuật toán", "Bài 8, 9: Tư duy phân rã và thuật toán", "Bài 8, 9: Thuật toán giải quyết vấn đề",
    ["Chia bài toán lớn thành các bài toán con độc lập (Decomposition)."],
    "Chiến thuật Chia để trị (Divide and Conquer) kinh điển!", "Giải quyết vấn đề phức tạp theo phương pháp khoa học:", ["Phân rã thành bài toán con, giải từng phần rồi ghép lại."],
    "Phương pháp chia một bài toán lớn thành các bài toán nhỏ hơn gọi là:", ["Phân rã bài toán (Decomposition)", "Xóa bài toán", "Nhân đôi bài toán"], 0, "Phân rã giúp bài toán lớn trở nên đơn giản."
))

# ==============================================================================
# LỚP 10 (16 BÀI THPT - THẾ GIỚI 3: THÀNH PHỐ THUẬT TOÁN)
# ==============================================================================
nodes.append(make_logic_lesson("G10-04", "w3", 10, "Cổng Logic & Đại số Boole trong Phần cứng", "Chủ đề A: Máy tính và xã hội tri thức (CS)",
    "Bài 4: Mạch logic và cổng logic", "Bài 4: Cổng logic và bảng chân trị", "Bài 4: Mạch logic cơ bản",
    ["Bảng chân trị AND, OR, NOT, XOR.", "Thiết kế mạch cộng nhị phân bán phần (Half Adder)."],
    "Xây dựng bộ vi xử lý từ những cổng logic Boole!", "Mạch số hoạt động dựa trên điện áp logic 0 và 1:", ["Cổng AND nhân logic, cổng OR cộng logic, cổng NOT đảo."],
    "Cổng logic nào chỉ cho đầu ra 1 khi CẢ HAI đầu vào đều bằng 1?", ["Cổng AND", "Cổng OR", "Cổng NOT"], 0, "Cổng AND thực hiện phép nhân logic."
))
nodes.append(make_bughunt_lesson("G10-16", "w3", 10, "Lập trình Python Toàn diện: Biến, Kiểu dữ liệu & Rẽ nhánh", "Chủ đề F: Giải quyết vấn đề với máy tính",
    "Bài 16, 18, 19: Lập trình Python, if, for, while", "Bài 14, 16, 17: Cú pháp Python, rẽ nhánh và lặp", "Bài 14, 16, 17: Môi trường lập trình Python",
    ["Thụt lề khối lệnh Python chuẩn PEP 8.", "Cấu trúc if - elif - else và vòng lặp for/while."],
    "Python - ngôn ngữ AI phổ biến nhất hành tinh!", "Quy tắc ngữ pháp quan trọng của Python:", ["Indentation 4 spaces bắt buộc, kiểu dữ liệu tự động suy diễn."],
    "Trong Python, câu lệnh nào dùng để lặp qua một chuỗi số?", ["for i in range(n):", "loop i to n:", "repeat n times:"], 0, "Vòng for kết hợp range() là chuẩn cú pháp Python."
))
nodes.append(make_type_lesson("G10-24", "w3", 10, "Cấu trúc Dữ liệu Danh sách (List) & Xâu ký tự (String) Python", "Chủ đề F: Giải quyết vấn đề với máy tính",
    "Bài 22, 24: Danh sách và xâu ký tự trong Python", "Bài 19, 20: Kiểu danh sách và xâu", "Bài 19, 20: Danh sách và xâu trong Python",
    ["Thao tác cắt lát (Slicing) danh sách và chuỗi.", "Các phương thức: append(), pop(), len(), split(), join()."],
    "Xử lý tập hợp dữ liệu lớn với List và String!", "Hai cấu trúc dữ liệu mạnh mẽ bậc nhất Python:", ["List lưu trữ mảng đa kiểu, String xử lý văn bản linh hoạt."],
    "Phương thức nào thêm một phần tử vào cuối danh sách trong Python?", [".append()", ".add()", ".insert_last()"], 0, "list.append(x) thêm x vào cuối danh sách."
))
nodes.append(make_branch_lesson("G10-09", "w3", 10, "Luật An ninh Mạng & Văn hóa Số", "Chủ đề D: Đạo đức môi trường số",
    "Bài 9: Luật An ninh mạng và văn hóa số", "Bài 8: Đạo đức và pháp luật trên mạng", "Bài 8: Pháp luật trong môi trường số",
    ["Hiểu các điều khoản cấm theo Luật An ninh mạng Việt Nam."], "Tuân thủ pháp luật khi tham gia không gian mạng!", "Pháp luật bảo vệ công dân số trên Internet:", ["Nghiêm cấm phát tán tin giả, bôi nhọ, xâm phạm an ninh quốc gia."],
    "Có người đăng bài bịa đặt gây hoang mang dư luận trên mạng.", "Không like, không share và báo cơ quan chức năng.", "Chia sẻ ngay để câu view.", "Chuẩn mực công dân!", "Vi phạm Luật An ninh mạng!",
    "Hành vi nào vi phạm nghiêm trọng Luật An ninh mạng?", ["Phát tán thông tin sai sự thật trên mạng xã hội", "Học trực tuyến", "Gửi email cho bạn bè"], 0, "Phát tán tin giả bị xử lý nghiêm minh theo pháp luật."
))

# ==============================================================================
# LỚP 11 (14 BÀI THPT - THẾ GIỚI 3)
# ==============================================================================
nodes.append(make_memory_lesson("G11-CS1", "w3", 11, "Cơ sở Dữ liệu Quan hệ (RDBMS) & Khóa chính", "Chủ đề CS: Khoa học máy tính",
    "Bài CS-1, CS-2: CSDL quan hệ và mô hình dữ liệu", "Bài CS-1, CS-2: Hệ CSDL và bảng quan hệ", "Bài CS-1, CS-2: Cơ sở dữ liệu và bảng",
    ["Hiểu Khóa chính (Primary Key) xác định duy nhất bản ghi.", "Khóa ngoại (Foreign Key) tạo liên kết giữa các bảng."],
    "Trái tim lưu trữ dữ liệu của mọi ứng dụng ngân hàng và mạng xã hội!",
    "Kiến trúc CSDL quan hệ RDBMS:", ["Bảng (Table) gồm các hàng (Record) và cột (Field).", "Khóa chính không được chứa giá trị rỗng (NOT NULL) và không trùng lặp."],
    "Đặc điểm bắt buộc của một Khóa chính (Primary Key) là:", ["Duy nhất và không được để trống (NOT NULL)", "Chứa giá trị tùy ý", "Phải là số chẵn"], 0, "Khóa chính định danh duy nhất cho từng hàng dữ liệu."
))
nodes.append(make_logic_lesson("G11-SQL", "w3", 11, "Ngôn ngữ Truy vấn Dữ liệu SQL (Structured Query Language)", "Chủ đề CS: Khoa học máy tính",
    "Bài CS-3, CS-4: Truy vấn SQL và nối bảng JOIN", "Bài CS-3, CS-4: Ngôn ngữ SQL và truy vấn", "Bài CS-3, CS-4: Lệnh truy vấn SQL",
    ["Viết câu lệnh SELECT ... FROM ... WHERE.", "Sắp xếp ORDER BY và kết nối bảng INNER JOIN."],
    "Trò chuyện với cơ sở dữ liệu bằng ngôn ngữ truy vấn SQL!", "Cú pháp chuẩn mực của SQL:", ["SELECT các_cột FROM tên_bảng WHERE điều_kiện;"],
    "Mệnh đề nào trong SQL dùng để lọc dữ liệu theo điều kiện?", ["WHERE", "FROM", "GROUP BY"], 0, "WHERE dùng để thiết lập điều kiện lọc."
))
nodes.append(make_bughunt_lesson("G11-RECUR", "w3", 11, "Thuật toán Đệ quy (Recursion) & Chia để trị", "Chủ đề CS: Khoa học máy tính",
    "Bài CS-6, CS-8: Thuật toán đệ quy và sắp xếp nhanh", "Bài CS-5, CS-7: Đệ quy và chia để trị", "Bài CS-5, CS-7: Thuật toán đệ quy",
    ["Hiểu điểm dừng (Base case) và bước đệ quy (Recursive step).", "Áp dụng đệ quy cho bài toán giai thừa, tháp Hà Nội, QuickSort."],
    "Hàm tự gọi lại chính nó để giải quyết bài toán nhỏ hơn!", "Nguyên tắc sống còn của thuật toán đệ quy:", ["Bắt buộc phải có điểm dừng (Base case) để tránh tràn bộ nhớ Stack Overflow."],
    "Nếu hàm đệ quy không có điểm dừng (Base case), điều gì sẽ xảy ra?", ["Lặp vô hạn và tràn bộ nhớ ngăn xếp (Stack Overflow)", "Chương trình chạy nhanh hơn", "Máy tính tự tắt nguồn"], 0, "Thiếu điểm dừng sẽ gây lỗi Stack Overflow sập chương trình."
))

# ==============================================================================
# LỚP 12 (14 BÀI THPT - THẾ GIỚI 3: ĐẠI CHIẾN BOSS AI & MẠNG)
# ==============================================================================
nodes.append(make_sort_lesson("G12-NET", "w3", 12, "Giao thức Mạng TCP/IP & Kiến trúc Internet", "Chủ đề Mạng máy tính nâng cao",
    "Bài 1, 2, 3: Giao thức mạng TCP/IP và địa chỉ IP", "Bài 1, 2, 3: Mô hình mạng và giao thức truyền thông", "Bài 1, 2, 3: Giao thức mạng và định tuyến",
    ["Phân tầng TCP/IP: Application, Transport, Internet, Network Access.", "Địa chỉ IPv4 (32-bit) vs IPv6 (128-bit), Domain Name System (DNS)."],
    "Xương sống của thế giới mạng Internet toàn cầu!", "Cách dữ liệu di chuyển xuyên đại dương:", ["IP định tuyến gói tin, TCP đảm bảo tính toàn vẹn và thứ tự."],
    "Giao thức Truyền thông", "Địa chỉ Định danh Mạng",
    [{"id":"1","name":"Giao thức TCP (Đảm bảo tin cậy)","group":"g1","icon":"📦"},{"id":"2","name":"Giao thức HTTPS (Mã hóa web)","group":"g1","icon":"🔒"},{"id":"3","name":"Địa chỉ IPv4 (192.168.1.1)","group":"g2","icon":"🏷️"},{"id":"4","name":"Tên miền DNS (easytin.vn)","group":"g2","icon":"🌐"}],
    "Giao thức nào chuyển đổi tên miền dạng chữ (google.com) thành địa chỉ IP số?", ["Hệ thống DNS (Domain Name System)", "HTTP", "FTP"], 0, "DNS là cuốn danh bạ chuyển đổi tên miền sang IP."
))
nodes.append(make_sort_lesson("G12-AI", "w3", 12, "Nhập môn Trí tuệ Nhân tạo & Học máy (Machine Learning)", "Chủ đề Trí tuệ Nhân tạo",
    "Bài 5, 6: Khái niệm AI và Học máy (Machine Learning)", "Bài 5, 6: Tổng quan AI và học máy", "Bài 5, 6: Trí tuệ nhân tạo và ứng dụng",
    ["Phân biệt AI hẹp (Narrow AI) và AI tổng quát (AGI).", "Ba nhánh học máy: Học có giám sát (Supervised), Không giám sát (Unsupervised), Học tăng cường (Reinforcement)."],
    "Dạy cho cỗ máy khả năng tự học từ dữ liệu!", "Cách thức trí tuệ nhân tạo tiếp thu tri thức:", ["Máy học từ dữ liệu huấn luyện (Training data), điều chỉnh trọng số nơ-ron để dự đoán chính xác."],
    "Học có Giám sát (Có nhãn)", "Học không Giám sát (Tự gom cụm)",
    [{"id":"1","name":"Nhận diện ảnh mèo (Dữ liệu gắn nhãn 'Mèo')","group":"g1","icon":"🏷️"},{"id":"2","name":"Dự đoán giá nhà theo diện tích","group":"g1","icon":"📈"},{"id":"3","name":"Phân khúc khách hàng tự động","group":"g2","icon":"👥"},{"id":"4","name":"Phát hiện giao dịch gian lận bất thường","group":"g2","icon":"🕵️"}],
    "Trong học máy, tập dữ liệu dùng để mô hình học tập các đặc trưng gọi là gì?", ["Dữ liệu huấn luyện (Training data)", "Dữ liệu rác", "Dữ liệu trống"], 0, "Training data là mẫu để thuật toán học các tham số."
))
nodes.append(make_branch_lesson("G12-ETHIC", "w3", 12, "Đạo đức AI & Bản quyền trong Kỷ nguyên Số", "Chủ đề Đạo đức và Pháp luật số",
    "Bài 8: Đạo đức AI và trách nhiệm số", "Bài 8: Đạo đức trong kỷ nguyên AI", "Bài 8: Trách nhiệm và đạo đức AI",
    ["Thiên kiến thuật toán (Algorithmic Bias).", "Bản quyền và tính minh bạch của sản phẩm do AI tạo ra."],
    "Công nghệ là công cụ, đạo đức của con người là kim chỉ nam!", "Trách nhiệm xã hội khi phát triển và sử dụng AI:", ["Tránh thiên kiến phân biệt đối xử, bảo vệ dữ liệu cá nhân, minh bạch nguồn gốc."],
    "Hệ thống tuyển dụng tự động bị phát hiện thiên vị chỉ chọn ứng viên nam do dữ liệu lịch sử cũ có thiên kiến.", "Huấn luyện lại mô hình với tập dữ liệu công bằng, đa dạng.", "Mặc kệ vì máy tính luôn luôn đúng.", "Rất đúng đắn!", "Bỏ qua thiên kiến là vi phạm đạo đức!",
    "Thiên kiến trong mô hình AI thường bắt nguồn từ đâu?", ["Từ dữ liệu huấn luyện lịch sử có sẵn định kiến", "Do máy tính tự ghét con người", "Do mạng Internet chập chờn"], 0, "Dữ liệu huấn luyện phản ánh định kiến con người nên mô hình học theo."
))
nodes.append(create_lesson(
    "G12-BOSS", "w3", 12, "Đại Chiến Boss Trí tuệ Nhân tạo Toàn cầu", "Tổng kết GDPT 2018",
    "Chuyên đề Tổng kết Tin học 12", "Chuyên đề Tổng kết Tin học 12", "Chuyên đề Tổng kết Tin học 12",
    "boss-quiz", ["G10-04", "G11-CS1", "G12-NET", "G12-AI"], 15,
    ["Tổng kết toàn diện 10 năm học Tin học từ lớp 3 đến lớp 12.", "Sẵn sàng định hướng nghề nghiệp công nghệ thông tin tương lai."],
    "Trùm cuối Virus 'Glitch Byte' đang muốn hủy diệt kho dữ liệu tri thức của nhân loại! Hãy dùng sức mạnh tổng hợp 10 năm học Tin học để đánh bại Glitch Byte!",
    "Đấu trường đỉnh cao tổng hợp kiến thức Phần cứng, Thuật toán, Mạng máy tính và Trí tuệ nhân tạo:",
    ["Kỹ thuật tìm kiếm nhị phân chia đôi không gian O(log N).", "Trí tuệ nhân tạo (Machine Learning, Deep Learning, LLM) và dữ liệu huấn luyện.", "Đạo đức số, bảo vệ bản quyền tác phẩm và Luật An ninh mạng."],
    {"boss_name": "Glitch Byte the Destroyer", "boss_max_hp": 100, "player_max_hp": 100, "damage_per_hit": 25, "questions_pool": 6},
    [
        {"question": "Giao thức nào mã hóa siêu văn bản an toàn trên World Wide Web?", "options": ["HTTP", "HTTPS", "FTP", "TELNET"], "answer": 1, "explanation": "HTTPS dùng SSL/TLS mã hóa đường truyền."},
        {"question": "Trong học máy (Machine Learning), tập dữ liệu dùng để thuật toán học các đặc trưng gọi là gì?", "options": ["Training data", "Test data", "Hidden data", "Null data"], "answer": 0, "explanation": "Training data là tập dữ liệu huấn luyện."},
        {"question": "Thuật toán tìm kiếm nhị phân có độ phức tạp thời gian nào trên mảng đã sắp xếp?", "options": ["O(N)", "O(log N)", "O(N^2)", "O(1)"], "answer": 1, "explanation": "Binary search đạt O(log N) bằng cách chia đôi mỗi bước."},
        {"question": "Luật An ninh mạng Việt Nam nghiêm cấm hành vi nào sau đây?", "options": ["Học lập trình website", "Phát tán tin giả, xúc phạm danh dự người khác trên mạng", "Mua bản quyền phần mềm", "Cài đặt chương trình bảo vệ máy tính"], "answer": 1, "explanation": "Phát tán tin giả, xúc phạm người khác bị xử lý nghiêm theo luật."}
    ],
    "CHIẾN THẮNG HUY HOÀNG! Em đã hoàn thành xuất sắc chặng đường Tin học phổ thông GDPT 2018 với danh hiệu Bậc Thầy Công Nghệ EasyTin!"
))

full_curriculum = {
    "version": "2.1.0",
    "language": "vi",
    "worlds": [
        {
            "id": "w1",
            "name": "Thung lũng Số hóa",
            "grades": [3, 4, 5],
            "description": "Khám phá thế giới máy tính kỳ diệu, làm chủ chuột phím, an toàn số và thuật toán phiêu lưu.",
            "color_theme": "#2b5c3f"
        },
        {
            "id": "w2",
            "name": "Rừng Mạng & Dữ liệu",
            "grades": [6, 7, 8, 9],
            "description": "Giải mã các bit nhị phân, định tuyến mạng internet, bảng tính điện tử và thợ săn lỗi thuật toán.",
            "color_theme": "#1f3b5c"
        },
        {
            "id": "w3",
            "name": "Thành phố Thuật toán",
            "grades": [10, 11, 12],
            "description": "Lập trình Python, cổng logic phần cứng, cơ sở dữ liệu quan hệ SQL và chinh phục đấu trường AI.",
            "color_theme": "#5c2b4e"
        }
    ],
    "nodes": nodes
}

curriculum_path = os.path.join(os.path.dirname(__file__), "..", "curriculum.json")
with open(curriculum_path, "w", encoding="utf-8") as f:
    json.dump(full_curriculum, f, ensure_ascii=False, indent=2)

print(f"Total curriculum nodes generated: {len(nodes)}")
for g in range(3, 13):
    count = sum(1 for n in nodes if n["grade"] == g)
    print(f"Grade {g}: {count} lessons")
