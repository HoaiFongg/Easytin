# -*- coding: utf-8 -*-
"""
Công cụ bổ sung và chuẩn hoá cấu trúc Sư phạm toàn diện (Lí thuyết + Trò chơi + Thực hành)
cho toàn bộ 137 bài học trong EasyTin (Lớp 3 đến Lớp 12).
Đảm bảo:
- Lí thuyết (Theory) chi tiết, sinh động, không khô khan, có ví dụ đời sống thực tế và mẹo nhớ nhanh.
- Thực hành (Practice) có nhiệm vụ rõ ràng, từng bước thao tác máy tính (step-by-step), thử thách và checklist.
- Đồng bộ với chuẩn GDPT 2018 của cả 3 bộ sách: KNTT, Cánh Diều, CTST.
"""

import json
import os
import re

def enrich_node(node):
    nid = node["id"]
    grade = node["grade"]
    title = node["title"]
    domain = node["standard_domain"]
    goals = node.get("learning_goals", [])
    tb = node.get("textbook_mapping", {})
    kntt = tb.get("kntt", "")
    cd = tb.get("canhdieu", "")
    ctst = tb.get("ctst", "")
    hook = node["lesson_data"]["hook"]
    concept = node["lesson_data"]["concept"]
    summary = concept["summary"]
    key_points = concept["key_points"]

    # Xây dựng các khối lý thuyết & thực hành chuyên biệt theo từng chủ đề và khối lớp
    overview = f"Chào mừng em đến với bài học '{title}'! Trong chương trình Tin học lớp {grade} (theo các bộ sách {kntt.split(':')[0] if kntt else 'KNTT'}, {cd.split(':')[0] if cd else 'Cánh Diều'}, {ctst.split(':')[0] if ctst else 'CTST'}), chúng ta sẽ cùng khám phá những bí mật thú vị về {title.lower()}. Kiến thức này không chỉ giúp em đạt điểm cao trên lớp mà còn là hành trang công nghệ không thể thiếu trong đời sống số hiện đại."

    # Khởi tạo sections
    sec1_content = f"Kiến thức cốt lõi của bài học bao gồm: {summary}. Cụ thể, các nội dung trọng tâm mà học sinh lớp {grade} cần làm chủ:\n" + "\n".join([f"• {kp}" for kp in key_points])
    sec1_title = "1. Bản chất & Kiến thức Cốt lõi"

    # Tạo ví dụ thực tế trực quan theo lớp và chủ đề
    sec2_title = "2. Ví dụ Trực quan trong Đời sống"
    sec2_content = ""
    sec2_example = ""

    # Tạo mẹo thực chiến & lưu ý tránh bẫy
    sec3_title = "3. Bí kíp Thực chiến & Tránh Bẫy Thường Gặp"
    sec3_content = ""
    sec3_tip = ""

    memorize = ""

    # Tạo nhiệm vụ thực hành (Practice Mission)
    prac_title = f"Nhiệm vụ Thực hành: Làm chủ {title}"
    prac_goal = f"Vận dụng kiến thức {title} để thực hiện thành thạo thao tác trên máy tính hoặc tư duy giải quyết vấn đề."
    prac_steps = []
    prac_challenge = ""
    prac_tip = ""
    prac_checklist = []

    # =========================================================================
    # LOGIC CHUYÊN SÂU TỪNG KHỐI LỚP VÀ CHỦ ĐỀ
    # =========================================================================
    if grade == 3:
        if "Thông tin" in title or "Xử lý" in title:
            sec2_content = "Trong đời sống hằng ngày, các giác quan như mắt, tai, mũi, lưỡi và da liên tục thu nhận thông tin từ thế giới xung quanh để bộ não xử lý và đưa ra quyết định."
            sec2_example = "Ví dụ: Khi em chuẩn bị qua đường, mắt nhìn thấy đèn tín hiệu chuyển sang màu Đỏ và tai nghe thấy tiếng còi xe máy. Bộ não xử lý thông tin này và đưa ra quyết định: 'Dừng lại ngay trên vỉa hè, đợi đèn Xanh mới được bước qua'."
            sec3_content = "Học sinh thường nhầm lẫn giữa 'Thông tin' (nội dung mang lại hiểu biết) và 'Vật mang tin' (vật chứa thông tin như tờ báo, bảng tin, màn hình)."
            sec3_tip = "Ghi nhớ: Thông tin là cái em hiểu được; còn quyển sách hay máy tính là vật cất giữ thông tin đó."
            memorize = "💡 Thu nhận bằng giác quan -> Bộ não xử lý -> Ra quyết định chính xác!"
            prac_title = "Nhiệm vụ Thám tử Nhí: Phân tích Dòng Thông tin"
            prac_goal = "Nhận diện đúng 4 hoạt động thông tin (Thu nhận - Lưu trữ - Xử lý - Truyền đạt) trong một tình huống thực tế."
            prac_steps = [
                "Bước 1: Quan sát thời tiết ngoài trời qua cửa sổ phòng học (Thu nhận).",
                "Bước 2: Ghi chép nhiệt độ hoặc tình trạng mây mưa vào sổ tay (Lưu trữ).",
                "Bước 3: Nhận định xem hôm nay cần mặc áo ấm hay mang ô che mưa (Xử lý).",
                "Bước 4: Nhắc nhở bạn bè mang theo áo mưa trước khi tan học (Truyền đạt)."
            ]
            prac_challenge = "Tìm thêm 2 ví dụ về việc xử lý thông tin của chiếc đồng hồ báo thức thông minh."
            prac_tip = "Khi gặp bài tập trắc nghiệm, hãy tìm từ khóa: 'nhìn thấy, nghe thấy' là Thu nhận; 'nghĩ ra, tính toán' là Xử lý."
            prac_checklist = ["Đã phân biệt được thông tin và vật mang tin", "Đã xác định đủ 4 bước hoạt động thông tin", "Đã hoàn thành tình huống mẫu"]

        elif "Phần cứng" in title or "Máy tính" in title:
            sec2_content = "Máy tính để bàn giống như một đội bạn thân 4 thành viên cùng phối hợp ăn ý để giúp em học tập và giải trí."
            sec2_example = "Ví dụ: Thân máy là 'Bộ não' tính toán; Màn hình là 'Gương mặt' hiển thị kết quả; Bàn phím là 'Bút viết' nhập chữ số; Chuột là 'Bàn tay' chỉ huy trỏ vào đồ vật."
            sec3_content = "Nhiều bạn nghĩ chiếc màn hình là toàn bộ máy tính. Thực ra thân máy mới là bộ phận quan trọng nhất chứa bộ vi xử lý CPU."
            sec3_tip = "Không bao giờ để đồ uống hay thức ăn gần bàn phím và thân máy để tránh chập điện."
            memorize = "⭐ Bốn bạn thân máy tính: Thân máy xử lý, Màn hình ngắm nhìn, Bàn phím gõ chữ, Chuột chỉ đường đi!"
            prac_title = "Thực hành Khám phá & Kết nối Bộ phận Máy tính"
            prac_goal = "Chỉ đúng tên và công dụng của 4 bộ phận chính trên máy tính thực tế trong phòng thực hành."
            prac_steps = [
                "Bước 1: Quan sát thân máy tính và tìm nút nguồn (Power) có biểu tượng hình tròn gạch dọc.",
                "Bước 2: Nhận biết dây cắm kết nối của Chuột và Bàn phím vào cổng USB phía sau thân máy.",
                "Bước 3: Bật công tắc màn hình và quan sát đèn tín hiệu xanh báo hiệu màn hình hoạt động.",
                "Bước 4: Nhấn nhẹ nút nguồn thân máy và chờ máy khởi động vào màn hình làm việc Desktop."
            ]
            prac_challenge = "Nhận biết thêm loa, tai nghe hoặc máy in kết nối vào máy tính."
            prac_tip = "Khi tắt máy, nhớ dùng lệnh Start -> Shut down, tuyệt đối không rút dây điện đột ngột!"
            prac_checklist = ["Chỉ đúng vị trí 4 bộ phận chính", "Biết bật màn hình và thân máy đúng quy trình", "Nhớ nguyên tắc tắt máy an toàn"]

        elif "Chuột" in title or "Bàn phím" in title or "Gõ" in title:
            sec2_content = "Chuột và bàn phím là công cụ giao tiếp trực tiếp giữa em và thế giới ảo của máy tính. Thao tác chuẩn giúp em làm việc nhanh gấp 3 lần và không mỏi tay."
            sec2_example = "Ví dụ: Cầm chuột nhẹ nhàng bằng tay phải: ngón trỏ đặt lên nút trái, ngón giữa đặt lên nút phải. Khi muốn mở tệp tranh vẽ, em nháy đúp (bấm nhanh 2 lần nút trái)."
            sec3_content = "Lỗi phổ biến là học sinh gõ 'mổ cò' chỉ bằng 2 ngón trỏ, khiến tốc độ rất chậm và dễ sai tư thế cột sống."
            sec3_tip = "Đặt 2 ngón trỏ lên 2 phím có gờ F và J trên hàng phím cơ sở để định vị cả 10 ngón tay mà không cần nhìn bàn phím."
            memorize = "🎯 Ngón trỏ phím F và J, mười ngón dàn đều trên hàng cơ sở!"
            prac_title = "Đấu trường Luyện Ngón: Gõ Phím Mười Ngón & Rê Chuột Chuẩn Xác"
            prac_goal = "Thực hiện thành thạo thao tác nháy chuột, kéo thả và đặt đúng 10 ngón tay trên hàng phím cơ sở."
            prac_steps = [
                "Bước 1: Ngồi thẳng lưng, mắt cách màn hình 50 - 80cm, hai chân chạm sàn thoải mái.",
                "Bước 2: Đặt tay lên bàn phím: Ngón trỏ trái đặt lên phím F, ngón trỏ phải đặt lên phím J.",
                "Bước 3: Mở phần mềm gõ phím hoặc mở Notepad, thực hành gõ chuỗi: A S D F J K L ;",
                "Bước 4: Dùng chuột kéo thả một biểu tượng tệp tin từ góc trái sang góc phải màn hình."
            ]
            prac_challenge = "Gõ 20 chữ cái liên tục trên hàng phím cơ sở mà không cần nhìn xuống bàn phím."
            prac_tip = "Dùng ngón cái hai bàn tay để nhấn phím Cách (Spacebar) dài nhất trên bàn phím."
            prac_checklist = ["Tư thế ngồi chuẩn khoa học", "Đặt đúng 10 ngón trên hàng cơ sở", "Thao tác chuột mượt mà không bị rung"]

        elif "Thư mục" in title or "Phân loại" in title or "Cây" in title:
            sec2_content = "Cây thư mục trong máy tính cũng giống hệt như chiếc tủ sách nhiều ngăn ở nhà hay chiếc cặp sách đi học của em."
            sec2_example = "Ví dụ: Trong cặp sách có ngăn đựng Sách giáo khoa, ngăn đựng Vở bài tập, ngăn đựng Bút thước. Trên máy tính, em tạo thư mục 'HocTap', bên trong chứa 2 thư mục con là 'MonTinHoc' và 'MonToan'."
            sec3_content = "Lưu tệp lung tung ra màn hình Desktop khiến máy tính lộn xộn và rất khó tìm lại bài vẽ khi thầy cô yêu cầu."
            sec3_tip = "Luôn đặt tên thư mục ngắn gọn, có ý nghĩa và chứa đúng loại tệp tương ứng."
            memorize = "📂 Thư mục như chiếc tủ ngăn, sắp xếp khoa học tìm nhanh tức thì!"
            prac_title = "Phòng Lab Nhí: Thiết kế Cây Thư mục Học tập"
            prac_goal = "Tạo được thư mục chính và các thư mục con phân cấp rõ ràng trên ổ đĩa học tập."
            prac_steps = [
                "Bước 1: Mở File Explorer (nhấn tổ hợp phím Windows + E) và mở ổ đĩa D: hoặc thư mục Documents.",
                "Bước 2: Nháy chuột phải vào vùng trống, chọn New -> Folder, đặt tên là 'Lop3_TenEm'.",
                "Bước 3: Nháy đúp chuột để mở thư mục 'Lop3_TenEm' vừa tạo.",
                "Bước 4: Tạo tiếp 2 thư mục con bên trong: 'TapVe' và 'BaiTapTin'."
            ]
            prac_challenge = "Đổi tên thư mục 'TapVe' thành 'HoiHoa' bằng cách nhấn phím F2."
            prac_tip = "Tên thư mục nên viết không dấu hoặc có dấu cách rõ ràng, không chứa ký tự đặc biệt như * / \\ : ?"
            prac_checklist = ["Tạo thành công thư mục chính", "Tạo đúng 2 thư mục con theo cấp bậc", "Biết đổi tên thư mục thành thạo"]

        elif "Thuật toán" in title or "Mê cung" in title or "Vòng lặp" in title:
            sec2_content = "Thuật toán nghe có vẻ phức tạp nhưng thực ra chính là các bước chỉ dẫn từng bước rõ ràng để hoàn thành một công việc hằng ngày."
            sec2_example = "Ví dụ: Thuật toán Đánh răng gồm 3 bước: 1. Lấy kem đánh răng lên bàn chải -> 2. Chải đều các mặt răng trong 2 phút -> 3. Súc miệng sạch bằng nước. Nếu đảo bước 3 lên trước bước 1 thì sẽ hỏng việc!"
            sec3_content = "Lỗi thuật toán xảy ra khi các bước bị xếp sai thứ tự hoặc thiếu điều kiện dừng, dẫn đến kết quả sai lệch."
            sec3_tip = "Trước khi ra lệnh cho robot hay máy tính, hãy tự đọc nhẩm từng bước xem có bước nào vô lý không."
            memorize = "🔄 Thuật toán rõ từng bước, đúng thứ tự sẽ tới đích thành công!"
            prac_title = "Nhiệm vụ Lập trình viên Nhí: Chỉ đường Robot Vượt Mê Cung"
            prac_goal = "Mô tả được thuật toán di chuyển robot gồm các bước: Tiến lên, Rẽ trái, Rẽ phải, Lặp lại."
            prac_steps = [
                "Bước 1: Xác định vị trí xuất phát của chú Robot và vị trí của Ngôi sao mục tiêu.",
                "Bước 2: Viết ra nháp chuỗi lệnh: Tiến 2 bước -> Rẽ phải -> Tiến 3 bước -> Nhặt sao.",
                "Bước 3: Nhập các khối lệnh tương ứng vào trò chơi Block Maze trên màn hình.",
                "Bước 4: Nhấn nút 'Chạy thử' và quan sát robot di chuyển theo thuật toán vừa lập."
            ]
            prac_challenge = "Sử dụng khối lệnh 'Lặp lại 3 lần' thay vì ghép 3 khối lệnh 'Tiến lên' liên tiếp."
            prac_tip = "Khi robot đi sai đường, hãy dừng lại kiểm tra xem robot bị nhầm ở bước rẽ trái hay rẽ phải."
            prac_checklist = ["Xác định đúng mục tiêu mê cung", "Viết thuật toán tuần tự không bị thiếu bước", "Robot nhặt được sao thành công"]

        else:
            sec2_content = f"Chủ đề '{title}' mang lại cho em những hiểu biết sâu sắc và kỹ năng số cần thiết trong thế giới thông minh hôm nay."
            sec2_example = "Ví dụ: Luôn giữ khoảng cách an toàn với màn hình, không truy cập trang web lạ và luôn hỏi người lớn khi gặp tình huống đáng ngờ trên mạng."
            sec3_content = "Không chia sẻ mật khẩu, họ tên đầy đủ hay số điện thoại của gia đình cho người lạ trên mạng Internet."
            sec3_tip = "Bảo vệ thông tin cá nhân chính là bảo vệ sự an toàn cho chính em và gia đình."
            memorize = "🛡️ An toàn trên mạng, bảo vệ thông tin, tự tin tỏa sáng thời đại số!"
            prac_title = f"Thực hành Trải nghiệm Kỹ năng: {title}"
            prac_goal = f"Hoàn thành các nhiệm vụ mô phỏng liên quan đến {title}."
            prac_steps = [
                "Bước 1: Đọc kỹ tình huống mô phỏng được đưa ra trên màn hình.",
                "Bước 2: Phân tích các lựa chọn hành vi an toàn và văn minh.",
                "Bước 3: Thực hiện thao tác chọn phương án đúng nhất.",
                "Bước 4: Rút ra bài học kinh nghiệm và ghi nhớ quy tắc số."
            ]
            prac_challenge = "Giải thích cho bạn cùng bàn hiểu vì sao lựa chọn đó là chính xác nhất."
            prac_tip = "Luôn nhớ quy tắc: Cẩn trọng trước mỗi lượt nhấp chuột trên Internet."
            prac_checklist = ["Hiểu rõ thông điệp bài học", "Hoàn thành bài tập trắc nghiệm", "Áp dụng được vào thực tế"]

    elif 4 <= grade <= 5:
        if "Scratch" in title or "Lập trình" in title or "Nhân vật" in title or "Biến số" in title or "Rẽ nhánh" in title:
            sec2_content = "Lập trình Scratch cho phép em trở thành đạo diễn của một bộ phim hoạt hình hoặc tác giả của một trò chơi điện tử kỳ thú."
            sec2_example = "Ví dụ: Muốn nhân vật Chú mèo Scratch đuổi theo quả bóng: Khi bấm cờ xanh -> Lặp liên tục [Hướng về phía Quả bóng -> Di chuyển 10 bước -> Nếu chạm Quả bóng thì Phát âm thanh Meow và Tăng điểm số thêm 1]."
            sec3_content = "Học sinh hay quên đặt giá trị ban đầu cho Biến số (như Điểm số = 0 khi bắt đầu game) hoặc đặt sai câu lệnh rẽ nhánh 'Nếu... Thì' bên ngoài vòng lặp."
            sec3_tip = "Luôn đặt khối 'Nếu... Thì' bên trong khối 'Lặp lại liên tục' nếu muốn nhân vật liên tục kiểm tra va chạm trong suốt trò chơi."
            memorize = "🧩 Ghép khối logic, lặp liên tục kiểm tra va chạm, biến số ghi dấu chiến công!"
            prac_title = "Phòng Lab Sáng tạo Scratch: Lập trình Game Nhặt Kim Cương"
            prac_goal = "Tạo một nhân vật di chuyển theo phím mũi tên và tăng biến 'Điểm' khi chạm vào vật phẩm."
            prac_steps = [
                "Bước 1: Mở Scratch, chọn nhân vật Mèo Scratch và thêm nhân vật Kim Cương từ thư viện.",
                "Bước 2: Tạo một biến số mới đặt tên là 'DiemSo' trong nhóm lệnh Các biến số.",
                "Bước 3: Lập trình cho Mèo: Khi nhấn phím Mũi tên Phải -> Thay đổi X một lượng 10; Mũi tên Trái -> Thay đổi X một lượng -10.",
                "Bước 4: Ghép khối: Khi bấm vào Cờ xanh -> Đặt DiemSo thành 0 -> Lặp liên tục [Nếu đang chạm Kim Cương thì Thay đổi DiemSo một lượng 1]."
            ]
            prac_challenge = "Thêm câu lệnh 'Nếu DiemSo > 10 thì Nói Chiến thắng! trong 2 giây rồi Dừng lại tất cả'."
            prac_tip = "Dùng phím Space để test nhanh kịch bản trước khi chạy toàn màn hình."
            prac_checklist = ["Tạo đúng biến số DiemSo", "Nhân vật di chuyển mượt mà 4 hướng", "Va chạm tính điểm chính xác"]

        elif "Soạn thảo" in title or "Văn bản" in title or "Định dạng" in title or "Bảng" in title:
            sec2_content = "Soạn thảo văn bản trên máy tính giúp em làm những bài tập làm văn sạch đẹp, thiết kế thời khóa biểu và thiệp chúc mừng sinh nhật lung linh."
            sec2_example = "Ví dụ: Tiêu đề bài viết cần chọn chữ Đậm (Bold - Ctrl+B), căn giữa (Ctrl+E), cỡ chữ 16. Nội dung bài viết chọn cỡ chữ 13-14, căn đều hai bên (Ctrl+J) để mép trang giấy thẳng tắp."
            sec3_content = "Lỗi đặt dấu cách sai chính tả tiếng Việt: Nhiều bạn hay gõ dấu cách trước dấu chấm, dấu phẩy (sai: 'xin chào , các bạn .')."
            sec3_tip = "Quy tắc vàng: Dấu chấm, dấu phẩy gõ dính liền với từ đứng trước, sau đó mới gõ một dấu cách duy nhất (đúng: 'xin chào, các bạn.')."
            memorize = "📝 Gõ chuẩn Telex, dấu sát chữ trước, cách một nhịp mới sang từ sau!"
            prac_title = "Xưởng Soạn thảo: Trình bày Bảng Thời khóa biểu Tuần"
            prac_goal = "Tạo bảng (Table), chèn hàng/cột, căn chỉnh chữ và chèn hình ảnh minh họa sinh động."
            prac_steps = [
                "Bước 1: Mở Microsoft Word hoặc Google Docs, chọn phông chữ Times New Roman hoặc Arial, cỡ chữ 14.",
                "Bước 2: Gõ tiêu đề 'THỜI KHÓA BIỂU LỚP 4A', chọn In đậm và Căn giữa trang.",
                "Bước 3: Vào thẻ Insert -> Table, tạo bảng gồm 6 cột (Thứ 2 đến Thứ 7) và 5 hàng (các tiết học).",
                "Bước 4: Nhập các môn học vào các ô, chọn hàng tiêu đề và tô màu nền (Shading) nổi bật."
            ]
            prac_challenge = "Chèn thêm một hình ảnh icon nhỏ về môn Tin học vào góc phải của trang văn bản."
            prac_tip = "Dùng phím Tab để nhảy nhanh sang ô tiếp theo trong bảng mà không cần bấm chuột."
            prac_checklist = ["Đúng quy tắc dấu câu tiếng Việt", "Tạo bảng đúng số cột số hàng", "Định dạng màu sắc hài hòa"]

        elif "Trình chiếu" in title or "Hình ảnh" in title or "Đa phương tiện" in title:
            sec2_content = "Phần mềm trình chiếu (PowerPoint) biến bài thuyết trình của em thành một buổi diễn thuyết cuốn hút với hình ảnh, âm thanh và hiệu ứng sinh động."
            sec2_example = "Ví dụ: Mỗi trang chiếu (slide) giống như một trang áp phích triển lãm: tiêu đề nổi bật, 3-4 dòng chữ ngắn gọn, đi kèm một bức ảnh sắc nét minh họa chủ đề."
            sec3_content = "Nhồi nhét quá nhiều chữ li ti lên slide và dùng hiệu ứng hoạt hình bay lượn quá chóng mặt khiến người xem mất tập trung."
            sec3_tip = "Quy tắc 6x6: Mỗi slide tối đa 6 dòng, mỗi dòng tối đa 6 từ; màu chữ tương phản rõ với màu nền."
            memorize = "🎨 Trang chiếu súc tích, hình ảnh sắc nét, màu sắc tương phản thu hút người xem!"
            prac_title = "Studio Thuyết trình: Thiết kế Slide Giới thiệu Bản thân"
            prac_goal = "Tạo bài trình chiếu gồm 3 slide có tiêu đề, hình ảnh và hiệu ứng chuyển trang (Transitions)."
            prac_steps = [
                "Bước 1: Khởi động phần mềm PowerPoint, chọn một mẫu giao diện (Theme) trang nhã.",
                "Bước 2: Slide 1 (Bìa): Nhập 'XIN CHÀO! TÔI LÀ TINTIN' và họ tên, lớp của em.",
                "Bước 3: Slide 2 (Sở thích): Chèn 2 hình ảnh về sở thích và gõ 3 gạch đầu dòng ngắn gọn.",
                "Bước 4: Vào thẻ Transitions, chọn hiệu ứng chuyển trang 'Fade' hoặc 'Push' cho từng slide."
            ]
            prac_challenge = "Thêm hiệu ứng Animation xuất hiện từng dòng chữ khi nhấp chuột."
            prac_tip = "Nhấn phím F5 để bắt đầu trình chiếu toàn màn hình từ trang đầu tiên."
            prac_checklist = ["Slide có bố cục gọn gàng dễ đọc", "Hình ảnh chèn vừa vặn không bị méo tỉ lệ", "Hiệu ứng chuyển trang mượt mà"]

        elif "Bảng tính" in title:
            sec2_content = "Bảng tính Excel giống như một quyển sổ kế toán thông minh có khả năng tự động tính tổng, tính trung bình chỉ trong một cái chớp mắt."
            sec2_example = "Ví dụ: Em muốn tính tổng tiền mua sách vở: Cột A ghi tên món đồ, Cột B ghi số tiền. Thay vì bấm máy tính cầm tay, em chỉ cần gõ công thức =SUM(B2:B6) là xong."
            sec3_content = "Quên gõ dấu bằng '=' ở đầu công thức. Nếu không có dấu '=', Excel sẽ hiểu đó là một đoạn văn bản bình thường chứ không tính toán."
            sec3_tip = "Mọi công thức hoặc hàm trong Excel đều bắt buộc phải mở đầu bằng dấu bằng '='."
            memorize = "📊 Bảng tính thông minh, bắt đầu bằng dấu '=', SUM tính tổng trong nháy mắt!"
            prac_title = "Kế toán Nhí: Lập Bảng Quản lý Tiền Tiết kiệm"
            prac_goal = "Tạo bảng tính gồm các cột STT, Khoản chi, Số tiền và dùng hàm SUM để tính tổng."
            prac_steps = [
                "Bước 1: Mở Microsoft Excel, nhập tiêu đề 'BẢNG THEO DÕI TIẾT KIỆM' tại ô A1.",
                "Bước 2: Tại hàng 3, nhập các tiêu đề cột: A3: STT, B3: Nội dung, C3: Số tiền (VNĐ).",
                "Bước 3: Nhập dữ liệu 4 món đồ dùng học tập cùng giá tiền vào các ô tương ứng từ C4 đến C7.",
                "Bước 4: Tại ô C8, gõ công thức =SUM(C4:C7) rồi nhấn Enter để xem tổng tiền tự động."
            ]
            prac_challenge = "Thử thay đổi giá trị tiền của một món đồ ở ô C4 và quan sát kết quả ô C8 tự động cập nhật."
            prac_tip = "Định dạng số tiền có dấu phân cách hàng nghìn (ví dụ 50,000) bằng nút Comma Style trên thanh công cụ."
            prac_checklist = ["Nhập dữ liệu đúng hàng đúng cột", "Viết đúng cú pháp hàm =SUM(...)", "Kết quả tự động cập nhật chuẩn"]

        else:
            sec2_content = f"Chủ đề '{title}' mở ra cánh cửa giúp học sinh lớp {grade} làm chủ công nghệ và ứng xử văn minh trong môi trường số."
            sec2_example = "Ví dụ: Khi lấy tranh ảnh trên Internet để làm bài thuyết trình, em luôn ghi rõ nguồn tác giả và trang web lấy ảnh để tôn trọng bản quyền số."
            sec3_content = "Sao chép nguyên văn bài viết của người khác rồi nhận là của mình là hành vi vi phạm đạo đức và bản quyền."
            sec3_tip = "Hãy trích dẫn nguồn gốc tác giả và xin phép khi sử dụng tư liệu của người khác."
            memorize = "🌐 Tôn trọng bản quyền, ứng xử văn minh, bảo vệ danh tính số!"
            prac_title = f"Thực hành Dự án Khám phá: {title}"
            prac_goal = f"Vận dụng kiến thức {title} để giải quyết bài tập tình huống thực tế."
            prac_steps = [
                "Bước 1: Khởi động máy tính và mở công cụ học tập tương ứng.",
                "Bước 2: Quan sát và phân tích các dữ liệu đầu vào của bài toán.",
                "Bước 3: Áp dụng quy tắc tiêu chuẩn đã học để thực hiện thao tác.",
                "Bước 4: Kiểm tra lại sản phẩm và lưu tệp cẩn thận vào thư mục cá nhân."
            ]
            prac_challenge = "Mở rộng bài tập bằng cách thử nghiệm với bộ dữ liệu phức tạp hơn."
            prac_tip = "Luôn lưu bài thường xuyên bằng tổ hợp phím tắt Ctrl + S."
            prac_checklist = ["Thao tác đúng quy trình", "Tuân thủ quy chuẩn số", "Lưu bài an toàn vào ổ đĩa"]

    elif 6 <= grade <= 9:
        if "Nhị phân" in title or "Bit" in title or "Dung lượng" in title:
            sec2_content = "Máy tính tuy thông minh nhưng bên trong thực chất chỉ gồm hàng tỷ công tắc bóng bán dẫn siêu nhỏ, mỗi công tắc chỉ có 2 trạng thái: Bật (1) hoặc Tắt (0)."
            sec2_example = "Ví dụ: Mọi bản nhạc MP3, bức ảnh selfie hay video YouTube đều được máy tính băm nhỏ và mã hóa thành một dãy dài vô tận các số 0 và 1. Một chữ cái 'A' được biểu diễn bằng dãy 8 bit: 01000001."
            sec3_content = "Nhầm lẫn giữa Bit (b) và Byte (B). 1 Byte = 8 Bit. Tốc độ mạng thường đo bằng Megabit/giây (Mbps), còn dung lượng thẻ nhớ đo bằng Gigabyte (GB)."
            sec3_tip = "Hệ thống đơn vị: 1 KB = 1024 Bytes, 1 MB = 1024 KB, 1 GB = 1024 MB, 1 TB = 1024 GB (lũy thừa của 2: 2^10 = 1024)."
            memorize = "💾 Bit là 0 và 1, 8 bit thành 1 Byte, 1024 bước nhảy đo lường dung lượng số!"
            prac_title = "Phòng Lab Giải mã Nhị phân & Tính toán Dung lượng"
            prac_goal = "Chuyển đổi số thập phân sang nhị phân và tính toán dung lượng thiết bị lưu trữ thực tế."
            prac_steps = [
                "Bước 1: Lấy số thập phân 13, chia liên tiếp cho 2 và ghi lại phần dư: 13/2=6 dư 1, 6/2=3 dư 0, 3/2=1 dư 1, 1/2=0 dư 1.",
                "Bước 2: Viết các số dư theo chiều từ dưới lên trên để được mã nhị phân: 1101 (2).",
                "Bước 3: Mở File Explorer trên máy tính, nhấp chuột phải vào một tệp ảnh và xem kích thước (Size) bằng KB hoặc MB.",
                "Bước 4: Tính nhẩm xem một thẻ nhớ USB 16 GB có thể chứa được bao nhiêu bức ảnh 4 MB (16 x 1024 / 4 = 4096 ảnh)."
            ]
            prac_challenge = "Giải mã chuỗi nhị phân 01000010 sang số thập phân bằng cách nhân với các lũy thừa của 2."
            prac_tip = "Bật chế độ 'Programmer' trong ứng dụng Calculator của Windows để chuyển đổi nhanh giữa BIN, DEC và HEX."
            prac_checklist = ["Hiểu bản chất bit 0 và 1", "Chuyển đổi thành thạo DEC sang BIN", "Tính đúng dung lượng lưu trữ"]

        elif "Mạng" in title or "Internet" in title or "LAN" in title or "Web" in title or "Email" in title:
            sec2_content = "Mạng máy tính là một mạng lưới giao thông khổng lồ kết nối hàng tỷ thiết bị trên khắp hành tinh để chia sẻ dữ liệu và tài nguyên."
            sec2_example = "Ví dụ: Mạng LAN kết nối các máy tính trong phòng thực hành trường em để dùng chung một máy in. Mạng Internet kết nối mạng LAN của trường với các máy chủ của Google ở tận bên kia đại dương."
            sec3_content = "Nhầm lẫn giữa Internet (hạ tầng mạng lưới toàn cầu) và Web/WWW (một dịch vụ tra cứu thông tin chạy trên Internet)."
            sec3_tip = "Internet là 'đường cao tốc', còn Web, Email, Zoom là các 'chiếc xe' chở hàng hóa chạy trên con đường đó."
            memorize = "🌐 Internet là mạng lưới toàn cầu, LAN nội bộ, WWW tra cứu vạn tài nguyên!"
            prac_title = "Thực nghiệm Mạng Máy tính: Khảo sát Kết nối & IP"
            prac_goal = "Kiểm tra kết nối mạng, địa chỉ IP cục bộ và đo độ trễ mạng bằng lệnh Ping."
            prac_steps = [
                "Bước 1: Nhấn tổ hợp phím Windows + R, gõ 'cmd' và nhấn Enter để mở cửa sổ Command Prompt.",
                "Bước 2: Gõ lệnh 'ipconfig' rồi nhấn Enter để xem địa chỉ IPv4 của máy tính trong mạng LAN.",
                "Bước 3: Gõ lệnh 'ping google.com' để kiểm tra tốc độ phản hồi của gói tin (đo bằng mili-giây ms).",
                "Bước 4: Mở trình duyệt web, truy cập một trang web học tập và kiểm tra giao thức bảo mật ổ khóa HTTPS."
            ]
            prac_challenge = "Dùng lệnh 'tracert google.com' để xem gói tin đi qua bao nhiêu bộ định tuyến (router) trên đường truyền."
            prac_tip = "Khi mạng bị mất kết nối, lệnh ping 127.0.0.1 (loopback) giúp kiểm tra xem card mạng trên máy có bị hỏng phần cứng hay không."
            prac_checklist = ["Mở được cmd an toàn", "Xem được địa chỉ IP máy tính", "Hiểu ý nghĩa phản hồi lệnh ping"]

        elif "Tìm kiếm" in title or "Tuần tự" in title or "Nhị phân" in title or "Sắp xếp" in title or "Nổi bọt" in title:
            sec2_content = "Các thuật toán tìm kiếm và sắp xếp là trái tim của mọi ứng dụng công nghệ như Google Search, TikTok feed, hay hệ thống tra cứu điểm thi."
            sec2_example = "Ví dụ: Tìm kiếm tuần tự giống như lật từng trang vở từ đầu đến cuối (dùng khi vở chưa xếp thứ tự). Tìm kiếm nhị phân giống như tra từ điển: mở đôi cuốn sách ở giữa, so sánh chữ cái rồi vứt bỏ nửa trước hoặc nửa sau, tốc độ nhanh gấp hàng triệu lần!"
            sec3_content = "Áp dụng Tìm kiếm nhị phân cho một danh sách chưa được sắp xếp. Đây là sai lầm chết người vì thuật toán nhị phân BẮT BUỘC danh sách phải được sắp xếp trước!"
            sec3_tip = "Nếu mảng chưa sắp xếp: Tìm kiếm tuần tự O(N). Nếu mảng đã sắp xếp: Tìm kiếm nhị phân O(log N)."
            memorize = "⚡ Mảng lộn xộn tìm tuần tự, mảng ngay ngắn chia đôi nhị phân thần tốc!"
            prac_title = "Đấu trường Thuật toán: Thử nghiệm Tìm kiếm Nhị phân & Sắp xếp Nổi bọt"
            prac_goal = "Mô phỏng từng bước lặp của thuật toán Binary Search và Bubble Sort trên một dãy số thực tế."
            prac_steps = [
                "Bước 1: Cho dãy số đã sắp xếp: [3, 8, 12, 19, 25, 33, 47, 56]. Cần tìm số X = 33.",
                "Bước 2: Lần 1: Chỉ số đầu Low = 0, Cuối High = 7 -> Giữa Mid = (0+7)//2 = 3 (giá trị 19). Vì 33 > 19 nên bỏ nửa trái, đặt Low = Mid + 1 = 4.",
                "Bước 3: Lần 2: Low = 4, High = 7 -> Mid = (4+7)//2 = 5 (giá trị 33). So sánh: 33 == 33 -> Tìm thấy ở vị trí index 5!",
                "Bước 4: Thực hiện mô phỏng Bubble Sort với dãy [5, 1, 4, 2] bằng cách đổi chỗ từng cặp liền kề."
            ]
            prac_challenge = "Tính xem với một danh sách 1,000,000 phần tử đã sắp xếp, tìm kiếm nhị phân cần tối đa bao nhiêu lần so sánh (khoảng 20 lần vì 2^20 > 1,000,000)."
            prac_tip = "Trong Python, thuật toán sắp xếp Timsort tích hợp sẵn qua lệnh sorted(list) hoặc list.sort()."
            prac_checklist = ["Nắm vững điều kiện tiên quyết của tìm kiếm nhị phân", "Thực hiện đúng công thức tính Mid", "Mô phỏng thành công các bước đổi chỗ Bubble Sort"]

        elif "Python" in title or "Lập trình" in title or "Biến" in title or "Vòng lặp" in title or "Hàm" in title or "List" in title:
            sec2_content = "Python là ngôn ngữ lập trình phổ biến hàng đầu thế giới nhờ cú pháp trong sáng như tiếng Anh, được ứng dụng từ chế tạo website đến trí tuệ nhân tạo và tàu vũ trụ NASA."
            sec2_example = "Ví dụ: Viết một đoạn mã tính tiền điện: tong_tien = so_kwh * 2500. Sau đó dùng câu lệnh rẽ nhánh: if tong_tien > 500000: print('Cần tiết kiệm điện!')."
            sec3_content = "Lỗi thụt đầu dòng (IndentationError) và nhầm lẫn giữa toán tử gán '=' với toán tử so sánh bằng '=='."
            sec3_tip = "Mọi khối lệnh sau dấu hai chấm ':' (trong if, for, while, def) đều phải thụt lề 4 dấu cách (1 tab)."
            memorize = "🐍 Python sáng rõ, thụt lề 4 cách, gán bằng một '=', so sánh hai '=='!"
            prac_title = "Phòng Lab Lập trình Python: Xây dựng Chương trình Phân loại Điểm số"
            prac_goal = "Viết kịch bản Python hoàn chỉnh sử dụng biến số, nhập xuất input/print và cấu trúc rẽ nhánh if - elif - else."
            prac_steps = [
                "Bước 1: Mở môi trường IDLE hoặc VS Code, tạo tệp mới 'tinh_diem.py'.",
                "Bước 2: Nhập điểm từ bàn phím và ép kiểu sang số thực: diem = float(input('Nhập điểm tổng kết Tin học: ')).",
                "Bước 3: Viết logic rẽ nhánh:\nif diem >= 8.0:\n    print('Xếp loại: Giỏi')\nelif diem >= 6.5:\n    print('Xếp loại: Khá')\nelse:\n    print('Cần cố gắng thêm!')",
                "Bước 4: Nhấn F5 để chạy thử với các giá trị đầu vào: 9.5, 7.0, 5.0 và kiểm tra kết quả in ra màn hình."
            ]
            prac_challenge = "Thêm vòng lặp while True để chương trình tiếp tục hỏi điểm học sinh tiếp theo cho đến khi người dùng nhập số âm để thoát."
            prac_tip = "Hàm type(x) giúp kiểm tra kiểu dữ liệu của biến x trong lúc viết code."
            prac_checklist = ["Cú pháp đúng chuẩn thụt lề PEP 8", "Ép kiểu float/int cho dữ liệu nhập vào", "Chương trình chạy trơn tru không có lỗi cú pháp"]

        else:
            sec2_content = f"Nội dung '{title}' trang bị cho học sinh cấp 2 nền tảng tư duy máy tính vững chắc và kỹ năng xử lý thông tin thông minh."
            sec2_example = "Ví dụ: Áp dụng quy tắc sao lưu 3-2-1 để bảo vệ tài liệu học tập: Giữ ít nhất 3 bản sao chép, trên 2 loại thiết bị khác nhau (ổ cứng máy tính và USB), với 1 bản đặt trên đám mây (Google Drive)."
            sec3_content = "Mất dữ liệu do virus mã hóa tống tiền (Ransomware) hoặc hỏng phần cứng là rủi ro rất lớn nếu không có thói quen sao lưu định kỳ."
            sec3_tip = "Bật tính năng xác thực hai yếu tố (2FA) cho toàn bộ tài khoản email và mạng xã hội cá nhân."
            memorize = "🔒 Dữ liệu là tài sản, bảo mật hai lớp, sao lưu 3-2-1 an tâm trọn đời!"
            prac_title = f"Thực hành Dự án Kỹ năng Số: {title}"
            prac_goal = f"Thực hiện thành công quy trình xử lý dữ liệu chuẩn theo yêu cầu bài học {title}."
            prac_steps = [
                "Bước 1: Khởi động phần mềm chuyên dụng và mở tệp dữ liệu thực hành.",
                "Bước 2: Thiết lập các thông số kỹ thuật chuẩn theo hướng dẫn.",
                "Bước 3: Thực hiện thao tác xử lý, định dạng hoặc lập trình thuật toán.",
                "Bước 4: Xuất kết quả (Export) và kiểm thử chất lượng sản phẩm."
            ]
            prac_challenge = "Tối ưu hóa các bước thao tác bằng cách sử dụng các phím tắt nhanh."
            prac_tip = "Ghi chép lại các thông báo lỗi gặp phải để tra cứu cách giải quyết trong tài liệu kỹ thuật."
            prac_checklist = ["Thực hiện đủ các bước quy trình", "Kiểm thử kết quả đạt yêu cầu", "Lưu trữ sản phẩm khoa học"]

    else:  # THPT: Grade 10, 11, 12
        if "SQL" in title or "CSDL" in title or "Quan hệ" in title or "Khóa" in title:
            sec2_content = "Cơ sở dữ liệu quan hệ (RDBMS) là xương sống của mọi hệ thống thương mại điện tử, ngân hàng và mạng xã hội như Shopee, Facebook, Momo."
            sec2_example = "Ví dụ: Tại Shopee, bảng HOC_SINH liên kết với bảng DIEM_THI qua Khóa chính (MaHS) và Khóa ngoại. Khi cần in danh sách học sinh đạt loại Giỏi, lệnh SELECT kết hợp INNER JOIN sẽ truy xuất dữ liệu từ hàng triệu bản ghi chỉ trong vài mili-giây."
            sec3_content = "Thực hiện lệnh UPDATE hoặc DELETE mà quên mệnh đề WHERE. Nếu không có WHERE, toàn bộ dữ liệu trong cả bảng sẽ bị sửa hoặc xóa sạch!"
            sec3_tip = "Quy tắc an toàn: Luôn viết lệnh SELECT với điều kiện WHERE để kiểm tra xem đúng những dòng cần xóa/sửa chưa trước khi chạy DELETE/UPDATE."
            memorize = "🗄️ Khóa chính định danh duy nhất, Khóa ngoại kết nối nhiều bảng, SQL WHERE cứu nguy thảm họa!"
            prac_title = "Phòng Lab Quản trị CSDL: Viết Truy vấn SQL Báo cáo Học lực"
            prac_goal = "Thực hiện thành thạo các câu lệnh SELECT, WHERE, INNER JOIN, GROUP BY và COUNT trong MySQL/PostgreSQL."
            prac_steps = [
                "Bước 1: Mở giao diện dòng lệnh MySQL hoặc SQLite Studio, kết nối tới cơ sở dữ liệu 'QuanLyTruongHoc'.",
                "Bước 2: Viết truy vấn lấy mã số, họ tên học sinh lớp 11A1:\nSELECT MaHS, HoTen FROM HocSinh WHERE Lop = '11A1';",
                "Bước 3: Viết truy vấn kết nối 2 bảng để tính điểm trung bình từng môn:\nSELECT H.HoTen, D.MonHoc, D.DiemSo FROM HocSinh H INNER JOIN BangDiem D ON H.MaHS = D.MaHS;",
                "Bước 4: Thống kê số lượng học sinh theo từng lớp bằng mệnh đề GROUP BY:\nSELECT Lop, COUNT(*) AS SiSo FROM HocSinh GROUP BY Lop;"
            ]
            prac_challenge = "Dùng mệnh đề HAVING để lọc ra những lớp có sĩ số trên 40 học sinh."
            prac_tip = "Tên từ khóa SQL nên viết HOA toàn bộ (SELECT, FROM, WHERE) để phân biệt rõ với tên bảng và cột."
            prac_checklist = ["Hiểu đúng vai trò khóa chính khóa ngoại", "Viết đúng cú pháp INNER JOIN", "Áp dụng thành công GROUP BY và COUNT"]

        elif "Thuật toán" in title or "Đệ quy" in title or "Quick Sort" in title or "Merge Sort" in title or "Big-O" in title:
            sec2_content = "Độ phức tạp thuật toán (Big-O) là thước đo khoa học để đánh giá xem một thuật toán chạy nhanh như thế nào khi khối lượng dữ liệu phình to lên hàng tỷ phần tử."
            sec2_example = "Ví dụ: Thuật toán O(N^2) như Bubble Sort khi xử lý 1 triệu tài khoản ngân hàng sẽ mất hàng chục giờ chạy máy tính. Nhưng thuật toán O(N log N) như Quick Sort hay Merge Sort chỉ mất vỏn vẹn dưới 1 giây!"
            sec3_content = "Quên điều kiện dừng (Base Case) trong hàm đệ quy, khiến chương trình rơi vào vòng lặp vô tận và làm tràn ngăn xếp bộ nhớ (RecursionError: maximum recursion depth exceeded)."
            sec3_tip = "Bất kỳ hàm đệ quy nào cũng phải có 2 phần: 1. Base Case (điều kiện dừng trực tiếp) và 2. Recursive Step (bước gọi lại chính nó với bài toán nhỏ hơn)."
            memorize = "⚡ Đệ quy phải có điểm dừng, Quick Sort chia để trị, N log N đánh bại mọi thách thức Big Data!"
            prac_title = "Đấu trường Thuật toán Nâng cao: Cài đặt và Đo lường Hiệu năng Quick Sort"
            prac_goal = "Cài đặt thuật toán Quick Sort bằng Python và so sánh thời gian chạy thực tế với Bubble Sort trên mảng ngẫu nhiên 5,000 phần tử."
            prac_steps = [
                "Bước 1: Cài đặt hàm quick_sort(arr) trong Python theo chiến thuật chia để trị chọn chốt (pivot).",
                "Bước 2: Thiết lập điều kiện cơ sở: if len(arr) <= 1: return arr.",
                "Bước 3: Dùng module time và random để sinh một danh sách 5,000 số nguyên ngẫu nhiên.",
                "Bước 4: Đo thời gian thực thi: t0 = time.time(); quick_sort(arr); print('Quick Sort:', time.time() - t0)."
            ]
            prac_challenge = "Phân tích trường hợp xấu nhất (Worst-case) của Quick Sort dẫn đến O(N^2) khi nào và cách khắc phục bằng cách chọn Randomized Pivot."
            prac_tip = "Với Python, đệ quy mặc định giới hạn 1000 tầng, có thể tăng lên bằng sys.setrecursionlimit()."
            prac_checklist = ["Cài đặt đúng Base Case cho hàm đệ quy", "Chạy thử thành công trên mảng ngẫu nhiên", "Hiểu bản chất độ phức tạp O(N log N)"]

        elif "AI" in title or "Trí tuệ" in title or "Machine Learning" in title or "Nơ-ron" in title or "LLM" in title:
            sec2_content = "Trí tuệ nhân tạo (AI) và Học máy (Machine Learning) là bước nhảy vọt vĩ đại, biến máy tính từ cỗ máy chỉ biết làm theo lệnh cứng nhắc thành thực thể có khả năng tự học hỏi từ dữ liệu khổng lồ."
            sec2_example = "Ví dụ: Thuật toán nhận diện khuôn mặt trên điện thoại học từ hàng triệu bức ảnh để tự trích xuất các đặc trưng mắt, mũi, miệng. Chatbot ChatGPT hay Gemini được huấn luyện trên hàng nghìn tỷ từ văn bản để hiểu ngôn ngữ tự nhiên của con người."
            sec3_content = "Hiện tượng Quá khớp (Overfitting): Mô hình học vẹt quá mức dữ liệu huấn luyện (Training data), đạt độ chính xác 100% khi luyện tập nhưng khi gặp dữ liệu thực tế mới lạ thì dự đoán sai be bét."
            sec3_tip = "Luôn chia dữ liệu thành 2 tập riêng biệt: Tập Huấn luyện (Train set ~ 80%) và Tập Kiểm thử (Test set ~ 20%) để đánh giá khách quan năng lực tổng quát hóa của mô hình."
            memorize = "🧠 Dữ liệu là thức ăn của AI, huấn luyện chống Overfitting, đạo đức số soi sáng công nghệ!"
            prac_title = "Phòng Lab Trí tuệ Nhân tạo: Trải nghiệm Huấn luyện Mô hình Thị giác Máy tính"
            prac_goal = "Thu thập tập dữ liệu ảnh, huấn luyện mô hình phân loại cử chỉ tay bằng Teachable Machine hoặc Scikit-Learn."
            prac_steps = [
                "Bước 1: Truy cập công cụ Teachable Machine của Google qua trình duyệt.",
                "Bước 2: Tạo 2 lớp nhãn dữ liệu (Classes): Lớp 1: 'GioTay' (thu thập 30 ảnh qua webcam); Lớp 2: 'KhongGioTay' (30 ảnh tư thế bình thường).",
                "Bước 3: Nhấn nút 'Train Model' để máy tính tự động tối ưu hóa trọng số mạng nơ-ron.",
                "Bước 4: Thử nghiệm thực tế trước webcam: giơ tay lên và quan sát thanh xác suất dự đoán (Confidence score) đạt trên 95%."
            ]
            prac_challenge = "Đưa ra các góc chụp ảnh mới trong điều kiện ánh sáng yếu để kiểm tra giới hạn của mô hình và phân tích nguyên nhân."
            prac_tip = "Chất lượng và độ đa dạng của dữ liệu (Data Quality & Diversity) quyết định 80% độ thông minh của mô hình AI."
            prac_checklist = ["Thu thập đủ mẫu dữ liệu đại diện", "Huấn luyện mô hình hội tụ thành công", "Đánh giá được độ chính xác trên tập dữ liệu kiểm thử"]

        elif "Web" in title or "HTML" in title or "CSS" in title or "JavaScript" in title:
            sec2_content = "Bộ ba HTML5, CSS3 và JavaScript là nền tảng cốt lõi của mọi trang web trên toàn cầu: HTML tạo khung xương, CSS tạo vẻ đẹp diện mạo, JavaScript thổi hồn sức sống tương tác."
            sec2_example = "Ví dụ: HTML tạo nút bấm '<button>Đăng ký</button>', CSS tô màu nút bấm thành màu xanh gradient nổi bật và bo tròn góc, JavaScript lắng nghe sự kiện nhấp chuột (addEventListener) để kiểm tra mật khẩu và gửi lời chúc mừng."
            sec3_content = "Quên đóng thẻ HTML hoặc viết sai cú pháp CSS Selector khiến toàn bộ giao diện trang web bị vỡ khung hình."
            sec3_tip = "Dùng công cụ Chrome DevTools (nhấn F12) để kiểm tra phần tử (Inspect Element) và xem trước các thay đổi CSS ngay tức thì."
            memorize = "🌐 HTML dựng khung sườn, CSS điểm tô diện mạo, JavaScript tương tác thông minh!"
            prac_title = "Studio Lập trình Web: Xây dựng Giao diện Thẻ Sản phẩm Động"
            prac_goal = "Tạo một trang web gồm cấu trúc HTML5 ngữ nghĩa, định kiểu CSS Flexbox hiện đại và nút bấm tương tác JavaScript."
            prac_steps = [
                "Bước 1: Tạo tệp 'index.html', khai báo khung sườn chuẩn với <!DOCTYPE html>, <html>, <head> và <body>.",
                "Bước 2: Sử dụng các thẻ ngữ nghĩa: <header>, <main>, <article class='card'>, <h3>, <p> và <button id='btnBuy'>.",
                "Bước 3: Viết CSS trong thẻ <style>: thiết lập display: flex; justify-content: center; border-radius: 8px; box-shadow.",
                "Bước 4: Viết kịch bản JavaScript: document.getElementById('btnBuy').addEventListener('click', () => alert('Đã thêm vào giỏ hàng!'));"
            ]
            prac_challenge = "Thêm thuộc tính transition và :hover trong CSS để tạo hiệu ứng phóng to thẻ khi người dùng rê chuột qua."
            prac_tip = "Sử dụng đơn vị rem và Flexbox/Grid để giao diện hiển thị co giãn đẹp mắt trên cả điện thoại di động và máy tính (Responsive Design)."
            prac_checklist = ["Dùng đúng thẻ HTML5 chuẩn ngữ nghĩa", "Định dạng CSS Flexbox căn giữa hoàn hảo", "Bắt sự kiện click JavaScript thành công"]

        elif "Mạng" in title or "OSI" in title or "TCP/IP" in title or "IP" in title or "Router" in title or "An ninh" in title or "Mã hóa" in title:
            sec2_content = "Kiến trúc mạng máy tính và an ninh thông tin là lá chắn bảo vệ toàn bộ không gian số quốc gia trước các cuộc tấn công mạng nguy hiểm."
            sec2_example = "Ví dụ: Khi em gửi tin nhắn qua Zalo, mô hình TCP/IP chia tin nhắn thành các gói tin (packet), gán địa chỉ IP người gửi và người nhận, mã hóa bằng giao thức HTTPS/TLS, rồi các thiết bị Router sẽ tìm tuyến đường ngắn nhất trên Internet để chuyển gói tin tới bạn bè chỉ sau 0.05 giây."
            sec3_content = "Nhầm lẫn giữa Tầng Vận chuyển (TCP - đảm bảo tin cậy không mất gói; UDP - truyền nhanh thời gian thực cho video/game) và Tầng Mạng (IP - đánh địa chỉ định tuyến)."
            sec3_tip = "Nhớ câu thần chú mô hình OSI 7 tầng: 'All People Seem To Need Data Processing' (Application, Presentation, Session, Transport, Network, Data Link, Physical)."
            memorize = "🛡️ TCP/IP phân tầng gói tin, mã hóa HTTPS chống nghe lén, Router dẫn đường chính xác!"
            prac_title = "Phòng Lab An ninh Mạng: Phân tích Gói tin Mạng & Kiểm tra Chứng chỉ SSL"
            prac_goal = "Khảo sát luồng gói tin TCP bằng Wireshark hoặc kiểm tra cấu trúc chứng chỉ SSL/TLS trên trình duyệt web."
            prac_steps = [
                "Bước 1: Mở trình duyệt web Google Chrome, truy cập vào một trang web ngân hàng hoặc trang tin tức có ổ khóa HTTPS.",
                "Bước 2: Nhấp chuột vào biểu tượng ổ khóa cạnh thanh địa chỉ URL, chọn 'Kết nối an toàn' -> 'Chứng chỉ hợp lệ'.",
                "Bước 3: Quan sát thông tin cơ quan cấp chứng chỉ (Issuer CA: Let's Encrypt, DigiCert...), thuật toán mã hóa (RSA 2048 bit hoặc ECC) và thời hạn hiệu lực.",
                "Bước 4: Mở cmd và thực hiện lệnh 'nslookup vnexpress.net' để quan sát máy chủ DNS phân giải tên miền sang địa chỉ IP thực."
            ]
            prac_challenge = "Phân tích vì sao giao thức HTTP gửi dữ liệu dạng bản rõ (plaintext) lại có thể bị kẻ tấn công tấn công trung gian (Man-in-the-Middle)."
            prac_tip = "Luôn kiểm tra kỹ tên miền URL trước khi nhập mật khẩu để tránh các trang web lừa đảo giả mạo (Phishing)."
            prac_checklist = ["Hiểu rõ vai trò phân tầng của mô hình mạng", "Kiểm tra được chứng chỉ số SSL/TLS", "Hiểu cơ chế bảo mật truyền tin mã hóa"]

        else:
            sec2_content = f"Chuyên đề '{title}' mở rộng tầm nhìn công nghệ thế hệ mới cho học sinh THPT chuẩn bị bước vào giảng đường đại học và thị trường việc làm toàn cầu."
            sec2_example = "Ví dụ: Ứng dụng các quy trình phát triển phần mềm chuyên nghiệp, tư duy thuật toán tối ưu và tinh thần trách nhiệm với xã hội trong kỷ nguyên số hóa toàn diện."
            sec3_content = "Coi nhẹ vấn đề bản quyền trí tuệ và đạo đức số khi ứng dụng công nghệ trí tuệ nhân tạo."
            sec3_tip = "Luôn tuân thủ nguyên tắc minh bạch, công bằng và tôn trọng quyền riêng tư dữ liệu người dùng."
            memorize = "🚀 Tư duy công nghệ bứt phá, bản lĩnh làm chủ tương lai số hóa toàn cầu!"
            prac_title = f"Dự án Nghiên cứu & Ứng dụng: {title}"
            prac_goal = f"Hoàn thiện chuyên đề thực hành nâng cao về {title} theo chuẩn đầu ra GDPT 2018."
            prac_steps = [
                "Bước 1: Nghiên cứu tài liệu kỹ thuật và xác định các yêu cầu bài toán đặt ra.",
                "Bước 2: Lập kế hoạch thiết kế kiến trúc hệ thống hoặc thuật toán giải quyết.",
                "Bước 3: Triển khai cài đặt mã nguồn hoặc xây dựng mô hình thử nghiệm.",
                "Bước 4: Đánh giá độ phức tạp, kiểm thử lỗi và viết tài liệu báo cáo kỹ thuật."
            ]
            prac_challenge = "Đề xuất giải pháp cải tiến hiệu năng hoặc mở rộng tính năng cho hệ thống."
            prac_tip = "Áp dụng phương pháp kiểm thử đơn vị (Unit Test) để đảm bảo chất lượng từng module mã nguồn."
            prac_checklist = ["Nắm vững lý thuyết chuyên sâu", "Hoàn thành bài thực hành dự án", "Báo cáo phân tích chuyên nghiệp"]

    # Đóng gói đối tượng theory
    node["lesson_data"]["theory"] = {
        "overview": overview,
        "sections": [
            {
                "title": sec1_title,
                "content": sec1_content,
                "example": f"Trọng tâm YCCĐ bài học: {', '.join(goals[:2])}." if goals else "Nắm vững lý thuyết cơ bản và kỹ năng thực hành chuẩn.",
                "tip": f"Bài học tương ứng với các SGK: {kntt} | {cd} | {ctst}."
            },
            {
                "title": sec2_title,
                "content": sec2_content,
                "example": sec2_example,
                "tip": "Hãy liên hệ khái niệm trên với những đồ vật hoặc hoạt động quen thuộc quanh em!"
            },
            {
                "title": sec3_title,
                "content": sec3_content,
                "example": "Thử làm bài tập ví dụ trong sách giáo khoa để kiểm tra độ hiểu sâu của em.",
                "tip": sec3_tip
            }
        ],
        "memorize": memorize
    }

    # Đóng gói đối tượng practice
    node["lesson_data"]["practice"] = {
        "mission": {
            "title": prac_title,
            "goal": prac_goal,
            "steps": prac_steps,
            "challenge": prac_challenge,
            "tip": prac_tip
        },
        "checklist": prac_checklist
    }

    return node

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    curriculum_path = os.path.join(root, "curriculum.json")

    with open(curriculum_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    nodes = data.get("nodes", [])
    print(f"Bắt đầu bổ sung Lí thuyết & Thực hành cho {len(nodes)} bài học...")

    enriched_nodes = []
    for node in nodes:
        enriched_node = enrich_node(node)
        enriched_nodes.append(enriched_node)

    data["nodes"] = enriched_nodes

    with open(curriculum_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"ĐÃ HOÀN THÀNH: Đã ghi cấu trúc Lí thuyết & Thực hành chuẩn cho toàn bộ {len(enriched_nodes)} bài học vào curriculum.json!")

if __name__ == "__main__":
    main()
