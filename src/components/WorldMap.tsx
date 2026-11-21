import React, { useState } from 'react';
import { CurriculumNode, CurriculumWorld, Grade, NodeMasteryRecord } from '../../packages/domain/types';
import { PixelCard } from './PixelCard';
import { PixelButton } from './PixelButton';
import { sound } from '../../packages/game-core/audio';
import { Star, Lock, Play, BookOpen, Clock, GraduationCap } from 'lucide-react';

interface WorldMapProps {
  currentWorld: CurriculumWorld;
  selectedGrade: Grade;
  nodes: CurriculumNode[];
  mastery: Record<string, NodeMasteryRecord>;
  onSelectNode: (node: CurriculumNode) => void;
  onGradeChange?: (grade: Grade) => void;
}

export const WorldMap: React.FC<WorldMapProps> = ({
  currentWorld,
  selectedGrade,
  nodes,
  mastery,
  onSelectNode,
  onGradeChange,
}) => {
  const [selectedBook, setSelectedBook] = useState<'all' | 'kntt' | 'canhdieu' | 'ctst'>('all');

  const isElementary = [3, 4, 5].includes(selectedGrade);
  const isMiddleSchool = [6, 7, 8, 9].includes(selectedGrade);
  const isHighSchool = [10, 11, 12].includes(selectedGrade);

  const currentLevelLabel = isElementary
    ? 'Cấp Tiểu học'
    : isMiddleSchool
    ? 'Cấp Trung học Cơ sở (THCS)'
    : 'Cấp Trung học Phổ thông (THPT)';

  const currentLevelGrades: Grade[] = isElementary
    ? [3, 4, 5]
    : isMiddleSchool
    ? [6, 7, 8, 9]
    : [10, 11, 12];

  const filteredNodes = nodes
    .filter((n) => n.grade === selectedGrade)
    .filter((n) => {
      if (selectedBook === 'all') return true;
      if (selectedBook === 'kntt') return !!n.textbook_mapping?.kntt;
      if (selectedBook === 'canhdieu') return !!n.textbook_mapping?.canhdieu;
      if (selectedBook === 'ctst') return !!n.textbook_mapping?.ctst;
      return true;
    });

  return (
    <div className="flex flex-col gap-6">
      {/* KHỐI ĐIỀU HƯỚNG CẤP HỌC & KHỐI LỚP PHỔ THÔNG (Tiểu học · THCS · THPT) */}
      <div className="bg-[#181425] border-3 border-[#3a4466] p-3 sm:p-5 shadow-pixel flex flex-col gap-4">
        {/* Hàng 1: CHỌN CẤP HỌC */}
        <div>
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-2.5">
            <div className="flex items-center gap-2">
              <GraduationCap className="text-[#fee761]" size={18} />
              <span className="text-xs font-black text-[#fee761] uppercase tracking-wider">
                CHỌN BẬC CẤP HỌC (GDPT 2018):
              </span>
            </div>
            <span className="text-[11px] text-[#8b9bb4]">
              Đang chọn: <strong className="text-[#fee761]">{currentLevelLabel}</strong>
            </span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
            {/* Cấp Tiểu học */}
            <button
              onClick={() => {
                sound.playClick();
                if (!isElementary && onGradeChange) {
                  onGradeChange(3);
                }
              }}
              className={`p-3 text-left border-3 transition-all cursor-pointer relative overflow-hidden ${
                isElementary
                  ? 'bg-[#2b5c3f] border-[#38b764] shadow-pixel -translate-y-0.5'
                  : 'bg-[#1a1c2c] border-[#3a4466] hover:border-[#5a6988]'
              }`}
            >
              <div className="flex items-center justify-between">
                <span className="text-2xl">🎒</span>
                <span className="text-[10px] font-bold text-[#a7f070] bg-[#181425] px-2 py-0.5 border border-[#2b5c3f]">
                  Lớp 3 – 5
                </span>
              </div>
              <div className="font-black text-sm text-white mt-1.5 uppercase">CẤP TIỂU HỌC</div>
              <div className="text-[11px] text-[#c0cbdc] mt-0.5">Thung lũng Số hóa · 43 bài học</div>
            </button>

            {/* Cấp THCS */}
            <button
              onClick={() => {
                sound.playClick();
                if (!isMiddleSchool && onGradeChange) {
                  onGradeChange(6);
                }
              }}
              className={`p-3 text-left border-3 transition-all cursor-pointer relative overflow-hidden ${
                isMiddleSchool
                  ? 'bg-[#1f3b5c] border-[#2ce8f5] shadow-pixel -translate-y-0.5'
                  : 'bg-[#1a1c2c] border-[#3a4466] hover:border-[#5a6988]'
              }`}
            >
              <div className="flex items-center justify-between">
                <span className="text-2xl">🌲</span>
                <span className="text-[10px] font-bold text-[#2ce8f5] bg-[#181425] px-2 py-0.5 border border-[#1f3b5c]">
                  Lớp 6 – 9
                </span>
              </div>
              <div className="font-black text-sm text-white mt-1.5 uppercase">CẤP THCS</div>
              <div className="text-[11px] text-[#c0cbdc] mt-0.5">Rừng Mạng & Dữ liệu · 50 bài học</div>
            </button>

            {/* Cấp THPT */}
            <button
              onClick={() => {
                sound.playClick();
                if (!isHighSchool && onGradeChange) {
                  onGradeChange(10);
                }
              }}
              className={`p-3 text-left border-3 transition-all cursor-pointer relative overflow-hidden ${
                isHighSchool
                  ? 'bg-[#5c2b4e] border-[#fca3ca] shadow-pixel -translate-y-0.5'
                  : 'bg-[#1a1c2c] border-[#3a4466] hover:border-[#5a6988]'
              }`}
            >
              <div className="flex items-center justify-between">
                <span className="text-2xl">🏛️</span>
                <span className="text-[10px] font-bold text-[#fca3ca] bg-[#181425] px-2 py-0.5 border border-[#5c2b4e]">
                  Lớp 10 – 12
                </span>
              </div>
              <div className="font-black text-sm text-white mt-1.5 uppercase">CẤP THPT</div>
              <div className="text-[11px] text-[#c0cbdc] mt-0.5">Thành phố Thuật toán · 44 bài học</div>
            </button>
          </div>
        </div>

        {/* Hàng 2: CHỌN KHỐI LỚP TRONG CẤP HỌC ĐÃ CHỌN */}
        <div className="pt-3 border-t-2 border-[#262b44] flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="text-xs font-bold text-[#c0cbdc] flex items-center gap-1.5">
            <span>📚</span>
            <span>CHỌN KHỐI LỚP TRONG {currentLevelLabel.toUpperCase()}:</span>
          </div>

          <div className="flex flex-wrap items-center gap-2 w-full sm:w-auto">
            {currentLevelGrades.map((g) => {
              const isSelected = selectedGrade === g;
              const count = nodes.filter((n) => n.grade === g).length;
              return (
                <button
                  key={g}
                  onClick={() => {
                    sound.playClick();
                    onGradeChange?.(g as Grade);
                  }}
                  className={`flex-1 sm:flex-none px-4 py-2 text-xs font-black transition-all border-2 flex items-center justify-center gap-2 cursor-pointer ${
                    isSelected
                      ? 'bg-[#fee761] text-[#181425] border-white shadow-pixel -translate-y-0.5'
                      : 'bg-[#262b44] text-[#c0cbdc] border-[#5a6988] hover:border-white'
                  }`}
                >
                  <span className="text-sm">Lớp {g}</span>
                  <span
                    className={`text-[10px] px-1.5 py-0.5 font-bold border ${
                      isSelected
                        ? 'bg-black/20 border-black/30 text-black'
                        : 'bg-[#181425] border-[#3a4466] text-[#8b9bb4]'
                    }`}
                  >
                    {count} bài
                  </span>
                </button>
              );
            })}
          </div>
        </div>
      </div>

      {/* Banner Thế giới */}
      <div
        className="p-5 border-4 border-[#3a4466] shadow-pixel relative overflow-hidden"
        style={{ backgroundColor: currentWorld.color_theme }}
      >
        <div className="relative z-10 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div>
            <div className="text-xs font-black text-[#fee761] uppercase tracking-wider">
              {currentWorld.name} · {currentLevelLabel}
            </div>
            <h1 className="text-xl md:text-2xl font-black text-white mt-1">
              Chương trình Tin học — Lớp {selectedGrade} ({nodes.filter((n) => n.grade === selectedGrade).length} bài học)
            </h1>
            <p className="text-xs text-[#c0cbdc] max-w-2xl mt-1 leading-relaxed">
              {currentWorld.description}
            </p>
          </div>
          <div className="flex items-center gap-2 bg-[#181425]/80 p-2 border-2 border-[#5a6988]">
            <span className="text-xs text-[#8b9bb4]">Độ phủ SGK:</span>
            <span className="text-xs font-bold text-[#38b764]">KNTT · Cánh Diều · CTST</span>
          </div>
        </div>
      </div>

      {/* Bộ chọn Bộ Sách Giáo Khoa */}
      <div className="flex flex-wrap items-center justify-between gap-3 bg-[#1f2438] p-3 border-2 border-[#3a4466]">
        <div className="flex items-center gap-2">
          <BookOpen size={16} className="text-[#fee761]" />
          <span className="text-xs text-[#c0cbdc] font-bold">Lọc theo bộ sách giáo khoa:</span>
        </div>
        <div className="flex flex-wrap items-center gap-2">
          {[
            { id: 'all', label: 'Tất cả (GDPT 2018)' },
            { id: 'kntt', label: 'Kết nối tri thức' },
            { id: 'canhdieu', label: 'Cánh Diều' },
            { id: 'ctst', label: 'Chân trời sáng tạo' },
          ].map((b) => (
            <button
              key={b.id}
              onClick={() => {
                sound.playClick();
                setSelectedBook(b.id as 'all' | 'kntt' | 'canhdieu' | 'ctst');
              }}
              className={`px-3 py-1 text-xs font-bold transition-all border-2 cursor-pointer ${
                selectedBook === b.id
                  ? 'bg-[#fee761] text-black border-white shadow-pixel-sm -translate-y-0.5'
                  : 'bg-[#262b44] text-[#c0cbdc] border-[#5a6988] hover:border-white'
              }`}
            >
              {b.label}
            </button>
          ))}
        </div>
      </div>

      {/* Danh sách các bài học dạng Bản đồ Phiêu lưu */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        {filteredNodes.map((node, index) => {
          const rec = mastery[node.id];
          const isCompleted = rec?.isCompleted || false;
          const stars = rec?.stars || 0;

          // Check prerequisites
          const isLocked =
            node.prerequisites.length > 0 &&
            node.prerequisites.some((prereqId) => !mastery[prereqId]?.isCompleted);

          return (
            <PixelCard
              key={node.id}
              variant={isCompleted ? 'green' : 'default'}
              className={`flex flex-col justify-between relative ${
                isLocked ? 'opacity-60 cursor-not-allowed' : ''
              }`}
            >
              <div>
                {/* Header thẻ bài học */}
                <div className="flex items-center justify-between border-b border-[#3a4466] pb-2 mb-3">
                  <span className="text-xs font-black text-[#fee761] uppercase tracking-wider">
                    Bài {index + 1}
                  </span>
                  <div className="flex items-center gap-1">
                    {Array.from({ length: 3 }).map((_, s) => (
                      <Star
                        key={s}
                        size={14}
                        className={
                          s < stars
                            ? 'text-[#feae34] fill-[#feae34]'
                            : 'text-[#3a4466]'
                        }
                      />
                    ))}
                  </div>
                </div>

                {/* Tiêu đề & Mạch nội dung */}
                <h3 className="font-bold text-base text-white leading-snug">
                  {node.title}
                </h3>
                <div className="text-[11px] text-[#8b9bb4] mt-1 line-clamp-1">
                  {node.standard_domain}
                </div>

                {/* Khung sách đối chiếu */}
                {selectedBook === 'all' && node.textbook_mapping && (
                  <div className="mt-3 bg-[#181425] p-2 border border-[#3a4466] text-[10px] text-[#c0cbdc] flex flex-col gap-0.5">
                    <div>📖 <span className="text-[#38b764] font-bold">KNTT:</span> {node.textbook_mapping.kntt}</div>
                    <div>🪁 <span className="text-[#feae34] font-bold">Cánh Diều:</span> {node.textbook_mapping.canhdieu}</div>
                    <div>🌅 <span className="text-[#2ce8f5] font-bold">CTST:</span> {node.textbook_mapping.ctst}</div>
                  </div>
                )}

                {selectedBook === 'kntt' && node.textbook_mapping?.kntt && (
                  <div className="mt-3 bg-[#193c3e] border-2 border-[#38b764] p-2 text-xs font-bold text-[#a7f070]">
                    📖 Kết nối tri thức: {node.textbook_mapping.kntt}
                  </div>
                )}

                {selectedBook === 'canhdieu' && node.textbook_mapping?.canhdieu && (
                  <div className="mt-3 bg-[#3e2731] border-2 border-[#f77622] p-2 text-xs font-bold text-[#fee761]">
                    🪁 Cánh Diều: {node.textbook_mapping.canhdieu}
                  </div>
                )}

                {selectedBook === 'ctst' && node.textbook_mapping?.ctst && (
                  <div className="mt-3 bg-[#1f3b5c] border-2 border-[#2ce8f5] p-2 text-xs font-bold text-[#2ce8f5]">
                    🌅 Chân trời sáng tạo: {node.textbook_mapping.ctst}
                  </div>
                )}
              </div>

              {/* Footer thẻ: Khuôn game & Nút vào học */}
              <div className="mt-4 pt-3 border-t border-[#3a4466] flex items-center justify-between">
                <div className="flex items-center gap-1.5 text-xs text-[#8b9bb4]">
                  <span className="bg-[#181425] border border-[#5a6988] px-1.5 py-0.5 text-[10px] font-mono text-[#2ce8f5]">
                    {node.template}
                  </span>
                  <span className="flex items-center gap-0.5 text-[10px]">
                    <Clock size={11} /> {node.estimated_minutes}p
                  </span>
                </div>

                {isLocked ? (
                  <div className="flex items-center gap-1 text-xs text-[#8b9bb4]">
                    <Lock size={14} /> Khóa
                  </div>
                ) : (
                  <PixelButton
                    variant={isCompleted ? 'ghost' : 'primary'}
                    size="sm"
                    onClick={() => {
                      sound.playClick();
                      onSelectNode(node);
                    }}
                  >
                    {isCompleted ? 'Ôn lại' : 'Bắt đầu'} <Play size={12} />
                  </PixelButton>
                )}
              </div>
            </PixelCard>
          );
        })}
      </div>

      {filteredNodes.length === 0 && (
        <div className="text-center py-12 bg-[#262b44] border-2 border-[#3a4466] p-6">
          <BookOpen size={40} className="mx-auto text-[#5a6988] mb-2" />
          <div className="font-bold text-base text-white">Chưa có bài học cho lớp này</div>
          <div className="text-xs text-[#8b9bb4] mt-1">
            Nội dung đang được mở rộng tuần tự theo lộ trình GDPT 2018.
          </div>
        </div>
      )}
    </div>
  );
};

