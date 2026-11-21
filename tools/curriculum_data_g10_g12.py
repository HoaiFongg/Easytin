# -*- coding: utf-8 -*-
"""
Dữ liệu chương trình học EasyTin: Khối THPT (Lớp 10, 11, 12)
Phủ 100% tất cả các bài học và YCCĐ của cả 3 bộ sách: KNTT, Cánh Diều, CTST
theo 2 định hướng Khoa học máy tính (CS) và Tin học ứng dụng (ICT).
"""

def get_high_school_nodes():
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
    # LỚP 10 (15 NÚT - THẾ GIỚI 3)
    # =========================================================================
    nodes.append(make_lesson(
        "G10-01", "w3", 10, "Thông tin, Tri thức & Thiết bị Thông minh IoT", "Chủ đề 1: Máy tính và xã hội tri thức",
        "Bài 1, 2: Thông tin, xử lý & Thiết bị thông minh", "Bài 1, 2: Dữ liệu, thông tin & Thiết bị số", "Bài 1, 2: Xử lý thông tin số & Thiết bị thông minh",
        "branch-story", [], 8,
        ["Hiểu kim tự tháp DIKW: Dữ liệu (Data) -> Thông tin (Information) -> Tri thức (Knowledge) -> Trí tuệ (Wisdom).", "Vai trò của thiết bị thông minh và Internet vạn vật (IoT) trong cuộc cách mạng 4.0."],
        "Một chiếc máy đo huyết áp đeo tay tự động gọi cấp cứu khi phát hiện nhịp tim người già bất thường - đó là sức mạnh của kỷ nguyên IoT!",
        "Dữ liệu là các con số hay ký tự thô. Khi dữ liệu được xử lý trong một ngữ cảnh xác định thì trở thành thông tin. Khi thông tin được con người đúc kết và áp dụng để giải quyết bài toán thực tế thì trở thành tri thức. Thiết bị thông minh là thiết bị điện tử có bộ vi xử lý và khả năng kết nối mạng để tự động tương tác và điều khiển.",
        ["Internet vạn vật (IoT): mạng lưới kết nối các đồ vật vật lý qua cảm biến và Internet.", "Xã hội tri thức: nền kinh tế dựa trên việc sáng tạo, phân phối và sử dụng tri thức."],
        {"scenarios": [{"id": "s1", "prompt": "Một hệ thống nông nghiệp công nghệ cao sử dụng cảm biến độ ẩm đất để tự động bật máy tưới tiêu khi đất khô và gửi báo cáo về điện thoại người nông dân.", "choices": [{"text": "Đó là ứng dụng điển hình của thiết bị thông minh và mạng IoT phục vụ sản xuất.", "is_correct": True, "feedback": "Rất chuẩn xác! Cảm biến và tự động hóa giúp tăng năng suất và tiết kiệm nước."}, {"text": "Đó chỉ là công tắc điện thông thường.", "is_correct": False, "feedback": "Sai rồi! Hệ thống có cảm biến thông minh, bộ xử lý và kết nối mạng điều khiển."}]}]},
        [{"question": "Trong kim tự tháp DIKW, tầng nào là kết quả của việc con người đúc kết, liên kết các thông tin và áp dụng vào thực tiễn?", "options": ["Tri thức (Knowledge)", "Dữ liệu thô (Data)", "Tín hiệu điện"], "answer": 0, "explanation": "Tri thức là sự đúc kết thông tin có hệ thống phục vụ hành động của con người."}],
        "Em đã thấu suốt bản chất của thông tin, tri thức và làn sóng công nghệ IoT!"
    ))

    nodes.append(make_lesson(
        "G10-02", "w3", 10, "Kiến trúc Mạng Máy tính & Mô hình Client-Server", "Chủ đề 1: Máy tính và xã hội tri thức",
        "Bài 3, 4: Một số kiểu mạng & Thiết bị mạng", "Bài 3, 4: Mạng máy tính & Điện toán đám mây", "Bài 3, 4: Mô hình kết nối mạng & Thiết bị",
        "sort-drag", ["G10-01"], 8,
        ["Phân biệt mạng cục bộ (LAN), mạng diện rộng (WAN), mạng cá nhân (PAN).", "Phân tích mô hình Khách - Chủ (Client - Server) và mô hình Ngang hàng (Peer-to-Peer)."],
        "Khi em gõ google.com trên trình duyệt, có một cuộc trò chuyện thần tốc diễn ra giữa máy khách của em và máy chủ Google!",
        "Mô hình Client - Server: Máy khách (Client) gửi yêu cầu (Request), Máy chủ (Server) cấu hình mạnh xử lý và trả về phản hồi (Response). Mô hình Ngang hàng (P2P): các máy tính bình đẳng vừa đóng vai trò chia sẻ vừa tải dữ liệu (như mạng torrent, blockchain).",
        ["Mạng PAN: phạm vi vài mét (kết nối Bluetooth giữa điện thoại và tai nghe).", "Mạng WAN: kết nối các chi nhánh ngân hàng xuyên quốc gia."],
        {"groups": [{"id": "g1", "name": "Mô hình Khách - Chủ (Client - Server)"}, {"id": "g2", "name": "Mô hình Mạng Ngang hàng (P2P)"}], "items": [{"id":"1","name":"Trình duyệt Web tải trang báo điện tử từ Web Server","group":"g1","icon":"🌐"},{"id":"2","name":"Ứng dụng di động gửi truy vấn tới Database Server","group":"g1","icon":"🗄️"},{"id":"3","name":"Giao thức BitTorrent chia sẻ tệp phân tán","group":"g2","icon":"🔗"},{"id":"4","name":"Mạng chuỗi khối phi tập trung Blockchain","group":"g2","icon":"⛓️"}]},
        [{"question": "Trong mô hình Client - Server, máy tính nào đóng vai trò tiếp nhận yêu cầu và cung cấp dịch vụ dữ liệu cho các máy khác?", "options": ["Máy chủ (Server)", "Máy khách (Client)", "Máy in"], "answer": 0, "explanation": "Máy chủ (Server) là trung tâm lưu trữ và cung cấp tài nguyên dịch vụ cho mạng."}],
        "Em đã nắm vững kiến trúc mạng và mô hình truyền thông Client - Server!"
    ))

    nodes.append(make_lesson(
        "G10-03", "w3", 10, "Văn hóa Mạng Xã hội & An toàn Không gian Mạng", "Chủ đề 1: Máy tính và xã hội tri thức",
        "Bài 5, 6: Mạng xã hội & An toàn trên không gian mạng", "Bài 5, 6: Ứng xử nhân văn & Pháp luật an toàn", "Bài 5, 6: Trách nhiệm công dân & An toàn mạng",
        "branch-story", ["G10-02"], 8,
        ["Nhận diện các loại mã độc nguy hiểm: Virus, Worm (Sâu máy tính), Trojan Horse, Spyware.", "Kỹ thuật phòng chống lừa đảo trực tuyến (Phishing) và bảo vệ danh tính số."],
        "Con ngựa gỗ thành Troy thời cổ đại đang tái sinh dưới hình dạng các tệp trò chơi miễn phí trên mạng!",
        "Trojan Horse là phần mềm độc hại ngụy trang dưới vỏ bọc một ứng dụng hữu ích để lừa người dùng tải về. Sâu máy tính (Worm) có khả năng tự động nhân bản và lây lan qua lỗ hổng mạng mà không cần người dùng thao tác. Tấn công giả mạo (Phishing) dùng email hoặc web ngân hàng giả để đánh cắp mật khẩu và OTP.",
        ["Cài đặt tường lửa và phần mềm phòng thủ Endpoint Protection.", "Luôn kiểm tra thanh địa chỉ web xem có giao thức bảo mật HTTPS (ổ khóa xanh) hay không."],
        {"scenarios": [{"id": "s1", "prompt": "Em nhận được tin nhắn SMS xưng là Ngân hàng thông báo tài khoản bị tạm khóa, yêu cầu nhấp vào đường link 'ngan-hang-xyz-verify.com' để nhập mật khẩu và mã OTP.", "choices": [{"text": "Tuyệt đối không nhấp vào đường link lạ! Đây là tấn công giả mạo Phishing nhằm chiếm đoạt tài khoản.", "is_correct": True, "feedback": "Rất cảnh giác! Các ngân hàng không bao giờ gửi link lạ bắt khách hàng nhập mã OTP."}, {"text": "Nhấp vào đường link và nhập ngay mật khẩu tài khoản.", "is_correct": False, "feedback": "Mất sạch tiền trong tài khoản! Mã OTP một khi bị lộ sẽ giúp kẻ xấu chuyển tiền đi ngay!"}]}]},
        [{"question": "Loại mã độc nào sau đây có khả năng tự động lây lan qua hệ thống mạng từ máy này sang máy khác mà không cần sự can thiệp của người dùng?", "options": ["Sâu máy tính (Worm)", "Virus cổ điển", "File ảnh thông thường"], "answer": 0, "explanation": "Sâu máy tính (Worm) tự động khai thác lỗ hổng mạng để phát tán diện rộng."}],
        "Em đã dựng lên bức tường lửa phòng thủ thép bảo vệ mình trên không gian mạng!"
    ))

    nodes.append(make_lesson(
        "G10-04", "w3", 10, "Phần mềm Nguồn mở (FOSS) & Bản quyền Số", "Chủ đề 2: Đạo đức, pháp luật",
        "Bài 7, 8: Phần mềm nguồn mở & Bản quyền thông tin", "Bài 7: Phần mềm tự do nguồn mở", "Bài 7: Phần mềm nguồn mở & Giấy phép",
        "sort-drag", ["G10-01"], 8,
        ["Phân biệt phần mềm thương mại đóng mã (Proprietary) và phần mềm nguồn mở tự do (FOSS).", "Nắm vững 4 quyền tự do của giấy phép GNU GPL và Creative Commons."],
        "Hơn 90% các siêu máy tính nhanh nhất hành tinh và máy chủ Internet toàn cầu đang vận hành trên hệ điều hành nguồn mở Linux!",
        "Phần mềm nguồn mở (Free and Open Source Software): cho phép người dùng tự do xem mã nguồn, sửa đổi, cải tiến và phân phối lại. Các giấy phép nguồn mở nổi tiếng: GNU GPL (buộc dẫn xuất phải mở mã), MIT License, Apache 2.0. Bản quyền Creative Commons (CC) dành cho các tác phẩm tranh ảnh, bài viết, âm nhạc.",
        ["Ưu điểm của FOSS: minh bạch bảo mật, không bị phụ thuộc nhà cung cấp, chi phí bản quyền 0 đồng.", "Quyền sở hữu trí tuệ: người dùng mã nguồn mở vẫn phải ghi nhận tác giả gốc."],
        {"groups": [{"id": "g1", "name": "Phần mềm Nguồn mở (Open Source - FOSS)"}, {"id": "g2", "name": "Phần mềm Thương mại Đóng mã (Proprietary)"}], "items": [{"id":"1","name":"Hệ điều hành Linux Ubuntu & Nhân Linux","group":"g1","icon":"🐧"},{"id":"2","name":"Trình duyệt web Mozilla Firefox","group":"g1","icon":"🦊"},{"id":"3","name":"Hệ điều hành Microsoft Windows 11","group":"g2","icon":"🪟"},{"id":"4","name":"Bộ phần mềm văn phòng Microsoft Office","group":"g2","icon":"💼"}]},
        [{"question": "Đặc điểm mang tính nguyên tắc sống còn của phần mềm nguồn mở (Open Source) là gì?", "options": ["Người dùng được quyền tự do xem mã nguồn, sửa đổi và phân phối lại", "Mã nguồn bị khóa kín không ai được xem", "Bắt buộc phải trả phí hàng tháng"], "answer": 0, "explanation": "Công khai mã nguồn để cộng đồng cùng kiểm tra và phát triển là tinh thần của FOSS."}],
        "Em đã am hiểu sâu sắc về phong trào phần mềm tự do nguồn mở thế giới!"
    ))

    nodes.append(make_lesson(
        "G10-05", "w3", 10, "Thiết kế Đồ họa Vector với Inkscape", "Chủ đề 3: Ứng dụng tin học",
        "Bài 12, 13, 14, 15: Phần mềm thiết kế đồ họa Inkscape", "Bài 8, 9, 10, 11: Thiết kế đồ họa với Inkscape", "Bài 8, 9, 10, 11: Đồ họa vector Inkscape",
        "sort-drag", ["G8-05"], 8,
        ["Phân biệt đồ họa điểm ảnh (Raster/Bitmap: vỡ hạt khi phóng to) và đồ họa véc-tơ (Vector: sắc nét ở mọi độ phóng).", "Sử dụng các phép biến đổi hình học (Union, Difference, Intersection) và đường cong Bézier."],
        "Phóng to logo từ kích thước chiếc tem thư lên kích cỡ biển quảng cáo tòa nhà 50 tầng mà không hề bị vỡ hạt!",
        "Đồ họa Vector biểu diễn hình ảnh bằng các phương trình toán học (điểm, đường cong Bézier, màu lấp đầy). Định dạng file chuẩn: SVG. Các phép toán tổ hợp hình khối Boolean: Hợp nhất (Union), Hiệu hai hình (Difference - cắt xén), Giao nhau (Intersection).",
        ["Raster (.png, .jpg) thích hợp cho ảnh chụp thực tế.", "Vector (.svg, .ai) thích hợp cho thiết kế Logo, Icon, Typography."],
        {"groups": [{"id": "g1", "name": "Đặc trưng Đồ họa Vector (.svg)"}, {"id": "g2", "name": "Đặc trưng Đồ họa Điểm ảnh Raster (.jpg/.png)"}], "items": [{"id":"1","name":"Phóng to vô hạn không bao giờ bị vỡ hạt","group":"g1","icon":"📐"},{"id":"2","name":"Tạo hình bằng các phương trình toán học Bézier","group":"g1","icon":"✒️"},{"id":"3","name":"Cấu tạo từ lưới các ô vuông điểm ảnh (Pixels)","group":"g2","icon":"▦"},{"id":"4","name":"Thích hợp cho ảnh chụp thực tế bằng máy ảnh số","group":"g2","icon":"📷"}]},
        [{"question": "Khi phóng to một bức ảnh lên gấp 10 lần mà hình ảnh vẫn sắc nét hoàn hảo, không bị nhòe hay vỡ hạt, đó chắc chắn là loại đồ họa nào?", "options": ["Đồ họa véc-tơ (Vector Graphic)", "Đồ họa điểm ảnh (Bitmap)", "Đồ họa vẽ bằng bút chì"], "answer": 0, "explanation": "Đồ họa vector sử dụng công thức toán học nên giữ nguyên độ sắc nét ở mọi kích thước phóng đại."}],
        "Tác phẩm đồ họa vector của em đạt chuẩn thiết kế công nghiệp rất tinh tế!"
    ))

    nodes.append(make_lesson(
        "G10-06", "w3", 10, "Nhập môn Python: Cú pháp, Biến & Nhập xuất", "Chủ đề 4: Lập trình Python",
        "Bài 16, 17, 18: Ngôn ngữ Python, Biến & Lệnh vào ra", "Bài 12, 13, 14: Ngôn ngữ Python & Phép toán vào ra", "Bài 12, 13, 14: Làm quen Python & Nhập xuất",
        "type-run", ["G8-07"], 8,
        ["Cú pháp lệnh print() với chuỗi định dạng F-string.", "Hàm input() kết hợp ép kiểu dữ liệu int() và float()."],
        "Chào mừng em đến với Python - ngôn ngữ lập trình phổ biến số 1 thế giới của kỷ nguyên AI và Data Science!",
        "Python là ngôn ngữ lập trình bậc cao thông dịch, cú pháp trong sáng như tiếng Anh giao tiếp thường ngày. Quy tắc biến: tên biến phân biệt chữ hoa chữ thường, không bắt đầu bằng số. Ép kiểu bắt buộc khi nhận dữ liệu từ input(): tuổi = int(input(\"Nhập tuổi: \")).",
        ["Cú pháp in F-string hiện đại: print(f\"Xin chào {ten}, bạn {tuoi} tuổi!\").", "Toán tử // (chia lấy nguyên), % (chia lấy dư), ** (lũy thừa)."],
        {"words": ["print", "input", "float", "while"]},
        [{"question": "Trong Python, câu lệnh 'a = input()' sẽ trả về giá trị thuộc kiểu dữ liệu nào?", "options": ["Kiểu xâu ký tự (str)", "Kiểu số nguyên (int)", "Kiểu số thực (float)"], "answer": 0, "explanation": "Hàm input() trong Python luôn trả về dữ liệu dạng chuỗi ký tự (str)."}],
        "Những dòng mã lệnh Python đầu tiên của em chạy rất mượt mà!"
    ))

    nodes.append(make_lesson(
        "G10-07", "w3", 10, "Cấu trúc Rẽ nhánh Python: If - Elif - Else", "Chủ đề 4: Lập trình Python",
        "Bài 19: Câu lệnh điều kiện if", "Bài 15, 16: Câu lệnh if-else & Nhiều trường hợp", "Bài 15, 16: Cấu trúc if & Elif",
        "bug-hunt", ["G10-06"], 8,
        ["Cú pháp khối lệnh if, if-else, if-elif-else trong Python.", "Quy tắc thụt lề 4 dấu cách (Indentation) bắt buộc theo chuẩn PEP 8."],
        "Trong Python, thụt đầu dòng không chỉ để đẹp mắt, đó là linh hồn của cấu trúc ngữ pháp!",
        "Khác với C/C++ hay Java dùng cặp ngoặc nhọn { }, Python dùng thụt đầu dòng (thường là 4 phím cách Space) để xác định khối mã lệnh trực thuộc câu lệnh điều kiện. Sau mệnh đề if, elif, else bắt buộc phải có dấu hai chấm (:).",
        ["Điều kiện logic kết hợp các từ khóa: and, or, not.", "Lỗi kinh điển: IndentationError (thụt lề không đều nhau)."],
        {},
        [{"question": "Trong Python, sau mệnh đề 'if a > 0' bắt buộc phải có ký tự gì trước khi xuống dòng viết thân lệnh?", "options": ["Dấu hai chấm (:)", "Dấu chấm phẩy (;)", "Dấu ngoặc nhọn {"] , "answer": 0, "explanation": "Dấu hai chấm (:) là cú pháp chuẩn bắt buộc để mở đầu một khối lệnh mới trong Python."}],
        "Em đã làm chủ cú pháp rẽ nhánh if-elif-else chuẩn mực của Python!"
    ))

    nodes.append(make_lesson(
        "G10-08", "w3", 10, "Vòng lặp Python: For, While, Range & Break", "Chủ đề 4: Lập trình Python",
        "Bài 20, 21: Câu lệnh lặp for và while", "Bài 17, 18: Vòng lặp for, while & Range", "Bài 17, 18: Vòng lặp for & while",
        "block-maze", ["G10-07"], 8,
        ["Hàm sinh dãy số range(start, stop, step): lưu ý dừng trước stop.", "Sử dụng lệnh break (ngắt lặp) và continue (bỏ qua bước lặp)."],
        "Duyệt qua hàng triệu phần tử trong tích tắc với sức mạnh của vòng lặp Python!",
        "Cú pháp for: for i in range(1, 10, 2): sinh dãy 1, 3, 5, 7, 9 (dừng trước 10). Cú pháp while: while điều_kiện: lặp cho đến khi điều kiện sai. Lệnh break thoát vòng lặp ngay khi tìm thấy kết quả.",
        ["range(N): sinh dãy từ 0 đến N - 1.", "Vòng lặp lồng nhau (Nested loops) dùng để duyệt ma trận 2 chiều."],
        {"grid_size": 4, "start": {"x": 0, "y": 0, "dir": "E"}, "target": {"x": 3, "y": 3}, "walls": [{"x": 1, "y": 1}, {"x": 2, "y": 2}], "allowed_blocks": ["forward", "turn_right", "turn_left"], "max_blocks": 8},
        [{"question": "Đoạn mã 'for i in range(2, 8, 2):' sẽ duyệt qua những giá trị nào của biến i?", "options": ["2, 4, 6", "2, 4, 6, 8", "2, 3, 4, 5, 6, 7, 8"], "answer": 0, "explanation": "Bước nhảy là 2 và luôn dừng trước giá trị stop = 8, nên các giá trị là 2, 4, 6."}],
        "Vòng lặp Python của em được tối ưu hóa số vòng quay rất hoàn hảo!"
    ))

    nodes.append(make_lesson(
        "G10-09", "w3", 10, "Danh sách List trong Python: Chỉ số, Slicing", "Chủ đề 4: Lập trình Python",
        "Bài 22, 23: Kiểu dữ liệu danh sách & Các lệnh", "Bài 19, 20: Kiểu danh sách & Phương thức", "Bài 19, 20: Danh sách List & Xử lý",
        "logic-puzzle", ["G10-08"], 8,
        ["Truy cập phần tử qua chỉ số âm: a[-1] là phần tử cuối cùng.", "Kỹ thuật cắt lát danh sách (Slicing): a[start:stop:step] và các phương thức: append, pop, sort, reverse."],
        "Danh sách List trong Python cực kỳ linh hoạt: có thể chứa đủ mọi kiểu dữ liệu cùng một lúc!",
        "Khởi tạo: a = [10, 20, 30, 40, 50]. Chỉ số dương: 0, 1, 2, 3, 4; Chỉ số âm: -5, -4, -3, -2, -1. Slicing: a[1:4] lấy các phần tử từ chỉ số 1 đến 3: [20, 30, 40]. Các hàm dựng sẵn: len(a), sum(a), min(a), max(a).",
        ["Phương thức a.append(x): thêm x vào cuối danh sách.", "Phương thức a.sort(): sắp xếp trực tiếp danh sách tăng dần."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [6, 12, 15]},
        [{"question": "Cho danh sách a = [5, 10, 15, 20, 25]. Biểu thức a[-1] trả về giá trị bằng bao nhiêu?", "options": ["25", "5", "Lỗi cú pháp"], "answer": 0, "explanation": "Chỉ số âm -1 trong Python luôn quy ước trỏ tới phần tử cuối cùng của danh sách."}],
        "Kỹ thuật thao tác mảng danh sách List của em đạt đẳng cấp rất chuyên nghiệp!"
    ))

    nodes.append(make_lesson(
        "G10-10", "w3", 10, "Xâu Ký tự String: Cắt chuỗi & Chuẩn hóa", "Chủ đề 4: Lập trình Python",
        "Bài 24, 25: Xâu ký tự & Lệnh làm việc với xâu", "Bài 21, 22: Xâu ký tự & Chuẩn hóa", "Bài 21, 22: Kiểu chuỗi & Xử lý xâu",
        "type-run", ["G10-09"], 8,
        ["Hiểu xâu ký tự là kiểu dữ liệu bất biến (Immutable).", "Sử dụng các phương thức xử lý văn bản: split(), join(), strip(), replace(), upper(), lower()."],
        "Lập trình thuật toán tự động nhận diện và chuẩn hóa họ tên học sinh sạch đẹp!",
        "Xâu ký tự là chuỗi các ký tự đặt trong cặp nháy kép \"...\" hoặc nháy đơn '...'. Phương thức s.strip(): xóa khoảng trắng thừa ở hai đầu xâu. Phương thức s.split(): tách xâu thành danh sách các từ. Phương thức ' '.join(words): ghép danh sách các từ lại thành một xâu hoàn chỉnh.",
        ["Kiểm tra chuỗi đối xứng (Palindrome): s == s[::-1].", "Đếm số lần xuất hiện của từ: s.count('tin')."],
        {"words": ["split", "strip", "upper", "lower"]},
        [{"question": "Trong Python, câu lệnh ' \"  Ha Noi  \".strip() ' cho kết quả là xâu ký tự nào?", "options": ["\"Ha Noi\"", "\"HaNoi\"", "\"  Ha Noi\""], "answer": 0, "explanation": "Hàm strip() loại bỏ toàn bộ khoảng trắng thừa ở hai đầu đầu mút của chuỗi."}],
        "Em đã làm chủ toàn diện các kỹ thuật xử lý và chuẩn hóa chuỗi ký tự trong Python!"
    ))

    nodes.append(make_lesson(
        "G10-11", "w3", 10, "Hàm trong Python: Def, Return & Phạm vi Biến", "Chủ đề 4: Lập trình Python",
        "Bài 26, 27, 28: Hàm, Tham số & Phạm vi biến", "Bài 23, 24, 25: Khái niệm hàm & Tham số", "Bài 23, 24, 25: Hàm & Chương trình con",
        "bug-hunt", ["G10-10"], 8,
        ["Định nghĩa hàm với từ khóa def, truyền tham số và trả về giá trị qua lệnh return.", "Phân biệt biến cục bộ (Local Scope) trong hàm và biến toàn cục (Global Scope)."],
        "Module hóa mã nguồn: Xây dựng các khối lego chức năng để tái sử dụng mãi mãi!",
        "Cú pháp hàm: def ten_ham(tham_so): ... return ket_qua. Lệnh return kết thúc hàm và chuyển giá trị kết quả ra ngoài. Biến khai báo bên trong hàm là biến cục bộ, chỉ tồn tại khi hàm đang chạy. Muốn sửa biến toàn cục trong hàm phải khai báo từ khóa global.",
        ["Hàm giúp mã nguồn ngắn gọn, dễ đọc, dễ kiểm thử và tái sử dụng.", "Truyền tham số mặc định (Default arguments): def tinh_tien(gia, vat=0.1):."],
        {},
        [{"question": "Từ khóa nào trong Python dùng để định nghĩa một hàm mới?", "options": ["def", "function", "void"], "answer": 0, "explanation": "Từ khóa 'def' (viết tắt của define) dùng để khai báo định nghĩa hàm trong Python."}],
        "Kiến trúc chương trình con của em được module hóa rất chặt chẽ và sáng sủa!"
    ))

    nodes.append(make_lesson(
        "G10-12", "w3", 10, "Kỹ thuật Kiểm thử Hộp đen & Bắt Lỗi Try-Except", "Chủ đề 4: Lập trình Python",
        "Bài 29, 30: Nhận biết lỗi, Kiểm thử & Gỡ lỗi", "Bài 26, 27: Nhận diện lỗi & Ngoại lệ try/except", "Bài 26, 27: Gỡ lỗi & Kiểm thử test cases",
        "bug-hunt", ["G10-11"], 8,
        ["Thiết kế bộ dữ liệu kiểm thử (Test Cases) bao gồm ca kiểm thử biên (Boundary tests).", "Xử lý các ngoại lệ thời gian chạy phổ biến: ZeroDivisionError, ValueError, IndexError."],
        "Kiểm thử phần mềm là tấm khiên bảo vệ uy tín và độ tin cậy của mọi sản phẩm công nghệ!",
        "Kiểm thử hộp đen (Black-box testing): kiểm tra chức năng chương trình mà không cần nhìn vào mã nguồn bên trong; đưa các đầu vào đặc biệt (số 0, số âm cực lớn, chuỗi rỗng) để xem chương trình có xử lý đúng không. Khối try-except bắt các lỗi người dùng nhập sai để hiển thị thông báo dịu dàng.",
        ["Quy tắc: Thử ngoại lệ hẹp (specific exception) trước khi dùng except chung chung.", "Bộ Test Cases tốt phải bao phủ tất cả các nhánh điều kiện if/else."],
        {},
        [{"question": "Khi thực hiện phép tính 'a = 10 / 0' trong Python, trình thông dịch sẽ ném ra ngoại lệ lỗi nào?", "options": ["ZeroDivisionError", "ValueError", "TypeError"], "answer": 0, "explanation": "ZeroDivisionError là ngoại lệ sinh ra khi chia một số cho số 0."}],
        "Khả năng bắt lỗi và bảo vệ phần mềm trước các ca kiểm thử biên của em rất xuất sắc!"
    ))

    nodes.append(make_lesson(
        "G10-13", "w3", 10, "Thao tác Tệp Văn bản File I/O trong Python", "Chủ đề 4: Lập trình Python",
        "Bài 31: Thực hành viết chương trình", "Bài 28: Làm việc với tệp văn bản", "Bài 28: Đọc và ghi tệp dữ liệu",
        "logic-puzzle", ["G10-11"], 8,
        ["Mở tệp đọc ('r') và ghi ('w') dữ liệu với cú pháp chuẩn: with open(path) as f:.", "Đọc dữ liệu từ INPUT.TXT và ghi kết quả ra OUTPUT.TXT chuẩn thi học sinh giỏi."],
        "Lưu giữ vĩnh viễn kết quả xử lý của chương trình vào ổ cứng qua các tệp tin dữ liệu!",
        "Cú pháp chuẩn: `with open(\"data.txt\", \"r\", encoding=\"utf-8\") as f: lines = f.readlines()`. Sử dụng từ khóa `with` giúp tệp tự động được đóng an toàn ngay cả khi xảy ra lỗi. Đọc từng dòng bằng `readline()`, đọc toàn bộ thành danh sách dòng bằng `readlines()`.",
        ["Chế độ 'w' (ghi đè, xóa dữ liệu cũ), chế độ 'a' (ghi nối tiếp vào cuối tệp).", "Luôn chỉ định encoding=\"utf-8\" để xử lý văn bản tiếng Việt có dấu."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [5, 9, 13]},
        [{"question": "Trong Python, cú pháp 'with open(\"data.txt\", \"r\") as f:' có ưu điểm vượt trội gì so với mở tệp thông thường?", "options": ["Tệp sẽ tự động được đóng lại an toàn sau khi kết thúc khối lệnh, tránh rò rỉ bộ nhớ", "Tệp sẽ chạy nhanh hơn gấp 10 lần", "Tệp tự động được mã hóa chống xem trộm"], "answer": 0, "explanation": "Context manager 'with' tự động dọn dẹp và giải phóng tài nguyên tệp tin."}],
        "Em đã làm chủ thành thạo thao tác đọc và ghi tệp tin dữ liệu chuẩn quốc tế!"
    ))

    nodes.append(make_lesson(
        "G10-14", "w3", 10, "Cổng Logic Số & Bảng Chân trị (AND, OR, NOT, XOR)", "Chủ đề CS: Khoa học máy tính",
        "Chuyên đề CS 10: Kiến trúc máy tính & Cổng logic", "Chuyên đề CS 10: Mạch logic & Bảng chân trị", "Chuyên đề CS 10: Phần cứng số & Cổng logic",
        "logic-puzzle", ["G10-01"], 8,
        ["Hiểu nguyên lý các cổng logic cơ bản: AND (Và), OR (Hoặc), NOT (Đảo), XOR (Loại trừ).", "Lập bảng chân trị (Truth Table) và thiết kế mạch cộng nhị phân nửa (Half Adder)."],
        "Khám phá các viên gạch điện tử siêu nhỏ tạo nên bộ não siêu máy tính hiện đại!",
        "Cổng AND: ngõ ra 1 khi TẤT CẢ ngõ vào đều là 1. Cổng OR: ngõ ra 1 khi CÓ ÍT NHẤT MỘT ngõ vào là 1. Cổng NOT: đảo bit 0 thành 1 và ngược lại. Cổng XOR: ngõ ra 1 khi hai ngõ vào KHÁC NHAU. Mạch Half Adder kết hợp cổng XOR (tính Tổng Sum) và cổng AND (tính Số nhớ Carry) để cộng 2 bit nhị phân.",
        ["Bảng chân trị liệt kê tất cả các tổ hợp đầu vào và ngõ ra tương ứng.", "Hàng tỷ cổng logic được tích hợp trong một con chip CPU kích cỡ móng tay."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [3, 7, 12]},
        [{"question": "Cổng logic nào có ngõ ra bằng 1 khi và chỉ khi hai tín hiệu ngõ vào có giá trị KHÁC NHAU (một bên 0, một bên 1)?", "options": ["Cổng XOR", "Cổng AND", "Cổng OR"], "answer": 0, "explanation": "Cổng XOR (Exclusive OR) phát hiện sự khác biệt giữa hai tín hiệu đầu vào."}],
        "Em đã giải mã hoàn hảo nguyên lý mạch điện tử số của ngành Khoa học máy tính!"
    ))

    nodes.append(make_lesson(
        "G10-15", "w3", 10, "Đấu trường Trùm Lớp 10: Cao thủ Python & Phần cứng Số", "Tổng kết GDPT 2018 Lớp 10",
        "Bài 33, 34: Nghề nghiệp, Dự án học tập & Tổng kết", "Bài 31, 32: Nghề lập trình & Đánh giá năng lực 10", "Bài 31, 32: Nghề đồ họa, lập trình & Tổng kết",
        "boss-quiz", ["G10-05", "G10-07", "G10-08", "G10-09", "G10-14"], 15,
        ["Tổng kết toàn diện chuẩn kiến thức Tin học Lớp 10 của cả 3 bộ sách.", "Sẵn sàng nhận huy hiệu Cao Thủ Python & Phần Cứng Số EasyTin."],
        "Trùm Glitch Byte Chúa Tể đang xâm chiếm không gian mạng! Hãy dùng sức mạnh tổng hợp của Python và Mạch Logic để đánh bại nó!",
        "Đấu trường tổng hợp đỉnh cao: IoT, Phần mềm nguồn mở, Đồ họa vector Inkscape, Thuật toán Python, Cổng logic và Bảng chân trị.",
        ["Hàm Python, Danh sách List, Xâu String, Xử lý file.", "Cổng logic AND, OR, XOR và kiến trúc Client - Server."],
        {"boss_name": "Glitch Byte Chúa Tể", "boss_max_hp": 100, "player_max_hp": 100, "damage_per_hit": 25, "questions_pool": 4},
        [
            {"question": "Trong Python, kết quả của biểu thức 'len([1, 2, 3] * 2)' là bao nhiêu?", "options": ["6 (danh sách được nhân bản thành [1, 2, 3, 1, 2, 3])", "3", "2", "Lỗi cú pháp"], "answer": 0, "explanation": "Toán tử * trên danh sách sẽ nhân đôi các phần tử của danh sách đó."},
            {"question": "Cổng logic XOR có kết quả bằng bao nhiêu khi hai đầu vào là A = 1 và B = 1?", "options": ["0", "1", "2", "Không xác định"], "answer": 0, "explanation": "Hai đầu vào giống nhau thì ngõ ra của cổng XOR bằng 0."},
            {"question": "Mô hình mạng nào sau đây có các máy tính bình đẳng vừa đóng vai trò chia sẻ vừa tải tài nguyên dữ liệu?", "options": ["Mạng ngang hàng (Peer-to-Peer - P2P)", "Mạng Khách - Chủ (Client - Server)", "Mạng hình sao tập trung", "Mạng vòng"], "answer": 0, "explanation": "P2P là mô hình mạng ngang hàng phân tán phi tập trung."},
            {"question": "Định dạng đồ họa nào sau đây là định dạng đồ họa véc-tơ chuẩn?", "options": [".svg", ".jpg", ".png", ".bmp"], "answer": 0, "explanation": ".svg (Scalable Vector Graphics) là định dạng vector chuẩn web."}
        ],
        "CHIẾN CÔNG VANG DỘI! Em đã tiêu diệt Glitch Byte Chúa Tể và hoàn thành xuất sắc toàn bộ chương trình Tin học Lớp 10 của cả 3 bộ sách KNTT, Cánh Diều, CTST!"
    ))

    # =========================================================================
    # LỚP 11 (14 NÚT - THẾ GIỚI 3)
    # =========================================================================
    nodes.append(make_lesson(
        "G11-01", "w3", 11, "Hệ Cơ sở Dữ liệu (DBMS) & Mô hình Quan hệ", "Chủ đề CS: Khoa học máy tính",
        "Bài CS-1, CS-2: Giới thiệu CSDL & Hệ QTCSDL", "Bài CS-1, CS-2: CSDL & Bảng dữ liệu", "Bài CS-1, CS-2: Khái niệm CSDL quan hệ",
        "sort-drag", ["G10-02"], 8,
        ["Khái niệm Cơ sở dữ liệu (Database) và Hệ quản trị CSDL (DBMS).", "Phân tích cấu trúc bảng dữ liệu quan hệ: Bảng (Table), Bản ghi (Record/Row), Thuộc tính trường (Field/Column)."],
        "Làm thế nào ngân hàng Vietcombank hay mạng xã hội Facebook lưu trữ và tra cứu thông tin của 100 triệu người dùng chỉ trong 0.01 giây?",
        "CSDL là tập hợp dữ liệu có cấu trúc, liên quan logic với nhau và được lưu trữ có tổ chức trên máy tính. Hệ quản trị CSDL (RDBMS: MySQL, PostgreSQL, Oracle, SQL Server) là phần mềm trung gian giúp người dùng tạo lập, cập nhật, truy vấn và bảo mật CSDL tập trung.",
        ["Tránh dư thừa dữ liệu (Data Redundancy) và đảm bảo tính nhất quán dữ liệu.", "Độc lập dữ liệu: thay đổi cấu trúc lưu trữ vật lý không làm hỏng ứng dụng."],
        {"groups": [{"id": "g1", "name": "Thành phần Bảng CSDL Quan hệ"}, {"id": "g2", "name": "Hệ Quản trị CSDL Phổ biến (RDBMS)"}], "items": [{"id":"1","name":"Bản ghi (Record/Row) chứa thông tin 1 học sinh","group":"g1","icon":"📋"},{"id":"2","name":"Trường (Field/Column) biểu diễn thuộc tính Điểm_Toan","group":"g1","icon":"🏷️"},{"id":"3","name":"Hệ quản trị CSDL nguồn mở MySQL","group":"g2","icon":"🐬"},{"id":"4","name":"Hệ quản trị CSDL doanh nghiệp PostgreSQL","group":"g2","icon":"🐘"}]},
        [{"question": "Trong cơ sở dữ liệu quan hệ, mỗi hàng (Row) trong một bảng được gọi là gì?", "options": ["Bản ghi (Record)", "Trường thuộc tính (Field)", "Kiểu dữ liệu"], "answer": 0, "explanation": "Mỗi hàng trong bảng biểu diễn một thực thể dữ liệu trọn vẹn gọi là Bản ghi (Record)."}],
        "Em đã nắm vững khái niệm nền tảng về Cơ sở dữ liệu quan hệ RDBMS!"
    ))

    nodes.append(make_lesson(
        "G11-02", "w3", 11, "Toàn vẹn Thực thể: Khóa chính & Khóa ngoại", "Chủ đề CS: Khoa học máy tính",
        "Bài CS-3: Khóa chính và khóa ngoại", "Bài CS-3: Khóa chính & Liên kết bảng", "Bài CS-3: Ràng buộc toàn vẹn CSDL",
        "logic-puzzle", ["G11-01"], 8,
        ["Xác định Khóa chính (Primary Key): duy nhất (Unique) và không được rỗng (Not Null).", "Xác định Khóa ngoại (Foreign Key): tham chiếu liên kết giữa hai bảng dữ liệu."],
        "Khóa chính giống như Số Căn cước công dân: Mỗi công dân chỉ có duy nhất một số để không bao giờ bị nhầm lẫn!",
        "Khóa chính (PK) là một hoặc nhiều trường xác định duy nhất mỗi bản ghi trong bảng. Khóa ngoại (FK) là trường trong một bảng tham chiếu trực tiếp đến Khóa chính của một bảng khác, tạo mối quan hệ ràng buộc toàn vẹn dữ liệu (Referential Integrity).",
        ["Bảng chứa khóa ngoại là bảng con, bảng chứa khóa chính được tham chiếu là bảng cha.", "Không thể xóa bản ghi bảng cha nếu đang có bản ghi bảng con tham chiếu đến."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [5, 9, 13]},
        [{"question": "Đặc điểm bắt buộc của một Khóa chính (Primary Key) trong bảng dữ liệu là gì?", "options": ["Giá trị phải là duy nhất và không được để trống (NOT NULL)", "Phải là số chẵn", "Có thể trùng lặp tùy ý"], "answer": 0, "explanation": "Khóa chính định danh duy nhất cho từng hàng nên không được phép trùng lặp hoặc để trống."}],
        "Tư duy thiết kế khóa và ràng buộc toàn vẹn CSDL của em rất chuẩn xác!"
    ))

    nodes.append(make_lesson(
        "G11-03", "w3", 11, "Ngôn ngữ SQL: Lệnh SELECT & Điều kiện WHERE", "Chủ đề CS: Khoa học máy tính",
        "Bài CS-4, CS-5: Ngôn ngữ SQL & Lọc sắp xếp", "Bài CS-4, CS-5: Ngôn ngữ SQL & Mệnh đề WHERE", "Bài CS-4, CS-5: Truy vấn SQL & Bộ lọc",
        "logic-puzzle", ["G11-02"], 8,
        ["Cú pháp chuẩn mực của câu lệnh truy vấn dữ liệu SQL: SELECT ... FROM ... WHERE ...", "Sử dụng các toán tử so sánh (=, !=, >, <), toán tử logic (AND, OR, NOT) và toán tử LIKE mẫu chuỗi."],
        "Trò chuyện trực tiếp với kho dữ liệu khổng lồ bằng ngôn ngữ truy vấn có cấu trúc SQL!",
        "SQL (Structured Query Language) là ngôn ngữ chuẩn mực để thao tác dữ liệu. Mệnh đề SELECT chọn các cột cần lấy; Mệnh đề FROM chỉ định nguồn bảng; Mệnh đề WHERE thiết lập điều kiện lọc bản ghi; Mệnh đề ORDER BY sắp xếp kết quả tăng dần (ASC) hoặc giảm dần (DESC).",
        ["Ví dụ: SELECT HoTen, DiemTB FROM HocSinh WHERE DiemTB >= 8.0 ORDER BY DiemTB DESC;.", "Toán tử LIKE 'Nguyen%': tìm tất cả các học sinh có họ Nguyễn."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [4, 7, 14]},
        [{"question": "Trong câu lệnh SQL, mệnh đề nào sau đây dùng để thiết lập điều kiện lọc dữ liệu?", "options": ["Mệnh đề WHERE", "Mệnh đề FROM", "Mệnh đề SELECT"], "answer": 0, "explanation": "Mệnh đề WHERE dùng để chỉ định điều kiện lọc các bản ghi thỏa mãn."}],
        "Em đã viết thành thạo những câu lệnh truy vấn SQL kinh điển!"
    ))

    nodes.append(make_lesson(
        "G11-04", "w3", 11, "Ngôn ngữ SQL: Gom nhóm GROUP BY & Hàm Tổng hợp", "Chủ đề CS: Khoa học máy tính",
        "Bài CS-6: Các hàm tổng hợp trong SQL", "Bài CS-6: Các hàm tính toán tổng hợp", "Bài CS-6: Gom nhóm dữ liệu GROUP BY",
        "logic-puzzle", ["G11-03"], 8,
        ["Sử dụng 5 hàm tổng hợp: COUNT(), SUM(), AVG(), MIN(), MAX().", "Kết hợp mệnh đề gom nhóm GROUP BY và điều kiện lọc nhóm HAVING."],
        "Thống kê điểm trung bình của từng lớp học trong toàn trường chỉ bằng 3 dòng mã SQL!",
        "Mệnh đề GROUP BY gom các bản ghi có cùng giá trị trên một cột thành một nhóm. Các hàm tổng hợp sẽ tính toán trên từng nhóm đó: COUNT(*) đếm số lượng, AVG(Diem) tính trung bình. Mệnh đề HAVING dùng để lọc các nhóm sau khi gom (khác với WHERE lọc từng bản ghi trước khi gom).",
        ["Ví dụ: SELECT Lop, AVG(DiemTB) FROM HocSinh GROUP BY Lop HAVING AVG(DiemTB) >= 7.0;.", "Mọi cột xuất hiện trong SELECT (ngoài hàm tổng hợp) đều phải có mặt trong GROUP BY."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [6, 11, 15]},
        [{"question": "Để lọc các nhóm dữ liệu SAU KHI đã thực hiện gom nhóm GROUP BY trong SQL, ta dùng mệnh đề nào?", "options": ["Mệnh đề HAVING", "Mệnh đề WHERE", "Mệnh đề ORDER BY"], "answer": 0, "explanation": "HAVING là mệnh đề chuyên biệt dùng để thiết lập điều kiện lọc cho các nhóm sau GROUP BY."}],
        "Khả năng thống kê và phân tích số liệu dữ liệu lớn bằng SQL của em rất xuất sắc!"
    ))

    nodes.append(make_lesson(
        "G11-05", "w3", 11, "Ngôn ngữ SQL: Liên kết Nhiều Bảng (INNER JOIN)", "Chủ đề CS: Khoa học máy tính",
        "Bài CS-7: Liên kết bảng với INNER JOIN", "Bài CS-7: Truy vấn kết nối nhiều bảng", "Bài CS-7: Kết nối bảng dữ liệu JOIN",
        "logic-puzzle", ["G11-04"], 8,
        ["Hiểu cơ chế kết nối bảng dữ liệu qua khóa ngoại bằng mệnh đề INNER JOIN ... ON ...", "Trích xuất thông tin tổng hợp từ 2 hoặc nhiều bảng liên kết."],
        "Nối các mảnh ghép dữ liệu từ nhiều bảng thành bức tranh thông tin hoàn chỉnh!",
        "INNER JOIN kết hợp các hàng từ hai bảng dựa trên điều kiện so khớp khóa: BảngA.KhoaChinh = BảngB.KhoaNgoai. Chỉ những hàng có giá trị khớp ở cả hai bảng mới xuất hiện trong kết quả truy vấn.",
        ["Ví dụ: SELECT HocSinh.HoTen, LopHoc.TenLop FROM HocSinh INNER JOIN LopHoc ON HocSinh.MaLop = LopHoc.MaLop;.", "Có thể kết hợp nhiều mệnh đề JOIN liên tiếp để nối 3, 4 bảng."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [3, 10, 13]},
        [{"question": "Mệnh đề INNER JOIN kết nối các bảng dữ liệu dựa trên điều kiện gì được chỉ định sau từ khóa ON?", "options": ["Sự so khớp giá trị giữa Khóa chính và Khóa ngoại của hai bảng", "Tên bảng giống nhau", "Độ dài dữ liệu bằng nhau"], "answer": 0, "explanation": "INNER JOIN kết nối các bản ghi dựa trên sự tương thích giữa khóa chính và khóa ngoại."}],
        "Em đã làm chủ kỹ thuật liên kết dữ liệu quan hệ đa bảng đỉnh cao!"
    ))

    nodes.append(make_lesson(
        "G11-06", "w3", 11, "Ngôn ngữ SQL: Thao tác INSERT, UPDATE & DELETE", "Chủ đề CS: Khoa học máy tính",
        "Bài CS-8: Cập nhật và xóa dữ liệu SQL", "Bài CS-8: Chèn, sửa và xóa bản ghi", "Bài CS-8: Thao tác dữ liệu an toàn",
        "bug-hunt", ["G11-05"], 8,
        ["Thành thạo các lệnh thao tác dữ liệu (DML): INSERT INTO, UPDATE, DELETE.", "Quy tắc an toàn sống còn: Luôn có điều kiện WHERE khi chạy lệnh UPDATE và DELETE."],
        "Cẩn trọng từng ký tự: Quên một chữ WHERE trong lệnh DELETE có thể xóa sạch toàn bộ dữ liệu công ty!",
        "INSERT INTO Bảng (Cột1, Cột2) VALUES (GiaTri1, GiaTri2) thêm bản ghi mới. UPDATE Bảng SET Cột = GiaTriMoi WHERE DieuKien sửa bản ghi. DELETE FROM Bảng WHERE DieuKien xóa bản ghi. Nếu không có WHERE, lệnh UPDATE và DELETE sẽ áp dụng lên TẤT CẢ các hàng trong bảng!",
        ["Giao dịch CSDL (Transaction): COMMIT để xác nhận lưu, ROLLBACK để hủy thao tác khi có sự cố.", "Quy tắc toàn vẹn dữ liệu ngăn chặn việc xóa bản ghi cha đang được tham chiếu."],
        {},
        [{"question": "Nếu chạy câu lệnh 'DELETE FROM HocSinh;' mà KHÔNG có mệnh đề WHERE, điều gì thảm khốc sẽ xảy ra?", "options": ["Toàn bộ dữ liệu của tất cả học sinh trong bảng sẽ bị xóa sạch hoàn toàn", "Chỉ xóa học sinh đầu tiên", "Chương trình tự động hỏi lại"], "answer": 0, "explanation": "Thiếu WHERE khiến lệnh DELETE quét sạch không sót một bản ghi nào trong bảng."}],
        "Em đã trang bị tác phong cẩn trọng và chuẩn mực của một chuyên gia quản trị CSDL chuyên nghiệp!"
    ))

    nodes.append(make_lesson(
        "G11-07", "w3", 11, "Thiết kế & Chuẩn hóa CSDL (1NF, 2NF, 3NF)", "Chủ đề CS: Khoa học máy tính",
        "Bài CS-9, CS-10: Thiết kế & Chuẩn hóa dữ liệu", "Bài CS-9, CS-10: Phân tích CSDL & Dạng chuẩn", "Bài CS-9, CS-10: Chuẩn hóa CSDL quan hệ",
        "sort-drag", ["G11-06"], 8,
        ["Nhận biết các dị thường dữ liệu (Dư thừa, Sửa đổi, Xóa bất thường).", "Nắm vững 3 dạng chuẩn: 1NF (nguyên tử), 2NF (phụ thuộc hàm đầy đủ), 3NF (không phụ thuộc bắc cầu)."],
        "Thiết kế CSDL tối ưu giống như xây dựng nền móng một tòa cao ốc chọc trời: Vững chắc và không bao giờ sụp đổ!",
        "Dạng chuẩn 1 (1NF): Mọi giá trị thuộc tính phải là nguyên tử (không chứa mảng hay danh sách giá trị trong một ô). Dạng chuẩn 2 (2NF): Đạt 1NF và mọi thuộc tính không khóa phải phụ thuộc hàm đầy đủ vào toàn bộ khóa chính. Dạng chuẩn 3 (3NF): Đạt 2NF và không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa chính qua thuộc tính khác.",
        ["Chuẩn hóa giúp loại bỏ triệt để tình trạng dư thừa dữ liệu lãng phí bộ nhớ.", "Ngăn ngừa lỗi mất dữ liệu khi cập nhật thông tin."],
        {"groups": [{"id": "g1", "name": "Tiêu chí Dạng chuẩn CSDL"}, {"id": "g2", "name": "Các Dị thường CSDL chưa chuẩn hóa"}], "items": [{"id":"1","name":"Dạng chuẩn 1NF (Giá trị ô phải mang tính nguyên tử)","group":"g1","icon":"1️⃣"},{"id":"2","name":"Dạng chuẩn 3NF (Loại bỏ phụ thuộc hàm bắc cầu)","group":"g1","icon":"3️⃣"},{"id":"3","name":"Dư thừa dữ liệu lặp đi lặp lại nhiều lần","group":"g2","icon":"🔁"},{"id":"4","name":"Dị thường xóa (Xóa thông tin này vô tình mất thông tin khác)","group":"g2","icon":"⚠️"}]},
        [{"question": "Một bảng CSDL đạt Dạng chuẩn 1 (1NF) khi thỏa mãn điều kiện bắt buộc nào?", "options": ["Tất cả các giá trị thuộc tính trong mỗi ô tính đều phải mang tính nguyên tử (không thể phân chia nhỏ hơn)", "Bảng phải có ít nhất 100 hàng", "Khóa chính phải là số nguyên"], "answer": 0, "explanation": "Tính nguyên tử (Atomic) là yêu cầu tiên quyết của dạng chuẩn 1NF."}],
        "Tư duy thiết kế CSDL chuẩn hóa 3NF của em đạt chất lượng của kỹ sư hệ thống phần mềm!"
    ))

    nodes.append(make_lesson(
        "G11-08", "w3", 11, "Kỹ thuật Thuật toán Đệ quy (Recursion)", "Chủ đề CS: Khoa học máy tính",
        "Bài CS-11, CS-12: Thuật toán đệ quy & Tháp Hà Nội", "Bài CS-11, CS-12: Phương pháp đệ quy & Quay lui", "Bài CS-11, CS-12: Đệ quy & Bài toán kinh điển",
        "bug-hunt", ["G10-11"], 8,
        ["Hiểu bản chất đệ quy: Hàm tự gọi lại chính nó với bài toán con nhỏ hơn.", "Bắt buộc phải có hai thành phần: Điểm dừng (Base Case) và Bước đệ quy (Recursive Step)."],
        "Chiếc gương phản chiếu vô tận trong lập trình: Giải quyết bài toán lớn bằng chính nó trong phiên bản nhỏ hơn!",
        "Hàm đệ quy gọi lại chính nó. Điểm dừng (Base case) là điều kiện bài toán đơn giản nhất đã biết kết quả, ngăn không cho hàm gọi đệ quy tiếp. Nếu thiếu điểm dừng, hàm sẽ gọi nhau vô hạn làm tràn bộ nhớ ngăn xếp (Stack Overflow Error) sập chương trình. Bài toán kinh điển: Tính giai thừa N! = N * (N - 1)!, Dãy Fibonacci, Tháp Hà Nội.",
        ["Ngăn xếp lời gọi hàm (Call Stack) lưu vết các tầng đệ quy.", "Kỹ thuật tối ưu đệ quy có nhớ (Memoization)."],
        {},
        [{"question": "Nếu một hàm đệ quy bị lập trình viên viết thiếu điều kiện điểm dừng (Base Case), điều gì chắc chắn sẽ xảy ra?", "options": ["Lặp đệ quy vô hạn và làm tràn bộ nhớ ngăn xếp (Stack Overflow Error)", "Chương trình chạy nhanh hơn gấp đôi", "Máy tính tự tìm ra kết quả"], "answer": 0, "explanation": "Thiếu điểm dừng khiến hàm tự gọi mãi mãi làm cạn kiệt bộ nhớ ngăn xếp Call Stack."}],
        "Em đã làm chủ kỹ thuật đệ quy tư duy trừu tượng đỉnh cao của Khoa học máy tính!"
    ))

    nodes.append(make_lesson(
        "G11-09", "w3", 11, "Thuật toán Chia để trị & Sắp xếp Trộn (Merge Sort)", "Chủ đề CS: Khoa học máy tính",
        "Bài CS-13: Thuật toán chia để trị & Merge Sort", "Bài CS-13: Thuật toán sắp xếp trộn Merge Sort", "Bài CS-13: Sắp xếp trộn & Chia để trị",
        "logic-puzzle", ["G11-08"], 8,
        ["Nguyên lý chiến lược Chia để trị (Divide and Conquer): Chia -> Trị -> Kết hợp.", "Mô tả thuật toán Sắp xếp trộn (Merge Sort) đạt độ phức tạp tối ưu O(N log N)."],
        "Chiến lược 'Chia để trị' của các vị tướng đại tài được ứng dụng hoàn hảo vào giải thuật sắp xếp dữ liệu lớn!",
        "Bước 1 (Chia): Chia danh sách ban đầu thành 2 nửa bằng nhau cho đến khi mỗi danh sách con chỉ còn 1 phần tử. Bước 2 (Trị): Danh sách 1 phần tử coi như đã sắp xếp. Bước 3 (Kết hợp): Trộn (Merge) từng cặp hai danh sách con đã sắp xếp lại thành một danh sách có thứ tự. Thuật toán luôn đạt tốc độ O(N log N) trong mọi trường hợp.",
        ["Merge Sort là thuật toán sắp xếp ổn định (Stable Sort).", "Cần bộ nhớ phụ để thực hiện thao tác trộn hai mảng."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [2, 7, 13]},
        [{"question": "Độ phức tạp thời gian của thuật toán Sắp xếp trộn (Merge Sort) trong trường hợp xấu nhất là bao nhiêu?", "options": ["O(N log N)", "O(N^2)", "O(N)"], "answer": 0, "explanation": "Merge Sort chia đôi liên tục log(N) tầng và mỗi tầng mất N phép so sánh nên đạt O(N log N)."}],
        "Tư duy thuật toán Chia để trị của em vận hành cực kỳ tối ưu!"
    ))

    nodes.append(make_lesson(
        "G11-10", "w3", 11, "Thuật toán Sắp xếp Nhanh (Quick Sort)", "Chủ đề CS: Khoa học máy tính",
        "Bài CS-14: Thuật toán sắp xếp nhanh Quick Sort", "Bài CS-14: Thuật toán Quick Sort & Phân đoạn", "Bài CS-14: Sắp xếp nhanh & Phân đoạn",
        "bug-hunt", ["G11-09"], 8,
        ["Hiểu cơ chế chọn phần tử chốt (Pivot) và phân hoạch mảng (Partitioning).", "So sánh hiệu năng thực tế của Quick Sort và các thuật toán khác."],
        "Thuật toán sắp xếp được sử dụng phổ biến nhất trong mọi thư viện chuẩn của các ngôn ngữ lập trình hiện đại!",
        "Nguyên lý: Chọn 1 phần tử làm Chốt (Pivot). Phân hoạch mảng sao cho tất cả các phần tử nhỏ hơn chốt dồn về bên trái, các phần tử lớn hơn chốt dồn về bên phải. Gọi đệ quy Quick Sort cho hai nửa mảng trái và phải. Tốc độ trung bình đạt O(N log N) và sắp xếp tại chỗ (In-place) không tốn bộ nhớ phụ.",
        ["Cách chọn Pivot thông minh: lấy phần tử ở giữa hoặc trung vị của 3 phần tử.", "Trường hợp xấu nhất: mảng đã sắp xếp và chọn chốt ở đầu mút (O(N^2))."],
        {},
        [{"question": "Trong thuật toán Quick Sort, phần tử đặc biệt được chọn làm mốc để chia mảng thành hai nửa nhỏ hơn và lớn hơn được gọi là gì?", "options": ["Phần tử chốt (Pivot)", "Phần tử gốc", "Phần tử đỉnh"], "answer": 0, "explanation": "Pivot (chốt) là mốc phân đoạn cốt lõi của thuật toán Quick Sort."}],
        "Em đã nắm vững thuật toán Sắp xếp nhanh Quick Sort huyền thoại!"
    ))

    nodes.append(make_lesson(
        "G11-11", "w3", 11, "Đánh giá Độ phức tạp Thuật toán (Big-O)", "Chủ đề CS: Khoa học máy tính",
        "Bài CS-15: Đánh giá độ phức tạp thuật toán", "Bài CS-15: Độ phức tạp & Tối ưu mã nguồn", "Bài CS-15: Đánh giá Big-O thuật toán",
        "logic-puzzle", ["G11-10"], 8,
        ["Hiểu ý nghĩa của ký hiệu Big-O biểu diễn tốc độ tăng thời gian thực thi theo kích thước đầu vào N.", "So sánh các bậc tăng trưởng: O(1) < O(log N) < O(N) < O(N log N) < O(N^2) < O(2^N)."],
        "Thước đo vàng đánh giá một thuật toán đẳng cấp hay yếu kém của các nhà khoa học máy tính!",
        "Ký hiệu O(f(N)) biểu diễn tiệm cận trên thời gian chạy của thuật toán khi N tiến tới vô cùng. O(1): thời gian hằng số (truy cập mảng). O(log N): tìm kiếm nhị phân. O(N): tìm kiếm tuần tự. O(N log N): sắp xếp nhanh/trộn. O(N^2): sắp xếp nổi bọt. O(2^N): duyệt đệ quy vét cạn.",
        ["Bỏ qua các hằng số nhân và số hạng bậc thấp khi tính Big-O: O(3N^2 + 5N) = O(N^2).", "Mục tiêu tối thượng: đưa các thuật toán từ O(N^2) xuống O(N log N)."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [1, 5, 14]},
        [{"question": "Trong các độ phức tạp thuật toán sau, độ phức tạp nào cho thời gian chạy NHANH NHẤT khi N rất lớn?", "options": ["O(log N)", "O(N)", "O(N^2)"], "answer": 0, "explanation": "O(log N) tăng trưởng cực kỳ chậm, nhanh hơn rất nhiều so với O(N) và O(N^2)."}],
        "Khả năng phân tích đánh giá độ phức tạp Big-O của em đạt chuẩn nhà khoa học máy tính!"
    ))

    nodes.append(make_lesson(
        "G11-12", "w3", 11, "Thiết kế Đồ họa Đa phương tiện & Xử lý Ảnh ICT", "Chủ đề ICT: Tin học ứng dụng",
        "Chuyên đề ICT 11: Chỉnh sửa ảnh & Đồ họa", "Chuyên đề ICT 11: Đồ họa đa phương tiện", "Chuyên đề ICT 11: Biên tập ảnh số",
        "sort-drag", ["G10-05"], 8,
        ["Khai thác các bộ lọc hiệu ứng (Filters), điều chỉnh đường cong màu Curves.", "Thiết kế bộ nhận diện thương hiệu và ấn phẩm truyền thông số đa kênh."],
        "Biến những bức ảnh chụp thô sơ thành tác phẩm nghệ thuật đồ họa làm say đắm người xem!",
        "Chỉnh sửa ảnh chuyên nghiệp: Cân bằng trắng (White Balance), khử nhiễu hạt (Denoise), điều chỉnh sắc độ RGB qua đồ thị Curves. Kỹ thuật tách chủ thể phức tạp (tóc, viền lông thú) bằng mặt nạ lớp (Layer Mask) kết hợp chế độ hòa trộn Blending Modes.",
        ["Layer Mask: Màu trắng hiển thị, màu đen che giấu (không phá hủy ảnh gốc).", "Xuất file chuẩn in ấn CMYK (300 DPI) và chuẩn màn hình RGB (72/144 DPI)."],
        {"groups": [{"id": "g1", "name": "Kỹ thuật Chỉnh màu Nâng cao"}, {"id": "g2", "name": "Kỹ thuật Tách nền & Ghép ảnh"}], "items": [{"id":"1","name":"Điều chỉnh dải sáng tối qua đồ thị Curves","group":"g1","icon":"📈"},{"id":"2","name":"Cân chỉnh nhiệt độ màu Color Balance","group":"g1","icon":"🌡️"},{"id":"3","name":"Mặt nạ lớp Layer Mask không phá hủy điểm ảnh","group":"g2","icon":"🎭"},{"id":"4","name":"Hòa trộn lớp ánh sáng phơi sáng Overlay/Multiply","group":"g2","icon":"✨"}]},
        [{"question": "Trong kỹ thuật sử dụng Mặt nạ lớp (Layer Mask), vùng được tô màu ĐEN trên mặt nạ sẽ có tác dụng gì?", "options": ["Che giấu (làm trong suốt) phần hình ảnh đó trên lớp", "Làm phần ảnh đó sáng rực lên", "Xóa vĩnh viễn tệp ảnh gốc"], "answer": 0, "explanation": "Quy tắc kinh điển của Layer Mask: Màu đen che giấu (ẩn đi), màu trắng hiển thị."}],
        "Tay nghề đồ họa và xử lý hình ảnh đa phương tiện của em rất điêu luyện!"
    ))

    nodes.append(make_lesson(
        "G11-13", "w3", 11, "Quản trị Hệ điều hành & Bảng tính Phân tích Nâng cao", "Chủ đề ICT: Tin học ứng dụng",
        "Chuyên đề ICT 11: Hệ điều hành & Bảng tính nâng cao", "Chuyên đề ICT 11: Bảng tính phân tích số liệu", "Chuyên đề ICT 11: Bảng tính chuyên sâu",
        "sort-drag", ["G11-03"], 8,
        ["Sử dụng bảng tổng hợp phân tích đa chiều Pivot Table trong Excel.", "Các hàm tìm kiếm nâng cao: VLOOKUP, XLOOKUP, INDEX & MATCH."],
        "Tổng hợp và phân tích hàng trăm ngàn giao dịch kinh doanh chỉ trong 3 cú click chuột với Pivot Table!",
        "Pivot Table là công cụ phân tích dữ liệu quyền năng nhất của bảng tính: tự động gom nhóm, tính tổng, tính trung bình theo nhiều chiều tiêu chí mà không cần viết công thức phức tạp. Hàm XLOOKUP hiện đại tìm kiếm linh hoạt cả bên trái và bên phải, thay thế hoàn toàn cho VLOOKUP cũ.",
        ["Kỹ thuật xác thực dữ liệu đầu vào (Data Validation) tạo danh sách chọn thả xuống.", "Thiết lập định dạng có điều kiện (Conditional Formatting) tô màu trực quan số liệu."],
        {"groups": [{"id": "g1", "name": "Công cụ Phân tích Đa chiều"}, {"id": "g2", "name": "Hàm Tra cứu Dữ liệu Nâng cao"}], "items": [{"id":"1","name":"Bảng tổng hợp động Pivot Table kéo thả","group":"g1","icon":"📊"},{"id":"2","name":"Biểu đồ phân tích động Pivot Chart","group":"g1","icon":"📈"},{"id":"3","name":"Hàm tra cứu hiện đại XLOOKUP đa hướng","group":"g2","icon":"🔎"},{"id":"4","name":"Bộ đôi hàm tra cứu ma trận INDEX & MATCH","group":"g2","icon":"🎯"}]},
        [{"question": "Công cụ nào trong bảng tính Excel cho phép kéo thả để tổng hợp, gom nhóm và tính toán hàng chục ngàn dòng số liệu thành báo cáo đa chiều trong vài giây?", "options": ["Pivot Table", "Công cụ Paint", "Công cụ WordArt"], "answer": 0, "explanation": "Pivot Table là công cụ số 1 thế giới về tổng hợp phân tích dữ liệu bảng tính."}],
        "Kỹ năng phân tích số liệu kinh doanh của em đạt đẳng cấp chuyên viên phân tích dữ liệu cao cấp!"
    ))

    nodes.append(make_lesson(
        "G11-14", "w3", 11, "Đấu trường Trùm Lớp 11: Bậc Thầy CSDL SQL & Thuật toán", "Tổng kết GDPT 2018 Lớp 11",
        "Bài CS-16: Dự án CSDL & Tổng kết Tin học 11", "Bài CS-16: Dự án phần mềm & Đánh giá năng lực 11", "Bài CS-16: Hệ thống quản lý điểm thi & Tổng kết",
        "boss-quiz", ["G11-01", "G11-03", "G11-05", "G11-09", "G11-10"], 15,
        ["Tổng kết toàn diện chuẩn năng lực Tin học Lớp 11 cả 2 nhánh CS & ICT của 3 bộ sách.", "Sẵn sàng nhận danh hiệu Bậc Thầy CSDL SQL & Thuật Toán Tối Ưu EasyTin."],
        "Trùm Dữ Liệu 'Database Destroyer' đang muốn xóa sổ toàn bộ cơ sở dữ liệu quốc gia! Hãy dùng các câu lệnh SQL và Thuật toán tối ưu để phong ấn nó!",
        "Đấu trường đỉnh cao tổng hợp: CSDL quan hệ, Khóa chính, SQL SELECT / WHERE / GROUP BY / JOIN, Đệ quy, Merge Sort, Quick Sort và Big-O.",
        ["SQL INNER JOIN, GROUP BY, HAVING.", "Độ phức tạp thuật toán O(N log N) và chuẩn hóa CSDL 3NF."],
        {"boss_name": "Database Destroyer Trùm Dữ Liệu", "boss_max_hp": 100, "player_max_hp": 100, "damage_per_hit": 25, "questions_pool": 4},
        [
            {"question": "Mệnh đề nào trong SQL dùng để gom nhóm các bản ghi có cùng giá trị lại để thực hiện các phép tính tổng hợp (như COUNT, SUM, AVG)?", "options": ["GROUP BY", "ORDER BY", "WHERE", "SELECT"], "answer": 0, "explanation": "GROUP BY là mệnh đề chuẩn để gom nhóm dữ liệu trong SQL."},
            {"question": "Thuật toán sắp xếp nào sau đây có độ phức tạp thời gian trung bình là O(N log N) và sắp xếp tại chỗ (In-place)?", "options": ["Quick Sort (Sắp xếp nhanh)", "Bubble Sort (Sắp xếp nổi bọt)", "Selection Sort (Sắp xếp chọn)", "Linear Search"], "answer": 0, "explanation": "Quick Sort đạt O(N log N) và sắp xếp tại chỗ không tốn bộ nhớ phụ."},
            {"question": "Trong thiết kế CSDL, khóa ngoại (Foreign Key) có vai trò cốt lõi là gì?", "options": ["Tạo liên kết và bảo đảm ràng buộc toàn vẹn tham chiếu giữa hai bảng", "Tăng tốc độ khởi động máy tính", "Làm đẹp giao diện người dùng", "Khóa máy tính khi hết giờ"], "answer": 0, "explanation": "Khóa ngoại liên kết hai bảng và bảo vệ tính toàn vẹn tham chiếu dữ liệu."},
            {"question": "Công cụ nào trong phần mềm Excel dùng để tra cứu dữ liệu linh hoạt cả về phía trước và phía sau mà không bị giới hạn cột đầu tiên?", "options": ["Hàm XLOOKUP", "Hàm SUM", "Hàm MIN", "Hàm NOW"], "answer": 0, "explanation": "XLOOKUP là hàm tra cứu hiện đại, khắc phục toàn bộ nhược điểm của VLOOKUP."}
        ],
        "CHIẾN CÔNG HIỂN HÁCH! Em đã tiêu diệt Database Destroyer và xuất sắc hoàn thành toàn bộ chương trình Tin học Lớp 11 của cả 3 bộ sách KNTT, Cánh Diều, CTST!"
    ))

    # =========================================================================
    # LỚP 12 (15 NÚT - THẾ GIỚI 3: ĐỈNH CAO CÔNG NGHỆ)
    # =========================================================================
    nodes.append(make_lesson(
        "G12-01", "w3", 12, "Mô hình OSI 7 tầng & Kiến trúc Phân tầng TCP/IP", "Chủ đề Mạng máy tính nâng cao",
        "Bài 1: Mô hình OSI và bộ giao thức TCP/IP", "Bài 1: Kiến trúc mạng máy tính hiện đại", "Bài 1: Kiến trúc mạng & Mô hình phân tầng",
        "sort-drag", ["G10-02"], 8,
        ["Hiểu 7 tầng của mô hình tham chiếu OSI và 4 tầng của bộ giao thức Internet TCP/IP.", "Cơ chế đóng gói dữ liệu (Encapsulation) từ Tầng ứng dụng xuống Tầng vật lý."],
        "Mỗi bức ảnh em gửi qua mạng được xé nhỏ thành hàng ngàn gói tin, dán nhãn địa chỉ và bay qua nửa vòng Trái Đất!",
        "Mô hình OSI: Tầng Vật lý -> Liên kết dữ liệu -> Mạng -> Giao vận -> Phiên -> Trình diễn -> Ứng dụng. Kiến trúc TCP/IP thực tế gồm 4 tầng: Tầng truy nhập mạng (Network Access), Tầng Internet (giao thức IP), Tầng giao vận (TCP/UDP) và Tầng ứng dụng (HTTP, HTTPS, DNS, FTP).",
        ["Cơ chế đóng gói: Mỗi tầng thêm tiêu đề (Header) chứa thông tin điều khiển riêng.", "Giao thức IP chịu trách nhiệm định địa chỉ, giao thức TCP đảm bảo truyền tin cậy."],
        {"groups": [{"id": "g1", "name": "Tầng Ứng dụng & Giao vận (Application & Transport)"}, {"id": "g2", "name": "Tầng Mạng & Truy nhập (Internet & Network Access)"}], "items": [{"id":"1","name":"Giao thức truyền siêu văn bản an toàn HTTPS","group":"g1","icon":"🔒"},{"id":"2","name":"Giao thức giao vận tin cậy bắt tay 3 bước TCP","group":"g1","icon":"🤝"},{"id":"3","name":"Giao thức định tuyến địa chỉ Internet (IPv4/IPv6)","group":"g2","icon":"🏷️"},{"id":"4","name":"Khung tin dữ liệu phần cứng địa chỉ MAC (Ethernet)","group":"g2","icon":"🌐"}]},
        [{"question": "Trong kiến trúc mạng TCP/IP, giao thức nào ở tầng Giao vận chịu trách nhiệm truyền dữ liệu tin cậy, bảo đảm không bị mất gói tin và đúng thứ tự?", "options": ["Giao thức TCP", "Giao thức UDP", "Giao thức IP"], "answer": 0, "explanation": "TCP (Transmission Control Protocol) là giao thức kết nối tin cậy có kiểm soát lỗi."}],
        "Em đã nắm vững cấu trúc phân tầng vi diệu của mạng Internet toàn cầu!"
    ))

    nodes.append(make_lesson(
        "G12-02", "w3", 12, "Địa chỉ IPv4, IPv6, Subnetting & Hệ thống DNS", "Chủ đề Mạng máy tính nâng cao",
        "Bài 2: Địa chỉ IP và phân giải tên miền", "Bài 2: Định tuyến & Giao thức truyền thông", "Bài 2: Địa chỉ IP & Định tuyến dữ liệu",
        "logic-puzzle", ["G12-01"], 8,
        ["Cấu trúc địa chỉ IPv4 (32-bit: 4 octet) và IPv6 (128-bit: 8 nhóm hex).", "Hệ thống phân giải tên miền DNS (Domain Name System) chuyển đổi tên miền dạng chữ thành địa chỉ IP số."],
        "DNS chính là cuốn danh bạ điện thoại khổng lồ của toàn bộ mạng Internet!",
        "Địa chỉ IPv4 có độ dài 32 bit, chia thành Network ID và Host ID thông qua Subnet Mask (ví dụ: 192.168.1.1/24). Do cạn kiệt IPv4, thế giới đang chuyển dịch sang IPv6 (128 bit, cung cấp hàng tỷ tỷ địa chỉ cho mọi hạt bụi). Máy chủ DNS dịch tên miền dễ nhớ (easytin.vn) thành địa chỉ IP số để thiết bị tìm đến nhau.",
        ["Địa chỉ IP riêng tư (Private IP): 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.", "Truy vấn DNS đệ quy từ Root DNS Server -> TLD Server -> Authoritative Server."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [4, 9, 14]},
        [{"question": "Hệ thống nào trên mạng Internet đóng vai trò như cuốn danh bạ chuyển đổi tên miền dạng chữ (như google.com) sang địa chỉ IP dạng số?", "options": ["Hệ thống phân giải tên miền DNS (Domain Name System)", "Giao thức DHCP", "Tường lửa Firewall"], "answer": 0, "explanation": "DNS là dịch vụ chuyển đổi tên miền thân thiện thành địa chỉ IP mà máy tính hiểu được."}],
        "Em đã thấu hiểu nguyên lý định danh và phân dải địa chỉ trên Internet!"
    ))

    nodes.append(make_lesson(
        "G12-03", "w3", 12, "Thiết bị Switch, Router & Định tuyến Gói tin", "Chủ đề Mạng máy tính nâng cao",
        "Bài 3: Thiết bị mạng & Định tuyến gói tin", "Bài 3: Quản trị thiết bị mạng", "Bài 3: Thiết bị mạng chuyên dụng",
        "sort-drag", ["G12-02"], 8,
        ["Phân biệt cơ chế chuyển tiếp của Switch (tầng 2: Bảng MAC) và Router (tầng 3: Bảng định tuyến Routing Table).", "Giao thức cấp phát địa chỉ IP động DHCP (Dynamic Host Configuration Protocol)."],
        "Người điều phối giao thông tài ba đưa các gói tin vượt qua hàng chục nghìn km cáp quang ngầm dưới đáy biển!",
        "Switch (Bộ chuyển mạch): hoạt động ở tầng Liên kết dữ liệu (Data Link), học và ghi nhớ địa chỉ MAC của từng máy tính cắm vào cổng để chuyển tiếp khung tin chính xác, không gây nghẽn mạng. Router (Bộ định tuyến): hoạt động ở tầng Mạng (Network), đọc địa chỉ IP đích và tra bảng định tuyến để gửi gói tin đi trên con đường tối ưu nhất.",
        ["Máy chủ DHCP tự động cấp phát địa chỉ IP, Subnet Mask, Default Gateway cho thiết bị mới kết nối.", "NAT (Network Address Translation): chuyển đổi giữa dải IP riêng tư nội bộ và 1 IP công cộng."],
        {"groups": [{"id": "g1", "name": "Đặc trưng Bộ Chuyển mạch Switch (Tầng 2)"}, {"id": "g2", "name": "Đặc trưng Bộ Định tuyến Router (Tầng 3)"}], "items": [{"id":"1","name":"Chuyển tiếp khung tin dựa trên bảng địa chỉ vật lý MAC","group":"g1","icon":"🔀"},{"id":"2","name":"Tạo mạng nội bộ LAN kết nối các máy tính trong phòng","group":"g1","icon":"🏢"},{"id":"3","name":"Định tuyến gói tin giữa các mạng khác nhau dựa trên IP","group":"g2","icon":"🌐"},{"id":"4","name":"Tích hợp tính năng NAT chia sẻ Internet và DHCP","group":"g2","icon":"📡"}]},
        [{"question": "Thiết bị mạng nào hoạt động ở Tầng 3 (Network Layer) có chức năng tìm đường đi tối ưu để chuyển tiếp gói tin giữa các mạng khác nhau?", "options": ["Bộ định tuyến Router", "Bộ chuyển mạch Switch", "Hub"], "answer": 0, "explanation": "Router là thiết bị tầng 3 chuyên trách tìm đường và định tuyến các gói tin IP."}],
        "Em đã làm chủ kỹ năng cấu hình và nguyên lý định tuyến mạng chuyên nghiệp!"
    ))

    nodes.append(make_lesson(
        "G12-04", "w3", 12, "Nguy cơ An ninh Mạng: DDoS, SQL Injection & MitM", "Chủ đề An ninh mạng nâng cao",
        "Bài 4: Các nguy cơ và tấn công mạng", "Bài 4: Phòng chống tấn công mạng", "Bài 4: Kỹ thuật tấn công & Phòng chống",
        "branch-story", ["G12-03"], 8,
        ["Nhận diện bản chất các cuộc tấn công mạng nguy hiểm: Tấn công từ chối dịch vụ phân tán (DDoS), Tấn công chèn mã SQL Injection, Tấn công trung gian (Man-in-the-Middle).", "Nguyên tắc phòng thủ theo chiều sâu (Defense in Depth)."],
        "Chiến trường vô hình khốc liệt nhất hành tinh: Cuộc chiến giữa các chiến binh bảo mật và tin tặc mũ đen!",
        "Tấn công DDoS: sử dụng mạng máy tính ma (Botnet) gồm hàng triệu thiết bị IoT bị nhiễm mã độc gửi đồng loạt hàng tỷ yêu cầu rác làm sập máy chủ mục tiêu. SQL Injection: kẻ xấu chèn các câu lệnh SQL độc hại vào ô nhập liệu để đánh cắp toàn bộ cơ sở dữ liệu. Man-in-the-Middle (MitM): nghe lén và đánh cắp dữ liệu trên mạng Wi-Fi công cộng không có mã hóa.",
        ["Sử dụng Prepared Statements / Parameterized Queries để diệt sạch lỗi SQL Injection.", "Không bao giờ giao dịch ngân hàng trên mạng Wi-Fi công cộng mở."],
        {"scenarios": [{"id": "s1", "prompt": "Một hệ thống bán hàng trực tuyến bị sập do hacker chèn dòng mã ' OR '1'='1 vào ô đăng nhập mật khẩu để đăng nhập thành công vào tài khoản Quản trị Admin.", "choices": [{"text": "Hệ thống đã bị tấn công chèn mã SQL Injection -> Cần viết lại câu truy vấn sử dụng cơ chế tham số hóa dữ liệu Prepared Statements.", "is_correct": True, "feedback": "Rất chuẩn mực! Prepared Statements giúp vô hiệu hóa hoàn toàn SQL Injection."}, {"text": "Tăng thêm dung lượng RAM cho máy chủ.", "is_correct": False, "feedback": "Sai lầm! Đây là lỗ hổng bảo mật mã nguồn, thêm RAM không giải quyết được lỗ hổng!"}]}]},
        [{"question": "Hình thức tấn công mạng nào sử dụng hàng vạn máy tính ma (Botnet) cùng gửi yêu cầu ồ ạt để làm tê liệt máy chủ nạn nhân?", "options": ["Tấn công từ chối dịch vụ phân tán (DDoS)", "Tấn công lừa đảo Phishing", "Nhiễm virus màn hình"], "answer": 0, "explanation": "DDoS làm cạn kiệt tài nguyên băng thông và CPU của máy chủ mục tiêu."}],
        "Em đã trang bị kiến thức phân tích lỗ hổng và phòng thủ mạng vững như bàn thạch!"
    ))

    nodes.append(make_lesson(
        "G12-05", "w3", 12, "Tường lửa, Mã hóa HTTPS & Giao thức SSL/TLS", "Chủ đề An ninh mạng nâng cao",
        "Bài 5: Các giải pháp phòng thủ an ninh số", "Bài 5: Bảo vệ hệ thống thông tin", "Bài 5: Tường lửa & Bảo mật hệ thống",
        "sort-drag", ["G12-04"], 8,
        ["Hiểu chức năng của Tường lửa (Firewall): lọc gói tin theo luật (Rules: IP, Port, Protocol).", "Nguyên lý mã hóa bất đối xứng (Khóa công khai & Khóa bí mật) trong giao thức HTTPS / SSL / TLS."],
        "Mọi thông tin mật khẩu và số thẻ ngân hàng của em khi gửi qua web đều được mã hóa thành các ký tự xáo trộn không thể giải mã!",
        "Tường lửa (Firewall) đóng vai trò người gác cổng kiểm tra mọi gói tin đi vào/đi ra dựa trên tập luật (Rule). Giao thức HTTPS (chạy trên cổng 443) sử dụng chứng chỉ số SSL/TLS và mật mã học bất đối xứng: dùng Khóa công khai (Public Key) để mã hóa dữ liệu và Khóa bí mật (Private Key) để giải mã, bảo đảm kẻ nghe lén trên đường truyền không thể đọc được nội dung.",
        ["Hệ thống phát hiện xâm nhập IDS (Intrusion Detection System) cảnh báo dấu hiệu bất thường.", "Mô hình bảo mật Zero Trust: Không tin tưởng bất kỳ ai, luôn luôn xác thực."],
        {"groups": [{"id": "g1", "name": "Giải pháp Tường lửa (Firewall Rules)"}, {"id": "g2", "name": "Công nghệ Mã hóa Kênh truyền (SSL/TLS)"}], "items": [{"id":"1","name":"Chặn cổng mạng nguy hiểm Port 23 (Telnet không mã hóa)","group":"g1","icon":"🧱"},{"id":"2","name":"Chỉ cho phép dải IP nội bộ truy cập máy chủ CSDL","group":"g1","icon":"🛡️"},{"id":"3","name":"Giao thức HTTPS mã hóa dữ liệu với chứng chỉ SSL số","group":"g2","icon":"🔒"},{"id":"4","name":"Cặp khóa mật mã bất đối xứng Public Key & Private Key","group":"g2","icon":"🔑"}]},
        [{"question": "Cổng dịch vụ chuẩn (Port) nào trên máy chủ web được sử dụng cho giao thức truyền siêu văn bản an toàn có mã hóa HTTPS?", "options": ["Cổng 443", "Cổng 80", "Cổng 21"], "answer": 0, "explanation": "Cổng 443 là cổng chuẩn quốc tế dành cho lưu lượng mã hóa HTTPS (cổng 80 là HTTP thường)."}],
        "Em đã thiết lập pháo đài an ninh số bất khả xâm phạm!"
    ))

    nodes.append(make_lesson(
        "G12-06", "w3", 12, "Tổng quan Trí tuệ Nhân tạo & Phép thử Turing", "Chủ đề Trí tuệ Nhân tạo (AI)",
        "Bài 6, 7: Tổng quan AI & Kỹ thuật nền tảng", "Bài 6, 7: Khám phá AI & Ứng dụng đột phá", "Bài 6, 7: Trí tuệ nhân tạo & Ứng dụng",
        "match-memory", ["G11-11"], 8,
        ["Lịch sử hình thành AI: Phép thử Turing (Turing Test) năm 1950 của Alan Turing.", "Phân biệt 3 cấp độ AI: AI hẹp (Narrow AI), AI tổng quát (AGI) và Siêu trí tuệ (Super AI)."],
        "Cỗ máy có thể suy nghĩ như con người không? Câu hỏi lịch sử làm thay đổi vận mệnh của nền văn minh nhân loại!",
        "Trí tuệ nhân tạo (AI) là ngành khoa học máy tính nghiên cứu tạo ra các cỗ máy có khả năng thực hiện các nhiệm vụ đòi hỏi trí thông minh của con người (nhận thức thị giác, nhận dạng tiếng nói, ra quyết định, dịch thuật). Phép thử Turing: nếu người đánh giá trò chuyện qua bàn phím mà không thể phân biệt được đâu là con người, đâu là cỗ máy thì máy tính đó vượt qua phép thử.",
        ["Narrow AI (AI hẹp): giỏi một nhiệm vụ chuyên biệt (chơi cờ, nhận diện mặt, lái xe). Tất cả AI hiện nay đều là Narrow AI.", "AGI (Artificial General Intelligence): AI tổng quát có trí tuệ toàn diện ngang bằng con người."],
        {"cards": [{"id":"1","name":"Phép thử Turing (Turing Test)","match":"Tiêu chuẩn đánh giá cỗ máy có biểu hiện hành vi thông minh như con người"},{"id":"2","name":"AI hẹp (Narrow AI)","match":"Hệ thống AI chuyên biệt cho một bài toán cụ thể (như AlphaGo chơi cờ)"},{"id":"3","name":"AI tổng quát (AGI)","match":"Trí tuệ nhân tạo có khả năng học tập và suy luận ngang bằng trí não con người"},{"id":"4","name":"Alan Turing","match":"Nhà toán học thiên tài người Anh, cha đẻ của khoa học máy tính và AI"}]},
        [{"question": "Hệ thống trí tuệ nhân tạo hiện nay (như trợ lý ảo, xe tự hành, cờ vây) thuộc cấp độ AI nào?", "options": ["AI hẹp (Narrow AI / Weak AI)", "Siêu trí tuệ nhân tạo (Super AI)", "AI đã có cảm xúc con người"], "answer": 0, "explanation": "Toàn bộ AI hiện nay đều là AI hẹp, chỉ giải quyết xuất sắc một lĩnh vực chuyên biệt."}],
        "Em đã nắm vững lịch sử và các nấc thang tiến hóa của Trí tuệ nhân tạo!"
    ))

    nodes.append(make_lesson(
        "G12-07", "w3", 12, "Ba Nhánh Học máy (Machine Learning) Cốt lõi", "Chủ đề Trí tuệ Nhân tạo (AI)",
        "Bài 8: Nhập môn Học máy (Machine Learning)", "Bài 8: Các phương pháp Học máy cơ bản", "Bài 8: Các kỹ thuật Học máy",
        "sort-drag", ["G12-06"], 8,
        ["Hiểu cơ chế: Thay vì viết từng dòng lệnh quy tắc cứng, ta nạp dữ liệu để máy tính tự học các quy luật.", "Phân biệt 3 nhánh học máy: Học có giám sát (Supervised), Học không giám sát (Unsupervised), Học tăng cường (Reinforcement Learning)."],
        "Dạy cỗ máy khả năng tự học từ kinh nghiệm giống như cách một đứa trẻ lớn lên và khám phá thế giới!",
        "Học có giám sát: Dữ liệu huấn luyện đã được con người gắn nhãn (Label). Ví dụ bài toán Phân loại (ảnh Chó hay Mèo) và Hồi quy (dự đoán giá nhà). Học không giám sát: Dữ liệu chưa có nhãn, thuật toán tự tìm ra các cụm cấu trúc ẩn (Clustering). Học tăng cường: Tác nhân (Agent) tự học thông qua thử - sai trong môi trường để tối đa hóa phần thưởng (Reward), ví dụ robot tập đi, AI chơi game Mario.",
        ["Học máy (ML) là tập con của AI.", "Chất lượng của mô hình phụ thuộc sống còn vào chất lượng của dữ liệu huấn luyện."],
        {"groups": [{"id": "g1", "name": "Học có Giám sát (Dữ liệu đã gắn nhãn)"}, {"id": "g2", "name": "Học không Giám sát & Tăng cường"}], "items": [{"id":"1","name":"Nhận diện biển số xe (Ảnh kèm nhãn số đúng)","group":"g1","icon":"🏷️"},{"id":"2","name":"Dự đoán giá bán cổ phiếu theo thời gian","group":"g1","icon":"📈"},{"id":"3","name":"Tự động phân khúc 1 triệu khách hàng theo thói quen","group":"g2","icon":"👥"},{"id":"4","name":"Robot tự học giữ thăng bằng qua phần thưởng thưởng phạt","group":"g2","icon":"🤖"}]},
        [{"question": "Trong học máy, bài toán huấn luyện mô hình dự đoán email là 'Thư rác' hay 'Hộp thư đến' dựa trên tập email đã được người dùng đánh dấu trước thuộc nhánh học nào?", "options": ["Học có giám sát (Supervised Learning)", "Học không giám sát", "Học tăng cường"], "answer": 0, "explanation": "Dữ liệu có gắn nhãn sẵn (Spam/Inbox) là đặc trưng cốt lõi của Học có giám sát."}],
        "Em đã phân định rạch ròi 3 trụ cột của công nghệ Học máy hiện đại!"
    ))

    nodes.append(make_lesson(
        "G12-08", "w3", 12, "Dữ liệu Huấn luyện & Hiện tượng Quá khớp (Overfitting)", "Chủ đề Trí tuệ Nhân tạo (AI)",
        "Bài 9: Dữ liệu huấn luyện và mô hình", "Bài 9: Đánh giá độ chính xác mô hình", "Bài 9: Huấn luyện mô hình và kiểm thử",
        "bug-hunt", ["G12-07"], 8,
        ["Quy trình chia dữ liệu: Tập huấn luyện (Train Set: 80%) và Tập kiểm thử (Test Set: 20%).", "Hiểu hiện tượng Quá khớp (Overfitting - học vẹt) và Dưới khớp (Underfitting)."],
        "Hiện tượng 'học vẹt' trong máy tính: Học thuộc lòng đáp án bộ đề cũ nhưng đi thi gặp đề mới thì làm sai bét!",
        "Overfitting (Quá khớp): mô hình ghi nhớ cả những chi tiết nhiễu của tập huấn luyện (độ chính xác trên Train set 100%), nhưng khi gặp dữ liệu thực tế mới lạ thì dự đoán rất tệ (độ chính xác trên Test set tụt dốc). Underfitting (Dưới khớp): mô hình quá đơn giản, không học được quy luật chung. Các chỉ số đo lường: Độ chính xác (Accuracy), Precision, Recall, F1-score.",
        ["Giải pháp chống Overfitting: Thu thập thêm dữ liệu, giảm bớt độ phức tạp mạng, dùng kỹ thuật Dropout và Regularization.", "Tuyệt đối không để dữ liệu kiểm thử rò rỉ vào quá trình huấn luyện."],
        {},
        [{"question": "Hiện tượng mô hình AI đạt độ chính xác gần 100% trên tập dữ liệu học (Training Data) nhưng lại dự đoán rất kém trên tập dữ liệu mới (Testing Data) được gọi là hiện tượng gì?", "options": ["Hiện tượng Quá khớp (Overfitting - học vẹt)", "Hiện tượng Dưới khớp (Underfitting)", "Lỗi tràn bộ nhớ"], "answer": 0, "explanation": "Overfitting là hiện tượng mô hình học vẹt chi tiết nhiễu, mất khả năng khái quát hóa."}],
        "Em đã làm chủ kỹ năng thẩm định và tối ưu hóa mô hình Học máy chuẩn khoa học dữ liệu!"
    ))

    nodes.append(make_lesson(
        "G12-09", "w3", 12, "Mạng Nơ-ron Nhân tạo & Học sâu (Deep Learning)", "Chủ đề Trí tuệ Nhân tạo (AI)",
        "Bài 10: Mạng nơ-ron và Học sâu", "Bài 10: Mạng nơ-ron và xử lý ngôn ngữ", "Bài 10: Mạng nơ-ron & Học sâu",
        "logic-puzzle", ["G12-08"], 8,
        ["Mô phỏng nơ-ron sinh học: Perceptron, Trọng số (Weights), Độ lệch (Bias), Hàm kích hoạt (Activation Function).", "Mạng nơ-ron sâu nhiều tầng ẩn và mạng tích chập CNN nhận diện hình ảnh."],
        "Mô phỏng mạng lưới 86 tỷ tế bào nơ-ron thần kinh trong bộ não con người bằng các phương trình toán học!",
        "Mỗi nơ-ron nhân tạo nhận các tín hiệu vào x, nhân với trọng số w tương ứng, cộng độ lệch b và đưa qua hàm kích hoạt phi tuyến (ReLU, Sigmoid). Học sâu (Deep Learning) sử dụng mạng nơ-ron có hàng chục đến hàng trăm lớp ẩn (Hidden Layers), có khả năng tự động trích xuất các đặc trưng phức tạp từ ảnh, âm thanh thô.",
        ["Thuật toán Lan truyền ngược (Backpropagation) điều chỉnh trọng số w để giảm thiểu sai số.", "Mạng CNN (Convolutional Neural Network) là vua trong lĩnh vực thị giác máy tính."],
        {"bits_count": 4, "weights": [8, 4, 2, 1], "target_values": [5, 10, 15]},
        [{"question": "Thuật toán kinh điển nào được sử dụng trong Học sâu (Deep Learning) để tính toán đạo hàm sai số và điều chỉnh trọng số của các nơ-ron theo chiều ngược lại từ đầu ra về đầu vào?", "options": ["Thuật toán Lan truyền ngược (Backpropagation)", "Thuật toán sắp xếp nhanh QuickSort", "Thuật toán tìm kiếm nhị phân"], "answer": 0, "explanation": "Backpropagation là hòn đá tảng giúp huấn luyện mạng nơ-ron nhiều lớp."}],
        "Em đã giải mã bí ẩn toán học của mạng nơ-ron nhân tạo và công nghệ Học sâu!"
    ))

    nodes.append(make_lesson(
        "G12-10", "w3", 12, "Mô hình Ngôn ngữ Lớn (LLM) & Generative AI", "Chủ đề Trí tuệ Nhân tạo (AI)",
        "Bài 11: Mô hình ngôn ngữ lớn & GenAI", "Bài 11: AI tạo sinh và tương lai", "Bài 11: AI tạo sinh & Ứng dụng",
        "branch-story", ["G12-09"], 8,
        ["Nguyên lý kiến trúc Transformer và cơ chế tự chú ý (Self-Attention).", "Hiểu cách thức Generative AI sinh văn bản, hình ảnh, mã nguồn và kỹ năng viết lời nhắc Prompt Engineering."],
        "Cơn địa chấn công nghệ toàn cầu: Khi cỗ máy có thể sáng tác thơ, vẽ tranh và lập trình phần mềm như con người!",
        "Mô hình ngôn ngữ lớn (LLM: GPT-4, Gemini) được huấn luyện trên hàng nghìn tỷ từ ngữ từ kho tri thức nhân loại. Cơ chế Attention giúp mô hình nắm bắt mối quan hệ ngữ cảnh giữa các từ xa nhau trong câu. Kỹ thuật Prompt Engineering: Cung cấp vai trò (Role), bối cảnh (Context), hướng dẫn rõ ràng (Instructions) và ví dụ (Examples) để AI đưa ra câu trả lời xuất sắc nhất.",
        ["Hiện tượng 'Ảo giác AI' (Hallucination): AI tự bịa ra thông tin sai sự thật một cách rất tự tin.", "Luôn kiểm chứng lại kết quả của AI trước khi đưa vào sử dụng thực tế."],
        {"scenarios": [{"id": "s1", "prompt": "Em cần tạo một kịch bản video học tập ngắn bằng công cụ Generative AI.", "choices": [{"text": "Viết Prompt rõ ràng: Đóng vai chuyên gia giáo dục, viết kịch bản 3 phút cho học sinh lớp 12, nêu 3 ví dụ thực tế và kiểm chứng lại thông tin AI tạo ra.", "is_correct": True, "feedback": "Kỹ năng Prompting đỉnh cao! Kết quả trả về sẽ rất sâu sắc và chuẩn xác."}, {"text": "Chỉ gõ cộc lốc một từ: 'Viết bài' rồi sao chép nguyên văn nộp cho thầy cô mà không đọc lại.", "is_correct": False, "feedback": "Kết quả sẽ rất sơ sài và có thể chứa các thông tin ảo giác sai lệch!"}]}]},
        [{"question": "Hiện tượng mô hình ngôn ngữ lớn (LLM) tạo ra các thông tin hoàn toàn sai sự thật nhưng diễn đạt rất tự tin và trôi chảy được gọi là hiện tượng gì?", "options": ["Ảo giác AI (Hallucination)", "Lỗi cú pháp SyntaxError", "Lỗi tràn bộ nhớ Stack Overflow"], "answer": 0, "explanation": "Hallucination là thách thức lớn nhất hiện nay của các mô hình Generative AI."}],
        "Em đã nắm vững nghệ thuật làm chủ công nghệ Trí tuệ nhân tạo tạo sinh!"
    ))

    nodes.append(make_lesson(
        "G12-11", "w3", 12, "Đạo đức AI, Thiên kiến Thuật toán & Trách nhiệm", "Chủ đề Trí tuệ Nhân tạo (AI)",
        "Bài 12: Đạo đức AI và trách nhiệm xã hội", "Bài 12: Trách nhiệm & Đạo đức kỷ nguyên số", "Bài 12: Đạo đức trong kỷ nguyên AI",
        "branch-story", ["G12-10"], 8,
        ["Nhận diện thiên kiến thuật toán (Algorithmic Bias) bắt nguồn từ dữ liệu lịch sử con người.", "Vấn đề bản quyền tác phẩm sáng tạo bởi AI và nguy cơ công nghệ Deepfake mạo danh lừa đảo."],
        "Công nghệ là công cụ, đạo đức của con người là kim chỉ nam quyết định tương lai của nền văn minh!",
        "AI học từ dữ liệu quá khứ của con người, nếu dữ liệu có sẵn định kiến phân biệt giới tính, màu da hay tôn giáo, AI sẽ học theo và khuếch đại định kiến đó. Công nghệ Deepfake giả mạo giọng nói, khuôn mặt video đang bị tội phạm dùng để lừa đảo chiếm đoạt tài sản. Con người phải luôn giữ vai trò kiểm soát cuối cùng (Human-in-the-loop).",
        ["Tính minh bạch và khả năng giải trình (Explainable AI - XAI).", "Bảo vệ bản quyền nghệ sĩ: không tự tiện dùng tranh ảnh của họa sĩ để huấn luyện AI thương mại khi chưa xin phép."],
        {"scenarios": [{"id": "s1", "prompt": "Một hệ thống AI chấm điểm tín dụng ngân hàng tự động từ chối cho vay đối với tất cả phụ nữ do dữ liệu huấn luyện lịch sử 30 năm trước chủ yếu là nam giới vay vốn.", "choices": [{"text": "Đây là thiên kiến thuật toán (Algorithmic Bias) nghiêm trọng -> Cần làm sạch, cân bằng lại dữ liệu huấn luyện và thiết lập quy tắc công bằng đạo đức.", "is_correct": True, "feedback": "Rất công bằng và tiến bộ! Đạo đức AI bảo vệ quyền lợi bình đẳng của mọi công dân."}, {"text": "Chấp nhận vì máy tính AI luôn luôn công tâm tuyệt đối.", "is_correct": False, "feedback": "Sai lầm! Máy tính học từ dữ liệu có thiên kiến nên đã tạo ra sự bất công xã hội!"}]}]},
        [{"question": "Thiên kiến thuật toán (Algorithmic Bias) trong các mô hình AI thường bắt nguồn từ nguyên nhân chủ yếu nào?", "options": ["Dữ liệu huấn luyện lịch sử phản ánh những định kiến sẵn có của con người trong quá khứ", "Do máy tính tự ghét con người", "Do tốc độ mạng Internet chập chờn"], "answer": 0, "explanation": "Dữ liệu huấn luyện phản ánh định kiến xã hội dẫn đến mô hình AI học theo các sai lệch đó."}],
        "Em là một nhà lãnh đạo công nghệ có lương tri và trách nhiệm đạo đức cao cả!"
    ))

    nodes.append(make_lesson(
        "G12-12", "w3", 12, "Xây dựng Cấu trúc Trang Web Ngữ nghĩa (HTML5)", "Chủ đề Lập trình Web hiện đại",
        "Bài 13: Ngôn ngữ HTML5 và cấu trúc web", "Bài 13: Xây dựng cấu trúc web với HTML", "Bài 13: Cấu trúc tài liệu web HTML5",
        "type-run", ["G10-06"], 8,
        ["Cấu trúc tài liệu chuẩn HTML5: <!DOCTYPE html>, <html>, <head>, <body>.", "Sử dụng các thẻ ngữ nghĩa (Semantic HTML): <header>, <nav>, <section>, <article>, <aside>, <footer>."],
        "HTML5 chính là bộ xương vững chắc tạo nên hàng tỷ trang web trên mạng Internet toàn cầu!",
        "Các thẻ ngữ nghĩa giúp công cụ tìm kiếm Google và các thiết bị đọc màn hình cho người khiếm thị hiểu rõ cấu trúc bài viết: <header> phần đầu trang, <nav> thanh điều hướng thực đơn, <main> nội dung chính, <section> phân đoạn chuyên đề, <footer> chân trang bản quyền. Thẻ biểu mẫu <form> thu thập dữ liệu người dùng qua các trường <input>, <select>, <button>.",
        ["Cặp thẻ đóng mở: <tag>Nội dung</tag>, thẻ tự đóng: <img src=\"...\" alt=\"...\" />.", "Thuộc tính id là duy nhất trong trang, thuộc tính class dùng chung cho nhiều phần tử."],
        {"words": ["header", "article", "section", "footer"]},
        [{"question": "Thẻ ngữ nghĩa (Semantic Tag) nào trong HTML5 dùng để biểu diễn thanh thực đơn điều hướng liên kết của trang web?", "options": ["<nav>", "<header>", "<menu_bar>"], "answer": 0, "explanation": "<nav> (viết tắt của Navigation) là thẻ chuẩn mực của HTML5 dành riêng cho thanh điều hướng."}],
        "Cấu trúc trang web HTML5 của em được xây dựng rất chuẩn ngữ nghĩa và tối ưu SEO!"
    ))

    nodes.append(make_lesson(
        "G12-13", "w3", 12, "Định kiểu Hiện đại với CSS3 Flexbox & Grid", "Chủ đề Lập trình Web hiện đại",
        "Bài 14: Định kiểu giao diện với CSS3", "Bài 14: Thiết kế giao diện hiện đại CSS", "Bài 14: Bố cục hiện đại CSS3 Flexbox",
        "sort-drag", ["G12-12"], 8,
        ["Mô hình hộp CSS Box Model: Margin (lề ngoài) -> Border (đường viền) -> Padding (vùng đệm) -> Content (nội dung).", "Thiết kế giao diện đáp ứng (Responsive Design) với CSS Flexbox và Media Queries thích ứng mọi màn hình."],
        "Biến bộ xương HTML thô kệch thành tác phẩm nghệ thuật giao diện lung linh, sống động!",
        "CSS (Cascading Style Sheets) định nghĩa diện mạo trang web: màu sắc, phông chữ, khoảng cách và bố cục. CSS Flexbox: căn chỉnh và phân bổ không gian cho các phần tử theo hàng ngang hoặc cột dọc linh hoạt. Media Queries: `@media (max-width: 768px)` giúp giao diện tự động co giãn từ màn hình máy tính lớn sang điện thoại nhỏ.",
        ["Độ ưu tiên CSS (Specificity): Inline style > ID selector > Class selector > Tag selector.", "CSS Grid: bố cục dạng lưới 2 chiều (hàng và cột) cho các trang web phức tạp."],
        {"groups": [{"id": "g1", "name": "Thành phần Mô hình Hộp (CSS Box Model)"}, {"id": "g2", "name": "Bố cục Linh hoạt (Responsive Flexbox)"}], "items": [{"id":"1","name":"Vùng đệm Padding nằm giữa nội dung và đường viền","group":"g1","icon":"📦"},{"id":"2","name":"Khoảng cách lề Margin nằm ngoài đường viền Border","group":"g1","icon":"📏"},{"id":"3","name":"Thiết lập display: flex căn chỉnh phần tử tự động co giãn","group":"g2","icon":"📐"},{"id":"4","name":"Quy tắc @media thích ứng màn hình điện thoại di động","group":"g2","icon":"📱"}]},
        [{"question": "Trong mô hình hộp CSS Box Model, khoảng cách nằm giữa nội dung (Content) và đường viền (Border) được gọi là gì?", "options": ["Padding (Vùng đệm trong)", "Margin (Lề ngoài)", "Outline"], "answer": 0, "explanation": "Padding là khoảng đệm bên trong đường viền của phần tử."}],
        "Giao diện trang web của em trông cực kỳ hiện đại, thẩm mỹ và thích ứng đa màn hình!"
    ))

    nodes.append(make_lesson(
        "G12-14", "w3", 12, "Lập trình Tương tác Động JavaScript & DOM", "Chủ đề Lập trình Web hiện đại",
        "Bài 15: Tương tác động với JavaScript", "Bài 15: Lập trình hành động JavaScript", "Bài 15: Tương tác người dùng qua DOM",
        "bug-hunt", ["G12-13"], 8,
        ["Hiểu mô hình đối tượng tài liệu DOM (Document Object Model).", "Bắt các sự kiện người dùng: click, submit, change bằng addEventListener và cập nhật nội dung động."],
        "Thổi linh hồn vào trang web: Biến những trang văn bản tĩnh thành ứng dụng tương tác thời gian thực đầy mê hoặc!",
        "JavaScript là ngôn ngữ lập trình của web. Trình duyệt chuyển đổi tài liệu HTML thành cây đối tượng DOM. JavaScript có thể: Tìm phần tử qua `document.querySelector()`, thay đổi nội dung qua `.textContent`, đổi kiểu dáng CSS qua `.style`, và lắng nghe hành động của người dùng qua `button.addEventListener('click', xuLy)`. Kiểm tra biểu mẫu nhập liệu (Form Validation) trước khi gửi lên máy chủ.",
        ["Biến số hiện đại: let (biến có thể gán lại), const (hằng số không thể gán lại).", "Giao tiếp bất đồng bộ fetch() gửi và nhận dữ liệu JSON từ máy chủ API."],
        {},
        [{"question": "Trong JavaScript, phương thức chuẩn nào dùng để đăng ký lắng nghe sự kiện khi người dùng nhấp chuột vào một nút bấm?", "options": ["element.addEventListener('click', hamXuLy)", "element.onClickNow()", "element.listenMouse()"], "answer": 0, "explanation": "addEventListener là phương thức chuẩn mực của W3C để xử lý các sự kiện DOM."}],
        "Em đã trở thành một kỹ sư phát triển web Full-Stack đầy bản lĩnh!"
    ))

    nodes.append(make_lesson(
        "G12-BOSS", "w3", 12, "ĐẠI CHIẾN BOSS TRÍ TUỆ NHÂN TẠO & CÔNG NGHỆ TOÀN CẦU", "Đỉnh cao GDPT 2018 Toàn diện",
        "Tổng kết Chuyên đề Tin học 12", "Tổng kết Chuyên đề Tin học 12", "Đấu trường Công nghệ EasyTin",
        "boss-quiz", ["G12-01", "G12-04", "G12-07", "G12-10", "G12-14"], 20,
        ["Tổng kết đỉnh cao toàn bộ 10 năm học Tin học phổ thông từ Lớp 3 đến Lớp 12 của cả 3 bộ sách KNTT, Cánh Diều, CTST.", "Vinh danh danh hiệu Huyền Thoại Công Nghệ Toàn Năng EasyTin."],
        "Trùm Cuối Vũ Trụ 'Glitch Titan the Destroyer' đang giải phóng làn sóng siêu virus muốn xóa sạch toàn bộ nền văn minh tri thức số của nhân loại! Hãy hợp nhất toàn bộ sức mạnh 10 năm học Tin học từ lớp 3 đến lớp 12 để cứu rỗi thế giới!",
        "Đấu trường tối thượng tổng kết: Kiến trúc máy tính Von Neumann, Hệ nhị phân, Mạng TCP/IP, An ninh mạng, CSDL quan hệ SQL, Thuật toán tối ưu Big-O, Học máy Machine Learning, Học sâu và Generative AI.",
        ["Phân tầng TCP/IP, Địa chỉ IPv4/IPv6, Tường lửa và HTTPS.", "Mô hình quan hệ RDBMS, SQL JOIN, Thuật toán O(N log N).", "Machine Learning, Overfitting, Transformer, Đạo đức AI và Phát triển Web."],
        {"boss_name": "Glitch Titan the Destroyer", "boss_max_hp": 100, "player_max_hp": 100, "damage_per_hit": 25, "questions_pool": 6},
        [
            {"question": "Trong mô hình học máy (Machine Learning), kỹ thuật chia tập dữ liệu thành Train Set và Test Set nhằm mục đích tối thượng nào?", "options": ["Đánh giá khả năng dự đoán của mô hình trên dữ liệu mới và phát hiện hiện tượng học vẹt (Overfitting)", "Làm cho máy tính chạy nhanh hơn", "Tiết kiệm dung lượng thẻ nhớ", "Để in ra giấy làm kỷ niệm"], "answer": 0, "explanation": "Tách biệt dữ liệu kiểm thử là nguyên tắc sống còn để đánh giá năng lực khái quát hóa của mô hình AI."},
            {"question": "Cơ chế nào trong kiến trúc Transformer cho phép mô hình ngôn ngữ lớn (LLM) cân nhắc đồng thời mối quan hệ ngữ cảnh giữa tất cả các từ trong câu?", "options": ["Cơ chế tự chú ý (Self-Attention)", "Cơ chế đệ quy tuần tự", "Cơ chế sắp xếp nổi bọt", "Cơ chế chia đôi nhị phân"], "answer": 0, "explanation": "Cơ chế Self-Attention là bước đột phá cách mạng của kiến trúc Transformer tạo nên ChatGPT, Gemini."},
            {"question": "Giao thức nào ở tầng Giao vận trong bộ giao thức TCP/IP thực hiện cơ chế bắt tay ba bước (3-way handshake) để thiết lập kết nối truyền tin cậy?", "options": ["Giao thức TCP", "Giao thức UDP", "Giao thức IP", "Giao thức ARP"], "answer": 0, "explanation": "TCP bắt tay 3 bước (SYN, SYN-ACK, ACK) để bảo đảm kết nối ổn định trước khi truyền dữ liệu."},
            {"question": "Trong cơ sở dữ liệu quan hệ, mệnh đề nào sau đây kết nối hai bảng dữ liệu dựa trên sự so khớp khóa chính và khóa ngoại?", "options": ["INNER JOIN ... ON ...", "SELECT ... FROM ...", "GROUP BY ... HAVING ...", "ORDER BY ... ASC ..."], "answer": 0, "explanation": "INNER JOIN là mệnh đề kết nối các bản ghi thỏa mãn điều kiện so khớp khóa."},
            {"question": "Luật An ninh mạng và các quy định pháp luật về bảo vệ dữ liệu cá nhân nghiêm cấm hành vi nào sau đây?", "options": ["Mua bán, phát tán thông tin dữ liệu cá nhân của người dân khi chưa được phép", "Học lập trình website", "Sử dụng phần mềm nguồn mở", "Sao lưu dữ liệu lên đám mây"], "answer": 0, "explanation": "Mua bán, phát tán dữ liệu cá nhân trái phép là hành vi phạm tội hình sự bị xử phạt nghiêm khắc."},
            {"question": "Độ phức tạp thời gian tốt nhất có thể đạt được của thuật toán tìm kiếm trên danh sách gồm N phần tử đã được sắp xếp trước là bao nhiêu?", "options": ["O(log N) bằng thuật toán Tìm kiếm nhị phân", "O(N) bằng tìm kiếm tuần tự", "O(N^2) bằng duyệt vét cạn", "O(1) trong mọi trường hợp"], "answer": 0, "explanation": "Binary search chia đôi phạm vi sau mỗi bước lặp nên đạt hiệu năng siêu tốc O(log N)."}
        ],
        "CHIẾN THẮNG HUY HOÀNG LỊCH SỬ! Em đã tiêu diệt hoàn toàn Glitch Titan, hoàn thành xuất sắc 100% toàn bộ chương trình Tin học phổ thông GDPT 2018 của cả 3 bộ sách Kết Nối Tri Thức, Cánh Diều, Chân Trời Sáng Tạo từ Lớp 3 đến Lớp 12 với danh xưng tối thượng: HUYỀN THOẠI CÔNG NGHỆ EASYTIN!"
    ))

    return nodes

print("curriculum_data_g10_g12 loaded")
