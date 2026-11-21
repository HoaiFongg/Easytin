# -*- coding: utf-8 -*-
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
# LỚP 3 (TIỂU HỌC - THẾ GIỚI 1)
# ==============================================================================
nodes.append(create_lesson(
    "G3-INFO-01", "w1", 3, "Thông tin và Quyết định", "Chủ đề A: Máy tính và em",
    "Bài 1: Thông tin và quyết định", "Bài 2: Nhận biết thông tin", "Bài 1: Thông tin và tiếp nhận",
    "branch-story", [], 5,
    ["Nhận biết được thông tin xung quanh thu nhận qua các giác quan.", "Hiểu được thông tin giúp con người đưa ra quyết định đúng đắn."],
    "Buổi sáng thức dậy, em nghe tiếng chuông báo thức reo và nhìn thấy ngoài trời đang mưa to. Tiếng chuông và cơn mưa là thông tin, em sẽ quyết định làm gì tiếp theo?",
    "Thông tin là những hiểu biết về thế giới xung quanh thu nhận qua mắt, tai, mũi, lưỡi và da.",
    ["Thông tin giúp em đưa ra hành động và quyết định phù hợp trong cuộc sống.", "Mắt giúp nhìn thấy màu sắc, chữ viết, hình ảnh.", "Tai giúp nghe thấy âm thanh, tiếng nói, tiếng chuông."],
    {
        "scenarios": [
            {
                "id": "s1",
                "prompt": "Em nhìn thấy đèn tín hiệu giao thông chuyển sang màu ĐỎ. Em sẽ đưa ra quyết định gì?",
                "choices": [
                    {"text": "Dừng lại trước vạch kẻ đường an toàn.", "is_correct": True, "feedback": "Chính xác! Đèn đỏ là thông tin báo hiệu phải dừng lại."},
                    {"text": "Tiếp tục chạy thật nhanh qua đường.", "is_correct": False, "feedback": "Rất nguy hiểm! Đèn đỏ báo hiệu bắt buộc phải dừng xe."}
                ]
            }
        ]
    },
    [
        {"question": "Giác quan nào giúp em nhìn thấy màu sắc của chiếc cặp sách?", "options": ["Tai", "Mắt", "Mũi", "Lưỡi"], "answer": 1, "explanation": "Mắt là cơ quan thị giác giúp em thu nhận thông tin hình ảnh và màu sắc."},
        {"question": "Khi nghe tiếng còi báo cháy, thông tin này giúp em quyết định điều gì?", "options": ["Đi ngủ tiếp", "Bật nhạc to hơn", "Nhanh chóng sơ tán ra nơi an toàn", "Mở tivi xem phim"], "answer": 2, "explanation": "Tiếng còi báo cháy là thông tin nguy hiểm, giúp em quyết định sơ tán ngay lập tức."}
    ],
    "Em đã hiểu thông tin là gì và cách thông tin dẫn lối cho mọi quyết định đúng đắn!"
))

nodes.append(create_lesson(
    "G3-PROC-02", "w1", 3, "Xử lý Thông tin trong Đời sống", "Chủ đề A: Máy tính và em",
    "Bài 2: Xử lý thông tin", "Bài 2: Nhận biết thông tin", "Bài 2: Xử lý thông tin",
    "sort-drag", ["G3-INFO-01"], 6,
    ["Nêu được 4 hoạt động cơ bản: Thu nhận, Lưu trữ, Xử lý và Truyền thông tin.", "Lấy được ví dụ cụ thể về xử lý thông tin của con người và máy tính."],
    "Bộ não của bạn nhỏ và máy tính giống như một nhà máy kỳ diệu! Hãy giúp bạn phân loại các hành động vào đúng 4 công đoạn xử lý thông tin nhé!",
    "Quá trình xử lý thông tin luôn trải qua 4 bước liên hoàn:",
    ["1. Thu nhận: Tiếp nhận dữ liệu từ bên ngoài (nhìn, nghe, gõ phím).", "2. Lưu trữ: Ghi nhớ vào não hoặc lưu vào đĩa nhớ của máy tính.", "3. Xử lý: Suy nghĩ, tính toán, biến đổi dữ liệu thành kết quả.", "4. Truyền đạt: Nói ra, in ra màn hình hoặc gửi cho người khác."],
    {
        "groups": [
            {"id": "input", "name": "Thu nhận & Lưu trữ"},
            {"id": "process", "name": "Xử lý & Truyền đạt"}
        ],
        "items": [
            {"id": "hear", "name": "Lắng nghe cô giảng bài", "group": "input", "icon": "👂"},
            {"id": "write", "name": "Chép bài vào vở", "group": "input", "icon": "📓"},
            {"id": "think", "name": "Tính nhẩm phép nhân", "group": "process", "icon": "🧠"},
            {"id": "speak", "name": "Phát biểu câu trả lời", "group": "process", "icon": "🗣️"}
        ]
    },
    [
        {"question": "Hành động em chép bài tập vào vở thuộc công đoạn nào?", "options": ["Xử lý thông tin", "Lưu trữ thông tin", "Thu nhận thông tin", "Xóa thông tin"], "answer": 1, "explanation": "Chép bài vào vở là lưu trữ thông tin để xem lại sau này."}
    ],
    "Tuyệt vời! Em đã thành thạo quy trình 4 bước xử lý thông tin!"
))

nodes.append(create_lesson(
    "G3-HARD-01", "w1", 3, "Máy tính – Những người bạn mới", "Chủ đề A: Máy tính và em",
    "Bài 3: Máy tính - những người bạn mới", "Bài 1: Làm quen với máy tính", "Bài 3: Em làm quen máy tính",
    "sort-drag", [], 5,
    ["Chỉ đúng tên và vị trí 4 bộ phận cơ bản của máy tính để bàn.", "Nhận biết máy tính xách tay và máy tính bảng."],
    "Chào mừng bạn nhỏ đến với phòng thực hành! Các linh kiện máy tính đang chờ được kết nối để khởi động, em hãy giúp phân loại nhé!",
    "Máy tính để bàn gồm 4 bộ phận chính: Thân máy, Màn hình, Bàn phím và Chuột.",
    ["Thân máy chứa bộ vi xử lý và ổ cứng, là 'não bộ' điều khiển mọi hoạt động.", "Màn hình là thiết bị xuất hiển thị chữ và hình ảnh.", "Bàn phím và chuột là thiết bị nhập gửi lệnh từ người dùng vào máy tính."],
    {
        "groups": [
            {"id": "in_dev", "name": "Bộ phận nhập lệnh (Vào)"},
            {"id": "out_dev", "name": "Bộ phận xử lý & hiển thị (Não & Ra)"}
        ],
        "items": [
            {"id": "mouse", "name": "Chuột máy tính", "group": "in_dev", "icon": "🖱️"},
            {"id": "keyboard", "name": "Bàn phím", "group": "in_dev", "icon": "⌨️"},
            {"id": "screen", "name": "Màn hình hiển thị", "group": "out_dev", "icon": "🖥️"},
            {"id": "case", "name": "Thân máy (CPU)", "group": "out_dev", "icon": "🗄️"}
        ]
    },
    [
        {"question": "Bộ phận nào được coi là 'bộ não' của máy tính?", "options": ["Bàn phím", "Màn hình", "Thân máy", "Chuột"], "answer": 2, "explanation": "Thân máy chứa vi xử lý trung tâm điều khiển toàn bộ máy tính."}
    ],
    "Em đã thuộc tên và chức năng của những người bạn máy tính thân thiết!"
))

nodes.append(create_lesson(
    "G3-MOUSE-01", "w1", 3, "Thao tác Chuột điêu luyện", "Chủ đề A: Máy tính và em",
    "Bài 4: Làm việc với máy tính", "Bài 3: Em tập dùng chuột", "Bài 4: Chuột máy tính",
    "sort-drag", ["G3-HARD-01"], 5,
    ["Cầm chuột đúng cách bằng tay phải.", "Thực hiện thành thạo: Di chuyển, Nháy chuột, Nháy đúp, Kéo thả."],
    "Để điều khiển chú robot TinTin, em cần nắm vững các tuyệt chiêu điều khiển chuột máy tính!",
    "Chuột máy tính có nút trái, nút phải và nút cuộn ở giữa.",
    ["Nháy chuột: Nhấn nút trái chuột một lần rồi thả ra.", "Nháy đúp: Nhấn nút trái chuột hai lần liên tiếp thật nhanh.", "Kéo thả chuột: Nhấn giữ nút trái, di chuyển đến vị trí mới rồi thả tay."],
    {
        "groups": [
            {"id": "left_btn", "name": "Thao tác Nút Trái"},
            {"id": "scroll", "name": "Thao tác Nút Cuộn & Nút Phải"}
        ],
        "items": [
            {"id": "click", "name": "Nháy chuột chọn biểu tượng", "group": "left_btn", "icon": "👆"},
            {"id": "dblclick", "name": "Nháy đúp mở phần mềm", "group": "left_btn", "icon": "✌️"},
            {"id": "scroll_action", "name": "Lăn cuộn trang web lên xuống", "group": "scroll", "icon": "🔄"},
            {"id": "right_click", "name": "Nháy nút phải mở menu", "group": "scroll", "icon": "📋"}
        ]
    },
    [
        {"question": "Để mở một phần mềm trò chơi trên màn hình, em thường thao tác chuột như thế nào?", "options": ["Nháy nút phải", "Lăn nút cuộn", "Nháy đúp chuột trái", "Giữ nút trái 10 giây"], "answer": 2, "explanation": "Nháy đúp chuột trái (nhấn 2 lần nhanh) dùng để khởi chạy ứng dụng."}
    ],
    "Tay em đã lướt chuột cực kỳ chuẩn xác và nhanh nhẹn!"
))

nodes.append(create_lesson(
    "G3-KEY-01", "w1", 3, "Làm quen Bàn phím & Khu vực phím chính", "Chủ đề A: Máy tính và em",
    "Bài 5: Sử dụng bàn phím", "Bài 4: Em tập dùng bàn phím", "Bài 5: Bàn phím máy tính",
    "type-run", ["G3-HARD-01"], 6,
    ["Nhận biết các hàng phím: Hàng phím số, hàng phím trên, hàng cơ sở, hàng phím dưới.", "Nhận biết hai phím có gai F và J để đặt ngón trỏ."],
    "Đường đua gõ phím bắt đầu! Hãy ghi nhớ vị trí hàng phím cơ sở và gõ thật chuẩn xác nhé!",
    "Hàng phím cơ sở là quan trọng nhất vì tay em luôn nghỉ ngơi tại đây.",
    ["Hai phím có gai F và J giúp ngón trỏ định vị mà không cần nhìn bàn phím.", "Phím Space (phím cách) dài nhất dùng ngón cái để gõ khoảng trắng.", "Phím Enter dùng để xuống dòng hoặc đồng ý thực hiện lệnh."],
    {},
    [
        {"question": "Hai phím nào trên hàng phím cơ sở có gờ gai nhỏ để định vị ngón tay trỏ?", "options": ["A và L", "F và J", "G và H", "Q và P"], "answer": 1, "explanation": "Phím F (ngón trỏ trái) và J (ngón trỏ phải) có gai để cảm nhận vị trí chuẩn."}
    ],
    "Đôi tay em đã gõ phím rất nhịp nhàng trên hàng cơ sở!"
))

nodes.append(create_lesson(
    "G3-NET-01", "w1", 3, "Khám phá Thế giới qua Internet", "Chủ đề B: Mạng máy tính và Internet",
    "Bài 6: Khám phá thông tin trên Internet", "Chủ đề B - Bài 1: Thông tin trên Internet", "Bài 6: Khám phá thế giới qua Internet",
    "branch-story", [], 6,
    ["Nhận biết Internet là kho thông tin khổng lồ toàn cầu.", "Biết nhờ người lớn hướng dẫn khi tìm kiếm thông tin trên mạng."],
    "Internet giống như một thư viện kỳ diệu không biên giới! Nhưng trong thư viện cũng có những cuốn sách chưa phù hợp với lứa tuổi của em. Em sẽ khám phá như thế nào?",
    "Internet kết nối hàng triệu máy tính trên thế giới với nhau:",
    ["Em có thể xem tranh ảnh động vật, nghe bài hát thiếu nhi, học tiếng Anh trên mạng.", "Luôn đồng hành cùng cha mẹ hoặc thầy cô khi lướt web.", "Không tự ý bấm vào các đường link lạ hoặc quảng cáo nhấp nháy."],
    {
        "scenarios": [
            {
                "id": "s1",
                "prompt": "Khi đang xem video học tập, một trang web lạ xuất hiện mời em tải trò chơi bí mật.",
                "choices": [
                    {"text": "Bấm tải ngay lập tức về máy tính.", "is_correct": False, "feedback": "Nguy hiểm! Trang web lạ có thể chứa vi-rút làm hỏng máy."},
                    {"text": "Đóng trang web lại và hỏi ý kiến người lớn.", "is_correct": True, "feedback": "Rất sáng suốt! Luôn nhờ người lớn kiểm tra trước khi tải tệp."}
                ]
            }
        ]
    },
    [
        {"question": "Khi muốn tìm video hướng dẫn gấp hạc giấy trên Internet, em nên làm gì?", "options": ["Tự mở mọi liên kết trên màn hình", "Nhờ bố mẹ hoặc thầy cô hướng dẫn tìm kiếm an toàn", "Bấm vào các quảng cáo trúng thưởng", "Tắt máy tính ngay"], "answer": 1, "explanation": "Nhờ người lớn giúp đỡ sẽ đảm bảo em tiếp cận nguồn thông tin an toàn."}
    ],
    "Em đã trở thành nhà thám hiểm Internet thông thái và cẩn trọng!"
))

nodes.append(create_lesson(
    "G3-FILE-01", "w1", 3, "Sắp xếp Đồ vật, Tệp và Thư mục cây", "Chủ đề C: Tổ chức lưu trữ thông tin",
    "Bài 7, 8: Sắp xếp để dễ tìm. Tệp và thư mục", "Chủ đề C - Bài 1, 2: Cây thư mục và tệp", "Bài 7: Sắp xếp tệp và thư mục",
    "sort-drag", [], 6,
    ["Hiểu lợi ích của việc sắp xếp đồ vật và thông tin ngăn nắp.", "Phân biệt được Thư mục (ngăn chứa) và Tệp (tài liệu, hình ảnh, bài hát)."],
    "Bàn học bừa bộn sẽ làm em mất cả tiếng đồng hồ để tìm một cây bút chì! Máy tính cũng vậy, nếu không có Thư mục, dữ liệu sẽ bị lạc mất!",
    "Thư mục giống như chiếc cặp sách, bên trong chứa các tệp và các thư mục con:",
    ["Tệp (File): Chứa nội dung cụ thể như bài văn Word, tranh vẽ Paint, bài hát.", "Thư mục (Folder): Biểu tượng màu vàng dùng để gom nhóm các tệp cùng loại.", "Sơ đồ cây giúp tìm kiếm thông tin nhanh chóng và khoa học."],
    {
        "groups": [
            {"id": "folder_pic", "name": "Thư mục 'Hinh_Anh'"},
            {"id": "folder_doc", "name": "Thư mục 'Bai_Hoc'"}
        ],
        "items": [
            {"id": "p1", "name": "Tranh_Ve_Meo.png", "group": "folder_pic", "icon": "🖼️"},
            {"id": "p2", "name": "Anh_Gia_Dinh.jpg", "group": "folder_pic", "icon": "📷"},
            {"id": "d1", "name": "Bai_Tap_Toan.docx", "group": "folder_doc", "icon": "📄"},
            {"id": "d2", "name": "Tap_Lam_Van.docx", "group": "folder_doc", "icon": "📝"}
        ]
    },
    [
        {"question": "Biểu tượng nào trong máy tính thường đại diện cho một thư mục?", "options": ["Tờ giấy trắng", "Chiếc kẹp màu vàng", "Chiếc đĩa CD", "Chiếc kéo"], "answer": 1, "explanation": "Thư mục thường có biểu tượng chiếc kẹp/cặp tài liệu màu vàng."}
    ],
    "Kho dữ liệu của em giờ đây đã ngăn nắp và khoa học như một thư viện chuẩn mực!"
))

nodes.append(create_lesson(
    "G3-SAFE-01", "w1", 3, "Sử dụng Máy tính An toàn & Đúng cách", "Chủ đề D: Đạo đức, pháp luật môi trường số",
    "Bài 9: An toàn với máy tính", "Chủ đề D - Bài 1: An toàn khi dùng máy tính", "Bài 8: Sử dụng máy tính an toàn",
    "branch-story", [], 5,
    ["Biết ngồi đúng tư thế khi học máy tính để tránh cận thị và gù lưng.", "Tuân thủ an toàn điện: không chạm tay vào dây nguồn, không ăn uống gần máy."],
    "Bảo vệ sức khỏe và an toàn điện là quy tắc số một của mọi kỹ sư công nghệ tương lai!",
    "Quy tắc vàng khi ngồi trước máy tính:",
    ["Tư thế ngồi thẳng lưng, mắt cách màn hình 50 - 70 cm.", "Cứ sau 30 phút học tập, cho mắt nghỉ ngơi 2 - 3 phút nhìn ra xa.", "Không đem đồ ăn, nước uống để lên bàn phím."],
    {
        "scenarios": [
            {
                "id": "s1",
                "prompt": "Em đang khát nước khi đang chơi game trên máy tính để bàn.",
                "choices": [
                    {"text": "Đặt ly nước ngọt đầy ngay cạnh bàn phím máy tính.", "is_correct": False, "feedback": "Nguy hiểm! Nước đổ vào bàn phím gây chập điện và hỏng máy."},
                    {"text": "Tạm dừng game, đứng dậy ra bàn ăn uống nước rồi quay lại.", "is_correct": True, "feedback": "Rất chuẩn mực! Em vừa bảo vệ máy tính vừa cho mắt nghỉ ngơi."}
                ]
            }
        ]
    },
    [
        {"question": "Khoảng cách an toàn từ mắt đến màn hình máy tính nên là bao nhiêu?", "options": ["10 - 20 cm", "50 - 70 cm (khoảng một sải tay)", "2 mét", "Càng gần càng tốt"], "answer": 1, "explanation": "50 - 70 cm giúp bảo vệ mắt khỏi mỏi và ngăn ngừa cận thị học đường."}
    ],
    "Em đã nắm vững quy tắc giữ gìn sức khỏe vàng trước màn hình máy tính!"
))

nodes.append(create_lesson(
    "G3-ALGO-01", "w1", 3, "Robot Vượt Mê Cung Lệnh", "Chủ đề F: Giải quyết vấn đề với máy tính",
    "Bài 14, 15: Thực hiện công việc theo các bước", "Chủ đề F - Bài 1, 2: Chia việc thành việc nhỏ", "Bài 12, 13: Các bước thực hiện công việc",
    "block-maze", ["G3-MOUSE-01"], 7,
    ["Biết chia một nhiệm vụ thành các bước tuần tự rõ ràng.", "Lập trình khối lệnh điều khiển robot TinTin về đích."],
    "Robot TinTin đang bị lạc trong mê cung đá! Hãy lập trình các khối lệnh từng bước để đưa TinTin tới viên ngọc năng lượng nhé!",
    "Thuật toán là dãy các chỉ dẫn từng bước rõ ràng để hoàn thành một mục tiêu.",
    ["Máy tính thực hiện chính xác từng lệnh theo thứ tự từ trên xuống dưới.", "Nếu nhầm một lệnh, robot có thể va vào tường.", "Chia việc lớn thành các việc nhỏ giúp giải quyết dễ dàng hơn."],
    {
        "grid_size": 4,
        "start": {"x": 0, "y": 0, "dir": "E"},
        "target": {"x": 2, "y": 2},
        "walls": [{"x": 1, "y": 0}, {"x": 1, "y": 1}],
        "allowed_blocks": ["forward", "turn_left", "turn_right"],
        "max_blocks": 6
    },
    [
        {"question": "Khi ra lệnh cho máy tính, thứ tự các câu lệnh có quan trọng không?", "options": ["Không quan trọng, muốn làm lệnh nào trước cũng được", "Rất quan trọng, máy thực hiện tuần tự từng bước từ trên xuống dưới", "Chỉ làm lệnh cuối cùng", "Máy tự đảo lộn lệnh"], "answer": 1, "explanation": "Thứ tự câu lệnh quyết định kết quả của chương trình máy tính."}
    ],
    "Em vừa hoàn thành thuật toán điều khiển robot xuất sắc đầu tiên của mình!"
))

# ==============================================================================
# LỚP 4 (TIỂU HỌC - THẾ GIỚI 1)
# ==============================================================================
nodes.append(create_lesson(
    "G4-HARD-01", "w1", 4, "Phân loại Phần cứng & Phần mềm", "Chủ đề A: Máy tính và em",
    "Bài 1: Phần cứng và phần mềm", "Bài 1: Phần cứng và phần mềm máy tính", "Bài 1: Phần cứng và phần mềm",
    "sort-drag", ["G3-HARD-01"], 5,
    ["Phân biệt được phần cứng (vật lý) và phần mềm (chương trình).", "Nêu được mối quan hệ: phần mềm điều khiển phần cứng."],
    "Phần cứng như thể xác, còn phần mềm như tâm trí thông minh! Hãy giúp robot phân loại các vật phẩm vào đúng kho nhé!",
    "Máy tính luôn cần cả Phần cứng và Phần mềm để hoạt động:",
    ["Phần cứng (Hardware): Tai nghe, chuột, webcam, đĩa cứng sờ chạm được.", "Phần mềm (Software): Windows, Scratch, Paint, trình duyệt Chrome vô hình."],
    {
        "groups": [
            {"id": "hw", "name": "Kho Phần Cứng"},
            {"id": "sw", "name": "Kho Phần Mềm"}
        ],
        "items": [
            {"id": "mic", "name": "Microphone thu âm", "group": "hw", "icon": "🎤"},
            {"id": "scratch", "name": "Phần mềm Scratch", "group": "sw", "icon": "🐱"},
            {"id": "printer", "name": "Máy in màu", "group": "hw", "icon": "🖨️"},
            {"id": "word", "name": "Phần mềm Word", "group": "sw", "icon": "📄"}
        ]
    },
    [
        {"question": "Trò chơi điện tử em chơi trên máy tính là phần cứng hay phần mềm?", "options": ["Phần cứng", "Phần mềm", "Cả hai", "Không phải loại nào"], "answer": 1, "explanation": "Trò chơi là chương trình phần mềm được cài đặt trên máy tính."}
    ],
    "Chúc mừng em đã phân biệt vanh vách giữa phần cứng và phần mềm!"
))

nodes.append(create_lesson(
    "G4-ETHIC-01", "w1", 4, "Hiệp sĩ An toàn số & Bản quyền", "Chủ đề D: Đạo đức, pháp luật môi trường số",
    "Bài 7: Sử dụng máy tính có văn hóa", "Bài 6: Đạo đức khi dùng mạng", "Bài 6: Bản quyền nội dung số",
    "branch-story", [], 6,
    ["Tôn trọng bản quyền hình ảnh, bài viết của người khác trên mạng.", "Không công khai mật khẩu và số điện thoại cha mẹ cho người lạ."],
    "Một hiệp sĩ số dũng cảm không chỉ giỏi kỹ thuật mà còn có trái tim chính trực và tôn trọng luật pháp!",
    "Bản quyền bảo vệ công sức sáng tạo của tác giả:",
    ["Khi dùng ảnh trên mạng, phải xin phép hoặc ghi rõ nguồn tác giả.", "Không bao giờ tự ý nhận tác phẩm của người khác là của mình.", "Bảo mật tài khoản: đặt mật khẩu mạnh và không chia sẻ cho ai."],
    {
        "scenarios": [
            {
                "id": "s1",
                "prompt": "Em thấy một bài thơ rất hay của bạn cùng lớp và muốn chia sẻ lên nhóm lớp.",
                "choices": [
                    {"text": "Đăng bài thơ và ghi rõ tên bạn là tác giả.", "is_correct": True, "feedback": "Rất đáng khen! Đó là hành vi văn minh và tôn trọng bản quyền."},
                    {"text": "Xóa tên bạn đi và ghi tên mình vào để được khen.", "is_correct": False, "feedback": "Sai trái! Đó là hành vi đạo văn và vi phạm đạo đức số."}
                ]
            }
        ]
    },
    [
        {"question": "Hành vi nào sau đây thể hiện sự tôn trọng bản quyền trên Internet?", "options": ["Tải phim lậu về xem", "Ghi rõ tên tác giả và nguồn khi trích dẫn tài liệu", "Nhận tranh vẽ của bạn là của mình", "Chia sẻ mật khẩu tài khoản"], "answer": 1, "explanation": "Ghi rõ tác giả là quy tắc chuẩn mực thể hiện sự tôn trọng quyền sở hữu trí tuệ."}
    ],
    "Danh hiệu Hiệp sĩ An toàn số đã thuộc về em hoàn toàn xứng đáng!"
))

nodes.append(create_lesson(
    "G4-SCRATCH-01", "w1", 4, "Làm quen Scratch & Điều khiển nhân vật", "Chủ đề F: Giải quyết vấn đề với máy tính",
    "Bài 13, 14: Làm quen Scratch, chuyển động", "Bài 11, 12: Môi trường lập trình trực quan", "Bài 12, 13: Sân khấu và nhân vật Scratch",
    "block-maze", ["G3-ALGO-01"], 7,
    ["Làm quen giao diện Scratch: Sân khấu, Nhân vật, Khu vực khối lệnh.", "Ghép khối lệnh di chuyển 10 bước và xoay 15 độ."],
    "Chào mừng em đến với thế giới phù thủy lập trình Scratch! Nơi em có thể biến mọi ý tưởng hoạt hình thành hiện thực!",
    "Trong Scratch, em là đạo diễn sân khấu:",
    ["Sân khấu (Stage): Nơi nhân vật biểu diễn hành động.", "Khối lệnh Motion (Chuyển động): Giúp nhân vật đi tới, rẽ hướng, nhảy múa.", "Cờ xanh: Nút bấm bắt đầu chạy toàn bộ chương trình kịch bản."],
    {
        "grid_size": 4,
        "start": {"x": 0, "y": 0, "dir": "E"},
        "target": {"x": 3, "y": 0},
        "walls": [],
        "allowed_blocks": ["forward"],
        "max_blocks": 4
    },
    [
        {"question": "Nút bấm nào trong Scratch dùng để bắt đầu chạy chương trình?", "options": ["Nút chấm đỏ", "Lá cờ xanh", "Biểu tượng thùng rác", "Nút dấu cộng"], "answer": 1, "explanation": "Lá cờ xanh (Green Flag) là biểu tượng kích hoạt kịch bản Scratch."}
    ],
    "Em đã sẵn sàng sáng tạo những bộ phim hoạt hình kỳ diệu với Scratch!"
))

# ==============================================================================
# LỚP 5 (TIỂU HỌC - THẾ GIỚI 1)
# ==============================================================================
nodes.append(create_lesson(
    "G5-VAR-01", "w1", 5, "Biến số trong Lập trình Trực quan", "Chủ đề F: Giải quyết vấn đề với máy tính",
    "Bài 8: Biến trong lập trình", "Bài 8: Khái niệm biến số", "Bài 8: Biến trong Scratch",
    "block-maze", ["G4-SCRATCH-01"], 8,
    ["Hiểu biến số là chiếc hộp lưu trữ giá trị có thể thay đổi trong khi chạy chương trình.", "Tạo biến điểm số (Score) và tăng điểm khi nhân vật ăn quà."],
    "Trong trò chơi đuổi bắt, làm sao máy tính nhớ được em đã ăn được bao nhiêu quả táo? Đó chính là nhờ chiếc hộp thần kỳ mang tên Biến số!",
    "Biến số (Variable) là một ô nhớ có tên dùng để lưu trữ dữ liệu:",
    ["Giá trị của biến có thể tăng lên, giảm đi hoặc thay đổi linh hoạt.", "Ví dụ: Biến 'DiemSo' bắt đầu bằng 0, mỗi lần chạm vật phẩm tăng 1.", "Biến 'ThoiGian' đếm lùi từng giây."],
    {
        "grid_size": 4,
        "start": {"x": 0, "y": 0, "dir": "E"},
        "target": {"x": 2, "y": 2},
        "walls": [{"x": 1, "y": 0}],
        "allowed_blocks": ["forward", "turn_right", "turn_left"],
        "max_blocks": 5
    },
    [
        {"question": "Khi nhân vật nhặt được một đồng vàng và điểm số tăng từ 5 lên 6, điều gì đã xảy ra?", "options": ["Chương trình bị lỗi", "Giá trị của biến điểm số đã thay đổi", "Màn hình máy tính bị tắt", "Bàn phím bị kẹt"], "answer": 1, "explanation": "Biến số lưu trữ điểm đã cập nhật giá trị mới tăng thêm 1."}
    ],
    "Em đã làm chủ khái niệm biến số - chìa khóa vàng của mọi trò chơi điện tử!"
))

# ==============================================================================
# LỚP 6 (THCS - THẾ GIỚI 2: RỪNG MẠNG & DỮ LIỆU)
# ==============================================================================
nodes.append(create_lesson(
    "G6-BIN-01", "w2", 6, "Thế giới Số Nhị phân 0 & 1 và Dung lượng", "Chủ đề A: Máy tính và cộng đồng",
    "Bài 3: Thông tin trong máy tính", "Bài 3: Biểu diễn số nhị phân", "Bài 2: Biểu diễn dữ liệu số",
    "logic-puzzle", [], 8,
    ["Hiểu máy tính biểu diễn mọi thông tin văn bản, ảnh, âm thanh bằng dãy bit 0 và 1.", "Nắm vững các đơn vị đo dung lượng: Bit, Byte, KB, MB, GB, TB."],
    "Sâu trong lòng vi mạch bán dẫn, hàng triệu bóng bán dẫn chỉ biết bật hoặc tắt dòng điện. Hãy cùng giải mã ngôn ngữ 0 và 1 của máy tính!",
    "Hệ nhị phân là ngôn ngữ gốc của phần cứng máy tính:",
    ["1 Bit = một chữ số nhị phân (0 hoặc 1).", "1 Byte = 8 Bit (đủ lưu 1 ký tự chữ cái).", "1 KB = 1024 Bytes; 1 MB = 1024 KB; 1 GB = 1024 MB."],
    {
        "bits_count": 4,
        "weights": [8, 4, 2, 1],
        "target_values": [5, 9, 13]
    },
    [
        {"question": "1 Byte bằng bao nhiêu Bit?", "options": ["4 Bit", "8 Bit", "16 Bit", "1024 Bit"], "answer": 1, "explanation": "Theo quy chuẩn quốc tế, 1 Byte tương đương đúng 8 Bit dữ liệu."},
        {"question": "Thẻ nhớ có dung lượng 64 GB chứa được nhiều dữ liệu hơn thẻ nhớ 64 MB bao nhiêu lần?", "options": ["2 lần", "10 lần", "1024 lần", "Không nhiều hơn"], "answer": 2, "explanation": "1 GB = 1024 MB nên 64 GB gấp 1024 lần 64 MB."}
    ],
    "Em đã mở khóa cánh cổng nhị phân sâu thẳm của khoa học máy tính!"
))

nodes.append(create_lesson(
    "G6-NET-01", "w2", 6, "Mạng Máy tính & Thiết bị Mạng", "Chủ đề B: Mạng máy tính và Internet",
    "Bài 4: Mạng máy tính", "Bài 4: Khái niệm mạng máy tính", "Bài 3: Các thành phần của mạng",
    "sort-drag", ["G6-BIN-01"], 7,
    ["Nêu được lợi ích của mạng máy tính: chia sẻ dữ liệu và dùng chung thiết bị.", "Phân biệt mạng có dây (cáp mạng) và mạng không dây (Wi-Fi)."],
    "Nếu các máy tính đứng riêng lẻ, chúng ta không thể gửi tin nhắn hay chia sẻ tệp cho nhau. Mạng máy tính ra đời để kết nối mọi người!",
    "Mạng máy tính gồm thiết bị đầu cuối, thiết bị kết nối và phần mềm mạng:",
    ["Thiết bị đầu cuối: Máy tính để bàn, điện thoại, máy in.", "Thiết bị kết nối: Switch (bộ chuyển mạch), Router (bộ định tuyến), Modem.", "Mạng không dây sử dụng sóng vô tuyến Wi-Fi tiện lợi."],
    {
        "groups": [
            {"id": "end_dev", "name": "Thiết bị Đầu cuối"},
            {"id": "net_dev", "name": "Thiết bị Mạng kết nối"}
        ],
        "items": [
            {"id": "pc", "name": "Máy tính học sinh", "group": "end_dev", "icon": "💻"},
            {"id": "phone", "name": "Điện thoại thông minh", "group": "end_dev", "icon": "📱"},
            {"id": "router", "name": "Bộ phát Wi-Fi (Router)", "group": "net_dev", "icon": "📡"},
            {"id": "switch", "name": "Bộ chia mạng (Switch)", "group": "net_dev", "icon": "🔀"}
        ]
    },
    [
        {"question": "Thiết bị nào sau đây là thiết bị kết nối mạng?", "options": ["Máy quét", "Router (Bộ định tuyến)", "Bàn phím", "Màn hình"], "answer": 1, "explanation": "Router là thiết bị mạng định tuyến các gói tin giữa các mạng máy tính."}
    ],
    "Em đã nắm vững cấu trúc của xa lộ thông tin mạng máy tính!"
))

# ==============================================================================
# LỚP 7 (THCS - THẾ GIỚI 2)
# ==============================================================================
nodes.append(create_lesson(
    "G7-SHEET-01", "w2", 7, "Bảng tính Điện tử & Các Hàm Cơ bản", "Chủ đề E: Ứng dụng tin học",
    "Bài 6, 7: Làm quen bảng tính, các hàm tính toán", "Bài 5, 6: Địa chỉ ô và hàm SUM, AVERAGE", "Bài 5, 6: Phần mềm bảng tính điện tử",
    "match-memory", [], 7,
    ["Nhận biết cấu trúc bảng tính: Hàng, Cột, Ô và Địa chỉ ô (ví dụ: B3).", "Sử dụng thành thạo các hàm toán học: SUM, AVERAGE, COUNT, MIN, MAX."],
    "Làm sao thủ quỹ trường có thể tính tổng điểm và điểm trung bình cho 1000 học sinh chỉ trong 1 giây? Hãy khám phá sức mạnh của bảng tính điện tử!",
    "Bảng tính tự động tính toán lại kết quả khi dữ liệu đầu vào thay đổi:",
    ["Hàm =SUM(A1:A5): Tính tổng các số từ ô A1 đến A5.", "Hàm =AVERAGE(B1:B10): Tính giá trị trung bình cộng.", "Hàm =MAX và =MIN: Tìm số lớn nhất và số nhỏ nhất trong vùng dữ liệu."],
    {},
    [
        {"question": "Công thức nào sau đây dùng để tính trung bình cộng của 3 ô A1, A2, A3?", "options": ["=SUM(A1:A3)", "=AVERAGE(A1:A3)", "=COUNT(A1:A3)", "=MIN(A1:A3)"], "answer": 1, "explanation": "=AVERAGE là hàm tính trung bình cộng trong bảng tính."}
    ],
    "Em đã trở thành bậc thầy quản lý và phân tích số liệu trên bảng tính!"
))

nodes.append(create_lesson(
    "G7-SORT-01", "w2", 7, "Thuật toán Sắp xếp Nổi bọt (Bubble Sort)", "Chủ đề F: Giải quyết vấn đề với máy tính",
    "Bài 11: Thuật toán sắp xếp nổi bọt", "Bài 11: Sắp xếp nổi bọt", "Bài 11: Thuật toán sắp xếp",
    "bug-hunt", [], 8,
    ["Mô tả được ý tưởng thuật toán sắp xếp nổi bọt so sánh từng cặp phần tử liền kề.", "Thực hiện từng bước đổi chỗ để đưa số lớn nhất về cuối dãy."],
    "Giống như các bọt khí nhẹ hơn nổi dần lên mặt nước, thuật toán Bubble Sort so sánh và đẩy dần các số lớn về đúng vị trí!",
    "Nguyên lý hoạt động của Bubble Sort:",
    ["Duyệt từ đầu đến cuối dãy, so sánh cặp 2 số cạnh nhau.", "Nếu số trước lớn hơn số sau, ta đổi chỗ (hoán đổi) chúng.", "Lặp lại quy trình cho đến khi không còn cặp số nào bị ngược thứ tự."],
    {},
    [
        {"question": "Trong thuật toán sắp xếp nổi bọt tăng dần, nếu số đứng trước lớn hơn số đứng sau, ta làm gì?", "options": ["Xóa số đứng trước", "Đổi chỗ hai số đó cho nhau", "Bỏ qua không làm gì", "Dừng thuật toán"], "answer": 1, "explanation": "Ta hoán đổi vị trí của hai số để đưa số lớn hơn về phía sau."}
    ],
    "Tư duy thuật toán sắp xếp của em đã lên một tầm cao mới!"
))

# ==============================================================================
# LỚP 8 (THCS - THẾ GIỚI 2)
# ==============================================================================
nodes.append(create_lesson(
    "G8-BUG-01", "w2", 8, "Thợ săn Lỗi Thuật toán", "Chủ đề F: Giải quyết vấn đề với máy tính",
    "Bài 14: Gỡ lỗi chương trình", "Bài 13: Phát hiện và sửa lỗi", "Bài 13: Thử nghiệm và gỡ lỗi",
    "bug-hunt", ["G7-SORT-01"], 8,
    ["Phân biệt được lỗi cú pháp (Syntax error) và lỗi logic (Semantic error).", "Thực hành gỡ lỗi (Debugging) để chương trình chạy đúng kết quả mong muốn."],
    "Một kỹ sư giỏi không phải là người không bao giờ gặp lỗi, mà là người truy vết và sửa lỗi nhanh nhất! Hãy tìm dòng code gây lỗi trong bài toán!",
    "Lỗi chương trình (Bug) gồm hai loại cơ bản:",
    ["Lỗi cú pháp: Viết sai từ khóa, thiếu dấu ngoặc - máy tính báo lỗi ngay.", "Lỗi ngữ nghĩa (logic): Chương trình chạy được nhưng kết quả sai do phép tính nhầm."],
    {},
    [
        {"question": "Khi em viết vòng lặp tính tổng các số từ 1 đến 5 nhưng dùng phép trừ thay vì phép cộng, đó là loại lỗi gì?", "options": ["Lỗi phần cứng", "Lỗi cú pháp", "Lỗi logic (ngữ nghĩa)", "Lỗi mạng"], "answer": 2, "explanation": "Chương trình vẫn chạy nhưng tính ra kết quả sai logic bài toán."}
    ],
    "Kỹ năng thợ săn lỗi tinh tường của em đã giúp mã nguồn chạy mượt mà!"
))

# ==============================================================================
# LỚP 9 (THCS - THẾ GIỚI 2)
# ==============================================================================
nodes.append(create_lesson(
    "G9-CYBER-01", "w2", 9, "Tường lửa & Phòng vệ An ninh Mạng", "Chủ đề D: Đạo đức, pháp luật môi trường số",
    "Bài 2, 3: Mã độc và an toàn trên mạng", "Bài 2, 3: Phòng chống nguy cơ mạng", "Bài 2, 3: Tác động của tin học và an toàn số",
    "branch-story", [], 7,
    ["Nhận diện các loại mã độc: Vi-rút, Sâu máy tính (Worm), Trojan.", "Biết cách phòng tránh lừa đảo mạo danh (Phishing) và bảo vệ danh tính số."],
    "Không gian mạng là chiến trường vô hình nơi tin tặc rình rập đánh cắp mật khẩu ngân hàng và thông tin cá nhân. Hãy kích hoạt lá chắn bảo vệ!",
    "Quy tắc phòng thủ an ninh mạng hiện đại:",
    ["Không mở tệp đính kèm trong email gửi từ người lạ không rõ nguồn gốc.", "Xác thực hai yếu tố (2FA): Bảo vệ tài khoản ngay cả khi lộ mật khẩu.", "Luôn kiểm tra địa chỉ trang web có giao thức bảo mật HTTPS an toàn."],
    {
        "scenarios": [
            {
                "id": "s1",
                "prompt": "Em nhận được tin nhắn từ số lạ tự xưng là 'Ban Giám Hiệu' yêu cầu cung cấp mã OTP ngân hàng của bố mẹ.",
                "choices": [
                    {"text": "Báo ngay cho bố mẹ và chặn số điện thoại lừa đảo.", "is_correct": True, "feedback": "Rất chuẩn xác! Không có cơ quan nào yêu cầu cung cấp mã OTP cá nhân."},
                    {"text": "Gửi ngay mã OTP vì sợ bị kỷ luật ở trường.", "is_correct": False, "feedback": "Cực kỳ nguy hiểm! Kẻ gian mạo danh để rút trộm tiền trong tài khoản."}
                ]
            }
        ]
    },
    [
        {"question": "Mã OTP (One Time Password) có bao giờ được phép chia sẻ cho người khác không?", "options": ["Có, chia sẻ cho bạn thân", "Tuyệt đối không chia sẻ cho bất kỳ ai", "Chia sẻ cho người lạ khi được nhờ", "Đăng lên Facebook"], "answer": 1, "explanation": "Mã OTP là lớp bảo mật cuối cùng, chia sẻ sẽ dẫn đến mất tài khoản hoặc tiền bạc."}
    ],
    "Lá chắn tường lửa của em đã bảo vệ an toàn cho cả gia đình và lớp học!"
))

# ==============================================================================
# LỚP 10 (THPT - THẾ GIỚI 3: THÀNH PHỐ THUẬT TOÁN)
# ==============================================================================
nodes.append(create_lesson(
    "G10-GATE-01", "w3", 10, "Cổng Logic & Mạch Điện tử Số", "Chủ đề A: Máy tính và xã hội tri thức (CS)",
    "Bài 4: Mạch logic và cổng logic", "Bài 4: Bảng chân trị và cổng logic", "Bài 4: Cổng logic cơ bản",
    "logic-puzzle", ["G6-BIN-01"], 9,
    ["Hiểu bảng chân trị của các cổng logic cơ bản: AND, OR, NOT, XOR.", "Thiết kế mạch logic kích hoạt tín hiệu điều khiển."],
    "Bên trong vi xử lý chứa hàng tỷ cổng logic liên kết với nhau để thực hiện mọi phép toán đại số Boole. Hãy thông mạch tín hiệu cổng logic!",
    "Đặc tính hoạt động của các cổng logic:",
    ["Cổng AND: Đầu ra bằng 1 khi và chỉ khi TẤT CẢ đầu vào bằng 1.", "Cổng OR: Đầu ra bằng 1 khi CÓ ÍT NHẤT một đầu vào bằng 1.", "Cổng NOT: Đảo ngược tín hiệu đầu vào (0 thành 1, 1 thành 0)."],
    {
        "puzzle_type": "gate_circuit",
        "gates": ["AND", "OR", "NOT"],
        "scenarios": [
            {"inputs": [1, 0], "gate": "AND", "expected": 0},
            {"inputs": [1, 0], "gate": "OR", "expected": 1},
            {"inputs": [0], "gate": "NOT", "expected": 1}
        ]
    },
    [
        {"question": "Cho hai đầu vào A = 1 và B = 1 đi qua cổng AND, đầu ra nhận được là gì?", "options": ["0", "1", "Không xác định", "-1"], "answer": 1, "explanation": "Cổng AND có cả hai đầu vào bằng 1 nên đầu ra đạt mức logic 1."}
    ],
    "Chúc mừng kỹ sư phần cứng tương lai! Em đã làm chủ các cổng logic nền tảng CPU!"
))

nodes.append(create_lesson(
    "G10-PY-01", "w3", 10, "Lập trình Python: Cú pháp & Cấu trúc rẽ nhánh", "Chủ đề F: Giải quyết vấn đề với máy tính",
    "Bài 16, 18: Làm quen Python, rẽ nhánh if", "Bài 14, 16: Cú pháp Python và rẽ nhánh", "Bài 14, 16: Biến và câu lệnh if trong Python",
    "bug-hunt", ["G8-BUG-01"], 10,
    ["Nắm vững quy tắc thụt lề (Indentation) bắt buộc trong ngôn ngữ Python.", "Sử dụng thành thạo câu lệnh rẽ nhánh if - elif - else."],
    "Python là ngôn ngữ lập trình phổ biến số 1 thế giới trong lĩnh vực Trí tuệ Nhân tạo và Khoa học Dữ liệu. Hãy cùng viết những dòng mã đầu tiên!",
    "Đặc trưng nổi bật của Python:",
    ["Không dùng dấu ngoặc nhọn {}, Python dùng thụt đầu dòng (thường 4 dấu cách) để phân khối lệnh.", "Các kiểu dữ liệu cơ bản: int (số nguyên), float (số thực), str (chuỗi), bool (True/False).", "Rẽ nhánh: if điều_kiện: khối_lệnh else: khối_lệnh_khác."],
    {},
    [
        {"question": "Trong Python, điều gì được dùng để xác định một khối lệnh?", "options": ["Dấu ngoặc nhọn { }", "Thụt lề các dòng lệnh (Indentation)", "Dấu chấm phẩy ;", "Dấu ngoặc vuông [ ]"], "answer": 1, "explanation": "Python bắt buộc dùng thụt lề thống nhất để gom các lệnh cùng cấp."}
    ],
    "Mã nguồn Python của em đã chạy mượt mà và chuẩn mực công nghiệp!"
))

# ==============================================================================
# LỚP 11 (THPT - THẾ GIỚI 3)
# ==============================================================================
nodes.append(create_lesson(
    "G11-DB-01", "w3", 11, "Cơ sở Dữ liệu Quan hệ & Truy vấn SQL", "Chủ đề CS: Khoa học máy tính",
    "Bài CS-1, CS-3: CSDL quan hệ và SQL", "Bài CS-1, CS-3: Hệ CSDL và ngôn ngữ SQL", "Bài CS-1, CS-3: CSDL và bảng quan hệ",
    "match-memory", [], 10,
    ["Hiểu mô hình CSDL quan hệ: Bảng (Table), Bản ghi (Row/Record), Trường (Field/Column).", "Hiểu vai trò của Khóa chính (Primary Key) xác định duy nhất từng bản ghi."],
    "Làm sao mạng xã hội Facebook hay ngân hàng có thể lưu trữ và tìm kiếm hàng tỷ thông tin tài khoản mà không bị trùng lặp? Câu trả lời nằm ở Hệ cơ sở dữ liệu quan hệ!",
    "Nguyên lý cơ sở dữ liệu quan hệ (RDBMS):",
    ["Khóa chính (Primary Key): Nhãn định danh duy nhất (ví dụ: Số CCCD, Mã học sinh).", "Ngôn ngữ SQL (Structured Query Language): Dùng để truy vấn, lọc và nối bảng.", "Lệnh SELECT cột FROM bảng WHERE điều_kiện."],
    {},
    [
        {"question": "Trong một bảng học sinh, trường thông tin nào thích hợp nhất để làm Khóa chính (Primary Key)?", "options": ["Họ và tên", "Mã số học sinh (duy nhất)", "Năm sinh", "Nơi sinh"], "answer": 1, "explanation": "Mã số học sinh là duy nhất cho mỗi cá nhân, không bị trùng lặp như họ tên hay năm sinh."}
    ],
    "Em đã sẵn sàng trở thành chuyên gia thiết kế và quản trị cơ sở dữ liệu lớn!"
))

# ==============================================================================
# LỚP 12 (THPT - THẾ GIỚI 3: ĐẠI CHIẾN BOSS)
# ==============================================================================
nodes.append(create_lesson(
    "G12-BOSS-01", "w3", 12, "Đại Chiến Boss Trí tuệ Nhân tạo & Mạng Toàn cầu", "Tổng hợp toàn diện GDPT 2018",
    "Chuyên đề Tổng kết 12", "Chuyên đề Tổng kết 12", "Chuyên đề Tổng kết 12",
    "boss-quiz", ["G10-GATE-01", "G11-DB-01"], 12,
    ["Tổng hợp năng lực Tin học 10 năm học từ Lớp 3 đến Lớp 12.", "Sẵn sàng cho kỳ thi tốt nghiệp và định hướng nghề nghiệp thời đại số."],
    "Trùm cuối Virus 'Glitch Byte' đang tấn công xóa sổ kho dữ liệu số hóa của nhân loại! Hãy dùng vũ khí tri thức tin học của em để bảo vệ nền văn minh số!",
    "Đấu trường đỉnh cao thử thách phản xạ và trí tuệ:",
    ["Giao thức mạng TCP/IP và mã hóa dữ liệu HTTPS an toàn.", "Thuật toán tìm kiếm nhị phân tối ưu O(log N).", "Trí tuệ nhân tạo (AI), dữ liệu huấn luyện (Training Data) và Luật An ninh mạng."],
    {
        "boss_name": "Glitch Byte the Destroyer",
        "boss_max_hp": 100,
        "player_max_hp": 100,
        "damage_per_hit": 25,
        "questions_pool": 6
    },
    [
        {"question": "Giao thức nào chịu trách nhiệm truyền tải siêu văn bản an toàn có mã hóa?", "options": ["HTTP", "HTTPS", "FTP", "SMTP"], "answer": 1, "explanation": "HTTPS sử dụng SSL/TLS để mã hóa dữ liệu an toàn."},
        {"question": "Thuật toán tìm kiếm nhị phân (Binary Search) đạt độ phức tạp thời gian nào trên mảng đã sắp xếp?", "options": ["O(N)", "O(log N)", "O(N^2)", "O(1)"], "answer": 1, "explanation": "Binary search chia đôi không gian tìm kiếm sau mỗi bước nên đạt O(log N)."},
        {"question": "Tập dữ liệu dùng để thuật toán học các đặc trưng trong Machine Learning gọi là gì?", "options": ["Training data", "Test data", "Hidden data", "Random data"], "answer": 0, "explanation": "Training data (Dữ liệu huấn luyện) là mẫu để mô hình AI học tập."},
        {"question": "Hành vi nào bị nghiêm cấm theo Luật An ninh mạng Việt Nam?", "options": ["Học lập trình máy tính", "Phát tán thông tin sai sự thật, xúc phạm uy tín người khác", "Mua phần mềm có bản quyền", "Cài đặt phần mềm diệt vi-rút"], "answer": 1, "explanation": "Phát tán tin giả, bôi nhọ người khác bị nghiêm cấm theo Điều 8 Luật An ninh mạng."}
    ],
    "CHIẾN THẮNG HUY HOÀNG! Em đã hoàn thành xuất sắc chặng đường Tin học phổ thông GDPT 2018 với danh hiệu Bậc Thầy Công Nghệ EasyTin!"
))

full_curriculum = {
    "version": "2.0.0",
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

print(f"Generated {len(nodes)} comprehensive curriculum nodes successfully into {curriculum_path}!")
