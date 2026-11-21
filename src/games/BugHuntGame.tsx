import React, { useState } from 'react';
import { PixelButton } from '../components/PixelButton';
import { sound } from '../../packages/game-core/audio';
import { Bug, CheckCircle2 } from 'lucide-react';

interface CodeLine {
  lineNum: number;
  code: string;
  isBug: boolean;
  correction: string;
}

const DEFAULT_CODE: CodeLine[] = [
  { lineNum: 1, code: 'tong = 0', isBug: false, correction: '' },
  { lineNum: 2, code: 'for i in range(1, 6):', isBug: false, correction: '' },
  { lineNum: 3, code: '    tong = tong - i  # Tính tổng từ 1 đến 5', isBug: true, correction: '    tong = tong + i' },
  { lineNum: 4, code: 'print("Tổng là:", tong)', isBug: false, correction: '' },
];

export const BugHuntGame: React.FC<{ onComplete: (score: number) => void }> = ({ onComplete }) => {
  const [codeLines, setCodeLines] = useState<CodeLine[]>(DEFAULT_CODE);
  const [selectedLine, setSelectedLine] = useState<number | null>(null);
  const [fixed, setFixed] = useState(false);

  const handleSelectLine = (lineNum: number) => {
    if (fixed) return;
    sound.playClick();
    setSelectedLine(lineNum);
  };

  const handleFixBug = () => {
    const target = codeLines.find((l) => l.lineNum === selectedLine);
    if (!target) return;

    if (target.isBug) {
      sound.playVictory();
      setFixed(true);
      setCodeLines((prev) =>
        prev.map((l) => (l.lineNum === target.lineNum ? { ...l, code: l.correction, isBug: false } : l))
      );
      onComplete(1.0);
    } else {
      sound.playMistake();
    }
  };

  return (
    <div className="flex flex-col gap-5 bg-[#1a1c2c] p-6 border-3 border-[#5a6988]">
      <div className="flex items-center justify-between border-b border-[#3a4466] pb-2">
        <div className="flex items-center gap-2">
          <Bug className="text-[#e43b44]" size={20} />
          <span className="text-xs font-black text-[#fee761] uppercase tracking-wider">TRUY TÌM DÒNG LỆNH GÂY LỖI:</span>
        </div>
        <span className="text-xs text-[#8b9bb4]">Bài toán: Tính tổng các số từ 1 đến 5</span>
      </div>

      {/* Khung Editor Code Retro */}
      <div className="bg-[#181425] border-2 border-[#3a4466] font-mono text-sm p-4 flex flex-col gap-1">
        {codeLines.map((line) => {
          const isSelected = selectedLine === line.lineNum;
          return (
            <div
              key={line.lineNum}
              onClick={() => handleSelectLine(line.lineNum)}
              className={`flex items-center gap-3 px-2 py-1 cursor-pointer transition-colors ${
                isSelected
                  ? 'bg-[#3a4466] border-l-4 border-[#fee761]'
                  : 'hover:bg-[#262b44]'
              }`}
            >
              <span className="text-[#5a6988] select-none w-6">{line.lineNum}</span>
              <span className={line.isBug ? 'text-[#f6757a]' : 'text-[#38b764]'}>
                {line.code}
              </span>
            </div>
          );
        })}
      </div>

      {/* Nút hành động */}
      <div className="flex items-center justify-between">
        <div className="text-xs text-[#8b9bb4]">
          {selectedLine ? `Đã chọn dòng ${selectedLine}` : 'Bấm vào dòng lệnh em nghi ngờ có lỗi'}
        </div>
        {!fixed ? (
          <PixelButton
            variant="danger"
            size="md"
            onClick={handleFixBug}
            disabled={!selectedLine}
          >
            <Bug size={16} /> Diệt lỗi dòng này!
          </PixelButton>
        ) : (
          <div className="flex items-center gap-2 text-sm font-bold text-[#38b764]">
            <CheckCircle2 size={18} /> Đã sửa lỗi thành công! Chương trình chạy hoàn hảo!
          </div>
        )}
      </div>
    </div>
  );
};
