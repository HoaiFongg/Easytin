# -*- coding: utf-8 -*-
"""
Dữ liệu chương trình học EasyTin: Khối THCS (Lớp 6, 7, 8, 9)
Phủ 100% tất cả các bài học và YCCĐ của cả 3 bộ sách: KNTT, Cánh Diều, CTST.
"""

def get_middle_school_nodes():
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
    # LỚP 6 (12 NÚT)
    # =========================================================================
    nodes.append(make_lesson(
        "G6-01", "w2", 6, "Thông tin, Vật mang tin & Chu trình Xử lý", "Chủ đề 1: Máy tính và cộng đồng",
        "Bài 1, 2: Thông tin & Thu nhận, xử lý", "Bài 1, 2, 3: Thông tin & Hoạt động thông tin", "Bài 1: Thông tin và xử lý thông tin",
        "branch-story", [], 7,
        ["Phân biệt dữ liệu, thông tin và vật mang tin.", "Mô tả 4 bước trong mô hình xử lý thông tin: Nhập -> Xử lý -> Xuất -> Lưu trữ."],
        "Tại sao tiếng còi xe cấp cứu inh ỏi trên đường lại khiến mọi phương tiện lập tức dẹp sang hai bên nhường đường?",
        "Thông tin là những hiểu biết của con người về thế giới xung quanh. Vật mang tin là vật thể chứa đựng hoặc truyền tải thông tin (cuốn sách, USB, sóng phát thanh). Máy tính tiếp nhận dữ liệu đầu vào qua thiết bị vào, xử lý qua CPU, xuất ra màn hình và lưu vào bộ nhớ.",
        ["Dữ liệu là dạng thể hiện của thông tin (chữ viết, con số, hình ảnh thô).", "Thông tin có ý nghĩa giúp con người nhận thức và hành động."],
        {"scenarios": [{"id": "s1", "prompt": "Em nhận được một tờ rơi quảng cáo khóa học tiếng Anh có in mã QR Code và địa chỉ trường học.", "choices": [{"text": "Tờ giấy rơi là vật mang tin; chữ viết và hình ảnh in trên đó là dữ liệu mang lại thông tin.", "is_correct": True, "feedback": "Rất chuẩn xác! Tờ giấy là vật mang tin vật lý chứa đựng dữ liệu."}, {"text": "Tờ giấy chính là thông tin trừu tượng.", "is_correct": False, "feedback": "Sai rồi! Giấy là vật mang tin hữu hình, không phải thông tin trừu tượng."}]}]},
        [{"question": "Trong các đối tượng sau, vật nào là 'vật mang tin'?", "options": ["Chiếc thẻ nhớ USB chứa bài giảng", "Sự hiểu biết về định lý toán học", "Cảm giác vui sướng khi đạt điểm 10"], "answer": 0, "explanation": "Thẻ nhớ USB là vật thể vật lý dùng để chứa đựng dữ liệu."}],
        "Em đã phân biệt hoàn hảo giữa thông tin, dữ liệu và vật mang tin!"
    ))

    nodes.append(make_lesson(
        "G6-02", "w2", 6, "Số hóa Dữ liệu Nhị phân & Đơn vị Đo Dung lượng", "Chủ đề 1: Máy tính và cộng đồng",
        "Bài 3: Thông tin trong máy tính", "Bài 4, 5: Biểu diễn & Dữ liệu trong máy tính", "Bài 2: Biểu diễn dữ liệu số",
        "logic-puzzle", ["G6-01"], 8,
        ["Hiểu dữ liệu trong máy tính được biểu diễn bằng dãy bit (0 và 1).", "Thành thạo các đơn vị đo dung lượng: Bit, Byte, KB, MB, GB, TB."],
        "Bên trong máy vi tính không có chữ cái hay màu sắc, chỉ có hàng tỷ bóng bán dẫn siêu nhỏ bật và tắt dòng điện!",
        "Mỗi bit là một chữ số nhị phân nhận giá trị 0 (tắt) hoặc 1 (bật). 1 Byte = 8 bits. Bảng quy đổi tiền tố: 1 KB = 1024 Bytes, 1 MB = 1024 KB, 1 GB = 1024 MB, 1 TB = 1024 GB. Tất cả văn bản, bài hát, hình ảnh đều được mã hóa thành các dãy bit nhị phân.",
        ["Bit là đơn vị nhỏ nhất đo lượng thông tin trong máy tính.", "1 Byte tương đương với dung lượng lưu trữ 1 ký tự chữ cái tiếng Anh cơ bản."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [5, 10, 13]},
        [{"question": "Một gigabyte (1 GB) xấp xỉ bằng bao nhiêu megabyte (MB)?", "options": ["1024 MB", "100 MB", "10000 MB"], "answer": 0, "explanation": "Theo hệ số nhị phân 2^10, 1 GB = 1024 MB."}],
        "Em đã giải mã thành công bí mật hệ nhị phân của thế giới máy tính!"
    ))

    nodes.append(make_lesson(
        "G6-03", "w2", 6, "Mạng Máy tính & Phương thức Kết nối", "Chủ đề 1: Máy tính và cộng đồng",
        "Bài 4, 5: Mạng máy tính & Internet", "Bài 6, 7: Mạng máy tính & Kết nối Internet", "Bài 3, 4: Khái niệm mạng & Dịch vụ WWW",
        "sort-drag", ["G6-01"], 7,
        ["Hiểu mạng máy tính là hệ thống kết nối các máy tính để chia sẻ tài nguyên.", "Phân biệt mạng có dây (dây cáp xoắn, cáp quang) và mạng không dây (Wi-Fi, Bluetooth)."],
        "Điều gì cho phép em ngồi ở Việt Nam mà vẫn gửi được tài liệu cho bạn bè ở tận châu Mỹ chỉ trong tích tắc?",
        "Mạng máy tính gồm 3 thành phần chính: Các thiết bị đầu cuối (máy tính, điện thoại, máy in), Thiết bị kết nối mạng (Switch, Router, Access Point) và Môi trường truyền dẫn (dây cáp mạng, sóng vô tuyến không dây).",
        ["Mạng có dây truyền tín hiệu nhanh, ổn định qua dây cáp.", "Mạng không dây Wi-Fi tiện lợi, linh hoạt cho thiết bị di động."],
        {"groups": [{"id": "g1", "name": "Thiết bị Kết nối Mạng có dây"}, {"id": "g2", "name": "Thiết bị & Công nghệ Không dây"}], "items": [{"id":"1","name":"Dây cáp mạng bấm đầu RJ45","group":"g1","icon":"🔌"},{"id":"2","name":"Bộ chuyển mạch Switch mạng LAN","group":"g1","icon":"🔀"},{"id":"3","name":"Thiết bị phát sóng Wi-Fi (Access Point)","group":"g2","icon":"📶"},{"id":"4","name":"Kết nối tai nghe Bluetooth","group":"g2","icon":"🎧"}]},
        [{"question": "Thành phần nào sau đây là thiết bị kết nối mạng trung gian giúp định tuyến gói tin?", "options": ["Bộ định tuyến Router", "Màn hình máy tính", "Bàn phím cơ"], "answer": 0, "explanation": "Router là thiết bị mạng chuyên dụng định tuyến các gói tin qua Internet."}],
        "Em đã nắm vững cấu trúc và các thành phần cốt lõi của mạng máy tính!"
    ))

    nodes.append(make_lesson(
        "G6-04", "w2", 6, "Dịch vụ World Wide Web & Công cụ Tìm kiếm", "Chủ đề 2: Mạng xã hội",
        "Bài 6, 7: Mạng thông tin toàn cầu & Tìm kiếm", "Bài 8: Trình duyệt web và tìm kiếm", "Bài 4, 5: Dịch vụ WWW & Tìm kiếm khoa học",
        "match-memory", ["G6-03"], 7,
        ["Phân biệt Internet (hạ tầng mạng) và WWW (dịch vụ thông tin web).", "Sử dụng các toán tử tìm kiếm nâng cao (dấu ngoặc kép, dấu trừ)."],
        "World Wide Web như một cuốn bách khoa toàn thư vô tận được kết nối bằng hàng tỷ siêu liên kết!",
        "WWW (World Wide Web) là mạng lưới các trang web liên kết với nhau chạy trên nền tảng Internet. Trình duyệt web (Chrome, Edge, Firefox) gửi yêu cầu và hiển thị trang web. Công cụ tìm kiếm thu thập chỉ mục các trang web để tra cứu theo từ khóa.",
        ["Internet là mạng lưới phần cứng khổng lồ, WWW là dịch vụ phần mềm trên Internet.", "Sử dụng toán tử \"từ khóa\" để tìm chính xác, dấu trừ (-) để loại bỏ kết quả không mong muốn."],
        {"cards": [{"id":"1","name":"Trình duyệt Web","match":"Phần mềm giúp người dùng duyệt và xem các trang web"},{"id":"2","name":"Địa chỉ URL","match":"Đường dẫn định danh duy nhất của một trang web trên Internet"},{"id":"3","name":"Máy chủ Web (Server)","match":"Máy tính chuyên dụng lưu trữ và cung cấp nội dung trang web"},{"id":"4","name":"Siêu văn bản (Hypertext)","match":"Văn bản có chứa liên kết trỏ tới các tài liệu khác"}]},
        [{"question": "Trình duyệt web phổ biến hiện nay là phần mềm nào?", "options": ["Google Chrome", "Microsoft Word", "Photoshop"], "answer": 0, "explanation": "Chrome là trình duyệt web hàng đầu hiện nay."}],
        "Em đã trở thành một chuyên gia khai thác tài nguyên World Wide Web!"
    ))

    nodes.append(make_lesson(
        "G6-05", "w2", 6, "Thư điện tử (Email) & Văn hóa Mạng Xã hội", "Chủ đề 2: Mạng xã hội",
        "Bài 8, 9: Thư điện tử & Mạng xã hội", "Bài 9, 10: Thư điện tử & Mạng xã hội", "Bài 6, 7: Thư điện tử & Ứng xử số",
        "branch-story", ["G6-04"], 7,
        ["Hiểu cấu trúc địa chỉ email: <tên hộp thư>@<tên miền>.", "Quy tắc viết email lịch sự và ứng xử văn minh trên mạng xã hội."],
        "Hòm thư điện tử giúp trao đổi thư từ xuyên đại dương chỉ trong 1 giây, nhưng hãy cẩn thận với thư rác độc hại!",
        "Một địa chỉ email chuẩn gồm 2 phần cách nhau bởi ký tự @ (ví dụ: hoctot@gmail.com). Khi viết thư, luôn ghi tiêu đề rõ ràng, lời chào lịch sự và đính kèm tệp an toàn. Trên mạng xã hội, suy nghĩ kỹ trước khi bình luận, tôn trọng người khác.",
        ["Trường To: người nhận chính; CC: người cùng nhận; BCC: người nhận ẩn danh.", "Không bấm vào liên kết lạ trong email từ người gửi không quen biết."],
        {"scenarios": [{"id": "s1", "prompt": "Em nhận được email từ một địa chỉ lạ xưng là 'Ban Quản trị' yêu cầu gửi lại mật khẩu tài khoản ngay để không bị khóa hộp thư.", "choices": [{"text": "Xóa ngay email và đánh dấu là thư rác lừa đảo (Spam/Phishing).", "is_correct": True, "feedback": "Rất chuẩn! Không một dịch vụ uy tín nào yêu cầu gửi mật khẩu qua email."}, {"text": "Gửi ngay mật khẩu cho họ vì sợ bị khóa tài khoản.", "is_correct": False, "feedback": "Bẫy lừa đảo đấy! Em sẽ bị kẻ xấu chiếm đoạt tài khoản ngay lập tức!"}]}]},
        [{"question": "Trong địa chỉ email 'hocsinh@school.edu.vn', phần nào là tên miền của nhà cung cấp dịch vụ?", "options": ["school.edu.vn", "hocsinh", "Ký hiệu @"], "answer": 0, "explanation": "Phần đứng sau ký hiệu @ là tên miền của tổ chức hoặc nhà cung cấp."}],
        "Em đã nắm vững quy tắc sử dụng email chuẩn mực và an toàn số!"
    ))

    nodes.append(make_lesson(
        "G6-06", "w2", 6, "Bảo vệ Dữ liệu Cá nhân & Sở hữu Trí tuệ", "Chủ đề 3: Đạo đức, pháp luật",
        "Bài 10, 11: Đạo đức pháp luật & Bản quyền", "Bài 11: Bản quyền và đạo đức trên mạng", "Bài 8: Bảo vệ quyền riêng tư & bản quyền",
        "branch-story", ["G6-05"], 7,
        ["Hiểu tầm quan trọng của việc bảo vệ dữ liệu cá nhân trên mạng.", "Tuân thủ quy định trích dẫn bản quyền tác giả trong môi trường số."],
        "Dấu chân kỹ thuật số (Digital Footprint) ghi lại mọi hành động của em trên mạng Internet!",
        "Mỗi lần đăng ảnh, bấm like hay bình luận, em đều để lại dấu chân số. Hãy bảo vệ danh tính cá nhân, không chia sẻ lịch trình riêng tư. Sử dụng tranh ảnh hay tài liệu của người khác bắt buộc phải trích dẫn nguồn tác giả đầy đủ.",
        ["Bảo mật 2 lớp (2FA) giúp tài khoản không bị xâm nhập trái phép.", "Vi phạm bản quyền có thể bị phạt hành chính theo Luật Sở hữu trí tuệ."],
        {"scenarios": [{"id": "s1", "prompt": "Em đang chuẩn bị đi du lịch xa cùng gia đình trong 1 tuần.", "choices": [{"text": "Chờ khi đi du lịch về nhà an toàn rồi mới đăng ảnh kỷ niệm lên mạng xã hội.", "is_correct": True, "feedback": "Rất sáng suốt! Đăng tin nhà vắng người có thể thu hút kẻ trộm đột nhập."}, {"text": "Đăng thông báo lên mạng: Nhà em đi vắng cả tuần không có ai ở nhà đâu nhé!", "is_correct": False, "feedback": "Cực kỳ nguy hiểm! Kẻ xấu có thể lợi dụng sơ hở để trộm cắp tài sản!"}]}]},
        [{"question": "Hành động nào sau đây giúp bảo vệ tài khoản mạng an toàn nhất?", "options": ["Đặt mật khẩu mạnh trên 8 ký tự gồm chữ hoa, số, ký hiệu và bật xác thực 2 bước (2FA)", "Đặt mật khẩu là ngày sinh nhật của mình", "Dùng chung 1 mật khẩu đơn giản cho tất cả các tài khoản"], "answer": 0, "explanation": "Mật khẩu phức tạp kèm xác thực 2 bước mang lại độ an toàn cao nhất."}],
        "Em là một công dân số thông thái, biết tự bảo vệ mình trên không gian mạng!"
    ))

    nodes.append(make_lesson(
        "G6-07", "w2", 6, "Ứng dụng Sơ đồ Tư duy trong Học tập", "Chủ đề 4: Ứng dụng tin học",
        "Bài 10: Sơ đồ tư duy", "Bài 12: Sơ đồ tư duy và công cụ hỗ trợ", "Bài 9: Ứng dụng sơ đồ tư duy",
        "logic-puzzle", ["G6-01"], 8,
        ["Hiểu lợi ích của sơ đồ tư duy (Mindmap) trong việc tóm tắt và ghi nhớ kiến thức.", "Biết tạo sơ đồ tư duy gồm chủ đề trung tâm và các nhánh phụ bằng phần mềm."],
        "Bộ não con người ghi nhớ bằng hình ảnh và màu sắc tốt hơn gấp 10 lần những trang chữ đen trắng!",
        "Sơ đồ tư duy phát triển từ một chủ đề chính ở trung tâm, tỏa ra các nhánh cấp 1, nhánh cấp 2 bằng các từ khóa ngắn gọn, màu sắc và biểu tượng trực quan. Rất hữu ích khi ôn tập thi học kỳ môn Lịch sử, Địa lý, Sinh học.",
        ["Chủ đề trung tâm đặt ở giữa trang.", "Mỗi nhánh sử dụng một màu sắc riêng để kích thích trí nhớ thị giác."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [6, 9, 14]},
        [{"question": "Vị trí chuẩn để đặt chủ đề chính trong một sơ đồ tư duy là ở đâu?", "options": ["Ở chính giữa trung tâm trang giấy", "Ở góc dưới cùng bên trái", "Ở lề trên cùng"], "answer": 0, "explanation": "Chủ đề trung tâm luôn đặt ở giữa để các nhánh tỏa đều ra xung quanh."}],
        "Sơ đồ tư duy của em đã trực quan hóa kiến thức cực kỳ khoa học!"
    ))

    nodes.append(make_lesson(
        "G6-08", "w2", 6, "Soạn thảo Nâng cao & Trình bày Bảng biểu", "Chủ đề 4: Ứng dụng tin học",
        "Bài 11, 12, 13, 14: Định dạng văn bản & Bảng biểu", "Bài 13, 14: Soạn thảo nâng cao & Tạo bảng", "Bài 10, 11, 12: Soạn thảo văn bản & Báo cáo",
        "sort-drag", ["G6-07"], 7,
        ["Thiết lập lề trang giấy (Margins), hướng giấy in (Orientation).", "Định dạng bảng biểu số liệu khoa học và chèn ngắt trang tự động."],
        "Tạo ra một bản báo cáo nghiên cứu khoa học học đường đẹp như sách in chuyên nghiệp!",
        "Vào thẻ Layout để căn lề trang: Lề trên/dưới 2cm, Lề trái 3cm (để đóng gáy sách), Lề phải 2cm. Chèn Header (tiêu đề đầu trang) và Footer (đánh số trang tự động). Bảng số liệu được căn chỉnh số thẳng hàng phải, chữ thẳng hàng trái.",
        ["Phím tắt Ctrl + Enter để ngắt sang trang mới ngay lập tức.", "Đánh số trang tự động giúp người đọc dễ theo dõi mục lục."],
        {"groups": [{"id": "g1", "name": "Thiết lập Trang in (Page Setup)"}, {"id": "g2", "name": "Trình bày Dữ liệu Bảng (Table Format)"}], "items": [{"id":"1","name":"Căn lề trang in Margin (Trái 3cm, Phải 2cm)","group":"g1","icon":"📄"},{"id":"2","name":"Chọn hướng giấy in Dọc (Portrait) / Ngang (Landscape)","group":"g1","icon":"🔄"},{"id":"3","name":"Gộp các ô tiêu đề cột (Merge Cells)","group":"g2","icon":"🔲"},{"id":"4","name":"Tô màu nền xen kẽ cho các dòng bảng dữ liệu","group":"g2","icon":"🎨"}]},
        [{"question": "Để ngắt sang một trang mới mà không cần nhấn phím Enter liên tục, ta dùng tổ hợp phím nào?", "options": ["Ctrl + Enter", "Alt + Enter", "Shift + Enter"], "answer": 0, "explanation": "Ctrl + Enter là lệnh chèn dấu ngắt trang chuẩn (Page Break)."}],
        "Văn bản báo cáo của em đạt tiêu chuẩn trình bày chuẩn mực quốc gia!"
    ))

    nodes.append(make_lesson(
        "G6-09", "w2", 6, "Khái niệm Thuật toán & Ba Cấu trúc Điều khiển", "Chủ đề 5: Giải quyết vấn đề",
        "Bài 15, 16: Thuật toán & Cấu trúc điều khiển", "Bài 15, 16, 17: Thuật toán & Sơ đồ khối", "Bài 13, 14, 15: Tư duy thuật toán & Cấu trúc",
        "block-maze", ["G6-01"], 8,
        ["Hiểu 3 đặc trưng của thuật toán: Tính xác định, Tính dừng, Tính đúng đắn.", "Nhận biết 3 cấu trúc điều khiển cơ bản: Tuần tự, Rẽ nhánh, Lặp."],
        "Mọi phần mềm khổng lồ như Google hay Facebook đều được xây dựng từ 3 cấu trúc điều khiển cơ bản!",
        "Thuật toán là dãy hữu hạn các thao tác được sắp xếp theo trình tự xác định sao cho sau khi thực hiện sẽ cho ra kết quả mong muốn từ dữ liệu đầu vào. Ba cấu trúc nền tảng gồm: Cấu trúc tuần tự (lệnh 1 -> lệnh 2), Cấu trúc rẽ nhánh (Nếu... thì...), Cấu trúc lặp (Lặp lại khi điều kiện còn thỏa mãn).",
        ["Tính dừng: thuật toán bắt buộc phải kết thúc sau một số bước hữu hạn.", "Mọi bài toán phức tạp đều có thể giải quyết bằng sự kết hợp của 3 cấu trúc này."],
        {"grid_size": 4, "start": {"x": 0, "y": 0, "dir": "E"}, "target": {"x": 3, "y": 2}, "walls": [{"x": 1, "y": 1}, {"x": 2, "y": 0}], "allowed_blocks": ["forward", "turn_right", "turn_left"], "max_blocks": 8},
        [{"question": "Đặc trưng nào bắt buộc thuật toán không được phép chạy vô tận mà phải kết thúc sau hữu hạn bước?", "options": ["Tính dừng", "Tính xác định", "Tính đại chúng"], "answer": 0, "explanation": "Tính dừng đảm bảo thuật toán luôn đưa ra kết quả và kết thúc."}],
        "Em đã nắm vững linh hồn của khoa học máy tính: Tư duy thuật toán!"
    ))

    nodes.append(make_lesson(
        "G6-10", "w2", 6, "Mô tả Thuật toán bằng Sơ đồ khối Chuẩn", "Chủ đề 5: Giải quyết vấn đề",
        "Bài 16: Sơ đồ khối thuật toán", "Bài 16, 17: Sơ đồ khối & Cấu trúc", "Bài 14, 15: Biểu diễn sơ đồ khối",
        "logic-puzzle", ["G6-09"], 8,
        ["Sử dụng thành thạo các hình khối quy ước quốc tế ISO.", "Vẽ sơ đồ khối thuật toán tìm số lớn nhất (Max) trong hai số."],
        "Vẽ sơ đồ mạch tư duy giúp các kỹ sư phần mềm thống nhất ý tưởng trước khi lập trình!",
        "Quy chuẩn sơ đồ khối: Hình Oval (Bắt đầu/Kết thúc), Hình bình hành (Nhập dữ liệu vào / Xuất kết quả ra), Hình chữ nhật (Tính toán xử lý), Hình thoi (Kiểm tra điều kiện logic với hai nhánh Đúng/Sai).",
        ["Mỗi khối chỉ có một mũi tên đi vào và một mũi tên đi ra (riêng hình thoi có 2 mũi tên đi ra).", "Luồng đi của mũi tên luôn rõ ràng từ trên xuống dưới hoặc từ trái qua phải."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [7, 11, 15]},
        [{"question": "Trong sơ đồ khối, hình nào dùng để biểu diễn thao tác 'Nhập hai số A và B từ bàn phím'?", "options": ["Hình bình hành", "Hình chữ nhật", "Hình thoi"], "answer": 0, "explanation": "Hình bình hành dùng riêng cho các thao tác Nhập (Input) và Xuất (Output)."}],
        "Sơ đồ khối thuật toán của em rất chuẩn xác và rõ ràng!"
    ))

    nodes.append(make_lesson(
        "G6-11", "w2", 6, "Phát hiện Lỗi & Kiểm thử Thuật toán", "Chủ đề 5: Giải quyết vấn đề",
        "Bài 16: Kiểm thử thuật toán", "Bài 17: Cấu trúc rẽ nhánh & Lặp", "Bài 16: Phát hiện và gỡ lỗi thuật toán",
        "bug-hunt", ["G6-10"], 8,
        ["Kỹ năng chạy bàn (Trace table) kiểm tra từng bước giá trị của biến.", "Tìm ra trường hợp ngoại lệ (Edge cases) khiến thuật toán bị sai kết quả."],
        "Kiểm thử thuật toán bằng tay trên giấy trước khi cho chạy máy tính!",
        "Chạy bàn (Bảng theo dõi biến) là phương pháp liệt kê các cột biến số, điền giá trị của từng biến qua từng bước thực thi của thuật toán. Nhờ đó, ta dễ dàng phát hiện bước nào tính sai hoặc điều kiện nào bị lặp vô tận.",
        ["Luôn kiểm thử với dữ liệu số âm, số 0 và số dương.", "Kiểm tra kỹ điều kiện biên tại các điểm giao cắt của vòng lặp."],
        {},
        [{"question": "Phương pháp lập bảng ghi lại sự thay đổi giá trị của các biến qua từng bước của thuật toán gọi là gì?", "options": ["Chạy bàn (Trace table)", "In ảnh chụp màn hình", "Cài lại hệ điều hành"], "answer": 0, "explanation": "Chạy bàn (Trace table) là kỹ thuật kinh điển giúp kiểm tra tính đúng đắn của thuật toán."}],
        "Kỹ năng kiểm thử gỡ lỗi thuật toán của em đạt đẳng cấp rất cao!"
    ))

    nodes.append(make_lesson(
        "G6-12", "w2", 6, "Đấu trường Trùm Lớp 6: Hiệp sĩ An ninh Mạng", "Tổng kết GDPT 2018 Lớp 6",
        "Bài 17: Dự án: An toàn môi trường số", "Bài 18: Dự án: Phòng chống bạo lực mạng", "Bài 17: Dự án tuyên truyền an toàn số",
        "boss-quiz", ["G6-02", "G6-03", "G6-06", "G6-09", "G6-10"], 12,
        ["Tổng kết toàn diện chuẩn năng lực Tin học Lớp 6 của cả 3 bộ sách.", "Sẵn sàng nhận huy hiệu Hiệp Sĩ An Ninh Mạng EasyTin."],
        "Quái vật Mã Độc 'Crypto-Worm' đang lây lan trên hệ thống mạng trường học! Hãy hợp nhất tri thức Lớp 6 để tiêu diệt nó!",
        "Đấu trường tổng hợp: Hệ nhị phân 0-1, Dung lượng lưu trữ, Thiết bị mạng, Văn hóa số và Sơ đồ khối thuật toán.",
        ["Bit, Byte, KB, MB, GB, TB.", "Mạng máy tính, Router, Switch, Sơ đồ khối và An toàn dữ liệu."],
        {"boss_name": "Crypto-Worm Mã Độc", "boss_max_hp": 100, "player_max_hp": 100, "damage_per_hit": 25, "questions_pool": 4},
        [
            {"question": "Một byte (1 Byte) tương đương với bao nhiêu bit?", "options": ["8 bits", "4 bits", "16 bits", "1024 bits"], "answer": 0, "explanation": "1 Byte = 8 bits."},
            {"question": "Trong sơ đồ khối thuật toán, hình thoi dùng để thể hiện điều gì?", "options": ["Kiểm tra điều kiện rẽ nhánh", "Bắt đầu chương trình", "Thao tác tính toán cộng trừ", "Xuất dữ liệu ra màn hình"], "answer": 0, "explanation": "Hình thoi là khối kiểm tra điều kiện logic."},
            {"question": "Thiết bị nào có chức năng chuyển đổi giữa tín hiệu số của máy tính và sóng Wi-Fi không dây?", "options": ["Bộ phát Access Point / Router Wi-Fi", "Ổ đĩa cứng HDD", "Chuột quang", "Dây nguồn máy tính"], "answer": 0, "explanation": "Access Point / Router Wi-Fi phát sóng mạng không dây."},
            {"question": "Địa chỉ email nào sau đây có cú pháp ĐÚNG quy định?", "options": ["nguyenvanan@gmail.com", "nguyenvanan.gmail.com", "nguyenvanan@gmail@com", "nguyen van an@gmail.com"], "answer": 0, "explanation": "Địa chỉ email chuẩn có tên hộp thư, dấu @ và tên miền, không dấu cách."}
        ],
        "CHIẾN CÔNG HIỂN HÁCH! Em đã tiêu diệt Crypto-Worm và hoàn thành toàn bộ chương trình Tin học Lớp 6 của cả 3 bộ sách KNTT, Cánh Diều, CTST!"
    ))

    # =========================================================================
    # LỚP 7 (14 NÚT)
    # =========================================================================
    nodes.append(make_lesson(
        "G7-01", "w2", 7, "Thiết bị Vào - Ra & Cổng Giao tiếp", "Chủ đề 1: Máy tính và cộng đồng",
        "Bài 1: Thiết bị vào - ra", "Bài 1: Thiết bị vào và thiết bị ra", "Bài 1: Thiết bị vào - ra & Kết nối",
        "sort-drag", ["G6-01"], 7,
        ["Phân loại chính xác các thiết bị vào (Input) và thiết bị ra (Output).", "Nhận biết các cổng kết nối chuẩn: USB Type-A, USB Type-C, HDMI, DisplayPort."],
        "Một dàn máy tính hiện đại cần những giác quan và giọng nói nào để tương tác với thế giới con người?",
        "Thiết bị vào (Input Devices): tiếp nhận dữ liệu từ thế giới bên ngoài vào máy tính (bàn phím, chuột, máy quét, micro, webcam). Thiết bị ra (Output Devices): đưa thông tin từ máy tính ra cho con người hiểu (màn hình, máy in, loa, máy chiếu). Màn hình cảm ứng là thiết bị đa năng vừa vào vừa ra.",
        ["Cổng HDMI và DisplayPort truyền tải đồng thời cả hình ảnh độ nét cao và âm thanh số.", "Cổng USB Type-C tốc độ cao và cắm được cả 2 chiều thuận tiện."],
        {"groups": [{"id": "g1", "name": "Thiết bị Nhập dữ liệu (Input)"}, {"id": "g2", "name": "Thiết bị Xuất kết quả (Output)"}], "items": [{"id":"1","name":"Máy quét tài liệu Scanner","group":"g1","icon":"📠"},{"id":"2","name":"Micro thu âm giọng nói","group":"g1","icon":"🎙️"},{"id":"3","name":"Máy in laser màu khổ A4","group":"g2","icon":"🖨️"},{"id":"4","name":"Hệ thống Loa vòm 5.1","group":"g2","icon":"🔊"}]},
        [{"question": "Thiết bị nào sau đây vừa đóng vai trò thiết bị vào, vừa đóng vai trò thiết bị ra?", "options": ["Màn hình cảm ứng (Touchscreen)", "Bàn phím cơ", "Máy in"], "answer": 0, "explanation": "Màn hình cảm ứng vừa hiển thị (ra) vừa nhận thao tác chạm tay (vào)."}],
        "Em đã phân loại rất chuẩn xác các thiết bị phần cứng vào - ra của máy tính!"
    ))

    nodes.append(make_lesson(
        "G7-02", "w2", 7, "Hệ điều hành & Phần mềm Ứng dụng", "Chủ đề 1: Máy tính và cộng đồng",
        "Bài 2: Phần mềm ứng dụng", "Bài 2: Hệ điều hành và phần mềm", "Bài 2: Hệ điều hành & Tiện ích",
        "sort-drag", ["G7-01"], 7,
        ["Hiểu vai trò của Hệ điều hành (OS) là nhạc trưởng quản lý toàn bộ máy tính.", "Phân biệt Hệ điều hành (Windows, Linux, macOS, Android, iOS) và phần mềm ứng dụng."],
        "Nếu máy tính là một dàn nhạc giao hưởng, thì Hệ điều hành chính là vị Nhạc trưởng tài ba điều khiển mọi nhạc công!",
        "Hệ điều hành quản lý tài nguyên phần cứng (CPU, bộ nhớ, ổ đĩa), quản lý tệp và tạo giao diện để người dùng chạy các phần mềm ứng dụng. Nếu không có hệ điều hành, máy tính chỉ là một khối sắt vô tri vô giác.",
        ["Hệ điều hành máy tính: Windows 11, macOS, Ubuntu Linux.", "Hệ điều hành di động: Android, iOS."],
        {"groups": [{"id": "g1", "name": "Hệ điều hành (Operating System)"}, {"id": "g2", "name": "Phần mềm Ứng dụng (Application)"}], "items": [{"id":"1","name":"Hệ điều hành Microsoft Windows 11","group":"g1","icon":"🪟"},{"id":"2","name":"Hệ điều hành di động Apple iOS","group":"g1","icon":"🍎"},{"id":"3","name":"Phần mềm đồ họa Adobe Photoshop","group":"g2","icon":"🎨"},{"id":"4","name":"Phần mềm duyệt web Google Chrome","group":"g2","icon":"🌐"}]},
        [{"question": "Phần mềm nào sau đây đóng vai trò là Hệ điều hành máy tính?", "options": ["Linux Ubuntu", "Microsoft Word", "Trình duyệt Safari"], "answer": 0, "explanation": "Linux Ubuntu là một hệ điều hành máy tính nguồn mở phổ biến."}],
        "Em đã nắm vững vai trò sống còn của Hệ điều hành đối với máy tính!"
    ))

    nodes.append(make_lesson(
        "G7-03", "w2", 7, "Quản lý Tệp, Thư mục & Đường dẫn (Path)", "Chủ đề 1: Máy tính và cộng đồng",
        "Bài 3: Quản lý dữ liệu trong máy tính", "Bài 3: Quản lý tệp và thư mục", "Bài 3: Lưu trữ dữ liệu an toàn",
        "sort-drag", ["G7-02"], 7,
        ["Hiểu cấu trúc cây thư mục phân cấp trong ổ đĩa.", "Đọc và viết đường dẫn tệp tuyệt đối (ví dụ: C:\\TinHoc7\\BaiTap\\bai1.xlsx)."],
        "Làm sao máy tính có thể định vị chính xác 1 bức ảnh trong số hơn 500.000 tệp tin đang lưu trên ổ đĩa cứng?",
        "Đường dẫn (Path) là chỉ dẫn từng bước từ ổ đĩa gốc qua các thư mục lồng nhau để đến tệp tin cần tìm. Các thành phần phân tách nhau bằng dấu gạch chéo ngược (\\ trong Windows) hoặc gạch chéo (/ trong Linux/macOS).",
        ["Tên tệp = Phần tên chính + Dấu chấm + Phần đuôi mở rộng.", "Phần mở rộng xác định loại tệp: .docx (văn bản), .xlsx (bảng tính), .pptx (trình chiếu), .pdf (tài liệu số)."],
        {"groups": [{"id": "g1", "name": "Đường dẫn Tệp Tuyệt đối"}, {"id": "g2", "name": "Tên Tệp Kèm Đuôi mở rộng"}], "items": [{"id":"1","name":"D:\\TaiLieu\\TinHoc7\\KiemTra.docx","group":"g1","icon":"📍"},{"id":"2","name":"C:\\Users\\Admin\\Pictures\\Logo.png","group":"g1","icon":"📍"},{"id":"3","name":"BangDiemTongKet_HK1.xlsx","group":"g2","icon":"📄"},{"id":"4","name":"BaiThuyetTrinh_DiaLy.pptx","group":"g2","icon":"📄"}]},
        [{"question": "Trong đường dẫn 'D:\\HocTap\\TinHoc\\Bai1.docx', tệp 'Bai1.docx' nằm trực tiếp trong thư mục nào?", "options": ["Thư mục TinHoc", "Thư mục HocTap", "Ổ đĩa D"], "answer": 0, "explanation": "Tệp Bai1.docx nằm ngay sau dấu gạch chéo của thư mục TinHoc."}],
        "Em đã làm chủ cấu trúc cây thư mục và đường dẫn tệp tin khoa học!"
    ))

    nodes.append(make_lesson(
        "G7-04", "w2", 7, "Mạng Xã hội & Quy tắc Ứng xử Văn hóa", "Chủ đề 2: Mạng xã hội",
        "Bài 4, 5: Mạng xã hội & Ứng xử trên mạng", "Bài 4: Giao tiếp văn minh trên MXH", "Bài 4: Ứng xử có văn hóa trên MXH",
        "branch-story", ["G6-05"], 7,
        ["Nhận thức sâu sắc tác động tích cực và mặt trái của mạng xã hội.", "Thực hiện Bộ quy tắc ứng xử trên mạng xã hội do Bộ Thông tin & Truyền thông ban hành."],
        "Lời nói gió bay, nhưng một câu bình luận trên mạng có thể tồn tại mãi mãi và để lại vết thương sâu sắc!",
        "Mạng xã hội giúp kết nối người thân, chia sẻ kiến thức, nhưng cũng tiềm ẩn nguy cơ bắt nạt ảo (Cyberbullying), tin giả, lừa đảo tài chính và nghiện mạng xã hội. Hãy luôn tôn trọng sự khác biệt, dùng ngôn từ nhã nhặn, không cổ xúy bạo lực.",
        ["Nguyên tắc: Tôn trọng - Trách nhiệm - Lành mạnh - An toàn.", "Không chia sẻ clip bạo lực học đường, không hùa theo đám đông chửi bới người khác."],
        {"scenarios": [{"id": "s1", "prompt": "Dưới bài đăng của một người bạn, có một nhóm người lạ vào bình luận ác ý, chê bai ngoại hình của bạn ấy thậm tệ.", "choices": [{"text": "Báo cáo bình luận xấu độc (Report), động viên bạn và khuyên bạn chặn các tài khoản đó.", "is_correct": True, "feedback": "Rất nhân văn! Em đã đứng về phía lẽ phải và bảo vệ bạn bè."}, {"text": "A dua hùa theo bình luận trêu chọc thêm cho vui.", "is_correct": False, "feedback": "Đó là hành vi tiếp tay cho bắt nạt trên không gian mạng rất xấu!"}]}]},
        [{"question": "Hành vi nào sau đây thể hiện văn hóa ứng xử tốt trên mạng xã hội?", "options": ["Tôn trọng quan điểm người khác, sử dụng ngôn từ lịch sự, văn minh", "Bình luận tục tĩu xúc phạm người khác", "Đăng tải ảnh nhạy cảm của bạn bè để trêu đùa"], "answer": 0, "explanation": "Văn minh, lịch sự là chuẩn mực đạo đức hàng đầu trên không gian mạng."}],
        "Em là một đại sứ văn hóa số đích thực, lan tỏa những điều tốt đẹp lên mạng xã hội!"
    ))

    nodes.append(make_lesson(
        "G7-05", "w2", 7, "An toàn Trực tuyến & Phòng chống Bắt nạt Mạng", "Chủ đề 3: Đạo đức, pháp luật",
        "Bài 5: An toàn trực tuyến", "Bài 5: An toàn trực tuyến & Tài khoản", "Bài 5: Nhận diện rủi ro không gian mạng",
        "branch-story", ["G7-04"], 7,
        ["Nhận diện các thủ đoạn lừa đảo qua mạng: giả mạo công an, hack tài khoản, dụ dỗ nạp tiền.", "Biết cách ứng phó khi bị đe dọa hoặc bắt nạt trên mạng."],
        "Không gian mạng không hoàn toàn màu hồng, luôn có những cạm bẫy vô hình rình rập người dùng sơ hở!",
        "Các kẻ lừa đảo thường đánh vào lòng tham hoặc sự sợ hãi của nạn nhân. Tuyệt đối không chuyển tiền theo yêu cầu của người lạ trên mạng, không bấm vào liên kết trúng thưởng, không gọi video call với người lạ yêu cầu cởi đồ hoặc làm hành vi nhạy cảm.",
        ["Bình tĩnh lưu lại bằng chứng (chụp ảnh màn hình) khi bị đe dọa.", "Chia sẻ ngay với bố mẹ, thầy cô hoặc gọi Tổng đài Quốc gia Bảo vệ Trẻ em 111."],
        {"scenarios": [{"id": "s1", "prompt": "Một tài khoản mạng mạo danh cô giáo chủ nhiệm nhắn tin yêu cầu em chuyển tiền quỹ lớp gấp vào một số tài khoản lạ.", "choices": [{"text": "Gọi điện thoại trực tiếp bằng số điện thoại di động thông thường cho cô giáo để xác minh.", "is_correct": True, "feedback": "Tuyệt vời! Gọi điện thoại trực tiếp là cách tốt nhất để chống lừa đảo mạo danh."}, {"text": "Chuyển tiền ngay vì sợ cô giáo phạt.", "is_correct": False, "feedback": "Sập bẫy lừa đảo rồi! Tài khoản đó đã bị hack hoặc mạo danh cô giáo!"}]}]},
        [{"question": "Khi trẻ em hoặc học sinh bị bắt nạt, đe dọa trên không gian mạng, số điện thoại Tổng đài Quốc gia miễn phí cần gọi ngay là gì?", "options": ["111 (Tổng đài Quốc gia Bảo vệ Trẻ em)", "113", "114"], "answer": 0, "explanation": "111 là số điện thoại đường dây nóng quốc gia bảo vệ trẻ em 24/7 hoàn toàn miễn phí."}],
        "Em đã trang bị lá chắn phòng thủ kiên cố trước mọi cạm bẫy trên không gian số!"
    ))

    nodes.append(make_lesson(
        "G7-06", "w2", 7, "Làm quen Bảng tính Điện tử & Địa chỉ Ô", "Chủ đề 4: Ứng dụng tin học",
        "Bài 6: Làm quen với phần mềm bảng tính", "Bài 6: Giao diện và thao tác bảng tính", "Bài 6: Làm quen Excel / Sheets",
        "sort-drag", ["G6-08"], 7,
        ["Nhận biết các thành phần giao diện: Hàng (Row), Cột (Column), Ô (Cell), Khối ô (Range).", "Phân biệt kiểu dữ liệu số, ký tự và ngày tháng trong bảng tính."],
        "Bảng tính điện tử sinh ra để giải phóng con người khỏi những phép tính cộng trừ sổ sách khô khan!",
        "Một bảng tính gồm nhiều trang tính (Worksheet). Cột được đánh dấu bằng chữ cái (A, B, C... Z, AA...), hàng đánh số (1, 2, 3...). Khối ô là vùng hình chữ nhật gồm nhiều ô liền kề, ký hiệu bằng địa chỉ ô góc trên bên trái và góc dưới bên phải cách nhau bởi dấu hai chấm (ví dụ: A1:D10).",
        ["Dữ liệu dạng số mặc định được căn thẳng lề bên phải ô tính.", "Dữ liệu dạng văn bản mặc định được căn thẳng lề bên trái ô tính."],
        {"groups": [{"id": "g1", "name": "Địa chỉ Khối ô Hợp lệ (Range)"}, {"id": "g2", "name": "Dữ liệu Kiểu Số (Number)"}], "items": [{"id":"1","name":"Khối ô B2:E8 (Hình chữ nhật 7 hàng 4 cột)","group":"g1","icon":"🔲"},{"id":"2","name":"Khối ô A1:A100 (Cột A gồm 100 hàng)","group":"g1","icon":"📏"},{"id":"3","name":"Con số 9.75 (Điểm trung bình học kỳ)","group":"g2","icon":"🔢"},{"id":"4","name":"Số tiền 1.500.000 đ (Chi phí quỹ lớp)","group":"g2","icon":"💵"}]},
        [{"question": "Trong phần mềm bảng tính, dữ liệu dạng số mặc định được căn lề nào trong ô?", "options": ["Căn thẳng lề phải", "Căn thẳng lề trái", "Căn giữa ô"], "answer": 0, "explanation": "Dữ liệu số căn phải để các hàng đơn vị, chục, trăm thẳng cột nhau."}],
        "Em đã nắm rất vững cấu trúc địa chỉ ô và khối ô của bảng tính điện tử!"
    ))

    nodes.append(make_lesson(
        "G7-07", "w2", 7, "Tính toán Tự động bằng Công thức Số học", "Chủ đề 4: Ứng dụng tin học",
        "Bài 7: Tính toán tự động trên bảng tính", "Bài 7: Nhập công thức và tính tự động", "Bài 7: Công thức & Tính toán",
        "logic-puzzle", ["G7-06"], 8,
        ["Nhập công thức toán học bắt đầu bằng dấu bằng (=).", "Hiểu cơ chế sao chép công thức tự động cập nhật địa chỉ ô tương đối."],
        "Thay đổi một con số ở ô đầu vào, hàng ngàn ô kết quả tự động tính toán lại trong chớp mắt!",
        "Quy tắc vàng: Mọi công thức trong bảng tính luôn phải bắt đầu bằng dấu =. Sử dụng toán tử: + (cộng), - (trừ), * (nhân), / (chia), ^ (lũy thừa). Khi sao chép công thức xuống dưới, các địa chỉ ô tương đối (như A1, B1) sẽ tự động dịch chuyển tương ứng (thành A2, B2).",
        ["Ví dụ công thức: =B2*C2 (Thành tiền = Số lượng nhân Đơn giá).", "Sử dụng dấu ngoặc tròn () để ưu tiên phép tính."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [4, 8, 12]},
        [{"question": "Tại ô D2, công thức '=B2+C2' có kết quả là 15. Nếu sao chép công thức này xuống ô D3, công thức tại ô D3 sẽ tự động chuyển thành gì?", "options": ["=B3+C3", "=B2+C2", "=B4+C4"], "answer": 0, "explanation": "Địa chỉ tương đối tự động tăng số hàng lên 1 khi kéo công thức xuống dưới."}],
        "Công thức tính toán tự động của em chạy cực kỳ chính xác!"
    ))

    nodes.append(make_lesson(
        "G7-08", "w2", 7, "Các hàm Tính toán Cơ bản (SUM, AVG, MIN, MAX)", "Chủ đề 4: Ứng dụng tin học",
        "Bài 8: Công cụ hỗ trợ tính toán", "Bài 8: Các hàm tính toán thông dụng", "Bài 8: Hàm xử lý dữ liệu cơ bản",
        "logic-puzzle", ["G7-07"], 8,
        ["Sử dụng thành thạo 5 hàm cốt lõi: SUM, AVERAGE, COUNT, MAX, MIN.", "Cú pháp chuẩn: =TÊN_HÀM(danh_sách_đối_số)."],
        "Không cần viết dấu cộng cho 50 ô, chỉ cần một hàm SUM duy nhất!",
        "Hàm là công thức đã được định nghĩa sẵn: =SUM(A1:A50) tính tổng 50 ô; =AVERAGE(B2:B10) tính giá trị trung bình cộng; =MAX(C1:C20) tìm giá trị lớn nhất; =MIN(C1:C20) tìm giá trị nhỏ nhất; =COUNT(D1:D30) đếm số lượng ô chứa dữ liệu số.",
        ["Đối số của hàm có thể là địa chỉ ô, khối ô hoặc các số cụ thể.", "Tên hàm không phân biệt chữ hoa chữ thường (sum hay SUM đều đúng)."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [5, 11, 14]},
        [{"question": "Để tìm điểm số cao nhất trong danh sách điểm ở khối ô C2:C40, em dùng hàm nào sau đây?", "options": ["=MAX(C2:C40)", "=SUM(C2:C40)", "=AVERAGE(C2:C40)"], "answer": 0, "explanation": "Hàm MAX trả về giá trị số lớn nhất trong danh sách đối số."}],
        "Em đã vận dụng thành thạo các hàm tính toán thống kê bảng tính!"
    ))

    nodes.append(make_lesson(
        "G7-09", "w2", 7, "Trình bày & Định dạng Bảng tính Chuẩn mực", "Chủ đề 4: Ứng dụng tin học",
        "Bài 9, 10: Trình bày & Định dạng nâng cao", "Bài 9, 10: Kẻ khung & In bảng tính", "Bài 9, 10: Định dạng & Sắp xếp dữ liệu",
        "sort-drag", ["G7-08"], 7,
        ["Kẻ đường viền khung bảng (Borders), tô màu nền (Fill Color).", "Định dạng hiển thị kiểu tiền tệ (Currency), số thập phân (Decimal Places), phần trăm (Percentage)."],
        "Một bảng tính được trình bày trang nhã giúp sếp và đối tác đọc hiểu số liệu trong vòng 5 giây!",
        "Vào nhóm Font để kẻ viền bảng: Viền ngoài nét đậm, viền trong nét đơn. Vào nhóm Number để chỉnh số chữ số sau dấu phẩy (Increase/Decrease Decimal). Sử dụng tính năng Cố định hàng tiêu đề (Freeze Panes) để khi cuộn trang xuống sâu, tiêu đề bảng vẫn luôn hiển thị.",
        ["Gộp ô và căn giữa tiêu đề lớn bằng nút Merge & Center.", "Chức năng Wrap Text giúp chữ tự động xuống dòng trong ô hẹp."],
        {"groups": [{"id": "g1", "name": "Định dạng Hiển thị Số (Number Format)"}, {"id": "g2", "name": "Trình bày Khung bảng (Cell Styles)"}], "items": [{"id":"1","name":"Thêm ký hiệu tiền tệ VNĐ vào sau số","group":"g1","icon":"💲"},{"id":"2","name":"Lấy 2 chữ số thập phân sau dấu phẩy (ví dụ: 8.50)","group":"g1","icon":"🎯"},{"id":"3","name":"Kẻ đường viền đôi All Borders xung quanh bảng","group":"g2","icon":"▦"},{"id":"4","name":"Cố định hàng tiêu đề đầu tiên (Freeze Top Row)","group":"g2","icon":"📌"}]},
        [{"question": "Khi ô tính xuất hiện dãy ký tự '###', điều đó có nghĩa là gì?", "options": ["Độ rộng của cột quá hẹp không đủ hiển thị hết con số", "Công thức bị lỗi tính toán", "Dữ liệu bị virus xóa mất"], "answer": 0, "explanation": "Dãy '###' báo hiệu cột bị hẹp, chỉ cần kéo rộng cột ra là số sẽ hiện bình thường."}],
        "Bảng tính của em được định dạng rất chuyên nghiệp và thẩm mỹ cao!"
    ))

    nodes.append(make_lesson(
        "G7-10", "w2", 7, "Thiết kế Bài Trình chiếu Chuyên đề", "Chủ đề 4: Ứng dụng tin học",
        "Bài 11, 12: Tạo bài trình chiếu & Định dạng", "Bài 11, 12: Bài trình chiếu chuyên đề & Hoạt cảnh", "Bài 11, 12: Thuyết trình ấn tượng & Video",
        "match-memory", ["G6-08"], 7,
        ["Thiết lập bài thuyết trình có cấu trúc phân tầng khoa học.", "Tích hợp biểu đồ, sơ đồ SmartArt và định dạng đồng bộ Theme."],
        "Thuyết trình là nghệ thuật truyền cảm hứng: Hình ảnh dẫn lối, câu từ chắt lọc!",
        "Một bài trình chiếu chuyên đề hoàn chỉnh cần: Trang bìa (Tiêu đề, Tác giả), Trang mục lục, Các trang nội dung theo từng chương, Trang kết luận và Trang cảm ơn. Sử dụng sơ đồ SmartArt để mô hình hóa quy trình thay vì gạch đầu dòng khô khan.",
        ["Quy tắc 1 slide 1 thông điệp chính.", "Sử dụng màu sắc trang nhã, tránh dùng quá 3 phông chữ trên 1 bài trình chiếu."],
        {"cards": [{"id":"1","name":"Sơ đồ SmartArt","match":"Công cụ trực quan hóa quy trình, chu trình và phân cấp ý tưởng"},{"id":"2","name":"Mẫu Slide Master","match":"Trang mẫu định nghĩa bố cục, màu sắc và logo chung cho toàn bộ bài"},{"id":"3","name":"Hiệu ứng Nhấn mạnh (Emphasis)","match":"Làm đổi màu hoặc phóng to đối tượng để thu hút sự chú ý"},{"id":"4","name":"Bộ màu Theme Colors","match":"Bảng phối màu hài hòa chuẩn mỹ thuật thị giác"}]},
        [{"question": "Công cụ nào trong PowerPoint giúp chuyển danh sách gạch đầu dòng thành sơ đồ khối đồ họa bắt mắt chỉ bằng 1 cú nhấp chuột?", "options": ["Chuyển đổi sang SmartArt (Convert to SmartArt)", "Chèn hình ảnh Pictures", "Vẽ bảng Table"], "answer": 0, "explanation": "SmartArt tự động biến văn bản thành các khối sơ đồ trực quan."}],
        "Bài thuyết trình của em đạt đẳng cấp thuyết phục người xem rất cao!"
    ))

    nodes.append(make_lesson(
        "G7-11", "w2", 7, "Thuật toán Tìm kiếm Tuần tự (Sequential Search)", "Chủ đề 5: Giải quyết vấn đề",
        "Bài 13: Thuật toán tìm kiếm tuần tự", "Bài 13: Tìm kiếm tuần tự trong danh sách", "Bài 13: Thuật toán tìm kiếm tuần tự",
        "block-maze", ["G6-09"], 8,
        ["Mô tả nguyên lý tìm kiếm tuần tự: duyệt lần lượt từ đầu đến cuối danh sách.", "Đánh giá số lần so sánh: Trường hợp tốt nhất (1 lần) và xấu nhất (N lần)."],
        "Khi tìm một chiếc chìa khóa bị đánh rơi trên sân bóng, em sẽ tìm như thế nào nếu sân bóng chưa được dọn dẹp ngăn nắp?",
        "Tìm kiếm tuần tự duyệt qua từng phần tử một trong danh sách, bắt đầu từ phần tử đầu tiên cho đến khi tìm thấy phần tử cần tìm hoặc đã duyệt hết toàn bộ danh sách mà không thấy. Thuật toán này áp dụng được cho mọi danh sách, kể cả danh sách chưa sắp xếp.",
        ["Ưu điểm: đơn giản, áp dụng được cho danh sách lộn xộn.", "Nhược điểm: chạy chậm khi số lượng phần tử N rất lớn."],
        {"grid_size": 4, "start": {"x": 0, "y": 0, "dir": "E"}, "target": {"x": 3, "y": 1}, "walls": [{"x": 1, "y": 0}], "allowed_blocks": ["forward", "turn_right", "turn_left"], "max_blocks": 6},
        [{"question": "Trong danh sách gồm 100 học sinh, nếu dùng thuật toán tìm kiếm tuần tự, trong trường hợp xấu nhất (học sinh ở cuối danh sách hoặc không có), ta phải thực hiện bao nhiêu lần so sánh?", "options": ["100 lần so sánh", "1 lần so sánh", "10 lần so sánh"], "answer": 0, "explanation": "Trường hợp xấu nhất thuật toán phải duyệt qua toàn bộ 100 phần tử."}],
        "Em đã nắm vững nguyên lý hoạt động của thuật toán tìm kiếm tuần tự!"
    ))

    nodes.append(make_lesson(
        "G7-12", "w2", 7, "Thuật toán Tìm kiếm Nhị phân (Binary Search)", "Chủ đề 5: Giải quyết vấn đề",
        "Bài 14: Thuật toán tìm kiếm nhị phân", "Bài 14: Tìm kiếm nhị phân trên dãy đã sắp", "Bài 14: Tìm kiếm nhị phân chia để trị",
        "logic-puzzle", ["G7-11"], 8,
        ["Hiểu điều kiện tiên quyết: danh sách BẮT BUỘC phải được sắp xếp trước.", "Nguyên lý chia đôi không gian tìm kiếm: mỗi bước loại bỏ 1/2 danh sách."],
        "Đoán một số từ 1 đến 1.000.000 mà chỉ cần tối đa 20 câu hỏi? Đó chính là sức mạnh thần kỳ của Tìm kiếm nhị phân!",
        "Thuật toán so sánh giá trị cần tìm với phần tử ở chính giữa danh sách. Nếu bằng nhau -> Tìm thấy! Nếu nhỏ hơn -> Bỏ nửa sau, chỉ tìm ở nửa trước. Nếu lớn hơn -> Bỏ nửa trước, chỉ tìm ở nửa sau. Cứ như vậy, phạm vi thu hẹp theo cấp số nhân: log2(N).",
        ["Với 1 tỷ phần tử đã sắp xếp, tìm kiếm nhị phân chỉ mất tối đa 30 lần so sánh!", "Bắt buộc danh sách phải được sắp xếp tăng dần hoặc giảm dần trước."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [1, 2, 4]},
        [{"question": "Điều kiện BẮT BUỘC để có thể áp dụng được thuật toán tìm kiếm nhị phân là gì?", "options": ["Danh sách phải được sắp xếp theo thứ tự (tăng dần hoặc giảm dần)", "Danh sách phải có số lượng phần tử chẵn", "Danh sách phải toàn là số nguyên dương"], "answer": 0, "explanation": "Tìm kiếm nhị phân chỉ hoạt động khi danh sách đã được sắp xếp."}],
        "Tư duy tìm kiếm nhị phân chia đôi không gian của em thật siêu việt!"
    ))

    nodes.append(make_lesson(
        "G7-13", "w2", 7, "Thuật toán Sắp xếp Nổi bọt (Bubble Sort)", "Chủ đề 5: Giải quyết vấn đề",
        "Bài 15: Thuật toán sắp xếp nổi bọt", "Bài 15: Sắp xếp bằng thuật toán nổi bọt", "Bài 15: Thuật toán sắp xếp nổi bọt",
        "block-maze", ["G7-11"], 8,
        ["Mô tả cơ chế hoán đổi các cặp phần tử liền kề sai thứ tự.", "Hiểu tại sao gọi là nổi bọt: phần tử lớn nhất dần nổi về cuối dãy sau mỗi lượt duyệt."],
        "Giống như những bọt khí nhẹ nổi dần lên mặt nước, các số lớn sẽ nổi dần về cuối dãy!",
        "Ở mỗi lượt duyệt, ta so sánh từng cặp hai phần tử cạnh nhau. Nếu phần tử đứng trước lớn hơn phần tử đứng sau, ta đổi chỗ (hoán đổi) chúng cho nhau. Sau lượt duyệt thứ nhất, phần tử lớn nhất dãy chắc chắn nằm ở vị trí cuối cùng. Lặp lại với các phần tử còn lại.",
        ["Cần thực hiện tối đa N - 1 lượt duyệt.", "Độ phức tạp thời gian trong trường hợp xấu nhất là O(N^2)."],
        {"grid_size": 4, "start": {"x": 0, "y": 0, "dir": "E"}, "target": {"x": 3, "y": 3}, "walls": [{"x": 1, "y": 2}, {"x": 2, "y": 1}], "allowed_blocks": ["forward", "turn_right", "turn_left"], "max_blocks": 8},
        [{"question": "Trong thuật toán sắp xếp nổi bọt tăng dần, nếu hai phần tử liền kề là [8, 3], máy tính sẽ làm gì?", "options": ["Đổi chỗ hai số cho nhau thành [3, 8]", "Giữ nguyên thứ tự", "Xóa số 8 đi"], "answer": 0, "explanation": "Vì 8 > 3 nên nghịch thế, cần hoán đổi để số nhỏ đứng trước."}],
        "Em đã mô phỏng thành công thuật toán sắp xếp nổi bọt kinh điển!"
    ))

    nodes.append(make_lesson(
        "G7-14", "w2", 7, "Đấu trường Trùm Lớp 7: Phù thủy Sắp xếp & Tìm kiếm", "Tổng kết GDPT 2018 Lớp 7",
        "Bài 16: Thuật toán sắp xếp chọn & Tổng kết", "Bài 16: Sắp xếp chọn & Tổng kết", "Bài 16: Sắp xếp chọn & Đánh giá năng lực",
        "boss-quiz", ["G7-06", "G7-08", "G7-11", "G7-12", "G7-13"], 12,
        ["Tổng kết toàn diện chuẩn năng lực Tin học Lớp 7 của cả 3 bộ sách.", "Sẵn sàng nhận danh hiệu Phù Thủy Thuật Toán Sắp Xếp & Tìm Kiếm EasyTin."],
        "Trùm Thuật Toán Hắc Ám 'Glitch-Sorter' đang đảo lộn toàn bộ dữ liệu bảng tính thế giới! Hãy dùng các thuật toán đỉnh cao để đánh bại nó!",
        "Đấu trường tổng hợp: Hệ điều hành, Bảng tính Excel, Hàm thống kê, Tìm kiếm nhị phân và Sắp xếp nổi bọt / Sắp xếp chọn.",
        ["Tìm kiếm nhị phân chia đôi không gian O(log N).", "Bảng tính điện tử và các hàm SUM, AVERAGE, MIN, MAX."],
        {"boss_name": "Glitch-Sorter Trùm Thuật Toán", "boss_max_hp": 100, "player_max_hp": 100, "damage_per_hit": 25, "questions_pool": 4},
        [
            {"question": "Thuật toán sắp xếp chọn (Selection Sort) hoạt động theo nguyên lý nào?", "options": ["Tìm phần tử nhỏ nhất trong dãy chưa sắp xếp rồi đưa về vị trí đầu tiên", "So sánh hai phần tử liền kề và đổi chỗ", "Chia đôi danh sách làm hai nửa độc lập", "Xóa các phần tử lẻ"], "answer": 0, "explanation": "Sắp xếp chọn luôn tìm phần tử cực trị (min/max) đưa về đúng vị trí."},
            {"question": "Trong bảng tính, công thức '=AVERAGE(10, 20, 30)' cho kết quả bằng bao nhiêu?", "options": ["20", "60", "30", "10"], "answer": 0, "explanation": "Trung bình cộng của (10 + 20 + 30) / 3 = 60 / 3 = 20."},
            {"question": "Nếu danh sách có 16 phần tử đã sắp xếp, thuật toán tìm kiếm nhị phân cần tối đa bao nhiêu lần so sánh để tìm ra phần tử?", "options": ["4 lần (vì 2^4 = 16)", "16 lần", "8 lần", "1 lần"], "answer": 0, "explanation": "log2(16) = 4, tối đa chỉ cần 4 lần chia đôi."},
            {"question": "Hành vi nào sau đây là vi phạm pháp luật trên mạng xã hội?", "options": ["Xúc phạm danh dự, vu khống người khác", "Chia sẻ bài viết học tập có trích nguồn", "Báo cáo nội dung xấu độc cho quản trị viên", "Đổi mật khẩu định kỳ 3 tháng/lần"], "answer": 0, "explanation": "Vu khống, xúc phạm người khác vi phạm nghiêm trọng Luật An ninh mạng."}
        ],
        "CHIẾN THẮNG HUY HOÀNG! Em đã chinh phục trọn vẹn toàn bộ chương trình Tin học Lớp 7 của cả 3 bộ sách KNTT, Cánh Diều, CTST!"
    ))

    # =========================================================================
    # LỚP 8 (13 NÚT)
    # =========================================================================
    nodes.append(make_lesson(
        "G8-01", "w2", 8, "Lược sử Phát triển Máy tính & Định luật Moore", "Chủ đề 1: Máy tính và cộng đồng",
        "Bài 1: Lược sử công cụ tính toán", "Bài 1: Lịch sử phát triển máy tính", "Bài 1: Quá trình phát triển máy tính",
        "match-memory", ["G7-01"], 7,
        ["Nêu 5 thế hệ máy tính điện tử từ đèn điện tử chân không đến vi xử lý VLSI.", "Hiểu nội dung Định luật Moore về sự tăng trưởng số lượng bóng bán dẫn."],
        "Từ cỗ máy tính nặng 30 tấn ENIAC chiếm trọn căn phòng lớn đến chiếc điện thoại siêu mỏng nằm gọn trong lòng bàn tay!",
        "Thế hệ 1 (1940-1956): Đèn điện tử chân không, kích thước khổng lồ, tiêu tốn điện năng. Thế hệ 2 (1956-1963): Bóng bán dẫn Transistor, nhỏ gọn và bền hơn. Thế hệ 3 (1964-1971): Mạch tích hợp IC. Thế hệ 4 (1971-nay): Vi xử lý siêu tích hợp VLSI (chip CPU). Thế hệ 5: Máy tính quang học, máy tính lượng tử và Trí tuệ nhân tạo.",
        ["Định luật Moore: Số lượng bóng bán dẫn trên một vi mạch tăng gấp đôi sau mỗi khoảng 2 năm.", "Máy tính ngày càng nhỏ hơn, rẻ hơn, nhanh hơn và tiết kiệm năng lượng hơn."],
        {"cards": [{"id":"1","name":"Thế hệ 1 (1945)","match":"Đèn điện tử chân không (Vacuum Tube) - Máy ENIAC"},{"id":"2","name":"Thế hệ 2 (1955)","match":"Bóng bán dẫn Transistor nhỏ gọn và tin cậy hơn"},{"id":"3","name":"Thế hệ 3 (1965)","match":"Mạch tích hợp IC (Integrated Circuit) chứa nhiều linh kiện"},{"id":"4","name":"Thế hệ 4 (1971-nay)","match":"Vi xử lý Microprocessor chứa hàng triệu transistor trên 1 chip"}]},
        [{"question": "Linh kiện điện tử chủ đạo của thế hệ máy tính thứ nhất (như máy ENIAC) là gì?", "options": ["Đèn điện tử chân không", "Bóng bán dẫn Transistor", "Mạch vi xử lý vi mô"], "answer": 0, "explanation": "Thế hệ máy tính đầu tiên sử dụng hàng vạn bóng đèn điện tử chân không to và nóng."}],
        "Em đã nắm vững các mốc son lịch sử vẻ vang của ngành khoa học máy tính thế giới!"
    ))

    nodes.append(make_lesson(
        "G8-02", "w2", 8, "Thông tin Đáng tin cậy trong Môi trường Số", "Chủ đề 1: Máy tính và cộng đồng",
        "Bài 2, 3: Thông tin số & Khai thác thông tin", "Bài 2: Thông tin đáng tin cậy", "Bài 2: Thông tin đáng tin cậy & không tin cậy",
        "branch-story", ["G7-04"], 7,
        ["Đánh giá 4 tiêu chí của thông tin đáng tin cậy: Tác giả, Mục đích, Tính cập nhật, Dẫn chứng khoa học.", "Phương pháp kiểm chứng chéo (Cross-check) từ nhiều nguồn dữ liệu."],
        "Trong thời đại bùng nổ thông tin, khả năng phân định đúng sai quý giá hơn bất kỳ kho vàng nào!",
        "Thông tin sai lệch có thể gây tổn hại kinh tế, sức khỏe và danh dự. Khi đọc tin tức trên mạng, hãy đặt câu hỏi: Ai là tác giả? Trang web này thuộc tổ chức nào? Bài viết có dẫn số liệu nghiên cứu cụ thể không? Ngày xuất bản khi nào?",
        ["Tránh bẫy tin tức giật gân (Clickbait) kích động cảm xúc thù ghét hoặc sợ hãi.", "Kiểm tra chéo với các trang thông tấn báo chí chính thống uy tín."],
        {"scenarios": [{"id": "s1", "prompt": "Một bài đăng trên mạng xã hội khẳng định 'Uống nước lá cây rừng có thể chữa khỏi 100% bệnh ung thư' và kêu gọi chuyển khoản mua thuốc gấp.", "choices": [{"text": "Báo cáo tin giả lừa đảo, đối chiếu với khuyến cáo của Bộ Y tế và khuyên người thân không tin theo.", "is_correct": True, "feedback": "Rất chuẩn mực! Đó là tin giả lừa đảo chữa bệnh cực kỳ nguy hiểm."}, {"text": "Chia sẻ ngay bài viết lên trang cá nhân để mọi người cùng mua.", "is_correct": False, "feedback": "Tiếp tay cho lừa đảo y tế có thể làm hại đến tính mạng người bệnh!"}]}]},
        [{"question": "Tiêu chí nào sau đây khẳng định một bài viết khoa học có độ tin cậy cao?", "options": ["Có trích dẫn nguồn số liệu từ viện nghiên cứu y khoa uy tín và rõ tên tác giả", "Có nhiều biểu tượng cảm xúc nhấp nháy bắt mắt", "Được nhiều tài khoản ẩn danh chia sẻ"], "answer": 0, "explanation": "Dẫn chứng khoa học từ viện nghiên cứu chính thống là bảo chứng cho độ tin cậy."}],
        "Em đã rèn luyện tư duy phản biện sắc sảo trước mọi luồng thông tin trên mạng!"
    ))

    nodes.append(make_lesson(
        "G8-03", "w2", 8, "Đạo đức, Văn hóa Số & Luật An ninh Mạng", "Chủ đề 3: Đạo đức, pháp luật",
        "Bài 4: Đạo đức và văn hóa số", "Bài 3: Đạo đức, pháp luật & Văn hóa số", "Bài 3: Đạo đức và văn hóa số",
        "branch-story", ["G7-05"], 7,
        ["Hiểu các điều khoản cơ bản của Luật An ninh mạng năm 2018 tại Việt Nam.", "Quy định về bảo vệ bản quyền phần mềm và chế tài xử phạt khi dùng phần mềm bẻ khóa (Crack)."],
        "Không gian mạng là thế giới ảo nhưng trách nhiệm pháp lý và hậu quả là hoàn toàn có thật!",
        "Luật An ninh mạng nghiêm cấm: Xúc phạm nghiêm trọng danh dự người khác, phát tán tin giả gây hoang mang dư luận, tấn công phá hoại hệ thống thông tin quốc gia. Sử dụng phần mềm bẻ khóa (crack) vừa vi phạm pháp luật sở hữu trí tuệ, vừa khiến máy tính bị cài mã độc gián điệp.",
        ["Ưu tiên sử dụng phần mềm có bản quyền chính hãng hoặc phần mềm nguồn mở FOSS.", "Mọi phát ngôn trên mạng đều có thể được cơ quan an ninh truy vết qua địa chỉ IP."],
        {"scenarios": [{"id": "s1", "prompt": "Một người bạn gửi cho em đường link tải bản 'Crack' của một phần mềm đồ họa nổi tiếng có giá gốc rất đắt.", "choices": [{"text": "Từ chối tải và sử dụng phần mềm mã nguồn mở miễn phí hợp pháp tương đương (như GIMP/Inkscape).", "is_correct": True, "feedback": "Rất thông thái! Phần mềm nguồn mở vừa miễn phí, vừa an toàn không chứa mã độc."}, {"text": "Tắt phần mềm diệt virus rồi chạy file crack đó ngay.", "is_correct": False, "feedback": "File crack thường bị kẻ xấu cài cắm Trojan gián điệp đánh cắp mật khẩu!"}]}]},
        [{"question": "Hành vi nào sau đây bị nghiêm cấm theo Luật An ninh mạng Việt Nam?", "options": ["Phát tán chương trình tin học độc hại, xâm nhập trái phép mạng máy tính", "Học lập trình website", "Gửi email chúc mừng sinh nhật bạn"], "answer": 0, "explanation": "Phát tán mã độc, tấn công mạng là tội phạm công nghệ cao bị xử phạt rất nặng."}],
        "Em là một công dân số gương mẫu, luôn tuân thủ pháp luật và đạo đức số!"
    ))

    nodes.append(make_lesson(
        "G8-04", "w2", 8, "Bảng tính Nâng cao: Lọc Dữ liệu & Biểu đồ", "Chủ đề 4: Ứng dụng tin học",
        "Bài 5, 6, 7: Bảng tính, Sắp xếp, Lọc & Biểu đồ", "Bài 4, 5: Biểu đồ & Bộ lọc Filter", "Bài 4, 5: Bảng tính nâng cao & Biểu đồ",
        "sort-drag", ["G7-09"], 7,
        ["Sử dụng công cụ AutoFilter để trích lọc dữ liệu theo điều kiện số và chữ.", "Tạo các dạng biểu đồ: Biểu đồ cột (Column), Biểu đồ tròn (Pie), Biểu đồ đường (Line)."],
        "Một bức biểu đồ trực quan có giá trị truyền tải thông tin bằng cả ngàn dòng số liệu khô khan!",
        "Công cụ AutoFilter tạo các nút mũi tên thả xuống ở tiêu đề cột: có thể lọc các giá trị lớn hơn mức chuẩn, lọc các học sinh đạt học lực Xuất sắc. Biểu đồ cột dùng để so sánh số lượng; Biểu đồ tròn biểu diễn tỉ lệ phần trăm cơ cấu; Biểu đồ đường biểu diễn xu hướng biến động theo thời gian.",
        ["Vào thẻ Insert chọn nhóm Charts để chèn biểu đồ.", "Tùy biến tiêu đề biểu đồ (Chart Title), chú giải (Legend) và nhãn dữ liệu (Data Labels)."],
        {"groups": [{"id": "g1", "name": "Dạng Biểu đồ Trực quan (Chart Types)"}, {"id": "g2", "name": "Công cụ Xử lý Dữ liệu Nâng cao"}], "items": [{"id":"1","name":"Biểu đồ tròn Pie Chart (Tỉ lệ phần trăm học lực)","group":"g1","icon":"🥧"},{"id":"2","name":"Biểu đồ cột Clustered Column (So sánh doanh thu)","group":"g1","icon":"📊"},{"id":"3","name":"Bộ lọc tự động AutoFilter theo tiêu chí","group":"g2","icon":"🔍"},{"id":"4","name":"Sắp xếp đa cấp tiêu chí (Custom Sort)","group":"g2","icon":"🔀"}]},
        [{"question": "Khi muốn biểu diễn sự biến động nhiệt độ của các tháng trong năm để thấy rõ xu hướng tăng giảm, dạng biểu đồ nào là thích hợp nhất?", "options": ["Biểu đồ đường (Line Chart)", "Biểu đồ tròn (Pie Chart)", "Biểu đồ thanh ngang"], "answer": 0, "explanation": "Biểu đồ đường là lựa chọn tối ưu để thể hiện xu hướng biến động theo thời gian."}],
        "Kỹ năng trực quan hóa dữ liệu và trích lọc thông tin của em rất xuất sắc!"
    ))

    nodes.append(make_lesson(
        "G8-05", "w2", 8, "Đồ họa Chỉnh sửa Ảnh Raster & Tạo Ảnh động GIF", "Chủ đề 4: Ứng dụng tin học",
        "Bài 8, 9: Đồ họa chỉnh sửa ảnh & Ảnh động", "Bài 6, 7: Chỉnh sửa ảnh & Hiệu ứng", "Bài 6, 7: Đồ họa ảnh & Biên tập",
        "sort-drag", ["G7-10"], 7,
        ["Làm quen khái niệm Lớp ảnh (Layers) trong phần mềm đồ họa (GIMP/Photoshop).", "Tạo ảnh động GIF bằng cách kết hợp chuỗi khung hình (Frames) và tốc độ chuyển khung hình."],
        "Khám phá phép thuật biến hóa hình ảnh của các phù thủy thiết kế đồ họa số!",
        "Lớp ảnh (Layer) giống như những tấm kính trong suốt xếp chồng lên nhau. Vẽ trên lớp này không làm hỏng hình ảnh của lớp bên dưới. Ảnh động (Animated GIF) được tạo thành từ nhiều lớp ảnh phát tuần tự theo thời gian tạo ảo giác chuyển động nhịp nhàng.",
        ["Độ phân giải DPI và hệ màu RGB (Red, Green, Blue) cho màn hình hiển thị.", "Công cụ Clone Stamp sao chép và xóa vật thể thừa trên ảnh."],
        {"groups": [{"id": "g1", "name": "Khái niệm Lớp ảnh (Layers)"}, {"id": "g2", "name": "Thông số Kỹ thuật Ảnh động (GIF)"}], "items": [{"id":"1","name":"Xếp chồng các lớp ảnh trong suốt lên nhau","group":"g1","icon":"📑"},{"id":"2","name":"Đổi chế độ hòa trộn lớp Blending Mode","group":"g1","icon":"✨"},{"id":"3","name":"Thiết lập thời gian trễ giữa các khung hình (100ms)","group":"g2","icon":"⏱️"},{"id":"4","name":"Chế độ lặp lại vô tận (Looping Forever)","group":"g2","icon":"🔁"}]},
        [{"question": "Trong phần mềm chỉnh sửa ảnh, tính năng 'Layer' (Lớp) mang lại ưu điểm lớn nhất là gì?", "options": ["Cho phép chỉnh sửa từng chi tiết độc lập mà không ảnh hưởng đến các phần khác", "Làm máy tính chạy chậm hơn", "Làm mất màu bức ảnh"], "answer": 0, "explanation": "Các lớp ảnh độc lập giúp thiết kế linh hoạt, dễ dàng sửa đổi từng chi tiết."}],
        "Tác phẩm đồ họa và ảnh động của em trông cực kỳ nghệ thuật và sống động!"
    ))

    nodes.append(make_lesson(
        "G8-06", "w2", 8, "Nhập môn Lập trình Giải quyết Bài toán", "Chủ đề 5: Giải quyết vấn đề",
        "Bài 10: Lập trình trực quan giải bài toán", "Bài 8: Lập trình giải quyết bài toán", "Bài 8: Khái niệm lập trình & thuật toán",
        "block-maze", ["G7-13"], 8,
        ["Quy trình 4 bước phát triển phần mềm: Xác định bài toán -> Thiết kế thuật toán -> Viết mã nguồn -> Kiểm thử.", "Chuyển từ tư duy kéo thả Scratch sang tư duy câu lệnh tường minh."],
        "Lập trình không chỉ là gõ code, đó là nghệ thuật tư duy giải quyết vấn đề của con người thời đại số!",
        "Bước 1: Xác định Input (Đầu vào) và Output (Đầu ra). Bước 2: Thiết kế thuật toán bằng sơ đồ khối hoặc mã giả. Bước 3: Cài đặt bằng ngôn ngữ lập trình cụ thể. Bước 4: Kiểm thử với nhiều bộ dữ liệu để gỡ sạch lỗi.",
        ["Chương trình = Cấu trúc dữ liệu + Thuật toán.", "Tính logic chặt chẽ: máy tính làm chính xác những gì ta ra lệnh, không phải những gì ta nghĩ trong đầu."],
        {"grid_size": 4, "start": {"x": 0, "y": 0, "dir": "E"}, "target": {"x": 3, "y": 2}, "walls": [{"x": 1, "y": 1}], "allowed_blocks": ["forward", "turn_right", "turn_left"], "max_blocks": 6},
        [{"question": "Bước đầu tiên và quan trọng nhất khi bắt đầu giải quyết một bài toán tin học là gì?", "options": ["Xác định rõ dữ liệu đầu vào (Input) và kết quả mong muốn (Output)", "Bật máy tính gõ mã lệnh ngay lập tức", "Thiết kế logo biểu tượng phần mềm"], "answer": 0, "explanation": "Xác định rõ Input và Output là kim chỉ nam cho toàn bộ quá trình lập trình."}],
        "Em đã nắm vững phương pháp luận chuẩn mực của kỹ sư phần mềm!"
    ))

    nodes.append(make_lesson(
        "G8-07", "w2", 8, "Kiểu Dữ liệu, Biến, Hằng & Biểu thức Số học", "Chủ đề 5: Giải quyết vấn đề",
        "Bài 11: Kiểu dữ liệu và biểu thức", "Bài 9: Biến số, hằng số & Kiểu dữ liệu", "Bài 9: Biến, kiểu dữ liệu & Phép toán",
        "logic-puzzle", ["G8-06"], 8,
        ["Phân biệt 4 kiểu dữ liệu cơ bản: Số nguyên (Integer), Số thực (Float), Xâu ký tự (String), Logic (Boolean).", "Phân biệt Biến (thay đổi giá trị) và Hằng (giá trị bất biến không đổi suốt chương trình)."],
        "Mỗi loại dữ liệu đều cần một chiếc bình chứa có hình dạng và kích thước thích hợp!",
        "Kiểu số nguyên (int): -5, 0, 100. Kiểu số thực (float): 3.14, -0.5. Kiểu xâu ký tự (string): đặt trong nháy kép \"Xin chao\". Kiểu logic (bool): chỉ nhận True hoặc False. Hằng số (Constant): ví dụ hằng số PI = 3.14159, cố định giá trị để tránh vô tình bị sửa đổi.",
        ["Toán tử chia lấy phần nguyên (//) và chia lấy phần dư (%).", "Biểu thức so sánh: ==, !=, >, <, >=, <= kết hợp logic and, or, not."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [3, 9, 15]},
        [{"question": "Phép toán '17 % 5' (chia lấy phần dư) trong lập trình cho kết quả bằng bao nhiêu?", "options": ["2 (vì 17 chia 5 bằng 3 dư 2)", "3", "0"], "answer": 0, "explanation": "Toán tử % chia lấy phần dư: 17 = 5 * 3 + 2, phần dư là 2."}],
        "Tư duy kiểu dữ liệu và biểu thức toán học của em rất chuẩn xác!"
    ))

    nodes.append(make_lesson(
        "G8-08", "w2", 8, "Cấu trúc Điều kiện Rẽ nhánh (If - Else Nâng cao)", "Chủ đề 5: Giải quyết vấn đề",
        "Bài 12: Câu lệnh rẽ nhánh", "Bài 10: Biểu thức logic & Câu lệnh if/else", "Bài 10: Cấu trúc rẽ nhánh lồng nhau",
        "bug-hunt", ["G8-07"], 8,
        ["Lập trình câu lệnh điều kiện rẽ nhánh lồng nhau (Nested If).", "Cài đặt thuật toán giải và biện luận phương trình bậc nhất ax + b = 0."],
        "Xử lý những bài toán quyết định đa tầng phức tạp trong cuộc sống thực tế!",
        "Cấu trúc if-elif-else giúp phân loại nhiều trường hợp liên tiếp. Ví dụ xếp loại học lực: Nếu Điểm >= 8.0 thì 'Giỏi', Ngược lại nếu Điểm >= 6.5 thì 'Khá', Ngược lại nếu Điểm >= 5.0 thì 'Trung bình', Còn lại là 'Chưa đạt'.",
        ["Thụt đầu dòng (Indentation) xác định khối mã lệnh trực thuộc nhánh điều kiện.", "Cẩn thận bẫy logic khi các điều kiện kiểm tra bị chồng chéo thứ tự."],
        {},
        [{"question": "Trong bài toán xét học lực, nếu học sinh có Điểm = 7.5 và đoạn mã kiểm tra theo thứ tự: (1) Nếu Điểm >= 8.0 -> Giỏi; (2) Ngược lại nếu Điểm >= 6.5 -> Khá; Kết quả nhận được là gì?", "options": ["Khá", "Giỏi", "Trung bình"], "answer": 0, "explanation": "7.5 không >= 8.0 nhưng thỏa mãn >= 6.5 nên nhận kết quả 'Khá'."}],
        "Em đã làm chủ cấu trúc điều kiện rẽ nhánh phức hợp rất logic!"
    ))

    nodes.append(make_lesson(
        "G8-09", "w2", 8, "Cấu trúc Vòng lặp For và While", "Chủ đề 5: Giải quyết vấn đề",
        "Bài 13: Câu lệnh lặp", "Bài 11: Vòng lặp for và while", "Bài 11: Vòng lặp với điều kiện",
        "block-maze", ["G8-08"], 8,
        ["Phân biệt vòng lặp lặp với số lần biết trước (For) và lặp với điều kiện chưa biết trước (While).", "Biết kỹ thuật tính tổng dồn S = S + i và đếm số thỏa mãn điều kiện."],
        "Sức mạnh vô song của máy tính: Tính toán tổng của 1 triệu số nguyên chỉ trong 1 phần ngàn giây!",
        "Vòng lặp For: dùng khi biết trước số lần lặp (ví dụ duyệt qua 30 ngày trong tháng). Vòng lặp While: lặp liên tục chừng nào điều kiện vẫn còn đúng (ví dụ: lặp nhận mật khẩu cho đến khi người dùng nhập đúng). Chú ý cập nhật biến đếm trong While để tránh lỗi lặp vô tận (Infinite Loop).",
        ["Lệnh break: thoát ra khỏi vòng lặp ngay lập tức.", "Lệnh continue: bỏ qua các lệnh còn lại của vòng hiện tại để nhảy sang vòng lặp tiếp theo."],
        {"grid_size": 4, "start": {"x": 0, "y": 0, "dir": "E"}, "target": {"x": 3, "y": 3}, "walls": [{"x": 1, "y": 0}, {"x": 2, "y": 2}], "allowed_blocks": ["forward", "turn_right", "turn_left"], "max_blocks": 8},
        [{"question": "Nếu trong thân vòng lặp While mà ta quên không viết lệnh tăng biến đếm, điều gì sẽ xảy ra?", "options": ["Vòng lặp chạy vô tận không bao giờ dừng lại (Treo chương trình)", "Chương trình chạy nhanh gấp đôi", "Máy tính tự động sửa lỗi"], "answer": 0, "explanation": "Điều kiện lặp luôn đúng sẽ gây ra lỗi lặp vô hạn (Infinite Loop)."}],
        "Vòng lặp thuật toán của em vận hành cực kỳ tối ưu và chính xác!"
    ))

    nodes.append(make_lesson(
        "G8-10", "w2", 8, "Cấu trúc Dữ liệu Danh sách (List / Mảng)", "Chủ đề 5: Giải quyết vấn đề",
        "Bài 14: Mảng và danh sách", "Bài 12: Cấu trúc danh sách trong lập trình", "Bài 12: Xử lý dữ liệu danh sách",
        "bug-hunt", ["G8-09"], 8,
        ["Hiểu cấu trúc mảng danh sách lưu trữ dãy các phần tử cùng hoặc khác kiểu.", "Thao tác truy cập phần tử qua chỉ số Index (bắt đầu từ 0) và duyệt danh sách."],
        "Thay vì khai báo 50 biến riêng lẻ a1, a2... a50, hãy gom tất cả vào một mảng danh sách duy nhất!",
        "Danh sách (List) là tập hợp có thứ tự của các phần tử. Phần tử đầu tiên có chỉ số Index là 0, phần tử thứ hai có chỉ số là 1. Độ dài danh sách len(L). Các thao tác kinh điển: Thêm phần tử vào cuối (append), Xóa phần tử (remove/pop), Tìm giá trị lớn nhất trong mảng.",
        ["Duyệt mảng bằng vòng lặp For: for item in List.", "Lỗi kinh điển: IndexError (truy cập chỉ số vượt quá độ dài danh sách)."],
        {},
        [{"question": "Cho danh sách A = [10, 20, 30, 40]. Phần tử A[0] có giá trị bằng bao nhiêu?", "options": ["10", "20", "40"], "answer": 0, "explanation": "Trong lập trình hiện đại, chỉ số mảng danh sách luôn bắt đầu từ số 0."}],
        "Em đã làm chủ cấu trúc mảng danh sách - công cụ lưu trữ dữ liệu vạn năng!"
    ))

    nodes.append(make_lesson(
        "G8-11", "w2", 8, "Kỹ thuật Kiểm thử & Gỡ lỗi (Debugging)", "Chủ đề 5: Giải quyết vấn đề",
        "Bài 15: Dự án lập trình & kiểm thử", "Bài 13, 14: Game điểm & Kiểm thử gỡ lỗi", "Bài 13, 14: Game & Gỡ lỗi logic",
        "bug-hunt", ["G8-10"], 8,
        ["Phân biệt 3 loại lỗi lập trình: Lỗi cú pháp (Syntax Error), Lỗi thời gian chạy (Runtime Error) và Lỗi ngữ nghĩa logic (Logic Error).", "Kỹ thuật gỡ lỗi bằng cách in giá trị trung gian (Print Debugging)."],
        "Lập trình viên giỏi không phải là người không bao giờ mắc lỗi, mà là người có khả năng truy tìm và sửa lỗi nhanh nhất!",
        "Syntax Error: viết sai chính tả từ khóa hoặc thiếu dấu hai chấm (trình biên dịch báo lỗi ngay). Runtime Error: chia cho số 0, gọi biến chưa khai báo (chương trình bị văng khi đang chạy). Logic Error: chương trình chạy êm xuôi nhưng cho ra kết quả sai (loại lỗi khó tìm nhất, cần kiểm thử với nhiều Test Cases).",
        ["Viết câu lệnh in biến print() để theo dõi dòng chảy dữ liệu.", "Chia nhỏ hàm để kiểm thử độc lập từng đơn vị chức năng."],
        {},
        [{"question": "Khi chương trình chạy không báo lỗi cú pháp nào nhưng kết quả tính toán chu vi hình chữ nhật lại ra sai, đó là loại lỗi gì?", "options": ["Lỗi ngữ nghĩa / Lỗi logic (Logic Error)", "Lỗi cú pháp (Syntax Error)", "Lỗi phần cứng"], "answer": 0, "explanation": "Chương trình chạy được nhưng sai kết quả tính toán chính là lỗi logic."}],
        "Kỹ năng săn lỗi và gỡ mã độc của em đạt đến trình độ thượng thừa!"
    ))

    nodes.append(make_lesson(
        "G8-12", "w2", 8, "Khám phá Thị trường Nghề nghiệp CNTT", "Chủ đề 6: Hướng nghiệp",
        "Bài 16: Nghề nghiệp lĩnh vực CNTT", "Bài 15, 16: Dự án mô phỏng & Nghề nghiệp", "Bài 15, 16: Dự án sáng tạo & Nghề nghiệp",
        "match-memory", ["G8-03"], 7,
        ["Tìm hiểu các vị trí việc làm phổ biến: Kỹ sư phần mềm, Chuyên viên an ninh mạng, Quản trị CSDL, Kỹ sư AI.", "Nhận thức các kỹ năng mềm quan trọng: Làm việc nhóm, Giao tiếp, Tiếng Anh chuyên ngành."],
        "Thế giới công nghệ thông tin mở ra hàng ngàn cánh cửa tương lai xán lạn cho thế hệ trẻ!",
        "Ngành CNTT không chỉ có ngồi gõ code mà rất đa dạng: Lập trình viên Front-end/Back-end, Chuyên viên kiểm thử chất lượng phần mềm (QA/QC), Chuyên viên bảo mật an ninh mạng (Security Analyst), Nhà khoa học dữ liệu (Data Scientist) và Kỹ sư Trí tuệ nhân tạo (AI Engineer).",
        ["Tự học liên tục là chìa khóa sống còn trong kỷ nguyên số biến đổi nhanh chóng.", "Kỹ năng tư duy logic và giải quyết vấn đề là nền tảng cốt lõi."],
        {"cards": [{"id":"1","name":"Kỹ sư Phần mềm (Software Engineer)","match":"Thiết kế, xây dựng và bảo trì các ứng dụng hệ thống"},{"id":"2","name":"Chuyên viên An ninh mạng (Cyber Security)","match":"Bảo vệ hệ thống mạng chống lại các cuộc tấn công hacker"},{"id":"3","name":"Nhà Khoa học Dữ liệu (Data Scientist)","match":"Phân tích dữ liệu lớn để tìm ra quy luật kinh doanh thông minh"},{"id":"4","name":"Kỹ sư Trí tuệ Nhân tạo (AI Engineer)","match":"Huấn luyện các mô hình học máy tự động hóa thông minh"}]},
        [{"question": "Vị trí nào trong ngành CNTT chịu trách nhiệm chính về việc bảo vệ hệ thống máy tính khỏi sự tấn công của tin tặc?", "options": ["Chuyên viên an ninh mạng (Cyber Security)", "Thiết kế đồ họa UI/UX", "Nhân viên bán hàng phần mềm"], "answer": 0, "explanation": "Chuyên viên an ninh mạng là người canh gác bảo vệ hệ thống dữ liệu."}],
        "Em đã có bức tranh toàn cảnh về tương lai nghề nghiệp công nghệ thông tin!"
    ))

    nodes.append(make_lesson(
        "G8-13", "w2", 8, "Đấu trường Trùm Lớp 8: Thợ săn Bug Thuật toán", "Tổng kết GDPT 2018 Lớp 8",
        "Bài 16: Tổng kết & Đánh giá năng lực 8", "Bài 16: Khám phá ngành nghề & Tổng kết", "Bài 16: Dự án sáng tạo & Đánh giá năng lực",
        "boss-quiz", ["G8-04", "G8-07", "G8-08", "G8-09", "G8-10"], 12,
        ["Tổng kết toàn diện chuẩn năng lực Tin học Lớp 8 của cả 3 bộ sách.", "Sẵn sàng nhận huy hiệu Bậc Thầy Săn Bug Thuật Toán EasyTin."],
        "Chúa tể Lỗi Mã 'Zero-Day Bug' đang đe dọa làm sập toàn bộ các máy chủ dữ liệu! Hãy vận dụng sức mạnh thuật toán để tiêu diệt nó!",
        "Đấu trường tổng hợp: Lịch sử máy tính, Bảng tính nâng cao, Đồ họa layer, Cấu trúc if/else lồng nhau, Vòng lặp For/While và Mảng danh sách.",
        ["Cấu trúc dữ liệu mảng danh sách List và Index.", "Vòng lặp For, While, xử lý lỗi logic và định luật Moore."],
        {"boss_name": "Zero-Day Bug Chúa Tể", "boss_max_hp": 100, "player_max_hp": 100, "damage_per_hit": 25, "questions_pool": 4},
        [
            {"question": "Định luật Moore dự đoán điều gì về sự phát triển của công nghệ vi mạch?", "options": ["Số lượng bóng bán dẫn trên chip tăng gấp đôi sau mỗi khoảng 2 năm", "Tốc độ máy tính sẽ chậm dần theo thời gian", "Giá máy tính sẽ ngày càng đắt đỏ"], "answer": 0, "explanation": "Định luật Moore phản ánh sự phát triển bùng nổ theo hàm mũ của chip vi xử lý."},
            {"question": "Trong Python, kết quả của biểu thức '3 * 2 ** 2' là bao nhiêu?", "options": ["12 (lũy thừa tính trước: 2^2=4, rồi nhân 3*4=12)", "36", "24"], "answer": 0, "explanation": "Toán tử lũy thừa (**) có độ ưu tiên cao hơn phép nhân (*)."},
            {"question": "Vòng lặp nào sau đây phù hợp nhất khi ta CHƯA BIẾT trước số lần lặp mà chỉ biết điều kiện dừng?", "options": ["Vòng lặp While", "Vòng lặp For", "Vòng lặp Repeat 10"], "answer": 0, "explanation": "While lặp dựa trên điều kiện kiểm tra, rất phù hợp khi số lần chưa xác định trước."},
            {"question": "Để lọc dữ liệu tự động trong bảng tính Excel, ta sử dụng công cụ nào trên thanh Data?", "options": ["Bộ lọc Filter", "Công cụ Zoom", "Công cụ Save As"], "answer": 0, "explanation": "Filter là công cụ chuẩn để trích lọc dữ liệu theo điều kiện."}
        ],
        "CHIẾN THẮNG HUY HOÀNG! Em đã tiêu diệt Zero-Day Bug và xuất sắc hoàn thành toàn bộ chương trình Tin học Lớp 8 của cả 3 bộ sách KNTT, Cánh Diều, CTST!"
    ))

    # =========================================================================
    # LỚP 9 (11 NÚT)
    # =========================================================================
    nodes.append(make_lesson(
        "G9-01", "w2", 9, "Kiến trúc Máy tính Von Neumann, CPU & Bus", "Chủ đề 1: Máy tính và cộng đồng",
        "Bài 1: Bộ xử lý, bộ nhớ và thiết bị vào - ra", "Bài 1: Cấu trúc phần cứng máy tính", "Bài 1: Nguyên lý hoạt động máy tính",
        "sort-drag", ["G8-01"], 7,
        ["Mô tả kiến trúc máy tính kinh điển Von Neumann.", "Hiểu chu trình lệnh của CPU: Nạp lệnh (Fetch) -> Giải mã (Decode) -> Thực thi (Execute)."],
        "Nguyên lý kiến trúc thiên tài ra đời từ năm 1945 của nhà bác học John von Neumann vẫn đang vận hành 100% máy tính hiện đại ngày nay!",
        "Kiến trúc Von Neumann gồm: CPU (gồm khối điều khiển CU và khối tính toán ALU), Bộ nhớ chính (RAM/ROM), Bộ nhớ phụ (SSD/HDD), Các thiết bị Vào/Ra và Hệ thống Bus truyền dữ liệu. Điểm mấu chốt: chương trình và dữ liệu được lưu trữ chung trong bộ nhớ dưới dạng nhị phân.",
        ["Tốc độ xung nhịp CPU đo bằng Gigahertz (GHz) thể hiện số tỷ chu kỳ thực hiện trong 1 giây.", "Thanh ghi (Registers) là bộ nhớ siêu tốc độ nằm ngay bên trong nhân CPU."],
        {"groups": [{"id": "g1", "name": "Khối Chức năng trong CPU"}, {"id": "g2", "name": "Hệ thống Bộ nhớ & Truyền dẫn"}], "items": [{"id":"1","name":"Khối số học logic ALU (Thực hiện phép tính)","group":"g1","icon":"🔢"},{"id":"2","name":"Khối điều khiển CU (Chỉ đạo nạp lệnh)","group":"g1","icon":"🎛️"},{"id":"3","name":"Bộ nhớ đệm siêu tốc Cache CPU L1/L2/L3","group":"g2","icon":"⚡"},{"id":"4","name":"Hệ thống đường truyền Bus truyền dẫn dữ liệu","group":"g2","icon":"🚌"}]},
        [{"question": "Trong kiến trúc máy tính Von Neumann, khối chức năng nào chịu trách nhiệm thực hiện các phép tính số học (+, -, *, /) và phép so sánh logic?", "options": ["Khối số học logic ALU", "Khối điều khiển CU", "Màn hình"], "answer": 0, "explanation": "ALU (Arithmetic Logic Unit) là khối chuyên trách tính toán số học và logic của CPU."}],
        "Em đã nắm vững nguyên lý hoạt động sâu sắc nhất của phần cứng máy tính!"
    ))

    nodes.append(make_lesson(
        "G9-02", "w2", 9, "Chất lượng Thông tin & Ra quyết định", "Chủ đề 1: Máy tính và cộng đồng",
        "Bài 2, 3: Chất lượng thông tin & Đánh giá", "Bài 2: Thu thập & Thẩm định thông tin", "Bài 2: Giá trị thông tin & Ra quyết định",
        "branch-story", ["G8-02"], 7,
        ["Đánh giá 5 thuộc tính chất lượng thông tin: Tính chính xác, Kịp thời, Đầy đủ, Thích hợp, Bảo mật.", "Hiểu mối quan hệ: Dữ liệu chất lượng -> Quyết định chính xác."],
        "Một quyết định tài chính hay y tế sai lầm dựa trên thông tin rác có thể trả giá bằng hàng triệu đô la hoặc tính mạng con người!",
        "Thông tin chất lượng cao phải đảm bảo: (1) Tính chính xác (không có sai số); (2) Tính kịp thời (đúng lúc cần, tin tức cũ không còn giá trị); (3) Tính đầy đủ (không bị cắt xén phiến diện); (4) Tính thích hợp (phù hợp với bài toán); (5) Tính bảo mật (không bị lộ lọt cho đối thủ).",
        ["Dữ liệu lớn (Big Data) đòi hỏi quy trình làm sạch và lọc dữ liệu rác nghiêm ngặt.", "Không đưa ra quyết định khi thông tin còn mơ hồ hoặc mâu thuẫn."],
        {"scenarios": [{"id": "s1", "prompt": "Một tập đoàn vận tải nhận được dự báo bão giật cấp 12 trên vùng biển dự kiến tàu xuất bến trong 3 giờ tới.", "choices": [{"text": "Thông tin mang tính kịp thời và chính xác cao -> Quyết định hoãn chuyến tàu ngay lập tức để bảo đảm an toàn sinh mạng hành khách.", "is_correct": True, "feedback": "Quyết định chuẩn mực! Thông tin chất lượng đã cứu sống hàng trăm người."}, {"text": "Bỏ qua dự báo, cứ cho tàu xuất bến theo đúng lịch trình cũ.", "is_correct": False, "feedback": "Hậu quả thảm khốc! Coi thường thông tin chất lượng có thể gây đắm tàu!"}]}]},
        [{"question": "Thuộc tính nào của thông tin thể hiện rằng thông tin phản ánh đúng hiện thực khách quan, không bị sai lệch?", "options": ["Tính chính xác", "Tính kịp thời", "Tính thẩm mỹ"], "answer": 0, "explanation": "Tính chính xác là thuộc tính cốt lõi bảo đảm thông tin phản ánh đúng sự thật."}],
        "Em đã thấu hiểu giá trị chiến lược của chất lượng thông tin trong việc ra quyết định!"
    ))

    nodes.append(make_lesson(
        "G9-03", "w2", 9, "Pháp luật Số & Bảo vệ Dữ liệu Cá nhân", "Chủ đề 3: Đạo đức, pháp luật",
        "Bài 4: Thực hành đạo đức và pháp luật", "Bài 3: Công nghệ số & Luật an ninh mạng", "Bài 3: Pháp luật trong thời đại số",
        "branch-story", ["G8-03"], 7,
        ["Hiểu Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân tại Việt Nam.", "Quyền của chủ thể dữ liệu: Quyền được biết, Quyền đồng ý, Quyền yêu cầu xóa dữ liệu."],
        "Dữ liệu cá nhân là tài sản số vô giá, được pháp luật bảo vệ nghiêm ngặt chống lại việc mua bán trái phép!",
        "Dữ liệu cá nhân gồm dữ liệu cơ bản (họ tên, ngày sinh, số điện thoại, căn cước) và dữ liệu nhạy cảm (dữ liệu y tế sinh trắc học, tài khoản ngân hàng). Doanh nghiệp và cá nhân thu thập dữ liệu bắt buộc phải có sự đồng ý của chủ thể và có biện pháp mã hóa bảo vệ.",
        ["Nghiêm cấm hành vi mua bán danh sách số điện thoại khách hàng.", "Mọi người dân có quyền yêu cầu xóa thông tin cá nhân của mình khỏi các nền tảng dịch vụ."],
        {"scenarios": [{"id": "s1", "prompt": "Một ứng dụng trò chơi giải đố miễn phí yêu cầu cấp quyền truy cập toàn bộ Danh bạ điện thoại, Vị trí GPS và Tin nhắn SMS riêng tư.", "choices": [{"text": "Từ chối cấp quyền và gỡ cài đặt ứng dụng vì đòi hỏi quyền hạn vượt quá chức năng của game.", "is_correct": True, "feedback": "Rất cảnh giác! Đây là ứng dụng có hành vi thu thập dữ liệu bất hợp pháp."}, {"text": "Bấm đồng ý tất cả mọi quyền để được chơi game nhanh.", "is_correct": False, "feedback": "Nguy hiểm! Toàn bộ số điện thoại người thân và tin nhắn của em sẽ bị đánh cắp!"}]}]},
        [{"question": "Theo quy định pháp luật về bảo vệ dữ liệu cá nhân, hành vi nào sau đây là BẤT HỢP PHÁP?", "options": ["Mua bán danh sách thông tin số điện thoại của người dân khi chưa được đồng ý", "Yêu cầu xóa thông tin cá nhân của mình", "Đặt mật khẩu bảo vệ tài khoản"], "answer": 0, "explanation": "Mua bán dữ liệu cá nhân là hành vi vi phạm pháp luật hình sự."}],
        "Em đã trang bị kiến thức pháp lý vững vàng về bảo vệ quyền riêng tư số!"
    ))

    nodes.append(make_lesson(
        "G9-04", "w2", 9, "Phần mềm Mô phỏng Khoa học & Bài trình chiếu", "Chủ đề 4: Ứng dụng tin học",
        "Bài 5, 6: Phần mềm mô phỏng & Trình chiếu đa phương tiện", "Bài 4: Phần mềm mô phỏng học tập", "Bài 4: Mô phỏng khoa học",
        "match-memory", ["G8-05"], 7,
        ["Khám phá ứng dụng của phần mềm mô phỏng (Simulation): PhET, GeoGebra, Stellarium.", "Thiết kế bài trình chiếu đa phương tiện kết hợp mô phỏng thí nghiệm."],
        "Mở phòng thí nghiệm ảo không gian vũ trụ ngay trên màn hình máy tính!",
        "Phần mềm mô phỏng tái tạo lại các hiện tượng tự nhiên hoặc thí nghiệm nguy hiểm/tốn kém trong thực tế: phản ứng hạt nhân, quỹ đạo chuyển động của các hành tinh, sự lan truyền sóng âm. Giúp học sinh học tập tương tác trực quan và an toàn tuyệt đối.",
        ["Thay đổi các tham số đầu vào để quan sát sự thay đổi kết quả mô phỏng theo thời gian thực.", "Nhúng hình ảnh động mô phỏng vào bài báo cáo khoa học."],
        {"cards": [{"id":"1","name":"Phần mềm PhET","match":"Mô phỏng các thí nghiệm Vật lý, Hóa học và Sinh học tương tác"},{"id":"2","name":"Phần mềm GeoGebra","match":"Mô phỏng hình học không gian 3D, đại số và đồ thị hàm số"},{"id":"3","name":"Phần mềm Stellarium","match":"Bản đồ sao mô phỏng bầu trời đêm thiên văn học 3D"},{"id":"4","name":"Thí nghiệm ảo (Virtual Lab)","match":"Môi trường thực hành thí nghiệm khoa học không nguy hiểm cháy nổ"}]},
        [{"question": "Lợi ích lớn nhất của việc sử dụng phần mềm mô phỏng trong học tập khoa học là gì?", "options": ["Quan sát trực quan các thí nghiệm nguy hiểm, tốn kém hoặc trừu tượng một cách an toàn", "Thay thế hoàn toàn người giáo viên", "Làm tốn nhiều dung lượng bộ nhớ máy tính"], "answer": 0, "explanation": "Mô phỏng giúp thực hành an toàn các thí nghiệm độc hại, phóng xạ hoặc quá lớn như vũ trụ."}],
        "Em đã khai thác xuất sắc các công nghệ mô phỏng khoa học đỉnh cao!"
    ))

    nodes.append(make_lesson(
        "G9-05", "w2", 9, "Biên tập Video Ngắn & Xuất bản Truyền thông Số", "Chủ đề 4: Ứng dụng tin học",
        "Bài 7, 8: Biên tập video ngắn & Dự án đa phương tiện", "Bài 5, 6: Thiết kế dựng video & Dự án học đường", "Bài 5, 6: Xử lý video & Xuất bản số",
        "sort-drag", ["G9-04"], 7,
        ["Nắm vững quy trình làm phim: Kịch bản phân cảnh -> Quay tư liệu -> Cắt dựng -> Hậu kỳ âm thanh -> Xuất file.", "Sử dụng các công cụ cắt ghép (Split), hiệu ứng chuyển cảnh (Transitions), phụ đề (Subtitles)."],
        "Trở thành đạo diễn kiêm nhà sản xuất video chuyên nghiệp trong kỷ nguyên TikTok và YouTube!",
        "Quy trình dựng video: (1) Cắt bỏ đoạn lỗi thừa; (2) Chèn hiệu ứng chuyển cảnh mượt mà giữa các đoạn clip; (3) Thêm nhạc nền (Background music) và điều chỉnh âm lượng giọng đọc to rõ; (4) Thêm phụ đề tự động; (5) Xuất video chuẩn Full HD 1080p, định dạng nén MP4 (H.264).",
        ["Tỉ lệ khung hình: 16:9 (màn hình ngang máy tính/tivi), 9:16 (video ngắn dọc điện thoại).", "Tôn trọng bản quyền âm nhạc: sử dụng các bản nhạc miễn phí bản quyền (Royalty-free music)."],
        {"groups": [{"id": "g1", "name": "Thao tác Dựng hình Video"}, {"id": "g2", "name": "Hậu kỳ Âm thanh & Phụ đề"}], "items": [{"id":"1","name":"Cắt tỉa phân đoạn clip (Trim/Split video)","group":"g1","icon":"✂️"},{"id":"2","name":"Áp dụng hiệu ứng chuyển cảnh hòa tan (Cross Dissolve)","group":"g1","icon":"🎬"},{"id":"3","name":"Giảm âm lượng nhạc nền khi có tiếng người nói (Ducking)","group":"g2","icon":"📉"},{"id":"4","name":"Tự động tạo phụ đề chạy chữ (Auto Captions)","group":"g2","icon":"📝"}]},
        [{"question": "Khi xuất bản video ngắn dành cho điện thoại di động (Reels, TikTok, Shorts), tỉ lệ khung hình chuẩn là bao nhiêu?", "options": ["9:16 (Dọc)", "16:9 (Ngang)", "4:3"], "answer": 0, "explanation": "Tỉ lệ 9:16 tối ưu cho màn hình điện thoại cầm dọc của người xem."}],
        "Sản phẩm video truyền thông của em đạt chất lượng nghệ thuật rất chuyên nghiệp!"
    ))

    nodes.append(make_lesson(
        "G9-06", "w2", 9, "Thuật toán Bài toán Số học & Lập trình Tối ưu", "Chủ đề 5: Giải quyết vấn đề",
        "Bài 9, 10: Khái niệm bài toán & Thuật toán", "Bài 7, 8: Phân tích bài toán & Thuật toán", "Bài 7, 8: Xây dựng thuật toán số học",
        "logic-puzzle", ["G8-10"], 8,
        ["Cài đặt thuật toán kiểm tra số nguyên tố tối ưu duyệt đến căn bậc hai của N.", "Thuật toán tìm ước chung lớn nhất (UCLN) bằng phép trừ liên tiếp hoặc phép chia dư Euclid."],
        "Tối ưu thuật toán giúp biến một chương trình chạy mất 1 tiếng đồng hồ xuống còn chạy trong 1 phần trăm giây!",
        "Kiểm tra số nguyên tố ngây thơ: duyệt từ 2 đến N - 1 (rất chậm khi N lớn). Thuật toán tối ưu: chỉ cần duyệt từ 2 đến căn bậc hai của N (sqrt(N)), nếu không chia hết cho số nào thì kết luận luôn là số nguyên tố. Thuật toán Euclid tìm UCLN(A, B): liên tục thay (A, B) bằng (B, A % B) cho đến khi B = 0, khi đó UCLN là A.",
        ["Toán tử toán học trong thư viện math: math.isqrt(), math.gcd().", "Tối ưu số phép tính là bí quyết thi học sinh giỏi Tin học."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [2, 6, 11]},
        [{"question": "Để kiểm tra số nguyên dương N có phải là số nguyên tố hay không, cách duyệt vòng lặp tối ưu nhất là duyệt đến đâu?", "options": ["Duyệt đến căn bậc hai của N (căn(N))", "Duyệt đến N - 1", "Duyệt đến 2 * N"], "answer": 0, "explanation": "Nếu N có ước lớn hơn căn(N) thì chắc chắn phải có ước tương ứng nhỏ hơn căn(N)."}],
        "Tư duy tối ưu hóa thuật toán số học của em đạt trình độ rất sắc bén!"
    ))

    nodes.append(make_lesson(
        "G9-07", "w2", 9, "Bẫy lỗi, Xử lý Ngoại lệ & Thiết kế Giao diện", "Chủ đề 5: Giải quyết vấn đề",
        "Bài 11, 12: Bẫy lỗi & Lập trình ứng dụng", "Bài 9, 10: Bắt lỗi & Giao diện tương tác", "Bài 9, 10: Kiểm thử & Phần mềm giải trí",
        "bug-hunt", ["G9-06"], 8,
        ["Sử dụng khối bắt lỗi ngoại lệ try... except... để chương trình không bị sập bất ngờ.", "Thiết kế giao diện tương tác người dùng thân thiện, hướng dẫn nhập liệu đúng chuẩn."],
        "Một phần mềm chuyên nghiệp không bao giờ được phép văng màn hình khi người dùng lỡ bấm nhầm phím!",
        "Kỹ thuật bẫy lỗi (Exception Handling): Khối `try` chứa đoạn mã có nguy cơ phát sinh lỗi (như người dùng nhập chữ vào ô đòi hỏi số); Khối `except ValueError` bắt lỗi và hiển thị thông báo hướng dẫn người dùng nhập lại mà không làm sập toàn bộ ứng dụng.",
        ["Thông báo lỗi phải rõ ràng, mang tính xây dựng, chỉ dẫn cách khắc phục.", "Kiểm tra tính hợp lệ của dữ liệu đầu vào (Input Validation) trước khi đem đi tính toán."],
        {},
        [{"question": "Trong lập trình, cấu trúc lệnh nào dùng để bẫy lỗi và ngăn chặn chương trình không bị sập khi gặp ngoại lệ?", "options": ["Khối lệnh try ... except", "Khối lệnh for ... while", "Khối lệnh if ... else"], "answer": 0, "explanation": "try... except là cú pháp chuẩn của Python để xử lý các ngoại lệ thời gian chạy."}],
        "Ứng dụng phần mềm của em vận hành cực kỳ bền bỉ và thân thiện với người dùng!"
    ))

    nodes.append(make_lesson(
        "G9-08", "w2", 9, "Mạng Cục bộ LAN, Wi-Fi & Điện toán Đám mây", "Chủ đề 2: Mạng máy tính",
        "Bài 13, 14: Mạng LAN, Internet & Dịch vụ đám mây", "Bài 11, 12: Mạng LAN, Wi-Fi & Lưu trữ đám mây", "Bài 11, 12: Mạng LAN & Ứng dụng đám mây",
        "sort-drag", ["G6-03"], 7,
        ["Hiểu cấu trúc mạng LAN trường học: Địa chỉ IP tĩnh, máy chủ DHCP, bảo mật mạng Wi-Fi.", "Khai thác dịch vụ điện toán đám mây (Cloud Computing: Google Drive, OneDrive) để cộng tác thời gian thực."],
        "Không còn cảnh lo lắng quên USB ở nhà, toàn bộ tài nguyên học tập đồng bộ trên mây mọi lúc mọi nơi!",
        "Mạng cục bộ LAN kết nối các thiết bị trong phạm vi hẹp (phòng máy trường học). Điện toán đám mây cung cấp tài nguyên máy chủ, lưu trữ và phần mềm qua Internet theo yêu cầu. Cho phép nhiều học sinh cùng chỉnh sửa một tài liệu Google Docs theo thời gian thực.",
        ["Địa chỉ IPv4 cục bộ thường có dạng: 192.168.1.X.", "Chia sẻ quyền truy cập đám mây: Quyền Xem (View), Nhận xét (Comment), Chỉnh sửa (Editor)."],
        {"groups": [{"id": "g1", "name": "Thành phần Mạng Cục bộ (LAN)"}, {"id": "g2", "name": "Dịch vụ Điện toán Đám mây (Cloud)"}], "items": [{"id":"1","name":"Cáp xoắn đôi Cat6 & Đầu bấm RJ45","group":"g1","icon":"🔌"},{"id":"2","name":"Đặt địa chỉ IP tĩnh cho máy in trường học","group":"g1","icon":"🖨️"},{"id":"3","name":"Đồng bộ hóa thư mục tự động lên Google Drive","group":"g2","icon":"☁️"},{"id":"4","name":"Đồng chỉnh sửa bài thuyết trình trên Google Slides","group":"g2","icon":"👥"}]},
        [{"question": "Ưu điểm vượt trội nhất của việc lưu trữ tài liệu trên nền tảng đám mây (Cloud) so với ổ cứng máy tính cá nhân là gì?", "options": ["Truy cập được tài liệu từ bất kỳ thiết bị nào có Internet và không sợ mất dữ liệu khi hỏng máy", "Không cần kết nối mạng vẫn đồng bộ được", "Chứa được cả đồ vật hữu hình"], "answer": 0, "explanation": "Đám mây lưu trữ dữ liệu an toàn trên các trung tâm dữ liệu toàn cầu."}],
        "Em đã khai thác tối đa sức mạnh của mạng LAN và công nghệ điện toán đám mây!"
    ))

    nodes.append(make_lesson(
        "G9-09", "w2", 9, "An toàn Dữ liệu Số & Quy tắc Sao lưu 3-2-1", "Chủ đề 3: Đạo đức, pháp luật",
        "Bài 15: An toàn dữ liệu số", "Bài 13, 14: Mã hóa dữ liệu & Sao lưu", "Bài 13, 14: Bảo mật dữ liệu & Chống lừa đảo",
        "branch-story", ["G9-03"], 7,
        ["Nhận thức các nguy cơ: Mã độc tống tiền (Ransomware), hỏng hóc phần cứng ổ đĩa.", "Áp dụng chiến lược sao lưu dữ liệu vàng: Quy tắc 3-2-1."],
        "Trên thế giới chỉ có 2 loại người: Người đã từng mất dữ liệu và Người sắp mất dữ liệu!",
        "Quy tắc sao lưu 3-2-1 chuẩn mực quốc tế: (3) Giữ ít nhất 3 bản sao dữ liệu quan trọng; (2) Lưu trữ trên 2 loại thiết bị lưu trữ khác nhau (ví dụ: ổ cứng máy tính và ổ cứng di động); (1) Có ít nhất 1 bản sao được lưu ở nơi khác (ví dụ: lưu trên đám mây Cloud ngoài nhà).",
        ["Mã độc Ransomware mã hóa toàn bộ dữ liệu của nạn nhân đòi tiền chuộc.", "Cài đặt phần mềm phòng chống mã độc và thường xuyên cập nhật bản vá bảo mật OS."],
        {"scenarios": [{"id": "s1", "prompt": "Em vừa hoàn thành đề tài nghiên cứu khoa học lớn sau 3 tháng miệt mài gõ máy.", "choices": [{"text": "Áp dụng quy tắc sao lưu 3-2-1: Lưu bản gốc trên máy, sao chép sang USB và đồng bộ lên Google Drive.", "is_correct": True, "feedback": "Tuyệt đối an toàn! Dù máy tính có hỏng đột ngột thì dữ liệu vẫn còn nguyên vẹn."}, {"text": "Chỉ để duy nhất 1 bản trên màn hình Desktop máy tính bàn của trường.", "is_correct": False, "feedback": "Cực kỳ rủi ro! Nếu máy bị lỗi win hoặc người khác vô tình xóa là mất trắng 3 tháng công sức!"}]}]},
        [{"question": "Trong quy tắc sao lưu dữ liệu 3-2-1, con số '1' thể hiện nguyên tắc nào?", "options": ["Phải có ít nhất 1 bản sao lưu được cất giữ ở một vị trí địa lý khác (như đám mây Cloud)", "Chỉ sao lưu 1 lần trong đời", "Chỉ giữ lại 1 tệp duy nhất"], "answer": 0, "explanation": "Bản sao lưu ở vị trí khác phòng ngừa các rủi ro hỏa hoạn, mất cắp hoặc ngập lụt tại chỗ."}],
        "Em đã trang bị chiến lược phòng thủ an toàn dữ liệu số đạt chuẩn quốc tế!"
    ))

    nodes.append(make_lesson(
        "G9-10", "w2", 9, "Hướng nghiệp: Ngành nghề Tin học & Cơ hội", "Chủ đề 6: Hướng nghiệp",
        "Bài 16: Hướng nghiệp: Ngành nghề Tin học", "Bài 16: Lựa chọn hướng học tập & Nghề nghiệp", "Bài 16: Thị trường lao động công nghệ số",
        "match-memory", ["G8-12"], 7,
        ["Phân biệt 2 định hướng Tin học cấp THPT: Khoa học máy tính (CS) và Tin học ứng dụng (ICT).", "Định hình sở thích, năng khiếu để chọn tổ hợp môn học bước vào lớp 10."],
        "Ngã rẽ quan trọng bước vào bậc Trung học phổ thông: Em chọn trở thành Nhà sáng tạo công nghệ hay Bậc thầy ứng dụng số?",
        "Định hướng Khoa học máy tính (CS): Đi sâu vào thuật toán, cấu trúc dữ liệu, kiến trúc phần cứng, lập trình hệ thống, phát triển AI. Định hướng Tin học ứng dụng (ICT): Tập trung vào khai thác phần mềm ứng dụng, thiết kế đồ họa, truyền thông đa phương tiện, phát triển web và ứng dụng văn phòng nâng cao.",
        ["CS dành cho học sinh đam mê toán học, thuật toán, tư duy logic trừu tượng.", "ICT dành cho học sinh yêu thích sáng tạo nội dung, thiết kế, truyền thông số."],
        {"cards": [{"id":"1","name":"Định hướng CS (Khoa học máy tính)","match":"Nghiên cứu thuật toán, trí tuệ nhân tạo, lập trình hệ thống"},{"id":"2","name":"Định hướng ICT (Tin học ứng dụng)","match":"Thiết kế đồ họa, làm web, truyền thông số, quản trị văn phòng"},{"id":"3","name":"Tổ hợp môn xét tuyển ĐH khối A00/A01","match":"Toán - Lý - Hóa / Toán - Lý - Tiếng Anh rất hợp với CS"},{"id":"4","name":"Thị trường việc làm toàn cầu","match":"Nhu cầu kỹ sư CNTT chất lượng cao liên tục tăng trưởng mạnh mẽ"}]},
        [{"question": "Học sinh yêu thích tư duy toán học, thuật toán, muốn trở thành chuyên gia lập trình Trí tuệ nhân tạo (AI) nên chọn định hướng nào ở cấp THPT?", "options": ["Khoa học máy tính (Computer Science - CS)", "Tin học ứng dụng (ICT)", "Chỉ học đánh máy văn bản"], "answer": 0, "explanation": "Khoa học máy tính (CS) là nền tảng cốt lõi của lập trình và Trí tuệ nhân tạo."}],
        "Em đã sẵn sàng lựa chọn con đường tương lai phù hợp nhất với đam mê của mình!"
    ))

    nodes.append(make_lesson(
        "G9-11", "w2", 9, "Đấu trường Trùm Lớp 9: Tốt nghiệp Trung học Cơ sở", "Tổng kết GDPT 2018 THCS",
        "Bài 16: Tổng kết & Đánh giá năng lực 9", "Bài 16: Dự án hỗ trợ cộng đồng & Tổng kết", "Bài 15, 16: Trường học thông minh & Đánh giá",
        "boss-quiz", ["G9-01", "G9-02", "G9-06", "G9-08", "G9-09"], 12,
        ["Tổng kết toàn diện 4 năm học Tin học THCS (Lớp 6, 7, 8, 9) của cả 3 bộ sách.", "Sẵn sàng vươn cánh bước vào thế giới THPT đỉnh cao."],
        "Trùm Cuối THCS 'Malware Phantom' đang muốn phá hủy cánh cổng chuyển tiếp lên cấp 3! Hãy dùng toàn bộ nội lực 4 năm THCS để tiêu diệt nó!",
        "Đấu trường đỉnh cao tổng hợp: Kiến trúc Von Neumann, Tiêu chí chất lượng thông tin, Thuật toán số học tối ưu, Mạng LAN & Đám mây, An toàn số 3-2-1.",
        ["Chu trình lệnh CPU (Fetch - Decode - Execute).", "Quy tắc sao lưu 3-2-1 và định hướng nghề nghiệp CS/ICT."],
        {"boss_name": "Malware Phantom Trùm THCS", "boss_max_hp": 100, "player_max_hp": 100, "damage_per_hit": 25, "questions_pool": 4},
        [
            {"question": "Kiến trúc máy tính kinh điển Von Neumann gồm các thành phần cơ bản nào?", "options": ["CPU, Bộ nhớ chính, Bộ nhớ phụ, Thiết bị Vào/Ra và Hệ thống Bus", "Chỉ gồm màn hình và bàn phím", "Chỉ gồm phần mềm hệ thống", "Chuột và loa"], "answer": 0, "explanation": "Von Neumann định nghĩa mô hình phần cứng gồm 5 khối thành phần cốt lõi."},
            {"question": "Chiến lược sao lưu dữ liệu chuẩn quốc tế theo quy tắc 3-2-1 đòi hỏi điều gì?", "options": ["3 bản sao, trên 2 loại thiết bị khác nhau, ít nhất 1 bản lưu ở vị trí khác (như đám mây)", "Sao lưu 3 lần trong 1 ngày", "Mỗi tuần sao lưu 1 lần", "Chỉ lưu vào 1 thẻ nhớ duy nhất"], "answer": 0, "explanation": "Quy tắc 3-2-1 bảo đảm dữ liệu sống sót qua mọi sự cố phần cứng hay thiên tai."},
            {"question": "Thuật toán Euclid tìm Ước chung lớn nhất (UCLN) của hai số A và B dựa trên phép toán nào?", "options": ["Phép chia lấy phần dư liên tiếp (A % B)", "Phép nhân lũy thừa", "Phép khai căn bậc hai", "Phép đếm số chữ số"], "answer": 0, "explanation": "Thuật toán Euclid liên tục lấy số dư cho đến khi số dư bằng 0."},
            {"question": "Hai định hướng phân hóa môn Tin học ở cấp Trung học phổ thông (THPT) theo chương trình GDPT 2018 là gì?", "options": ["Khoa học máy tính (CS) và Tin học ứng dụng (ICT)", "Tin học văn phòng và Tin học đồ họa", "Lập trình game và Sửa máy tính", "Tin học đại cương và Tin học nâng cao"], "answer": 0, "explanation": "GDPT 2018 chính thức chia thành 2 định hướng: Khoa học máy tính (CS) và Tin học ứng dụng (ICT)."}
        ],
        "VINH QUANG TRUNG HỌC CƠ SỞ! Chúc mừng em đã hoàn thành xuất sắc toàn bộ chặng đường Tin học THCS (Lớp 6, 7, 8, 9) của cả 3 bộ sách KNTT, Cánh Diều, CTST với danh hiệu Bậc Thầy Công Nghệ THCS!"
    ))

    return nodes

print("curriculum_data_g6_g9 loaded")
