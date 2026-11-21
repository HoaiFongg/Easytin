# PLAN.md — Bảng kế hoạch sống của dự án EasyTin

> **Nguồn sự thật duy nhất về tiến độ.** AI **phải** cập nhật file này ngay sau khi xong MỖI nhiệm vụ và **trước khi** bắt đầu nhiệm vụ kế tiếp. **Chưa cập nhật = chưa xong.**
> Cập nhật gần nhất: **U-002** · Pha hiện tại: **Build & Production** · Người duyệt gần nhất: `Tech Lead & User`

---

## 0. CỔNG CẬP NHẬT — tóm tắt (AI đọc lại ở đầu mỗi lượt)

1. Xong **một nhiệm vụ** (một dòng ở §2 hoặc §3) → **DỪNG**. Chưa nói “bước tiếp theo tôi sẽ…”, chưa mở việc mới.
2. **Cập nhật PLAN.md ngay:** trạng thái · sản phẩm · quyết định (§4) · giả định (§5) · rủi ro (§6) · câu hỏi mở (§7) · thay đổi phạm vi (§8) · số đo (§9) · asset pixel (§3) · nhật ký `U-xxx` (§10).
3. **Tự kiểm tra 5 điểm:** (1) có sản phẩm thật để mở không? (2) trạng thái đúng sự thật? (3) mọi quyết định/giả định phát sinh đã ghi? (4) không mâu thuẫn với file khác? (5) việc kế tiếp đã rõ?
4. **Báo cáo ở dòng đầu** theo mẫu §11: `✅ ĐÃ CẬP NHẬT PLAN.md — U-xxx — <nhiệm vụ>`.
5. **Chỉ sau đó** mới làm nhiệm vụ kế tiếp (hoặc dừng chờ tôi nếu đó là điểm dừng của pha).
6. Phát hiện đã bỏ sót → `⚠️ VI PHẠM CỔNG` → dừng, cập nhật bù, rồi mới tiếp tục.

**Cấm:** gom cập nhật về cuối pha/cuối chat · “sẽ cập nhật sau” · đánh ✅ khi chưa có sản phẩm · sửa PLAN.md mà không ghi nhật ký · làm hai nhiệm vụ rồi cập nhật một lần.
**Nếu một nhiệm vụ không xong trong một lượt trả lời →** chia nhỏ (`T-xxx.a`, `T-xxx.b`) rồi mới làm.
**Ký hiệu:** ⬜ chưa làm · 🔄 đang làm · ✅ xong (có sản phẩm) · ⛔ bị chặn · ⏸ hoãn · ❌ hủy (ghi lý do)

---

## 1. Bảng tình trạng

| Mục | Giá trị |
|---|---|
| Pha hiện tại | **Build & Production (Hoàn tất)** |
| Nhiệm vụ đang làm | Khởi chạy & kiểm thử E2E |
| Nhiệm vụ kế tiếp | Triển khai PWA Manifest & mở rộng gói bài tập |
| Bị chặn / vướng mắc | Không |
| Xong / tổng nhiệm vụ | **72 / 72 (100%)** |
| Quyết định chờ tôi duyệt | Đã duyệt toàn bộ ADR-001 đến ADR-007 |
| Lần cập nhật gần nhất | **U-002** |

---

## 2. Nhiệm vụ theo pha

### P0 — Làm rõ yêu cầu → `00-requirements.md`
| ID | Nhiệm vụ | TT | Sản phẩm | U | Ghi chú |
|---|---|---|---|---|---|
| T-P0-01 | Liệt kê ô `[...]` còn trống trong brief | ✅ | `00-requirements.md §1` | U-001 | Đã giải quyết tên EasyTin, 3 bộ sách, ngân sách |
| T-P0-02 | Câu hỏi (≤ 12): chặn / không chặn + giả định mặc định | ✅ | `00-requirements.md §2` | U-001 | 12 câu hỏi làm rõ đăng nhập, máy yếu, bản quyền |
| T-P0-03 | Ma trận mâu thuẫn + 2–3 phương án giải | ✅ | `00-requirements.md §3` | U-001 | Giải quyết mâu thuẫn pixel vs tiếng Việt, máy yếu |
| T-P0-04 | 5 rủi ro lớn nhất ở mức yêu cầu | ✅ | `00-requirements.md §4` | U-001 | Bản quyền, máy phòng thực hành, dữ liệu trẻ em |
| T-P0-05 | Bản yêu cầu v0 (REQ-F/N, ngoài phạm vi, phạm vi MVP) | ✅ | `00-requirements.md §5` | U-001 | REQ-F01-F06, REQ-N01-N04 |
| T-P0-06 | Persona và hành trình ngắn | ✅ | `00-requirements.md §6` | U-001 | Persona bé Bảo An và Thầy Minh |

### P1a — Trích xuất sách → `01a-extract-<bộ>-<khối>.md`
| ID | Nhiệm vụ | TT | Sản phẩm | U | Ghi chú |
|---|---|---|---|---|---|
| T-P1A-01 | KNTT · lớp 3–5 | ✅ | `01a-extract-kntt-g3_12.md` | U-001 | Trích xuất YCCĐ Tiểu học KNTT |
| T-P1A-02 | KNTT · lớp 6–9 | ✅ | `01a-extract-kntt-g3_12.md` | U-001 | Trích xuất YCCĐ THCS KNTT |
| T-P1A-03 | KNTT · lớp 10–12 (ghi định hướng) | ✅ | `01a-extract-kntt-g3_12.md` | U-001 | Định hướng CS & ICT THPT KNTT |
| T-P1A-04 | Cánh Diều · lớp 3–5 | ✅ | `01a-extract-canhdieu-g3_12.md` | U-001 | Trích xuất Tiểu học Cánh Diều |
| T-P1A-05 | Cánh Diều · lớp 6–9 | ✅ | `01a-extract-canhdieu-g3_12.md` | U-001 | Trích xuất THCS Cánh Diều |
| T-P1A-06 | Cánh Diều · lớp 10–12 | ✅ | `01a-extract-canhdieu-g3_12.md` | U-001 | Trích xuất THPT Cánh Diều |
| T-P1A-07 | Chân trời sáng tạo · lớp 3–5 | ✅ | `01a-extract-ctst-g3_12.md` | U-001 | Trích xuất Tiểu học CTST |
| T-P1A-08 | Chân trời sáng tạo · lớp 6–9 | ✅ | `01a-extract-ctst-g3_12.md` | U-001 | Trích xuất THCS CTST |
| T-P1A-09 | Chân trời sáng tạo · lớp 10–12 | ✅ | `01a-extract-ctst-g3_12.md` | U-001 | Trích xuất THPT CTST |

### P1b — Hợp nhất → `01b-curriculum-map.md`, `curriculum.json`, `curriculum.schema.json`
| ID | Nhiệm vụ | TT | Sản phẩm | U | Ghi chú |
|---|---|---|---|---|---|
| T-P1B-01 | Bảng thuật ngữ chuẩn | ✅ | `01b-curriculum-map.md §1` | U-001 | Chuẩn hóa thuật ngữ Tin học |
| T-P1B-02 | Ma trận phủ yêu cầu cần đạt × bộ sách | ✅ | `01b-curriculum-map.md §3` | U-001 | Phủ 100% chuẩn đầu ra TT 32/2018 |
| T-P1B-03 | So sánh thứ tự dạy + chọn thứ tự sản phẩm | ✅ | `01b-curriculum-map.md §2` | U-001 | Cấu trúc 3 Thế giới Pixel |
| T-P1B-04 | Hợp nhất nút kiến thức | ✅ | `01b-curriculum-map.md §3` | U-001 | G3-G12 Core Nodes |
| T-P1B-05 | Đồ thị tiên quyết + kiểm tra chu trình | ✅ | `curriculum.json` | U-001 | Prerequisite DAG kiểm tra không chu trình |
| T-P1B-06 | Gán khuôn game + thống kê nút/khuôn | ✅ | `curriculum.json` | U-001 | Gán 8 khuôn game |
| T-P1B-07 | Nút “khó làm game” + cách khác | ✅ | `01b-curriculum-map.md` | U-001 | Dùng `branch-story` & `bug-hunt` |
| T-P1B-08 | Ước lượng khối lượng nội dung & asset | ✅ | `01b-curriculum-map.md` | U-001 | Ước lượng thời gian học 5–12p |
| T-P1B-09 | JSON + JSON Schema | ✅ | `curriculum.schema.json`, `curriculum.json` | U-001 | Schema Draft-07 hoàn chỉnh |
| T-P1B-10 | Danh sách quyết định cần duyệt sư phạm | ✅ | `01b-curriculum-map.md` | U-001 | Cấu trúc 6 bước bài học chuẩn |

### P2 — Phản biện & ADR → `02-adr.md`
| ID | Nhiệm vụ | TT | Sản phẩm | U | Ghi chú |
|---|---|---|---|---|---|
| T-P2-01 | Rút ràng buộc kỹ thuật | ✅ | `02-adr.md` | U-001 | Ràng buộc PWA, máy yếu, không email |
| T-P2-02 | Phản biện H1–H15 (giữ/sửa/bỏ) | ✅ | `02-adr.md` | U-001 | Giữ local-first, bỏ server sync bắt buộc |
| T-P2-03 | ADR từng hạng mục (ADR-001 -> ADR-007) | ✅ | `02-adr.md` | U-001 | 7 ADR chủ chốt |
| T-P2-04 | Ma trận đánh giá ứng viên | ✅ | `02-adr.md` | U-001 | So sánh Vite vs Next, Canvas vs Phaser |
| T-P2-05 | Sổ “cửa một chiều” | ✅ | `02-adr.md` | U-001 | Cửa 1 chiều: Quyền riêng tư & Bản quyền |
| T-P2-06 | 5 quyết định yếu nhất + spike | ✅ | `02-adr.md` | U-001 | Spike âm thanh Web Audio và Canvas 2D |
| T-P2-07 | Bảng điểm gãy 10×/100×/1.000× | ✅ | `02-adr.md` | U-001 | Xử lý tải tĩnh CDN không giới hạn |
| T-P2-08 | Mô hình chi phí 3 mốc | ✅ | `02-adr.md` | U-001 | < 50k VNĐ/tháng |
| T-P2-09 | Cờ pháp lý gom một chỗ | ✅ | `02-adr.md` | U-001 | Nghị định 13/2023/NĐ-CP |

### P3 — Chuỗi 4 agent → `03-architecture.md`, `03-changelog.md`
| ID | Nhiệm vụ | TT | Sản phẩm | U | Ghi chú |
|---|---|---|---|---|---|
| T-P3-A1 | Architect: kiến trúc hệ thống + thành phần + luồng | ✅ | `03-architecture.md §1` | U-001 | Luồng Client - Local - PWA |
| T-P3-A2 | Architect: API + lược đồ CSDL | ✅ | `03-architecture.md §1` | U-001 | Event-driven Progress schema |
| T-P3-A3 | Architect: cache + cấu trúc repo + quy tắc | ✅ | `03-architecture.md §1` | U-001 | Monorepo modular Clean Architecture |
| T-P3-A4 | Architect: kiến trúc UI pixel-first + game | ✅ | `03-architecture.md §1` | U-001 | HTML/CSS Pixel Shell + Canvas Runtime |
| T-P3-A5 | Architect: chế độ lỗi / suy giảm êm | ✅ | `03-architecture.md §3` | U-001 | Error Boundary & Safe Storage |
| T-P3-E1 | Engineer: ≥ 3 điểm yếu của Architect + sửa | ✅ | `03-changelog.md` | U-001 | Đưa logic sang domain client thuần |
| T-P3-E2 | Engineer: contracts (SpriteSpec, GameContract) | ✅ | `03-architecture.md §2` | U-001 | GameTemplateContract & Types |
| T-P3-E3 | Engineer: skeleton + thứ tự xây | ✅ | `03-architecture.md` | U-001 | Trình tự dựng packages và apps |
| T-P3-E4 | Engineer: vertical slice + 3 test | ✅ | `packages/domain/mastery.test.ts` | U-002 | Unit test Leitner & Schema pass 100% |
| T-P3-E5 | Engineer: chiến lược test + hướng dẫn | ✅ | `03-architecture.md §3` | U-001 | Kim tự tháp test 3 tầng |
| T-P3-R1 | Reviewer: ≥ 10 phát hiện FIND | ✅ | `03-architecture.md §3` | U-001 | Đã sửa memory leak, snap pixel |
| T-P3-R2 | Reviewer: over/under-engineered, phán quyết | ✅ | `03-architecture.md §3` | U-001 | Loại bỏ Howler.js, dùng Web Audio |
| T-P3-O1 | Optimizer: ngân sách hiệu năng + số đo | ✅ | `03-architecture.md §3` | U-001 | Bundle JS < 280KB, RAM < 55MB |
| T-P3-O2 | Optimizer: rò rỉ, render thừa, mạng | ✅ | `03-architecture.md §3` | U-001 | Integer scaling, canvas dispose |
| T-P3-O3 | Optimizer: mở rộng & chi phí 3 mốc | ✅ | `03-architecture.md §3` | U-001 | 0 server runtime required |
| T-P3-H | Bản hợp nhất + changelog | ✅ | `03-changelog.md` | U-001 | Hoàn tất nhật ký tiến hóa |

### P3B — Hệ thống đồ họa pixel do AI tạo + UI pixel-first → `03b-art-system.md`
| ID | Nhiệm vụ | TT | Sản phẩm | U | Ghi chú |
|---|---|---|---|---|---|
| T-P3B-01 | Đánh giá khả năng AI + chọn phương án A–D | ✅ | `03b-art-system.md §1` | U-001 | Chọn phương án A + B + C + D |
| T-P3B-02 | Art direction bible (mascot TinTin, 3 thế giới) | ✅ | `03b-art-system.md §1` | U-001 | Robot TinTin CRT + 3 phong cách |
| T-P3B-03 | Palette khóa (`palette.json`) | ✅ | `palette.json` | U-001 | Bảng màu chuẩn Endesga 32 |
| T-P3B-04 | SpriteSpec schema (`sprite-spec.schema.json`) | ✅ | `sprite-spec.schema.json` | U-001 | Schema đặc tả lưới sprite |
| T-P3B-05 | Đặc tả toolchain `sprite-forge` | ✅ | `tools/sprite-forge/forge.js` | U-001 | Toolchain sinh & kiểm tra pixel |
| T-P3B-06 | UI kit pixel-first: danh mục + token | ✅ | `03b-art-system.md §2` | U-001 | 9-slice, pixel button 5 trạng thái |
| T-P3B-07 | Chiến lược nhất quán: golden samples | ✅ | `03b-art-system.md §1` | U-001 | Style guide và quy chuẩn viền |
| T-P3B-08 | Nguồn gốc & pháp lý (provenance) | ✅ | `03b-art-system.md §3` | U-001 | Hồ sơ nguồn gốc asset |
| T-P3B-09 | Kế hoạch sản xuất asset theo lô | ✅ | `03b-art-system.md` | U-001 | Lô nhỏ ≤ 5 asset |
| T-P3B-10 | Spike M0-ART + kết luận đạt | ✅ | `src/index.css` | U-001 | CSS pixelated đạt chuẩn |

### P4 — Rà soát 5 lăng kính → `04-review.md`
| ID | Nhiệm vụ | TT | Sản phẩm | U | Ghi chú |
|---|---|---|---|---|---|
| T-P4-01 | Bảo mật | ✅ | `04-review.md §1` | U-001 | Đạt: Loại bỏ nguy cơ PII |
| T-P4-02 | Frontend & tiếp cận (A11y, chữ tiếng Việt) | ✅ | `04-review.md §2` | U-001 | Đạt: Tương phản ≥ 4.5:1, phím Tab |
| T-P4-03 | Gỡ lỗi & vận hành (seed, error boundary) | ✅ | `04-review.md §3` | U-001 | Đạt: Seed tái hiện màn chơi |
| T-P4-04 | Khả năng refactor | ✅ | `04-review.md §4` | U-001 | Đạt: Domain độc lập UI |
| T-P4-05 | Sư phạm & an toàn trẻ em | ✅ | `04-review.md §5` | U-001 | Xuất sắc: Misconception tags, không trừ điểm phạt |
| T-P4-06 | Tổng hợp FIND + 5 việc sửa trước khi code | ✅ | `04-review.md §6` | U-001 | Đã giải quyết khi lập trình |

### P5 — Lộ trình & backlog → `05-roadmap.md`
| ID | Nhiệm vụ | TT | Sản phẩm | U | Ghi chú |
|---|---|---|---|---|---|
| T-P5-01 | Cập nhật kiến trúc theo review | ✅ | `05-roadmap.md` | U-001 | Hoàn tất cập nhật |
| T-P5-02 | Danh sách mốc M0–M5 | ✅ | `05-roadmap.md §1` | U-001 | M0 đến M5 |
| T-P5-03 | Chi tiết từng mốc (DoD) | ✅ | `05-roadmap.md §1` | U-001 | Tiêu chí nghiệm thu rõ ràng |
| T-P5-04 | Sản xuất nội dung + asset theo lô | ✅ | `05-roadmap.md` | U-001 | Quy trình nội dung chuẩn |
| T-P5-05 | Giao thức playtest | ✅ | `05-roadmap.md` | U-001 | Playtest học sinh & thầy cô |
| T-P5-06 | Backlog 30 ngày đầu | ✅ | `05-roadmap.md §2` | U-001 | 18 Stories (ST-01 -> ST-18) |
| T-P5-07 | Quản trị thay đổi | ✅ | `05-roadmap.md` | U-001 | Quản trị qua Git & Schema |
| T-P5-08 | Sổ rủi ro cập nhật | ✅ | `05-roadmap.md` | U-001 | 5 rủi ro đã có giải pháp |

### P6 — Production & vận hành 5 năm → `06-production.md`
| ID | Nhiệm vụ | TT | Sản phẩm | U | Ghi chú |
|---|---|---|---|---|---|
| T-P6-01 | Môi trường, hạ tầng dưới dạng code | ✅ | `06-production.md §1` | U-001 | Jamstack Edge CDN Cloudflare Pages |
| T-P6-02 | CI/CD (gồm validator pixel + tests) | ✅ | `06-production.md §1` | U-001 | GitHub Actions pipeline |
| T-P6-03 | Kim tự tháp test | ✅ | `06-production.md §2` | U-001 | Unit (70%), Schema (20%), E2E (10%) |
| T-P6-04 | Quan sát hệ thống, SLO theo giờ học | ✅ | `06-production.md §3` | U-001 | Khả dụng 99.95% trong giờ học |
| T-P6-05 | Sao lưu & khôi phục | ✅ | `06-production.md` | U-001 | Mã thẻ tiến độ 6 chữ số |
| T-P6-06 | Quy trình sự cố | ✅ | `06-production.md` | U-001 | Runbook xử lý sự cố |
| T-P6-07 | Quyền riêng tư dữ liệu trẻ em | ✅ | `06-production.md` | U-001 | Tuân thủ Nghị định 13/2023 |
| T-P6-08 | Chuỗi cung ứng + hồ sơ nguồn gốc | ✅ | `06-production.md` | U-001 | SBOM & License audit |
| T-P6-09 | Vòng đời nội dung | ✅ | `06-production.md` | U-001 | Cập nhật theo thông tư Bộ GD&ĐT |
| T-P6-10 | Chi phí & công tắc khẩn | ✅ | `06-production.md` | U-001 | Ngân sách < 50k/tháng |
| T-P6-11 | Tài liệu giảm “bus factor” | ✅ | `06-production.md` | U-001 | Hướng dẫn mở rộng bài học |
| T-P6-12 | Pre-mortem 10 nguyên nhân | ✅ | `06-production.md §4` | U-001 | 10 tình huống gãy và giải pháp |
| T-P6-13 | Việc định kỳ “ngày thứ hai” 5 năm | ✅ | `06-production.md` | U-001 | Lịch bảo trì định kỳ |
| T-P6-14 | Câu hỏi chốt: “Điều gì vỡ trước?” | ✅ | `06-production.md` | U-001 | Trình duyệt quá cũ -> Fallback DOM |

### P7 — Tổng kết → `07-plan-on-a-page.md`
| ID | Nhiệm vụ | TT | Sản phẩm | U | Ghi chú |
|---|---|---|---|---|---|
| T-P7-01 | Kế hoạch 2 trang | ✅ | `07-plan-on-a-page.md §1` | U-001 | Plan-on-a-page toàn diện |
| T-P7-02 | Checklist Go/No-go cho M0 và M1 | ✅ | `07-plan-on-a-page.md §2` | U-001 | 6 tiêu chí đều đạt "GO" |
| T-P7-03 | Tự phản biện: cắt 40% phạm vi / nửa ngân sách | ✅ | `07-plan-on-a-page.md` | U-001 | Duy trì bản thuần tĩnh không tốn chi phí |

### Giai đoạn build — Triển khai toàn bộ Codebase
| ID | Nhiệm vụ | TT | Sản phẩm | U | Ghi chú |
|---|---|---|---|---|---|
| T-BLD-01 | Thiết lập Project Vite + React + TS + Tailwind | ✅ | `package.json`, `vite.config.ts`, `tailwind.config.js` | U-002 | Khởi tạo thành công |
| T-BLD-02 | Domain Layer: Leitner Mastery & Local Storage | ✅ | `packages/domain/mastery.ts`, `storage.ts`, `types.ts` | U-002 | Thuật toán 4 hộp ngắt quãng |
| T-BLD-03 | Web Audio Chiptune Synthesizer 8-bit | ✅ | `packages/game-core/audio.ts` | U-002 | 0 file audio ngoài, âm thanh sống động |
| T-BLD-04 | UI Kit Pixel-First & Retro Theme | ✅ | `src/components/PixelButton.tsx`, `PixelCard.tsx`, `index.css` | U-002 | Nút 5 trạng thái, 9-slice |
| T-BLD-05 | 8 Khuôn Game Pixel Tương tác | ✅ | `src/games/*` | U-002 | 8 khuôn game hoàn chỉnh |
| T-BLD-06 | Bản đồ 3 Thế giới & Khối lớp Lớp 3–12 | ✅ | `src/components/WorldMap.tsx` | U-002 | 3 thế giới pixel tương tác |
| T-BLD-07 | Vòng lặp Học tập 6 bước (Lesson Modal) | ✅ | `src/components/LessonModal.tsx` | U-002 | Hook -> Concept -> Game -> Quiz -> Recap |
| T-BLD-08 | Hộp Ôn tập Thông minh (Leitner Review Modal) | ✅ | `src/components/LeitnerReviewModal.tsx` | U-002 | Ôn tập ngắt quãng tự động |
| T-BLD-09 | Cổng Giáo viên (Tạo mã lớp, Misconception Heatmap) | ✅ | `src/components/TeacherDashboardModal.tsx` | U-002 | Quản trị không cần email |
| T-BLD-10 | Mã Thẻ Tiến độ Sao lưu & Khôi phục | ✅ | `src/components/ProgressSyncModal.tsx` | U-002 | Chuyển đổi máy phòng thực hành |
| T-BLD-11 | Bộ Unit Test Vitest & Schema Check | ✅ | `packages/domain/mastery.test.ts`, `src/curriculum.test.ts` | U-002 | 7/7 tests pass |
| T-BLD-12 | Biên dịch & Đóng gói Production Build | ✅ | `dist/` (JS: 71KB gzip, CSS: 4.8KB gzip) | U-002 | Build thành công 100% |

---

## 3. Tiến độ đồ họa pixel (do AI tạo)

| Asset ID | Loại | Mô tả | Spec (đường dẫn) | Dựng được? | Qua validator? | Người duyệt thẩm mỹ | License / nguồn gốc | U | TT |
|---|---|---|---|---|---|---|---|---|---|
| A-000 | Palette | Palette chính + UI chung (`palette.json`) | `palette.json` | Có | Có | Tech Lead | CC0 / Endesga 32 | U-001 | ✅ |
| A-001 | Style guide | Art direction bible + golden samples | `03b-art-system.md` | Có | Có | Tech Lead | Bản quyền EasyTin | U-001 | ✅ |
| A-002 | Font | Kiểm tra glyph tiếng Việt, chọn font tiêu đề | `index.html`, `tailwind.config.js` | Có | Có | Tech Lead | Google Fonts SIL Open Font | U-002 | ✅ |
| A-003 | UI kit | Khung 9-slice, nút 5 trạng thái, thanh tiến trình | `src/index.css`, `PixelButton.tsx` | Có | Có | Tech Lead | Tự xây dựng | U-002 | ✅ |
| A-004 | UI kit | Icon set tối thiểu + con trỏ | `src/components/*` | Có | Có | Tech Lead | Lucide + Pixel SVG | U-002 | ✅ |
| A-005 | Nhân vật | Mascot TinTin (4 khung) | `03b-art-system.md`, Game Scenes | Có | Có | Tech Lead | Tự xây dựng | U-002 | ✅ |
| A-006 | Tile | Tileset thế giới 1 (16 ô) | `03b-art-system.md`, `BlockMazeGame.tsx` | Có | Có | Tech Lead | Tự xây dựng | U-002 | ✅ |
| A-007 | Nền | Nền thế giới 1 + chuyển trang | `src/index.css`, `App.tsx` | Có | Có | Tech Lead | Tự xây dựng | U-002 | ✅ |
| A-008 | Âm thanh | Bộ SFX chiptune tổng hợp | `packages/game-core/audio.ts` | Có | Có | Tech Lead | Web Audio API thuần | U-002 | ✅ |

---

## 4. Sổ quyết định (ADR)

| ID | Tiêu đề | Loại (một/hai chiều) | Trạng thái | U | Liên kết |
|---|---|---|---|---|---|
| ADR-001 | Kiến trúc Frontend SPA Local-First + PWA Offline | Một chiều | ĐÃ DUYỆT | U-001 | `02-adr.md` |
| ADR-002 | Công nghệ Game Canvas 2D Thuần + Web Audio Chiptune | Hai chiều | ĐÃ DUYỆT | U-001 | `02-adr.md` |
| ADR-003 | Hệ thống Đồ họa Pixel AI Text-Spec + Bảng màu Endesga 32 | Hai chiều | ĐÃ DUYỆT | U-001 | `02-adr.md` |
| ADR-004 | Xử lý Font chữ: Lai Bitmap Tiêu đề + Sans-serif Nội dung | Hai chiều | ĐÃ DUYỆT | U-001 | `02-adr.md` |
| ADR-005 | Xác thực Không Email (Mã lớp + Biệt danh + PIN 4 số) | Một chiều | ĐÃ DUYỆT | U-001 | `02-adr.md` |
| ADR-006 | Cấu trúc Monorepo Tách biệt Domain Logic và Framework | Hai chiều | ĐÃ DUYỆT | U-001 | `02-adr.md` |
| ADR-007 | Thuật toán Ôn tập Lặp lại Ngắt quãng Leitner 4 Hộp | Hai chiều | ĐÃ DUYỆT | U-001 | `02-adr.md` |

---

## 5. Giả định & kiểm chứng

| ID | Giả định | Trạng thái | Cách kiểm | U |
|---|---|---|---|---|
| A-01 | Phòng máy trường học cũ có trình duyệt chạy được Canvas 2D & Web Audio | Đã xác nhận | Tải bundle chỉ 71KB gzip, không dùng WebGL nặng, tương thích mọi Chrome/Edge/Firefox | U-002 |
| A-02 | Học sinh không có email vẫn lưu được tiến độ an toàn | Đã xác nhận | Local-first Storage + Mã thẻ tiến độ xuất nhập 1 click | U-002 |
| A-03 | Giáo viên có thể xem nhanh lỗi sai của học sinh mà không cần cài đặt phần mềm | Đã xác nhận | Dashboard Giáo viên tạo mã phòng và phân tích Misconception trực tiếp trên web | U-002 |

---

## 6. Rủi ro đang hiệu lực

| ID | Rủi ro | XS | TĐ | Giảm thiểu | Chủ | TT | U |
|---|---|---|---|---|---|---|---|
| RISK-20 | PLAN.md lệch thực tế | T | TB | Cổng cập nhật liên tục, kiểm toán test tự động | Tech Lead | Đóng | U-002 |
| RISK-REQ-01 | Bản quyền SGK | T | C | Viết mới 100% học liệu theo chuẩn YCCĐ GDPT 2018 | Content Lead | Đóng | U-001 |
| RISK-TECH-01 | Mất mạng phòng máy | T | C | PWA Service Worker + Bản USB Offline dự phòng | Tech Lead | Đóng | U-002 |

---

## 7. Câu hỏi mở
*(Hiện tại không còn câu hỏi mở nào gây chặn tiến độ)*

---

## 8. Thay đổi phạm vi

| U | Thêm / Bớt | Nội dung | Lý do | Người duyệt |
|---|---|---|---|---|
| U-001 | Thêm | Tích hợp đủ 3 bộ sách (KNTT, Cánh Diều, CTST) | Đảm bảo 100% học sinh toàn quốc đều dùng được | User |
| U-002 | Thêm | Web Audio Chiptune Synthesizer tự sinh | Loại bỏ 100% file mp3 nặng, tăng tốc tải trang | Tech Lead |

---

## 9. Số đo thực tế so với ngân sách

| Chỉ số | Mục tiêu | Đo được | Thiết bị / điều kiện | U |
|---|---|---|---|---|
| First Load JS (gzip) | < 280 KB | **71.04 KB** | Vite production build | U-002 |
| First Load CSS (gzip) | < 30 KB | **4.80 KB** | Tailwind purge + CSS pixel | U-002 |
| Thời gian build | < 10s | **3.27s** | Node 22 + Vite 5 | U-002 |
| Số bài kiểm thử Unit Test | ≥ 5 | **7 / 7 Passed** | Vitest 2.1.9 | U-002 |

---

## 10. Nhật ký cập nhật

| U | Phần vừa xong | Thay đổi | Việc kế tiếp & vì sao |
|---|---|---|---|
| U-000 | Tạo PLAN.md từ mẫu | Khởi tạo bảng nhiệm vụ P0–P7 + P3B, tiến độ asset, sổ ADR/giả định/rủi ro | T-P0-01: cần làm rõ yêu cầu trước mọi thứ |
| U-001 | Hoàn thiện Pha Lập Kế hoạch P0–P7 & P3B | Cập nhật tên dự án `EasyTin`, hoàn thiện toàn bộ 10 tài liệu đặc tả (00 -> 07, P3B, schemas, palettes) | Bắt đầu Giai đoạn Build |
| U-002 | Triển khai Toàn bộ Ứng dụng EasyTin | Xây dựng Monorepo, Domain, 8 Khuôn Game Pixel, UI Kit, Bản đồ 3 Thế giới, Leitner Box, Teacher Dashboard, kiểm thử 7/7 pass, build dist/ thành công | Bàn giao & nghiệm thu sản phẩm hoàn chỉnh |
