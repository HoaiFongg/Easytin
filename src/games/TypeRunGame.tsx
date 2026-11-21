import React, { useState } from 'react';
import { PixelButton } from '../components/PixelButton';
import { sound } from '../../packages/game-core/audio';
import { RotateCcw } from 'lucide-react';

interface TypeRunGameProps {
  onComplete: (score: number) => void;
}

const WORDS = [
  'chuot',
  'ban phim',
  'man hinh',
  'thuat toan',
  'phan cung',
  'phan mem',
  'an toan mang',
];

export const TypeRunGame: React.FC<TypeRunGameProps> = ({ onComplete }) => {
  const [wordIndex, setWordIndex] = useState(0);
  const [inputVal, setInputVal] = useState('');
  const [runnerPos, setRunnerPos] = useState(0);
  const [finished, setFinished] = useState(false);

  const currentWord = WORDS[wordIndex] || 'hoan thanh';

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const val = e.target.value;
    setInputVal(val);

    // Normalize comparison
    if (val.trim().toLowerCase() === currentWord.toLowerCase()) {
      sound.playCorrect();
      setInputVal('');
      const nextIndex = wordIndex + 1;
      setWordIndex(nextIndex);
      setRunnerPos((nextIndex / WORDS.length) * 100);

      if (nextIndex >= WORDS.length) {
        sound.playVictory();
        setFinished(true);
        onComplete(1.0);
      }
    } else {
      sound.playClick();
    }
  };

  const handleReset = () => {
    setWordIndex(0);
    setInputVal('');
    setRunnerPos(0);
    setFinished(false);
  };

  return (
    <div className="flex flex-col gap-6 bg-[#1a1c2c] p-6 border-3 border-[#5a6988]">
      {/* Đường đua nhân vật pixel */}
      <div className="relative w-full h-20 bg-[#181425] border-2 border-[#3a4466] overflow-hidden flex items-end px-4 pb-2">
        {/* Đường chạy */}
        <div className="absolute bottom-0 left-0 right-0 h-2 bg-[#2b5c3f] border-t border-[#38b764]"></div>

        {/* Cờ đích */}
        <div className="absolute right-4 bottom-2 text-2xl">🏁</div>

        {/* Chú robot TinTin đang chạy */}
        <div
          className="absolute bottom-2 transition-all duration-300 text-2xl"
          style={{ left: `calc(${runnerPos}% * 0.85)` }}
        >
          🤖💨
        </div>
      </div>

      {/* Màn hình gõ chữ */}
      {!finished ? (
        <div className="flex flex-col items-center gap-3">
          <div className="text-xs text-[#8b9bb4]">TỪ CẦN GÕ TIẾP THEO:</div>
          <div className="font-pixel text-2xl text-[#fee761] tracking-widest bg-[#262b44] px-6 py-3 border-2 border-[#5a6988]">
            {currentWord}
          </div>

          <div className="w-full max-w-sm mt-2">
            <input
              type="text"
              autoFocus
              value={inputVal}
              onChange={handleChange}
              placeholder="Gõ từ trên vào đây..."
              className="w-full bg-[#181425] border-3 border-[#38b764] px-4 py-2.5 font-bold text-center text-white outline-none focus:border-[#fee761]"
            />
          </div>

          <div className="text-xs text-[#8b9bb4]">
            Tiến độ: {wordIndex} / {WORDS.length} từ
          </div>
        </div>
      ) : (
        <div className="flex flex-col items-center gap-3 py-4">
          <div className="text-xl font-bold text-[#38b764]">VỀ ĐÍCH THÀNH CÔNG!</div>
          <div className="text-xs text-[#c0cbdc]">
            Đôi tay của em gõ phím rất nhanh và chuẩn xác!
          </div>
          <PixelButton variant="primary" size="md" onClick={handleReset}>
            <RotateCcw size={16} /> Chơi lại lần nữa
          </PixelButton>
        </div>
      )}
    </div>
  );
};
