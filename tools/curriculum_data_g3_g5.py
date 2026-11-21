# -*- coding: utf-8 -*-
"""
Dữ liệu chương trình học EasyTin: Khối Tiểu học (Lớp 3, 4, 5)
Phủ 100% tất cả các bài học và YCCĐ của cả 3 bộ sách: KNTT, Cánh Diều, CTST.
"""

def get_elementary_nodes():
    nodes = []

    def make_lesson(nid, wid, gr, title, domain, kntt, cd, ctst, tmpl, prereqs, mins, goals, hook, summ, pts, gcfg, quiz, recap):
        return {
            "id": nid, "world_id": wid, "grade": gr, "title": title, "standard_domain": domain,
            "textbook_mapping": {"kntt": kntt, "canhdieu": cd, "ctst": ctst},
            "template": tmpl, "prerequisites": prereqs, "estimated_minutes": mins, "learning_goals": goals,
            "lesson_data": {
                "hook": hook,
                "concept": {"summary": summ, "key_points": pts},
                "game_config": gcfg,
                "quiz": quiz,
                "recap": recap
            }
        }

    # =========================================================================
    # LỚP 3 (14 NÚT)
    # =========================================================================
    nodes.append(make_lesson(
        "G3-01", "w1", 3, "Thông tin và Quyết định Cuộc sống", "Chủ đề A: Máy tính và em",
        "Bài 1: Thông tin và quyết định", "Bài 1: Em làm quen với máy tính", "Bài 1: Thông tin và tiếp nhận thông tin",
        "branch-story", [], 6,
        ["Nhận biết thông tin thu nhận qua các giác quan.", "Hiểu thông tin giúp con người đưa ra quyết định phù hợp."],
        "Buổi sáng bước ra cửa, em nhìn thấy trời nhiều mây đen và nghe tiếng sấm chớp ầm ầm. Em sẽ quyết định thế nào?",
        "Thông tin là những điều em nhìn thấy, nghe thấy hoặc cảm nhận được từ thế giới xung quanh. Nhờ có thông tin, con người đưa ra các quyết định hành động phù hợp.",
        ["Mắt nhìn thấy, tai nghe thấy đều mang lại thông tin hữu ích.", "Quyết định đúng đắn dựa trên thông tin chính xác."],
        {"scenarios": [{"id": "s1", "prompt": "Trời bắt đầu đổ mưa rào khi em chuẩn bị đi học đến trường.", "choices": [{"text": "Mang theo ô (dù) hoặc mặc áo mưa cẩn thận.", "is_correct": True, "feedback": "Rất đúng! Thông tin trời mưa giúp em bảo vệ sức khỏe."}, {"text": "Mặc kệ cứ đi tay không ra ngoài.", "is_correct": False, "feedback": "Em có thể bị ướt và cảm lạnh!"}]}]},
        [{"question": "Giác quan nào giúp em nhìn thấy màu sắc của tín hiệu đèn giao thông?", "options": ["Mắt (Thị giác)", "Tai (Thính giác)", "Mũi (Khứu giác)"], "answer": 0, "explanation": "Mắt giúp ta quan sát và thu nhận thông tin hình ảnh, màu sắc."}],
        "Em đã hiểu rất rõ cách thu nhận thông tin để đưa ra quyết định sáng suốt mỗi ngày!"
    ))

    nodes.append(make_lesson(
        "G3-02", "w1", 3, "Xử lý Thông tin & Các dạng Dữ liệu", "Chủ đề A: Máy tính và em",
        "Bài 2: Xử lý thông tin", "Bài 2: Các bộ phận của máy tính", "Bài 1: Thông tin và tiếp nhận thông tin",
        "sort-drag", ["G3-01"], 6,
        ["Phân biệt 4 bước: Thu nhận -> Lưu trữ -> Xử lý -> Truyền đạt.", "Nhận diện dạng thông tin: Chữ, Hình ảnh, Âm thanh."],
        "Máy tính và con người đều có khả năng tiếp nhận và xử lý thông tin hiệu quả!",
        "Bốn hoạt động thông tin cơ bản gồm: Thu nhận thông tin, Lưu trữ thông tin, Xử lý thông tin và Truyền đạt thông tin.",
        ["Bộ não con người và bộ vi xử lý máy tính đều thực hiện xử lý thông tin.", "Thông tin có thể lưu trữ trong sách vở hoặc ổ đĩa máy tính."],
        {"groups": [{"id": "g1", "name": "Thu nhận thông tin (Đầu vào)"}, {"id": "g2", "name": "Truyền đạt thông tin (Đầu ra)"}], "items": [{"id":"1","name":"Đọc dòng chữ trên bảng lớp","group":"g1","icon":"👀"},{"id":"2","name":"Nghe tiếng chuông báo giờ ra chơi","group":"g1","icon":"🔔"},{"id":"3","name":"Nói lời chào thầy cô","group":"g2","icon":"🗣️"},{"id":"4","name":"Gửi thư báo tin vui cho bạn bè","group":"g2","icon":"✉️"}]},
        [{"question": "Khi em nghe bạn kể một câu chuyện vui rồi bật cười, hoạt động nghe thuộc bước nào?", "options": ["Thu nhận thông tin", "Xử lý thông tin", "Lưu trữ thông tin"], "answer": 0, "explanation": "Tai nghe âm thanh câu chuyện là bước thu nhận thông tin."}],
        "Chúc mừng em đã phân loại chính xác các hoạt động thông tin!"
    ))

    nodes.append(make_lesson(
        "G3-03", "w1", 3, "Khám phá Phần cứng & Bộ phận Máy tính", "Chủ đề A: Máy tính và em",
        "Bài 3: Máy tính - những người bạn mới", "Bài 2: Các bộ phận của máy tính", "Bài 2: Khám phá máy tính",
        "sort-drag", ["G3-01"], 6,
        ["Nhận biết 4 bộ phận cơ bản: Thân máy, Màn hình, Bàn phím, Chuột.", "Hiểu chức năng chính của từng bộ phận."],
        "Gặp gỡ biệt đội máy tính kỳ diệu hỗ trợ việc học tập mỗi ngày!",
        "Máy tính để bàn gồm 4 bộ phận chính: Thân máy (bộ não xử lý), Màn hình (hiển thị kết quả), Bàn phím (nhập chữ và số), Chuột (điều khiển nhanh chóng).",
        ["Thân máy chứa bộ xử lý trung tâm CPU điều khiển mọi hoạt động.", "Màn hình giúp em nhìn thấy chữ, tranh ảnh và video sinh động."],
        {"groups": [{"id": "g1", "name": "Bộ phận Nhập dữ liệu"}, {"id": "g2", "name": "Bộ phận Xuất & Xử lý"}], "items": [{"id":"1","name":"Bàn phím máy tính","group":"g1","icon":"⌨️"},{"id":"2","name":"Chuột máy tính","group":"g1","icon":"🖱️"},{"id":"3","name":"Màn hình hiển thị","group":"g2","icon":"🖥️"},{"id":"4","name":"Thân máy (CPU)","group":"g2","icon":"🧠"}]},
        [{"question": "Bộ phận nào được coi là 'bộ não' điều khiển mọi hoạt động của máy tính?", "options": ["Thân máy tính", "Màn hình", "Bàn phím"], "answer": 0, "explanation": "Thân máy chứa CPU thực hiện các phép tính và chỉ huy máy tính hoạt động."}],
        "Em đã nắm vững chức năng của các bộ phận máy tính!"
    ))

    nodes.append(make_lesson(
        "G3-04", "w1", 3, "Làm việc với Máy tính An toàn", "Chủ đề A: Máy tính và em",
        "Bài 4: Làm việc với máy tính", "Bài 1: Em làm quen với máy tính", "Bài 2: Khám phá máy tính",
        "branch-story", ["G3-03"], 6,
        ["Biết bật và tắt máy tính đúng quy trình an toàn.", "Ngồi đúng tư thế, giữ khoảng cách mắt từ 50-80cm."],
        "Sử dụng máy tính đúng cách giúp em học giỏi và bảo vệ đôi mắt sáng ngời!",
        "Khi ngồi học máy tính, giữ lưng thẳng, mắt ngang tầm màn hình cách từ 50 đến 80 cm. Không cắm rút dây điện khi chưa được người lớn cho phép.",
        ["Tắt máy tính bằng lệnh Start -> Shut down, không tự ý rút phích cắm nguồn.", "Sau 30-45 phút ngồi máy tính, nên đứng dậy vận động nhẹ."],
        {"scenarios": [{"id": "s1", "prompt": "Em học xong bài tập vẽ trên máy tính và muốn tắt máy đi ngủ.", "choices": [{"text": "Nhấp chuột vào nút Start chọn lệnh Shut down.", "is_correct": True, "feedback": "Rất chuẩn! Tắt máy đúng cách bảo vệ dữ liệu và hệ điều hành."}, {"text": "Giật phích cắm điện của máy tính ra khỏi ổ cắm tường.", "is_correct": False, "feedback": "Tắt đột ngột có thể làm hỏng máy tính và chập điện nguy hiểm!"}]}]},
        [{"question": "Khoảng cách an toàn từ mắt đến màn hình máy tính là bao nhiêu?", "options": ["Từ 50 cm đến 80 cm (khoảng một sải tay)", "Từ 10 cm đến 20 cm", "Càng gần càng tốt"], "answer": 0, "explanation": "Khoảng cách 50-80cm giúp mắt không bị mỏi và tránh cận thị."}],
        "Em đã là một học sinh gương mẫu khi làm việc với máy tính rất an toàn!"
    ))

    nodes.append(make_lesson(
        "G3-05", "w1", 3, "Luyện tập Thao tác Chuột Máy tính Chuẩn xác", "Chủ đề A: Máy tính và em",
        "Bài 6: Sử dụng chuột máy tính", "Bài 3: Em tập dùng chuột", "Bài 3: Em tập sử dụng chuột",
        "sort-drag", ["G3-03"], 6,
        ["Cầm chuột đúng tư thế bằng tay phải.", "Thực hiện thành thạo 5 thao tác cơ bản với chuột."],
        "Chú chuột máy tính nhỏ bé nhưng có sức mạnh điều khiển phi thường!",
        "Năm thao tác chuột cơ bản gồm: Di chuyển chuột, Nháy chuột (chuột trái), Nháy nút phải chuột, Nháy đúp chuột (nhấp nhanh 2 lần) và Kéo thả chuột.",
        ["Đặt ngón trỏ lên nút chuột trái, ngón giữa lên nút chuột phải.", "Kéo thả chuột dùng để di chuyển biểu tượng trên màn hình."],
        {"groups": [{"id": "g1", "name": "Thao tác Nháy đơn (1 lần)"}, {"id": "g2", "name": "Thao tác Nháy kép / Kéo thả"}], "items": [{"id":"1","name":"Nháy nút trái chuột để chọn thư mục","group":"g1","icon":"👆"},{"id":"2","name":"Nháy nút phải chuột mở thực đơn lệnh","group":"g1","icon":"👉"},{"id":"3","name":"Nháy đúp chuột để khởi động phần mềm","group":"g2","icon":"✌️"},{"id":"4","name":"Kéo thả biểu tượng tệp vào thùng rác","group":"g2","icon":"✋"}]},
        [{"question": "Để mở nhanh một trò chơi trên màn hình máy tính, em dùng thao tác chuột nào?", "options": ["Nháy đúp chuột (nhấp nhanh 2 lần nút trái)", "Nháy chuột phải", "Chỉ di chuyển chuột"], "answer": 0, "explanation": "Nháy đúp nút trái là thao tác mở tệp hoặc phần mềm."}],
        "Kỹ năng sử dụng chuột của em rất khéo léo và chính xác!"
    ))

    nodes.append(make_lesson(
        "G3-06", "w1", 3, "Làm quen Bàn phím & Hàng phím Cơ sở", "Chủ đề A: Máy tính và em",
        "Bài 5: Sử dụng bàn phím", "Bài 4: Em tập gõ hàng phím cơ sở", "Bài 4: Em tập sử dụng bàn phím",
        "type-run", ["G3-03"], 6,
        ["Nhận biết hàng phím cơ sở và hai phím có gờ F, J.", "Đặt đúng 8 ngón tay tại vị trí xuất phát."],
        "Luyện đôi bàn tay lướt phím chuẩn xác như nghệ sĩ đàn piano!",
        "Hàng phím cơ sở là hàng phím quan trọng nhất. Phím F và phím J có gờ nhỏ nổi lên để ngón trỏ đặt vào làm mốc định vị cho hai bàn tay.",
        ["Ngón trỏ tay trái đặt phím F, ngón trỏ tay phải đặt phím J.", "Hai ngón cái phụ trách gõ phím cách Spacebar dài nhất."],
        {"words": ["asdf", "jkl", "fjfj", "dksa"]},
        [{"question": "Hai phím nào trên hàng phím cơ sở có gờ nhô lên để định vị ngón trỏ?", "options": ["Phím F và phím J", "Phím A và phím L", "Phím G và phím H"], "answer": 0, "explanation": "Gờ trên phím F và J giúp ta đặt tay đúng mà không cần nhìn bàn phím."}],
        "Bàn tay em đã đặt đúng các vị trí chuẩn trên hàng phím cơ sở!"
    ))

    nodes.append(make_lesson(
        "G3-07", "w1", 3, "Mở rộng Kỹ năng Gõ mười ngón", "Chủ đề E: Ứng dụng tin học",
        "Bài 12: Em tập gõ bàn phím", "Bài 5: Em tập gõ các hàng phím khác", "Bài 9: Phần mềm luyện gõ phím",
        "type-run", ["G3-06"], 6,
        ["Gõ phím hàng trên (Q W E R T Y U I O P).", "Gõ phím hàng dưới (Z X C V B N M) và phím Enter."],
        "Chinh phục toàn bộ các hàng phím để gõ văn bản nhanh như chớp!",
        "Mỗi ngón tay phụ trách một vùng phím cố định. Sau khi vươn lên hàng trên hoặc đưa xuống hàng dưới, ngón tay luôn quay về nghỉ tại hàng phím cơ sở.",
        ["Phím Shift dùng để viết hoa ký tự.", "Phím Enter dùng để xuống dòng mới."],
        {"words": ["quyet", "viet", "hoc", "tin"]},
        [{"question": "Sau khi vươn ngón tay lên gõ các phím ở hàng trên, ngón tay cần quay về đâu?", "options": ["Quay về hàng phím cơ sở", "Để nguyên ở hàng trên", "Rút tay ra khỏi bàn phím"], "answer": 0, "explanation": "Ngón tay luôn phải trở về hàng phím cơ sở để sẵn sàng cho ký tự tiếp theo."}],
        "Tốc độ gõ phím của em đang tiến bộ vượt bậc từng ngày!"
    ))

    nodes.append(make_lesson(
        "G3-08", "w1", 3, "Khám phá Thế giới Mạng Internet", "Chủ đề B: Mạng và Internet",
        "Bài 7: Khám phá Internet", "Bài 6: Thông tin trên Internet", "Bài 5: Khám phá Internet",
        "branch-story", ["G3-01"], 6,
        ["Hiểu Internet là mạng kết nối máy tính toàn cầu.", "Biết khai thác thông tin bổ ích và tránh thông tin xấu."],
        "Bước vào đại dương tri thức Internet với hàng triệu điều kỳ thú!",
        "Internet kết nối hàng triệu máy tính khắp hành tinh. Em có thể xem video bài học, nghe nhạc, đọc báo thiếu nhi và trò chuyện cùng bạn bè ở xa.",
        ["Chỉ truy cập các trang web học tập lành mạnh phù hợp lứa tuổi thiếu nhi.", "Hỏi ý kiến cha mẹ hoặc thầy cô khi thấy nội dung bất thường."],
        {"scenarios": [{"id": "s1", "prompt": "Khi đang xem video khoa học, bỗng xuất hiện một cửa sổ quảng cáo lạ nhấp nháy đòi bấm vào để nhận quà trúng thưởng lớn.", "choices": [{"text": "Báo ngay cho bố mẹ hoặc thầy cô và đóng trang web đó lại.", "is_correct": True, "feedback": "Rất thông minh! Đó là bẫy lừa đảo quảng cáo độc hại."}, {"text": "Bấm ngay vào để nhận quà vì quà miễn phí rất thích.", "is_correct": False, "feedback": "Bấm vào quảng cáo lạ có thể khiến máy tính bị nhiễm virus nguy hiểm!"}]}]},
        [{"question": "Internet mang lại lợi ích gì cho việc học tập của học sinh?", "options": ["Tra cứu kiến thức, xem bài giảng và hình ảnh bổ ích", "Giúp chơi game cả ngày không cần học", "Làm hỏng mắt và máy tính"], "answer": 0, "explanation": "Internet là kho tàng tri thức khổng lồ giúp mở rộng hiểu biết."}],
        "Em đã biết cách khám phá Internet thông minh và an toàn!"
    ))

    nodes.append(make_lesson(
        "G3-09", "w1", 3, "Sắp xếp Phân loại Đồ vật & Thông tin", "Chủ đề C: Tổ chức lưu trữ",
        "Bài 8, 9: Sắp xếp để dễ tìm", "Bài 7: Sắp xếp đồ vật hợp lí", "Bài 6: Sắp xếp và phân loại thông tin",
        "sort-drag", ["G3-01"], 6,
        ["Biết phân loại đồ vật, tài liệu theo tiêu chí rõ ràng.", "Hiểu lợi ích của sắp xếp ngăn nắp giúp tìm kiếm nhanh."],
        "Cùng dọn dẹp góc học tập và sắp xếp tài liệu ngăn nắp!",
        "Khi đồ vật hoặc thông tin được phân loại theo tiêu chí (màu sắc, công dụng, môn học), em sẽ tìm thấy đồ dùng nhanh chóng mà không mất thời gian tìm kiếm.",
        ["Sắp xếp khoa học giúp tiết kiệm thời gian và rèn luyện tính kỷ luật.", "Dữ liệu trong máy tính cũng được phân loại vào từng thư mục tương tự."],
        {"groups": [{"id": "g1", "name": "Đồ dùng học tập Vẽ mỹ thuật"}, {"id": "g2", "name": "Đồ dùng học tập Môn Toán"}], "items": [{"id":"1","name":"Hộp bút sáp màu 12 màu","group":"g1","icon":"🖍️"},{"id":"2","name":"Tập giấy vẽ trắng A4","group":"g1","icon":"📄"},{"id":"3","name":"Thước kẻ eke đo góc","group":"g2","icon":"📐"},{"id":"4","name":"Compa vẽ hình tròn","group":"g2","icon":"📏"}]},
        [{"question": "Lợi ích lớn nhất của việc sắp xếp đồ vật và thông tin ngăn nắp là gì?", "options": ["Tìm kiếm nhanh chóng, dễ dàng khi cần sử dụng", "Để cho đẹp mắt người khác ngắm", "Làm tốn nhiều thời gian sắp xếp"], "answer": 0, "explanation": "Ngăn nắp giúp ta tìm kiếm đồ dùng ngay lập tức khi cần."}],
        "Góc học tập và dữ liệu của em đã trở nên cực kỳ gọn gàng!"
    ))

    nodes.append(make_lesson(
        "G3-10", "w1", 3, "Sơ đồ Cây & Biểu diễn Phân cấp", "Chủ đề C: Tổ chức lưu trữ",
        "Bài 10: Sơ đồ tư duy", "Bài 8: Sơ đồ hình cây", "Bài 7: Sơ đồ phân loại đồ vật",
        "logic-puzzle", ["G3-09"], 8,
        ["Làm quen với sơ đồ hình cây (Tree structure).", "Biết đọc hiểu mối quan hệ phân cấp nhánh cha - con."],
        "Vẽ cây tri thức biểu diễn cách tổ chức đồ dùng trong gia đình!",
        "Sơ đồ hình cây bắt đầu từ gốc (chủ đề lớn), sau đó tỏa ra các cành nhánh chính và nhánh con nhỏ hơn, giúp trực quan hóa cấu trúc dữ liệu phân cấp.",
        ["Cấu trúc cây rất giống cấu trúc thư mục chứa các tệp tin trong máy tính.", "Mỗi nhánh con thuộc về một nhánh cha xác định."],
        {"bits_count": 3, "weights": [4, 2, 1], "target_values": [3, 5, 6]},
        [{"question": "Trong sơ đồ hình cây phân loại cặp sách, nhánh 'Vở ghi chép' nằm dưới nhánh cha nào?", "options": ["Đồ dùng học tập", "Đồ chơi giải trí", "Quần áo thời trang"], "answer": 0, "explanation": "Vở ghi chép là nhánh con thuộc nhóm Đồ dùng học tập."}],
        "Tư duy phân cấp hình cây của em thật sáng tạo và rõ ràng!"
    ))

    nodes.append(make_lesson(
        "G3-11", "w1", 3, "Bảo vệ Thông tin Bí mật Cá nhân", "Chủ đề D: Đạo đức, pháp luật",
        "Bài 11: Lưu trữ và trao đổi thông tin", "Bài 9: Em bảo vệ thông tin cá nhân", "Bài 8: Bảo vệ dữ liệu cá nhân",
        "branch-story", ["G3-08"], 6,
        ["Nhận biết thông tin cá nhân cần bảo mật tuyệt đối.", "Không chia sẻ mật khẩu, địa chỉ cho người lạ trên mạng."],
        "Chủ động bảo vệ bí mật thông tin của bản thân và gia đình.",
        "Thông tin cá nhân bao gồm: Họ và tên đầy đủ, ngày sinh, địa chỉ nhà, số điện thoại bố mẹ, mật khẩu tài khoản. Tiết lộ cho kẻ xấu có thể gây nguy hiểm cho gia đình.",
        ["Mật khẩu tài khoản chỉ được chia sẻ với bố mẹ, không nói cho bạn bè.", "Không chụp ảnh gửi thẻ căn cước hay giấy tờ nhà lên mạng xã hội."],
        {"scenarios": [{"id": "s1", "prompt": "Một người lạ trên mạng nhắn tin hứa tặng tài khoản game xịn nếu em gửi họ tên, số điện thoại và địa chỉ nhà của em.", "choices": [{"text": "Tuyệt đối từ chối và báo ngay cho bố mẹ biết.", "is_correct": True, "feedback": "Rất tỉnh táo! Em đã ngăn chặn kẻ xấu thu thập thông tin."}, {"text": "Gửi ngay thông tin để nhận tài khoản game miễn phí.", "is_correct": False, "feedback": "Kẻ gian có thể dùng thông tin đó để lừa đảo hoặc tiếp cận em!"}]}]},
        [{"question": "Thông tin nào sau đây TUYỆT ĐỐI không được cung cấp cho người lạ trên mạng?", "options": ["Mật khẩu tài khoản và địa chỉ nhà riêng", "Tên loài hoa em yêu thích", "Màu sắc của bầu trời"], "answer": 0, "explanation": "Mật khẩu và địa chỉ nhà là thông tin bảo mật sống còn."}],
        "Em đã biết cách bảo vệ thông tin an toàn cho bản thân và gia đình!"
    ))

    nodes.append(make_lesson(
        "G3-12", "w1", 3, "Trình tự các bước & Thuật toán Hành động", "Chủ đề F: Giải quyết vấn đề",
        "Bài 14, 15: Công việc theo các bước", "Bài 12, 13: Chia việc & Làm theo bước", "Bài 11, 12: Trình tự công việc",
        "block-maze", ["G3-01"], 7,
        ["Hiểu công việc được giải quyết theo trình tự các bước.", "Biết chia nhỏ một nhiệm vụ phức tạp thành việc nhỏ."],
        "Điều khiển chú Robot thông minh hoàn thành công việc từng bước một!",
        "Mỗi việc hàng ngày như đánh răng, pha trà, rửa tay đều gồm các bước theo thứ tự nhất định. Thay đổi thứ tự các bước có thể làm hỏng kết quả công việc.",
        ["Bước 1 làm trước, bước 2 làm sau, không thể đảo lộn tùy tiện.", "Chia việc lớn thành nhiều việc nhỏ giúp làm bài tập dễ dàng hơn."],
        {"grid_size": 4, "start": {"x": 0, "y": 0, "dir": "E"}, "target": {"x": 2, "y": 2}, "walls": [{"x": 1, "y": 0}], "allowed_blocks": ["forward", "turn_right", "turn_left"], "max_blocks": 6},
        [{"question": "Trong quy trình đánh răng, bước nào sau đây phải thực hiện trước tiên?", "options": ["Lấy kem đánh răng lên bàn chải", "Súc miệng nhổ nước ra ngoài", "Rửa sạch bàn chải sau khi đánh xong"], "answer": 0, "explanation": "Phải lấy kem đánh răng lên bàn chải trước rồi mới bắt đầu chải răng."}],
        "Em đã nắm vững quy trình các bước để giải quyết mọi nhiệm vụ chuẩn xác!"
    ))

    nodes.append(make_lesson(
        "G3-13", "w1", 3, "Vượt Mê cung & Trò chơi Rèn luyện Tư duy", "Chủ đề F: Giải quyết vấn đề",
        "Bài 16: Trò chơi học tập", "Bài 14, 15: Giải bài toán bằng sơ đồ", "Bài 13, 14: Trò chơi tư duy mê cung",
        "block-maze", ["G3-12"], 7,
        ["Vận dụng các lệnh rẽ trái, rẽ phải, đi thẳng để vượt mê cung.", "Rèn luyện tư duy không gian và tối ưu số bước đi."],
        "Đấu trí cùng mê cung số! Tìm con đường ngắn nhất dẫn tới kho báu tri thức!",
        "Để nhân vật đến được vạch đích, ta phải lập một kế hoạch tuần tự các lệnh di chuyển. Cần quan sát chướng ngại vật để tránh bị va chạm.",
        ["Lệnh 'Đi thẳng 1 ô', 'Rẽ phải 90 độ', 'Rẽ trái 90 độ'.", "Kiểm tra kỹ lưỡng từng bước đi trước khi cho Robot khởi hành."],
        {"grid_size": 4, "start": {"x": 0, "y": 0, "dir": "E"}, "target": {"x": 3, "y": 3}, "walls": [{"x": 1, "y": 1}, {"x": 2, "y": 1}], "allowed_blocks": ["forward", "turn_right", "turn_left"], "max_blocks": 8},
        [{"question": "Nếu phía trước Robot có bức tường cản đường, Robot cần làm gì trước khi đi tiếp?", "options": ["Rẽ sang hướng không có vật cản (trái hoặc phải)", "Cứ đi thẳng đâm vào tường", "Tắt máy đứng yên mãi mãi"], "answer": 0, "explanation": "Robot phải rẽ sang hướng thông thoáng để tiếp tục hành trình."}],
        "Thuật toán vượt mê cung của em đạt điểm tối đa!"
    ))

    nodes.append(make_lesson(
        "G3-14", "w1", 3, "Ôn tập & Đánh giá Năng lực Tin học Lớp 3", "Tổng kết GDPT 2018 Lớp 3",
        "Bài 16: Tổng kết Tin học 3", "Bài 16: Em tập trình bày ý kiến", "Bài 15, 16: Đánh giá & Dự án Tin học",
        "boss-quiz", ["G3-01", "G3-03", "G3-05", "G3-11", "G3-12"], 12,
        ["Tổng kết toàn diện kiến thức Tin học Lớp 3 chuẩn GDPT 2018.", "Sẵn sàng hoàn thành chương trình Tin học Lớp 3."],
        "Hãy vận dụng toàn bộ kiến thức đã học trong năm lớp 3 để hoàn thành xuất sắc bài đánh giá tổng hợp!",
        "Bài đánh giá tổng hợp: Phân biệt bộ phận máy tính, thao tác chuột phím, an toàn thông tin và tư duy thuật toán từng bước.",
        ["4 bộ phận máy tính: Thân máy, Màn hình, Bàn phím, Chuột.", "Bảo vệ thông tin cá nhân và quy tắc làm việc theo trình tự."],
        {"boss_name": "Thử thách Tổng hợp Lớp 3", "boss_max_hp": 100, "player_max_hp": 100, "damage_per_hit": 25, "questions_pool": 4},
        [
            {"question": "Bộ phận nào của máy tính thực hiện việc nhập ký tự chữ và số?", "options": ["Bàn phím", "Màn hình", "Loa", "Máy in"], "answer": 0, "explanation": "Bàn phím dùng để nhập ký tự vào máy tính."},
            {"question": "Hai phím nào trên bàn phím có gờ định vị ngón trỏ?", "options": ["F và J", "A và L", "G và H", "Z và M"], "answer": 0, "explanation": "Phím F và J là mốc định vị của hàng cơ sở."},
            {"question": "Hành động nào sau đây là đúng khi dùng mạng Internet?", "options": ["Hỏi ý kiến người lớn khi gặp thông tin lạ", "Tự ý gửi địa chỉ nhà cho người lạ", "Bấm vào mọi quảng cáo trúng thưởng", "Chơi game liên tục không nghỉ"], "answer": 0, "explanation": "Luôn trao đổi với cha mẹ, thầy cô khi dùng mạng."},
            {"question": "Thứ tự các bước giải quyết công việc gọi là gì?", "options": ["Quy trình / Thuật toán", "Bức tranh", "Tệp văn bản", "Mật khẩu"], "answer": 0, "explanation": "Quy trình tuần tự từng bước chính là thuật toán."}
        ],
        "CHÚC MỪNG EM! Em đã hoàn thành xuất sắc toàn bộ chương trình Tin học Lớp 3 theo chuẩn GDPT 2018 của cả 3 bộ sách!"
    ))

    # =========================================================================
    # LỚP 4 (15 NÚT)
    # =========================================================================
    nodes.append(make_lesson(
        "G4-01", "w1", 4, "Phần cứng & Phần mềm Máy tính", "Chủ đề A: Máy tính và em",
        "Bài 1: Phần cứng và phần mềm máy tính", "Bài 1: Phần cứng và phần mềm", "Bài 1: Phần cứng và phần mềm",
        "sort-drag", ["G3-03"], 6,
        ["Phân biệt phần cứng (Hardware) và phần mềm (Software).", "Nêu mối quan hệ: phần mềm điều khiển phần cứng hoạt động."],
        "Máy tính giống như một cơ thể sống: Phần cứng là thân thể, Phần mềm là trí tuệ!",
        "Phần cứng là các linh kiện vật lý sờ chạm được (ổ cứng, CPU, bàn phím, màn hình). Phần mềm là các chương trình máy tính chạy bên trong (Windows, Word, Paint, Scratch).",
        ["Không có phần mềm, phần cứng không thể hoạt động được.", "Phần mềm được lưu trữ bên trong các thiết bị nhớ của phần cứng."],
        {"groups": [{"id": "g1", "name": "Thiết bị Phần cứng (Hardware)"}, {"id": "g2", "name": "Chương trình Phần mềm (Software)"}], "items": [{"id":"1","name":"Thẻ nhớ USB & Ổ đĩa cứng","group":"g1","icon":"💾"},{"id":"2","name":"Màn hình & Bàn phím máy tính","group":"g1","icon":"🖥️"},{"id":"3","name":"Hệ điều hành Windows 11","group":"g2","icon":"🪟"},{"id":"4","name":"Phần mềm lập trình Scratch 3.0","group":"g2","icon":"🐱"}]},
        [{"question": "Phần mềm máy tính có đặc điểm nào sau đây?", "options": ["Là chương trình chỉ thị cho máy tính hoạt động", "Có thể cầm nắm được trên tay", "Làm bằng vỏ nhựa hoặc kim loại"], "answer": 0, "explanation": "Phần mềm là các chương trình được cài đặt trong máy tính."}],
        "Em đã phân biệt rạch ròi giữa phần cứng và phần mềm máy tính!"
    ))

    nodes.append(make_lesson(
        "G4-02", "w1", 4, "Luyện gõ Mười ngón & Tiếng Việt Telex", "Chủ đề A: Máy tính và em",
        "Bài 2: Gõ bàn phím đúng cách", "Bài 2: Luyện tập gõ mười ngón", "Bài 2: Rèn luyện kỹ năng gõ phím",
        "type-run", ["G3-07"], 6,
        ["Gõ bàn phím mười ngón đúng tư thế quy định.", "Gõ tiếng Việt thành thạo theo quy tắc gõ chữ Telex (s, f, r, x, j)."],
        "Gõ tiếng Việt có dấu thật diệu kỳ với bộ gõ Unikey kiểu gõ Telex!",
        "Quy tắc gõ dấu thanh Telex: s (sắc), f (huyền), r (hỏi), x (ngã), j (nặng). Các chữ cái đặc biệt: aa -> â, aw -> ă, ee -> ê, oo -> ô, ow -> ơ, uw -> ư, dd -> đ.",
        ["Gõ chữ trước, gõ dấu thanh sau cùng của từ.", "Duy trì vị trí ngón tay trên hàng cơ sở."],
        {"words": ["truong", "lop", "hoc", "viet"]},
        [{"question": "Trong kiểu gõ Telex, phím nào dùng để gõ dấu huyền?", "options": ["Phím F", "Phím S", "Phím J"], "answer": 0, "explanation": "Trong quy tắc Telex: phím F là dấu huyền (ví dụ: baf -> bà)."}],
        "Kỹ năng gõ tiếng Việt Telex của em rất chuẩn xác!"
    ))

    nodes.append(make_lesson(
        "G4-03", "w1", 4, "Thông tin trên Web & Siêu liên kết", "Chủ đề B: Mạng và Internet",
        "Bài 3: Thông tin trên trang web", "Bài 3: Khám phá trang web", "Bài 3: Tìm kiếm an toàn trên Internet",
        "branch-story", ["G3-08"], 6,
        ["Nhận biết các thành phần trang web: văn bản, hình ảnh, video, siêu liên kết.", "Biết điều hướng bằng cách nhấp chuột vào siêu liên kết."],
        "Lướt mạng toàn cầu: Khám phá những cánh cửa bí mật mở ra tri thức mới!",
        "Siêu liên kết (Hyperlink) là từ hoặc hình ảnh khi nhấp chuột vào sẽ đưa em chuyển đến một trang web mới. Con trỏ chuột thường đổi thành hình bàn tay chỉ ngón trỏ.",
        ["Thanh địa chỉ URL hiển thị đường dẫn trang web.", "Nút Back (mũi tên quay lại) đưa về trang vừa xem trước đó."],
        {"scenarios": [{"id": "s1", "prompt": "Khi rê chuột qua một dòng chữ màu xanh gạch chân, con trỏ chuột biến thành hình bàn tay trỏ ngón.", "choices": [{"text": "Nhấp chuột trái vào đó để mở trang thông tin liên kết.", "is_correct": True, "feedback": "Chính xác! Đó là siêu liên kết (Hyperlink)."}, {"text": "Tắt ngay máy tính vì sợ virus.", "is_correct": False, "feedback": "Đó chỉ là siêu liên kết thông thường, không phải virus!"}]}]},
        [{"question": "Dấu hiệu nhận biết con trỏ chuột đang trỏ vào một siêu liên kết là gì?", "options": ["Con trỏ đổi thành hình bàn tay chỉ ngón trỏ", "Con trỏ biến mất hoàn toàn", "Màn hình chuyển sang màu đỏ"], "answer": 0, "explanation": "Biểu tượng bàn tay là quy ước quốc tế cho liên kết web."}],
        "Em đã làm chủ kỹ năng điều hướng và duyệt web an toàn!"
    ))

    nodes.append(make_lesson(
        "G4-04", "w1", 4, "Kỹ năng Tìm kiếm Thông tin Khoa học", "Chủ đề B: Mạng và Internet",
        "Bài 4: Tìm kiếm thông tin trên Internet", "Bài 4: Tìm kiếm thông tin hữu ích", "Bài 3: Tìm kiếm an toàn trên Internet",
        "sort-drag", ["G4-03"], 6,
        ["Sử dụng máy tìm kiếm (Google) với từ khóa chính xác.", "Lọc và chọn đường link uy tín để đọc nội dung."],
        "Tìm kiếm tài liệu học tập trong nháy mắt nhờ cỗ máy tìm kiếm thông minh!",
        "Từ khóa (Keyword) là từ hoặc cụm từ ngắn gọn thể hiện chính xác điều em muốn tìm. Đặt từ khóa trong ngoặc kép \"...\" để tìm chính xác cụm từ đó.",
        ["Tránh nhập cả câu dài dòng vào ô tìm kiếm.", "Ưu tiên chọn các trang web giáo dục có đuôi .edu.vn hoặc báo chính thống."],
        {"groups": [{"id": "g1", "name": "Từ khóa Tìm kiếm Ngắn gọn, Chính xác"}, {"id": "g2", "name": "Cụm từ Dài dòng, Không hiệu quả"}], "items": [{"id":"1","name":"\"Động vật hoang dã Việt Nam\"","group":"g1","icon":"🐅"},{"id":"2","name":"Lịch sử Vua Hùng dựng nước","group":"g1","icon":"👑"},{"id":"3","name":"Bác Google ơi tìm giúp cháu xem con voi sống ở đâu với ạ","group":"g2","icon":"🗣️"},{"id":"4","name":"Cho tôi hỏi ngày mai thời tiết Hà Nội có mưa không nhỉ","group":"g2","icon":"❓"}]},
        [{"question": "Để tìm kiếm thông tin về loài gấu trúc, từ khóa nào sau đây là tốt nhất?", "options": ["Gấu trúc", "Tôi muốn tìm hiểu về cuộc sống của gấu trúc", "Cho xem ảnh gấu"], "answer": 0, "explanation": "Từ khóa ngắn gọn 'Gấu trúc' cho kết quả chính xác và đầy đủ nhất."}],
        "Em đã trở thành một chuyên gia tìm kiếm thông tin tài ba!"
    ))

    nodes.append(make_lesson(
        "G4-05", "w1", 4, "Quản lý Tệp và Cây Thư mục Khoa học", "Chủ đề C: Tổ chức lưu trữ",
        "Bài 5: Thao tác với tệp và thư mục", "Bài 5: Quản lý tệp và thư mục", "Bài 4: Quản lý tệp và thư mục",
        "sort-drag", ["G3-10"], 6,
        ["Phân biệt tệp (file) và thư mục (folder).", "Thực hiện thành thạo: Tạo mới, Đổi tên, Sao chép, Xóa."],
        "Xây dựng ngôi nhà ngăn nắp cho các tệp tài liệu học tập trong máy tính!",
        "Thư mục giống như ngăn kéo chứa các tệp tài liệu hoặc các thư mục con. Tệp có phần tên và phần mở rộng (đuôi tệp) thể hiện loại tài liệu (.docx, .png, .mp4).",
        ["Tên tệp nên đặt không dấu, có nghĩa rõ ràng để dễ tìm.", "Không xóa các tệp hệ thống trong ổ đĩa C của máy tính."],
        {"groups": [{"id": "g1", "name": "Tệp tin dữ liệu (Files)"}, {"id": "g2", "name": "Thư mục chứa (Folders)"}], "items": [{"id":"1","name":"BaiTapToan_Lop4.docx","group":"g1","icon":"📝"},{"id":"2","name":"HinhAnh_GiaDinh.png","group":"g1","icon":"🖼️"},{"id":"3","name":"Thư mục: MÔN TIN HỌC","group":"g2","icon":"📁"},{"id":"4","name":"Thư mục: VIDEO BÀI GIẢNG","group":"g2","icon":"📂"}]},
        [{"question": "Biểu tượng của một thư mục trong hệ điều hành Windows thường có màu gì?", "options": ["Màu vàng hình chiếc kẹp tài liệu", "Màu đỏ hình tam giác", "Màu xanh lá cây"], "answer": 0, "explanation": "Thư mục có biểu tượng chiếc kẹp hồ sơ màu vàng đặc trưng."}],
        "Cây thư mục bài học của em được tổ chức cực kỳ khoa học!"
    ))

    nodes.append(make_lesson(
        "G4-06", "w1", 4, "Bản quyền Tác giả & Đạo đức Phần mềm", "Chủ đề D: Đạo đức, pháp luật",
        "Bài 6: Sử dụng phần mềm khi được phép", "Bài 6: Tôn trọng quyền tác giả", "Bài 5: Bản quyền và thông tin hợp pháp",
        "branch-story", ["G3-11"], 6,
        ["Hiểu phần mềm và nội dung số là tài sản trí tuệ.", "Tôn trọng bản quyền, xin phép tác giả trước khi sử dụng."],
        "Trở thành công dân số văn minh, luôn tôn trọng công sức lao động của người khác!",
        "Phần mềm, tranh ảnh, bài hát trên mạng đều do tác giả bỏ công sức sáng tạo. Không sao chép lậu, không sử dụng khi chưa được tác giả cho phép.",
        ["Ghi rõ nguồn tác giả khi trích dẫn tranh ảnh vào bài thuyết trình.", "Ủng hộ các phần mềm bản quyền chính hãng và phần mềm tự do nguồn mở."],
        {"scenarios": [{"id": "s1", "prompt": "Em thấy trên mạng có một bức ảnh vẽ rất đẹp và muốn đưa vào bài trình chiếu dự thi của mình.", "choices": [{"text": "Xin phép tác giả hoặc ghi chú nguồn tên tác giả dưới bức ảnh.", "is_correct": True, "feedback": "Tuyệt vời! Em là một học sinh trung thực và tôn trọng bản quyền."}, {"text": "Cắt bỏ chữ ký tác giả và nhận đó là tranh do mình tự vẽ.", "is_correct": False, "feedback": "Xóa tên tác giả và nhận vơ là vi phạm pháp luật sở hữu trí tuệ!"}]}]},
        [{"question": "Khi sử dụng bài văn hoặc bức ảnh của người khác vào bài làm của mình, em cần làm gì?", "options": ["Ghi rõ họ tên tác giả và nguồn gốc trích dẫn", "Tự nhận đó là do mình sáng tác", "Không cần ghi gì cả"], "answer": 0, "explanation": "Ghi nguồn trích dẫn là thể hiện sự tôn trọng bản quyền tác giả."}],
        "Em là tấm gương sáng về tôn trọng bản quyền và đạo đức số!"
    ))

    nodes.append(make_lesson(
        "G4-07", "w1", 4, "Soạn thảo Văn bản & Chèn Hình ảnh", "Chủ đề E: Ứng dụng tin học",
        "Bài 7: Chèn hình ảnh vào văn bản", "Bài 7: Soạn thảo văn bản có hình ảnh", "Bài 6: Chèn hình và căn lề văn bản",
        "sort-drag", ["G4-02"], 6,
        ["Soạn thảo văn bản tiếng Việt đúng chính tả.", "Chèn hình ảnh từ máy tính vào trang văn bản và chỉnh kích thước."],
        "Biến trang văn bản mộc mạc thành tờ báo tường rực rỡ sắc màu!",
        "Trong phần mềm soạn thảo Word/Docs, vào thẻ Insert chọn Pictures để chèn hình ảnh. Nhấp vào các nút góc của ảnh để phóng to, thu nhỏ tùy ý.",
        ["Chèn ảnh phù hợp với chủ đề nội dung đoạn văn.", "Chọn chế độ Wrap Text (Wrap Square/Tight) để chữ bao quanh ảnh hài hòa."],
        {"groups": [{"id": "g1", "name": "Công cụ Định dạng Chữ (Text)"}, {"id": "g2", "name": "Công cụ Chèn & Xử lý Ảnh (Image)"}], "items": [{"id":"1","name":"Chọn phông chữ Times New Roman","group":"g1","icon":"🔤"},{"id":"2","name":"Tô màu chữ đỏ nổi bật","group":"g1","icon":"🎨"},{"id":"3","name":"Chèn tranh ảnh từ tệp Pictures","group":"g2","icon":"🖼️"},{"id":"4","name":"Thu nhỏ kích thước ảnh vừa trang giấy","group":"g2","icon":"📐"}]},
        [{"question": "Để chèn một bức ảnh vào văn bản Word, em chọn bảng chọn nào trên thanh công cụ?", "options": ["Bảng chọn Insert (Chèn)", "Bảng chọn File", "Bảng chọn View"], "answer": 0, "explanation": "Insert chứa các lệnh chèn hình ảnh, bảng biểu, hình khối."}],
        "Văn bản có hình ảnh minh họa của em trông vô cùng sinh động!"
    ))

    nodes.append(make_lesson(
        "G4-08", "w1", 4, "Định dạng Đoạn Văn bản Chuyên nghiệp", "Chủ đề E: Ứng dụng tin học",
        "Bài 8: Định dạng văn bản", "Bài 8: Định dạng đoạn văn bản", "Bài 7: Định dạng kiểu chữ và màu sắc",
        "type-run", ["G4-07"], 6,
        ["Định dạng ký tự: Đậm (B), Nghiêng (I), Gạch chân (U).", "Căn lề đoạn văn: Căn trái, căn phải, căn giữa, căn đều hai bên."],
        "Trình bày văn bản chuẩn mực như một nhà xuất bản chuyên nghiệp!",
        "Phím tắt thông dụng: Ctrl + B (in đậm), Ctrl + I (in nghiêng), Ctrl + U (gạch chân), Ctrl + E (căn giữa tiêu đề), Ctrl + J (căn đều hai lề đoạn văn).",
        ["Tiêu đề bài viết thường được in đậm và căn giữa trang.", "Đoạn nội dung chính nên căn đều hai lề để trang in thẳng hàng đẹp mắt."],
        {"words": ["dinh", "dang", "can", "le"]},
        [{"question": "Tổ hợp phím nào sau đây dùng để in đậm (Bold) chữ đã chọn?", "options": ["Ctrl + B", "Ctrl + I", "Ctrl + U"], "answer": 0, "explanation": "Ctrl + B (viết tắt của Bold) dùng để bật/tắt in đậm chữ."}],
        "Trang văn bản của em được định dạng rất chuẩn mực và đẹp mắt!"
    ))

    nodes.append(make_lesson(
        "G4-09", "w1", 4, "Thiết kế Bài Trình chiếu Sinh động", "Chủ đề E: Ứng dụng tin học",
        "Bài 9, 10: Tạo bài trình chiếu", "Bài 9, 10: Phần mềm trình chiếu", "Bài 8, 9: Trang trình chiếu & Báo cáo",
        "match-memory", ["G4-07"], 6,
        ["Tạo trang chiếu mới (New Slide), nhập tiêu đề và nội dung.", "Áp dụng mẫu bố cục Layouts và hiệu ứng chuyển trang Transitions."],
        "Trở thành nhà diễn thuyết tài ba với những trang trình chiếu PowerPoint cuốn hút!",
        "Mỗi trang chiếu chỉ nên chứa ý chính súc tích kết hợp hình ảnh minh họa. Sử dụng hiệu ứng chuyển trang nhịp nhàng để tạo sự bất ngờ.",
        ["Không viết quá nhiều chữ dày đặc trên một trang chiếu.", "Màu chữ phải tương phản nổi bật trên màu nền (nền sáng chữ tối hoặc ngược lại)."],
        {"cards": [{"id":"1","name":"Trang tiêu đề","match":"Giới thiệu tên bài thuyết trình và tên tác giả"},{"id":"2","name":"Hiệu ứng Transitions","match":"Chuyển động khi chuyển đổi giữa các slide"},{"id":"3","name":"Hiệu ứng Animations","match":"Chuyển động xuất hiện của từng dòng chữ hoặc hình ảnh"},{"id":"4","name":"Mẫu giao diện Theme","match":"Bộ màu sắc và phông chữ thiết kế đồng bộ"}]},
        [{"question": "Nguyên tắc phối màu chuẩn khi thiết kế trang chiếu là gì?", "options": ["Chữ tối màu trên nền sáng (hoặc chữ sáng trên nền tối)", "Chữ vàng trên nền trắng", "Chữ xám mờ trên nền đen"], "answer": 0, "explanation": "Độ tương phản cao giúp người ngồi xa dưới lớp vẫn đọc rõ chữ."}],
        "Bài thuyết trình trình chiếu của em rất ấn tượng và chuyên nghiệp!"
    ))

    nodes.append(make_lesson(
        "G4-10", "w1", 4, "Xử lý & Chỉnh sửa Hình ảnh Cơ bản", "Chủ đề E: Ứng dụng tin học",
        "Bài 11: Chỉnh sửa hình ảnh", "Bài 11: Xử lý hình ảnh đơn giản", "Bài 10: Chỉnh sửa ảnh cơ bản",
        "sort-drag", ["G4-07"], 6,
        ["Cắt bớt chi tiết thừa (Crop) của bức ảnh.", "Xoay hình ảnh (Rotate) và lật gương (Flip)."],
        "Hô biến bức ảnh trở nên hoàn hảo với các công cụ biên tập hình ảnh!",
        "Công cụ Crop giúp em cắt lấy góc ảnh đẹp nhất và loại bỏ nền thừa. Công cụ Rotate giúp xoay ngay ngắn các bức ảnh bị chụp nghiêng.",
        ["Giữ tỉ lệ khung hình để ảnh không bị méo mó, co giãn dị dạng.", "Lưu ảnh ở định dạng nén chất lượng cao PNG hoặc JPG."],
        {"groups": [{"id": "g1", "name": "Thao tác Cắt xén (Crop)"}, {"id": "g2", "name": "Thao tác Xoay & Lật (Rotate/Flip)"}], "items": [{"id":"1","name":"Cắt bỏ góc phòng thừa trong bức ảnh chụp","group":"g1","icon":"✂️"},{"id":"2","name":"Cắt ảnh thành hình vuông làm ảnh đại diện","group":"g1","icon":"🔲"},{"id":"3","name":"Xoay ảnh 90 độ theo chiều kim đồng hồ","group":"g2","icon":"🔄"},{"id":"4","name":"Lật ảnh ngang để nhân vật quay mặt sang phải","group":"g2","icon":"↔️"}]},
        [{"question": "Muốn cắt bỏ phần thừa hai bên mép của bức ảnh, em dùng công cụ nào?", "options": ["Công cụ Crop (Cắt xén)", "Công cụ Rotate", "Công cụ Zoom"], "answer": 0, "explanation": "Crop là công cụ chuẩn để cắt bớt khung hình ảnh."}],
        "Kỹ năng xử lý hình ảnh của em rất khéo léo!"
    ))

    nodes.append(make_lesson(
        "G4-11", "w1", 4, "Khám phá Lập trình Trực quan Scratch", "Chủ đề F: Giải quyết vấn đề",
        "Bài 12, 13: Môi trường Scratch & Lệnh đầu tiên", "Bài 12: Em làm quen với Scratch", "Bài 11, 12: Môi trường & Nhân vật",
        "match-memory", ["G3-13"], 6,
        ["Nhận biết 4 khu vực chính trên giao diện Scratch.", "Hiểu cách lắp ghép các khối lệnh theo màu sắc chức năng."],
        "Chào mừng em đến với thế giới sáng tạo Scratch cùng chú Mèo tinh nghịch!",
        "Giao diện Scratch gồm: Bảng khối lệnh (chia theo màu sắc), Khu vực kịch bản (nơi lắp ghép lệnh), Sân khấu (nơi kịch bản diễn ra) và Danh sách nhân vật.",
        ["Khối lệnh màu xanh lam: Chuyển động (Motion).", "Khối lệnh màu vàng: Sự kiện (Events) khởi động chương trình."],
        {"cards": [{"id":"1","name":"Khối Sự kiện (Màu vàng)","match":"Khi bấm vào lá cờ xanh để bắt đầu chạy kịch bản"},{"id":"2","name":"Khối Chuyển động (Màu xanh lam)","match":"Di chuyển 10 bước, xoay hướng 15 độ"},{"id":"3","name":"Khối Hiển thị (Màu tím)","match":"Nói xin chào, đổi trang phục cho nhân vật"},{"id":"4","name":"Khối Âm thanh (Màu hồng)","match":"Phát tiếng kêu Meo meo vui nhộn"}]},
        [{"question": "Khối lệnh nào sau đây thường được đặt ở đầu tiên để kích hoạt chương trình Scratch chạy?", "options": ["Khi bấm vào lá cờ xanh (When green flag clicked)", "Di chuyển 10 bước", "Dừng lại tất cả"], "answer": 0, "explanation": "Bấm vào cờ xanh là tín hiệu chuẩn để khởi động kịch bản Scratch."}],
        "Em đã làm quen thành thạo với giao diện Scratch sáng tạo!"
    ))

    nodes.append(make_lesson(
        "G4-12", "w1", 4, "Điều khiển Nhân vật Chuyển động", "Chủ đề F: Giải quyết vấn đề",
        "Bài 14: Điều khiển nhân vật chuyển động", "Bài 13: Nhân vật chuyển động theo lệnh", "Bài 13: Điều khiển nhân vật di chuyển",
        "block-maze", ["G4-11"], 7,
        ["Sử dụng khối lệnh di chuyển Move và xoay Turn.", "Sử dụng lệnh nếu chạm cạnh thì bật lại (If on edge, bounce)."],
        "Điều khiển chú Mèo chạy nhảy tự do trên sân khấu không bị lọt ra ngoài mép màn hình!",
        "Khối lệnh 'Di chuyển 10 bước' đưa nhân vật tiến về phía trước theo hướng hiện tại. Khối lệnh 'Bật lại nếu chạm cạnh' giúp nhân vật không bị biến mất khỏi màn hình.",
        ["Hướng 90 độ là nhìn sang phải, -90 độ là nhìn sang trái.", "Đặt kiểu xoay trái-phải để nhân vật không bị lộn ngược đầu."],
        {"grid_size": 4, "start": {"x": 0, "y": 0, "dir": "E"}, "target": {"x": 2, "y": 2}, "walls": [{"x": 1, "y": 0}], "allowed_blocks": ["forward", "turn_right", "turn_left"], "max_blocks": 6},
        [{"question": "Lệnh nào giúp nhân vật Scratch tự động quay đầu khi chạm vào mép ngoài của sân khấu?", "options": ["Nếu chạm cạnh, bật lại (If on edge, bounce)", "Ẩn nhân vật (Hide)", "Dừng lại 1 giây"], "answer": 0, "explanation": "If on edge, bounce giữ nhân vật luôn chạy bên trong sân khấu."}],
        "Nhân vật của em đã lướt đi rất uyển chuyển trên sân khấu!"
    ))

    nodes.append(make_lesson(
        "G4-13", "w1", 4, "Cấu trúc Vòng lặp Tuần hoàn (Repeat)", "Chủ đề F: Giải quyết vấn đề",
        "Bài 15: Lặp lại một việc", "Bài 14: Cấu trúc lặp trong lập trình", "Bài 14: Vòng lặp trong chương trình",
        "block-maze", ["G4-12"], 7,
        ["Hiểu ý nghĩa cấu trúc lặp: giảm bớt số dòng lệnh trùng lặp.", "Sử dụng khối lệnh lặp lại N lần (Repeat N)."],
        "Thay vì viết 100 lần dòng lệnh bước đi, chỉ cần một vòng lặp nhỏ xinh!",
        "Vòng lặp giúp máy tính thực hiện các hành động lặp đi lặp lại một cách tự động và chính xác. Để vẽ hình vuông, ta chỉ cần lặp lại 4 lần: Đi thẳng và Rẽ phải 90 độ.",
        ["Vòng lặp Repeat 10: lặp đúng 10 lần rồi dừng lại.", "Vòng lặp Forever: lặp mãi mãi không dừng cho đến khi bấm nút đỏ."],
        {"grid_size": 4, "start": {"x": 0, "y": 0, "dir": "E"}, "target": {"x": 3, "y": 3}, "walls": [{"x": 1, "y": 1}], "allowed_blocks": ["forward", "turn_right", "turn_left"], "max_blocks": 6},
        [{"question": "Để nhân vật vẽ một hình tam giác đều 3 cạnh, khối lệnh lặp cần thiết lập số lần lặp là bao nhiêu?", "options": ["Lặp lại 3 lần", "Lặp lại 4 lần", "Lặp lại 10 lần"], "answer": 0, "explanation": "Hình tam giác có 3 cạnh nên lặp lại 3 lần vẽ cạnh và xoay góc."}],
        "Vòng lặp của em đã giúp đoạn mã trở nên cực kỳ gọn gàng!"
    ))

    nodes.append(make_lesson(
        "G4-14", "w1", 4, "Biểu diễn Thuật toán bằng Sơ đồ khối", "Chủ đề F: Giải quyết vấn đề",
        "Bài 16: Biểu diễn thuật toán", "Bài 15: Xây dựng câu chuyện tương tác", "Bài 15: Sơ đồ khối thuật toán",
        "logic-puzzle", ["G4-13"], 8,
        ["Nhận biết quy ước hình khối chuẩn: Bắt đầu/Kết thúc, Thao tác, Điều kiện.", "Đọc hiểu luồng thực thi của sơ đồ khối."],
        "Vẽ bản đồ tư duy thuật toán trước khi bắt tay vào gõ từng dòng lệnh!",
        "Sơ đồ khối dùng các hình hình học và mũi tên để mô tả đường đi của thuật toán: Hình Oval (Bắt đầu/Kết thúc), Hình chữ nhật (Hành động xử lý), Hình thoi (Kiểm tra điều kiện).",
        ["Mũi tên chỉ hướng thực hiện tiếp theo của chương trình.", "Từ hình thoi luôn có 2 nhánh rẽ: Đúng (Yes) hoặc Sai (No)."],
        {"bits_count": 3, "weights": [4, 2, 1], "target_values": [1, 2, 4]},
        [{"question": "Trong sơ đồ khối thuật toán, hình nào dùng để biểu diễn bước kiểm tra điều kiện rẽ nhánh?", "options": ["Hình thoi", "Hình chữ nhật", "Hình tròn"], "answer": 0, "explanation": "Hình thoi là ký hiệu quốc tế chuẩn cho khối quyết định điều kiện."}],
        "Em đã làm chủ kỹ năng đọc và vẽ sơ đồ khối thuật toán!"
    ))

    nodes.append(make_lesson(
        "G4-15", "w1", 4, "Ôn tập & Đánh giá Năng lực Tin học Lớp 4", "Tổng kết GDPT 2018 Lớp 4",
        "Bài 16: Dự án Tin học 4", "Bài 16: Dự án lập trình trò chơi", "Bài 16: Dự án Em làm nhà lập trình",
        "boss-quiz", ["G4-01", "G4-05", "G4-08", "G4-11", "G4-13"], 12,
        ["Tổng kết toàn diện kiến thức Tin học Lớp 4 của 3 bộ sách.", "Sẵn sàng nhận danh hiệu Nhà Lập Trình Nhí EasyTin."],
        "Hãy vận dụng tư duy thuật toán và kỹ năng lập trình Scratch để hoàn thành bài đánh giá năng lực!",
        "Bài đánh giá tổng hợp: Phân biệt Phần cứng - Phần mềm, Cây thư mục, Định dạng văn bản và Khối lệnh lập trình Scratch.",
        ["Phần cứng và Phần mềm phối hợp nhịp nhàng.", "Cấu trúc lặp Repeat N tối ưu hóa thuật toán."],
        {"boss_name": "Thử thách Tổng hợp Lớp 4", "boss_max_hp": 100, "player_max_hp": 100, "damage_per_hit": 25, "questions_pool": 4},
        [
            {"question": "Thành phần nào sau đây là phần mềm máy tính?", "options": ["Hệ điều hành Windows", "Chuột không dây", "Màn hình LED", "Bàn phím cơ"], "answer": 0, "explanation": "Windows là phần mềm hệ thống điều khiển máy tính."},
            {"question": "Trong Scratch, khối lệnh 'Lặp lại 10 lần' nằm trong nhóm lệnh nào?", "options": ["Điều khiển (Control)", "Chuyển động (Motion)", "Âm thanh (Sound)", "Cảm biến (Sensing)"], "answer": 0, "explanation": "Nhóm Control (màu cam) quản lý các vòng lặp và điều kiện."},
            {"question": "Để tìm chính xác cụm từ trên Google, ta đặt cụm từ đó trong dấu gì?", "options": ["Dấu ngoặc kép \"...\"", "Dấu ngoặc đơn (...)", "Dấu chấm than !...", "Dấu hỏi chấm ?..."], "answer": 0, "explanation": "Dấu ngoặc kép tìm kiếm chính xác từng từ trong cụm từ."},
            {"question": "Đuôi mở rộng nào sau đây là của tệp văn bản Word?", "options": [".docx", ".png", ".mp3", ".exe"], "answer": 0, "explanation": ".docx là định dạng chuẩn của tài liệu Word."}
        ],
        "CHÚC MỪNG EM! Em đã làm chủ toàn bộ chương trình Tin học Lớp 4 của cả 3 bộ sách KNTT, Cánh Diều, CTST!"
    ))

    # =========================================================================
    # LỚP 5 (14 NÚT)
    # =========================================================================
    nodes.append(make_lesson(
        "G5-01", "w1", 5, "Máy tính và Cuộc sống Hiện đại", "Chủ đề A: Máy tính và em",
        "Bài 1: Máy tính và cuộc sống", "Bài 1: Vai trò máy tính thời đại số", "Bài 1: Thiết bị thông minh quanh em",
        "match-memory", ["G4-01"], 6,
        ["Nêu vai trò của máy tính trong sản xuất, giao thông, y tế, giáo dục.", "Nhận biết các thiết bị số thông minh xung quanh."],
        "Khám phá các cỗ máy thông minh đang thay đổi thế giới xung quanh chúng ta!",
        "Máy tính không chỉ là máy để bàn hay laptop, mà còn nằm trong robot y tế phẫu thuật, hệ thống dẫn đường máy bay, camera an ninh và điện thoại thông minh.",
        ["Thiết bị thông minh giúp con người làm việc nhanh hơn, an toàn hơn.", "Tin học thúc đẩy sự phát triển của mọi ngành nghề xã hội."],
        {"cards": [{"id":"1","name":"Robot y tế","match":"Hỗ trợ bác sĩ phẫu thuật chính xác cao"},{"id":"2","name":"Vệ tinh viễn thông","match":"Truyền tín hiệu truyền hình và định vị toàn cầu GPS"},{"id":"3","name":"Máy gặt đập liên hợp thông minh","match":"Tự động thu hoạch lúa trên cánh đồng nông nghiệp"},{"id":"4","name":"Hệ thống đèn tín hiệu giao thông số","match":"Tự động điều tiết xe cộ chống ùn tắc"}]},
        [{"question": "Thiết bị nào sau đây là thiết bị số thông minh?", "options": ["Đồng hồ thông minh Smartwatch", "Cái chổi quét nhà thông thường", "Chiếc bàn gỗ"], "answer": 0, "explanation": "Smartwatch có bộ xử lý máy tính thu nhận và xử lý nhịp tim, bước chân."}],
        "Em đã nhận thức rất rõ vai trò của công nghệ số trong cuộc sống!"
    ))

    nodes.append(make_lesson(
        "G5-02", "w1", 5, "Khám phá Phần cứng bên trong Thân máy", "Chủ đề A: Máy tính và em",
        "Bài 2: Khám phá phần cứng máy tính", "Bài 1: Các bộ phận máy tính", "Bài 1: Khám phá phần cứng",
        "sort-drag", ["G4-01"], 6,
        ["Nhận biết các khối linh kiện bên trong thân máy: CPU, RAM, Ổ cứng, Bo mạch chủ.", "Hiểu chức năng lưu trữ tạm thời của RAM và lâu dài của SSD/HDD."],
        "Mở nắp thân máy tính để khám phá trái tim và bộ não điện tử diệu kỳ!",
        "Bên trong thân máy gồm: Bo mạch chủ (kết nối tất cả linh kiện), CPU (bộ vi xử lý trung tâm), RAM (bộ nhớ tạm thời, mất điện sẽ mất dữ liệu), Ổ đĩa SSD/HDD (lưu trữ lâu dài).",
        ["CPU thực hiện hàng tỷ phép tính mỗi giây.", "Ổ đĩa cứng lưu trữ hệ điều hành, trò chơi và tài liệu học tập của em."],
        {"groups": [{"id": "g1", "name": "Linh kiện Xử lý & Bộ nhớ tạm thời"}, {"id": "g2", "name": "Thiết bị Lưu trữ dữ liệu lâu dài"}], "items": [{"id":"1","name":"Bộ xử lý trung tâm CPU (Intel/AMD)","group":"g1","icon":"🧠"},{"id":"2","name":"Thanh bộ nhớ truy cập ngẫu nhiên RAM","group":"g1","icon":"⚡"},{"id":"3","name":"Ổ đĩa cứng thể rắn SSD 512GB","group":"g2","icon":"💾"},{"id":"4","name":"Thẻ nhớ MicroSD & Ổ đĩa di động","group":"g2","icon":"💳"}]},
        [{"question": "Khi máy tính bị mất điện đột ngột, dữ liệu trong bộ phận nào sẽ bị mất sạch?", "options": ["Bộ nhớ RAM", "Ổ đĩa cứng SSD", "Đĩa quang CD"], "answer": 0, "explanation": "RAM là bộ nhớ khả biến, cần nguồn điện liên tục để duy trì dữ liệu."}],
        "Em đã hiểu tường tận kiến trúc các linh kiện bên trong máy tính!"
    ))

    nodes.append(make_lesson(
        "G5-03", "w1", 5, "An toàn Điện, Bảo vệ Mắt & Tiết kiệm Điện", "Chủ đề A: Máy tính và em",
        "Bài 3: Sử dụng máy tính an toàn, tiết kiệm điện", "Bài 2: An toàn thông tin và sức khỏe", "Bài 2: An toàn trực tuyến",
        "branch-story", ["G4-01"], 6,
        ["Nêu các biện pháp phòng chống cháy nổ, giật điện khi dùng máy tính.", "Thực hiện quy tắc 20-20-20 bảo vệ thị lực."],
        "Học tin học thông minh kết hợp bảo vệ sức khỏe và tiết kiệm năng lượng!",
        "Quy tắc 20-20-20: Cứ sau 20 phút nhìn màn hình, hãy nhìn ra xa 20 feet (khoảng 6 mét) trong 20 giây để mắt thư giãn. Tắt màn hình khi rời khỏi bàn học để tiết kiệm điện.",
        ["Không ăn uống gần bàn phím để tránh đổ nước chập cháy điện.", "Luôn kiểm tra dây điện xem có bị hở vỏ bọc hay không."],
        {"scenarios": [{"id": "s1", "prompt": "Em đang ngồi học thì nhìn thấy dây cắm chuột bị chuột cắn rách vỏ cao su lộ lõi dây đồng bên trong.", "choices": [{"text": "Báo ngay cho bố mẹ hoặc thầy cô giáo, không tự ý chạm tay vào chỗ hở.", "is_correct": True, "feedback": "Rất chuẩn! Tuyệt đối không chạm tay vào dây điện hở để phòng tránh giật điện."}, {"text": "Lấy tay nắm thử xem có bị giật hay không.", "is_correct": False, "feedback": "Cực kỳ nguy hiểm! Có thể gây giật điện nguy hiểm đến tính mạng!"}]}]},
        [{"question": "Quy tắc 20-20-20 khi dùng máy tính khuyên em sau 20 phút nên làm gì?", "options": ["Nhìn xa khoảng 6 mét trong 20 giây để thư giãn mắt", "Ăn một cái kẹo trong 20 phút", "Nhắm mắt ngủ luôn 20 phút"], "answer": 0, "explanation": "Quy tắc 20-20-20 giúp cơ mắt thư giãn, chống mỏi mắt và cận thị."}],
        "Em đã hình thành thói quen bảo vệ sức khỏe và sử dụng điện an toàn!"
    ))

    nodes.append(make_lesson(
        "G5-04", "w1", 5, "Thẩm định Độ tin cậy Thông tin trên Mạng", "Chủ đề B: Mạng và Internet",
        "Bài 4: Tìm kiếm thông tin trên Internet", "Bài 3: Tìm kiếm và đánh giá thông tin", "Bài 3: Đánh giá độ tin cậy thông tin",
        "sort-drag", ["G4-04"], 6,
        ["Biết so sánh thông tin từ nhiều nguồn chính thống khác nhau.", "Nhận diện dấu hiệu của tin giả (Fake news) và tin lừa đảo."],
        "Trở thành thám tử nhí vạch trần những thông tin sai lệch trên Internet!",
        "Không phải mọi thứ trên mạng đều là sự thật. Tin giả thường có tiêu đề giật gân, câu like, giục bấm vào link gấp, không có tác giả rõ ràng hoặc nguồn từ các trang web lạ.",
        ["So sánh thông tin với các trang báo chính thống của Nhà nước.", "Hỏi ý kiến thầy cô giáo trước khi tin theo các thông tin gây xôn xao trên mạng."],
        {"groups": [{"id": "g1", "name": "Nguồn tin Tin cậy, Chính thống"}, {"id": "g2", "name": "Thông tin Đáng ngờ, Sai lệch (Fake news)"}], "items": [{"id":"1","name":"Cổng thông tin Bộ Giáo dục và Đào tạo (moet.gov.vn)","group":"g1","icon":"🏛️"},{"id":"2","name":"Báo Điện tử Đài Tiếng nói Việt Nam (VOV)","group":"g1","icon":"📻"},{"id":"3","name":"Trang mạng xã hội giật gân: Bấm vào nhận 500k thẻ cào ngay lập tức!","group":"g2","icon":"🚨"},{"id":"4","name":"Tin nhắn nặc danh: Ngày mai toàn bộ trường học được nghỉ Tết sớm","group":"g2","icon":"❌"}]},
        [{"question": "Đặc điểm nào sau đây cho thấy một bài viết trên mạng KHÔNG đáng tin cậy?", "options": ["Tiêu đề giật gân, thôi thúc chia sẻ ngay nhưng không rõ tác giả", "Có trích dẫn nguồn từ Bộ Y tế", "Được đăng trên trang web có đuôi tên miền .gov.vn"], "answer": 0, "explanation": "Tin giả thường giật gân để lừa người xem chia sẻ mà không có căn cứ."}],
        "Em đã có đôi mắt tinh tường phân biệt tin thật và tin giả trên không gian số!"
    ))

    nodes.append(make_lesson(
        "G5-05", "w1", 5, "Bản quyền Số & Trách nhiệm Chia sẻ", "Chủ đề D: Đạo đức, pháp luật",
        "Bài 5: Bản quyền và thông tin an toàn", "Bài 4: Bản quyền và đạo đức trên mạng", "Bài 4: Tôn trọng quyền riêng tư & trí tuệ",
        "branch-story", ["G4-06"], 6,
        ["Tôn trọng bản quyền tác phẩm kỹ thuật số.", "Không lan truyền thông tin sai sự thật hoặc bôi nhọ bạn bè."],
        "Mỗi lượt chia sẻ trên mạng là một trách nhiệm đối với cộng đồng!",
        "Khi chia sẻ bài viết, video hay hình ảnh trên mạng xã hội, em phải chịu trách nhiệm về nội dung đó. Không đăng ảnh dìm hàng, xúc phạm người khác; không sao chép tác phẩm có bản quyền.",
        ["Lan truyền tin giả có thể bị xử lý theo Luật An ninh mạng.", "Tôn trọng quyền riêng tư: hỏi ý kiến bạn trước khi chụp ảnh đăng lên mạng."],
        {"scenarios": [{"id": "s1", "prompt": "Một bạn trong lớp quay lén cảnh bạn khác trượt chân ngã và định đăng lên mạng để câu like trêu chọc.", "choices": [{"text": "Khuyên bạn xóa video và không được đăng lên mạng làm nhục bạn bè.", "is_correct": True, "feedback": "Rất đáng khen! Em đã bảo vệ danh dự và quyền riêng tư của bạn."}, {"text": "Chia sẻ video đó cho nhiều người khác cùng cười chế giễu.", "is_correct": False, "feedback": "Đó là hành vi bắt nạt trên mạng (Cyberbullying) rất đáng lên án!"}]}]},
        [{"question": "Hành vi nào sau đây vi phạm bản quyền và đạo đức số?", "options": ["Tải tranh của người khác về rồi tự nhận là tranh do mình vẽ", "Mua phần mềm bản quyền chính hãng", "Trích dẫn nguồn bài viết đầy đủ"], "answer": 0, "explanation": "Nhận vơ tác phẩm của người khác là hành vi đạo văn, vi phạm bản quyền."}],
        "Em là một công dân số có tinh thần trách nhiệm và lòng nhân ái cao đẹp!"
    ))

    nodes.append(make_lesson(
        "G5-06", "w1", 5, "Soạn thảo Nâng cao & Chèn Bảng biểu", "Chủ đề E: Ứng dụng tin học",
        "Bài 6, 7: Định dạng nâng cao & Thực hành", "Bài 7: Soạn thảo văn bản nâng cao", "Bài 6: Soạn thảo chèn bảng biểu",
        "sort-drag", ["G4-08"], 6,
        ["Tạo danh sách dấu đầu dòng (Bullets) và số thứ tự (Numbering).", "Chèn bảng dữ liệu (Table), thêm bớt hàng cột và gộp ô."],
        "Thiết kế bản báo cáo học tập chuyên nghiệp có bảng biểu và gạch đầu dòng rõ ràng!",
        "Chức năng Bullets and Numbering giúp liệt kê các ý rành mạch. Bảng (Table) gồm các hàng (Rows) và cột (Columns), giao điểm của hàng và cột gọi là ô (Cell).",
        ["Chọn thẻ Table Design để đổi màu viền và màu nền bảng biểu.", "Chọn thẻ Layout để gộp nhiều ô thành một ô lớn (Merge Cells)."],
        {"groups": [{"id": "g1", "name": "Công cụ Danh sách Liệt kê (List)"}, {"id": "g2", "name": "Công cụ Bảng biểu (Table)"}], "items": [{"id":"1","name":"Tạo danh sách dấu chấm tròn Bullets","group":"g1","icon":"•"},{"id":"2","name":"Đánh số thứ tự tự động 1, 2, 3...","group":"g1","icon":"🔢"},{"id":"3","name":"Chèn bảng 4 hàng 5 cột vào văn bản","group":"g2","icon":"📊"},{"id":"4","name":"Gộp 3 ô hàng trên cùng làm tiêu đề bảng","group":"g2","icon":"🔲"}]},
        [{"question": "Trong phần mềm soạn thảo văn bản, giao điểm giữa một hàng và một cột được gọi là gì?", "options": ["Ô (Cell)", "Thư mục", "Đoạn văn"], "answer": 0, "explanation": "Giao điểm giữa hàng và cột trong bảng biểu được gọi là ô tính (Cell)."}],
        "Văn bản báo cáo có bảng biểu của em trông cực kỳ chuyên nghiệp!"
    ))

    nodes.append(make_lesson(
        "G5-07", "w1", 5, "Bảng tính Điện tử & Tổ chức Dữ liệu", "Chủ đề E: Ứng dụng tin học",
        "Bài 8: Thu thập và sắp xếp dữ liệu", "Bài 5, 6: Thu thập & Xử lý dữ liệu", "Bài 5: Bảng tính & Dữ liệu",
        "sort-drag", ["G5-06"], 6,
        ["Làm quen giao diện phần mềm bảng tính (Excel/Sheets).", "Nhập số liệu và sắp xếp thứ tự tăng dần/giảm dần."],
        "Làm quen với chiếc máy tính thần kỳ có thể tính toán hàng ngàn con số trong 1 giây!",
        "Phần mềm bảng tính gồm các cột đặt tên bằng chữ cái (A, B, C...) và các hàng đánh số (1, 2, 3...). Địa chỉ ô tính được ghép từ tên cột và số hàng (ví dụ: A1, C5).",
        ["Tính năng Sort A->Z sắp xếp dữ liệu tăng dần.", "Tính năng Sort Z->A sắp xếp dữ liệu giảm dần."],
        {"groups": [{"id": "g1", "name": "Địa chỉ Ô tính Hợp lệ"}, {"id": "g2", "name": "Thao tác Xử lý Bảng tính"}], "items": [{"id":"1","name":"Ô tính B5 (Cột B, Hàng 5)","group":"g1","icon":"🎯"},{"id":"2","name":"Ô tính D10 (Cột D, Hàng 10)","group":"g1","icon":"📍"},{"id":"3","name":"Sắp xếp điểm kiểm tra từ cao xuống thấp","group":"g2","icon":"🔽"},{"id":"4","name":"Tính tổng số tiền thu được trong tuần","group":"g2","icon":"➕"}]},
        [{"question": "Ô nằm ở giao điểm của cột C và hàng 8 có địa chỉ là gì?", "options": ["C8", "8C", "C-8"], "answer": 0, "explanation": "Quy ước địa chỉ ô tính luôn viết chữ cái cột trước, số hàng sau: C8."}],
        "Em đã bước đầu làm chủ phần mềm bảng tính xử lý dữ liệu hiện đại!"
    ))

    nodes.append(make_lesson(
        "G5-08", "w1", 5, "Thiết kế Bài Trình chiếu Đa phương tiện", "Chủ đề E: Ứng dụng tin học",
        "Bài 9, 10: Trình chiếu đa phương tiện", "Bài 8: Bài trình chiếu đa phương tiện", "Bài 7: Thiết kế thuyết trình",
        "sort-drag", ["G4-09"], 6,
        ["Nhúng video clip và âm thanh vào trang chiếu.", "Thiết lập hiệu ứng hoạt cảnh Animation xuất hiện theo thứ tự nói."],
        "Đưa bài thuyết trình lên tầm cao mới với âm thanh và thước phim sống động!",
        "Trình chiếu đa phương tiện kết hợp chữ viết, hình ảnh, âm thanh lồng tiếng và video thực tế giúp bài thuyết trình cuốn hút, lôi cuốn người nghe từ đầu đến cuối.",
        ["Vào Insert -> Video để nhúng đoạn phim minh họa.", "Điều chỉnh thời gian xuất hiện hiệu ứng ăn khớp với lời phát biểu."],
        {"groups": [{"id": "g1", "name": "Thành phần Đa phương tiện (Media)"}, {"id": "g2", "name": "Thiết lập Trình diễn (Presentation)"}], "items": [{"id":"1","name":"Nhúng đoạn phim tư liệu lịch sử .mp4","group":"g1","icon":"🎬"},{"id":"2","name":"Chèn bài nhạc nền nhẹ nhàng .mp3","group":"g1","icon":"🎵"},{"id":"3","name":"Bật chế độ Trình chiếu toàn màn hình (F5)","group":"g2","icon":"🖥️"},{"id":"4","name":"Sử dụng bút chỉ laser trên màn hình","group":"g2","icon":"🔴"}]},
        [{"question": "Phím tắt nào trên bàn phím dùng để bắt đầu trình chiếu từ slide đầu tiên?", "options": ["Phím F5", "Phím Enter", "Phím Esc"], "answer": 0, "explanation": "F5 là phím tắt kinh điển để bắt đầu trình chiếu toàn màn hình."}],
        "Bài thuyết trình đa phương tiện của em đạt chất lượng xuất sắc!"
    ))

    nodes.append(make_lesson(
        "G5-09", "w1", 5, "Khái niệm Biến số trong Lập trình", "Chủ đề F: Giải quyết vấn đề",
        "Bài 11: Làm quen với biến trong lập trình", "Bài 9: Giới thiệu biến số Scratch", "Bài 8: Biến số & Lưu trữ dữ liệu",
        "logic-puzzle", ["G4-14"], 8,
        ["Hiểu biến (Variable) là chiếc hộp có tên dùng để lưu trữ dữ liệu.", "Nhận biết giá trị của biến có thể thay đổi trong quá trình chạy."],
        "Khám phá chiếc hộp ma thuật lưu trữ mọi thông tin trong trò chơi điện tử!",
        "Biến số giống như một chiếc hộp được dán nhãn tên (ví dụ: DiemSo). Khi người chơi ghi điểm, giá trị chứa bên trong hộp sẽ được cộng thêm lên.",
        ["Biến phải được đặt tên gợi nhớ ý nghĩa (Diem, Mau, ThoiGian).", "Khởi tạo biến: gán giá trị ban đầu cho biến (thường đặt DiemSo = 0 lúc đầu ván)."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [5, 10, 12]},
        [{"question": "Khi bắt đầu một ván chơi game bắn bóng, biến 'Điểm số' nên được thiết lập bằng bao nhiêu?", "options": ["Đặt DiemSo = 0", "Đặt DiemSo = 100", "Không cần đặt gì"], "answer": 0, "explanation": "Lúc bắt đầu ván đấu, điểm số người chơi luôn được khởi tạo về 0."}],
        "Em đã nắm vững khái niệm biến số - nền tảng của mọi ngôn ngữ lập trình!"
    ))

    nodes.append(make_lesson(
        "G5-10", "w1", 5, "Lập trình Biến số & Tính điểm trong Scratch", "Chủ đề F: Giải quyết vấn đề",
        "Bài 12: Sử dụng biến trong Scratch", "Bài 10: Sử dụng biến để đếm điểm", "Bài 9: Thực hành tính toán biến số",
        "block-maze", ["G5-09"], 7,
        ["Tạo biến mới trong bảng lệnh Variables của Scratch.", "Sử dụng lệnh: Đặt biến thành... và Thay đổi biến một lượng..."],
        "Lập trình cơ chế tính điểm thưởng combo khi chú Mèo bắt được chuột!",
        "Trong nhóm lệnh Variables (màu cam), ta bấm 'Make a Variable' để tạo biến. Dùng khối 'change Diem by 1' để cộng 1 điểm mỗi khi hoàn thành nhiệm vụ.",
        ["Lệnh 'set [Diem] to 0': đặt lại điểm số.", "Lệnh 'change [Diem] by 1': tăng biến điểm lên 1 đơn vị."],
        {"grid_size": 4, "start": {"x": 0, "y": 0, "dir": "E"}, "target": {"x": 3, "y": 2}, "walls": [{"x": 1, "y": 0}, {"x": 2, "y": 2}], "allowed_blocks": ["forward", "turn_right", "turn_left"], "max_blocks": 8},
        [{"question": "Để tăng giá trị của biến Điểm lên 5 đơn vị trong Scratch, em dùng khối lệnh nào?", "options": ["Thay đổi Điểm một lượng 5 (change Diem by 5)", "Đặt Điểm thành 5 (set Diem to 5)", "Hiện biến Điểm"], "answer": 0, "explanation": "'change by 5' là lệnh cộng dồn thêm 5 điểm vào giá trị hiện tại."}],
        "Hệ thống tính điểm trò chơi của em hoạt động rất mượt mà!"
    ))

    nodes.append(make_lesson(
        "G5-11", "w1", 5, "Cấu trúc Điều kiện Rẽ nhánh (If - Else)", "Chủ đề F: Giải quyết vấn đề",
        "Bài 13: Cấu trúc rẽ nhánh", "Bài 11, 12: Điều kiện Nếu... Thì...", "Bài 10, 11: Rẽ nhánh thuật toán",
        "logic-puzzle", ["G5-09"], 8,
        ["Hiểu cấu trúc rẽ nhánh dạng thiếu: Nếu <Điều kiện> Thì...", "Hiểu cấu trúc rẽ nhánh dạng đủ: Nếu <Điều kiện> Thì... Không thì..."],
        "Dạy cho máy tính khả năng tự phán đoán và ra quyết định thông minh!",
        "Cấu trúc rẽ nhánh giúp chương trình lựa chọn hướng đi tùy theo điều kiện thực tế. Ví dụ: Nếu Điểm >= 100 thì thông báo Chiến thắng, Không thì Tiếp tục chơi.",
        ["Điều kiện là biểu thức logic chỉ nhận giá trị Đúng hoặc Sai.", "Trong Scratch dùng khối 'if... then' và khối 'if... then... else'."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [3, 7, 15]},
        [{"question": "Nếu điều kiện trong khối lệnh 'if <chạm vào gai nhọn> then' là ĐÚNG, máy tính sẽ làm gì?", "options": ["Thực hiện các khối lệnh nằm bên trong khối if (ví dụ: trừ mạng)", "Bỏ qua không làm gì", "Tắt máy tính"], "answer": 0, "explanation": "Khi điều kiện đúng, các lệnh nằm trong thân khối if sẽ được thực thi."}],
        "Tư duy logic rẽ nhánh có điều kiện của em cực kỳ sắc bén!"
    ))

    nodes.append(make_lesson(
        "G5-12", "w1", 5, "Thực hành Lập trình Game Rẽ nhánh & Va chạm", "Chủ đề F: Giải quyết vấn đề",
        "Bài 14, 15: Tạo chương trình rẽ nhánh & Trò chơi", "Bài 13, 14: Game mê cung & Đối kháng", "Bài 12, 14: Vòng lặp rẽ nhánh & Đố vui",
        "block-maze", ["G5-10", "G5-11"], 7,
        ["Kết hợp khối lặp liên tục (forever) và khối rẽ nhánh (if... then).", "Sử dụng khối cảm biến va chạm: touching [chướng ngại vật]?"],
        "Xây dựng hoàn chỉnh trò chơi Chú Mèo vượt chướng ngại vật nhặt tiền vàng!",
        "Bằng cách lồng khối 'if touching [coin] then change Diem by 1' vào bên trong vòng lặp 'forever', trò chơi sẽ liên tục kiểm tra va chạm trong suốt thời gian người chơi điều khiển.",
        ["Khối cảm biến Sensing (màu xanh lơ) phát hiện va chạm.", "Âm thanh vui nhộn kích hoạt mỗi khi ăn được tiền thưởng."],
        {"grid_size": 4, "start": {"x": 0, "y": 0, "dir": "E"}, "target": {"x": 3, "y": 3}, "walls": [{"x": 1, "y": 2}, {"x": 2, "y": 1}], "allowed_blocks": ["forward", "turn_right", "turn_left"], "max_blocks": 8},
        [{"question": "Khối lệnh nào trong Scratch dùng để kiểm tra nhân vật có đang chạm vào chướng ngại vật hay không?", "options": ["Khối cảm biến chạm Đang chạm [Tên vật]? (touching...?)", "Khối di chuyển 10 bước", "Khối nói Xin chào"], "answer": 0, "explanation": "touching...? là khối cảm biến nhận diện va chạm giữa các đối tượng."}],
        "Trò chơi của em tương tác rất hấp dẫn và cuốn hút!"
    ))

    nodes.append(make_lesson(
        "G5-13", "w1", 5, "Phát hiện & Gỡ lỗi (Debugging) Chương trình", "Chủ đề F: Giải quyết vấn đề",
        "Bài 16: Ôn tập và kiểm thử", "Bài 15: Kiểm thử và sửa lỗi", "Bài 13: Phát hiện và sửa lỗi",
        "bug-hunt", ["G5-12"], 8,
        ["Hiểu khái niệm lỗi lập trình (Bug) và quá trình gỡ lỗi (Debugging).", "Biết đọc từng khối lệnh để tìm nguyên nhân chương trình chạy sai ý muốn."],
        "Trở thành thợ săn Bug huyền thoại, giải cứu mã nguồn trò chơi khỏi các lỗi ngớ ngẩn!",
        "Lỗi chương trình có thể do: quên khởi tạo điểm về 0, đặt nhầm hướng di chuyển, hoặc quên đặt khối lệnh bên trong vòng lặp liên tục. Gỡ lỗi là kỹ năng quan trọng nhất của lập trình viên.",
        ["Chạy thử từng phần nhỏ của chương trình để cô lập lỗi.", "Đọc kỹ thứ tự các khối lệnh từ trên xuống dưới."],
        {},
        [{"question": "Khi chơi game hứng táo, tại sao khi hứng được táo mà điểm số không tăng lên?", "options": ["Do quên đặt khối lệnh 'Thay đổi Điểm một lượng 1' bên trong khối kiểm tra va chạm", "Do máy tính bị hết pin", "Do màn hình hiển thị bị mờ"], "answer": 0, "explanation": "Quên lệnh cộng điểm là lỗi logic rất phổ biến trong lập trình game."}],
        "Em đã tiêu diệt toàn bộ các Bug lỗi và hoàn thiện mã nguồn tuyệt đối!"
    ))

    nodes.append(make_lesson(
        "G5-14", "w1", 5, "Ôn tập & Đánh giá Toàn diện Cấp Tiểu học", "Tổng kết Toàn diện Tiểu học",
        "Bài 16: Tổng kết & Dự án học tập 5", "Bài 16: Trình bày và chia sẻ sản phẩm số", "Bài 15, 16: Cuộc thi Tin học trẻ & Tổng kết",
        "boss-quiz", ["G5-01", "G5-02", "G5-07", "G5-10", "G5-12"], 12,
        ["Tổng kết toàn bộ chuẩn kiến thức Tin học cấp Tiểu học (Lớp 3, 4, 5) của cả 3 bộ sách.", "Sẵn sàng nhận bằng Vinh Danh Tốt Nghiệp Tiểu Học EasyTin."],
        "Hãy vận dụng toàn bộ kiến thức Tin học của 3 năm học Tiểu học để hoàn thành xuất sắc bài đánh giá năng lực cuối cấp!",
        "Bài đánh giá tổng hợp: Phần cứng máy tính, Xử lý bảng tính, Biến số trong lập trình và Thuật toán rẽ nhánh Scratch.",
        ["Kiến trúc máy tính: CPU, RAM, Ổ cứng.", "Kỹ năng lập trình biến số, điều kiện rẽ nhánh và an toàn số."],
        {"boss_name": "Thử thách Đánh giá Cuối Cấp Tiểu học", "boss_max_hp": 100, "player_max_hp": 100, "damage_per_hit": 25, "questions_pool": 4},
        [
            {"question": "Bộ phận nào trong thân máy tính thực hiện lưu trữ dữ liệu tạm thời và mất khi tắt điện?", "options": ["RAM", "Ổ đĩa cứng SSD", "Bộ xử lý CPU", "Nguồn điện"], "answer": 0, "explanation": "RAM lưu dữ liệu tạm thời khi máy đang chạy."},
            {"question": "Trong Scratch, chiếc hộp dùng để lưu điểm số và có thể thay đổi giá trị gọi là gì?", "options": ["Biến số (Variable)", "Sân khấu (Stage)", "Nhân vật (Sprite)", "Âm thanh (Sound)"], "answer": 0, "explanation": "Biến số là nơi lưu trữ giá trị thay đổi trong chương trình."},
            {"question": "Trong phần mềm bảng tính, công thức luôn luôn phải bắt đầu bằng ký tự nào?", "options": ["Dấu bằng (=)", "Dấu cộng (+)", "Dấu chấm hỏi (?)", "Dấu gạch ngang (-)"], "answer": 0, "explanation": "Dấu bằng (=) báo hiệu cho bảng tính biết đây là công thức tính toán."},
            {"question": "Quy tắc an toàn nào giúp bảo vệ mắt khi ngồi máy tính?", "options": ["Quy tắc 20-20-20 (nghỉ ngơi nhìn xa)", "Ngồi càng gần màn hình càng tốt", "Học thâu đêm không ngủ", "Vừa ăn vừa gõ phím"], "answer": 0, "explanation": "Quy tắc 20-20-20 giúp mắt thư giãn chống cận thị."}
        ],
        "CHÚC MỪNG EM! Em đã hoàn thành xuất sắc toàn diện chương trình Tin học Cấp Tiểu học (Lớp 3, 4, 5) của cả 3 bộ sách!"
    ))

    return nodes

print("curriculum_data_g3_g5 loaded")
