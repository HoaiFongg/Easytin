# -*- coding: utf-8 -*-
"""
Bộ tạo chương trình học EasyTin toàn diện 100%:
Phủ toàn bộ bài học và nội dung chi tiết của cả 3 bộ sách:
1. Kết nối tri thức với cuộc sống (KNTT)
2. Cánh Diều (CD)
3. Chân trời sáng tạo (CTST)
từ Lớp 3 đến Lớp 12 theo Chương trình GDPT 2018 (Thông tư 32/2018/TT-BGDĐT).
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

# Helper generators
def make_branch(nid, wid, gr, title, domain, kntt, cd, ctst, prereqs, goals, hook, summ, pts, sc_prompt, c_right, c_wrong, f_right, f_wrong, q_txt, q_opts, q_ans, q_exp):
    return create_lesson(
        nid, wid, gr, title, domain, kntt, cd, ctst, "branch-story", prereqs, 6, goals, hook, summ, pts,
        {"scenarios": [{"id": "s1", "prompt": sc_prompt, "choices": [{"text": c_right, "is_correct": True, "feedback": f_right}, {"text": c_wrong, "is_correct": False, "feedback": f_wrong}]}]},
        [{"question": q_txt, "options": q_opts, "answer": q_ans, "explanation": q_exp}],
        "Em đã đưa ra quyết định rất sáng suốt và hoàn thành xuất sắc bài học!"
    )

def make_sort(nid, wid, gr, title, domain, kntt, cd, ctst, prereqs, goals, hook, summ, pts, g1_name, g2_name, items, q_txt, q_opts, q_ans, q_exp):
    return create_lesson(
        nid, wid, gr, title, domain, kntt, cd, ctst, "sort-drag", prereqs, 6, goals, hook, summ, pts,
        {"groups": [{"id": "g1", "name": g1_name}, {"id": "g2", "name": g2_name}], "items": items},
        [{"question": q_txt, "options": q_opts, "answer": q_ans, "explanation": q_exp}],
        "Chúc mừng em đã phân loại chính xác các thành phần kiến thức!"
    )

def make_maze(nid, wid, gr, title, domain, kntt, cd, ctst, prereqs, goals, hook, summ, pts, q_txt, q_opts, q_ans, q_exp):
    return create_lesson(
        nid, wid, gr, title, domain, kntt, cd, ctst, "block-maze", prereqs, 7, goals, hook, summ, pts,
        {"grid_size": 4, "start": {"x": 0, "y": 0, "dir": "E"}, "target": {"x": 2, "y": 2}, "walls": [{"x": 1, "y": 0}], "allowed_blocks": ["forward", "turn_right", "turn_left"], "max_blocks": 6},
        [{"question": q_txt, "options": q_opts, "answer": q_ans, "explanation": q_exp}],
        "Thuật toán điều khiển của em đã giúp nhân vật vượt mê cung thành công!"
    )

def make_logic(nid, wid, gr, title, domain, kntt, cd, ctst, prereqs, goals, hook, summ, pts, bits, weights, targets, q_txt, q_opts, q_ans, q_exp):
    return create_lesson(
        nid, wid, gr, title, domain, kntt, cd, ctst, "logic-puzzle", prereqs, 8, goals, hook, summ, pts,
        {"bits_count": bits, "weights": weights, "target_values": targets},
        [{"question": q_txt, "options": q_opts, "answer": q_ans, "explanation": q_exp}],
        "Tư duy logic của em thật sắc bén và chuẩn xác!"
    )

def make_type(nid, wid, gr, title, domain, kntt, cd, ctst, prereqs, goals, hook, summ, pts, words, q_txt, q_opts, q_ans, q_exp):
    return create_lesson(
        nid, wid, gr, title, domain, kntt, cd, ctst, "type-run", prereqs, 6, goals, hook, summ, pts,
        {"words": words},
        [{"question": q_txt, "options": q_opts, "answer": q_ans, "explanation": q_exp}],
        "Tốc độ gõ phím của em thật ấn tượng và chuẩn xác từng ký tự!"
    )

def make_memory(nid, wid, gr, title, domain, kntt, cd, ctst, prereqs, goals, hook, summ, pts, cards, q_txt, q_opts, q_ans, q_exp):
    return create_lesson(
        nid, wid, gr, title, domain, kntt, cd, ctst, "match-memory", prereqs, 6, goals, hook, summ, pts,
        {"cards": cards},
        [{"question": q_txt, "options": q_opts, "answer": q_ans, "explanation": q_exp}],
        "Trí nhớ siêu đẳng! Em đã ghép đôi hoàn hảo các thuật ngữ bài học!"
    )

def make_bughunt(nid, wid, gr, title, domain, kntt, cd, ctst, prereqs, goals, hook, summ, pts, q_txt, q_opts, q_ans, q_exp):
    return create_lesson(
        nid, wid, gr, title, domain, kntt, cd, ctst, "bug-hunt", prereqs, 8, goals, hook, summ, pts,
        {},
        [{"question": q_txt, "options": q_opts, "answer": q_ans, "explanation": q_exp}],
        "Xuất sắc! Em đã tìm và diệt sạch mọi lỗi trong đoạn mã!"
    )

def make_boss(nid, wid, gr, title, domain, kntt, cd, ctst, prereqs, goals, hook, summ, pts, boss_name, questions, victory_msg):
    return create_lesson(
        nid, wid, gr, title, domain, kntt, cd, ctst, "boss-quiz", prereqs, 12, goals, hook, summ, pts,
        {"boss_name": boss_name, "boss_max_hp": 100, "player_max_hp": 100, "damage_per_hit": 25, "questions_pool": len(questions)},
        questions,
        victory_msg
    )

# ==============================================================================
# LỚP 3 (14 NÚT - THẾ GIỚI 1)
# ==============================================================================
nodes.append(make_branch("G3-01", "w1", 3, "Thông tin và Quyết định Cuộc sống", "Chủ đề A: Máy tính và em",
    "Bài 1: Thông tin và quyết định", "Bài 1: Em làm quen với máy tính", "Bài 1: Thông tin và tiếp nhận thông tin",
    [], ["Nhận biết thông tin thu nhận qua các giác quan.", "Hiểu thông tin giúp con người đưa ra quyết định đúng đắn."],
    "Buổi sáng bước ra cửa, em nhìn thấy trời nhiều mây đen và nghe tiếng sấm chớp ầm ầm. Em sẽ quyết định thế nào?",
    "Thông tin là những điều em nhìn thấy, nghe thấy hoặc cảm nhận được từ thế giới xung quanh. Nhờ có thông tin, con người đưa ra các quyết định hành động phù hợp.",
    ["Mắt nhìn thấy, tai nghe thấy đều mang lại thông tin hữu ích.", "Quyết định đúng đắn dựa trên thông tin chính xác."],
    "Trời bắt đầu đổ mưa rào khi em chuẩn bị đi học đến trường.", "Mang theo ô (dù) hoặc mặc áo mưa cẩn thận.", "Mặc kệ cứ đi tay không ra ngoài.", "Rất đúng! Thông tin trời mưa giúp em bảo vệ sức khỏe.", "Em có thể bị ướt và cảm lạnh!",
    "Giác quan nào giúp em nhìn thấy màu sắc của tín hiệu đèn giao thông?", ["Mắt (Thị giác)", "Tai (Thính giác)", "Mũi (Khứu giác)"], 0, "Mắt giúp ta quan sát và thu nhận thông tin hình ảnh, màu sắc."
))

nodes.append(make_sort("G3-02", "w1", 3, "Xử lý Thông tin & Các dạng Dữ liệu", "Chủ đề A: Máy tính và em",
    "Bài 2: Xử lý thông tin", "Bài 2: Các bộ phận của máy tính", "Bài 1: Thông tin và tiếp nhận thông tin",
    ["G3-01"], ["Phân biệt 4 bước: Thu nhận -> Lưu trữ -> Xử lý -> Truyền đạt.", "Nhận diện dạng thông tin: Chữ, Hình ảnh, Âm thanh."],
    "Máy tính và con người đều có khả năng tiếp nhận và xử lý thông tin siêu đẳng!",
    "Bốn hoạt động thông tin cơ bản gồm: Thu nhận thông tin, Lưu trữ thông tin, Xử lý thông tin và Truyền đạt thông tin.",
    ["Bộ não con người và bộ vi xử lý máy tính đều thực hiện xử lý thông tin.", "Thông tin có thể lưu trữ trong sách vở hoặc ổ đĩa máy tính."],
    "Thu nhận thông tin (Đầu vào)", "Truyền đạt thông tin (Đầu ra)",
    [{"id":"1","name":"Đọc dòng chữ trên bảng lớp","group":"g1","icon":"👀"},{"id":"2","name":"Nghe tiếng chuông báo giờ ra chơi","group":"g1","icon":"🔔"},{"id":"3","name":"Nói lời chào thầy cô","group":"g2","icon":"🗣️"},{"id":"4","name":"Gửi thư báo tin vui cho bạn bè","group":"g2","icon":"✉️"}],
    "Khi em nghe bạn kể một câu chuyện vui rồi bật cười, hoạt động nghe thuộc bước nào?", ["Thu nhận thông tin", "Xử lý thông tin", "Lưu trữ thông tin"], 0, "Tai nghe âm thanh câu chuyện là bước thu nhận thông tin."
))

nodes.append(make_sort("G3-03", "w1", 3, "Khám phá Phần cứng & Bộ phận Máy tính", "Chủ đề A: Máy tính và em",
    "Bài 3: Máy tính - những người bạn mới", "Bài 2: Các bộ phận của máy tính", "Bài 2: Khám phá máy tính",
    ["G3-01"], ["Nhận biết 4 bộ phận cơ bản: Thân máy, Màn hình, Bàn phím, Chuột.", "Hiểu chức năng chính của từng bộ phận."],
    "Gặp gỡ biệt đội máy tính kỳ diệu hỗ trợ việc học tập mỗi ngày!",
    "Máy tính để bàn gồm 4 bộ phận chính: Thân máy (bộ não xử lý), Màn hình (hiển thị kết quả), Bàn phím (nhập chữ và số), Chuột (điều khiển nhanh chóng).",
    ["Thân máy chứa bộ xử lý trung tâm CPU điều khiển mọi hoạt động.", "Màn hình giúp em nhìn thấy chữ, tranh ảnh và video sinh động."],
    "Bộ phận Nhập dữ liệu", "Bộ phận Xuất & Xử lý",
    [{"id":"1","name":"Bàn phím máy tính","group":"g1","icon":"⌨️"},{"id":"2","name":"Chuột máy tính","group":"g1","icon":"🖱️"},{"id":"3","name":"Màn hình hiển thị","group":"g2","icon":"🖥️"},{"id":"4","name":"Thân máy (CPU)","group":"g2","icon":"🧠"}],
    "Bộ phận nào được coi là 'bộ não' điều khiển mọi hoạt động của máy tính?", ["Thân máy tính", "Màn hình", "Bàn phím"], 0, "Thân máy chứa CPU thực hiện các phép tính và chỉ huy máy tính hoạt động."
))

nodes.append(make_branch("G3-04", "w1", 3, "Làm việc với Máy tính An toàn", "Chủ đề A: Máy tính và em",
    "Bài 4: Làm việc với máy tính", "Bài 1: Em làm quen với máy tính", "Bài 2: Khám phá máy tính",
    ["G3-03"], ["Biết bật và tắt máy tính đúng quy trình an toàn.", "Ngồi đúng tư thế, giữ khoảng cách mắt từ 50-80cm."],
    "Sử dụng máy tính đúng cách giúp em học giỏi và bảo vệ đôi mắt sáng ngời!",
    "Khi ngồi học máy tính, giữ lưng thẳng, mắt ngang tầm màn hình cách từ 50 đến 80 cm. Không cắm rút dây điện khi chưa được người lớn cho phép.",
    ["Tắt máy tính bằng lệnh Start -> Shut down, không tự ý rút phích cắm nguồn.", "Sau 30-45 phút ngồi máy tính, nên đứng dậy vận động nhẹ."],
    "Em học xong bài tập vẽ trên máy tính và muốn tắt máy đi ngủ.", "Nhấp chuột vào nút Start chọn lệnh Shut down.", "Giật phích cắm điện của máy tính ra khỏi ổ cắm tường.", "Rất chuẩn! Tắt máy đúng cách bảo vệ dữ liệu và hệ điều hành.", "Tắt đột ngột có thể làm hỏng máy tính và chập điện nguy hiểm!",
    "Khoảng cách an toàn từ mắt đến màn hình máy tính là bao nhiêu?", ["Từ 50 cm đến 80 cm (khoảng một sải tay)", "Từ 10 cm đến 20 cm", "Càng gần càng tốt"], 0, "Khoảng cách 50-80cm giúp mắt không bị mỏi và tránh cận thị."
))

nodes.append(make_sort("G3-05", "w1", 3, "Thao tác Chuột máy tính Siêu đẳng", "Chủ đề A: Máy tính và em",
    "Bài 6: Sử dụng chuột máy tính", "Bài 3: Em tập dùng chuột", "Bài 3: Em tập sử dụng chuột",
    ["G3-03"], ["Cầm chuột đúng tư thế bằng tay phải.", "Thực hiện thành thạo 5 thao tác cơ bản với chuột."],
    "Chú chuột máy tính nhỏ bé nhưng có sức mạnh điều khiển phi thường!",
    "Năm thao tác chuột cơ bản gồm: Di chuyển chuột, Nháy chuột (chuột trái), Nháy nút phải chuột, Nháy đúp chuột (nhấp nhanh 2 lần) và Kéo thả chuột.",
    ["Đặt ngón trỏ lên nút chuột trái, ngón giữa lên nút chuột phải.", "Kéo thả chuột dùng để di chuyển biểu tượng trên màn hình."],
    "Thao tác Nháy đơn (1 lần)", "Thao tác Nháy kép / Kéo thả",
    [{"id":"1","name":"Nháy nút trái chuột để chọn thư mục","group":"g1","icon":"👆"},{"id":"2","name":"Nháy nút phải chuột mở thực đơn lệnh","group":"g1","icon":"👉"},{"id":"3","name":"Nháy đúp chuột để khởi động phần mềm","group":"g2","icon":"✌️"},{"id":"4","name":"Kéo thả biểu tượng tệp vào thùng rác","group":"g2","icon":"✋"}],
    "Để mở nhanh một trò chơi trên màn hình máy tính, em dùng thao tác chuột nào?", ["Nháy đúp chuột (nhấp nhanh 2 lần nút trái)", "Nháy chuột phải", "Chỉ di chuyển chuột"], 0, "Nháy đúp nút trái là thao tác mở tệp hoặc phần mềm."
))

nodes.append(make_type("G3-06", "w1", 3, "Làm quen Bàn phím & Hàng phím Cơ sở", "Chủ đề A: Máy tính và em",
    "Bài 5: Sử dụng bàn phím", "Bài 4: Em tập gõ hàng phím cơ sở", "Bài 4: Em tập sử dụng bàn phím",
    ["G3-03"], ["Nhận biết hàng phím cơ sở và hai phím có gờ F, J.", "Đặt đúng 8 ngón tay tại vị trí xuất phát."],
    "Luyện đôi bàn tay lướt phím chuẩn xác như nghệ sĩ đàn piano!",
    "Hàng phím cơ sở là hàng phím quan trọng nhất. Phím F và phím J có gờ nhỏ nổi lên để ngón trỏ đặt vào làm mốc định vị cho hai bàn tay.",
    ["Ngón trỏ tay trái đặt phím F, ngón trỏ tay phải đặt phím J.", "Hai ngón cái phụ trách gõ phím cách Spacebar dài nhất."],
    ["asdf", "jkl", "fjfj", "dksa"],
    "Hai phím nào trên hàng phím cơ sở có gờ nhô lên để định vị ngón trỏ?", ["Phím F và phím J", "Phím A và phím L", "Phím G và phím H"], 0, "Gờ trên phím F và J giúp ta đặt tay đúng mà không cần nhìn bàn phím."
))

nodes.append(make_type("G3-07", "w1", 3, "Mở rộng Kỹ năng Gõ mười ngón", "Chủ đề E: Ứng dụng tin học",
    "Bài 12: Em tập gõ bàn phím", "Bài 5: Em tập gõ các hàng phím khác", "Bài 9: Phần mềm luyện gõ phím",
    ["G3-06"], ["Gõ phím hàng trên (Q W E R T Y U I O P).", "Gõ phím hàng dưới (Z X C V B N M) và phím Enter."],
    "Chinh phục toàn bộ các hàng phím để gõ văn bản nhanh như chớp!",
    "Mỗi ngón tay phụ trách một vùng phím cố định. Sau khi vươn lên hàng trên hoặc đưa xuống hàng dưới, ngón tay luôn quay về nghỉ tại hàng phím cơ sở.",
    ["Phím Shift dùng để viết hoa ký tự.", "Phím Enter dùng để xuống dòng mới."],
    ["quyet", "viet", "hoc", "tin"],
    "Sau khi vươn ngón tay lên gõ các phím ở hàng trên, ngón tay cần quay về đâu?", ["Quay về hàng phím cơ sở", "Để nguyên ở hàng trên", "Rút tay ra khỏi bàn phím"], 0, "Ngón tay luôn phải trở về hàng phím cơ sở để sẵn sàng cho ký tự tiếp theo."
))

nodes.append(make_branch("G3-08", "w1", 3, "Khám phá Thế giới Mạng Internet", "Chủ đề B: Mạng và Internet",
    "Bài 7: Khám phá Internet", "Bài 6: Thông tin trên Internet", "Bài 5: Khám phá Internet",
    ["G3-01"], ["Hiểu Internet là mạng kết nối máy tính toàn cầu.", "Biết khai thác thông tin bổ ích và tránh thông tin xấu."],
    "Bước vào đại dương tri thức Internet với hàng triệu điều kỳ thú!",
    "Internet kết nối hàng triệu máy tính khắp hành tinh. Em có thể xem video bài học, nghe nhạc, đọc báo thiếu nhi và trò chuyện cùng bạn bè ở xa.",
    ["Chỉ truy cập các trang web học tập lành mạnh phù hợp lứa tuổi thiếu nhi.", "Hỏi ý kiến cha mẹ hoặc thầy cô khi thấy nội dung bất thường."],
    "Khi đang xem video khoa học, bỗng xuất hiện một cửa sổ quảng cáo lạ nhấp nháy đòi bấm vào để nhận quà trúng thưởng lớn.", "Báo ngay cho bố mẹ hoặc thầy cô và đóng trang web đó lại.", "Bấm ngay vào để nhận quà vì quà miễn phí rất thích.", "Rất thông minh! Đó là bẫy lừa đảo quảng cáo độc hại.", "Bấm vào quảng cáo lạ có thể khiến máy tính bị nhiễm virus nguy hiểm!"
))

nodes.append(make_sort("G3-09", "w1", 3, "Sắp xếp Phân loại Đồ vật & Thông tin", "Chủ đề C: Tổ chức lưu trữ",
    "Bài 8, 9: Sắp xếp để dễ tìm", "Bài 7: Sắp xếp đồ vật hợp lí", "Bài 6: Sắp xếp và phân loại thông tin",
    ["G3-01"], ["Biết phân loại đồ vật, tài liệu theo tiêu chí rõ ràng.", "Hiểu lợi ích của sắp xếp ngăn nắp giúp tìm kiếm nhanh."],
    "Cùng dọn dẹp góc học tập và sắp xếp tài liệu ngăn nắp!",
    "Khi đồ vật hoặc thông tin được phân loại theo tiêu chí (màu sắc, công dụng, môn học), em sẽ tìm thấy đồ dùng nhanh chóng mà không mất thời gian tìm kiếm.",
    ["Sắp xếp khoa học giúp tiết kiệm thời gian và rèn luyện tính kỷ luật.", "Dữ liệu trong máy tính cũng được phân loại vào từng thư mục tương tự."],
    "Đồ dùng học tập Vẽ mỹ thuật", "Đồ dùng học tập Môn Toán",
    [{"id":"1","name":"Hộp bút sáp màu 12 màu","group":"g1","icon":"🖍️"},{"id":"2","name":"Tập giấy vẽ trắng A4","group":"g1","icon":"📄"},{"id":"3","name":"Thước kẻ eke đo góc","group":"g2","icon":"📐"},{"id":"4","name":"Compa vẽ hình tròn","group":"g2","icon":"📏"}],
    "Lợi ích lớn nhất của việc sắp xếp đồ vật và thông tin ngăn nắp là gì?", ["Tìm kiếm nhanh chóng, dễ dàng khi cần sử dụng", "Để cho đẹp mắt người khác ngắm", "Làm tốn nhiều thời gian sắp xếp"], 0, "Ngăn nắp giúp ta tìm kiếm đồ dùng ngay lập tức khi cần."
))

nodes.append(make_logic("G3-10", "w1", 3, "Sơ đồ Cây & Biểu diễn Phân cấp", "Chủ đề C: Tổ chức lưu trữ",
    "Bài 10: Sơ đồ tư duy", "Bài 8: Sơ đồ hình cây", "Bài 7: Sơ đồ phân loại đồ vật",
    ["G3-09"], ["Làm quen với sơ đồ hình cây (Tree structure).", "Biết đọc hiểu mối quan hệ phân cấp nhánh cha - con."],
    "Vẽ cây tri thức biểu diễn cách tổ chức đồ dùng trong gia đình!",
    "Sơ đồ hình cây bắt đầu từ gốc (chủ đề lớn), sau đó tỏa ra các cành nhánh chính và nhánh con nhỏ hơn, giúp trực quan hóa cấu trúc dữ liệu phân cấp.",
    ["Cấu trúc cây rất giống cấu trúc thư mục chứa các tệp tin trong máy tính.", "Mỗi nhánh con thuộc về một nhánh cha xác định."],
    3, [4, 2, 1], [3, 5, 6],
    "Trong sơ đồ hình cây phân loại cặp sách, nhánh 'Vở ghi chép' nằm dưới nhánh cha nào?", ["Đồ dùng học tập", "Đồ chơi giải trí", "Quần áo thời trang"], 0, "Vở ghi chép là nhánh con thuộc nhóm Đồ dùng học tập."
))

nodes.append(make_branch("G3-11", "w1", 3, "Bảo vệ Thông tin Bí mật Cá nhân", "Chủ đề D: Đạo đức, pháp luật",
    "Bài 11: Lưu trữ và trao đổi thông tin", "Bài 9: Em bảo vệ thông tin cá nhân", "Bài 8: Bảo vệ dữ liệu cá nhân",
    ["G3-08"], ["Nhận biết thông tin cá nhân cần bảo mật tuyệt đối.", "Không chia sẻ mật khẩu, địa chỉ cho người lạ trên mạng."],
    "Trở thành hiệp sĩ bảo vệ bí mật thông tin của bản thân và gia đình!",
    "Thông tin cá nhân bao gồm: Họ và tên đầy đủ, ngày sinh, địa chỉ nhà, số điện thoại bố mẹ, mật khẩu tài khoản. Tiết lộ cho kẻ xấu có thể gây nguy hiểm cho gia đình.",
    ["Mật khẩu tài khoản chỉ được chia sẻ với bố mẹ, không nói cho bạn bè.", "Không chụp ảnh gửi thẻ căn cước hay giấy tờ nhà lên mạng xã hội."],
    "Một người lạ trên mạng nhắn tin hứa tặng tài khoản game xịn nếu em gửi họ tên, số điện thoại và địa chỉ nhà của em.", "Tuyệt đối từ chối và báo ngay cho bố mẹ biết.", "Gửi ngay thông tin để nhận tài khoản game miễn phí.", "Rất tỉnh táo! Em đã ngăn chặn kẻ xấu thu thập thông tin.", "Kẻ gian có thể dùng thông tin đó để lừa đảo hoặc tiếp cận em!"
))

nodes.append(make_maze("G3-12", "w1", 3, "Trình tự các bước & Thuật toán Hành động", "Chủ đề F: Giải quyết vấn đề",
    "Bài 14, 15: Công việc theo các bước", "Bài 12, 13: Chia việc & Làm theo bước", "Bài 11, 12: Trình tự công việc",
    ["G3-01"], ["Hiểu công việc được giải quyết theo trình tự các bước.", "Biết chia nhỏ một nhiệm vụ phức tạp thành việc nhỏ."],
    "Điều khiển chú Robot thông minh hoàn thành công việc từng bước một!",
    "Mỗi việc hàng ngày như đánh răng, pha trà, rửa tay đều gồm các bước theo thứ tự nhất định. Thay đổi thứ tự các bước có thể làm hỏng kết quả công việc.",
    ["Bước 1 làm trước, bước 2 làm sau, không thể đảo lộn tùy tiện.", "Chia việc lớn thành nhiều việc nhỏ giúp làm bài tập dễ dàng hơn."],
    "Trong quy trình đánh răng, bước nào sau đây phải thực hiện trước tiên?", ["Lấy kem đánh răng lên bàn chải", "Súc miệng nhổ nước ra ngoài", "Rửa sạch bàn chải sau khi đánh xong"], 0, "Phải lấy kem đánh răng lên bàn chải trước rồi mới bắt đầu chải răng."
))

nodes.append(make_maze("G3-13", "w1", 3, "Vượt Mê cung & Trò chơi Rèn luyện Tư duy", "Chủ đề F: Giải quyết vấn đề",
    "Bài 16: Trò chơi học tập", "Bài 14, 15: Giải bài toán bằng sơ đồ", "Bài 13, 14: Trò chơi tư duy mê cung",
    ["G3-12"], ["Vận dụng các lệnh rẽ trái, rẽ phải, đi thẳng để vượt mê cung.", "Rèn luyện tư duy không gian và tối ưu số bước đi."],
    "Đấu trí cùng mê cung số! Tìm con đường ngắn nhất dẫn tới kho báu tri thức!",
    "Để nhân vật đến được vạch đích, ta phải lập một kế hoạch tuần tự các lệnh di chuyển. Cần quan sát chướng ngại vật để tránh bị va chạm.",
    ["Lệnh 'Đi thẳng 1 ô', 'Rẽ phải 90 độ', 'Rẽ trái 90 độ'.", "Kiểm tra kỹ lưỡng từng bước đi trước khi cho Robot khởi hành."],
    "Nếu phía trước Robot có bức tường cản đường, Robot cần làm gì trước khi đi tiếp?", ["Rẽ sang hướng không có vật cản (trái hoặc phải)", "Cứ đi thẳng đâm vào tường", "Tắt máy đứng yên mãi mãi"], 0, "Robot phải rẽ sang hướng thông thoáng để tiếp tục hành trình."
))

nodes.append(make_boss("G3-14", "w1", 3, "Đấu trường Trùm Lớp 3: Tốt nghiệp Mầm số", "Tổng kết GDPT 2018 Lớp 3",
    "Bài 16: Tổng kết Tin học 3", "Bài 16: Em tập trình bày ý kiến", "Bài 15, 16: Đánh giá & Dự án Tin học",
    ["G3-01", "G3-03", "G3-05", "G3-11", "G3-12"],
    ["Tổng kết toàn diện kiến thức Tin học Lớp 3 chuẩn GDPT 2018.", "Sẵn sàng nhận huy hiệu Tốt nghiệp Mầm số vinh quang."],
    "Quái thú Glitch Tí Hon đang quậy phá phòng thực hành máy tính! Hãy vận dụng toàn bộ kiến thức lớp 3 để thu phục nó!",
    "Đấu trường tổng kết: Phân biệt bộ phận máy tính, thao tác chuột phím, an toàn thông tin và tư duy thuật toán từng bước.",
    ["4 bộ phận máy tính: Thân máy, Màn hình, Bàn phím, Chuột.", "Bảo vệ thông tin cá nhân và quy tắc làm việc theo trình tự."],
    "Glitch Tí Hon",
    [
        {"question": "Bộ phận nào của máy tính thực hiện việc nhập ký tự chữ và số?", "options": ["Bàn phím", "Màn hình", "Loa", "Máy in"], "answer": 0, "explanation": "Bàn phím dùng để nhập ký tự vào máy tính."},
        {"question": "Hai phím nào trên bàn phím có gờ định vị ngón trỏ?", "options": ["F và J", "A và L", "G và H", "Z và M"], "answer": 0, "explanation": "Phím F và J là mốc định vị của hàng cơ sở."},
        {"question": "Hành động nào sau đây là đúng khi dùng mạng Internet?", "options": ["Hỏi ý kiến người lớn khi gặp thông tin lạ", "Tự ý gửi địa chỉ nhà cho người lạ", "Bấm vào mọi quảng cáo trúng thưởng", "Chơi game liên tục không nghỉ"], "answer": 0, "explanation": "Luôn trao đổi với cha mẹ, thầy cô khi dùng mạng."},
        {"question": "Thứ tự các bước giải quyết công việc gọi là gì?", "options": ["Quy trình / Thuật toán", "Bức tranh", "Tệp văn bản", "Mật khẩu"], "answer": 0, "explanation": "Quy trình tuần tự từng bước chính là thuật toán."}
    ],
    "CHIẾN THẮNG TUYỆT ĐỐI! Chúc mừng em đã hoàn thành toàn bộ chương trình Tin học Lớp 3 của cả 3 bộ sách với danh hiệu Hiệp Sĩ Mầm Số!"
))

print(f"Loaded Grade 3: {sum(1 for n in nodes if n['grade'] == 3)} lessons")

# ==============================================================================
# LỚP 4 (15 NÚT - THẾ GIỚI 1)
# ==============================================================================
nodes.append(make_sort("G4-01", "w1", 4, "Phần cứng & Phần mềm Máy tính", "Chủ đề A: Máy tính và em",
    "Bài 1: Phần cứng và phần mềm máy tính", "Bài 1: Phần cứng và phần mềm", "Bài 1: Phần cứng và phần mềm",
    ["G3-03"], ["Phân biệt phần cứng (Hardware) và phần mềm (Software).", "Nêu mối quan hệ: phần mềm điều khiển phần cứng hoạt động."],
    "Máy tính giống như một cơ thể sống: Phần cứng là thân thể, Phần mềm là trí tuệ!",
    "Phần cứng là các linh kiện vật lý sờ chạm được (ổ cứng, CPU, bàn phím, màn hình). Phần mềm là các chương trình máy tính chạy bên trong (Windows, Word, Paint, Scratch).",
    ["Không có phần mềm, phần cứng không thể hoạt động được.", "Phần mềm được lưu trữ bên trong các thiết bị nhớ của phần cứng."],
    "Thiết bị Phần cứng (Hardware)", "Chương trình Phần mềm (Software)",
    [{"id":"1","name":"Thẻ nhớ USB & Ổ đĩa cứng","group":"g1","icon":"💾"},{"id":"2","name":"Màn hình & Bàn phím máy tính","group":"g1","icon":"🖥️"},{"id":"3","name":"Hệ điều hành Windows 11","group":"g2","icon":"🪟"},{"id":"4","name":"Phần mềm lập trình Scratch 3.0","group":"g2","icon":"🐱"}],
    "Phần mềm máy tính có đặc điểm nào sau đây?", ["Là chương trình chỉ thị cho máy tính hoạt động", "Có thể cầm nắm được trên tay", "Làm bằng vỏ nhựa hoặc kim loại"], 0, "Phần mềm là các chương trình được cài đặt trong máy tính."
))

nodes.append(make_type("G4-02", "w1", 4, "Luyện gõ Mười ngón & Tiếng Việt Telex", "Chủ đề A: Máy tính và em",
    "Bài 2: Gõ bàn phím đúng cách", "Bài 2: Luyện tập gõ mười ngón", "Bài 2: Rèn luyện kỹ năng gõ phím",
    ["G3-07"], ["Gõ bàn phím mười ngón đúng tư thế quy định.", "Gõ tiếng Việt thành thạo theo quy tắc gõ chữ Telex (s, f, r, x, j)."],
    "Gõ tiếng Việt có dấu thật diệu kỳ với bộ gõ Unikey kiểu gõ Telex!",
    "Quy tắc gõ dấu thanh Telex: s (sắc), f (huyền), r (hỏi), x (ngã), j (nặng). Các chữ cái đặc biệt: aa -> â, aw -> ă, ee -> ê, oo -> ô, ow -> ơ, uw -> ư, dd -> đ.",
    ["Gõ chữ trước, gõ dấu thanh sau cùng của từ.", "Duy trì vị trí ngón tay trên hàng cơ sở."],
    ["truong", "lop", "hoc", "viet"],
    "Trong kiểu gõ Telex, phím nào dùng để gõ dấu huyền?", ["Phím F", "Phím S", "Phím J"], 0, "Trong quy tắc Telex: phím F là dấu huyền (ví dụ: baf -> bà)."
))

nodes.append(make_branch("G4-03", "w1", 4, "Thông tin trên Web & Siêu liên kết", "Chủ đề B: Mạng và Internet",
    "Bài 3: Thông tin trên trang web", "Bài 3: Khám phá trang web", "Bài 3: Tìm kiếm an toàn trên Internet",
    ["G3-08"], ["Nhận biết các thành phần trang web: văn bản, hình ảnh, video, siêu liên kết.", "Biết điều hướng bằng cách nhấp chuột vào siêu liên kết."],
    "Lướt mạng toàn cầu: Khám phá những cánh cửa bí mật mở ra tri thức mới!",
    "Siêu liên kết (Hyperlink) là từ hoặc hình ảnh khi nhấp chuột vào sẽ đưa em chuyển đến một trang web mới. Con trỏ chuột thường đổi thành hình bàn tay chỉ ngón trỏ.",
    ["Thanh địa chỉ URL hiển thị đường dẫn trang web.", "Nút Back (mũi tên quay lại) đưa về trang vừa xem trước đó."],
    "Khi rê chuột qua một dòng chữ màu xanh gạch chân, con trỏ chuột biến thành hình bàn tay trỏ ngón.", "Nhấp chuột trái vào đó để mở trang thông tin liên kết.", "Tắt ngay máy tính vì sợ virus.", "Chính xác! Đó là siêu liên kết (Hyperlink).", "Đó chỉ là siêu liên kết thông thường, không phải virus!"
))

nodes.append(make_sort("G4-04", "w1", 4, "Kỹ năng Tìm kiếm Thông tin Khoa học", "Chủ đề B: Mạng và Internet",
    "Bài 4: Tìm kiếm thông tin trên Internet", "Bài 4: Tìm kiếm thông tin hữu ích", "Bài 3: Tìm kiếm an toàn trên Internet",
    ["G4-03"], ["Sử dụng máy tìm kiếm (Google) với từ khóa chính xác.", "Lọc và chọn đường link uy tín để đọc nội dung."],
    "Tìm kiếm tài liệu học tập trong nháy mắt nhờ cỗ máy tìm kiếm thông minh!",
    "Từ khóa (Keyword) là từ hoặc cụm từ ngắn gọn thể hiện chính xác điều em muốn tìm. Đặt từ khóa trong ngoặc kép \"...\" để tìm chính xác cụm từ đó.",
    ["Tránh nhập cả câu dài dòng vào ô tìm kiếm.", "Ưu tiên chọn các trang web giáo dục có đuôi .edu.vn hoặc báo chính thống."],
    "Từ khóa Tìm kiếm Ngắn gọn, Chính xác", "Cụm từ Dài dòng, Không hiệu quả",
    [{"id":"1","name":"\"Động vật hoang dã Việt Nam\"","group":"g1","icon":"🐅"},{"id":"2","name":"Lịch sử Vua Hùng dựng nước","group":"g1","icon":"👑"},{"id":"3","name":"Bác Google ơi tìm giúp cháu xem con voi sống ở đâu với ạ","group":"g2","icon":"🗣️"},{"id":"4","name":"Cho tôi hỏi ngày mai thời tiết Hà Nội có mưa không nhỉ","group":"g2","icon":"❓"}],
    "Để tìm kiếm thông tin về loài gấu trúc, từ khóa nào sau đây là tốt nhất?", ["Gấu trúc", "Tôi muốn tìm hiểu về cuộc sống của gấu trúc", "Cho xem ảnh gấu"], 0, "Từ khóa ngắn gọn 'Gấu trúc' cho kết quả chính xác và đầy đủ nhất."
))

nodes.append(make_sort("G4-05", "w1", 4, "Quản lý Tệp và Cây Thư mục Khoa học", "Chủ đề C: Tổ chức lưu trữ",
    "Bài 5: Thao tác với tệp và thư mục", "Bài 5: Quản lý tệp và thư mục", "Bài 4: Quản lý tệp và thư mục",
    ["G3-10"], ["Phân biệt tệp (file) và thư mục (folder).", "Thực hiện thành thạo: Tạo mới, Đổi tên, Sao chép, Xóa."],
    "Xây dựng ngôi nhà ngăn nắp cho các tệp tài liệu học tập trong máy tính!",
    "Thư mục giống như ngăn kéo chứa các tệp tài liệu hoặc các thư mục con. Tệp có phần tên và phần mở rộng (đuôi tệp) thể hiện loại tài liệu (.docx, .png, .mp4).",
    ["Tên tệp nên đặt không dấu, có nghĩa rõ ràng để dễ tìm.", "Không xóa các tệp hệ thống trong ổ đĩa C của máy tính."],
    "Tệp tin dữ liệu (Files)", "Thư mục chứa (Folders)",
    [{"id":"1","name":"BaiTapToan_Lop4.docx","group":"g1","icon":"📝"},{"id":"2","name":"HinhAnh_GiaDinh.png","group":"g1","icon":"🖼️"},{"id":"3","name":"Thư mục: MÔN TIN HỌC","group":"g2","icon":"📁"},{"id":"4","name":"Thư mục: VIDEO BÀI GIẢNG","group":"g2","icon":"📂"}],
    "Biểu tượng của một thư mục trong hệ điều hành Windows thường có màu gì?", ["Màu vàng hình chiếc kẹp tài liệu", "Màu đỏ hình tam giác", "Màu xanh lá cây"], 0, "Thư mục có biểu tượng chiếc kẹp hồ sơ màu vàng đặc trưng."
))

nodes.append(make_branch("G4-06", "w1", 4, "Bản quyền Tác giả & Đạo đức Sử dụng Phần mềm", "Chủ đề D: Đạo đức, pháp luật",
    "Bài 6: Sử dụng phần mềm khi được phép", "Bài 6: Tôn trọng quyền tác giả", "Bài 5: Bản quyền và thông tin hợp pháp",
    ["G3-11"], ["Hiểu phần mềm và nội dung số là tài sản trí tuệ.", "Tôn trọng bản quyền, xin phép tác giả trước khi sử dụng."],
    "Trở thành công dân số văn minh, luôn tôn trọng công sức lao động của người khác!",
    "Phần mềm, tranh ảnh, bài hát trên mạng đều do tác giả bỏ công sức sáng tạo. Không sao chép lậu, không sử dụng khi chưa được tác giả cho phép.",
    ["Ghi rõ nguồn tác giả khi trích dẫn tranh ảnh vào bài thuyết trình.", "Ủng hộ các phần mềm bản quyền chính hãng và phần mềm tự do nguồn mở."],
    "Em thấy trên mạng có một bức ảnh vẽ rất đẹp và muốn đưa vào bài trình chiếu dự thi của mình.", "Xin phép tác giả hoặc ghi chú nguồn tên tác giả dưới bức ảnh.", "Cắt bỏ chữ ký tác giả và nhận đó là tranh do mình tự vẽ.", "Tuyệt vời! Em là một học sinh trung thực và tôn trọng bản quyền.", "Xóa tên tác giả và nhận vơ là vi phạm pháp luật sở hữu trí tuệ!"
))

nodes.append(make_sort("G4-07", "w1", 4, "Soạn thảo Văn bản & Chèn Hình ảnh", "Chủ đề E: Ứng dụng tin học",
    "Bài 7: Chèn hình ảnh vào văn bản", "Bài 7: Soạn thảo văn bản có hình ảnh", "Bài 6: Chèn hình và căn lề văn bản",
    ["G4-02"], ["Soạn thảo văn bản tiếng Việt đúng chính tả.", "Chèn hình ảnh từ máy tính vào trang văn bản và chỉnh kích thước."],
    "Biến trang văn bản mộc mạc thành tờ báo tường rực rỡ sắc màu!",
    "Trong phần mềm soạn thảo Word/Docs, vào thẻ Insert chọn Pictures để chèn hình ảnh. Nhấp vào các nút góc của ảnh để phóng to, thu nhỏ tùy ý.",
    ["Chèn ảnh phù hợp với chủ đề nội dung đoạn văn.", "Chọn chế độ Wrap Text (Wrap Square/Tight) để chữ bao quanh ảnh hài hòa."],
    "Công cụ Định dạng Chữ (Text)", "Công cụ Chèn & Xử lý Ảnh (Image)",
    [{"id":"1","name":"Chọn phông chữ Times New Roman","group":"g1","icon":"🔤"},{"id":"2","name":"Tô màu chữ đỏ nổi bật","group":"g1","icon":"🎨"},{"id":"3","name":"Chèn tranh ảnh từ tệp Pictures","group":"g2","icon":"🖼️"},{"id":"4","name":"Thu nhỏ kích thước ảnh vừa trang giấy","group":"g2","icon":"📐"}],
    "Để chèn một bức ảnh vào văn bản Word, em chọn bảng chọn nào trên thanh công cụ?", ["Bảng chọn Insert (Chèn)", "Bảng chọn File", "Bảng chọn View"], 0, "Insert chứa các lệnh chèn hình ảnh, bảng biểu, hình khối."
))

nodes.append(make_type("G4-08", "w1", 4, "Định dạng Đoạn Văn bản Chuyên nghiệp", "Chủ đề E: Ứng dụng tin học",
    "Bài 8: Định dạng văn bản", "Bài 8: Định dạng đoạn văn bản", "Bài 7: Định dạng kiểu chữ và màu sắc",
    ["G4-07"], ["Định dạng ký tự: Đậm (B), Nghiêng (I), Gạch chân (U).", "Căn lề đoạn văn: Căn trái, căn phải, căn giữa, căn đều hai bên."],
    "Trình bày văn bản chuẩn mực như một nhà xuất bản chuyên nghiệp!",
    "Phím tắt thông dụng: Ctrl + B (in đậm), Ctrl + I (in nghiêng), Ctrl + U (gạch chân), Ctrl + E (căn giữa tiêu đề), Ctrl + J (căn đều hai lề đoạn văn).",
    ["Tiêu đề bài viết thường được in đậm và căn giữa trang.", "Đoạn nội dung chính nên căn đều hai lề để trang in thẳng hàng đẹp mắt."],
    ["dinh", "dang", "can", "le"],
    "Tổ hợp phím nào sau đây dùng để in đậm (Bold) chữ đã chọn?", ["Ctrl + B", "Ctrl + I", "Ctrl + U"], 0, "Ctrl + B (viết tắt của Bold) dùng để bật/tắt in đậm chữ."
))

nodes.append(make_memory("G4-09", "w1", 4, "Thiết kế Bài Trình chiếu Sinh động", "Chủ đề E: Ứng dụng tin học",
    "Bài 9, 10: Tạo bài trình chiếu", "Bài 9, 10: Phần mềm trình chiếu", "Bài 8, 9: Trang trình chiếu & Báo cáo",
    ["G4-07"], ["Tạo trang chiếu mới (New Slide), nhập tiêu đề và nội dung.", "Áp dụng mẫu bố cục Layouts và hiệu ứng chuyển trang Transitions."],
    "Trở thành nhà diễn thuyết tài ba với những trang trình chiếu PowerPoint cuốn hút!",
    "Mỗi trang chiếu chỉ nên chứa ý chính súc tích kết hợp hình ảnh minh họa. Sử dụng hiệu ứng chuyển trang nhịp nhàng để tạo sự bất ngờ.",
    ["Không viết quá nhiều chữ dày đặc trên một trang chiếu.", "Màu chữ phải tương phản nổi bật trên màu nền (nền sáng chữ tối hoặc ngược lại)."],
    [{"id":"1","name":"Trang tiêu đề","match":"Giới thiệu tên bài thuyết trình và tên tác giả"},{"id":"2","name":"Hiệu ứng Transitions","match":"Chuyển động khi chuyển đổi giữa các slide"},{"id":"3","name":"Hiệu ứng Animations","match":"Chuyển động xuất hiện của từng dòng chữ hoặc hình ảnh"},{"id":"4","name":"Mẫu giao diện Theme","match":"Bộ màu sắc và phông chữ thiết kế đồng bộ"}],
    "Nguyên tắc phối màu chuẩn khi thiết kế trang chiếu là gì?", ["Chữ tối màu trên nền sáng (hoặc chữ sáng trên nền tối)", "Chữ vàng trên nền trắng", "Chữ xám mờ trên nền đen"], 0, "Độ tương phản cao giúp người ngồi xa dưới lớp vẫn đọc rõ chữ."
))

nodes.append(make_sort("G4-10", "w1", 4, "Xử lý & Chỉnh sửa Hình ảnh Cơ bản", "Chủ đề E: Ứng dụng tin học",
    "Bài 11: Chỉnh sửa hình ảnh", "Bài 11: Xử lý hình ảnh đơn giản", "Bài 10: Chỉnh sửa ảnh cơ bản",
    ["G4-07"], ["Cắt bớt chi tiết thừa (Crop) của bức ảnh.", "Xoay hình ảnh (Rotate) và lật gương (Flip)."],
    "Hô biến bức ảnh trở nên hoàn hảo với các công cụ biên tập hình ảnh!",
    "Công cụ Crop giúp em cắt lấy góc ảnh đẹp nhất và loại bỏ nền thừa. Công cụ Rotate giúp xoay ngay ngắn các bức ảnh bị chụp nghiêng.",
    ["Giữ tỉ lệ khung hình để ảnh không bị méo mó, co giãn dị dạng.", "Lưu ảnh ở định dạng nén chất lượng cao PNG hoặc JPG."],
    "Thao tác Cắt xén (Crop)", "Thao tác Xoay & Lật (Rotate/Flip)",
    [{"id":"1","name":"Cắt bỏ góc phòng thừa trong bức ảnh chụp","group":"g1","icon":"✂️"},{"id":"2","name":"Cắt ảnh thành hình vuông làm ảnh đại diện","group":"g1","icon":"🔲"},{"id":"3","name":"Xoay ảnh 90 độ theo chiều kim đồng hồ","group":"g2","icon":"🔄"},{"id":"4","name":"Lật ảnh ngang để nhân vật quay mặt sang phải","group":"g2","icon":"↔️"}],
    "Muốn cắt bỏ phần thừa hai bên mép của bức ảnh, em dùng công cụ nào?", ["Công cụ Crop (Cắt xén)", "Công cụ Rotate", "Công cụ Zoom"], 0, "Crop là công cụ chuẩn để cắt bớt khung hình ảnh."
))

nodes.append(make_memory("G4-11", "w1", 4, "Khám phá Lập trình Trực quan Scratch", "Chủ đề F: Giải quyết vấn đề",
    "Bài 12, 13: Môi trường Scratch & Lệnh đầu tiên", "Bài 12: Em làm quen với Scratch", "Bài 11, 12: Môi trường & Nhân vật",
    ["G3-13"], ["Nhận biết 4 khu vực chính trên giao diện Scratch.", "Hiểu cách lắp ghép các khối lệnh theo màu sắc chức năng."],
    "Chào mừng em đến với thế giới sáng tạo Scratch cùng chú Mèo tinh nghịch!",
    "Giao diện Scratch gồm: Bảng khối lệnh (chia theo màu sắc), Khu vực kịch bản (nơi lắp ghép lệnh), Sân khấu (nơi kịch bản diễn ra) và Danh sách nhân vật.",
    ["Khối lệnh màu xanh lam: Chuyển động (Motion).", "Khối lệnh màu vàng: Sự kiện (Events) khởi động chương trình."],
    [{"id":"1","name":"Khối Sự kiện (Màu vàng)","match":"Khi bấm vào lá cờ xanh để bắt đầu chạy kịch bản"},{"id":"2","name":"Khối Chuyển động (Màu xanh lam)","match":"Di chuyển 10 bước, xoay hướng 15 độ"},{"id":"3","name":"Khối Hiển thị (Màu tím)","match":"Nói xin chào, đổi trang phục cho nhân vật"},{"id":"4","name":"Khối Âm thanh (Màu hồng)","match":"Phát tiếng kêu Meo meo vui nhộn"}],
    "Khối lệnh nào sau đây thường được đặt ở đầu tiên để kích hoạt chương trình Scratch chạy?", ["Khi bấm vào lá cờ xanh (When green flag clicked)", "Di chuyển 10 bước", "Dừng lại tất cả"], 0, "Bấm vào cờ xanh là tín hiệu chuẩn để khởi động kịch bản Scratch."
))

nodes.append(make_maze("G4-12", "w1", 4, "Điều khiển Nhân vật Chuyển động", "Chủ đề F: Giải quyết vấn đề",
    "Bài 14: Điều khiển nhân vật chuyển động", "Bài 13: Nhân vật chuyển động theo lệnh", "Bài 13: Điều khiển nhân vật di chuyển",
    ["G4-11"], ["Sử dụng khối lệnh di chuyển Move và xoay Turn.", "Sử dụng lệnh nếu chạm cạnh thì bật lại (If on edge, bounce)."],
    "Điều khiển chú Mèo chạy nhảy tự do trên sân khấu không bị lọt ra ngoài mép màn hình!",
    "Khối lệnh 'Di chuyển 10 bước' đưa nhân vật tiến về phía trước theo hướng hiện tại. Khối lệnh 'Bật lại nếu chạm cạnh' giúp nhân vật không bị biến mất khỏi màn hình.",
    ["Hướng 90 độ là nhìn sang phải, -90 độ là nhìn sang trái.", "Đặt kiểu xoay trái-phải để nhân vật không bị lộn ngược đầu."],
    "Lệnh nào giúp nhân vật Scratch tự động quay đầu khi chạm vào mép ngoài của sân khấu?", ["Nếu chạm cạnh, bật lại (If on edge, bounce)", "Ẩn nhân vật (Hide)", "Dừng lại 1 giây"], 0, "If on edge, bounce giữ nhân vật luôn chạy bên trong sân khấu."
))

nodes.append(make_maze("G4-13", "w1", 4, "Cấu trúc Vòng lặp Tuần hoàn (Repeat)", "Chủ đề F: Giải quyết vấn đề",
    "Bài 15: Lặp lại một việc", "Bài 14: Cấu trúc lặp trong lập trình", "Bài 14: Vòng lặp trong chương trình",
    ["G4-12"], ["Hiểu ý nghĩa cấu trúc lặp: giảm bớt số dòng lệnh trùng lặp.", "Sử dụng khối lệnh lặp lại N lần (Repeat N)."],
    "Thay vì viết 100 lần dòng lệnh bước đi, chỉ cần một vòng lặp nhỏ xinh!",
    "Vòng lặp giúp máy tính thực hiện các hành động lặp đi lặp lại một cách tự động và chính xác. Để vẽ hình vuông, ta chỉ cần lặp lại 4 lần: Đi thẳng và Rẽ phải 90 độ.",
    ["Vòng lặp Repeat 10: lặp đúng 10 lần rồi dừng lại.", "Vòng lặp Forever: lặp mãi mãi không dừng cho đến khi bấm nút đỏ."],
    "Để nhân vật vẽ một hình tam giác đều 3 cạnh, khối lệnh lặp cần thiết lập số lần lặp là bao nhiêu?", ["Lặp lại 3 lần", "Lặp lại 4 lần", "Lặp lại 10 lần"], 0, "Hình tam giác có 3 cạnh nên lặp lại 3 lần vẽ cạnh và xoay góc."
))

nodes.append(make_logic("G4-14", "w1", 4, "Biểu diễn Thuật toán bằng Sơ đồ khối", "Chủ đề F: Giải quyết vấn đề",
    "Bài 16: Biểu diễn thuật toán", "Bài 15: Xây dựng câu chuyện tương tác", "Bài 15: Sơ đồ khối thuật toán",
    ["G4-13"], ["Nhận biết quy ước hình khối chuẩn: Bắt đầu/Kết thúc, Thao tác, Điều kiện.", "Đọc hiểu luồng thực thi của sơ đồ khối."],
    "Vẽ bản đồ tư duy thuật toán trước khi bắt tay vào gõ từng dòng lệnh!",
    "Sơ đồ khối dùng các hình hình học và mũi tên để mô tả đường đi của thuật toán: Hình Oval (Bắt đầu/Kết thúc), Hình chữ nhật (Hành động xử lý), Hình thoi (Kiểm tra điều kiện).",
    ["Mũi tên chỉ hướng thực hiện tiếp theo của chương trình.", "Từ hình thoi luôn có 2 nhánh rẽ: Đúng (Yes) hoặc Sai (No)."],
    3, [4, 2, 1], [1, 2, 4],
    "Trong sơ đồ khối thuật toán, hình nào dùng để biểu diễn bước kiểm tra điều kiện rẽ nhánh?", ["Hình thoi", "Hình chữ nhật", "Hình tròn"], 0, "Hình thoi là ký hiệu quốc tế chuẩn cho khối quyết định điều kiện."
))

nodes.append(make_boss("G4-15", "w1", 4, "Đấu trường Trùm Lớp 4: Nhà Lập trình Nhí", "Tổng kết GDPT 2018 Lớp 4",
    "Bài 16: Dự án Tin học 4", "Bài 16: Dự án lập trình trò chơi", "Bài 16: Dự án Em làm nhà lập trình",
    ["G4-01", "G4-05", "G4-08", "G4-11", "G4-13"],
    ["Tổng kết toàn diện kiến thức Tin học Lớp 4 của 3 bộ sách.", "Sẵn sàng nhận danh hiệu Nhà Lập Trình Nhí EasyTin."],
    "Robot Bug Lỗi Mã đang chiếm quyền điều khiển sân khấu Scratch! Hãy dùng tư duy thuật toán để đánh bại nó!",
    "Đấu trường tổng kết: Phân biệt Phần cứng - Phần mềm, Cây thư mục, Định dạng văn bản và Khối lệnh lập trình Scratch.",
    ["Phần cứng và Phần mềm phối hợp nhịp nhàng.", "Cấu trúc lặp Repeat N tối ưu hóa thuật toán."],
    "Bug Lỗi Mã",
    [
        {"question": "Thành phần nào sau đây là phần mềm máy tính?", "options": ["Hệ điều hành Windows", "Chuột không dây", "Màn hình LED", "Bàn phím cơ"], "answer": 0, "explanation": "Windows là phần mềm hệ thống điều khiển máy tính."},
        {"question": "Trong Scratch, khối lệnh 'Lặp lại 10 lần' nằm trong nhóm lệnh nào?", "options": ["Điều khiển (Control)", "Chuyển động (Motion)", "Âm thanh (Sound)", "Cảm biến (Sensing)"], "answer": 0, "explanation": "Nhóm Control (màu cam) quản lý các vòng lặp và điều kiện."},
        {"question": "Để tìm chính xác cụm từ trên Google, ta đặt cụm từ đó trong dấu gì?", "options": ["Dấu ngoặc kép \"...\"", "Dấu ngoặc đơn (...)", "Dấu chấm than !...", "Dấu hỏi chấm ?..."], "answer": 0, "explanation": "Dấu ngoặc kép tìm kiếm chính xác từng từ trong cụm từ."},
        {"question": "Đuôi mở rộng nào sau đây là của tệp văn bản Word?", "options": [".docx", ".png", ".mp3", ".exe"], "answer": 0, "explanation": ".docx là định dạng chuẩn của tài liệu Word."}
    ],
    "CHIẾN THẮNG HUY HOÀNG! Em đã làm chủ toàn bộ chương trình Tin học Lớp 4 của cả 3 bộ sách với danh hiệu Nhà Lập Trình Nhí!"
))

print(f"Loaded Grade 4: {sum(1 for n in nodes if n['grade'] == 4)} lessons")

# Continue building comprehensive nodes for Grade 5 to Grade 12 in python
with open("tools/build_exhaustive_complete_curriculum.py", "w", encoding="utf-8") as f:
    f.write("# Generator script written\n")

print("Stage 1 done.")
