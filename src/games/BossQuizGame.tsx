import React, { useState } from 'react';
import { PixelButton } from '../components/PixelButton';
import { sound } from '../../packages/game-core/audio';
import { Skull, Trophy } from 'lucide-react';

interface Question {
  question: string;
  options: string[];
  answer: number;
  explanation: string;
}

interface BossQuizGameProps {
  config: {
    boss_name?: string;
    boss_max_hp?: number;
    player_max_hp?: number;
    damage_per_hit?: number;
  };
  quizList?: Question[];
  onComplete: (score: number) => void;
}

export const BossQuizGame: React.FC<BossQuizGameProps> = ({ config, quizList, onComplete }) => {
  const bossName = config.boss_name || 'Hệ thống Thử thách Tổng hợp';
  const maxHp = config.boss_max_hp || 100;
  const questions: Question[] = quizList || [
    {
      question: 'Giao thức nào truyền tải siêu văn bản an toàn có mã hóa?',
      options: ['HTTP', 'HTTPS', 'FTP', 'SMTP'],
      answer: 1,
      explanation: 'HTTPS sử dụng chứng chỉ SSL/TLS để mã hóa dữ liệu giữa trình duyệt và máy chủ.',
    },
    {
      question: 'Độ phức tạp thuật toán tìm kiếm nhị phân trên mảng đã sắp xếp là:',
      options: ['O(N)', 'O(log N)', 'O(N^2)', 'O(1)'],
      answer: 1,
      explanation: 'Binary Search chia đôi không gian tìm kiếm sau mỗi bước nên đạt O(log N).',
    },
    {
      question: 'Thiết bị nào sau đây vừa là thiết bị vào vừa là thiết bị ra?',
      options: ['Bàn phím', 'Màn hình cảm ứng', 'Chuột', 'Máy in'],
      answer: 1,
      explanation: 'Màn hình cảm ứng vừa hiển thị (ra) vừa nhận thao tác chạm ngón tay (vào).',
    },
    {
      question: 'Dữ liệu được dùng để huấn luyện mô hình trí tuệ nhân tạo gọi là:',
      options: ['Training data', 'Test data', 'Hidden data', 'Cache data'],
      answer: 0,
      explanation: 'Training data (Dữ liệu huấn luyện) dùng để máy học các trọng số và đặc trưng.',
    },
  ];

  const [qIndex, setQIndex] = useState(0);
  const [bossHp, setBossHp] = useState(maxHp);
  const [playerHp, setPlayerHp] = useState(100);
  const [selectedOpt, setSelectedOpt] = useState<number | null>(null);
  const [answered, setAnswered] = useState(false);
  const [gameOver, setGameOver] = useState(false);

  const curQ = questions[qIndex];

  const handleSelectOption = (idx: number) => {
    if (answered || gameOver) return;
    setSelectedOpt(idx);
    setAnswered(true);

    if (idx === curQ?.answer) {
      sound.playCorrect();
      const dmg = Math.ceil(maxHp / questions.length);
      const newBossHp = Math.max(0, bossHp - dmg);
      setBossHp(newBossHp);

      if (newBossHp <= 0) {
        sound.playVictory();
        setGameOver(true);
        onComplete(1.0);
      }
    } else {
      sound.playMistake();
      setPlayerHp((hp) => Math.max(0, hp - 25));
    }
  };

  const handleNextQuestion = () => {
    sound.playClick();
    setSelectedOpt(null);
    setAnswered(false);
    if (qIndex + 1 < questions.length) {
      setQIndex((i) => i + 1);
    } else {
      setGameOver(true);
      onComplete(bossHp <= 0 ? 1.0 : 0.6);
    }
  };

  return (
    <div className="flex flex-col gap-6 bg-[#1a1c2c] p-6 border-3 border-[#5a6988]">
      {/* Giao diện Thử thách Tổng kết */}
      <div className="flex flex-col md:flex-row items-center justify-between gap-6 bg-[#181425] p-5 border-2 border-[#3a4466]">
        {/* TinTin Player */}
        <div className="flex items-center gap-3 w-full md:w-auto">
          <div className="text-3xl">🤖</div>
          <div className="flex-1">
            <div className="font-pixel text-xs text-[#38b764]">TinTin (Level Max)</div>
            <div className="w-32 h-3 bg-[#262b44] border border-[#5a6988] mt-1 overflow-hidden">
              <div
                className="h-full bg-[#38b764] transition-all duration-300"
                style={{ width: `${playerHp}%` }}
              ></div>
            </div>
            <div className="text-[10px] text-[#8b9bb4] mt-0.5">HP: {playerHp}/100</div>
          </div>
        </div>

        <div className="font-pixel text-xl text-[#e43b44] animate-pulse">VS</div>

        {/* Glitch Byte Boss */}
        <div className="flex items-center gap-3 w-full md:w-auto justify-end">
          <div className="flex-1 text-right">
            <div className="font-pixel text-xs text-[#f77622]">{bossName}</div>
            <div className="w-32 h-3 bg-[#262b44] border border-[#5a6988] mt-1 overflow-hidden ml-auto">
              <div
                className="h-full bg-[#e43b44] transition-all duration-300"
                style={{ width: `${(bossHp / maxHp) * 100}%` }}
              ></div>
            </div>
            <div className="text-[10px] text-[#8b9bb4] mt-0.5">HP: {bossHp}/{maxHp}</div>
          </div>
          <div className="text-3xl animate-bounce">👾</div>
        </div>
      </div>

      {/* Màn câu hỏi RPG */}
      {!gameOver && curQ ? (
        <div className="flex flex-col gap-4">
          <div className="text-xs font-black text-[#fee761] uppercase tracking-wider">
            CÂU HỎI THỬ THÁCH THỨ {qIndex + 1}/{questions.length}:
          </div>
          <div className="text-sm font-semibold text-white bg-[#262b44] p-4 border-2 border-[#5a6988]">
            {curQ.question}
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
            {curQ.options.map((opt, idx) => {
              const isSelected = selectedOpt === idx;
              const isCorrect = idx === curQ.answer;
              return (
                <button
                  key={idx}
                  onClick={() => handleSelectOption(idx)}
                  disabled={answered}
                  className={`p-3 text-left text-xs font-bold border-2 transition-all ${
                    answered
                      ? isCorrect
                        ? 'bg-[#193c3e] border-[#38b764] text-[#a7f070]'
                        : isSelected
                        ? 'bg-[#3e2731] border-[#e43b44] text-[#f6757a]'
                        : 'bg-[#262b44] border-[#3a4466] text-[#8b9bb4]'
                      : 'bg-[#262b44] border-[#5a6988] text-white hover:border-[#fee761]'
                  }`}
                >
                  {opt}
                </button>
              );
            })}
          </div>

          {answered && (
            <div className="flex items-center justify-between pt-2">
              <div className="text-xs text-[#c0cbdc] italic">
                {selectedOpt === curQ.answer ? '✨ Trả lời chính xác!' : '⚠️ Câu trả lời chưa chính xác!'}
              </div>
              <PixelButton variant="primary" size="sm" onClick={handleNextQuestion}>
                Tiếp tục câu hỏi ▶
              </PixelButton>
            </div>
          )}
        </div>
      ) : (
        <div className="flex flex-col items-center gap-3 py-6 text-center">
          {bossHp <= 0 ? (
            <>
              <Trophy className="text-[#fee761]" size={48} />
              <div className="text-xl font-black text-[#38b764] uppercase tracking-wider">XUẤT SẮC HOÀN THÀNH THỬ THÁCH TỔNG KẾT!</div>
              <div className="text-xs text-[#c0cbdc] max-w-md">
                Chúc mừng em đã hoàn thành xuất sắc toàn bộ nội dung ôn tập và đánh giá năng lực!
              </div>
            </>
          ) : (
            <>
              <Skull className="text-[#e43b44]" size={48} />
              <div className="text-lg font-black text-[#e43b44] uppercase tracking-wider">KẾT THÚC BÀI ĐÁNH GIÁ!</div>
              <div className="text-xs text-[#c0cbdc]">
                Điểm số bài làm: {100 - bossHp}%. Em hãy ôn tập lại các bài học để đạt kết quả tốt hơn nhé!
              </div>
            </>
          )}
        </div>
      )}
    </div>
  );
};
