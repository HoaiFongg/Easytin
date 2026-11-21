import React, { useState } from 'react';
import { CurriculumNode } from '../../packages/domain/types';
import { PixelButton } from './PixelButton';
import { sound } from '../../packages/game-core/audio';
import { X } from 'lucide-react';

// Import các game components
import { SortDragGame } from '../games/SortDragGame';
import { BlockMazeGame } from '../games/BlockMazeGame';
import { LogicPuzzleGame } from '../games/LogicPuzzleGame';
import { TypeRunGame } from '../games/TypeRunGame';
import { MatchMemoryGame } from '../games/MatchMemoryGame';
import { BranchStoryGame } from '../games/BranchStoryGame';
import { BugHuntGame } from '../games/BugHuntGame';
import { BossQuizGame } from '../games/BossQuizGame';

interface LessonModalProps {
  node: CurriculumNode;
  onClose: () => void;
  onFinishLesson: (score: number) => void;
}

type Step = 'hook' | 'concept' | 'game' | 'quiz' | 'recap';

export const LessonModal: React.FC<LessonModalProps> = ({ node, onClose, onFinishLesson }) => {
  const [step, setStep] = useState<Step>('hook');
  const [gameScore, setGameScore] = useState<number>(0);
  const [quizScore, setQuizScore] = useState<number>(0);
  const [quizAnswers, setQuizAnswers] = useState<Record<number, number>>({});
  const [quizSubmitted, setQuizSubmitted] = useState<boolean>(false);

  const lesson = node.lesson_data;

  const handleGameComplete = (score: number) => {
    setGameScore(score);
  };

  const handleSelectQuizOption = (qIdx: number, optIdx: number) => {
    if (quizSubmitted) return;
    sound.playClick();
    setQuizAnswers((prev) => ({ ...prev, [qIdx]: optIdx }));
  };

  const handleCheckQuiz = () => {
    let correct = 0;
    lesson.quiz.forEach((q, idx) => {
      if (quizAnswers[idx] === q.answer) correct++;
    });
    const s = lesson.quiz.length > 0 ? correct / lesson.quiz.length : 1;
    setQuizScore(s);
    setQuizSubmitted(true);

    if (s >= 0.8) {
      sound.playCorrect();
    } else {
      sound.playMistake();
    }
  };

  const handleFinishAll = () => {
    sound.playVictory();
    // Tổng hợp điểm: Game 50% + Quiz 50%
    const finalScore = (gameScore + quizScore) / 2;
    onFinishLesson(Math.max(0.8, finalScore));
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/80 flex items-center justify-center p-3 sm:p-5 overflow-y-auto">
      <div className="bg-[#181425] border-4 border-[#5a6988] shadow-pixel-lg w-full max-w-4xl max-h-[92vh] flex flex-col overflow-hidden">
        {/* Header Modal */}
        <div className="flex items-center justify-between bg-[#262b44] px-4 py-3 border-b-3 border-[#3a4466]">
          <div className="flex items-center gap-2">
            <span className="w-3 h-3 bg-[#38b764] rounded-none"></span>
            <span className="text-xs font-black text-[#fee761] uppercase tracking-wide">{node.title}</span>
          </div>
          <button
            onClick={() => {
              sound.playClick();
              onClose();
            }}
            className="text-[#8b9bb4] hover:text-white cursor-pointer p-1"
          >
            <X size={18} />
          </button>
        </div>

        {/* Thanh chuyển bước học tập */}
        <div className="flex items-center justify-around bg-[#1a1c2c] border-b-2 border-[#3a4466] px-2 py-1.5 text-xs font-bold">
          <button
            onClick={() => { sound.playClick(); setStep('hook'); }}
            className={`px-3 py-1 flex items-center gap-1.5 ${step === 'hook' ? 'text-[#fee761] border-b-2 border-[#fee761]' : 'text-[#8b9bb4]'}`}
          >
            1. Mở đầu
          </button>
          <button
            onClick={() => { sound.playClick(); setStep('concept'); }}
            className={`px-3 py-1 flex items-center gap-1.5 ${step === 'concept' ? 'text-[#fee761] border-b-2 border-[#fee761]' : 'text-[#8b9bb4]'}`}
          >
            2. Khám phá
          </button>
          <button
            onClick={() => { sound.playClick(); setStep('game'); }}
            className={`px-3 py-1 flex items-center gap-1.5 ${step === 'game' ? 'text-[#fee761] border-b-2 border-[#fee761]' : 'text-[#8b9bb4]'}`}
          >
            3. Chơi Game
          </button>
          <button
            onClick={() => { sound.playClick(); setStep('quiz'); }}
            className={`px-3 py-1 flex items-center gap-1.5 ${step === 'quiz' ? 'text-[#fee761] border-b-2 border-[#fee761]' : 'text-[#8b9bb4]'}`}
          >
            4. Trắc nghiệm
          </button>
          <button
            onClick={() => { sound.playClick(); setStep('recap'); }}
            className={`px-3 py-1 flex items-center gap-1.5 ${step === 'recap' ? 'text-[#fee761] border-b-2 border-[#fee761]' : 'text-[#8b9bb4]'}`}
          >
            5. Tổng kết
          </button>
        </div>

        {/* Nội dung từng bước */}
        <div className="p-5 flex-1 overflow-y-auto">
          {/* BƯỚC 1: Mở đầu / Hook */}
          {step === 'hook' && (
            <div className="flex flex-col items-center gap-5 py-4">
              <div className="text-5xl animate-bounce">🤖</div>
              <div className="bg-[#262b44] border-3 border-[#38b764] p-5 max-w-xl text-center relative shadow-pixel">
                <div className="text-xs font-black text-[#fee761] uppercase tracking-wider mb-2">LỜI NHẮN TỪ TINTIN:</div>
                <p className="text-sm text-white leading-relaxed">{lesson.hook}</p>
              </div>
              <PixelButton variant="primary" size="lg" onClick={() => { sound.playClick(); setStep('concept'); }}>
                Khám phá kiến thức ngay ▶
              </PixelButton>
            </div>
          )}

          {/* BƯỚC 2: Khám phá kiến thức / Concept */}
          {step === 'concept' && (
            <div className="flex flex-col gap-5 max-w-2xl mx-auto py-2">
              <div className="bg-[#262b44] p-4 border-2 border-[#5a6988]">
                <h4 className="font-bold text-sm text-[#fee761] mb-2">
                  {lesson.concept.summary}
                </h4>
                <div className="flex flex-col gap-2.5 mt-3">
                  {lesson.concept.key_points.map((point, idx) => (
                    <div key={idx} className="flex items-start gap-2.5 bg-[#181425] p-3 border border-[#3a4466]">
                      <span className="text-[#38b764] font-bold">✔</span>
                      <span className="text-xs text-[#c0cbdc] leading-relaxed">{point}</span>
                    </div>
                  ))}
                </div>
              </div>
              <div className="flex justify-end">
                <PixelButton variant="primary" size="md" onClick={() => { sound.playClick(); setStep('game'); }}>
                  Vào sân chơi thực hành ▶
                </PixelButton>
              </div>
            </div>
          )}

          {/* BƯỚC 3: Đấu trường Game / Game Arena */}
          {step === 'game' && (
            <div className="flex flex-col gap-4">
              {node.template === 'sort-drag' && (
                <SortDragGame config={lesson.game_config} onComplete={handleGameComplete} />
              )}
              {node.template === 'block-maze' && (
                <BlockMazeGame config={lesson.game_config} onComplete={handleGameComplete} />
              )}
              {node.template === 'logic-puzzle' && (
                <LogicPuzzleGame config={lesson.game_config} onComplete={handleGameComplete} />
              )}
              {node.template === 'type-run' && (
                <TypeRunGame onComplete={handleGameComplete} />
              )}
              {node.template === 'match-memory' && (
                <MatchMemoryGame onComplete={handleGameComplete} />
              )}
              {node.template === 'branch-story' && (
                <BranchStoryGame config={lesson.game_config} onComplete={handleGameComplete} />
              )}
              {node.template === 'bug-hunt' && (
                <BugHuntGame onComplete={handleGameComplete} />
              )}
              {node.template === 'boss-quiz' && (
                <BossQuizGame config={lesson.game_config} quizList={lesson.quiz} onComplete={handleGameComplete} />
              )}

              <div className="flex justify-between items-center pt-3 border-t border-[#3a4466]">
                <span className="text-xs text-[#8b9bb4]">
                  Điểm game hiện tại: {Math.round(gameScore * 100)}%
                </span>
                <PixelButton variant="accent" size="sm" onClick={() => { sound.playClick(); setStep('quiz'); }}>
                  Sang phần Trắc nghiệm củng cố ▶
                </PixelButton>
              </div>
            </div>
          )}

          {/* BƯỚC 4: Kiểm tra củng cố / Quiz */}
          {step === 'quiz' && (
            <div className="flex flex-col gap-5 max-w-2xl mx-auto">
              {lesson.quiz.map((q, qIdx) => {
                const userAns = quizAnswers[qIdx];
                return (
                  <div key={qIdx} className="bg-[#262b44] p-4 border-2 border-[#5a6988]">
                    <div className="font-bold text-sm text-white mb-3">
                      Câu {qIdx + 1}: {q.question}
                    </div>
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                      {q.options.map((opt, optIdx) => {
                        const isSelected = userAns === optIdx;
                        const isCorrect = optIdx === q.answer;
                        return (
                          <button
                            key={optIdx}
                            onClick={() => handleSelectQuizOption(qIdx, optIdx)}
                            disabled={quizSubmitted}
                            className={`p-2.5 text-left text-xs font-semibold border-2 transition-all ${
                              quizSubmitted
                                ? isCorrect
                                  ? 'bg-[#193c3e] border-[#38b764] text-[#a7f070]'
                                  : isSelected
                                  ? 'bg-[#3e2731] border-[#e43b44] text-[#f6757a]'
                                  : 'bg-[#181425] border-[#3a4466] text-[#8b9bb4]'
                                : isSelected
                                ? 'bg-[#3a4466] border-[#fee761] text-white shadow-pixel-sm'
                                : 'bg-[#181425] border-[#3a4466] text-[#c0cbdc] hover:border-[#8b9bb4]'
                            }`}
                          >
                            {opt}
                          </button>
                        );
                      })}
                    </div>

                    {quizSubmitted && (
                      <div className="mt-3 text-xs bg-[#181425] p-2.5 border border-[#3a4466] text-[#c0cbdc]">
                        <span className="text-[#fee761] font-bold">Giải thích:</span> {q.explanation}
                      </div>
                    )}
                  </div>
                );
              })}

              <div className="flex justify-between items-center">
                {!quizSubmitted ? (
                  <PixelButton
                    variant="primary"
                    size="md"
                    onClick={handleCheckQuiz}
                    disabled={Object.keys(quizAnswers).length < lesson.quiz.length}
                  >
                    Kiểm tra đáp án
                  </PixelButton>
                ) : (
                  <PixelButton variant="primary" size="md" onClick={() => { sound.playClick(); setStep('recap'); }}>
                    Xem tổng kết bài học ▶
                  </PixelButton>
                )}
              </div>
            </div>
          )}

          {/* BƯỚC 5: Tổng kết bài học & Thăng cấp Leitner / Recap */}
          {step === 'recap' && (
            <div className="flex flex-col items-center gap-5 py-4 max-w-xl mx-auto text-center">
              <div className="text-5xl">🏆</div>
              <h3 className="text-lg font-black text-[#fee761] uppercase tracking-wider">HOÀN THÀNH BÀI HỌC!</h3>
              <p className="text-xs text-[#c0cbdc] leading-relaxed bg-[#262b44] p-4 border-2 border-[#5a6988]">
                {lesson.recap}
              </p>

              <div className="grid grid-cols-2 gap-4 w-full">
                <div className="bg-[#1a1c2c] p-3 border border-[#3a4466]">
                  <div className="text-[10px] text-[#8b9bb4]">ĐIỂM GAME</div>
                  <div className="font-pixel text-base text-[#38b764]">{Math.round(gameScore * 100)}%</div>
                </div>
                <div className="bg-[#1a1c2c] p-3 border border-[#3a4466]">
                  <div className="text-[10px] text-[#8b9bb4]">ĐIỂM TRẮC NGHIỆM</div>
                  <div className="font-pixel text-base text-[#2ce8f5]">{Math.round(quizScore * 100)}%</div>
                </div>
              </div>

              <PixelButton variant="primary" size="lg" onClick={handleFinishAll}>
                Nhận thưởng & Cập nhật tiến độ
              </PixelButton>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
