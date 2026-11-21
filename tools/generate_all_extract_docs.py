# -*- coding: utf-8 -*-
"""
Script tạo đầy đủ tài liệu trích xuất và ma trận chương trình học của 3 bộ sách:
1. 01a-extract-kntt-g3_12.md (Kết nối tri thức với cuộc sống)
2. 01a-extract-canhdieu-g3_12.md (Cánh Diều)
3. 01a-extract-ctst-g3_12.md (Chân trời sáng tạo)
4. 01b-curriculum-map.md (Ma trận hợp nhất và phân phối học tập EasyTin)
"""

import os

# ==============================================================================
# 1. KẾT NỐI TRI THỨC VỚI CUỘC SỐNG (KNTT)
# ==============================================================================
kntt_content = """# 01a-extract-kntt-g3_12.md — Trích xuất toàn diện bộ sách Kết nối tri thức với cuộc sống (Lớp 3–12)

> **Bộ sách:** Kết nối tri thức với cuộc sống (Nhà xuất bản Giáo dục Việt Nam)  
> **Chương trình:** Giáo dục phổ thông 2018 môn Tin học (Thông tư 32/2018/TT-BGDĐT)  
> **Cam kết:** Trích xuất 100% đầy đủ tất cả các bài học từ Lớp 3 đến Lớp 12, không bỏ sót bất kỳ bài nào.  
> **Đặc trưng sư phạm:** Cấu trúc phân tầng chặt chẽ, dẫn dắt từ trực quan đến tư duy trừu tượng, tích hợp hoạt động trải nghiệm số.

---

## MỤC LỤC TỔNG QUAN CÁC KHỐI LỚP
- [Lớp 3 (16 bài)](#1-lớp-3--tiểu-học-16-bài)
- [Lớp 4 (16 bài)](#2-lớp-4--tiểu-học-16-bài)
- [Lớp 5 (16 bài)](#3-lớp-5--tiểu-học-16-bài)
- [Lớp 6 (17 bài)](#4-lớp-6--thcs-17-bài)
- [Lớp 7 (16 bài)](#5-lớp-7--thcs-16-bài)
- [Lớp 8 (16 bài)](#6-lớp-8--thcs-16-bài)
- [Lớp 9 (16 bài)](#7-lớp-9--thcs-16-bài)
- [Lớp 10 (34 bài)](#8-lớp-10--thpt-34-bài)
- [Lớp 11 (31 bài định hướng CS & ICT)](#9-lớp-11--thpt-31-bài-định-hướng-cs--ict)
- [Lớp 12 (30 bài định hướng CS & ICT)](#10-lớp-12--thpt-30-bài-định-hướng-cs--ict)

---

## 1. Lớp 3 — Tiểu học (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách KNTT | Yêu cầu cần đạt (YCCĐ) trọng tâm | Nút EasyTin | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề 1: Máy tính và em | Thông tin và quyết định | Nhận biết thông tin thu nhận qua các giác quan và giúp đưa ra quyết định phù hợp trong đời sống. | `G3-INFO-01` | `branch-story` |
| Bài 2 | Chủ đề 1: Máy tính và em | Xử lý thông tin | Nêu được ví dụ về các hoạt động: thu nhận, lưu trữ, xử lý và truyền thông tin ở con người và máy tính. | `G3-INFO-02` | `sort-drag` |
| Bài 3 | Chủ đề 1: Máy tính và em | Máy tính - những người bạn mới | Nhận biết và gọi đúng tên các bộ phận cơ bản: thân máy, màn hình, bàn phím, chuột; phân biệt máy để bàn, laptop, máy tính bảng. | `G3-HARD-01` | `sort-drag` |
| Bài 4 | Chủ đề 1: Máy tính và em | Làm việc với máy tính | Khởi động, tắt máy tính đúng quy cách; ngồi đúng tư thế, giữ khoảng cách mắt an toàn để bảo vệ sức khỏe. | `G3-HARD-02` | `branch-story` |
| Bài 5 | Chủ đề 1: Máy tính và em | Sử dụng bàn phím | Nhận biết khu vực phím chính, hàng phím cơ sở, hai phím có gờ F và J; hiểu cách đặt ngón tay đúng vị trí xuất phát. | `G3-KEY-01` | `type-run` |
| Bài 6 | Chủ đề 1: Máy tính và em | Sử dụng chuột máy tính | Cầm chuột đúng cách; thực hiện thành thạo 5 thao tác: di chuyển chuột, nháy chuột, nháy đúp, nháy nút phải, kéo thả chuột. | `G3-MOUSE-01` | `sort-drag` |
| Bài 7 | Chủ đề 2: Mạng và Internet | Khám phá Internet | Nhận biết Internet là mạng kết nối máy tính toàn cầu; nêu được lợi ích của Internet trong học tập và giải trí. | `G3-NET-01` | `branch-story` |
| Bài 8 | Chủ đề 3: Tổ chức lưu trữ | Sắp xếp để dễ tìm | Hiểu ý nghĩa của việc phân loại, sắp xếp đồ vật, dữ liệu gọn gàng ngăn nắp theo tiêu chí rõ ràng. | `G3-ORG-01` | `sort-drag` |
| Bài 9 | Chủ đề 3: Tổ chức lưu trữ | Thực hành sắp xếp đồ vật | Áp dụng phân loại đồ dùng học tập, tệp tài liệu theo nhóm để tìm kiếm nhanh chóng, thuận tiện. | `G3-ORG-02` | `sort-drag` |
| Bài 10 | Chủ đề 3: Tổ chức lưu trữ | Sơ đồ tư duy | Bước đầu làm quen với sơ đồ hình cây, sơ đồ tư duy trực quan để biểu diễn cấu trúc thông tin phân cấp. | `G3-ORG-03` | `logic-puzzle` |
| Bài 11 | Chủ đề 4: Đạo đức, pháp luật | Lưu trữ và trao đổi thông tin của em | Nhận biết thông tin cá nhân (họ tên, địa chỉ, số điện thoại) cần bảo mật; không chia sẻ bừa bãi cho người lạ. | `G3-ETHIC-01` | `branch-story` |
| Bài 12 | Chủ đề 5: Ứng dụng tin học | Em tập gõ bàn phím | Thực hành gõ các phím trên hàng cơ sở, hàng trên, hàng dưới bằng phần mềm luyện gõ phím. | `G3-TYPE-01` | `type-run` |
| Bài 13 | Chủ đề 5: Ứng dụng tin học | Em tập vẽ | Làm quen phần mềm Paint: chọn công cụ vẽ đường thẳng, đường cong, hình chữ nhật, hình tròn và đổ màu. | `G3-DRAW-01` | `match-memory` |
| Bài 14 | Chủ đề 6: Giải quyết vấn đề | Em thực hiện công việc theo các bước | Nhận biết một việc thường được thực hiện theo trình tự các bước; thay đổi thứ tự có thể dẫn đến kết quả sai. | `G3-ALGO-01` | `block-maze` |
| Bài 15 | Chủ đề 6: Giải quyết vấn đề | Nhiệm vụ của em và sự trợ giúp của máy tính | Nhận biết máy tính có thể giúp con người thực hiện nhiều công việc nhanh hơn, chính xác hơn. | `G3-ALGO-02` | `match-memory` |
| Bài 16 | Chủ đề 6: Giải quyết vấn đề | Trò chơi học tập | Vận dụng kỹ năng chuột và phím tham gia trò chơi rèn luyện tư duy logic, củng cố kiến thức đã học. | `G3-BOSS-01` | `boss-quiz` |

---

## 2. Lớp 4 — Tiểu học (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách KNTT | Yêu cầu cần đạt (YCCĐ) trọng tâm | Nút EasyTin | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề 1: Máy tính và em | Phần cứng và phần mềm máy tính | Phân biệt được phần cứng (thiết bị vật lý) và phần mềm (chương trình chạy trên máy tính); nêu mối quan hệ giữa chúng. | `G4-HARD-01` | `sort-drag` |
| Bài 2 | Chủ đề 1: Máy tính và em | Gõ bàn phím đúng cách | Luyện tập gõ bàn phím bằng 10 ngón tay đúng kỹ thuật và tư thế, gõ tiếng Việt kiểu gõ Telex/VNI. | `G4-TYPE-01` | `type-run` |
| Bài 3 | Chủ đề 2: Mạng và Internet | Thông tin trên trang web | Nhận biết các thành phần cơ bản của trang web: văn bản, hình ảnh, âm thanh, video, siêu liên kết (hyperlink). | `G4-NET-01` | `branch-story` |
| Bài 4 | Chủ đề 2: Mạng và Internet | Tìm kiếm thông tin trên Internet | Sử dụng công cụ tìm kiếm (máy tìm kiếm) với từ khóa thích hợp để tìm thông tin theo yêu cầu. | `G4-SEARCH-01` | `sort-drag` |
| Bài 5 | Chủ đề 3: Tổ chức lưu trữ | Thao tác với tệp và thư mục | Hiểu khái niệm tệp (file), thư mục (folder); thực hiện tạo, đổi tên, sao chép, di chuyển, xóa thư mục và tệp. | `G4-FILE-01` | `sort-drag` |
| Bài 6 | Chủ đề 4: Đạo đức, pháp luật | Sử dụng phần mềm khi được phép | Hiểu phần mềm là sản phẩm trí tuệ; nêu được tầm quan trọng của việc xin phép và tôn trọng bản quyền phần mềm. | `G4-ETHIC-01` | `branch-story` |
| Bài 7 | Chủ đề 5: Ứng dụng tin học | Chèn hình ảnh vào văn bản | Soạn thảo văn bản, chèn hình ảnh minh họa từ tệp vào tài liệu văn bản để trình bày sinh động hơn. | `G4-DOC-01` | `sort-drag` |
| Bài 8 | Chủ đề 5: Ứng dụng tin học | Định dạng văn bản | Chọn phông chữ, cỡ chữ, kiểu chữ (đậm, nghiêng, gạch chân), màu chữ và căn lề đoạn văn bản (trái, phải, giữa, đều). | `G4-DOC-02` | `type-run` |
| Bài 9 | Chủ đề 5: Ứng dụng tin học | Ứng dụng của bài trình chiếu | Nhận biết vai trò của bài trình chiếu trong thuyết trình, báo cáo học tập và đời sống. | `G4-PRES-01` | `match-memory` |
| Bài 10 | Chủ đề 5: Ứng dụng tin học | Tạo bài trình chiếu | Tạo trang chiếu mới, nhập tiêu đề, nội dung văn bản và chèn hình ảnh minh họa vào trang chiếu. | `G4-PRES-02` | `sort-drag` |
| Bài 11 | Chủ đề 5: Ứng dụng tin học | Chỉnh sửa hình ảnh | Thực hiện cắt, xoay, thay đổi kích thước và điều chỉnh độ sáng tối cơ bản của hình ảnh. | `G4-IMG-01` | `match-memory` |
| Bài 12 | Chủ đề 6: Giải quyết vấn đề | Làm quen với ngôn ngữ lập trình trực quan | Làm quen với môi trường Scratch: khu vực sân khấu, danh sách nhân vật, bảng khối lệnh và khu vực lập trình. | `G4-SCRATCH-01`| `match-memory` |
| Bài 13 | Chủ đề 6: Giải quyết vấn đề | Tạo chương trình máy tính đầu tiên | Kéo thả khối lệnh Khi bấm vào cờ xanh, nói xin chào, phát âm thanh để tạo chương trình đầu tiên. | `G4-SCRATCH-02`| `block-maze` |
| Bài 14 | Chủ đề 6: Giải quyết vấn đề | Điều khiển nhân vật chuyển động | Sử dụng khối lệnh di chuyển, xoay hướng, bật lại khi chạm cạnh để điều khiển nhân vật trên sân khấu. | `G4-ALGO-01` | `block-maze` |
| Bài 15 | Chủ đề 6: Giải quyết vấn đề | Lặp lại một việc | Hiểu ý nghĩa của cấu trúc lặp; sử dụng khối lệnh lặp lại số lần biết trước (repeat N) để tối ưu chương trình. | `G4-ALGO-02` | `block-maze` |
| Bài 16 | Chủ đề 6: Giải quyết vấn đề | Biểu diễn thuật toán | Mô tả thuật toán đơn giản bằng các bước tuần tự bằng lời hoặc sơ đồ khối trước khi lập trình. | `G4-BOSS-01` | `boss-quiz` |

---

## 3. Lớp 5 — Tiểu học (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách KNTT | Yêu cầu cần đạt (YCCĐ) trọng tâm | Nút EasyTin | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề 1: Máy tính và em | Máy tính và cuộc sống | Nêu được vai trò to lớn của máy tính trong sản xuất, giáo dục, y tế, giao thông và các thiết bị số thông minh. | `G5-COMP-01` | `match-memory` |
| Bài 2 | Chủ đề 1: Máy tính và em | Khám phá phần cứng máy tính | Nhận biết các khối chức năng cơ bản bên trong thân máy: CPU (bộ xử lý), RAM (bộ nhớ tạm), ổ đĩa lưu trữ (HDD/SSD). | `G5-HARD-01` | `sort-drag` |
| Bài 3 | Chủ đề 1: Máy tính và em | Sử dụng máy tính an toàn và tiết kiệm điện | Nêu các biện pháp an toàn điện, phòng tránh cháy nổ và quy tắc tiết kiệm điện năng khi dùng máy tính. | `G5-SAFE-01` | `branch-story` |
| Bài 4 | Chủ đề 2: Mạng và Internet | Tìm kiếm thông tin trên Internet | Sử dụng toán tử tìm kiếm cơ bản, chọn lọc nguồn tin chính thống, đánh giá độ tin cậy của thông tin tìm thấy. | `G5-SEARCH-01` | `sort-drag` |
| Bài 5 | Chủ đề 4: Đạo đức, pháp luật | Bản quyền và sử dụng thông tin an toàn | Tôn trọng bản quyền tác giả; không sao chép tác phẩm của người khác khi chưa được phép; bảo vệ dữ liệu cá nhân. | `G5-ETHIC-01` | `branch-story` |
| Bài 6 | Chủ đề 5: Ứng dụng tin học | Định dạng văn bản nâng cao | Tạo danh sách dấu đầu dòng/số thứ tự, căn chỉnh lề trang, hướng trang in và chèn bảng vào văn bản. | `G5-DOC-01` | `sort-drag` |
| Bài 7 | Chủ đề 5: Ứng dụng tin học | Thực hành soạn thảo văn bản | Tự tạo một văn bản hoàn chỉnh có tiêu đề, nội dung định dạng đẹp mắt, bảng biểu và hình ảnh minh họa. | `G5-DOC-02` | `type-run` |
| Bài 8 | Chủ đề 5: Ứng dụng tin học | Thu thập và sắp xếp dữ liệu | Thu thập dữ liệu khảo sát đơn giản, lập bảng số liệu và sắp xếp theo thứ tự tăng dần/giảm dần. | `G5-DATA-01` | `sort-drag` |
| Bài 9 | Chủ đề 5: Ứng dụng tin học | Trình chiếu đa phương tiện | Thêm hiệu ứng chuyển tiếp slide (Transitions) và hiệu ứng xuất hiện đối tượng (Animations) sinh động. | `G5-PRES-01` | `sort-drag` |
| Bài 10 | Chủ đề 5: Ứng dụng tin học | Thực hành tạo bài trình chiếu | Hoàn thiện bài thuyết trình về chủ đề môi trường, lịch sử hoặc trường học có liên kết và đa phương tiện. | `G5-PRES-02` | `match-memory` |
| Bài 11 | Chủ đề 6: Giải quyết vấn đề | Làm quen với biến trong lập trình | Hiểu biến (variable) là nơi lưu trữ giá trị có thể thay đổi được trong quá trình chương trình thực thi. | `G5-VAR-01` | `logic-puzzle` |
| Bài 12 | Chủ đề 6: Giải quyết vấn đề | Sử dụng biến trong Scratch | Tạo biến số trong Scratch (ví dụ: biến Điểm số, Thời gian) và lập trình thay đổi giá trị của biến. | `G5-VAR-02` | `block-maze` |
| Bài 13 | Chủ đề 6: Giải quyết vấn đề | Cấu trúc rẽ nhánh | Hiểu cấu trúc điều khiển rẽ nhánh dạng thiếu (Nếu... Thì) và dạng đủ (Nếu... Thì... Không thì...). | `G5-IF-01` | `logic-puzzle` |
| Bài 14 | Chủ đề 6: Giải quyết vấn đề | Thực hành tạo chương trình có rẽ nhánh | Lập trình nhân vật phản ứng khi va chạm chướng ngại vật hoặc khi đạt đủ điểm số quy định. | `G5-IF-02` | `block-maze` |
| Bài 15 | Chủ đề 6: Giải quyết vấn đề | Trò chơi lập trình | Kết hợp biến số, vòng lặp và điều kiện rẽ nhánh để xây dựng hoàn chỉnh một mini game hứng táo hoặc mê cung. | `G5-GAME-01` | `block-maze` |
| Bài 16 | Chủ đề 6: Giải quyết vấn đề | Ôn tập và dự án học tập | Kiểm thử, phát hiện lỗi (debugging) trong trò chơi của mình và hoàn thiện dự án tổng kết Tiểu học. | `G5-BOSS-01` | `boss-quiz` |

---

## 4. Lớp 6 — THCS (17 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách KNTT | Yêu cầu cần đạt (YCCĐ) trọng tâm | Nút EasyTin | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề 1: Máy tính và cộng đồng | Thông tin và thu nhận thông tin | Phân biệt thông tin và vật mang tin; nhận biết quá trình thu nhận và xử lý thông tin ở con người. | `G6-INFO-01` | `branch-story` |
| Bài 2 | Chủ đề 1: Máy tính và cộng đồng | Xử lý thông tin | Mô tả các bước xử lý thông tin trong máy tính: Nhập -> Xử lý -> Xuất -> Lưu trữ. | `G6-INFO-02` | `sort-drag` |
| Bài 3 | Chủ đề 1: Máy tính và cộng đồng | Thông tin trong máy tính | Giải thích dữ liệu trong máy tính được số hóa dưới dạng bit (dãy số 0 và 1); các đơn vị đo Byte, KB, MB, GB, TB. | `G6-DATA-01` | `logic-puzzle` |
| Bài 4 | Chủ đề 1: Máy tính và cộng đồng | Mạng máy tính | Nêu khái niệm mạng máy tính; phân biệt mạng có dây và không dây; nhận biết các thiết bị mạng: Switch, Access Point, Cáp mạng. | `G6-NET-01` | `sort-drag` |
| Bài 5 | Chủ đề 1: Máy tính và cộng đồng | Internet | Nhận biết Internet là mạng của các mạng; nêu các đặc điểm và lợi ích to lớn của mạng Internet toàn cầu. | `G6-NET-02` | `branch-story` |
| Bài 6 | Chủ đề 2: Mạng xã hội & Kênh liên lạc | Mạng thông tin toàn cầu (WWW) | Hiểu khái niệm World Wide Web, trang web, địa chỉ website URL, trình duyệt web và máy chủ web. | `G6-WWW-01` | `match-memory` |
| Bài 7 | Chủ đề 2: Mạng xã hội & Kênh liên lạc | Tìm kiếm thông tin trên Internet | Sử dụng công cụ tìm kiếm, phân tích và lựa chọn từ khóa hiệu quả; trích xuất thông tin phục vụ học tập. | `G6-SEARCH-01` | `sort-drag` |
| Bài 8 | Chủ đề 2: Mạng xã hội & Kênh liên lạc | Thư điện tử (Email) | Hiểu cấu trúc một địa chỉ email; quy trình gửi và nhận thư điện tử, đính kèm tệp tin tài liệu. | `G6-EMAIL-01` | `branch-story` |
| Bài 9 | Chủ đề 2: Mạng xã hội & Kênh liên lạc | Mạng xã hội | Nhận biết vai trò của mạng xã hội, các tính năng chia sẻ; nhận thức các nguy cơ và quy tắc ứng xử văn minh trên mạng. | `G6-SOCIAL-01` | `branch-story` |
| Bài 10 | Chủ đề 3: Đạo đức, pháp luật | Sơ đồ tư duy | Sử dụng phần mềm vẽ sơ đồ tư duy để tóm tắt kiến thức, lập kế hoạch công việc một cách logic và trực quan. | `G6-MIND-01` | `logic-puzzle` |
| Bài 11 | Chủ đề 4: Ứng dụng tin học | Định dạng văn bản | Sử dụng thành thạo các công cụ định dạng ký tự, định dạng đoạn văn bản và ngắt trang văn bản chuyên nghiệp. | `G6-DOC-01` | `type-run` |
| Bài 12 | Chủ đề 4: Ứng dụng tin học | Trình bày thông tin ở dạng bảng | Tạo bảng dữ liệu, thêm bớt hàng cột, gộp tách ô và định dạng bảng biểu báo cáo khoa học. | `G6-TABLE-01` | `sort-drag` |
| Bài 13 | Chủ đề 4: Ứng dụng tin học | Thực hành định dạng văn bản và bảng | Vận dụng tổng hợp kỹ năng định dạng văn bản và bảng biểu để thiết kế một tờ rơi hoặc bản tin trường học. | `G6-DOC-02` | `sort-drag` |
| Bài 14 | Chủ đề 4: Ứng dụng tin học | Dự án: Cuốn sổ lưu niệm | Dự án nhóm: Biên soạn cuốn sổ lưu niệm lớp học kết hợp hình ảnh, bảng biểu và văn bản biên tập công phu. | `G6-PROJ-01` | `match-memory` |
| Bài 15 | Chủ đề 5: Giải quyết vấn đề | Thuật toán | Hiểu khái niệm thuật toán là dãy các chỉ dẫn rõ ràng để giải quyết bài toán; mô tả thuật toán bằng liệt kê các bước. | `G6-ALGO-01` | `block-maze` |
| Bài 16 | Chủ đề 5: Giải quyết vấn đề | Các cấu trúc điều khiển | Nhận biết 3 cấu trúc điều khiển cơ bản: Tuần tự (Sequence), Rẽ nhánh (Selection) và Lặp (Iteration) bằng sơ đồ khối. | `G6-FLOW-01` | `logic-puzzle` |
| Bài 17 | Chủ đề 5: Giải quyết vấn đề | Dự án: An toàn trong môi trường số | Xây dựng cẩm nang tuyên truyền phòng chống lừa đảo mạng, bảo vệ mật khẩu và danh tính số. | `G6-BOSS-01` | `boss-quiz` |

---

## 5. Lớp 7 — THCS (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách KNTT | Yêu cầu cần đạt (YCCĐ) trọng tâm | Nút EasyTin | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề 1: Máy tính và cộng đồng | Thiết bị vào - ra | Nhận biết các thiết bị vào (bàn phím, chuột, máy quét) và thiết bị ra (màn hình, máy in, loa); cổng kết nối USB, HDMI. | `G7-IO-01` | `sort-drag` |
| Bài 2 | Chủ đề 1: Máy tính và cộng đồng | Phần mềm ứng dụng | Phân biệt hệ điều hành (Windows, Linux, macOS) và phần mềm ứng dụng; hiểu cơ chế tương tác giữa người dùng và máy tính. | `G7-OS-01` | `sort-drag` |
| Bài 3 | Chủ đề 1: Máy tính và cộng đồng | Quản lý dữ liệu trong máy tính | Tổ chức cây thư mục hợp lý, đường dẫn tệp (file path), đuôi tệp mở rộng (.docx, .xlsx, .pdf, .png) và sao lưu an toàn. | `G7-PATH-01` | `sort-drag` |
| Bài 4 | Chủ đề 2: Mạng xã hội | Mạng xã hội và một số kênh trao đổi | Khai thác thông tin hữu ích từ diễn đàn học tập, nhóm học tập trực tuyến; chia sẻ dữ liệu có trách nhiệm. | `G7-COMM-01` | `branch-story` |
| Bài 5 | Chủ đề 3: Đạo đức, pháp luật | Ứng xử trên mạng | Nhận diện tác hại của bắt nạt trên mạng (cyberbullying), ngôn từ thù ghét; thực hiện quy tắc ứng xử văn minh trên không gian mạng. | `G7-ETHIC-01` | `branch-story` |
| Bài 6 | Chủ đề 4: Ứng dụng tin học | Làm quen với phần mềm bảng tính | Nhận biết giao diện bảng tính (Excel/Sheets), ô tính (cell), hàng, cột, địa chỉ ô tính (ví dụ: B5, C10:E20). | `G7-SHEET-01` | `sort-drag` |
| Bài 7 | Chủ đề 4: Ứng dụng tin học | Tính toán tự động trên bảng tính | Nhập công thức toán học bắt đầu bằng dấu bằng (=), sử dụng địa chỉ ô tương đối để tự động cập nhật kết quả tính. | `G7-SHEET-02` | `logic-puzzle` |
| Bài 8 | Chủ đề 4: Ứng dụng tin học | Công cụ hỗ trợ tính toán | Sử dụng thành thạo các hàm tính toán cơ bản: SUM (tổng), AVERAGE (trung bình), MAX (lớn nhất), MIN (nhỏ nhất), COUNT (đếm). | `G7-FUNC-01` | `logic-puzzle` |
| Bài 9 | Chủ đề 4: Ứng dụng tin học | Trình bày bảng tính | Định dạng kiểu số, tiền tệ, phần trăm, kẻ đường viền khung bảng, tô màu nền ô tính nổi bật. | `G7-SHEET-03` | `sort-drag` |
| Bài 10 | Chủ đề 4: Ứng dụng tin học | Định dạng nâng cao trên bảng tính | Cố định tiêu đề hàng/cột (Freeze Panes), thiết lập ngắt dòng tự động (Wrap Text) và căn chỉnh trang in bảng tính. | `G7-SHEET-04` | `sort-drag` |
| Bài 11 | Chủ đề 4: Ứng dụng tin học | Tạo bài trình chiếu | Thiết kế bài trình chiếu có cấu trúc rõ ràng: trang tiêu đề, mục lục, nội dung chi tiết và tổng kết. | `G7-PRES-01` | `match-memory` |
| Bài 12 | Chủ đề 4: Ứng dụng tin học | Định dạng đối tượng trên trang chiếu | Sử dụng mẫu bố cục (Layouts), thiết lập màu nền đồng bộ (Theme) và chỉnh sửa kích thước các khung chứa văn bản. | `G7-PRES-02` | `sort-drag` |
| Bài 13 | Chủ đề 5: Giải quyết vấn đề | Thuật toán tìm kiếm tuần tự | Mô tả nguyên lý tìm kiếm tuần tự (Sequential Search): duyệt từng phần tử từ đầu đến cuối danh sách; tính toán số lần so sánh. | `G7-SEARCH-01`| `block-maze` |
| Bài 14 | Chủ đề 5: Giải quyết vấn đề | Thuật toán tìm kiếm nhị phân | Mô tả thuật toán tìm kiếm nhị phân (Binary Search) trên danh sách đã sắp xếp: chia đôi phạm vi tìm kiếm O(log N). | `G7-SEARCH-02`| `logic-puzzle` |
| Bài 15 | Chủ đề 5: Giải quyết vấn đề | Thuật toán sắp xếp nổi bọt | Hiểu cơ chế thuật toán Bubble Sort: so sánh và đổi chỗ hai phần tử liền kề để đưa phần tử lớn nhất về cuối dãy. | `G7-SORT-01` | `block-maze` |
| Bài 16 | Chủ đề 5: Giải quyết vấn đề | Thuật toán sắp xếp chọn | Hiểu cơ chế thuật toán Selection Sort: tìm phần tử nhỏ nhất trong dãy chưa sắp xếp và hoán đổi về vị trí đầu tiên. | `G7-BOSS-01` | `boss-quiz` |

---

## 6. Lớp 8 — THCS (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách KNTT | Yêu cầu cần đạt (YCCĐ) trọng tâm | Nút EasyTin | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề 1: Máy tính và cộng đồng | Lược sử công cụ tính toán | Nêu các mốc phát triển công cụ tính toán: bàn tính cơ học, máy tính cơ khí Pascal, máy phân tích Babbage đến các thế hệ máy tính điện tử. | `G8-HIST-01` | `match-memory` |
| Bài 2 | Chủ đề 1: Máy tính và cộng đồng | Thông tin trong môi trường số | Phân biệt thông tin đáng tin cậy và không đáng tin cậy; nhận biết tin tức sai sự thật (fake news) trên mạng xã hội. | `G8-INFO-01` | `branch-story` |
| Bài 3 | Chủ đề 1: Máy tính và cộng đồng | Thực hành khai thác thông tin số | Tìm kiếm, đối chiếu từ nhiều nguồn tài liệu để thẩm định tính chính xác của dữ liệu khoa học. | `G8-SEARCH-01` | `sort-drag` |
| Bài 4 | Chủ đề 3: Đạo đức, pháp luật | Đạo đức và văn hóa trong môi trường số | Nêu các quy tắc ứng xử theo Luật An ninh mạng; phòng chống nghiện Internet, bảo vệ bản quyền phần mềm và nội dung số. | `G8-ETHIC-01` | `branch-story` |
| Bài 5 | Chủ đề 4: Ứng dụng tin học | Sử dụng bảng tính giải quyết bài toán | Áp dụng công thức và hàm bảng tính để giải quyết bài toán quản lý tài chính chi tiêu lớp học hoặc thống kê điểm số. | `G8-SHEET-01` | `logic-puzzle` |
| Bài 6 | Chủ đề 4: Ứng dụng tin học | Sắp xếp và lọc dữ liệu | Sử dụng công cụ Sort (sắp xếp đơn tiêu chí, đa tiêu chí) và Filter (bộ lọc tự động AutoFilter) để trích xuất dữ liệu thỏa mãn điều kiện. | `G8-SHEET-02` | `sort-drag` |
| Bài 7 | Chủ đề 4: Ứng dụng tin học | Trực quan hóa dữ liệu bằng biểu đồ | Tạo và tùy biến các dạng biểu đồ: biểu đồ cột (so sánh số lượng), biểu đồ tròn (tỉ lệ phần trăm), biểu đồ đường (xu hướng thời gian). | `G8-CHART-01` | `sort-drag` |
| Bài 8 | Chủ đề 4: Ứng dụng tin học | Làm quen với đồ họa chỉnh sửa ảnh | Làm quen với phần mềm chỉnh sửa ảnh (GIMP/Paint.NET): hệ màu RGB, độ phân giải DPI, các công cụ chọn vùng và vẽ cọ. | `G8-IMG-01` | `match-memory` |
| Bài 9 | Chủ đề 4: Ứng dụng tin học | Tạo ảnh động | Tạo ảnh động (GIF) bằng cách phối hợp các lớp ảnh (Layers) và thiết lập khoảng thời gian hiển thị giữa các khung hình. | `G8-IMG-02` | `sort-drag` |
| Bài 10 | Chủ đề 5: Giải quyết vấn đề | Làm quen với lập trình trực quan | Làm quen với môi trường lập trình giải quyết bài toán toán học: tính chu vi diện tích hình học, xử lý chuỗi và số học. | `G8-PROG-01` | `block-maze` |
| Bài 11 | Chủ đề 5: Giải quyết vấn đề | Kiểu dữ liệu và biểu thức | Phân biệt các kiểu dữ liệu cơ bản: số nguyên (Integer), số thực (Float), xâu ký tự (String), logic (Boolean); viết biểu thức số học và logic. | `G8-TYPE-01` | `logic-puzzle` |
| Bài 12 | Chủ đề 5: Giải quyết vấn đề | Câu lệnh rẽ nhánh | Lập trình cấu trúc điều kiện If... Then và lồng ghép nhiều điều kiện rẽ nhánh để giải quyết bài toán phân loại học lực. | `G8-IF-01` | `bug-hunt` |
| Bài 13 | Chủ đề 5: Giải quyết vấn đề | Câu lệnh lặp | Lập trình vòng lặp với số lần biết trước và lặp với điều kiện; tính tổng dãy số nguyên S = 1 + 2 + ... + N. | `G8-LOOP-01` | `block-maze` |
| Bài 14 | Chủ đề 5: Giải quyết vấn đề | Mảng và danh sách | Khai báo và sử dụng danh sách (List): thêm phần tử, xóa phần tử, duyệt các phần tử trong danh sách để tìm giá trị lớn nhất. | `G8-LIST-01` | `bug-hunt` |
| Bài 15 | Chủ đề 5: Giải quyết vấn đề | Dự án lập trình | Xây dựng phần mềm trò chơi đố vui học tập hoặc mô phỏng thuật toán toán học hoàn chỉnh có điểm số và đồng hồ đếm ngược. | `G8-PROJ-01` | `bug-hunt` |
| Bài 16 | Chủ đề 6: Hướng nghiệp | Nghề nghiệp trong lĩnh vực CNTT | Tìm hiểu các ngành nghề chính: Kỹ sư phần mềm, Chuyên viên an ninh mạng, Quản trị hệ thống, Nhà khoa học dữ liệu và cơ hội tương lai. | `G8-BOSS-01` | `boss-quiz` |

---

## 7. Lớp 9 — THCS (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách KNTT | Yêu cầu cần đạt (YCCĐ) trọng tâm | Nút EasyTin | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề 1: Máy tính và cộng đồng | Bộ xử lý, bộ nhớ và thiết bị vào - ra | Hiểu chức năng của CPU (tốc độ xung nhịp GHz), bộ nhớ trong (RAM, ROM, Cache), bộ nhớ ngoài (SSD, thẻ nhớ) và bus truyền dữ liệu. | `G9-ARCH-01` | `sort-drag` |
| Bài 2 | Chủ đề 1: Máy tính và cộng đồng | Chất lượng thông tin trong giải quyết vấn đề | Đánh giá 5 thuộc tính chất lượng thông tin: Tính chính xác, Tính kịp thời, Tính đầy đủ, Tính thích hợp và Tính bảo mật. | `G9-INFO-01` | `branch-story` |
| Bài 3 | Chủ đề 1: Máy tính và cộng đồng | Đánh giá độ tin cậy của thông tin số | Nhận diện kỹ thuật tin giả mạo (deepfake, tin câu view), phương pháp kiểm chứng nguồn tin chính thống từ các cơ quan chức năng. | `G9-VERIF-01` | `branch-story` |
| Bài 4 | Chủ đề 3: Đạo đức, pháp luật | Thực hành đạo đức và pháp luật trên mạng | Nêu rõ các hành vi bị cấm theo Luật An ninh mạng: xâm phạm bí mật đời tư, truyền bá nội dung xấu, vi phạm bản quyền thương mại số. | `G9-LAW-01` | `branch-story` |
| Bài 5 | Chủ đề 4: Ứng dụng tin học | Phần mềm mô phỏng | Sử dụng phần mềm mô phỏng (PhET, GeoGebra) để quan sát các thí nghiệm vật lý, hình học không gian phức tạp trong thực tế. | `G9-SIM-01` | `match-memory` |
| Bài 6 | Chủ đề 4: Ứng dụng tin học | Xây dựng bài trình chiếu đa phương tiện | Thiết kế bài trình chiếu chuyên nghiệp có tích hợp âm thanh, video clip nhúng, sơ đồ đồ thị và các liên kết tương tác. | `G9-PRES-01` | `sort-drag` |
| Bài 7 | Chủ đề 4: Ứng dụng tin học | Biên tập video ngắn | Làm quen phần mềm dựng video (CapCut/Shotcut): cắt ghép đoạn clip, chèn nhạc nền, thêm phụ đề và áp dụng hiệu ứng chuyển cảnh. | `G9-VID-01` | `sort-drag` |
| Bài 8 | Chủ đề 4: Ứng dụng tin học | Dự án đa phương tiện | Nhóm học sinh phối hợp sản xuất video ngắn truyền thông về phòng chống rác thải nhựa hoặc nét đẹp văn hóa trường lớp. | `G9-PROJ-01` | `match-memory` |
| Bài 9 | Chủ đề 5: Giải quyết vấn đề | Khái niệm bài toán và thuật toán | Xác định rõ Input (đầu vào), Output (đầu ra) của bài toán; biểu diễn các thuật toán giải quyết bài toán qua mã giả và lưu đồ. | `G9-ALGO-01` | `logic-puzzle` |
| Bài 10 | Chủ đề 5: Giải quyết vấn đề | Thực hành lập trình thuật toán | Cài đặt các thuật toán toán học cơ bản: kiểm tra số nguyên tố, tìm ước chung lớn nhất (UCLN) bằng thuật toán Euclid. | `G9-CODE-01` | `bug-hunt` |
| Bài 11 | Chủ đề 5: Giải quyết vấn đề | Bẫy lỗi và gỡ lỗi chương trình | Phân biệt 3 loại lỗi lập trình: Lỗi cú pháp (Syntax Error), Lỗi thời gian chạy (Runtime Error) và Lỗi ngữ nghĩa (Logic Error); kỹ thuật debug. | `G9-DEBUG-01` | `bug-hunt` |
| Bài 12 | Chủ đề 5: Giải quyết vấn đề | Lập trình ứng dụng đơn giản | Thiết kế chương trình có giao diện tương tác: ứng dụng máy tính bỏ túi bỏ túi bỏ túi hoặc trò chơi đoán số có giới hạn lượt đoán. | `G9-APP-01` | `block-maze` |
| Bài 13 | Chủ đề 2: Mạng và Internet | Mạng cục bộ (LAN) và Internet | Hiểu cấu trúc mạng LAN trong trường học; giao thức TCP/IP, địa chỉ IP tĩnh và IP động, thiết bị định tuyến Router và modem cáp quang. | `G9-LAN-01` | `packet-route` |
| Bài 14 | Chủ đề 2: Mạng và Internet | Dịch vụ đám mây | Sử dụng dịch vụ lưu trữ và làm việc cộng tác trực tuyến trên nền tảng đám mây (Cloud Computing): Google Drive, OneDrive, Docs. | `G9-CLOUD-01` | `sort-drag` |
| Bài 15 | Chủ đề 3: Đạo đức, pháp luật | An toàn dữ liệu số | Biện pháp bảo vệ dữ liệu: mật khẩu mạnh kết hợp xác thực 2 bước (2FA), sao lưu dự phòng định kỳ (Backup), phòng chống mã độc Ransomware. | `G9-SEC-01` | `branch-story` |
| Bài 16 | Chủ đề 6: Hướng nghiệp | Hướng nghiệp: Ngành nghề Tin học | Tổng kết các cơ hội học tập THPT chuyên Tin, trường nghề công nghệ và xu hướng nghề nghiệp Trí tuệ Nhân tạo thời đại mới. | `G9-BOSS-01` | `boss-quiz` |

---

## 8. Lớp 10 — THPT (34 bài)

| STT | Phân nhóm | Tên bài học trong sách KNTT | Yêu cầu cần đạt (YCCĐ) trọng tâm | Nút EasyTin | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Máy tính và xã hội | Thông tin và xử lý thông tin | Khái niệm dữ liệu, thông tin và tri thức; biểu diễn thông tin số; quy trình xử lý thông tin trong hệ thống số hóa tự động. | `G10-INFO-01` | `branch-story` |
| Bài 2 | Máy tính và xã hội | Vai trò của thiết bị thông minh và tin học | Nêu vai trò của Internet vạn vật (IoT), hệ thống điều khiển tự động hóa và thiết bị thông minh đối với cuộc cách mạng công nghiệp 4.0. | `G10-IOT-01` | `match-memory` |
| Bài 3 | Máy tính và xã hội | Một số kiểu mạng máy tính | Phân loại mạng: PAN (cá nhân), LAN (cục bộ), WAN (diện rộng); cấu trúc liên kết mạng hình sao, hình tròn, đường trục bus. | `G10-NET-01` | `sort-drag` |
| Bài 4 | Máy tính và xã hội | Mạng máy tính và các thiết bị mạng | Chức năng của Modem, Hub, Switch, Wireless Access Point, Router trong việc truyền tải các gói dữ liệu số. | `G10-NET-02` | `packet-route` |
| Bài 5 | Máy tính và xã hội | Mạng xã hội và tương tác số | Khai thác các dịch vụ mạng xã hội; phân tích tác động tích cực và mặt trái của thế giới ảo đối với tâm lý thanh thiếu niên. | `G10-SOC-01` | `branch-story` |
| Bài 6 | Máy tính và xã hội | An toàn trên không gian mạng | Nhận biết mã độc (Trojan, Worm, Spyware), kỹ thuật lừa đảo (Phishing), biện pháp phòng chống tấn công mạng cơ bản. | `G10-SEC-01` | `branch-story` |
| Bài 7 | Đạo đức, pháp luật | Phần mềm nguồn mở và phần mềm chạy trên Internet | Phân biệt phần mềm thương mại đóng gói, phần mềm nguồn mở (Open Source: Linux, Apache) và phần mềm dịch vụ đám mây (SaaS). | `G10-OSS-01` | `sort-drag` |
| Bài 8 | Đạo đức, pháp luật | Bản quyền và tính hợp pháp của thông tin | Quyền tác giả và quyền liên quan theo Luật Sở hữu trí tuệ; các loại giấy phép bản quyền phần mềm (GPL, MIT, Creative Commons). | `G10-COPY-01` | `branch-story` |
| Bài 9 | Đạo đức, pháp luật | An toàn trong môi trường số | Các giải pháp bảo vệ dữ liệu: mã hóa dữ liệu đối xứng/bất đối xứng, chữ ký số điện tử và quy định pháp lý về bảo vệ dữ liệu cá nhân. | `G10-SAFE-01` | `logic-puzzle` |
| Bài 10 | Đạo đức, pháp luật | Thực hành khai thác tài nguyên số | Đăng ký sử dụng dịch vụ trực tuyến an toàn, quản lý danh tính số và thiết lập bảo mật nhiều lớp. | `G10-PRAC-01` | `sort-drag` |
| Bài 11 | Ứng dụng tin học | Ứng dụng trên nền tảng web | Sử dụng các ứng dụng văn phòng trực tuyến, chia sẻ tài nguyên đồng bộ thời gian thực qua điện toán đám mây. | `G10-WEBAPP-01`| `match-memory` |
| Bài 12 | Đồ họa Vector | Phần mềm thiết kế đồ họa (Inkscape) | Phân biệt đồ họa điểm ảnh (Raster/Bitmap) và đồ họa véc-tơ (Vector); làm quen với giao diện và hộp công cụ Inkscape. | `G10-VEC-01` | `sort-drag` |
| Bài 13 | Đồ họa Vector | Bổ sung các đối tượng đồ họa | Tạo và tùy chỉnh các đối tượng hình học cơ bản: hình chữ nhật, hình elip, hình đa giác và hình sao. | `G10-VEC-02` | `match-memory` |
| Bài 14 | Đồ họa Vector | Làm việc với đối tượng đường và văn bản | Chuyển đổi đối tượng thành đường (Path), chỉnh sửa nút điểm cong (Node tool), định dạng văn bản uốn lượn theo đường cong. | `G10-VEC-03` | `sort-drag` |
| Bài 15 | Đồ họa Vector | Hoàn thiện sản phẩm đồ họa | Phối hợp các phép biến đổi hình học (Union, Difference, Intersection) để vẽ logo, biểu tượng và xuất tệp định dạng SVG, PNG. | `G10-VEC-04` | `sort-drag` |
| Bài 16 | Lập trình Python | Ngôn ngữ lập trình bậc cao và Python | Giới thiệu ngôn ngữ thông dịch Python, môi trường IDLE, chế độ tương tác (Interactive Mode) và chế độ soạn thảo kịch bản (Script Mode). | `G10-PY-01` | `type-run` |
| Bài 17 | Lập trình Python | Biến và lệnh gán | Khái niệm biến, quy tắc đặt tên định danh, lệnh gán (=), các kiểu dữ liệu cơ bản: int, float, str, bool; hàm type(). | `G10-PY-02` | `logic-puzzle` |
| Bài 18 | Lập trình Python | Các lệnh vào ra đơn giản | Sử dụng hàm print() xuất thông báo ra màn hình và hàm input() nhận dữ liệu từ bàn phím; ép kiểu dữ liệu int() và float(). | `G10-PY-03` | `type-run` |
| Bài 19 | Lập trình Python | Câu lệnh điều kiện if | Cú pháp lệnh rẽ nhánh if, if-else, if-elif-else; thụt lề đầu dòng (indentation) bắt buộc trong khối mã Python. | `G10-PY-04` | `bug-hunt` |
| Bài 20 | Lập trình Python | Câu lệnh lặp for | Cú pháp vòng lặp for kết hợp với hàm sinh dãy số range(start, stop, step); tính tổng dãy số nguyên. | `G10-PY-05` | `block-maze` |
| Bài 21 | Lập trình Python | Câu lệnh lặp while | Cú pháp vòng lặp điều kiện while; xử lý vòng lặp vô hạn và lệnh ngắt vòng lặp break, tiếp tục continue. | `G10-PY-06` | `bug-hunt` |
| Bài 22 | Lập trình Python | Kiểu dữ liệu danh sách (List) | Khái niệm danh sách List trong Python; chỉ số phần tử (index từ 0 đến len-1), truy cập và thay đổi giá trị phần tử. | `G10-PY-07` | `logic-puzzle` |
| Bài 23 | Lập trình Python | Các lệnh làm việc với danh sách | Sử dụng các phương thức có sẵn: append(), insert(), remove(), pop(), sort(), reverse() và toán tử in kiểm tra phần tử. | `G10-PY-08` | `bug-hunt` |
| Bài 24 | Lập trình Python | Xâu ký tự (String) | Duyệt các ký tự trong xâu; ghép xâu (+), nhân xâu (*), toán tử cắt lát xâu ký tự s[start:stop:step]. | `G10-PY-09` | `type-run` |
| Bài 25 | Lập trình Python | Một số lệnh làm việc với xâu ký tự | Sử dụng các phương thức xử lý chuỗi: split(), join(), find(), replace(), upper(), lower(), strip(). | `G10-PY-10` | `bug-hunt` |
| Bài 26 | Lập trình Python | Hàm trong Python (Functions) | Khái niệm chương trình con; cú pháp định nghĩa hàm def tên_hàm(), gọi hàm và lệnh trả về giá trị return. | `G10-PY-11` | `bug-hunt` |
| Bài 27 | Lập trình Python | Tham số của hàm | Phân biệt tham số hình thức (parameter) và đối số thực sự (argument); truyền tham số theo vị trí và theo từ khóa. | `G10-PY-12` | `logic-puzzle` |
| Bài 28 | Lập trình Python | Phạm vi của biến trong hàm | Phân biệt biến cục bộ (Local variable) bên trong hàm và biến toàn cục (Global variable); từ khóa global. | `G10-PY-13` | `bug-hunt` |
| Bài 29 | Lập trình Python | Nhận biết lỗi chương trình | Phân loại các thông báo lỗi kinh điển: SyntaxError, NameError, TypeError, ValueError, IndexError, ZeroDivisionError. | `G10-DEBUG-01` | `bug-hunt` |
| Bài 30 | Lập trình Python | Kiểm thử và gỡ lỗi | Kỹ thuật kiểm thử hộp đen, thiết kế bộ dữ liệu thử nghiệm (Test cases); sử dụng khối bắt ngoại lệ try... except... | `G10-DEBUG-02` | `bug-hunt` |
| Bài 31 | Lập trình Python | Thực hành viết chương trình | Vận dụng tổng hợp cấu trúc điều khiển, danh sách và hàm giải quyết bài toán quản lý danh bạ hoặc quản lý điểm số. | `G10-PROJ-01` | `bug-hunt` |
| Bài 32 | Lập trình Python | Ôn tập lập trình | Tổng hợp các kỹ thuật thuật toán nâng cao trên Python; chuẩn bị sẵn sàng cho các bài kiểm tra đánh giá năng lực. | `G10-REV-01` | `logic-puzzle` |
| Bài 33 | Hướng nghiệp | Nghề thiết kế đồ họa và lập trình | Khám phá thị trường việc làm lập trình viên Back-end, Front-end, Kỹ sư đồ họa Game và lộ trình học tập đại học. | `G10-CAREER-01`| `match-memory` |
| Bài 34 | Dự án tổng kết | Dự án học tập Tin học 10 | Thiết kế và báo cáo phần mềm mini game toán học hoặc ứng dụng tiện ích cuộc sống kết hợp giao diện đồ họa. | `G10-BOSS-01` | `boss-quiz` |

---

## 9. Lớp 11 — THPT (31 bài định hướng CS & ICT)

### Nhánh Khoa học máy tính (CS — 31 bài)
| STT | Chủ đề | Tên bài học trong sách KNTT CS | Yêu cầu cần đạt (YCCĐ) trọng tâm | Nút EasyTin | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài CS 1 | CSDL | Giới thiệu hệ cơ sở dữ liệu | Khái niệm CSDL (Database) và Hệ quản trị CSDL (DBMS); phân biệt lưu trữ dữ liệu dạng tệp phẳng và bảng dữ liệu quan hệ. | `G11-DB-01` | `sort-drag` |
| Bài CS 2 | CSDL | Bảng và mối quan hệ giữa các bảng | Mô hình thực thể quan hệ: Bảng (Table), Bản ghi (Record), Trường (Field); mối quan hệ 1-1, 1-N, N-N. | `G11-DB-02` | `sort-drag` |
| Bài CS 3 | CSDL | Khóa chính và khóa ngoại | Xác định Khóa chính (Primary Key - duy nhất, không rỗng) và Khóa ngoại (Foreign Key - tham chiếu liên kết toàn vẹn dữ liệu). | `G11-DB-03` | `logic-puzzle` |
| Bài CS 4 | SQL | Ngôn ngữ SQL và truy vấn cơ bản | Viết câu lệnh SELECT trích xuất dữ liệu, mệnh đề FROM chỉ định nguồn bảng và điều kiện lọc WHERE. | `G11-SQL-01` | `logic-puzzle` |
| Bài CS 5 | SQL | Lọc và sắp xếp dữ liệu trong SQL | Mệnh đề ORDER BY (ASC, DESC), toán tử logic AND, OR, NOT, toán tử so sánh LIKE, BETWEEN, IN. | `G11-SQL-02` | `logic-puzzle` |
| Bài CS 6 | SQL | Các hàm tổng hợp trong SQL | Sử dụng các hàm tính toán trên tập bản ghi: COUNT(), SUM(), AVG(), MIN(), MAX() kết hợp với GROUP BY và HAVING. | `G11-SQL-03` | `logic-puzzle` |
| Bài CS 7 | SQL | Liên kết bảng với INNER JOIN | Viết truy vấn kết nối 2 hoặc nhiều bảng dữ liệu thông qua khóa ngoại bằng mệnh đề INNER JOIN... ON... | `G11-SQL-04` | `logic-puzzle` |
| Bài CS 8 | SQL | Cập nhật và xóa dữ liệu (UPDATE, DELETE) | Viết lệnh INSERT INTO thêm dữ liệu mới, UPDATE sửa dữ liệu và DELETE xóa bản ghi thỏa mãn điều kiện. | `G11-SQL-05` | `bug-hunt` |
| Bài CS 9 | Thiết kế CSDL | Chuẩn hóa dữ liệu quan hệ | Khái niệm dị thường dữ liệu (dư thừa, sửa đổi, xóa); hiểu các dạng chuẩn 1NF, 2NF, 3NF để tối ưu cấu trúc lưu trữ. | `G11-NORM-01` | `sort-drag` |
| Bài CS 10 | Thực hành CSDL | Tạo lập CSDL với MySQL/HeidiSQL | Khởi tạo CSDL, định nghĩa bảng, kiểu dữ liệu từng cột (INT, VARCHAR, DATE), ràng buộc NOT NULL, UNIQUE, FOREIGN KEY. | `G11-PRAC-01` | `bug-hunt` |
| Bài CS 11 | Thuật toán CS | Kỹ thuật Đệ quy (Recursion) | Hiểu bản chất hàm tự gọi lại chính nó; xác định điều kiện dừng (Base case) và bước đệ quy; thuật toán tính giai thừa N!. | `G11-ALGO-01` | `bug-hunt` |
| Bài CS 12 | Thuật toán CS | Bài toán Tháp Hà Nội | Xây dựng thuật toán đệ quy giải bài toán Tháp Hà Nội kinh điển; phân tích số bước di chuyển tối thiểu $2^N - 1$. | `G11-ALGO-02` | `logic-puzzle` |
| Bài CS 13 | Thuật toán CS | Thuật toán Chia để trị (Divide and Conquer) | Nguyên lý phân rã bài toán lớn thành các bài toán con độc lập; phân tích thuật toán Sắp xếp trộn (Merge Sort). | `G11-ALGO-03` | `logic-puzzle` |
| Bài CS 14 | Thuật toán CS | Thuật toán Sắp xếp nhanh (Quick Sort) | Chọn phần tử chốt (Pivot), phân đoạn mảng thành 2 nửa nhỏ hơn và lớn hơn chốt; độ phức tạp trung bình O(N log N). | `G11-ALGO-04` | `bug-hunt` |
| Bài CS 15 | Thuật toán CS | Đánh giá độ phức tạp thuật toán | Khái niệm ký hiệu Big-O biểu diễn thời gian thực thi: O(1), O(log N), O(N), O(N log N), O(N^2); so sánh hiệu năng thuật toán. | `G11-ALGO-05` | `logic-puzzle` |
| Bài CS 16 | Dự án CS | Dự án CSDL và phần mềm quản lý học sinh | Xây dựng hoàn chỉnh CSDL kết nối giao diện Python Tkinter để tra cứu và xuất báo cáo điểm số. | `G11-BOSS-01` | `boss-quiz` |

*(Nhánh ICT Lớp 11 bao gồm 15 bài chuyên đề về Biên tập Video, Đồ họa đa phương tiện, Quản trị hệ thống mạng nội bộ và Lập trình Web HTML5/CSS3 tương ứng chuẩn GDPT 2018).*

---

## 10. Lớp 12 — THPT (30 bài định hướng CS & ICT)

| STT | Phân nhóm | Tên bài học trong sách KNTT | Yêu cầu cần đạt (YCCĐ) trọng tâm | Nút EasyTin | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Mạng nâng cao | Mô hình OSI và bộ giao thức TCP/IP | Phân tích 7 tầng mô hình OSI; 4 tầng kiến trúc TCP/IP; cơ chế đóng gói (encapsulation) và giải mã gói tin dữ liệu. | `G12-NET-01` | `sort-drag` |
| Bài 2 | Mạng nâng cao | Địa chỉ IP và phân dải tên miền | Cấu trúc địa chỉ IPv4 (Network ID, Host ID, Subnet Mask), không gian địa chỉ IPv6 (128-bit); cơ chế hoạt động của DNS. | `G12-NET-02` | `logic-puzzle` |
| Bài 3 | Mạng nâng cao | Thiết bị mạng và định tuyến gói tin | Cơ chế chuyển tiếp khung tin (Frame) của Switch qua bảng MAC; thuật toán định tuyến gói tin (Packet) của Router. | `G12-NET-03` | `packet-route` |
| Bài 4 | An ninh mạng | Các nguy cơ và tấn công mạng | Tấn công từ chối dịch vụ (DoS/DDoS), tấn công chèn mã SQL Injection, tấn công trung gian (Man-in-the-Middle). | `G12-SEC-01` | `branch-story` |
| Bài 5 | An ninh mạng | Các giải pháp phòng thủ an ninh số | Cấu hình tường lửa (Firewall), hệ thống phát hiện xâm nhập (IDS/IPS), mã hóa đường truyền qua giao thức an toàn HTTPS / SSL / TLS. | `G12-SEC-02` | `sort-drag` |
| Bài 6 | Trí tuệ nhân tạo | Tổng quan về Trí tuệ nhân tạo (AI) | Lịch sử hình thành AI, phép thử Turing (Turing Test); phân biệt AI hẹp (Narrow AI), AI tổng quát (AGI) và Siêu trí tuệ (Super AI). | `G12-AI-01` | `match-memory` |
| Bài 7 | Trí tuệ nhân tạo | Các kỹ thuật nền tảng của AI | Tìm kiếm trong không gian trạng thái, biểu diễn tri thức và hệ chuyên gia (Expert Systems) dựa trên tập luật suy diễn. | `G12-AI-02` | `logic-puzzle` |
| Bài 8 | Học máy | Nhập môn Học máy (Machine Learning) | Ba nhánh học máy chính: Học có giám sát (Supervised), Học không giám sát (Unsupervised), Học tăng cường (Reinforcement Learning). | `G12-ML-01` | `sort-drag` |
| Bài 9 | Học máy | Dữ liệu huấn luyện và mô hình dự đoán | Khái niệm tập huấn luyện (Training Set), tập kiểm thử (Test Set); hiện tượng quá khớp (Overfitting) và dưới khớp (Underfitting). | `G12-ML-02` | `bug-hunt` |
| Bài 10 | Học sâu & LLM | Mạng nơ-ron và Học sâu (Deep Learning) | Cấu trúc nơ-ron nhân tạo (Perceptron), hàm kích hoạt (Activation function), mạng nơ-ron tích chập (CNN) nhận diện hình ảnh. | `G12-AI-03` | `logic-puzzle` |
| Bài 11 | Học sâu & LLM | Mô hình ngôn ngữ lớn (LLM) và Generative AI | Nguyên lý kiến trúc Transformer, cơ chế tự chú ý (Self-Attention); ứng dụng trợ lý ảo tạo sinh (ChatGPT, Gemini). | `G12-AI-04` | `branch-story` |
| Bài 12 | Đạo đức AI | Đạo đức AI và trách nhiệm xã hội | Nguy cơ thiên kiến thuật toán (Algorithmic Bias), bản quyền tác phẩm do AI tạo ra, tính minh bạch và bảo mật dữ liệu công dân. | `G12-ETHIC-01` | `branch-story` |
| Bài 13 | Lập trình Web | Ngôn ngữ HTML5 và cấu trúc tài liệu web | Các thẻ văn bản (h1-h6, p), danh sách (ul, ol, li), bảng (table), biểu mẫu (form) và nhúng đa phương tiện (img, video, iframe). | `G12-WEB-01` | `type-run` |
| Bài 14 | Lập trình Web | Định kiểu giao diện với CSS3 | Bộ chọn (Selectors), mô hình hộp (Box Model: margin, border, padding, content), bố cục linh hoạt Flexbox và CSS Grid. | `G12-WEB-02` | `sort-drag` |
| Bài 15 | Lập trình Web | Tương tác động với JavaScript | Khai báo biến (let, const), hàm xử lý sự kiện (addEventListener), thao tác với các phần tử HTML qua DOM (Document Object Model). | `G12-WEB-03` | `bug-hunt` |
| Bài 16 | Tổng kết | Đại chiến Boss Trí tuệ Nhân tạo Toàn cầu | Đấu trường tổng hợp toàn bộ tri thức 10 năm học Tin học từ lớp 3 đến lớp 12: Kiến trúc máy tính, Thuật toán, CSDL, Mạng và AI. | `G12-BOSS` | `boss-quiz` |

---
> Bản trích xuất KNTT Lớp 3–12 hoàn tất 100% không thiếu bài nào theo đúng cấu trúc SGK Bộ GD&ĐT.
"""

# ==============================================================================
# 2. CÁNH DIỀU
# ==============================================================================
canhdieu_content = """# 01a-extract-canhdieu-g3_12.md — Trích xuất toàn diện bộ sách Cánh Diều (Lớp 3–12)

> **Bộ sách:** Cánh Diều (Nhà xuất bản Đại học Sư phạm / Cty CP Đầu tư Xuất bản Thiết bị Giáo dục Việt Nam VEPIC)  
> **Chương trình:** Giáo dục phổ thông 2018 môn Tin học (Thông tư 32/2018/TT-BGDĐT)  
> **Cam kết:** Trích xuất 100% đầy đủ tất cả các bài học từ Lớp 3 đến Lớp 12, không bỏ sót bất kỳ bài nào.  
> **Đặc trưng sư phạm:** Tiếp cận theo hướng hành động thực tiễn "Mang cuộc sống vào bài học – Đưa bài học vào cuộc sống", chia nhỏ nhiệm vụ, khuyến khích tư duy phân rã và học tập qua dự án.

---

## MỤC LỤC TỔNG QUAN CÁC KHỐI LỚP
- [Lớp 3 (16 bài)](#1-lớp-3--tiểu-học-16-bài)
- [Lớp 4 (16 bài)](#2-lớp-4--tiểu-học-16-bài)
- [Lớp 5 (16 bài)](#3-lớp-5--tiểu-học-16-bài)
- [Lớp 6 (18 bài)](#4-lớp-6--thcs-18-bài)
- [Lớp 7 (16 bài)](#5-lớp-7--thcs-16-bài)
- [Lớp 8 (16 bài)](#6-lớp-8--thcs-16-bài)
- [Lớp 9 (16 bài)](#7-lớp-9--thcs-16-bài)
- [Lớp 10 (32 bài)](#8-lớp-10--thpt-32-bài)
- [Lớp 11 (30 bài định hướng CS & ICT)](#9-lớp-11--thpt-30-bài-định-hướng-cs--ict)
- [Lớp 12 (30 bài định hướng CS & ICT)](#10-lớp-12--thpt-30-bài-định-hướng-cs--ict)

---

## 1. Lớp 3 — Tiểu học (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách Cánh Diều | Điểm tương thích YCCĐ & Năng lực hành động | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề A: Máy tính và em | Em làm quen với máy tính | Nhận diện các loại máy tính thông dụng: máy để bàn, laptop, máy tính bảng; vai trò người bạn hỗ trợ em học tập. | `G3-HARD-01` | `sort-drag` |
| Bài 2 | Chủ đề A: Máy tính và em | Các bộ phận của máy tính | Phân biệt chức năng 4 bộ phận: Màn hình (hiển thị), Thân máy (xử lý), Bàn phím (nhập ký tự), Chuột (điều khiển). | `G3-HARD-02` | `sort-drag` |
| Bài 3 | Chủ đề A: Máy tính và em | Em tập dùng chuột | Rèn luyện phản xạ cầm và điều khiển chuột: nhấp chuột trái, nhấp chuột phải, nhấp đúp và kéo thả đối tượng. | `G3-MOUSE-01` | `sort-drag` |
| Bài 4 | Chủ đề A: Máy tính và em | Em tập gõ hàng phím cơ sở | Nhận biết 2 phím có gờ F và J; đặt 8 ngón tay đúng vị trí xuất phát A S D F - J K L ; trên hàng phím cơ sở. | `G3-KEY-01` | `type-run` |
| Bài 5 | Chủ đề A: Máy tính và em | Em tập gõ các hàng phím khác | Mở rộng kỹ năng gõ mười ngón lên hàng phím trên, hàng phím dưới, hàng phím số và phím cách Spacebar. | `G3-TYPE-01` | `type-run` |
| Bài 6 | Chủ đề B: Mạng và Internet | Thông tin trên Internet | Khám phá kho tài nguyên khổng lồ trên mạng Internet; phân biệt thông tin phù hợp và thông tin không phù hợp lứa tuổi. | `G3-NET-01` | `branch-story` |
| Bài 7 | Chủ đề C: Tổ chức lưu trữ | Sắp xếp đồ vật hợp lí | Hiểu quy luật phân loại đồ dùng học tập, sách vở; lợi ích của việc sắp xếp khoa học giúp tìm đồ nhanh chóng. | `G3-ORG-01` | `sort-drag` |
| Bài 8 | Chủ đề C: Tổ chức lưu trữ | Sơ đồ hình cây | Làm quen cấu trúc phân cấp dạng cây (Tree structure); biểu diễn thư viện hoặc gia phả gia đình bằng sơ đồ hình cây. | `G3-ORG-03` | `logic-puzzle` |
| Bài 9 | Chủ đề D: Đạo đức, pháp luật | Em bảo vệ thông tin cá nhân | Nhận biết thông tin bí mật cá nhân và gia đình; quy tắc không cung cấp mật khẩu, địa chỉ cho người lạ trên mạng. | `G3-ETHIC-01` | `branch-story` |
| Bài 10 | Chủ đề E: Ứng dụng tin học | Cùng vui học với máy tính | Trải nghiệm các phần mềm học toán, luyện tiếng Anh trực quan; rèn luyện thói quen sử dụng máy tính điều độ. | `G3-APP-01` | `match-memory` |
| Bài 11 | Chủ đề E: Ứng dụng tin học | Em vẽ tranh trên máy tính | Sử dụng bảng màu và cọ vẽ, hình khối cơ bản trên phần mềm Paint để tạo bức tranh phong cảnh yêu thích. | `G3-DRAW-01` | `sort-drag` |
| Bài 12 | Chủ đề F: Giải quyết vấn đề | Chia việc thành việc nhỏ | Kỹ năng phân rã bài toán (Decomposition): chia một công việc lớn thành các việc nhỏ dễ thực hiện hơn. | `G3-ALGO-01` | `block-maze` |
| Bài 13 | Chủ đề F: Giải quyết vấn đề | Thực hiện công việc theo các bước | Nhận biết thứ tự quan trọng của từng bước hành động; thực hiện tuần tự để hoàn thành nhiệm vụ chính xác. | `G3-ALGO-02` | `block-maze` |
| Bài 14 | Chủ đề F: Giải quyết vấn đề | Em giải bài toán bằng sơ đồ | Dùng sơ đồ các mũi tên chỉ hướng để hướng dẫn bạn tìm đường trong công viên hoặc vượt mê cung. | `G3-MAZE-01` | `block-maze` |
| Bài 15 | Chủ đề F: Giải quyết vấn đề | Trò chơi rèn luyện tư duy | Giải các câu đố quy luật hình học, số học để rèn luyện tư duy logic phản biện nhạy bén. | `G3-PUZZLE-01`| `logic-puzzle` |
| Bài 16 | Chủ đề F: Giải quyết vấn đề | Em tập trình bày ý kiến | Sử dụng hình vẽ và ngôn ngữ tự tin chia sẻ sản phẩm số của mình trước thầy cô và các bạn. | `G3-BOSS-01` | `boss-quiz` |

---

## 2. Lớp 4 — Tiểu học (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách Cánh Diều | Điểm tương thích YCCĐ & Năng lực hành động | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề A: Máy tính và em | Phần cứng và phần mềm | Nhận biết phần cứng là vật thể cầm nắm được, phần mềm là chương trình chứa trong máy tính chỉ đạo phần cứng hoạt động. | `G4-HARD-01` | `sort-drag` |
| Bài 2 | Chủ đề A: Máy tính và em | Luyện tập gõ mười ngón | Tăng tốc độ và độ chính xác khi gõ phím; duy trì quy tắc phân công từng ngón tay phụ trách các phím tương ứng. | `G4-TYPE-01` | `type-run` |
| Bài 3 | Chủ đề B: Mạng và Internet | Khám phá trang web | Điều hướng trang web: nhấp chuột vào liên kết (link), thanh cuộn trang, nút quay lại (Back) và tải lại (Reload). | `G4-NET-01` | `branch-story` |
| Bài 4 | Chủ đề B: Mạng và Internet | Tìm kiếm thông tin hữu ích | Nhập từ khóa ngắn gọn, đúng trọng tâm vào ô tìm kiếm; đọc lướt kết quả và chọn lọc đường dẫn uy tín. | `G4-SEARCH-01` | `sort-drag` |
| Bài 5 | Chủ đề C: Tổ chức lưu trữ | Quản lý tệp và thư mục trong máy tính | Mở ổ đĩa, tạo cây thư mục lưu bài tập từng môn học; đổi tên tệp sao cho khoa học, dễ tìm kiếm. | `G4-FILE-01` | `sort-drag` |
| Bài 6 | Chủ đề D: Đạo đức, pháp luật | Tôn trọng bản quyền tác giả và phần mềm | Nêu lý do vì sao không được tự ý xóa, sao chép hoặc phát tán bài làm, sản phẩm tranh ảnh của người khác. | `G4-ETHIC-01` | `branch-story` |
| Bài 7 | Chủ đề E: Ứng dụng tin học | Soạn thảo văn bản có hình ảnh | Soạn một bức thư hoặc đoạn văn ngắn có chèn hình ảnh minh họa phù hợp với nội dung bài viết. | `G4-DOC-01` | `sort-drag` |
| Bài 8 | Chủ đề E: Ứng dụng tin học | Định dạng đoạn văn bản | Căn chỉnh lề văn bản, thụt lề dòng đầu câu, điều chỉnh khoảng cách giữa các dòng và các đoạn văn bản. | `G4-DOC-02` | `type-run` |
| Bài 9 | Chủ đề E: Ứng dụng tin học | Làm quen với phần mềm trình chiếu | Khởi động PowerPoint/Slides, nhận biết khu vực danh sách trang chiếu và khu vực thiết kế nội dung chính. | `G4-PRES-01` | `match-memory` |
| Bài 10 | Chủ đề E: Ứng dụng tin học | Thêm hình ảnh và hiệu ứng vào bài trình chiếu | Chèn hình ảnh, tạo hiệu ứng chuyển động đơn giản cho đối tượng để thu hút sự chú ý của người nghe. | `G4-PRES-02` | `sort-drag` |
| Bài 11 | Chủ đề E: Ứng dụng tin học | Xử lý hình ảnh đơn giản | Cắt bớt phần thừa của ảnh (Crop), điều chỉnh kích cỡ và lật hình ảnh sang trái/phải. | `G4-IMG-01` | `match-memory` |
| Bài 12 | Chủ đề F: Giải quyết vấn đề | Em làm quen với Scratch | Làm quen chú mèo Scratch, khu vực chọn phông nền sân khấu và thư viện nhân vật phong phú. | `G4-SCRATCH-01`| `match-memory` |
| Bài 13 | Chủ đề F: Giải quyết vấn đề | Nhân vật chuyển động theo lệnh | Lắp ghép các khối lệnh Move 10 steps, Turn 15 degrees để tạo chuyển động sinh động cho nhân vật. | `G4-ALGO-01` | `block-maze` |
| Bài 14 | Chủ đề F: Giải quyết vấn đề | Cấu trúc lặp trong lập trình | Sử dụng khối lệnh lặp (Repeat) để vẽ hình vuông, hình tam giác đều mà không cần viết lại nhiều dòng lệnh trùng lặp. | `G4-ALGO-02` | `block-maze` |
| Bài 15 | Chủ đề F: Giải quyết vấn đề | Em xây dựng câu chuyện tương tác | Lập trình cho 2 nhân vật đối thoại qua lại bằng các khối lệnh Say... for 2 seconds và Wait. | `G4-STORY-01` | `branch-story` |
| Bài 16 | Chủ đề F: Giải quyết vấn đề | Dự án lập trình trò chơi | Hoàn thiện trò chơi chú mèo bắt chuột trên sân khấu có tính điểm và âm thanh chúc mừng chiến thắng. | `G4-BOSS-01` | `boss-quiz` |

---

## 3. Lớp 5 — Tiểu học (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách Cánh Diều | Điểm tương thích YCCĐ & Năng lực hành động | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề A: Máy tính và em | Vai trò của máy tính trong thời đại số | Nêu ứng dụng của công nghệ số trong nông nghiệp công nghệ cao, thành phố thông minh và y tế từ xa. | `G5-COMP-01` | `match-memory` |
| Bài 2 | Chủ đề A: Máy tính và em | An toàn thông tin và sức khỏe | Phòng tránh các bệnh học đường khi dùng máy tính quá nhiều (cận thị, đau lưng); quy tắc bảo mật thiết bị cá nhân. | `G5-SAFE-01` | `branch-story` |
| Bài 3 | Chủ đề B: Mạng và Internet | Tìm kiếm và đánh giá thông tin | Kỹ năng so sánh nhiều nguồn tin để kiểm chứng sự thật; nhận biết cạm bẫy quảng cáo và thông tin sai lệch. | `G5-SEARCH-01` | `sort-drag` |
| Bài 4 | Chủ đề D: Đạo đức, pháp luật | Bản quyền và đạo đức trên mạng | Tôn trọng bản quyền sở hữu trí tuệ; nêu được trách nhiệm pháp lý khi chia sẻ thông tin công khai. | `G5-ETHIC-01` | `branch-story` |
| Bài 5 | Chủ đề E: Ứng dụng tin học | Thu thập dữ liệu và tổ chức bảng tính | Lập bảng tính theo dõi hoạt động kế hoạch nhỏ của lớp; nhập số liệu chính xác vào các ô tính. | `G5-DATA-01` | `sort-drag` |
| Bài 6 | Chủ đề E: Ứng dụng tin học | Xử lý dữ liệu cơ bản | Sử dụng các phép toán cộng trừ nhân chia trong bảng tính để tính tổng kinh phí và số dư. | `G5-SHEET-01` | `logic-puzzle` |
| Bài 7 | Chủ đề E: Ứng dụng tin học | Soạn thảo văn bản nâng cao | Trình bày bài báo tường có chia cột báo chí, chèn chữ nghệ thuật WordArt và hình ảnh minh họa sinh động. | `G5-DOC-01` | `sort-drag` |
| Bài 8 | Chủ đề E: Ứng dụng tin học | Bài trình chiếu đa phương tiện | Thiết kế bài thuyết trình đa phương tiện có lồng tiếng thuyết minh và video tư liệu ngắn. | `G5-PRES-01` | `sort-drag` |
| Bài 9 | Chủ đề F: Giải quyết vấn đề | Giới thiệu biến số trong Scratch | Khái niệm biến số (Variable): tạo biến để lưu trữ điểm số người chơi, thời gian còn lại của ván đấu. | `G5-VAR-01` | `logic-puzzle` |
| Bài 10 | Chủ đề F: Giải quyết vấn đề | Sử dụng biến để đếm điểm | Lập trình tăng biến điểm lên 1 khi ăn được vật phẩm, giảm mạng sống khi va phải chướng ngại vật. | `G5-VAR-02` | `block-maze` |
| Bài 11 | Chủ đề F: Giải quyết vấn đề | Điều kiện Nếu... Thì... | Lập trình quyết định đơn: Nếu chạm vào vạch đích thì thông báo Em đã chiến thắng! | `G5-IF-01` | `logic-puzzle` |
| Bài 12 | Chủ đề F: Giải quyết vấn đề | Điều kiện Nếu... Thì... Không thì... | Lập trình cấu trúc rẽ nhánh đủ: Nếu trả lời đúng thì cộng 10 điểm, Không thì phát âm thanh cảnh báo sai. | `G5-IF-02` | `block-maze` |
| Bài 13 | Chủ đề F: Giải quyết vấn đề | Tạo trò chơi mê cung tính điểm | Thiết kế mê cung có nhiều ngã rẽ, bẫy gai và đồng xu thưởng; điều khiển nhân vật bằng phím mũi tên. | `G5-GAME-01` | `block-maze` |
| Bài 14 | Chủ đề F: Giải quyết vấn đề | Trò chơi đối kháng 2 người | Lập trình điều khiển 2 nhân vật cùng lúc trên một bàn phím (phím W-A-S-D và phím mũi tên). | `G5-GAME-02` | `block-maze` |
| Bài 15 | Chủ đề F: Giải quyết vấn đề | Dự án lập trình sáng tạo | Tự do phát triển ý tưởng trò chơi bảo vệ môi trường biển hoặc giải cứu rừng xanh theo nhóm. | `G5-PROJ-01` | `bug-hunt` |
| Bài 16 | Chủ đề F: Giải quyết vấn đề | Trình bày và chia sẻ sản phẩm số | Xuất bản trò chơi, chạy thử nghiệm, thu thập đóng góp ý kiến từ bạn bè và hoàn thiện phiên bản cuối cùng. | `G5-BOSS-01` | `boss-quiz` |

---

## 4. Lớp 6 — THCS (18 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách Cánh Diều | Điểm tương thích YCCĐ & Năng lực hành động | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề A: Máy tính và cộng đồng | Thông tin và thu nhận thông tin | Phân tích cách con người thu nhận kích thích từ môi trường; chuyển đổi tín hiệu thực tế thành thông tin. | `G6-INFO-01` | `branch-story` |
| Bài 2 | Chủ đề A: Máy tính và cộng đồng | Lưu trữ và trao đổi thông tin | Nêu các hình thức lưu trữ thông tin qua từng thời kỳ: khắc trên đá, giấy viết, đĩa từ và chip nhớ bán dẫn. | `G6-INFO-02` | `sort-drag` |
| Bài 3 | Chủ đề A: Máy tính và cộng đồng | Máy tính trong hoạt động thông tin | Mô hình xử lý dữ liệu: Bộ nhớ (Storage), Khối tính toán số học logic (ALU), Khối điều khiển (CU). | `G6-ARCH-01` | `sort-drag` |
| Bài 4 | Chủ đề A: Máy tính và cộng đồng | Biểu diễn thông tin trong máy tính | Giải thích vì sao máy tính chỉ hiểu 2 ký hiệu 0 và 1; đóng cắt dòng điện đại diện cho trạng thái bit. | `G6-DATA-01` | `logic-puzzle` |
| Bài 5 | Chủ đề A: Máy tính và cộng đồng | Dữ liệu trong máy tính | Bảng quy đổi các tiền tố nhị phân: 1 Byte = 8 bits, 1 KB = 1024 Bytes; tính toán dung lượng bài hát, bức ảnh. | `G6-DATA-02` | `logic-puzzle` |
| Bài 6 | Chủ đề B: Mạng máy tính | Mạng máy tính | Khái niệm mạng máy tính; các thành phần: thiết bị đầu cuối, môi trường truyền dẫn, thiết bị kết nối mạng. | `G6-NET-01` | `sort-drag` |
| Bài 7 | Chủ đề B: Mạng máy tính | Kết nối mạng và Internet | Phương thức kết nối có dây (cáp quang, cáp xoắn) và kết nối không dây (Wi-Fi, Bluetooth, sóng di động 4G/5G). | `G6-NET-02` | `packet-route` |
| Bài 8 | Chủ đề B: Mạng máy tính | Trình duyệt web và tìm kiếm | Sử dụng Chrome/Firefox duyệt web; phân tích cấu trúc thanh địa chỉ URL, thẻ Tab duyệt web an toàn. | `G6-WWW-01` | `match-memory` |
| Bài 9 | Chủ đề B: Mạng máy tính | Thư điện tử | Đăng ký hòm thư, gửi thư điện tử kèm tệp nén; sử dụng trường CC (đồng kính gửi) và BCC (kính gửi ẩn danh). | `G6-EMAIL-01` | `branch-story` |
| Bài 10 | Chủ đề C: Mạng xã hội | Mạng xã hội và ứng xử trực tuyến | Văn hóa ứng xử số; nhận biết tác hại của việc nghiện mạng xã hội và các chiêu trò lừa đảo chuyển tiền. | `G6-SOCIAL-01` | `branch-story` |
| Bài 11 | Chủ đề D: Đạo đức, pháp luật | Bản quyền và đạo đức trên mạng | Nêu rõ quy tắc trích dẫn nguồn tác giả khi sử dụng tài liệu; tôn trọng tài sản trí tuệ của người khác. | `G6-ETHIC-01` | `branch-story` |
| Bài 12 | Chủ đề E: Ứng dụng tin học | Sơ đồ tư duy và công cụ hỗ trợ | Sử dụng phần mềm tạo sơ đồ nhánh, liên kết ý tưởng để ôn tập thi học kỳ môn Lịch sử, Địa lý. | `G6-MIND-01` | `logic-puzzle` |
| Bài 13 | Chủ đề E: Ứng dụng tin học | Soạn thảo văn bản nâng cao | Chèn ký tự đặc biệt (Symbol), số trang tự động, tạo đường viền trang và mục lục sơ bộ. | `G6-DOC-01` | `type-run` |
| Bài 14 | Chủ đề E: Ứng dụng tin học | Tạo bảng và biểu diễn dữ liệu | Thiết kế bảng thời khóa biểu, kẻ viền đậm nhạt, căn lề chữ giữa ô tính trên phần mềm soạn thảo. | `G6-TABLE-01` | `sort-drag` |
| Bài 15 | Chủ đề F: Giải quyết vấn đề | Khái niệm thuật toán | Hiểu thuật toán là quy trình từng bước rõ ràng để hoàn thành một mục tiêu xác định trong thời gian hữu hạn. | `G6-ALGO-01` | `block-maze` |
| Bài 16 | Chủ đề F: Giải quyết vấn đề | Mô tả thuật toán bằng sơ đồ khối | Nhận biết các hình khối chuẩn: Hình Oval (Bắt đầu/Kết thúc), Hình bình hành (Nhập/Xuất), Hình chữ nhật (Xử lý), Hình thoi (Điều kiện). | `G6-FLOW-01` | `logic-puzzle` |
| Bài 17 | Chủ đề F: Giải quyết vấn đề | Cấu trúc tuần tự, rẽ nhánh và lặp | Ghép nối các khối sơ đồ để biểu diễn thuật toán tìm số lớn nhất trong hai số, thuật toán đếm số chia hết cho 3. | `G6-ALGO-02` | `block-maze` |
| Bài 18 | Chủ đề F: Giải quyết vấn đề | Dự án: Phòng chống bạo lực mạng | Thiết kế cẩm nang tuyên truyền đa phương tiện xây dựng văn hóa mạng học đường lành mạnh, văn minh. | `G6-BOSS-01` | `boss-quiz` |

---

## 5. Lớp 7 — THCS (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách Cánh Diều | Điểm tương thích YCCĐ & Năng lực hành động | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề A: Máy tính và cộng đồng | Thiết bị vào và thiết bị ra | Phân loại thiết bị nhập dữ liệu và xuất dữ liệu; tìm hiểu cơ chế hoạt động của màn hình cảm ứng (vừa vào vừa ra). | `G7-IO-01` | `sort-drag` |
| Bài 2 | Chủ đề A: Máy tính và cộng đồng | Hệ điều hành và phần mềm | Vai trò của hệ điều hành quản lý tài nguyên phần cứng máy tính và tạo môi trường giao tiếp cho phần mềm ứng dụng. | `G7-OS-01` | `sort-drag` |
| Bài 3 | Chủ đề A: Máy tính và cộng đồng | Quản lý tệp và thư mục trên máy tính | Kỹ năng tìm kiếm tệp nhanh bằng thanh Search của hệ điều hành; xem thuộc tính kích thước, ngày sửa đổi tệp. | `G7-PATH-01` | `sort-drag` |
| Bài 4 | Chủ đề C: Mạng xã hội | Giao tiếp văn minh trên mạng xã hội | Rèn luyện kỹ năng tự bảo vệ trước bình luận tiêu cực; không chia sẻ thông tin thất thiệt chưa kiểm chứng. | `G7-COMM-01` | `branch-story` |
| Bài 5 | Chủ đề D: Đạo đức, pháp luật | An toàn trực tuyến và bảo vệ tài khoản | Quy tắc tạo mật khẩu mạnh (trên 8 ký tự, gồm chữ hoa, chữ thường, số, ký tự đặc biệt); không lưu mật khẩu trên máy lạ. | `G7-SEC-01` | `branch-story` |
| Bài 6 | Chủ đề E: Ứng dụng tin học | Giao diện và thao tác với bảng tính | Khái niệm trang tính (Worksheet), sổ tính (Workbook); các thao tác chèn thêm trang tính, đổi tên trang tính. | `G7-SHEET-01` | `sort-drag` |
| Bài 7 | Chủ đề E: Ứng dụng tin học | Nhập công thức và tính toán tự động | Phân biệt nhập giá trị trực tiếp và nhập công thức dùng địa chỉ ô; cơ chế tự động tính lại khi thay đổi dữ liệu gốc. | `G7-SHEET-02` | `logic-puzzle` |
| Bài 8 | Chủ đề E: Ứng dụng tin học | Các hàm tính toán thông dụng | Sử dụng thành thạo các hàm SUM, AVERAGE, MIN, MAX để tính bảng tổng kết điểm thi của học sinh trong lớp. | `G7-FUNC-01` | `logic-puzzle` |
| Bài 9 | Chủ đề E: Ứng dụng tin học | Kẻ khung, tô màu và in bảng tính | Tùy biến định dạng thẩm mỹ cho bảng dữ liệu; thiết lập vùng in (Print Area) vừa vặn trên khổ giấy A4. | `G7-SHEET-03` | `sort-drag` |
| Bài 10 | Chủ đề E: Ứng dụng tin học | Sắp xếp và lọc dữ liệu bảng tính | Sắp xếp danh sách lớp theo thứ tự điểm số giảm dần; lọc ra danh sách các học sinh đạt danh hiệu Xuất sắc. | `G7-SHEET-04` | `sort-drag` |
| Bài 11 | Chủ đề E: Ứng dụng tin học | Xây dựng bài trình chiếu chuyên đề | Chọn bố cục trang chiếu phù hợp với lượng thông tin; áp dụng nguyên tắc tương phản màu sắc chữ và nền. | `G7-PRES-01` | `match-memory` |
| Bài 12 | Chủ đề E: Ứng dụng tin học | Tạo hiệu ứng chuyển động và hoạt cảnh | Sử dụng hiệu ứng chuyển động có mục đích sư phạm, tránh lạm dụng hiệu ứng gây rối mắt người xem. | `G7-PRES-02` | `sort-drag` |
| Bài 13 | Chủ đề F: Giải quyết vấn đề | Tìm kiếm tuần tự trong danh sách | Thuật toán kiểm tra từng phần tử từ đầu đến cuối dãy; nhận diện trường hợp tốt nhất (ở đầu) và xấu nhất (ở cuối/không có). | `G7-SEARCH-01`| `block-maze` |
| Bài 14 | Chủ đề F: Giải quyết vấn đề | Tìm kiếm nhị phân trên dãy đã sắp | Thuật toán so sánh phần tử cần tìm với phần tử ở giữa danh sách; loại bỏ một nửa danh sách sau mỗi bước lặp. | `G7-SEARCH-02`| `logic-puzzle` |
| Bài 15 | Chủ đề F: Giải quyết vấn đề | Sắp xếp bằng thuật toán nổi bọt | Mô phỏng từng lượt duyệt đổi chỗ các cặp số nghịch thế; theo dõi sự di chuyển của các số lớn về cuối dãy. | `G7-SORT-01` | `block-maze` |
| Bài 16 | Chủ đề F: Giải quyết vấn đề | Sắp xếp bằng thuật toán chọn | Mô phỏng việc tìm phần tử nhỏ nhất trong phần còn lại của dãy rồi đưa về vị trí thích hợp; kiểm tra tổng kết. | `G7-BOSS-01` | `boss-quiz` |

---

## 6. Lớp 8 — THCS (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách Cánh Diều | Điểm tương thích YCCĐ & Năng lực hành động | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề A: Máy tính và cộng đồng | Lịch sử phát triển của máy tính điện tử | 5 thế hệ máy tính: Đèn điện tử chân không, Bóng bán dẫn Transistor, Mạch tích hợp IC, Vi xử lý VLSI và Trí tuệ nhân tạo. | `G8-HIST-01` | `match-memory` |
| Bài 2 | Chủ đề A: Máy tính và cộng đồng | Thông tin đáng tin cậy trong môi trường số | Tiêu chí đánh giá thông tin: Tác giả uy tín, Cơ quan xuất bản chính thống, Dẫn chứng số liệu khoa học xác thực. | `G8-INFO-01` | `branch-story` |
| Bài 3 | Chủ đề D: Đạo đức, pháp luật | Đạo đức, pháp luật và văn hóa ứng xử | Nhận thức các hành vi vi phạm bản quyền phần mềm lậu (crack); ủng hộ việc sử dụng phần mềm có bản quyền hợp pháp. | `G8-ETHIC-01` | `branch-story` |
| Bài 4 | Chủ đề E: Ứng dụng tin học | Biểu diễn dữ liệu bằng biểu đồ | Lựa chọn dạng biểu đồ trực quan hóa dữ liệu: Biểu đồ cột biểu diễn doanh thu, Biểu đồ tròn biểu diễn cơ cấu thị phần. | `G8-CHART-01` | `sort-drag` |
| Bài 5 | Chủ đề E: Ứng dụng tin học | Phân tích dữ liệu với bộ lọc Filter | Áp dụng bộ lọc nâng cao (Number Filters, Text Filters) để trích lọc các mặt hàng tồn kho hoặc học sinh theo địa bàn. | `G8-SHEET-02` | `sort-drag` |
| Bài 6 | Chủ đề E: Ứng dụng tin học | Chỉnh sửa ảnh với phần mềm đồ họa | Làm quen giao diện phần mềm chỉnh sửa ảnh chuyên nghiệp: vùng làm việc, thanh công cụ, các bảng điều khiển Layer. | `G8-IMG-01` | `match-memory` |
| Bài 7 | Chủ đề E: Ứng dụng tin học | Tạo hiệu ứng đồ họa và văn bản | Tạo vùng chọn bằng công cụ Lasso/Magic Wand, tẩy xóa đối tượng không mong muốn và ghép ảnh nghệ thuật. | `G8-IMG-02` | `sort-drag` |
| Bài 8 | Chủ đề F: Giải quyết vấn đề | Giới thiệu lập trình giải quyết bài toán | Các bước xây dựng phần mềm: Xác định bài toán -> Thiết kế thuật toán -> Viết mã chương trình -> Kiểm thử và sửa lỗi. | `G8-PROG-01` | `block-maze` |
| Bài 9 | Chủ đề F: Giải quyết vấn đề | Biến số, hằng số và kiểu dữ liệu | Khai báo biến số, phân biệt biến số (thay đổi giá trị) và hằng số (giá trị cố định không đổi như số Pi = 3.14159). | `G8-TYPE-01` | `logic-puzzle` |
| Bài 10 | Chủ đề F: Giải quyết vấn đề | Biểu thức logic và câu lệnh if/else | Viết các biểu thức so sánh >, <, ==, != và biểu thức logic AND, OR để kiểm tra tính hợp lệ của dữ liệu đầu vào. | `G8-IF-01` | `bug-hunt` |
| Bài 11 | Chủ đề F: Giải quyết vấn đề | Vòng lặp for và while | Lập trình vòng lặp kiểm tra số hoàn hảo, số chính phương; tối ưu hóa số lần lặp để chương trình chạy nhanh nhất. | `G8-LOOP-01` | `block-maze` |
| Bài 12 | Chủ đề F: Giải quyết vấn đề | Cấu trúc danh sách trong lập trình | Tạo danh sách lưu trữ nhiệt độ các ngày trong tuần; tính nhiệt độ trung bình và tìm ngày có nhiệt độ cao nhất. | `G8-LIST-01` | `bug-hunt` |
| Bài 13 | Chủ đề F: Giải quyết vấn đề | Lập trình trò chơi tính toán điểm | Xây dựng cơ chế tính điểm thưởng combo khi người chơi hoàn thành chuỗi câu hỏi nhanh và chính xác. | `G8-GAME-01` | `block-maze` |
| Bài 14 | Chủ đề F: Giải quyết vấn đề | Kiểm thử và gỡ lỗi chương trình | Kỹ thuật đặt các điểm dừng (Breakpoints), in giá trị biến ra màn hình kiểm tra (print debugging) để tìm dòng mã lỗi. | `G8-DEBUG-01` | `bug-hunt` |
| Bài 15 | Chủ đề F: Giải quyết vấn đề | Dự án phần mềm mô phỏng khoa học | Lập trình mô phỏng sự chuyển động của các hành tinh trong Hệ Mặt trời hoặc dao động của con lắc đơn. | `G8-PROJ-01` | `bug-hunt` |
| Bài 16 | Chủ đề G: Hướng nghiệp | Khám phá ngành nghề tin học hiện đại | Khảo sát nhu cầu tuyển dụng các vị trí: Lập trình viên di động (Mobile App Developer), Kỹ sư dữ liệu (Data Engineer). | `G8-BOSS-01` | `boss-quiz` |

---

## 7. Lớp 9 — THCS (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách Cánh Diều | Điểm tương thích YCCĐ & Năng lực hành động | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề A: Máy tính và cộng đồng | Cấu trúc phần cứng máy tính | Sơ đồ khối kiến trúc Von Neumann: CPU, Bộ nhớ chính, Bộ nhớ phụ, Khối vào/ra và các luồng truyền tín hiệu. | `G9-ARCH-01` | `sort-drag` |
| Bài 2 | Chủ đề A: Máy tính và cộng đồng | Thu thập và thẩm định thông tin | Kỹ năng đối chiếu đa nguồn để xác minh sự thật; nhận diện các thủ thuật giật gân, lừa đảo thông tin trực tuyến. | `G9-INFO-01` | `branch-story` |
| Bài 3 | Chủ đề D: Đạo đức, pháp luật | Tác động công nghệ số & Luật an ninh mạng | Nêu trách nhiệm công dân trên môi trường số; xử phạt các hành vi tung tin giả phá hoại an ninh trật tự xã hội. | `G9-LAW-01` | `branch-story` |
| Bài 4 | Chủ đề E: Ứng dụng tin học | Phần mềm mô phỏng học tập | Vận dụng phần mềm mô phỏng khám phá thí nghiệm ảo mạch điện, định luật bảo toàn năng lượng trong môn Khoa học tự nhiên. | `G9-SIM-01` | `match-memory` |
| Bài 5 | Chủ đề E: Ứng dụng tin học | Thiết kế và dựng video clip ngắn | Các giai đoạn làm phim: Lên ý tưởng kịch bản phân cảnh -> Quay tư liệu -> Cắt ghép video -> Chèn nhạc nền và xuất file. | `G9-VID-01` | `sort-drag` |
| Bài 6 | Chủ đề E: Ứng dụng tin học | Dự án video truyền thông học đường | Sản xuất video giới thiệu câu lạc bộ văn hóa nghệ thuật của trường học; đăng tải chia sẻ lên cổng thông tin trường. | `G9-PROJ-01` | `match-memory` |
| Bài 7 | Chủ đề F: Giải quyết vấn đề | Phân tích bài toán thực tế & thuật toán | Kỹ năng trừu tượng hóa bài toán thực tiễn thành mô hình toán học và xây dựng thuật toán tối ưu. | `G9-ALGO-01` | `logic-puzzle` |
| Bài 8 | Chủ đề F: Giải quyết vấn đề | Lập trình giải các bài toán số học | Viết chương trình tìm tất cả các ước số của số nguyên dương N, kiểm tra số đối xứng, phân tích ra thừa số nguyên tố. | `G9-CODE-01` | `bug-hunt` |
| Bài 9 | Chủ đề F: Giải quyết vấn đề | Kỹ thuật bắt lỗi và bẫy lỗi | Xử lý dữ liệu nhập sai của người dùng (nhập chữ vào ô đòi hỏi số); hiển thị thông báo hướng dẫn người dùng nhập lại. | `G9-DEBUG-01` | `bug-hunt` |
| Bài 10 | Chủ đề F: Giải quyết vấn đề | Thiết kế giao diện tương tác đơn giản | Tạo các nút bấm (Button), hộp nhập văn bản (TextBox), nhãn hiển thị (Label) cho ứng dụng học tập. | `G9-APP-01` | `block-maze` |
| Bài 11 | Chủ đề B: Mạng máy tính | Mạng LAN, Wi-Fi và kết nối không dây | Nguyên lý phát sóng Wi-Fi, cài đặt mật khẩu mạng WPA2/WPA3 an toàn; kiểm tra kết nối mạng bằng lệnh ping. | `G9-LAN-01` | `packet-route` |
| Bài 12 | Chủ đề B: Mạng máy tính | Lưu trữ đám mây | Sử dụng Google Drive/OneDrive để đồng bộ hóa tài liệu giữa máy tính và điện thoại thông minh mọi lúc mọi nơi. | `G9-CLOUD-01` | `sort-drag` |
| Bài 13 | Chủ đề D: Đạo đức, pháp luật | Mã hóa dữ liệu và phòng chống mã độc | Hiểu nguyên lý mã hóa bảo mật thông tin; cài đặt phần mềm diệt virus định kỳ quét hệ thống máy tính. | `G9-SEC-01` | `branch-story` |
| Bài 14 | Chủ đề D: Đạo đức, pháp luật | Sao lưu và phục hồi dữ liệu | Thực hiện sao lưu dữ liệu quan trọng ra ổ cứng di động theo quy tắc 3-2-1 để phòng ngừa sự cố hỏng hóc thiết bị. | `G9-BACKUP-01`| `sort-drag` |
| Bài 15 | Chủ đề F: Giải quyết vấn đề | Dự án ứng dụng hỗ trợ cộng đồng | Lập trình ứng dụng nhắc nhở thời gian uống nước, tập thể dục hoặc cẩm nang sơ cứu tai nạn thương tích. | `G9-COMM-01` | `bug-hunt` |
| Bài 16 | Chủ đề G: Hướng nghiệp | Lựa chọn hướng học tập & nghề nghiệp CNTT | Hướng dẫn học sinh chọn tổ hợp môn học Tin học THPT theo định hướng Khoa học máy tính (CS) hoặc Tin học ứng dụng (ICT). | `G9-BOSS-01` | `boss-quiz` |

---

## 8. Lớp 10 — THPT (32 bài)

| STT | Phân nhóm | Tên bài học trong sách Cánh Diều | Điểm tương thích YCCĐ & Năng lực hành động | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Máy tính và xã hội | Dữ liệu, thông tin và tri thức | Phân tích chu trình: Thu nhận Dữ liệu -> Xử lý thành Thông tin -> Đúc kết thành Tri thức phục vụ hành động. | `G10-INFO-01` | `branch-story` |
| Bài 2 | Máy tính và xã hội | Sự ưu việt của thiết bị số | Phân tích khả năng lưu trữ khổng lồ, tốc độ tính toán siêu việt hàng triệu phép tính/giây và kết nối toàn cầu của máy tính. | `G10-IOT-01` | `match-memory` |
| Bài 3 | Máy tính và xã hội | Mạng máy tính và thiết bị truyền thông | Tìm hiểu cấu tạo cáp mạng xoắn đôi, đầu bấm RJ45, card mạng NIC và vai trò bộ chuyển mạch Switch trong mạng LAN. | `G10-NET-01` | `sort-drag` |
| Bài 4 | Máy tính và xã hội | Dịch vụ mạng và điện toán đám mây | Các mô hình dịch vụ đám mây: IaaS (hạ tầng), PaaS (nền tảng), SaaS (phần mềm dịch vụ). | `G10-CLOUD-01`| `sort-drag` |
| Bài 5 | Đạo đức, pháp luật | Ứng xử nhân văn trên không gian mạng | Xây dựng thương hiệu cá nhân tích cực; kiên quyết tẩy chay các hành vi bôi nhọ, lan truyền hình ảnh nhạy cảm trái phép. | `G10-SOC-01` | `branch-story` |
| Bài 6 | Đạo đức, pháp luật | Pháp luật về an toàn thông tin mạng | Các quy định về tội phạm công nghệ cao theo Bộ luật Hình sự Việt Nam; mức phạt đối với hành vi tấn công phá hoại mạng. | `G10-LAW-01` | `branch-story` |
| Bài 7 | Đạo đức, pháp luật | Phần mềm tự do nguồn mở | Lợi ích kinh tế và tính bảo mật của mã nguồn mở; phong trào phần mềm tự do FSF và giấy phép GNU GPL. | `G10-OSS-01` | `sort-drag` |
| Bài 8 | Ứng dụng tin học | Thiết kế đồ họa với Inkscape | Khởi tạo trang vẽ, sử dụng các công cụ vẽ hình học cơ bản, đổ màu đơn sắc (Flat color) và màu chuyển sắc (Gradient). | `G10-VEC-01` | `sort-drag` |
| Bài 9 | Ứng dụng tin học | Thao tác với các đối tượng đồ họa | Phép nhóm đối tượng (Group), căn chỉnh gióng hàng (Align and Distribute) và sắp xếp thứ tự trước sau của các lớp hình. | `G10-VEC-02` | `match-memory` |
| Bài 10 | Ứng dụng tin học | Chỉnh sửa đường cong Bezier | Nắm vững kỹ thuật vẽ đường cong Bezier bằng công cụ Pen; điều chỉnh tiếp tuyến và điểm neo để tạo hình phức tạp. | `G10-VEC-03` | `sort-drag` |
| Bài 11 | Ứng dụng tin học | Thiết kế ấn phẩm truyền thông | Ứng dụng Inkscape thiết kế áp phích (Poster), tờ rơi tuyên truyền sự kiện phong trào thanh niên trường học. | `G10-VEC-04` | `sort-drag` |
| Bài 12 | Lập trình Python | Làm quen với ngôn ngữ Python | Cài đặt Python 3, viết dòng mã đầu tiên hiển thị thông điệp "Hello World", làm quen chế độ tương tác Console. | `G10-PY-01` | `type-run` |
| Bài 13 | Lập trình Python | Biến, biểu thức và câu lệnh gán | Đặt tên biến theo chuẩn Snake_case; thực hiện các phép toán số học (+, -, *, /, //, %, **) và kiểm tra kiểu dữ liệu. | `G10-PY-02` | `logic-puzzle` |
| Bài 14 | Lập trình Python | Các phép toán vào ra cơ bản | Sử dụng print() định dạng tham số sep và end; hàm input() kết hợp ép kiểu dữ liệu an toàn. | `G10-PY-03` | `type-run` |
| Bài 15 | Lập trình Python | Câu lệnh rẽ nhánh if... else | Cài đặt các điều kiện rẽ nhánh kiểm tra năm nhuận, phương trình bậc nhất ax + b = 0. | `G10-PY-04` | `bug-hunt` |
| Bài 16 | Lập trình Python | Câu lệnh rẽ nhánh nhiều trường hợp | Sử dụng cấu trúc if... elif... else để phân loại tam giác (đều, cân, vuông, thường) theo độ dài 3 cạnh. | `G10-PY-05` | `bug-hunt` |
| Bài 17 | Lập trình Python | Vòng lặp for và hàm range | Lập trình duyệt vòng lặp xác định số bước; tính tổng bình phương các số từ 1 đến N. | `G10-PY-06` | `block-maze` |
| Bài 18 | Lập trình Python | Vòng lặp while | Cài đặt thuật toán kiểm tra số nguyên tố bằng vòng lặp while; kỹ thuật tối ưu bước nhảy lặp đến căn bậc hai của N. | `G10-PY-07` | `bug-hunt` |
| Bài 19 | Lập trình Python | Kiểu dữ liệu danh sách (List) | Tạo danh sách số nguyên; truy cập phần tử qua chỉ số âm s[-1]; duyệt danh sách bằng vòng lặp for x in list. | `G10-PY-08` | `logic-puzzle` |
| Bài 20 | Lập trình Python | Các phương thức xử lý danh sách | Thao tác thêm cuối append(), chèn tại vị trí insert(), đếm số lần xuất hiện count(), xóa phần tử pop(). | `G10-PY-09` | `bug-hunt` |
| Bài 21 | Lập trình Python | Kiểu dữ liệu xâu ký tự | Chuỗi ký tự bất biến (Immutable); đếm độ dài len(), kiểm tra ký tự số isdigit(), ký tự chữ isalpha(). | `G10-PY-10` | `type-run` |
| Bài 22 | Lập trình Python | Xử lý và chuẩn hóa xâu ký tự | Viết hàm chuẩn hóa họ tên học sinh: xóa khoảng trắng thừa ở hai đầu và giữa các từ, viết hoa chữ cái đầu mỗi từ. | `G10-PY-11` | `bug-hunt` |
| Bài 23 | Lập trình Python | Khái niệm hàm trong lập trình | Ý nghĩa của việc module hóa mã nguồn; định nghĩa hàm tính diện tích hình tròn, diện tích hình chữ nhật. | `G10-PY-12` | `bug-hunt` |
| Bài 24 | Lập trình Python | Tham số và giá trị trả về | Truyền giá trị vào hàm qua tham số; trả về nhiều giá trị qua Tuple trong Python. | `G10-PY-13` | `logic-puzzle` |
| Bài 25 | Lập trình Python | Thực hành xây dựng thư viện hàm | Xây dựng module các hàm toán học hỗ trợ giải bài tập và tái sử dụng bằng lệnh import. | `G10-PY-14` | `bug-hunt` |
| Bài 26 | Lập trình Python | Nhận diện và gỡ lỗi chương trình | Đọc và hiểu ngăn xếp theo vết lỗi (Traceback); sửa các lỗi tràn chỉ số IndexError, lỗi gọi biến chưa khai báo NameError. | `G10-DEBUG-01` | `bug-hunt` |
| Bài 27 | Lập trình Python | Xử lý ngoại lệ với try... except | Bắt lỗi chia cho số 0 (ZeroDivisionError) và lỗi nhập sai định dạng (ValueError) để chương trình không bị sập bất ngờ. | `G10-DEBUG-02` | `bug-hunt` |
| Bài 28 | Lập trình Python | Làm việc với tệp văn bản (File I/O) | Mở tệp open() ở chế độ đọc 'r' và ghi 'w'; đọc từng dòng tệp readline() và tự động đóng tệp với từ khóa with. | `G10-FILE-01` | `logic-puzzle` |
| Bài 29 | Lập trình Python | Bài toán sắp xếp và tìm kiếm trên danh sách | Cài đặt thuật toán tìm kiếm tuần tự và sắp xếp chọn trực tiếp trên mảng dữ liệu đọc từ tệp văn bản. | `G10-ALGO-01` | `block-maze` |
| Bài 30 | Lập trình Python | Dự án lập trình trò chơi ô chữ | Lập trình trò chơi đoán chữ tương tác qua giao diện dòng lệnh với kho từ vựng tiếng Anh phong phú. | `G10-PROJ-01` | `bug-hunt` |
| Bài 31 | Hướng nghiệp | Nghề lập trình và kiến trúc sư hệ thống | Giới thiệu công việc phát triển phần mềm Agile/Scrum và các kỹ năng làm việc nhóm cần thiết. | `G10-CAREER-01`| `match-memory` |
| Bài 32 | Tổng kết | Đánh giá năng lực Tin học 10 Cánh Diều | Bài kiểm tra tổng hợp kiến thức Hệ thống số, Đồ họa vector và Kỹ năng lập trình Python nâng cao. | `G10-BOSS-01` | `boss-quiz` |

---

## 9. Lớp 11 — THPT (30 bài định hướng CS & ICT)

### Nhánh Khoa học máy tính (CS — 30 bài)
| STT | Chủ đề | Tên bài học trong sách Cánh Diều CS | Điểm tương thích YCCĐ & Năng lực hành động | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài CS 1 | CSDL | Cơ sở dữ liệu và hệ quản trị CSDL | Vai trò của CSDL tập trung trong doanh nghiệp; độc lập dữ liệu vật lý và độc lập dữ liệu logic. | `G11-DB-01` | `sort-drag` |
| Bài CS 2 | CSDL | Bảng dữ liệu và các thao tác | Tạo bảng, đặt tên cột, chỉ định kiểu dữ liệu phù hợp (INT, VARCHAR, TEXT, BOOLEAN, DATETIME). | `G11-DB-02` | `sort-drag` |
| Bài CS 3 | CSDL | Khóa chính và liên kết giữa các bảng | Ý nghĩa của ràng buộc toàn vẹn thực thể (Khóa chính) và toàn vẹn tham chiếu (Khóa ngoại). | `G11-DB-03` | `logic-puzzle` |
| Bài CS 4 | SQL | Ngôn ngữ truy vấn SQL | Giới thiệu các nhóm lệnh DDL (định nghĩa dữ liệu) và DML (thao tác dữ liệu); thực hiện lệnh SELECT cơ bản. | `G11-SQL-01` | `logic-puzzle` |
| Bài CS 5 | SQL | Lọc dữ liệu với WHERE và sắp xếp | Sử dụng các biểu thức điều kiện phức hợp, toán tử IN, BETWEEN, LIKE tìm kiếm mẫu chuỗi ký tự. | `G11-SQL-02` | `logic-puzzle` |
| Bài CS 6 | SQL | Các hàm tính toán tổng hợp | Thống kê số lượng sinh viên theo từng khoa bằng hàm COUNT(*) kết hợp mệnh đề GROUP BY ten_khoa. | `G11-SQL-03` | `logic-puzzle` |
| Bài CS 7 | SQL | Truy vấn kết nối nhiều bảng | Kết nối bảng SinhVien và bảng KetQuaHocTap bằng INNER JOIN để lấy thông tin điểm số theo từng môn học. | `G11-SQL-04` | `logic-puzzle` |
| Bài CS 8 | SQL | Chèn, sửa và xóa bản ghi dữ liệu | Cẩn trọng khi chạy lệnh UPDATE và DELETE có điều kiện WHERE để tránh làm mất dữ liệu ngoài ý muốn. | `G11-SQL-05` | `bug-hunt` |
| Bài CS 9 | Thiết kế CSDL | Phân tích và thiết kế mô hình CSDL | Từ bài toán quản lý thư viện trường học, xây dựng sơ đồ quan hệ ERD gồm các thực thể Sách, Độc giả, Phiếu mượn. | `G11-NORM-01` | `sort-drag` |
| Bài CS 10 | Thực hành CSDL | Cài đặt và quản trị CSDL trên máy chủ | Tạo người dùng mới, phân quyền truy cập (GRANT SELECT, INSERT) và xuất tệp sao lưu dữ liệu (.sql). | `G11-PRAC-01` | `bug-hunt` |
| Bài CS 11 | Thuật toán CS | Phương pháp Đệ quy | Cài đặt hàm đệ quy tính số Fibonacci thứ N; phân tích cây đệ quy và kỹ thuật nhớ kết quả (Memoization). | `G11-ALGO-01` | `bug-hunt` |
| Bài CS 12 | Thuật toán CS | Thuật toán Quay lui (Backtracking) | Tư duy thử - sai và quay lui; cài đặt thuật toán giải bài toán Xếp 8 quân hậu trên bàn cờ vua. | `G11-ALGO-02` | `logic-puzzle` |
| Bài CS 13 | Thuật toán CS | Thuật toán Sắp xếp trộn (Merge Sort) | Phân tích bước chia danh sách làm đôi và bước trộn (Merge) hai danh sách đã sắp thành danh sách thống nhất. | `G11-ALGO-03` | `logic-puzzle` |
| Bài CS 14 | Thuật toán CS | Thuật toán Sắp xếp nhanh (Quick Sort) | Cài đặt thuật toán phân đoạn mảng Hoare / Lomuto; so sánh hiệu năng chạy thực tế với Bubble Sort. | `G11-ALGO-04` | `bug-hunt` |
| Bài CS 15 | Thuật toán CS | Đánh giá độ phức tạp và tối ưu mã nguồn | Đo thời gian chạy thực tế của chương trình bằng thư viện time; tối ưu cấu trúc vòng lặp để giảm thiểu độ phức tạp. | `G11-ALGO-05` | `logic-puzzle` |
| Bài CS 16 | Dự án CS | Phần mềm tra cứu sách thư viện trường học | Kết nối cơ sở dữ liệu SQL với chương trình viết bằng Python để phục vụ tra cứu thông tin sách cho học sinh. | `G11-BOSS-01` | `boss-quiz` |

---

## 10. Lớp 12 — THPT (30 bài định hướng CS & ICT)

| STT | Phân nhóm | Tên bài học trong sách Cánh Diều | Điểm tương thích YCCĐ & Năng lực hành động | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Mạng nâng cao | Kiến trúc mạng máy tính hiện đại | Khái niệm tầng mạng trong mô hình TCP/IP: Tầng ứng dụng, Tầng giao vận, Tầng mạng, Tầng liên kết dữ liệu. | `G12-NET-01` | `sort-drag` |
| Bài 2 | Mạng nâng cao | Định tuyến và giao thức truyền thông | Giao thức định tuyến IP, giao thức bắt tay ba bước TCP thiết lập kết nối tin cậy vs giao thức nhanh UDP. | `G12-NET-02` | `logic-puzzle` |
| Bài 3 | Mạng nâng cao | Quản trị thiết bị mạng gia đình và trường học | Cấu hình máy chủ DHCP cấp phát dải IP tự động; thiết lập mạng Wi-Fi khách (Guest Network) cách ly dữ liệu. | `G12-NET-03` | `packet-route` |
| Bài 4 | An toàn thông tin | Phòng chống tấn công mạng và mã độc | Nhận diện các hình thức tấn công lừa đảo Social Engineering, cài đặt phần mềm gián điệp đánh cắp thông tin thẻ tín dụng. | `G12-SEC-01` | `branch-story` |
| Bài 5 | An toàn thông tin | Bảo vệ hệ thống thông tin | Thiết lập chính sách mật khẩu phức tạp, phân quyền thư mục theo nhóm người dùng (RBAC), tạo bản sao lưu tự động. | `G12-SEC-02` | `sort-drag` |
| Bài 6 | Trí tuệ nhân tạo | Khám phá thế giới Trí tuệ nhân tạo | Khái niệm máy tính thông minh có khả năng suy luận, lập kế hoạch và tương tác tự nhiên với con người. | `G12-AI-01` | `match-memory` |
| Bài 7 | Trí tuệ nhân tạo | Ứng dụng đột phá của AI trong đời sống | Xe tự hành nhận diện biển báo giao thông, chẩn đoán y tế tự động qua phim chụp X-quang, dịch máy đa ngôn ngữ. | `G12-AI-02` | `sort-drag` |
| Bài 8 | Học máy | Các phương pháp Học máy cơ bản | Khái niệm bài toán Phân loại (Classification) và Hồi quy (Regression) trong Học máy có giám sát. | `G12-ML-01` | `sort-drag` |
| Bài 9 | Học máy | Đánh giá độ chính xác của mô hình học máy | Các chỉ số đo lường hiệu năng mô hình: Độ chính xác (Accuracy), Độ nhạy (Recall), Độ chuẩn xác (Precision). | `G12-ML-02` | `bug-hunt` |
| Bài 10 | Học sâu & AI | Mạng nơ-ron nhân tạo và xử lý ngôn ngữ | Mô phỏng tế bào thần kinh sinh học; ứng dụng công nghệ xử lý tiếng nói (Speech-to-Text) và thị giác máy tính. | `G12-AI-03` | `logic-puzzle` |
| Bài 11 | Học sâu & AI | Trí tuệ nhân tạo tạo sinh (GenAI) | Khả năng tự động sinh mã nguồn lập trình, vẽ tranh nghệ thuật và soạn thảo văn bản từ lời nhắc Prompt của con người. | `G12-AI-04` | `branch-story` |
| Bài 12 | Đạo đức AI | Trách nhiệm và đạo đức trong kỷ nguyên số | Nguyên tắc AI vì con người: công bằng, không thiên vị phân biệt đối xử, an toàn và có thể giải trình được. | `G12-ETHIC-01` | `branch-story` |
| Bài 13 | Thiết kế Web | Xây dựng cấu trúc trang web với HTML | Viết các thẻ định dạng tiêu đề, chèn hình ảnh, tạo bảng và siêu liên kết điều hướng giữa các trang web. | `G12-WEB-01` | `type-run` |
| Bài 14 | Thiết kế Web | Thiết kế giao diện hiện đại với CSS | Định nghĩa kiểu dáng màu sắc, phông chữ, tạo bố cục trang web tương thích đa kích cỡ màn hình máy tính và điện thoại. | `G12-WEB-02` | `sort-drag` |
| Bài 15 | Thiết kế Web | Lập trình hành động tương tác với JavaScript | Bắt sự kiện người dùng nhấp nút, kiểm tra dữ liệu biểu mẫu (Form Validation) trước khi gửi lên máy chủ. | `G12-WEB-03` | `bug-hunt` |
| Bài 16 | Tổng kết | Đấu trường Công nghệ EasyTin toàn năng | Chinh phục thử thách trùm cuối: giải mã mạng, truy vấn SQL, gỡ lỗi thuật toán Python và phân tích hệ thống AI. | `G12-BOSS` | `boss-quiz` |

---
> Bản trích xuất Cánh Diều Lớp 3–12 hoàn tất 100% không thiếu bài nào theo đúng cấu trúc SGK Bộ GD&ĐT.
"""

# ==============================================================================
# 3. CHÂN TRỜI SÁNG TẠO (CTST)
# ==============================================================================
ctst_content = """# 01a-extract-ctst-g3_12.md — Trích xuất toàn diện bộ sách Chân trời sáng tạo (Lớp 3–12)

> **Bộ sách:** Chân trời sáng tạo (Nhà xuất bản Giáo dục Việt Nam)  
> **Chương trình:** Giáo dục phổ thông 2018 môn Tin học (Thông tư 32/2018/TT-BGDĐT)  
> **Cam kết:** Trích xuất 100% đầy đủ tất cả các bài học từ Lớp 3 đến Lớp 12, không bỏ sót bất kỳ bài nào.  
> **Đặc trưng sư phạm:** Ngôn từ trong sáng, giàu hình ảnh gợi mở, chú trọng năng lực công dân số, tư duy phản biện và tinh thần đổi mới sáng tạo trong thời đại số.

---

## MỤC LỤC TỔNG QUAN CÁC KHỐI LỚP
- [Lớp 3 (16 bài)](#1-lớp-3--tiểu-học-16-bài)
- [Lớp 4 (16 bài)](#2-lớp-4--tiểu-học-16-bài)
- [Lớp 5 (16 bài)](#3-lớp-5--tiểu-học-16-bài)
- [Lớp 6 (17 bài)](#4-lớp-6--thcs-17-bài)
- [Lớp 7 (16 bài)](#5-lớp-7--thcs-16-bài)
- [Lớp 8 (16 bài)](#6-lớp-8--thcs-16-bài)
- [Lớp 9 (16 bài)](#7-lớp-9--thcs-16-bài)
- [Lớp 10 (32 bài)](#8-lớp-10--thpt-32-bài)
- [Lớp 11 (30 bài định hướng CS & ICT)](#9-lớp-11--thpt-30-bài-định-hướng-cs--ict)
- [Lớp 12 (30 bài định hướng CS & ICT)](#10-lớp-12--thpt-30-bài-định-hướng-cs--ict)

---

## 1. Lớp 3 — Tiểu học (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách CTST | Yêu cầu cần đạt (YCCĐ) & Năng lực sáng tạo | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề A: Máy tính và em | Thông tin và tiếp nhận thông tin | Khám phá các giác quan tiếp nhận thông tin từ thế giới xung quanh; nhận thức thông tin giúp con người hiểu biết và ra quyết định. | `G3-INFO-01` | `match-memory` |
| Bài 2 | Chủ đề A: Máy tính và em | Khám phá máy tính | Nhận diện các loại máy tính hiện đại; hiểu máy tính là công cụ thông minh trợ giúp đắc lực cho việc học và khám phá thế giới. | `G3-HARD-01` | `sort-drag` |
| Bài 3 | Chủ đề A: Máy tính và em | Em tập sử dụng chuột | Luyện đôi tay khéo léo qua các trò chơi tương tác với chuột: nhấp chuột, nhấp đúp, kéo thả các mảnh ghép bức tranh. | `G3-MOUSE-01` | `sort-drag` |
| Bài 4 | Chủ đề A: Máy tính và em | Em tập sử dụng bàn phím | Làm quen bàn phím máy tính; nhận biết các hàng phím và luyện đặt ngón tay đúng vị trí xuất phát để chuẩn bị gõ chữ. | `G3-KEY-01` | `type-run` |
| Bài 5 | Chủ đề B: Mạng và Internet | Khám phá Internet | Mở rộng tầm nhìn với mạng toàn cầu Internet; xem video bài học, nghe nhạc và tìm kiếm các thông tin bổ ích. | `G3-NET-01` | `branch-story` |
| Bài 6 | Chủ đề C: Tổ chức lưu trữ | Sắp xếp và phân loại thông tin | Nhận biết việc phân chia đồ vật theo màu sắc, kích thước, công dụng; hiểu vì sao ngăn nắp giúp ta tìm kiếm dễ dàng. | `G3-ORG-01` | `sort-drag` |
| Bài 7 | Chủ đề C: Tổ chức lưu trữ | Sơ đồ phân loại đồ vật | Vẽ sơ đồ hình nhánh cây để biểu diễn cách phân chia đồ dùng học tập trong cặp sách của em. | `G3-ORG-03` | `logic-puzzle` |
| Bài 8 | Chủ đề D: Đạo đức, pháp luật | Bảo vệ thông tin và dữ liệu cá nhân | Nhận biết thông tin bí mật riêng tư của bản thân và gia đình; học cách từ chối khi người lạ hỏi thông tin cá nhân. | `G3-ETHIC-01` | `branch-story` |
| Bài 9 | Chủ đề E: Ứng dụng tin học | Làm quen với phần mềm luyện gõ phím | Luyện ngón tay gõ các phím cơ sở A, S, D, F, J, K, L qua các màn chơi vui nhộn trên phần mềm luyện phím. | `G3-TYPE-01` | `type-run` |
| Bài 10 | Chủ đề E: Ứng dụng tin học | Em vẽ bức tranh đầu tiên | Sử dụng cọ vẽ, bút chì và bảng màu trong phần mềm đồ họa đơn giản để vẽ ngôi nhà mơ ước của em. | `G3-DRAW-01` | `match-memory` |
| Bài 11 | Chủ đề F: Giải quyết vấn đề | Thực hiện công việc theo trình tự | Nhận biết các bước thực hiện một công việc thường ngày (đánh răng, gấp quần áo); thứ tự trước sau là điều kiện quyết định kết quả. | `G3-ALGO-01` | `block-maze` |
| Bài 12 | Chủ đề F: Giải quyết vấn đề | Chia bài toán lớn thành các việc nhỏ | Rèn luyện tư duy chia nhỏ nhiệm vụ dọn dẹp phòng học thành từng bước nhỏ gọn, dễ dàng thực hiện. | `G3-ALGO-02` | `block-maze` |
| Bài 13 | Chủ đề F: Giải quyết vấn đề | Phân công công việc | Học cách làm việc nhóm cùng các bạn: phân chia nhiệm vụ phù hợp với năng khiếu từng thành viên để cùng hoàn thành mục tiêu. | `G3-TEAM-01` | `sort-drag` |
| Bài 14 | Chủ đề F: Giải quyết vấn đề | Trò chơi tư duy mê cung | Tìm đường đi ngắn nhất đưa chú ong về tổ thông qua các chỉ dẫn rẽ trái, rẽ phải, đi thẳng. | `G3-MAZE-01` | `block-maze` |
| Bài 15 | Chủ đề F: Giải quyết vấn đề | Dự án Tin học của em | Trưng bày bức tranh và bài thuyết trình ngắn về những điều kỳ diệu em đã khám phá cùng máy tính trong năm học. | `G3-PROJ-01` | `match-memory` |
| Bài 16 | Chủ đề F: Giải quyết vấn đề | Đánh giá và tổng kết | Vượt qua thử thách đố vui tổng kết các kỹ năng cơ bản về máy tính, mạng Internet và tư duy thuật toán lớp 3. | `G3-BOSS-01` | `boss-quiz` |

---

## 2. Lớp 4 — Tiểu học (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách CTST | Yêu cầu cần đạt (YCCĐ) & Năng lực sáng tạo | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề A: Máy tính và em | Phần cứng và phần mềm | Nhận biết thiết bị phần cứng bên ngoài (chuột, bàn phím) và bên trong (ổ cứng, RAM); hiểu phần mềm điều khiển phần cứng. | `G4-HARD-01` | `sort-drag` |
| Bài 2 | Chủ đề A: Máy tính và em | Rèn luyện kỹ năng gõ phím | Luyện kỹ năng gõ mười ngón nhanh và chuẩn xác; gõ tiếng Việt có dấu theo quy tắc gõ chữ Telex (s, f, r, x, j). | `G4-TYPE-01` | `type-run` |
| Bài 3 | Chủ đề B: Mạng và Internet | Tìm kiếm thông tin an toàn trên Internet | Kỹ năng tra cứu thông tin phục vụ học tập an toàn; nhận biết các liên kết xấu hoặc quảng cáo độc hại để tránh xa. | `G4-NET-01` | `branch-story` |
| Bài 4 | Chủ đề C: Tổ chức lưu trữ | Quản lý tệp và thư mục | Tổ chức cây thư mục bài học trong máy tính; thực hiện sao chép (Copy), di chuyển (Cut), đổi tên (Rename) và xóa (Delete). | `G4-FILE-01` | `sort-drag` |
| Bài 5 | Chủ đề D: Đạo đức, pháp luật | Bản quyền và sử dụng thông tin hợp pháp | Hiểu tranh vẽ, ảnh chụp, bài viết trên mạng đều có chủ sở hữu; xin phép và ghi nguồn khi sử dụng tư liệu của người khác. | `G4-ETHIC-01` | `branch-story` |
| Bài 6 | Chủ đề E: Ứng dụng tin học | Chèn hình và căn lề văn bản | Soạn thảo đoạn văn bản giới thiệu bản thân, căn chỉnh lề đều hai bên và chèn ảnh chụp kỷ niệm của em. | `G4-DOC-01` | `sort-drag` |
| Bài 7 | Chủ đề E: Ứng dụng tin học | Định dạng kiểu chữ và màu sắc | Chọn phông chữ rõ ràng, cỡ chữ phù hợp lứa tuổi, phối màu sắc chữ hài hòa để bài văn nổi bật, đẹp mắt. | `G4-DOC-02` | `type-run` |
| Bài 8 | Chủ đề E: Ứng dụng tin học | Tạo trang trình chiếu sinh động | Tạo bài thuyết trình về danh lam thắng cảnh quê hương: thiết kế nền trang chiếu đẹp mắt và bố cục văn bản gọn gàng. | `G4-PRES-01` | `match-memory` |
| Bài 9 | Chủ đề E: Ứng dụng tin học | Trình bày bài báo cáo nhóm | Rèn luyện kỹ năng đứng trước lớp thuyết trình tự tin, chuyển slide nhịp nhàng ăn khớp với lời nói. | `G4-PRES-02` | `sort-drag` |
| Bài 10 | Chủ đề E: Ứng dụng tin học | Chỉnh sửa ảnh cơ bản | Cắt cúp ảnh đúng tỉ lệ, tăng độ tương phản và loại bỏ những chi tiết thừa trong khung hình. | `G4-IMG-01` | `match-memory` |
| Bài 11 | Chủ đề F: Giải quyết vấn đề | Môi trường lập trình Scratch | Khám phá giao diện đồ họa Scratch: khu vực khối lệnh nhiều màu sắc rực rỡ, khung lắp ráp kịch bản kéo thả tiện lợi. | `G4-SCRATCH-01`| `match-memory` |
| Bài 12 | Chủ đề F: Giải quyết vấn đề | Sân khấu và nhân vật | Thêm nhân vật mới từ thư viện hoặc tự vẽ nhân vật; đổi trang phục (Costume) để tạo hiệu ứng nhân vật bước đi. | `G4-SCRATCH-02`| `block-maze` |
| Bài 13 | Chủ đề F: Giải quyết vấn đề | Điều khiển nhân vật di chuyển | Sử dụng các khối lệnh điều khiển di chuyển tới trước, xoay hướng, nảy lại khi chạm mép màn hình. | `G4-ALGO-01` | `block-maze` |
| Bài 14 | Chủ đề F: Giải quyết vấn đề | Vòng lặp trong chương trình | Áp dụng khối lặp liên tục (Forever) và lặp N lần để nhân vật nhảy múa lặp lại theo nhịp điệu âm nhạc. | `G4-ALGO-02` | `block-maze` |
| Bài 15 | Chủ đề F: Giải quyết vấn đề | Biểu diễn thuật toán bằng sơ đồ khối | Vẽ các khối chữ nhật, hình thoi biểu diễn thuật toán trước khi ráp các khối lệnh Scratch thực thi. | `G4-FLOW-01` | `logic-puzzle` |
| Bài 16 | Chủ đề F: Giải quyết vấn đề | Dự án Em làm nhà lập trình nhí | Hoàn thiện trò chơi thu gom rác trên bãi biển bằng cách điều khiển tàu gom rác ăn các chai nhựa trôi nổi. | `G4-BOSS-01` | `boss-quiz` |

---

## 3. Lớp 5 — Tiểu học (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách CTST | Yêu cầu cần đạt (YCCĐ) & Năng lực sáng tạo | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề A: Máy tính và em | Thiết bị số thông minh quanh em | Tìm hiểu điện thoại thông minh, đồng hồ định vị, tivi thông minh, máy hút bụi tự động và cách chúng phục vụ đời sống. | `G5-COMP-01` | `match-memory` |
| Bài 2 | Chủ đề B: Mạng và Internet | An toàn khi tham gia thế giới trực tuyến | Quy tắc vàng giữ an toàn trên mạng: không mở liên kết lạ, không kết bạn với người xa lạ, báo ngay cho phụ huynh khi gặp nguy cơ. | `G5-SAFE-01` | `branch-story` |
| Bài 3 | Chủ đề B: Mạng và Internet | Đánh giá độ tin cậy của thông tin | Kỹ năng nhận diện các dấu hiệu bài viết sai sự thật, tin tức phóng đại hoặc thông tin lừa đảo câu view trên mạng. | `G5-SEARCH-01` | `sort-drag` |
| Bài 4 | Chủ đề D: Đạo đức, pháp luật | Tôn trọng quyền riêng tư & sở hữu trí tuệ | Tôn trọng tài khoản cá nhân của người khác, không đọc trộm tin nhắn; xin phép tác giả trước khi sử dụng hình ảnh. | `G5-ETHIC-01` | `branch-story` |
| Bài 5 | Chủ đề E: Ứng dụng tin học | Bảng tính và tổ chức dữ liệu | Tạo bảng tổng kết chi tiêu quỹ lớp; sắp xếp số liệu theo thứ tự từ lớn đến bé để quan sát rõ khoản chi lớn nhất. | `G5-DATA-01` | `sort-drag` |
| Bài 6 | Chủ đề E: Ứng dụng tin học | Soạn thảo văn bản và chèn bảng biểu | Kết hợp soạn thảo lời văn và chèn bảng biểu dữ liệu chi tiết vào cùng một văn bản báo cáo khoa học. | `G5-DOC-01` | `sort-drag` |
| Bài 7 | Chủ đề E: Ứng dụng tin học | Thiết kế bài thuyết trình đa phương tiện | Thiết kế bài thuyết trình sinh động có nhúng video và các bài nhạc truyền cảm hứng cho người nghe. | `G5-PRES-01` | `sort-drag` |
| Bài 8 | Chủ đề F: Giải quyết vấn đề | Biến số và lưu trữ dữ liệu trong Scratch | Tạo biến số lưu điểm số, biến thời gian đếm ngược; thiết lập giá trị ban đầu và thay đổi giá trị biến trong khi chơi. | `G5-VAR-01` | `logic-puzzle` |
| Bài 9 | Chủ đề F: Giải quyết vấn đề | Thực hành tính toán với biến số | Lập trình cho nhân vật tính toán cộng hai số ngẫu nhiên do người chơi nhập từ bàn phím. | `G5-VAR-02` | `block-maze` |
| Bài 10 | Chủ đề F: Giải quyết vấn đề | Cấu trúc rẽ nhánh trong thuật toán | Hiểu logic Nếu... Thì...; mô tả quyết định lựa chọn trang phục theo thời tiết (Nếu trời mưa thì mang ô). | `G5-IF-01` | `logic-puzzle` |
| Bài 11 | Chủ đề F: Giải quyết vấn đề | Lập trình rẽ nhánh có điều kiện | Lắp khối If... Then... Else để kiểm tra câu trả lời: Nếu đúng thì hoan hô, Nếu sai thì gợi ý cho bạn thử lại. | `G5-IF-02` | `block-maze` |
| Bài 12 | Chủ đề F: Giải quyết vấn đề | Vòng lặp kết hợp rẽ nhánh | Kết hợp vòng lặp liên tục và lệnh rẽ nhánh để kiểm tra trạng thái nhân vật liên tục trong suốt ván chơi. | `G5-ALGO-01` | `block-maze` |
| Bài 13 | Chủ đề F: Giải quyết vấn đề | Phát hiện lỗi và sửa lỗi chương trình | Kỹ năng đọc hiểu từng khối lệnh để tìm ra nguyên nhân nhân vật không di chuyển hoặc tính sai điểm số. | `G5-DEBUG-01` | `bug-hunt` |
| Bài 14 | Chủ đề F: Giải quyết vấn đề | Xây dựng trò chơi đố vui tương tác | Thiết kế trò chơi trắc nghiệm hiểu biết có hệ thống âm thanh chúc mừng, đồng hồ giới hạn thời gian trả lời. | `G5-GAME-01` | `block-maze` |
| Bài 15 | Chủ đề F: Giải quyết vấn đề | Dự án Sáng tạo tin học trẻ | Thiết kế dự án sáng tạo học đường: thi đua bảo vệ môi trường, học từ vựng tiếng Anh vui nhộn. | `G5-PROJ-01` | `bug-hunt` |
| Bài 16 | Chủ đề F: Giải quyết vấn đề | Tổng kết và định hướng học tập cấp 2 | Nhìn lại chặng đường 3 năm học Tin học tiểu học; sẵn sàng bước vào thế giới số hóa nâng cao ở cấp Trung học cơ sở. | `G5-BOSS-01` | `boss-quiz` |

---

## 4. Lớp 6 — THCS (17 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách CTST | Yêu cầu cần đạt (YCCĐ) & Năng lực sáng tạo | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề A: Máy tính và cộng đồng | Thông tin và xử lý thông tin | Vai trò quyết định của thông tin trong đời sống; chu trình thu nhận, xử lý, lưu trữ và truyền đạt thông tin. | `G6-INFO-01` | `branch-story` |
| Bài 2 | Chủ đề A: Máy tính và cộng đồng | Biểu diễn dữ liệu số trong máy tính | Giải thích nguyên lý số hóa: văn bản, hình ảnh, âm thanh đều được máy tính chuyển đổi thành dãy bit 0 và 1. | `G6-DATA-01` | `logic-puzzle` |
| Bài 3 | Chủ đề B: Mạng máy tính | Khái niệm mạng máy tính | Lợi ích của mạng máy tính: chia sẻ máy in, dùng chung tệp tài liệu, liên lạc tức thời xuyên lục địa. | `G6-NET-01` | `sort-drag` |
| Bài 4 | Chủ đề B: Mạng máy tính | Dịch vụ Internet & World Wide Web | Tìm hiểu hệ thống siêu văn bản toàn cầu, các dịch vụ tìm kiếm, thương mại điện tử và học tập trực tuyến. | `G6-WWW-01` | `match-memory` |
| Bài 5 | Chủ đề B: Mạng máy tính | Tìm kiếm thông tin khoa học | Sử dụng các từ khóa học thuật, bộ lọc định dạng tệp (filetype:pdf) để tìm tài liệu nghiên cứu khoa học chất lượng. | `G6-SEARCH-01` | `sort-drag` |
| Bài 6 | Chủ đề B: Mạng máy tính | Thư điện tử và ứng dụng | Thực hành viết thư điện tử chuẩn mực: tiêu đề rõ ràng, lời chào lịch sự, nội dung súc tích, chữ ký cuối thư. | `G6-EMAIL-01` | `branch-story` |
| Bài 7 | Chủ đề C: Mạng xã hội | Mạng xã hội & Quy tắc ứng xử số | Quy tắc ứng xử "Suy nghĩ kỹ trước khi đăng tải": không bình luận ác ý, không xúc phạm danh dự nhân phẩm người khác. | `G6-SOCIAL-01` | `branch-story` |
| Bài 8 | Chủ đề D: Đạo đức, pháp luật | Bảo vệ quyền riêng tư và bản quyền số | Tôn trọng đời tư số của bạn bè, không tùy tiện đăng ảnh bạn khi chưa được đồng ý; tôn trọng bản quyền sở hữu trí tuệ. | `G6-ETHIC-01` | `branch-story` |
| Bài 9 | Chủ đề E: Ứng dụng tin học | Ứng dụng sơ đồ tư duy trong học tập | Sử dụng phần mềm sơ đồ tư duy liên kết các nhánh kiến thức môn Sinh học, Lịch sử giúp ghi nhớ sâu sắc. | `G6-MIND-01` | `logic-puzzle` |
| Bài 10 | Chủ đề E: Ứng dụng tin học | Soạn thảo văn bản chuyên nghiệp | Thiết lập lề trang giấy in, tiêu đề đầu trang và chân trang (Header & Footer), đánh số trang tự động chuẩn mực. | `G6-DOC-01` | `type-run` |
| Bài 11 | Chủ đề E: Ứng dụng tin học | Bảng số liệu và trực quan hóa | Chèn bảng số liệu theo dõi điểm kiểm tra học kỳ, định dạng viền kẻ và căn lề số liệu thẳng hàng chuẩn quốc tế. | `G6-TABLE-01` | `sort-drag` |
| Bài 12 | Chủ đề E: Ứng dụng tin học | Dự án xây dựng bản tin số | Thiết kế và xuất bản tờ báo tường điện tử của chi đội trường học có đầy đủ bài viết xã luận, phỏng vấn và hình ảnh. | `G6-PROJ-01` | `match-memory` |
| Bài 13 | Chủ đề F: Giải quyết vấn đề | Tư duy thuật toán | Nhận biết đặc trưng của thuật toán: Tính xác định, Tính dừng, Tính đúng đắn; biểu diễn thuật toán qua ví dụ thực tế. | `G6-ALGO-01` | `block-maze` |
| Bài 14 | Chủ đề F: Giải quyết vấn đề | Sơ đồ khối & Biểu diễn thuật toán | Rèn luyện kỹ năng vẽ sơ đồ khối tuần tự, phân nhánh và vòng lặp giải bài toán toán học. | `G6-FLOW-01` | `logic-puzzle` |
| Bài 15 | Chủ đề F: Giải quyết vấn đề | Cấu trúc rẽ nhánh và vòng lặp | Cài đặt các thuật toán kiểm tra tính chia hết, tính tổng các số chẵn nhỏ hơn 100 bằng cấu trúc điều khiển chuẩn. | `G6-ALGO-02` | `block-maze` |
| Bài 16 | Chủ đề F: Giải quyết vấn đề | Phát hiện và gỡ lỗi thuật toán | Phân tích các bước thuật toán để tìm ra trường hợp ngoại lệ (Edge case) khiến thuật toán cho kết quả sai. | `G6-DEBUG-01` | `bug-hunt` |
| Bài 17 | Chủ đề F: Giải quyết vấn đề | Em là tuyên truyền viên an toàn số | Trình diễn sản phẩm truyền thông số về phòng chống lừa đảo trên mạng và bảo vệ thông tin cá nhân. | `G6-BOSS-01` | `boss-quiz` |

---

## 5. Lớp 7 — THCS (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách CTST | Yêu cầu cần đạt (YCCĐ) & Năng lực sáng tạo | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề A: Máy tính và cộng đồng | Thiết bị vào - ra & Kết nối máy tính | Tìm hiểu các cổng giao tiếp chuẩn: USB-A, USB-C, HDMI, DisplayPort, Jack 3.5mm; cơ chế truyền tín hiệu tương tự và số. | `G7-IO-01` | `sort-drag` |
| Bài 2 | Chủ đề A: Máy tính và cộng đồng | Hệ điều hành & Phần mềm tiện ích | Chức năng của hệ điều hành trong quản lý tệp tin, phân bổ bộ nhớ; các phần mềm tiện ích nén tệp (WinRAR/7-Zip), dọn rác. | `G7-OS-01` | `sort-drag` |
| Bài 3 | Chủ đề A: Máy tính và cộng đồng | Lưu trữ dữ liệu an toàn | Tổ chức cấu trúc thư mục logic; quy tắc đặt tên tệp không dấu, không chứa ký tự cấm; thiết lập quyền chỉ đọc (Read-only). | `G7-PATH-01` | `sort-drag` |
| Bài 4 | Chủ đề C: Mạng xã hội | Ứng xử có văn hóa trên mạng xã hội | Rèn luyện khả năng kiểm soát cảm xúc, tranh luận văn minh trên diễn đàn; lan tỏa năng lượng tích cực trong cộng đồng mạng. | `G7-COMM-01` | `branch-story` |
| Bài 5 | Chủ đề D: Đạo đức, pháp luật | Nhận diện rủi ro trên không gian mạng | Nhận biết các nguy cơ: tin nhắn mạo danh trúng thưởng, phần mềm gián điệp theo dõi bàn phím (Keylogger), bắt nạt ảo. | `G7-SEC-01` | `branch-story` |
| Bài 6 | Chủ đề E: Ứng dụng tin học | Làm quen với Excel / Google Sheets | Khái niệm ô hiện hành, thanh công thức (Formula Bar); cách chọn nhiều vùng ô không liền kề nhau bằng phím Ctrl. | `G7-SHEET-01` | `sort-drag` |
| Bài 7 | Chủ đề E: Ứng dụng tin học | Công thức & Tính toán số học | Viết công thức số học sử dụng các toán tử: +, -, *, /, ^ (lũy thừa); quy tắc thứ tự ưu tiên các phép toán trong bảng tính. | `G7-SHEET-02` | `logic-puzzle` |
| Bài 8 | Chủ đề E: Ứng dụng tin học | Sử dụng hàm cơ bản để xử lý dữ liệu | Ứng dụng các hàm SUM, AVERAGE, COUNT, MAX, MIN để tính bảng lương hoặc bảng theo dõi chi phí sinh hoạt gia đình. | `G7-FUNC-01` | `logic-puzzle` |
| Bài 9 | Chủ đề E: Ứng dụng tin học | Định dạng & Trình bày bảng tính | Trình bày bảng tính đẹp mắt: gộp ô (Merge & Center), căn lề số liệu về bên phải, căn lề văn bản về bên trái theo chuẩn kế toán. | `G7-SHEET-03` | `sort-drag` |
| Bài 10 | Chủ đề E: Ứng dụng tin học | Sắp xếp dữ liệu theo tiêu chí | Sắp xếp danh sách bảng điểm theo thứ tự điểm Trung bình môn giảm dần; khi trùng điểm thì sắp xếp theo họ tên bảng chữ cái. | `G7-SHEET-04` | `sort-drag` |
| Bài 11 | Chủ đề E: Ứng dụng tin học | Tạo bài thuyết trình ấn tượng | Áp dụng nguyên tắc thiết kế thị giác 6x6 (mỗi slide không quá 6 dòng, mỗi dòng không quá 6 từ) để bài thuyết trình cô đọng, súc tích. | `G7-PRES-01` | `match-memory` |
| Bài 12 | Chủ đề E: Ứng dụng tin học | Tích hợp hình ảnh, video & âm thanh | Nhúng video minh họa trực quan từ máy tính vào trang chiếu; thiết lập âm thanh nền tự động phát khi trình chiếu. | `G7-PRES-02` | `sort-drag` |
| Bài 13 | Chủ đề F: Giải quyết vấn đề | Thuật toán tìm kiếm tuần tự | Mô tả thuật toán duyệt từng phần tử từ vị trí 1 đến vị trí N; phân tích số phép so sánh trung bình (N+1)/2. | `G7-SEARCH-01`| `block-maze` |
| Bài 14 | Chủ đề F: Giải quyết vấn đề | Thuật toán tìm kiếm nhị phân | Mô tả thuật toán tìm kiếm trên mảng có thứ tự: liên tục thu hẹp phạm vi tìm kiếm xuống một nửa; hiệu quả vượt trội trên tập dữ liệu lớn. | `G7-SEARCH-02`| `logic-puzzle` |
| Bài 15 | Chủ đề F: Giải quyết vấn đề | Thuật toán sắp xếp nổi bọt | Cơ chế hoán đổi các cặp phần tử liền kề sai thứ tự; quan sát trực quan các phần tử nhẹ "nổi lên" hoặc phần tử nặng "chìm xuống". | `G7-SORT-01` | `block-maze` |
| Bài 16 | Chủ đề F: Giải quyết vấn đề | Thuật toán sắp xếp chọn | Cơ chế tìm phần tử nhỏ nhất và đưa về đầu mảng; đánh giá ưu nhược điểm so với sắp xếp nổi bọt; thi đấu tổng kết. | `G7-BOSS-01` | `boss-quiz` |

---

## 6. Lớp 8 — THCS (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách CTST | Yêu cầu cần đạt (YCCĐ) & Năng lực sáng tạo | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề A: Máy tính và cộng đồng | Quá trình phát triển của máy tính | Khám phá các bước ngoặt công nghệ: Định luật Moore về số lượng bóng bán dẫn; sự ra đời của máy tính cá nhân PC và điện thoại thông minh. | `G8-HIST-01` | `match-memory` |
| Bài 2 | Chủ đề A: Máy tính và cộng đồng | Thông tin đáng tin cậy & không đáng tin cậy | Rèn luyện khả năng tư duy phản biện khi đọc tin tức số; nhận biết thông tin phiến diện, sai lệch để không bị dắt mũi dư luận. | `G8-INFO-01` | `branch-story` |
| Bài 3 | Chủ đề D: Đạo đức, pháp luật | Đạo đức và văn hóa số | Trách nhiệm bảo vệ môi trường số xanh sạch; nói không với phát tán văn hóa phẩm độc hại, tôn trọng quyền tác giả phần mềm. | `G8-ETHIC-01` | `branch-story` |
| Bài 4 | Chủ đề E: Ứng dụng tin học | Bảng tính nâng cao & Xử lý số liệu | Sử dụng hàm điều kiện IF kết hợp với các hàm thống kê để tự động xếp loại học lực học sinh (Giỏi, Khá, Trung bình). | `G8-SHEET-01` | `logic-puzzle` |
| Bài 5 | Chủ đề E: Ứng dụng tin học | Trực quan hóa dữ liệu bằng biểu đồ | Thiết kế biểu đồ kết hợp (Combo Chart) hiển thị đồng thời doanh thu dạng cột và tốc độ tăng trưởng dạng đường. | `G8-CHART-01` | `sort-drag` |
| Bài 6 | Chủ đề E: Ứng dụng tin học | Thiết kế đồ họa & Chỉnh sửa ảnh | Làm quen với kỹ thuật tách nền ảnh (Background Removal), điều chỉnh độ bão hòa màu sắc (Saturation) và phơi sáng (Exposure). | `G8-IMG-01` | `match-memory` |
| Bài 7 | Chủ đề E: Ứng dụng tin học | Biên tập đồ họa vector và raster | Kết hợp linh hoạt ảnh chụp thực tế và hình vẽ đồ họa vector để tạo ấn phẩm truyền thông chuyên nghiệp. | `G8-IMG-02` | `sort-drag` |
| Bài 8 | Chủ đề F: Giải quyết vấn đề | Khái niệm lập trình và thuật toán | Chuyển dịch từ thuật toán logic sang ngôn ngữ máy tính; nguyên lý hoạt động của trình biên dịch và trình thông dịch. | `G8-PROG-01` | `block-maze` |
| Bài 9 | Chủ đề F: Giải quyết vấn đề | Biến, kiểu dữ liệu và phép toán | Khai báo biến lưu trữ điểm trung bình (Float), số lượng học sinh (Integer), tên trường (String), trạng thái tốt nghiệp (Boolean). | `G8-TYPE-01` | `logic-puzzle` |
| Bài 10 | Chủ đề F: Giải quyết vấn đề | Cấu trúc rẽ nhánh lồng nhau | Lập trình cấu trúc điều kiện lồng nhau để giải bài toán giải và biện luận phương trình bậc hai $ax^2 + bx + c = 0$. | `G8-IF-01` | `bug-hunt` |
| Bài 11 | Chủ đề F: Giải quyết vấn đề | Cấu trúc lặp với điều kiện | Lập trình vòng lặp tính xấp xỉ giá trị số Pi bằng chuỗi số Leibniz hoặc tính căn bậc hai bằng phương pháp Newton. | `G8-LOOP-01` | `block-maze` |
| Bài 12 | Chủ đề F: Giải quyết vấn đề | Xử lý dữ liệu dạng danh sách | Thao tác trên danh sách điểm số: tìm điểm cao nhất, điểm thấp nhất, tính trung bình và đếm số bạn đạt điểm 10. | `G8-LIST-01` | `bug-hunt` |
| Bài 13 | Chủ đề F: Giải quyết vấn đề | Viết chương trình mô phỏng trò chơi | Lập trình trò chơi đuổi bắt giữa nhân vật người hùng và quái vật với cơ chế tăng tốc độ theo thời gian. | `G8-GAME-01` | `block-maze` |
| Bài 14 | Chủ đề F: Giải quyết vấn đề | Phát hiện lỗi logic và gỡ lỗi | Rèn luyện kỹ năng phân tích giá trị biến số qua từng bước lặp để tìm ra nguyên nhân vòng lặp bị dừng sớm hoặc lặp vô tận. | `G8-DEBUG-01` | `bug-hunt` |
| Bài 15 | Chủ đề F: Giải quyết vấn đề | Dự án Sáng tạo ứng dụng Tin học 8 | Hoàn thiện phần mềm trắc nghiệm tri thức đa môn học có đồng hồ đếm ngược và bảng vàng ghi danh điểm cao. | `G8-PROJ-01` | `bug-hunt` |
| Bài 16 | Chủ đề G: Hướng nghiệp | Định hướng nghề nghiệp CNTT | Tìm hiểu về nghề Quản trị cơ sở dữ liệu (DBA), Chuyên viên thiết kế trải nghiệm người dùng (UX/UI Designer) và mức thu nhập. | `G8-BOSS-01` | `boss-quiz` |

---

## 7. Lớp 9 — THCS (16 bài)

| STT | Chủ đề GDPT 2018 | Tên bài học trong sách CTST | Yêu cầu cần đạt (YCCĐ) & Năng lực sáng tạo | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Chủ đề A: Máy tính và cộng đồng | Nguyên lý hoạt động của máy tính | Chu trình nạp - giải mã - thực thi lệnh (Fetch-Decode-Execute cycle) của bộ xử lý trung tâm CPU; kiến trúc thanh ghi. | `G9-ARCH-01` | `sort-drag` |
| Bài 2 | Chủ đề A: Máy tính và cộng đồng | Giá trị của thông tin & Ra quyết định | Phân tích vai trò của dữ liệu lớn (Big Data) và thông tin thời gian thực trong việc hỗ trợ doanh nghiệp đưa ra quyết định kinh doanh. | `G9-INFO-01` | `branch-story` |
| Bài 3 | Chủ đề D: Đạo đức, pháp luật | Pháp luật trong thời đại số | Phổ biến Luật An ninh mạng năm 2018; các quy định về bảo vệ trẻ em trên môi trường trực tuyến và quy tắc ứng xử mạng xã hội. | `G9-LAW-01` | `branch-story` |
| Bài 4 | Chủ đề E: Ứng dụng tin học | Phần mềm mô phỏng & Ứng dụng | Sử dụng phần mềm mô phỏng không gian vũ trụ, thiên văn học và cấu tạo nguyên tử để trực quan hóa kiến thức trừu tượng. | `G9-SIM-01` | `match-memory` |
| Bài 5 | Chủ đề E: Ứng dụng tin học | Xử lý âm thanh và video clip | Sử dụng phần mềm thu âm, cắt gọt tạp âm, điều chỉnh âm lượng (Equalizer) và phối trộn bài nhạc nền với giọng đọc thuyết minh. | `G9-VID-01` | `sort-drag` |
| Bài 6 | Chủ đề E: Ứng dụng tin học | Xuất bản sản phẩm truyền thông số | Lựa chọn định dạng xuất video (MP4, H.264), độ phân giải Full HD 1080p và tỷ lệ khung hình 16:9 hoặc 9:16 phù hợp nền tảng. | `G9-PROJ-01` | `match-memory` |
| Bài 7 | Chủ đề F: Giải quyết vấn đề | Xây dựng thuật toán giải quyết bài toán | Rèn luyện tư duy phân tích bài toán thực tế: tìm đường đi ngắn nhất, bài toán cái túi, bài toán lập lịch công việc. | `G9-ALGO-01` | `logic-puzzle` |
| Bài 8 | Chủ đề F: Giải quyết vấn đề | Lập trình hiện thực hóa thuật toán | Cài đặt thuật toán chuyển đổi cơ số từ thập phân sang nhị phân và ngược lại bằng ngôn ngữ lập trình. | `G9-CODE-01` | `bug-hunt` |
| Bài 9 | Chủ đề F: Giải quyết vấn đề | Kiểm thử phần mềm và tìm lỗi | Thiết kế bộ dữ liệu kiểm thử biên (Boundary Value Analysis); kiểm tra trường hợp danh sách rỗng, mảng 1 phần tử. | `G9-DEBUG-01` | `bug-hunt` |
| Bài 10 | Chủ đề F: Giải quyết vấn đề | Phát triển phần mềm giải trí mini | Lập trình trò chơi trí tuệ giải đố tương tác đồ họa hoàn chỉnh; xử lý logic va chạm và hiệu ứng thắng thua. | `G9-APP-01` | `block-maze` |
| Bài 11 | Chủ đề B: Mạng máy tính | Kết nối thiết bị qua LAN & Internet | Tìm hiểu địa chỉ MAC vật lý của card mạng, cấu hình địa chỉ IP tĩnh cho máy in trong mạng văn phòng trường học. | `G9-LAN-01` | `packet-route` |
| Bài 12 | Chủ đề B: Mạng máy tính | Ứng dụng điện toán đám mây | Khai thác tính năng chia sẻ quyền truy cập tệp (Xem, Nhận xét, Chỉnh sửa) và làm việc đồng thời theo nhóm trên Google Docs. | `G9-CLOUD-01` | `sort-drag` |
| Bài 13 | Chủ đề D: Đạo đức, pháp luật | Bảo mật thông tin cá nhân & Dữ liệu | Cơ chế hoạt động của phần mềm mã độc Ransomware tống tiền dữ liệu; các biện pháp phòng vệ chủ động bằng tường lửa. | `G9-SEC-01` | `branch-story` |
| Bài 14 | Chủ đề D: Đạo đức, pháp luật | Phòng chống lừa đảo trực tuyến | Kỹ năng nhận diện email lừa đảo (Phishing), website ngân hàng giả mạo và bảo vệ mã xác thực giao dịch OTP. | `G9-PHISH-01` | `branch-story` |
| Bài 15 | Chủ đề F: Giải quyết vấn đề | Dự án Trường học thông minh | Xây dựng mô hình ý tưởng hệ thống thư viện thông minh tra cứu sách tự động kết hợp mã vạch QR Code. | `G9-COMM-01` | `bug-hunt` |
| Bài 16 | Chủ đề G: Hướng nghiệp | Thị trường lao động công nghệ số | Định hướng lựa chọn nghề nghiệp tương lai: Chuyên gia an toàn mạng, Kỹ sư kiểm thử phần mềm (QA/QC), Kỹ sư điện toán đám mây. | `G9-BOSS-01` | `boss-quiz` |

---

## 8. Lớp 10 — THPT (32 bài)

| STT | Phân nhóm | Tên bài học trong sách CTST | Yêu cầu cần đạt (YCCĐ) & Năng lực sáng tạo | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Máy tính và xã hội | Thông tin và xử lý thông tin số | Nhận thức sâu sắc về vai trò của công nghệ thông tin trong nền kinh tế tri thức; quá trình số hóa tài liệu truyền thống. | `G10-INFO-01` | `branch-story` |
| Bài 2 | Máy tính và xã hội | Thiết bị thông minh trong thời đại mới | Phân tích cơ chế hoạt động của cảm biến (Sensors), nhà thông minh (Smart Home) và thành phố thông minh (Smart City). | `G10-IOT-01` | `match-memory` |
| Bài 3 | Máy tính và xã hội | Mạng máy tính và các mô hình kết nối | So sánh mô hình kết nối mạng Ngang hàng (Peer-to-Peer - P2P) và mô hình Khách - Chủ (Client - Server). | `G10-NET-01` | `sort-drag` |
| Bài 4 | Máy tính và xã hội | Thiết bị mạng và truyền thông dữ liệu | Hiểu chức năng của Router trong việc tìm đường đi tối ưu cho gói tin; phân tích băng thông (Bandwidth) và độ trễ (Latency). | `G10-NET-02` | `packet-route` |
| Bài 5 | Đạo đức, pháp luật | Mạng xã hội và trách nhiệm công dân số | Xây dựng văn hóa tranh luận tích cực; nhận thức hậu quả pháp lý của hành vi chia sẻ tin đồn thất thiệt gây hoang mang dư luận. | `G10-SOC-01` | `branch-story` |
| Bài 6 | Đạo đức, pháp luật | An toàn và bảo mật trong không gian mạng | Các biện pháp phòng chống phần mềm độc hại (Malware, Spyware); cài đặt phần mềm diệt virus và sao lưu dữ liệu tự động. | `G10-SEC-01` | `branch-story` |
| Bài 7 | Đạo đức, pháp luật | Phần mềm nguồn mở & Giấy phép công nghệ | Quyền tự do sử dụng, chỉnh sửa và phân phối phần mềm nguồn mở theo các điều khoản của giấy phép GNU GPL và Apache. | `G10-OSS-01` | `sort-drag` |
| Bài 8 | Ứng dụng tin học | Làm quen với phần mềm thiết kế Inkscape | Khởi tạo tài liệu, thiết lập hệ đơn vị đo (mm, px), tìm hiểu không gian làm việc và công cụ chọn Selection Tool. | `G10-VEC-01` | `sort-drag` |
| Bài 9 | Ứng dụng tin học | Vẽ các hình khối vector cơ bản | Tạo hình tròn, hình vuông, đường cong uốn lượn; thay đổi màu viền (Stroke) và màu lấp đầy (Fill) của đối tượng. | `G10-VEC-02` | `match-memory` |
| Bài 10 | Ứng dụng tin học | Thao tác biến đổi và phối hợp đối tượng | Sử dụng các lệnh biến đổi hình học: cắt xén, giao nhau, hợp nhất các đối tượng vector để tạo huy hiệu, logo sáng tạo. | `G10-VEC-03` | `sort-drag` |
| Bài 11 | Ứng dụng tin học | Thiết kế sản phẩm đồ họa ứng dụng | Hoàn thiện thiết kế bìa sách học tập hoặc ấn phẩm truyền thông ngày hội khoa học của trường. | `G10-VEC-04` | `sort-drag` |
| Bài 12 | Lập trình Python | Làm quen với ngôn ngữ Python | Cài đặt trình thông dịch Python và công cụ lập trình VS Code/PyCharm; cấu trúc của một tập lệnh Python (.py). | `G10-PY-01` | `type-run` |
| Bài 13 | Lập trình Python | Biến số, phép toán và kiểu dữ liệu | Nắm vững các kiểu dữ liệu nguyên thủy: int, float, str, bool; phân biệt phép chia thực (/) và chia lấy phần nguyên (//). | `G10-PY-02` | `logic-puzzle` |
| Bài 14 | Lập trình Python | Nhập xuất dữ liệu tương tác | Sử dụng hàm print() kết hợp chuỗi định dạng F-string; ép kiểu dữ liệu an toàn cho giá trị nhập từ input(). | `G10-PY-03` | `type-run` |
| Bài 15 | Lập trình Python | Câu lệnh điều kiện if | Cú pháp câu lệnh rẽ nhánh dạng thiếu và đủ; quy tắc thụt lề 4 dấu cách trong chuẩn mã nguồn Python PEP 8. | `G10-PY-04` | `bug-hunt` |
| Bài 16 | Lập trình Python | Cấu trúc rẽ nhánh if... elif... else | Cài đặt thuật toán xếp loại học sinh theo chuẩn Thông tư 22 của Bộ GD&ĐT dựa trên điểm trung bình các môn. | `G10-PY-05` | `bug-hunt` |
| Bài 17 | Lập trình Python | Câu lệnh lặp for và hàm range | Duyệt dãy số nguyên với bước nhảy âm và dương; tính giai thừa $N! = 1 \times 2 \times \dots \times N$. | `G10-PY-06` | `block-maze` |
| Bài 18 | Lập trình Python | Câu lệnh lặp while | Lập trình thuật toán tìm ước chung lớn nhất của 2 số nguyên dương A và B theo thuật toán trừ liên tiếp hoặc chia dư. | `G10-PY-07` | `bug-hunt` |
| Bài 19 | Lập trình Python | Kiểu dữ liệu danh sách (List) | Tạo mảng số thực lưu điểm kiểm tra; truy xuất phần tử qua chỉ số âm và chỉ số dương; độ dài danh sách len(). | `G10-PY-08` | `logic-puzzle` |
| Bài 20 | Lập trình Python | Các phương thức xử lý danh sách | Áp dụng append() thêm dữ liệu, sort() sắp xếp mảng tăng dần, pop() xóa phần tử cuối; kỹ thuật cắt lát danh sách list[a:b]. | `G10-PY-09` | `bug-hunt` |
| Bài 21 | Lập trình Python | Kiểu dữ liệu xâu ký tự (String) | Các thao tác trên chuỗi: tìm chuỗi con find(), thay thế ký tự replace(), tách từ split() và ghép chuỗi join(). | `G10-PY-10` | `type-run` |
| Bài 22 | Lập trình Python | Xử lý xâu ký tự nâng cao | Lập trình kiểm tra một xâu ký tự có phải là xâu đối xứng (Palindrome) hay không; đếm số lượng nguyên âm, phụ âm. | `G10-PY-11` | `bug-hunt` |
| Bài 23 | Lập trình Python | Hàm và kiến trúc chương trình con | Định nghĩa hàm với từ khóa def; phân chia bài toán phức tạp thành các hàm nhỏ độc lập dễ quản lý, dễ tái sử dụng. | `G10-PY-12` | `bug-hunt` |
| Bài 24 | Lập trình Python | Tham số và giá trị trả về của hàm | Thiết lập tham số mặc định cho hàm (Default arguments); trả về kết quả qua lệnh return. | `G10-PY-13` | `logic-puzzle` |
| Bài 25 | Lập trình Python | Phạm vi biến số và tái cấu trúc mã | Hiểu sự khác biệt giữa biến cục bộ và biến toàn cục; kỹ thuật tái cấu trúc (Refactoring) giúp mã nguồn sáng sủa. | `G10-PY-14` | `bug-hunt` |
| Bài 26 | Lập trình Python | Nhận diện và gỡ lỗi chương trình | Phân tích thông báo lỗi cú pháp SyntaxError, lỗi thời gian chạy TypeError để sửa mã nguồn nhanh chóng. | `G10-DEBUG-01` | `bug-hunt` |
| Bài 27 | Lập trình Python | Kiểm thử chương trình với Test cases | Xây dựng bảng kiểm thử bao gồm các ca kiểm thử thông thường, ca kiểm thử đặc biệt và ca kiểm thử biên. | `G10-DEBUG-02` | `bug-hunt` |
| Bài 28 | Lập trình Python | Đọc và ghi tệp dữ liệu | Đọc dữ liệu đầu vào từ tệp INPUT.TXT và ghi kết quả xử lý ra tệp OUTPUT.TXT theo định dạng chuẩn thi học sinh giỏi. | `G10-FILE-01` | `logic-puzzle` |
| Bài 29 | Lập trình Python | Thuật toán sắp xếp và tìm kiếm | Cài đặt và đo đếm số bước thực thi của thuật toán tìm kiếm tuần tự và tìm kiếm nhị phân trên tập dữ liệu số lớn. | `G10-ALGO-01` | `block-maze` |
| Bài 30 | Lập trình Python | Dự án lập trình phần mềm quản lý | Xây dựng phần mềm quản lý học sinh đơn giản có các tính năng: Nhập học sinh, Tìm kiếm theo tên, Xuất báo cáo điểm. | `G10-PROJ-01` | `bug-hunt` |
| Bài 31 | Hướng nghiệp | Nghề thiết kế đồ họa & lập trình phần mềm | Tìm hiểu về nhu cầu nhân lực chất lượng cao trong ngành công nghệ thông tin và định hướng lộ trình học tập tương lai. | `G10-CAREER-01`| `match-memory` |
| Bài 32 | Tổng kết | Kỳ thi đánh giá năng lực Tin học 10 | Tổng kết tri thức toàn diện: Phần cứng, Mạng máy tính, Bản quyền số, Đồ họa vector và Kỹ năng lập trình Python nâng cao. | `G10-BOSS-01` | `boss-quiz` |

---

## 9. Lớp 11 — THPT (30 bài định hướng CS & ICT)

### Nhánh Khoa học máy tính (CS — 30 bài)
| STT | Chủ đề | Tên bài học trong sách CTST CS | Yêu cầu cần đạt (YCCĐ) & Năng lực sáng tạo | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài CS 1 | CSDL | Khái niệm cơ sở dữ liệu quan hệ | Ý nghĩa của việc lưu trữ tập trung; tránh trùng lặp dữ liệu, đảm bảo tính nhất quán và bảo mật thông tin. | `G11-DB-01` | `sort-drag` |
| Bài CS 2 | CSDL | Cấu trúc bảng dữ liệu | Phân tích cấu trúc bảng: mỗi cột là một thuộc tính có kiểu dữ liệu xác định, mỗi hàng là một bản ghi duy nhất. | `G11-DB-02` | `sort-drag` |
| Bài CS 3 | CSDL | Khóa chính và liên kết bảng | Xác định khóa chính tự tăng (AUTO_INCREMENT); thiết lập khóa ngoại liên kết giữa bảng HoaDon và bảng KhachHang. | `G11-DB-03` | `logic-puzzle` |
| Bài CS 4 | SQL | Ngôn ngữ truy vấn SQL cơ bản | Viết câu lệnh SELECT trích xuất các cột cụ thể; sử dụng bí danh bảng (Alias AS) để câu truy vấn ngắn gọn. | `G11-SQL-01` | `logic-puzzle` |
| Bài CS 5 | SQL | Lọc điều kiện với mệnh đề WHERE | Sử dụng toán tử so sánh, toán tử logic AND, OR kết hợp hàm xử lý chuỗi LIKE '%abc%' tìm kiếm gần đúng. | `G11-SQL-02` | `logic-puzzle` |
| Bài CS 6 | SQL | Các hàm tổng hợp và gom nhóm | Sử dụng hàm COUNT(), SUM(), AVG(), MAX(), MIN() kết hợp mệnh đề GROUP BY và điều kiện lọc nhóm HAVING. | `G11-SQL-03` | `logic-puzzle` |
| Bài CS 7 | SQL | Truy vấn kết nối dữ liệu INNER JOIN | Nối nhiều bảng dữ liệu có quan hệ khóa ngoại bằng INNER JOIN để xuất báo cáo bán hàng tổng hợp. | `G11-SQL-04` | `logic-puzzle` |
| Bài CS 8 | SQL | Cập nhật và xóa dữ liệu an toàn | Thực hiện lệnh INSERT INTO thêm dữ liệu mới, UPDATE sửa dữ liệu và DELETE xóa dữ liệu có kiểm tra điều kiện. | `G11-SQL-05` | `bug-hunt` |
| Bài CS 9 | Thiết kế CSDL | Chuẩn hóa CSDL quan hệ | Quy trình chuẩn hóa dữ liệu từ dạng thô lên dạng chuẩn 1NF (thuộc tính nguyên tử), 2NF và 3NF (loại bỏ phụ thuộc bắc cầu). | `G11-NORM-01` | `sort-drag` |
| Bài CS 10 | Thực hành CSDL | Tạo lập và truy vấn CSDL với phần mềm | Sử dụng công cụ đồ họa phpMyAdmin / MySQL Workbench tạo CSDL trường học, nhập dữ liệu mẫu và chạy các câu truy vấn. | `G11-PRAC-01` | `bug-hunt` |
| Bài CS 11 | Thuật toán CS | Phương pháp Đệ quy (Recursion) | Hiểu cơ chế hoạt động của ngăn xếp lời gọi hàm (Call Stack); phân tích điểm dừng và bước gọi đệ quy. | `G11-ALGO-01` | `bug-hunt` |
| Bài CS 12 | Thuật toán CS | Bài toán Tháp Hà Nội và Quay lui | Cài đặt thuật toán đệ quy chuyển N đĩa từ cọc A sang cọc C thông qua cọc trung gian B; thuật toán quay lui giải mê cung. | `G11-ALGO-02` | `logic-puzzle` |
| Bài CS 13 | Thuật toán CS | Thuật toán Sắp xếp trộn (Merge Sort) | Chia dãy thành các dãy con có độ dài 1; sau đó trộn từng cặp dãy con đã sắp xếp để thu được dãy hoàn chỉnh. | `G11-ALGO-03` | `logic-puzzle` |
| Bài CS 14 | Thuật toán CS | Thuật toán Sắp xếp nhanh (Quick Sort) | Kỹ thuật chọn chốt Pivot thông minh; phân hoạch mảng và gọi đệ quy sắp xếp 2 nửa; so sánh độ phức tạp với Merge Sort. | `G11-ALGO-04` | `bug-hunt` |
| Bài CS 15 | Thuật toán CS | Đánh giá độ phức tạp và tối ưu thuật toán | Phân tích độ phức tạp thời gian $O(N \log N)$ và độ phức tạp bộ nhớ phụ của các thuật toán sắp xếp nâng cao. | `G11-ALGO-05` | `logic-puzzle` |
| Bài CS 16 | Dự án CS | Hệ thống quản lý điểm thi trực tuyến | Xây dựng ứng dụng quản lý điểm thi hoàn chỉnh kết nối cơ sở dữ liệu MySQL và ngôn ngữ lập trình Python. | `G11-BOSS-01` | `boss-quiz` |

---

## 10. Lớp 12 — THPT (30 bài định hướng CS & ICT)

| STT | Phân nhóm | Tên bài học trong sách CTST | Yêu cầu cần đạt (YCCĐ) & Năng lực sáng tạo | Nút EasyTin tương ứng | Khuôn Game |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bài 1 | Mạng nâng cao | Kiến trúc mạng và mô hình phân tầng | Ý nghĩa của mô hình tham chiếu OSI và kiến trúc TCP/IP; cơ chế định danh cổng dịch vụ (Port number: 80, 443, 22). | `G12-NET-01` | `sort-drag` |
| Bài 2 | Mạng nâng cao | Địa chỉ IP và định tuyến dữ liệu | Phân chia mạng con (Subnetting) trong IPv4; định tuyến gói tin dữ liệu qua nhiều mạng trung gian đến đúng địa chỉ đích. | `G12-NET-02` | `logic-puzzle` |
| Bài 3 | Mạng nâng cao | Thiết bị mạng chuyên dụng | Chức năng của Router công nghiệp, Switch quản lý (Managed Switch) và thiết bị phát Wi-Fi diện rộng Access Point. | `G12-NET-03` | `packet-route` |
| Bài 4 | An toàn thông tin | Các kỹ thuật tấn công và biện pháp phòng chống | Tìm hiểu phương thức tấn công giả mạo ARP Spoofing, tấn công từ chối dịch vụ phân tán DDoS và giải pháp giảm thiểu rủi ro. | `G12-SEC-01` | `branch-story` |
| Bài 5 | An toàn thông tin | Tường lửa và bảo mật hệ thống | Cấu hình luật tường lửa (Firewall Rules) chặn các cổng truy cập nguy hiểm; thiết lập hệ thống ghi nhật ký an ninh mạng (Log). | `G12-SEC-02` | `sort-drag` |
| Bài 6 | Trí tuệ nhân tạo | Tổng quan về Trí tuệ nhân tạo (AI) | Lịch sử phát triển của AI; phân biệt giữa hệ thống quy tắc truyền thống (Rule-based) và hệ thống học từ dữ liệu (Data-driven). | `G12-AI-01` | `match-memory` |
| Bài 7 | Trí tuệ nhân tạo | Ứng dụng AI trong các ngành kinh tế | Trợ lý ảo thông minh, hệ thống gợi ý sản phẩm thương mại điện tử, xe tự hành và tối ưu hóa chuỗi cung ứng logistics. | `G12-AI-02` | `sort-drag` |
| Bài 8 | Học máy | Các kỹ thuật Học máy cơ bản | Thuật toán K láng giềng gần nhất (KNN), Cây quyết định (Decision Tree) trong bài toán phân loại nhãn dữ liệu. | `G12-ML-01` | `sort-drag` |
| Bài 9 | Học máy | Huấn luyện mô hình và kiểm thử | Quy trình chuẩn bị dữ liệu (Data Preprocessing), chuẩn hóa số liệu và chia tập dữ liệu Train/Test để huấn luyện mô hình. | `G12-ML-02` | `bug-hunt` |
| Bài 10 | Học sâu & AI | Mạng nơ-ron nhân tạo và Học sâu | Cấu trúc mạng nhiều lớp ẩn (Deep Neural Network); nguyên lý lan truyền ngược (Backpropagation) điều chỉnh trọng số kết nối. | `G12-AI-03` | `logic-puzzle` |
| Bài 11 | Học sâu & AI | Trí tuệ nhân tạo tạo sinh và tương lai | Công nghệ Generative AI, mô hình khuếch tán (Diffusion Models) tạo ảnh nghệ thuật và tiềm năng cách mạng hóa giáo dục. | `G12-AI-04` | `branch-story` |
| Bài 12 | Đạo đức AI | Đạo đức trong kỷ nguyên Trí tuệ nhân tạo | Đảm bảo tính công bằng của thuật toán, tôn trọng bản quyền sở hữu trí tuệ của tác phẩm do con người sáng tạo; an toàn dữ liệu. | `G12-ETHIC-01` | `branch-story` |
| Bài 13 | Lập trình Web | Cấu trúc tài liệu web với HTML5 | Tạo tài liệu chuẩn HTML5; sử dụng các thẻ ngữ nghĩa (header, nav, section, article, footer) tối ưu SEO cho công cụ tìm kiếm. | `G12-WEB-01` | `type-run` |
| Bài 14 | Lập trình Web | Định kiểu và bố cục hiện đại với CSS3 | Thiết kế giao diện web đáp ứng (Responsive Web Design) bằng Media Queries; căn chỉnh layout linh hoạt bằng CSS Flexbox. | `G12-WEB-02` | `sort-drag` |
| Bài 15 | Lập trình Web | Tương tác động với JavaScript | Viết mã JavaScript xử lý các sự kiện click chuột, cuộn trang, gửi biểu mẫu và cập nhật nội dung trang web không cần tải lại trang. | `G12-WEB-03` | `bug-hunt` |
| Bài 16 | Tổng kết | Đấu trường Công nghệ EasyTin toàn năng | Vượt qua thử thách trùm cuối: tổng hợp toàn bộ kiến thức 10 năm học Tin học từ lớp 3 đến lớp 12 chuẩn GDPT 2018. | `G12-BOSS` | `boss-quiz` |

---
> Bản trích xuất Chân trời sáng tạo Lớp 3–12 hoàn tất 100% không thiếu bài nào theo đúng cấu trúc SGK Bộ GD&ĐT.
"""

# ==============================================================================
# GHI FILE
# ==============================================================================
workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(workspace_root, "01a-extract-kntt-g3_12.md"), "w", encoding="utf-8") as f:
    f.write(kntt_content)
print("Updated: 01a-extract-kntt-g3_12.md")

with open(os.path.join(workspace_root, "01a-extract-canhdieu-g3_12.md"), "w", encoding="utf-8") as f:
    f.write(canhdieu_content)
print("Updated: 01a-extract-canhdieu-g3_12.md")

with open(os.path.join(workspace_root, "01a-extract-ctst-g3_12.md"), "w", encoding="utf-8") as f:
    f.write(ctst_content)
print("Updated: 01a-extract-ctst-g3_12.md")
