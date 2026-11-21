import React, { useState, useRef, useEffect } from 'react';
import { Grade, CurriculumNode } from '../../packages/domain/types';
import { useI18n } from '../i18nContext';
import { sound } from '../../packages/game-core/audio';
import { BookOpen, ChevronDown, Check, RotateCcw } from 'lucide-react';

export type TextbookFilterId = 'all' | 'kntt' | 'canhdieu' | 'ctst';

export interface TextbookOption {
  id: TextbookFilterId;
  name: string;
  fullName: string;
  publisher: string;
  icon: string;
  count: number;
}

interface TextbookSelectorProps {
  selectedBook: TextbookFilterId;
  onSelectBook: (id: TextbookFilterId) => void;
  selectedGrade: Grade;
  nodes: CurriculumNode[];
  isLight: boolean;
}

export const TextbookSelector: React.FC<TextbookSelectorProps> = ({
  selectedBook,
  onSelectBook,
  selectedGrade,
  nodes,
  isLight,
}) => {
  const { t } = useI18n();
  const [isOpen, setIsOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  const nodesInGrade = nodes.filter((n) => n.grade === selectedGrade);
  const totalCount = nodesInGrade.length;
  const knttCount = nodesInGrade.filter((n) => !!n.textbook_mapping?.kntt).length;
  const canhdieuCount = nodesInGrade.filter((n) => !!n.textbook_mapping?.canhdieu).length;
  const ctstCount = nodesInGrade.filter((n) => !!n.textbook_mapping?.ctst).length;

  const options: TextbookOption[] = [
    {
      id: 'all',
      name: t('filter_all'),
      fullName: t('textbook_list_all'),
      publisher: t('textbook_list_all_desc'),
      icon: '📚',
      count: totalCount,
    },
    {
      id: 'kntt',
      name: t('filter_kntt'),
      fullName: t('textbook_list_kntt'),
      publisher: t('textbook_list_kntt_desc'),
      icon: '📗',
      count: knttCount,
    },
    {
      id: 'canhdieu',
      name: t('filter_canhdieu'),
      fullName: t('textbook_list_canhdieu'),
      publisher: t('textbook_list_canhdieu_desc'),
      icon: '📙',
      count: canhdieuCount,
    },
    {
      id: 'ctst',
      name: t('filter_ctst'),
      fullName: t('textbook_list_ctst'),
      publisher: t('textbook_list_ctst_desc'),
      icon: '📘',
      count: ctstCount,
    },
  ];

  const currentOption = options.find((o) => o.id === selectedBook) || options[0];

  // Close dropdown on outside click or Escape key
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    };

    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        setIsOpen(false);
      }
    };

    if (isOpen) {
      document.addEventListener('mousedown', handleClickOutside);
      document.addEventListener('keydown', handleKeyDown);
    }
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, [isOpen]);

  const handleToggle = () => {
    sound.playClick();
    setIsOpen((prev) => !prev);
  };

  const handleSelect = (id: TextbookFilterId) => {
    sound.playClick();
    onSelectBook(id);
    setIsOpen(false);
  };

  return (
    <div
      className={`border-2 w-full p-3 transition-colors ${
        isLight ? 'bg-white border-[#cbd5e1] shadow-pixel-sm' : 'bg-[#1f2438] border-[#3a4466]'
      }`}
    >
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-3">
        {/* Tiêu đề & Thông điệp sư phạm */}
        <div className="flex items-center gap-2.5">
          <div
            className={`w-7 h-7 flex items-center justify-center border ${
              isLight
                ? 'bg-[#fef3c7] border-[#f59e0b] text-[#b45309]'
                : 'bg-[#2a2744] border-[#fee761] text-[#fee761]'
            }`}
          >
            <BookOpen size={15} />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className={`text-xs font-bold uppercase tracking-wider ${
                isLight ? 'text-[#1e293b]' : 'text-[#f1f5f9]'
              }`}>
                {t('textbook_list_heading')}
              </span>
              <span className={`text-[10px] px-1.5 py-0.2 font-mono font-bold border ${
                isLight
                  ? 'bg-[#f1f5f9] text-[#475569] border-[#cbd5e1]'
                  : 'bg-[#181425] text-[#8b9bb4] border-[#3a4466]'
              }`}>
                Lớp {selectedGrade}
              </span>
            </div>
            <p className={`text-[11px] leading-tight mt-0.5 ${
              isLight ? 'text-[#64748b]' : 'text-[#8b9bb4]'
            }`}>
              {t('textbook_list_select_hint')} ({currentOption.count} {t('textbook_list_matched')})
            </p>
          </div>
        </div>

        {/* Hộp chọn Danh sách (Dropdown List Selector) */}
        <div className="relative flex items-center gap-2" ref={dropdownRef}>
          {/* Nút bấm mở danh sách (Trigger) */}
          <button
            type="button"
            onClick={handleToggle}
            aria-expanded={isOpen}
            aria-haspopup="listbox"
            className={`flex items-center justify-between gap-3 px-3.5 py-2 min-w-[280px] sm:min-w-[340px] text-xs font-bold font-mono transition-all border-2 cursor-pointer select-none ${
              isOpen
                ? isLight
                  ? 'bg-[#fef08a] text-[#713f12] border-[#ca8a04] shadow-pixel-sm'
                  : 'bg-[#262b44] text-[#fee761] border-[#fee761] shadow-pixel-sm'
                : isLight
                ? 'bg-[#f8fafc] text-[#1e293b] border-[#cbd5e1] hover:border-[#94a3b8]'
                : 'bg-[#181425] text-[#f1f5f9] border-[#3a4466] hover:border-[#fee761]'
            }`}
          >
            <div className="flex items-center gap-2 truncate">
              <span className="text-sm select-none">{currentOption.icon}</span>
              <span className="truncate">{currentOption.fullName}</span>
            </div>

            <div className="flex items-center gap-2 shrink-0">
              <span
                className={`text-[10px] px-1.5 py-0.5 font-bold border ${
                  isLight
                    ? 'bg-[#e2e8f0] text-[#334155] border-[#cbd5e1]'
                    : 'bg-[#262b44] text-[#fee761] border-[#3a4466]'
                }`}
              >
                {currentOption.count} bài
              </span>
              <ChevronDown
                size={14}
                className={`transition-transform duration-200 ${
                  isOpen ? 'rotate-180 text-[#fee761]' : ''
                }`}
              />
            </div>
          </button>

          {/* Nút reset nhanh nếu đang chọn 1 bộ sách riêng lẻ */}
          {selectedBook !== 'all' && (
            <button
              type="button"
              onClick={() => handleSelect('all')}
              title="Xem tất cả bộ SGK"
              className={`p-2 border-2 cursor-pointer transition-colors ${
                isLight
                  ? 'bg-[#f8fafc] border-[#cbd5e1] text-[#475569] hover:bg-[#e2e8f0]'
                  : 'bg-[#181425] border-[#3a4466] text-[#8b9bb4] hover:text-[#fee761] hover:border-[#fee761]'
              }`}
            >
              <RotateCcw size={14} />
            </button>
          )}

          {/* Menu Danh Sách Thả Xuống (Dropdown List) */}
          {isOpen && (
            <div
              role="listbox"
              className={`absolute right-0 top-full mt-1.5 w-full sm:w-[420px] max-w-[95vw] border-2 z-40 p-2 shadow-pixel-lg anim-pixel-pop-in ${
                isLight ? 'bg-white border-[#94a3b8]' : 'bg-[#1f2438] border-[#fee761]'
              }`}
            >
              <div
                className={`px-2 py-1 mb-1.5 text-[10px] font-bold font-mono tracking-wider uppercase border-b ${
                  isLight
                    ? 'text-[#64748b] border-[#e2e8f0]'
                    : 'text-[#8b9bb4] border-[#3a4466]'
                }`}
              >
                DANH SÁCH BỘ SÁCH GIÁO KHOA TIN HỌC
              </div>

              <div className="space-y-1">
                {options.map((opt) => {
                  const isSelected = selectedBook === opt.id;
                  return (
                    <div
                      key={opt.id}
                      role="option"
                      aria-selected={isSelected}
                      onClick={() => handleSelect(opt.id)}
                      className={`flex items-center justify-between p-2.5 border transition-all cursor-pointer select-none ${
                        isSelected
                          ? isLight
                            ? 'bg-[#fef9c3] border-[#ca8a04] text-[#713f12] shadow-pixel-xs'
                            : 'bg-[#2a2d48] border-[#fee761] text-white shadow-pixel-xs'
                          : isLight
                          ? 'bg-[#f8fafc] border-[#e2e8f0] text-[#334155] hover:bg-[#f1f5f9] hover:border-[#cbd5e1]'
                          : 'bg-[#181425] border-[#2e3756] text-[#c0cbdc] hover:bg-[#262b44] hover:border-[#5a6988]'
                      }`}
                    >
                      <div className="flex items-center gap-2.5 truncate mr-2">
                        <span className="text-base select-none shrink-0">{opt.icon}</span>
                        <div className="truncate">
                          <div className={`text-xs font-bold truncate ${
                            isSelected
                              ? isLight ? 'text-[#854d0e]' : 'text-[#fee761]'
                              : isLight ? 'text-[#0f172a]' : 'text-[#f1f5f9]'
                          }`}>
                            {opt.fullName}
                          </div>
                          <div className={`text-[10px] truncate ${
                            isLight ? 'text-[#64748b]' : 'text-[#8b9bb4]'
                          }`}>
                            {opt.publisher}
                          </div>
                        </div>
                      </div>

                      <div className="flex items-center gap-2 shrink-0">
                        <span
                          className={`text-[10px] px-2 py-0.5 font-bold font-mono border ${
                            isSelected
                              ? isLight
                                ? 'bg-[#ca8a04] text-white border-[#a16207]'
                                : 'bg-[#fee761] text-black border-white'
                              : isLight
                              ? 'bg-[#e2e8f0] text-[#475569] border-[#cbd5e1]'
                              : 'bg-[#262b44] text-[#8b9bb4] border-[#3a4466]'
                          }`}
                        >
                          {opt.count} bài
                        </span>
                        {isSelected && (
                          <div
                            className={`w-5 h-5 flex items-center justify-center rounded-none border ${
                              isLight
                                ? 'bg-[#ca8a04] text-white border-[#a16207]'
                                : 'bg-[#fee761] text-black border-white'
                            }`}
                          >
                            <Check size={12} strokeWidth={3} />
                          </div>
                        )}
                      </div>
                    </div>
                  );
                })}
              </div>

              <div
                className={`mt-2 pt-1.5 text-[10px] text-center font-mono border-t ${
                  isLight ? 'text-[#64748b] border-[#e2e8f0]' : 'text-[#8b9bb4] border-[#3a4466]'
                }`}
              >
                💡 Hỗ trợ học sinh tự học và ôn tập kiến thức Tin học
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
