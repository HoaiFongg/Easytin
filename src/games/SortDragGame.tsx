import React, { useState } from 'react';
import { PixelButton } from '../components/PixelButton';
import { sound } from '../../packages/game-core/audio';
import { CheckCircle2, RotateCcw, Lightbulb } from 'lucide-react';

interface Group {
  id: string;
  name: string;
}

interface Item {
  id: string;
  name: string;
  group: string;
  icon?: string;
}

interface SortDragGameProps {
  config: {
    groups?: Group[];
    items?: Item[];
  };
  onComplete: (score: number) => void;
}

export const SortDragGame: React.FC<SortDragGameProps> = ({ config, onComplete }) => {
  const groups = config.groups || [
    { id: 'in', name: 'Thiết bị Vào' },
    { id: 'out', name: 'Thiết bị Ra' },
  ];
  const items = config.items || [
    { id: 'mouse', name: 'Chuột', group: 'in', icon: '🖱️' },
    { id: 'keyboard', name: 'Bàn phím', group: 'in', icon: '⌨️' },
    { id: 'monitor', name: 'Màn hình', group: 'out', icon: '🖥️' },
    { id: 'speaker', name: 'Loa', group: 'out', icon: '🔊' },
  ];

  const [selectedItemId, setSelectedItemId] = useState<string | null>(items[0]?.id || null);
  const [placements, setPlacements] = useState<Record<string, string>>({});
  const [hintCount, setHintCount] = useState(3);
  const [submitted, setSubmitted] = useState(false);
  const [feedback, setFeedback] = useState<string | null>(null);

  const handlePlace = (groupId: string) => {
    if (!selectedItemId) return;
    sound.playJump();
    setPlacements((prev) => ({
      ...prev,
      [selectedItemId]: groupId,
    }));

    // Find next unplaced item
    const nextUnplaced = items.find((it) => it.id !== selectedItemId && !placements[it.id]);
    if (nextUnplaced) {
      setSelectedItemId(nextUnplaced.id);
    }
  };

  const handleUseHint = () => {
    if (hintCount <= 0 || !selectedItemId) return;
    sound.playClick();
    const currentItem = items.find((i) => i.id === selectedItemId);
    if (currentItem) {
      setPlacements((prev) => ({
        ...prev,
        [currentItem.id]: currentItem.group,
      }));
      setHintCount((c) => c - 1);
    }
  };

  const handleReset = () => {
    sound.playClick();
    setPlacements({});
    setSelectedItemId(items[0]?.id || null);
    setSubmitted(false);
    setFeedback(null);
  };

  const handleSubmit = () => {
    let correct = 0;
    items.forEach((it) => {
      if (placements[it.id] === it.group) {
        correct++;
      }
    });

    const score = correct / items.length;
    setSubmitted(true);

    if (score >= 0.8) {
      sound.playCorrect();
      setFeedback(`Xuất sắc! Em đã xếp đúng ${correct}/${items.length} món đồ!`);
    } else {
      sound.playMistake();
      setFeedback(`Em đúng được ${correct}/${items.length}. Hãy thử bấm "Làm lại" để đạt 100% nhé!`);
    }

    onComplete(score);
  };

  const allPlaced = items.every((it) => placements[it.id]);

  return (
    <div className="flex flex-col gap-5">
      {/* Thanh công cụ */}
      <div className="flex items-center justify-between bg-[#1f2438] p-3 border-2 border-[#3a4466]">
        <div className="text-xs text-[#8b9bb4]">
          <span className="text-[#38b764] font-bold">Cách chơi:</span> Chọn món đồ bên dưới rồi bấm vào Nhóm tương ứng.
        </div>
        <div className="flex items-center gap-2">
          <PixelButton
            variant="ghost"
            size="sm"
            onClick={handleUseHint}
            disabled={hintCount <= 0 || submitted}
          >
            <Lightbulb size={14} className="text-[#feae34]" /> Gợi ý ({hintCount})
          </PixelButton>
          <PixelButton variant="ghost" size="sm" onClick={handleReset}>
            <RotateCcw size={14} /> Làm lại
          </PixelButton>
        </div>
      </div>

      {/* Danh sách các nhóm đích */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {groups.map((group) => {
          const placedInThisGroup = items.filter((it) => placements[it.id] === group.id);
          return (
            <div
              key={group.id}
              onClick={() => !submitted && handlePlace(group.id)}
              className="border-3 border-dashed border-[#5a6988] bg-[#1a1c2c] p-4 min-h-[160px] flex flex-col justify-between cursor-pointer hover:border-[#38b764] transition-colors"
            >
              <div className="flex items-center justify-between border-b border-[#3a4466] pb-2 mb-3">
                <span className="font-pixel text-xs text-[#fee761]">{group.name}</span>
                <span className="text-xs text-[#8b9bb4]">{placedInThisGroup.length} món</span>
              </div>

              {/* Items placed in this group */}
              <div className="flex flex-wrap gap-2">
                {placedInThisGroup.map((it) => (
                  <div
                    key={it.id}
                    className="flex items-center gap-1.5 bg-[#262b44] border-2 border-[#5a6988] px-2.5 py-1 text-xs text-white"
                  >
                    <span>{it.icon || '📦'}</span>
                    <span className="font-semibold">{it.name}</span>
                    {submitted && (
                      <span className="text-xs ml-1">
                        {it.group === group.id ? '✅' : '❌'}
                      </span>
                    )}
                  </div>
                ))}
                {placedInThisGroup.length === 0 && (
                  <div className="text-xs text-[#5a6988] italic py-6 text-center w-full">
                    Bấm vào đây để xếp món đang chọn vào nhóm này
                  </div>
                )}
              </div>

              {!submitted && (
                <div className="mt-2 text-right">
                  <span className="text-[10px] text-[#38b764] uppercase font-bold">
                    + Xếp vào nhóm này
                  </span>
                </div>
              )}
            </div>
          );
        })}
      </div>

      {/* Khay đồ vật cần xếp */}
      <div>
        <div className="text-xs font-pixel text-[#8b9bb4] mb-2">ĐỒ VẬT CẦN PHÂN LOẠI:</div>
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
          {items.map((it) => {
            const isPlaced = !!placements[it.id];
            const isSelected = selectedItemId === it.id;
            return (
              <div
                key={it.id}
                onClick={() => {
                  if (!submitted) {
                    sound.playClick();
                    setSelectedItemId(it.id);
                  }
                }}
                className={`p-2.5 border-2 cursor-pointer flex items-center gap-2 transition-all ${
                  isSelected
                    ? 'border-[#fee761] bg-[#3a4466] -translate-y-1 shadow-pixel'
                    : isPlaced
                    ? 'border-[#3a4466] bg-[#1a1c2c] opacity-60'
                    : 'border-[#5a6988] bg-[#262b44] hover:border-[#8b9bb4]'
                }`}
              >
                <span className="text-xl">{it.icon || '📦'}</span>
                <div className="flex-1 min-w-0">
                  <div className="text-xs font-bold truncate">{it.name}</div>
                  <div className="text-[10px] text-[#8b9bb4]">
                    {isPlaced ? 'Đã xếp' : 'Chưa xếp'}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Nút nộp bài & Kết quả */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-3 pt-2">
        {feedback && (
          <div className="text-xs font-bold text-[#fee761] bg-[#1f2438] px-3 py-2 border border-[#feae34]">
            {feedback}
          </div>
        )}
        <div className="ml-auto">
          <PixelButton
            variant="primary"
            size="md"
            onClick={handleSubmit}
            disabled={!allPlaced || submitted}
          >
            <CheckCircle2 size={16} /> Kiểm tra kết quả
          </PixelButton>
        </div>
      </div>
    </div>
  );
};
