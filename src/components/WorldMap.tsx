import React, { useState } from 'react';
import { CurriculumNode, CurriculumWorld, Grade, NodeMasteryRecord } from '../../packages/domain/types';
import { AccountManager, AVATAR_OPTIONS } from '../../packages/domain/account';
import { useI18n } from '../i18nContext';
import { useTheme } from '../ThemeContext';
import { PixelCard } from './PixelCard';
import { PixelButton } from './PixelButton';
import { PixelMascot } from './PixelMascot';
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
  const { t } = useI18n();
  const { effectiveTheme } = useTheme();
  const isLight = effectiveTheme === 'light';
  const [selectedBook, setSelectedBook] = useState<'all' | 'kntt' | 'canhdieu' | 'ctst'>('all');

  const isElementary = [3, 4, 5].includes(selectedGrade);
  const isMiddleSchool = [6, 7, 8, 9].includes(selectedGrade);
  const isHighSchool = [10, 11, 12].includes(selectedGrade);

  const activeAccount = AccountManager.getActiveAccount();
  const currentMascotId = activeAccount?.avatarId || 'tin_bot';
  const currentMascot = AVATAR_OPTIONS.find((a) => a.id === currentMascotId) || AVATAR_OPTIONS[0];

  const currentLevelLabel = isElementary
    ? t('level_elementary_full')
    : isMiddleSchool
    ? t('level_middle_full')
    : t('level_high_full');

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
    <div className="flex flex-col gap-6 w-full anim-pixel-fade-up">
      {/* KHỐI ĐIỀU HƯỚNG CẤP HỌC & KHỐI LỚP PHỔ THÔNG (Tiểu học · THCS · THPT) */}
      <div className={`border-3 p-3 sm:p-5 shadow-pixel flex flex-col gap-4 w-full transition-colors ${
        isLight
          ? 'bg-white border-[#cbd5e1]'
          : 'bg-[#181425] border-[#3a4466]'
      }`}>
        {/* Hàng 1: CHỌN CẤP HỌC */}
        <div className="w-full">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-2.5">
            <div className="flex items-center gap-2">
              <GraduationCap className={isLight ? 'text-[#b45309]' : 'text-[#fee761]'} size={18} />
              <span className={`text-xs font-black uppercase tracking-wider ${
                isLight ? 'text-[#b45309]' : 'text-[#fee761]'
              }`}>
                CHỌN BẬC CẤP HỌC (GDPT 2018):
              </span>
            </div>
            <span className={`text-[11px] ${isLight ? 'text-[#64748b]' : 'text-[#8b9bb4]'}`}>
              Đang chọn: <strong className={isLight ? 'text-[#047857]' : 'text-[#fee761]'}>{currentLevelLabel}</strong>
            </span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-3 sm:gap-4 w-full">
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
                  ? isLight
                    ? 'bg-[#ecfdf5] border-[#10b981] shadow-pixel -translate-y-0.5'
                    : 'bg-[#2b5c3f] border-[#38b764] shadow-pixel -translate-y-0.5'
                  : isLight
                  ? 'bg-white border-[#cbd5e1] hover:border-[#94a3b8] hover:-translate-y-0.5 shadow-pixel-sm'
                  : 'bg-[#1a1c2c] border-[#3a4466] hover:border-[#5a6988]'
              }`}
            >
              <div className="flex items-center justify-between">
                <span className="text-2xl">🎒</span>
                <span className={`text-[10px] font-bold px-2 py-0.5 border ${
                  isElementary
                    ? isLight
                      ? 'bg-white text-[#047857] border-[#6ee7b7]'
                      : 'text-[#a7f070] bg-[#181425] border-[#2b5c3f]'
                    : isLight
                    ? 'bg-[#f1f5f9] text-[#475569] border-[#cbd5e1]'
                    : 'text-[#a7f070] bg-[#181425] border-[#2b5c3f]'
                }`}>
                  {t('grade_prefix')} 3 – 5
                </span>
              </div>
              <div className={`font-black text-sm mt-1.5 uppercase ${
                isElementary
                  ? isLight ? 'text-[#064e3b]' : 'text-white'
                  : isLight ? 'text-[#0f172a]' : 'text-white'
              }`}>
                {t('level_elementary_full')}
              </div>
              <div className={`text-[11px] mt-0.5 ${
                isElementary
                  ? isLight ? 'text-[#047857]' : 'text-[#c0cbdc]'
                  : isLight ? 'text-[#64748b]' : 'text-[#c0cbdc]'
              }`}>
                {t('world_valley')} · 43 {t('lessons_suffix')}
              </div>
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
                  ? isLight
                    ? 'bg-[#eff6ff] border-[#3b82f6] shadow-pixel -translate-y-0.5'
                    : 'bg-[#1f3b5c] border-[#2ce8f5] shadow-pixel -translate-y-0.5'
                  : isLight
                  ? 'bg-white border-[#cbd5e1] hover:border-[#94a3b8] hover:-translate-y-0.5 shadow-pixel-sm'
                  : 'bg-[#1a1c2c] border-[#3a4466] hover:border-[#5a6988]'
              }`}
            >
              <div className="flex items-center justify-between">
                <span className="text-2xl">🌲</span>
                <span className={`text-[10px] font-bold px-2 py-0.5 border ${
                  isMiddleSchool
                    ? isLight
                      ? 'bg-white text-[#1d4ed8] border-[#93c5fd]'
                      : 'text-[#2ce8f5] bg-[#181425] border-[#1f3b5c]'
                    : isLight
                    ? 'bg-[#f1f5f9] text-[#475569] border-[#cbd5e1]'
                    : 'text-[#2ce8f5] bg-[#181425] border-[#1f3b5c]'
                }`}>
                  {t('grade_prefix')} 6 – 9
                </span>
              </div>
              <div className={`font-black text-sm mt-1.5 uppercase ${
                isMiddleSchool
                  ? isLight ? 'text-[#1e3a8a]' : 'text-white'
                  : isLight ? 'text-[#0f172a]' : 'text-white'
              }`}>
                {t('level_middle_full')}
              </div>
              <div className={`text-[11px] mt-0.5 ${
                isMiddleSchool
                  ? isLight ? 'text-[#2563eb]' : 'text-[#c0cbdc]'
                  : isLight ? 'text-[#64748b]' : 'text-[#c0cbdc]'
              }`}>
                {t('world_forest')} · 50 {t('lessons_suffix')}
              </div>
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
                  ? isLight
                    ? 'bg-[#fdf2f8] border-[#ec4899] shadow-pixel -translate-y-0.5'
                    : 'bg-[#5c2b4e] border-[#fca3ca] shadow-pixel -translate-y-0.5'
                  : isLight
                  ? 'bg-white border-[#cbd5e1] hover:border-[#94a3b8] hover:-translate-y-0.5 shadow-pixel-sm'
                  : 'bg-[#1a1c2c] border-[#3a4466] hover:border-[#5a6988]'
              }`}
            >
              <div className="flex items-center justify-between">
                <span className="text-2xl">🏛️</span>
                <span className={`text-[10px] font-bold px-2 py-0.5 border ${
                  isHighSchool
                    ? isLight
                      ? 'bg-white text-[#be185d] border-[#f472b6]'
                      : 'text-[#fca3ca] bg-[#181425] border-[#5c2b4e]'
                    : isLight
                    ? 'bg-[#f1f5f9] text-[#475569] border-[#cbd5e1]'
                    : 'text-[#fca3ca] bg-[#181425] border-[#5c2b4e]'
                }`}>
                  {t('grade_prefix')} 10 – 12
                </span>
              </div>
              <div className={`font-black text-sm mt-1.5 uppercase ${
                isHighSchool
                  ? isLight ? 'text-[#831843]' : 'text-white'
                  : isLight ? 'text-[#0f172a]' : 'text-white'
              }`}>
                {t('level_high_full')}
              </div>
              <div className={`text-[11px] mt-0.5 ${
                isHighSchool
                  ? isLight ? 'text-[#db2777]' : 'text-[#c0cbdc]'
                  : isLight ? 'text-[#64748b]' : 'text-[#c0cbdc]'
              }`}>
                {t('world_city')} · 44 {t('lessons_suffix')}
              </div>
            </button>
          </div>
        </div>

        {/* Hàng 2: CHỌN KHỐI LỚP TRONG CẤP HỌC ĐÃ CHỌN */}
        <div className={`pt-3 border-t-2 flex flex-col lg:flex-row lg:items-center justify-between gap-3 w-full ${
          isLight ? 'border-[#e2e8f0]' : 'border-[#262b44]'
        }`}>
          <div className={`text-xs font-bold flex items-center gap-1.5 shrink-0 ${
            isLight ? 'text-[#334155]' : 'text-[#c0cbdc]'
          }`}>
            <span>📚</span>
            <span>CHỌN KHỐI LỚP TRONG {currentLevelLabel.toUpperCase()}:</span>
          </div>

          <div className="grid grid-cols-3 sm:flex sm:flex-wrap items-center gap-2 w-full lg:w-auto">
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
                      ? isLight
                        ? 'bg-[#fef08a] text-[#713f12] border-[#ca8a04] shadow-pixel -translate-y-0.5'
                        : 'bg-[#fee761] text-[#181425] border-white shadow-pixel -translate-y-0.5'
                      : isLight
                      ? 'bg-white text-[#334155] border-[#cbd5e1] hover:border-[#94a3b8]'
                      : 'bg-[#262b44] text-[#c0cbdc] border-[#5a6988] hover:border-white'
                  }`}
                >
                  <span className="text-sm">{t('grade_prefix')} {g}</span>
                  <span
                    className={`text-[10px] px-1.5 py-0.5 font-bold border ${
                      isSelected
                        ? isLight
                          ? 'bg-[#ca8a04] text-white border-[#a16207]'
                          : 'bg-black/20 border-black/30 text-black'
                        : isLight
                        ? 'bg-[#f1f5f9] border-[#e2e8f0] text-[#64748b]'
                        : 'bg-[#181425] border-[#3a4466] text-[#8b9bb4]'
                    }`}
                  >
                    {count} {t('lessons_suffix')}
                  </span>
                </button>
              );
            })}
          </div>
        </div>
      </div>

      {/* Banner Thế giới */}
      <div
        className={`p-5 border-4 shadow-pixel relative overflow-hidden transition-all ${
          isLight
            ? isElementary
              ? 'bg-[#ecfdf5] border-[#10b981]'
              : isMiddleSchool
              ? 'bg-[#eff6ff] border-[#3b82f6]'
              : 'bg-[#fdf2f8] border-[#ec4899]'
            : 'border-[#3a4466]'
        }`}
        style={!isLight ? { backgroundColor: currentWorld.color_theme } : undefined}
      >
        <div className="relative z-10 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div>
            <div className={`text-xs font-black uppercase tracking-wider ${
              isLight
                ? isElementary
                  ? 'text-[#047857]'
                  : isMiddleSchool
                  ? 'text-[#1d4ed8]'
                  : 'text-[#be185d]'
                : 'text-[#fee761]'
            }`}>
              {currentWorld.name} · {currentLevelLabel}
            </div>
            <h1 className={`text-xl md:text-2xl font-black mt-1 ${
              isLight
                ? isElementary
                  ? 'text-[#064e3b]'
                  : isMiddleSchool
                  ? 'text-[#1e3a8a]'
                  : 'text-[#831843]'
                : 'text-white'
            }`}>
              {t('curriculum_title')} {selectedGrade} ({nodes.filter((n) => n.grade === selectedGrade).length} {t('lessons_count')})
            </h1>
            <p className={`text-xs max-w-4xl mt-1 leading-relaxed ${
              isLight
                ? isElementary
                  ? 'text-[#065f46]'
                  : isMiddleSchool
                  ? 'text-[#1e40af]'
                  : 'text-[#9d174d]'
                : 'text-[#c0cbdc]'
            }`}>
              {currentWorld.description}
            </p>
          </div>
          <div className={`flex items-center gap-2 p-2 border-2 shrink-0 ${
            isLight
              ? isElementary
                ? 'bg-white/95 border-[#a7f3d0]'
                : isMiddleSchool
                ? 'bg-white/95 border-[#bfdbfe]'
                : 'bg-white/95 border-[#fbcfe8]'
              : 'bg-[#181425]/80 border-[#5a6988]'
          }`}>
            <span className={`text-xs ${isLight ? 'text-[#475569]' : 'text-[#8b9bb4]'}`}>Độ phủ SGK:</span>
            <span className={`text-xs font-bold ${
              isLight
                ? isElementary
                  ? 'text-[#047857]'
                  : isMiddleSchool
                  ? 'text-[#1d4ed8]'
                  : 'text-[#be185d]'
                : 'text-[#38b764]'
            }`}>KNTT · Cánh Diều · CTST</span>
          </div>
        </div>
      </div>

      {/* Linh vật Pixel Đồng hành (Interactive Mascot Companion) */}
      <div className={`p-3 sm:p-4 shadow-pixel flex items-center gap-3 sm:gap-4 relative overflow-hidden w-full border-3 ${
        isLight
          ? 'bg-[#fffbeb] border-[#f59e0b]'
          : 'bg-[#1f2438] border-[#fee761]'
      }`}>
        <div
          className={`w-14 h-14 sm:w-16 sm:h-16 border-2 flex items-center justify-center p-1 shadow-pixel-sm shrink-0 cursor-pointer hover:scale-105 transition-transform ${
            isLight
              ? 'bg-white border-[#f59e0b]'
              : 'bg-[#181425] border-[#fee761]'
          }`}
          onClick={() => sound.playJump()}
          title="Nhấp để cổ vũ linh vật!"
        >
          <PixelMascot mascotId={currentMascotId} size={48} animated={true} />
        </div>
        <div className="flex-1">
          <div className="flex items-center gap-2 flex-wrap">
            <span className={`text-xs font-black uppercase tracking-wider ${
              isLight ? 'text-[#92400e]' : 'text-[#fee761]'
            }`}>
              {currentMascot.name} ({currentMascot.role}):
            </span>
            <span className={`text-[10px] px-2 py-0.5 font-bold border animate-pulse ${
              isLight
                ? 'bg-[#dcfce7] text-[#166534] border-[#86efac]'
                : 'bg-[#1a2e22] text-[#38b764] border-[#2b5c3f]'
            }`}>
              Đồng hành cùng em
            </span>
          </div>
          <div className={`text-xs mt-1 leading-relaxed ${
            isLight ? 'text-[#78350f]' : 'text-[#c0cbdc]'
          }`}>
            "Chào bạn nhỏ! Mỗi bài học Tin học hôm nay là một bước tiến rèn luyện tư duy số. Hãy hoàn thành tốt nhé!"
          </div>
        </div>
      </div>

      {/* Bộ chọn Bộ Sách Giáo Khoa */}
      <div className={`flex flex-wrap items-center justify-between gap-3 p-3 border-2 w-full ${
        isLight ? 'bg-white border-[#cbd5e1] shadow-pixel-sm' : 'bg-[#1f2438] border-[#3a4466]'
      }`}>
        <div className="flex items-center gap-2">
          <BookOpen size={16} className={isLight ? 'text-[#b45309]' : 'text-[#fee761]'} />
          <span className={`text-xs font-bold ${isLight ? 'text-[#334155]' : 'text-[#c0cbdc]'}`}>
            Lọc theo bộ sách giáo khoa:
          </span>
        </div>
        <div className="flex flex-wrap items-center gap-2">
          {[
            { id: 'all', label: t('filter_all') },
            { id: 'kntt', label: t('filter_kntt') },
            { id: 'canhdieu', label: t('filter_canhdieu') },
            { id: 'ctst', label: t('filter_ctst') },
          ].map((b) => {
            const isSelected = selectedBook === b.id;
            return (
              <button
                key={b.id}
                onClick={() => {
                  sound.playClick();
                  setSelectedBook(b.id as 'all' | 'kntt' | 'canhdieu' | 'ctst');
                }}
                className={`px-3 py-1 text-xs font-bold transition-all border-2 cursor-pointer ${
                  isSelected
                    ? isLight
                      ? 'bg-[#fef08a] text-[#713f12] border-[#ca8a04] shadow-pixel-sm -translate-y-0.5'
                      : 'bg-[#fee761] text-black border-white shadow-pixel-sm -translate-y-0.5'
                    : isLight
                    ? 'bg-[#f8fafc] text-[#475569] border-[#cbd5e1] hover:border-[#94a3b8]'
                    : 'bg-[#262b44] text-[#c0cbdc] border-[#5a6988] hover:border-white'
                }`}
              >
                {b.label}
              </button>
            );
          })}
        </div>
      </div>

      {/* Danh sách các bài học dạng Bản đồ Phiêu lưu */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-5 gap-4 sm:gap-5 w-full">
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
              className={`flex flex-col justify-between relative transition-all hover-pixel-lift h-full ${
                isLocked ? 'opacity-60 cursor-not-allowed' : ''
              } ${isLight ? 'bg-white shadow-pixel-sm hover:shadow-pixel' : ''}`}
            >
              <div className="flex flex-col flex-1">
                {/* Header thẻ bài học */}
                <div className={`flex items-center justify-between border-b pb-2 mb-2.5 h-7 ${
                  isLight ? 'border-[#e2e8f0]' : 'border-[#3a4466]'
                }`}>
                  <span className={`text-xs font-black uppercase tracking-wider ${
                    isLight ? 'text-[#b45309]' : 'text-[#fee761]'
                  }`}>
                    Bài {index + 1}
                  </span>
                  <div className="flex items-center gap-1">
                    {Array.from({ length: 3 }).map((_, s) => (
                      <Star
                        key={s}
                        size={14}
                        className={
                          s < stars
                            ? `text-[#f59e0b] fill-[#f59e0b] ${stars === 3 ? 'anim-shimmer-star' : ''}`
                            : isLight
                            ? 'text-[#cbd5e1]'
                            : 'text-[#3a4466]'
                        }
                      />
                    ))}
                  </div>
                </div>

                {/* Tiêu đề: Khóa cố định chiều cao 2 dòng (h-11 sm:h-12 line-clamp-2) để 100% thẻ đều ngay hàng thẳng lối */}
                <h3
                  className={`font-bold text-sm sm:text-base leading-snug line-clamp-2 h-11 sm:h-12 flex items-start ${
                    isLight ? 'text-[#0f172a]' : 'text-white'
                  }`}
                  title={node.title}
                >
                  {node.title}
                </h3>

                {/* Mạch nội dung (Chuẩn GDPT 2018): Khóa cố định 1 dòng h-5 */}
                <div className={`text-[11px] mt-1 h-5 line-clamp-1 flex items-center ${
                  isLight ? 'text-[#64748b]' : 'text-[#8b9bb4]'
                }`}>
                  {node.standard_domain}
                </div>

                {/* Khung sách đối chiếu: Cố định độ cao và căn chỉnh dòng thẳng thớm */}
                <div className="mt-2.5 flex-1 flex flex-col justify-end">
                  {selectedBook === 'all' && node.textbook_mapping && (
                    <div className={`p-2 border text-[10px] flex flex-col justify-center gap-0.5 min-h-[64px] ${
                      isLight
                        ? 'bg-[#f8fafc] border-[#e2e8f0] text-[#334155]'
                        : 'bg-[#181425] border-[#3a4466] text-[#c0cbdc]'
                    }`}>
                      <div className="truncate">📖 <span className={isLight ? 'text-[#16a34a] font-bold' : 'text-[#38b764] font-bold'}>KNTT:</span> {node.textbook_mapping.kntt}</div>
                      <div className="truncate">🪁 <span className={isLight ? 'text-[#d97706] font-bold' : 'text-[#feae34] font-bold'}>Cánh Diều:</span> {node.textbook_mapping.canhdieu}</div>
                      <div className="truncate">🌅 <span className={isLight ? 'text-[#0284c7] font-bold' : 'text-[#2ce8f5] font-bold'}>CTST:</span> {node.textbook_mapping.ctst}</div>
                    </div>
                  )}

                  {selectedBook === 'kntt' && node.textbook_mapping?.kntt && (
                    <div className={`border-2 p-2 text-xs font-bold min-h-[46px] flex items-center ${
                      isLight
                        ? 'bg-[#f0fdf4] border-[#86efac] text-[#166534]'
                        : 'bg-[#193c3e] border-[#38b764] text-[#a7f070]'
                    }`}>
                      <span className="line-clamp-2">📖 Kết nối tri thức: {node.textbook_mapping.kntt}</span>
                    </div>
                  )}

                  {selectedBook === 'canhdieu' && node.textbook_mapping?.canhdieu && (
                    <div className={`border-2 p-2 text-xs font-bold min-h-[46px] flex items-center ${
                      isLight
                        ? 'bg-[#fff7ed] border-[#fdba74] text-[#9a3412]'
                        : 'bg-[#3e2731] border-[#f77622] text-[#fee761]'
                    }`}>
                      <span className="line-clamp-2">🪁 Cánh Diều: {node.textbook_mapping.canhdieu}</span>
                    </div>
                  )}

                  {selectedBook === 'ctst' && node.textbook_mapping?.ctst && (
                    <div className={`border-2 p-2 text-xs font-bold min-h-[46px] flex items-center ${
                      isLight
                        ? 'bg-[#f0f9ff] border-[#7dd3fc] text-[#0369a1]'
                        : 'bg-[#1f3b5c] border-[#2ce8f5] text-[#2ce8f5]'
                    }`}>
                      <span className="line-clamp-2">🌅 Chân trời sáng tạo: {node.textbook_mapping.ctst}</span>
                    </div>
                  )}
                </div>
              </div>

              {/* Footer thẻ: Khuôn game & Nút vào học */}
              <div className={`mt-3 pt-2.5 border-t flex items-center justify-between ${
                isLight ? 'border-[#e2e8f0]' : 'border-[#3a4466]'
              }`}>
                <div className={`flex items-center gap-1.5 text-xs ${
                  isLight ? 'text-[#64748b]' : 'text-[#8b9bb4]'
                }`}>
                  <span className={`px-1.5 py-0.5 text-[10px] font-mono border ${
                    isLight
                      ? 'bg-[#f1f5f9] border-[#cbd5e1] text-[#0284c7]'
                      : 'bg-[#181425] border-[#5a6988] text-[#2ce8f5]'
                  }`}>
                    {node.template}
                  </span>
                  <span className="flex items-center gap-0.5 text-[10px]">
                    <Clock size={11} /> {node.estimated_minutes}p
                  </span>
                </div>

                {isLocked ? (
                  <div className={`flex items-center gap-1 text-xs ${isLight ? 'text-[#94a3b8]' : 'text-[#8b9bb4]'}`}>
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
        <div className={`text-center py-12 border-2 p-6 ${
          isLight
            ? 'bg-white border-[#cbd5e1] text-[#0f172a]'
            : 'bg-[#262b44] border-[#3a4466] text-white'
        }`}>
          <BookOpen size={40} className={`mx-auto mb-2 ${isLight ? 'text-[#94a3b8]' : 'text-[#5a6988]'}`} />
          <div className="font-bold text-base">Chưa có bài học cho lớp này</div>
          <div className={`text-xs mt-1 ${isLight ? 'text-[#64748b]' : 'text-[#8b9bb4]'}`}>
            Nội dung đang được mở rộng tuần tự theo lộ trình GDPT 2018.
          </div>
        </div>
      )}
    </div>
  );
};

