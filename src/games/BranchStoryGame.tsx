import React, { useState } from 'react';
import { PixelButton } from '../components/PixelButton';
import { sound } from '../../packages/game-core/audio';
import { ShieldCheck, AlertTriangle } from 'lucide-react';

interface Choice {
  text: string;
  is_correct: boolean;
  feedback: string;
}

interface Scenario {
  id: string;
  prompt: string;
  choices: Choice[];
}

interface BranchStoryGameProps {
  config: {
    scenarios?: Scenario[];
  };
  onComplete: (score: number) => void;
}

export const BranchStoryGame: React.FC<BranchStoryGameProps> = ({ config, onComplete }) => {
  const scenarios = config.scenarios || [
    {
      id: 'sc1',
      prompt: 'Một người lạ trên mạng nhắn tin khen em chơi game giỏi và đề nghị tặng 5.000 KC nếu em cho biết số điện thoại của mẹ.',
      choices: [
        { text: 'Cho số điện thoại ngay để lấy kim cương!', is_correct: false, feedback: 'Nguy hiểm! Kẻ gian có thể dùng số điện thoại để lừa đảo cha mẹ em.' },
        { text: 'Từ chối dứt khoát và báo ngay cho bố mẹ biết.', is_correct: true, feedback: 'Rất sáng suốt! Học sinh thông thái luôn chủ động bảo vệ thông tin cá nhân và người thân.' },
      ],
    },
  ];

  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedChoice, setSelectedChoice] = useState<Choice | null>(null);
  const [correctCount, setCorrectCount] = useState(0);

  const cur = scenarios[currentIndex];

  const handleSelectChoice = (choice: Choice) => {
    setSelectedChoice(choice);
    if (choice.is_correct) {
      sound.playCorrect();
      setCorrectCount((c) => c + 1);
    } else {
      sound.playMistake();
    }
  };

  const handleNext = () => {
    sound.playClick();
    if (currentIndex + 1 < scenarios.length) {
      setCurrentIndex((i) => i + 1);
      setSelectedChoice(null);
    } else {
      sound.playVictory();
      const score = (correctCount + (selectedChoice?.is_correct ? 1 : 0)) / scenarios.length;
      onComplete(score);
    }
  };

  return (
    <div className="flex flex-col gap-5 bg-[#1a1c2c] p-6 border-3 border-[#5a6988]">
      <div className="flex items-center gap-2 border-b border-[#3a4466] pb-2">
        <ShieldCheck className="text-[#38b764]" size={20} />
        <span className="text-xs font-black text-[#fee761] uppercase tracking-wider">
          TÌNH HUỐNG VĂN HÓA & ĐẠO ĐỨC SỐ ({currentIndex + 1}/{scenarios.length})
        </span>
      </div>

      {/* Đề bài tình huống được highlight nổi bật */}
      <div className="bg-[#242b45] border-l-4 border-[#2ce8f5] p-4 border-2 border-[#5a6988] shadow-pixel-sm">
        <div className="flex items-start gap-2.5">
          <span className="px-2 py-0.5 bg-[#2ce8f5] text-[#181425] font-black text-xs uppercase tracking-wider shrink-0 mt-0.5 shadow-pixel-sm">
            TÌNH HUỐNG {currentIndex + 1}
          </span>
          <span className="text-sm sm:text-base font-bold text-white leading-relaxed">
            {cur?.prompt}
          </span>
        </div>
      </div>

      {/* Các lựa chọn */}
      <div className="flex flex-col gap-3">
        {cur?.choices.map((choice, idx) => {
          const isChosen = selectedChoice === choice;
          return (
            <button
              key={idx}
              onClick={() => !selectedChoice && handleSelectChoice(choice)}
              disabled={!!selectedChoice}
              className={`p-3.5 text-left text-sm font-semibold border-2 transition-all ${
                isChosen
                  ? choice.is_correct
                    ? 'bg-[#193c3e] border-[#38b764] text-[#a7f070]'
                    : 'bg-[#3e2731] border-[#e43b44] text-[#f6757a]'
                  : 'bg-[#262b44] border-[#5a6988] text-white hover:border-[#8b9bb4]'
              }`}
            >
              {String.fromCharCode(65 + idx)}. {choice.text}
            </button>
          );
        })}
      </div>

      {/* Phản hồi sau khi chọn */}
      {selectedChoice && (
        <div className={`p-3.5 border-2 flex items-start gap-3 ${
          selectedChoice.is_correct
            ? 'bg-[#193c3e] border-[#38b764]'
            : 'bg-[#3e2731] border-[#e43b44]'
        }`}>
          {selectedChoice.is_correct ? (
            <ShieldCheck className="text-[#38b764] shrink-0 mt-0.5" size={20} />
          ) : (
            <AlertTriangle className="text-[#e43b44] shrink-0 mt-0.5" size={20} />
          )}
          <div className="flex-1">
            <div className="font-bold text-xs mb-1">
              {selectedChoice.is_correct ? 'LỰA CHỌN CHÍNH XÁC!' : 'CẢNH BÁO NGUY HIỂM!'}
            </div>
            <div className="text-xs text-[#c0cbdc] leading-normal">{selectedChoice.feedback}</div>
          </div>
        </div>
      )}

      {selectedChoice && (
        <div className="flex justify-end pt-2">
          <PixelButton variant="primary" size="md" onClick={handleNext}>
            {currentIndex + 1 < scenarios.length ? 'Tình huống tiếp theo ▶' : 'Hoàn thành bài tập'}
          </PixelButton>
        </div>
      )}
    </div>
  );
};
