import React, { useState } from 'react';
import { CurriculumNode } from '../../packages/domain/types';
import { PixelButton } from './PixelButton';
import { sound } from '../../packages/game-core/audio';
import { X, CheckSquare, Square, Lightbulb, BookOpen, Gamepad2, Laptop, Trophy, MessageSquare, Bookmark } from 'lucide-react';

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

type Step = 'hook' | 'theory' | 'game' | 'practice' | 'recap';

// Hàm hỗ trợ highlight các câu hỏi xuất hiện trong văn bản bài học
const renderTextWithHighlightedQuestions = (text: string) => {
  if (!text) return text;
  // Bắt các câu hỏi kết thúc bằng dấu '?'
  const questionRegex = /([^.!?\n]+(?:\?))/g;
  const parts: React.ReactNode[] = [];
  let lastIndex = 0;
  let match: RegExpExecArray | null;

  while ((match = questionRegex.exec(text)) !== null) {
    if (match.index > lastIndex) {
      parts.push(text.substring(lastIndex, match.index));
    }
    parts.push(
      <span
        key={match.index}
        className="bg-[#fee761]/15 text-[#fee761] font-bold px-1 py-0.5 border-b-2 border-[#fee761] inline"
      >
        {match[0].trim()}
      </span>
    );
    lastIndex = match.index + match[0].length;
  }

  if (lastIndex < text.length) {
    parts.push(text.substring(lastIndex));
  }

  return parts.length > 0 ? parts : text;
};

export const LessonModal: React.FC<LessonModalProps> = ({ node, onClose, onFinishLesson }) => {
  const [step, setStep] = useState<Step>('hook');
  const [gameScore, setGameScore] = useState<number>(0);
  const [quizScore, setQuizScore] = useState<number>(0);
  const [quizAnswers, setQuizAnswers] = useState<Record<number, number>>({});
  const [quizSubmitted, setQuizSubmitted] = useState<boolean>(false);
  const [completedSteps, setCompletedSteps] = useState<Record<number, boolean>>({});

  const lesson = node.lesson_data;
  const theory = lesson.theory;
  const practice = lesson.practice;

  const handleGameComplete = (score: number) => {
    setGameScore(score);
  };

  const handleToggleLabStep = (stepIdx: number) => {
    sound.playClick();
    setCompletedSteps((prev) => ({
      ...prev,
      [stepIdx]: !prev[stepIdx]
    }));
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
    // Tổng hợp điểm: Game 50% + Trắc nghiệm & Thực hành 50%
    const finalScore = (gameScore + (quizSubmitted ? quizScore : 1)) / 2;
    onFinishLesson(Math.max(0.8, finalScore));
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/85 flex items-center justify-center p-2 sm:p-4 overflow-y-auto">
      <div className="bg-[#181425] border-4 border-[#5a6988] shadow-pixel-lg w-full max-w-5xl xl:max-w-6xl max-h-[94vh] flex flex-col overflow-hidden anim-pixel-pop-in">
        {/* Header Modal */}
        <div className="flex items-center justify-between bg-[#262b44] px-4 py-2.5 border-b-3 border-[#3a4466]">
          <div className="flex items-center gap-2 overflow-hidden">
            <span className="w-3 h-3 bg-[#38b764] flex-shrink-0"></span>
            <span className="text-xs font-black text-[#fee761] uppercase tracking-wide truncate">
              {node.id}: {node.title}
            </span>
            <span className="hidden sm:inline-block px-2 py-0.5 bg-[#181425] text-[10px] text-[#2ce8f5] border border-[#3a4466]">
              Lớp {node.grade}
            </span>
          </div>
          <button
            onClick={() => {
              sound.playClick();
              onClose();
            }}
            className="text-[#8b9bb4] hover:text-white cursor-pointer p-1"
            title="Đóng"
          >
            <X size={18} />
          </button>
        </div>

        {/* Thanh chuyển 5 bước học tập tương tác */}
        <div className="flex items-center justify-around bg-[#1a1c2c] border-b-2 border-[#3a4466] px-1 py-1.5 text-xs font-bold overflow-x-auto">
          <button
            onClick={() => { sound.playClick(); setStep('hook'); }}
            className={`px-2.5 py-1 flex items-center gap-1.5 whitespace-nowrap transition-colors ${
              step === 'hook' ? 'text-[#fee761] border-b-2 border-[#fee761] bg-[#262b44]' : 'text-[#8b9bb4] hover:text-white'
            }`}
          >
            <span>🌟</span> 1. Mở đầu
          </button>
          <button
            onClick={() => { sound.playClick(); setStep('theory'); }}
            className={`px-2.5 py-1 flex items-center gap-1.5 whitespace-nowrap transition-colors ${
              step === 'theory' ? 'text-[#fee761] border-b-2 border-[#fee761] bg-[#262b44]' : 'text-[#8b9bb4] hover:text-white'
            }`}
          >
            <BookOpen size={13} /> 2. Lí thuyết
          </button>
          <button
            onClick={() => { sound.playClick(); setStep('game'); }}
            className={`px-2.5 py-1 flex items-center gap-1.5 whitespace-nowrap transition-colors ${
              step === 'game' ? 'text-[#fee761] border-b-2 border-[#fee761] bg-[#262b44]' : 'text-[#8b9bb4] hover:text-white'
            }`}
          >
            <Gamepad2 size={13} /> 3. Trò chơi
          </button>
          <button
            onClick={() => { sound.playClick(); setStep('practice'); }}
            className={`px-2.5 py-1 flex items-center gap-1.5 whitespace-nowrap transition-colors ${
              step === 'practice' ? 'text-[#fee761] border-b-2 border-[#fee761] bg-[#262b44]' : 'text-[#8b9bb4] hover:text-white'
            }`}
          >
            <Laptop size={13} /> 4. Thực hành
          </button>
          <button
            onClick={() => { sound.playClick(); setStep('recap'); }}
            className={`px-2.5 py-1 flex items-center gap-1.5 whitespace-nowrap transition-colors ${
              step === 'recap' ? 'text-[#fee761] border-b-2 border-[#fee761] bg-[#262b44]' : 'text-[#8b9bb4] hover:text-white'
            }`}
          >
            <Trophy size={13} /> 5. Tổng kết
          </button>
        </div>

        {/* Nội dung từng bước */}
        <div className="p-4 sm:p-5 flex-1 overflow-y-auto">
          {/* BƯỚC 1: Mở đầu / Hook */}
          {step === 'hook' && (
            <div className="flex flex-col items-center gap-5 py-4 max-w-xl mx-auto text-center">
              <div className="text-5xl animate-bounce">🤖</div>
              <div className="bg-[#262b44] border-3 border-[#38b764] p-5 w-full text-center relative shadow-pixel">
                <div className="text-xs font-black text-[#fee761] uppercase tracking-wider mb-2 flex items-center justify-center gap-1.5">
                  <MessageSquare size={14} className="text-[#fee761]" /> LỜI NHẮN TỪ ROBOT TINTIN:
                </div>
                {/* Hộp câu hỏi khởi động được highlight nổi bật */}
                <div className="bg-[#181425] border-l-4 border-[#fee761] p-3.5 sm:p-4 my-2 text-left border-y border-r border-[#3a4466] shadow-pixel-sm">
                  <p className="text-[11px] font-bold text-[#fee761] uppercase mb-1 flex items-center gap-1">
                    <span className="w-2 h-2 bg-[#fee761] inline-block"></span> CÂU HỎI KHỞI ĐỘNG BÀI HỌC:
                  </p>
                  <p className="text-sm sm:text-base font-bold text-white leading-relaxed">
                    {renderTextWithHighlightedQuestions(lesson.hook)}
                  </p>
                </div>
              </div>

              {node.textbook_mapping && (
                <div className="w-full bg-[#1a1c2c] border border-[#3a4466] p-3 text-left text-[11px] text-[#c0cbdc]">
                  <div className="font-bold text-[#fee761] mb-1.5 flex items-center gap-1">
                    <Bookmark size={12} /> BÀI HỌC TƯƠNG ỨNG TRONG 3 BỘ SÁCH GIÁO KHOA:
                  </div>
                  <div className="grid grid-cols-1 sm:grid-cols-3 gap-1.5">
                    <div className="bg-[#181425] p-1.5 border border-[#262b44]">
                      <span className="text-[#38b764] font-bold">KNTT:</span> {node.textbook_mapping.kntt || 'Chuẩn GDPT 2018'}
                    </div>
                    <div className="bg-[#181425] p-1.5 border border-[#262b44]">
                      <span className="text-[#2ce8f5] font-bold">Cánh Diều:</span> {node.textbook_mapping.canhdieu || 'Chuẩn GDPT 2018'}
                    </div>
                    <div className="bg-[#181425] p-1.5 border border-[#262b44]">
                      <span className="text-[#e4a672] font-bold">CTST:</span> {node.textbook_mapping.ctst || 'Chuẩn GDPT 2018'}
                    </div>
                  </div>
                </div>
              )}

              <PixelButton variant="primary" size="lg" onClick={() => { sound.playClick(); setStep('theory'); }}>
                Khám phá Lí thuyết ngay ▶
              </PixelButton>
            </div>
          )}

          {/* BƯỚC 2: Lí thuyết chuyên sâu / Theory */}
          {step === 'theory' && (
            <div className="flex flex-col gap-4 max-w-4xl xl:max-w-5xl mx-auto py-1 w-full">
              {/* Lời dẫn bài học */}
              <div className="bg-[#20243b] p-4 border-2 border-[#5a6988] shadow-pixel">
                <div className="flex items-center gap-2 mb-2">
                  <BookOpen size={16} className="text-[#fee761]" />
                  <h4 className="font-bold text-sm text-[#fee761] uppercase tracking-wide">
                    TỔNG QUAN KIẾN THỨC BÀI HỌC
                  </h4>
                </div>
                <p className="text-xs sm:text-sm text-[#c0cbdc] leading-relaxed">
                  {renderTextWithHighlightedQuestions(theory?.overview || lesson.concept.summary)}
                </p>
              </div>

              {/* Các phần lý thuyết chuyên sâu */}
              {theory?.sections && theory.sections.length > 0 ? (
                <div className="flex flex-col gap-3">
                  {theory.sections.map((sec, idx) => (
                    <div key={idx} className="bg-[#262b44] p-4 border-2 border-[#3a4466]">
                      <h5 className="font-bold text-xs sm:text-sm text-[#2ce8f5] mb-2 flex items-center gap-1.5">
                        <span>📌</span> {sec.title}
                      </h5>
                      <div className="text-xs text-[#e0e6ed] leading-relaxed whitespace-pre-line mb-3">
                        {renderTextWithHighlightedQuestions(sec.content)}
                      </div>

                      {/* Ví dụ thực tế */}
                      {sec.example && (
                        <div className="bg-[#193c3e] border border-[#38b764] p-3 text-xs text-[#a7f070] my-2 leading-relaxed">
                          <span className="font-bold text-white flex items-center gap-1 mb-1">
                            <span>🌱</span> Ví dụ thực tế đời sống:
                          </span>
                          {renderTextWithHighlightedQuestions(sec.example)}
                        </div>
                      )}

                      {/* Mẹo hoặc cảnh báo */}
                      {sec.tip && (
                        <div className="bg-[#3a3520] border border-[#e4a672] p-2.5 text-xs text-[#fee761] my-1.5 leading-relaxed">
                          <span className="font-bold flex items-center gap-1 mb-0.5">
                            <Lightbulb size={13} /> Lưu ý khi học tập:
                          </span>
                          {sec.tip}
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              ) : (
                /* Fallback với Concept key points */
                <div className="bg-[#262b44] p-4 border-2 border-[#5a6988]">
                  <h4 className="font-bold text-sm text-[#fee761] mb-2">{lesson.concept.summary}</h4>
                  <div className="flex flex-col gap-2 mt-3">
                    {lesson.concept.key_points.map((point, idx) => (
                      <div key={idx} className="flex items-start gap-2.5 bg-[#181425] p-3 border border-[#3a4466]">
                        <span className="text-[#38b764] font-bold">✔</span>
                        <span className="text-xs text-[#c0cbdc] leading-relaxed">{point}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Hộp ghi nhớ vàng */}
              {theory?.memorize && (
                <div className="bg-[#2a273f] border-2 border-[#fee761] p-3.5 text-center shadow-pixel">
                  <div className="text-[10px] font-black text-[#fee761] uppercase tracking-wider mb-1">
                    ⭐ KIẾN THỨC TRỌNG TÂM — EM CẦN GHI NHỚ:
                  </div>
                  <div className="text-xs sm:text-sm font-bold text-white">{theory.memorize}</div>
                </div>
              )}

              <div className="flex justify-end pt-2">
                <PixelButton variant="primary" size="md" onClick={() => { sound.playClick(); setStep('game'); }}>
                  Tiến vào Trò chơi học tập ▶
                </PixelButton>
              </div>
            </div>
          )}

          {/* BƯỚC 3: Trò chơi học tập / Game Arena */}
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
                  Điểm game hiện tại: <span className="text-[#38b764] font-bold">{Math.round(gameScore * 100)}%</span>
                </span>
                <PixelButton variant="accent" size="sm" onClick={() => { sound.playClick(); setStep('practice'); }}>
                  Sang Phòng Thực hành & Kiểm tra ▶
                </PixelButton>
              </div>
            </div>
          )}

          {/* BƯỚC 4: Phòng Thực hành Lab & Trắc nghiệm chẩn đoán / Practice */}
          {step === 'practice' && (
            <div className="flex flex-col gap-5 max-w-4xl xl:max-w-5xl mx-auto py-1 w-full">
              {/* Nhiệm vụ phòng Lab */}
              {practice?.mission ? (
                <div className="bg-[#20243b] p-4 border-2 border-[#5a6988] shadow-pixel">
                  <div className="flex items-center gap-2 mb-2">
                    <Laptop size={16} className="text-[#38b764]" />
                    <h4 className="font-bold text-sm text-[#38b764] uppercase tracking-wide">
                      {practice.mission.title}
                    </h4>
                  </div>
                  <div className="text-xs text-[#fee761] bg-[#181425] p-2.5 border border-[#3a4466] mb-3">
                    <span className="font-bold">🎯 Mục tiêu cần đạt:</span> {practice.mission.goal}
                  </div>

                  <div className="text-xs font-bold text-[#c0cbdc] mb-2 uppercase tracking-wide">
                    CÁC BƯỚC THAO TÁC MÁY TÍNH (NHẤP ĐỂ TÍCH HOÀN THÀNH):
                  </div>
                  <div className="flex flex-col gap-2">
                    {practice.mission.steps.map((st, sIdx) => {
                      const isDone = completedSteps[sIdx];
                      return (
                        <button
                          key={sIdx}
                          onClick={() => handleToggleLabStep(sIdx)}
                          className={`flex items-start gap-2.5 p-2.5 text-left text-xs border transition-colors ${
                            isDone
                              ? 'bg-[#193c3e] border-[#38b764] text-[#a7f070]'
                              : 'bg-[#181425] border-[#3a4466] text-[#c0cbdc] hover:border-[#8b9bb4]'
                          }`}
                        >
                          <span className="mt-0.5">
                            {isDone ? <CheckSquare size={14} className="text-[#38b764]" /> : <Square size={14} className="text-[#8b9bb4]" />}
                          </span>
                          <span className={`leading-relaxed ${isDone ? 'line-through opacity-85' : ''}`}>{st}</span>
                        </button>
                      );
                    })}
                  </div>

                  {practice.mission.tip && (
                    <div className="mt-3 text-xs bg-[#181425] p-2.5 border border-[#3a4466] text-[#fee761]">
                      <span className="font-bold">💡 Mẹo thực hành:</span> {practice.mission.tip}
                    </div>
                  )}

                  {practice.mission.challenge && (
                    <div className="mt-2 text-xs bg-[#2b203a] p-2.5 border border-[#c4538a] text-[#fca3ca]">
                      <span className="font-bold">🚀 Thử thách mở rộng:</span> {practice.mission.challenge}
                    </div>
                  )}
                </div>
              ) : null}

              {/* Phần Trắc nghiệm Chẩn đoán củng cố */}
              <div className="bg-[#262b44] p-4 border-2 border-[#5a6988]">
                <div className="flex items-center gap-2 mb-3">
                  <span className="text-base">📝</span>
                  <h4 className="font-bold text-sm text-[#fee761] uppercase tracking-wide">
                    TRẮC NGHIỆM CHẨN ĐOÁN CỦNG CỐ
                  </h4>
                </div>

                <div className="flex flex-col gap-4">
                  {lesson.quiz.map((q, qIdx) => {
                    const userAns = quizAnswers[qIdx];
                    return (
                      <div key={qIdx} className="bg-[#181425] p-3.5 border-2 border-[#3a4466] shadow-pixel-sm">
                        {/* Hộp câu hỏi được highlight nổi bật với viền vàng và badge */}
                        <div className="bg-[#242b45] border-l-4 border-[#fee761] p-3 sm:p-3.5 mb-3 border-y border-r border-[#3a4466] shadow-pixel-sm">
                          <div className="flex items-start gap-2.5">
                            <span className="px-2 py-0.5 bg-[#fee761] text-[#181425] font-black text-[11px] uppercase tracking-wider shrink-0 mt-0.5 shadow-pixel-sm">
                              CÂU HỎI {qIdx + 1}
                            </span>
                            <span className="text-xs sm:text-sm font-bold text-white leading-relaxed">
                              {q.question}
                            </span>
                          </div>
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
                          <div className="mt-3 text-xs bg-[#242b45] p-3 border-l-4 border-[#38b764] border-y border-r border-[#3a4466] text-[#c0cbdc] leading-relaxed">
                            <span className="text-[#38b764] font-bold">💡 Giải thích chi tiết:</span> {q.explanation}
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              </div>

              {/* Điều khiển Bước 4 */}
              <div className="flex justify-between items-center pt-2">
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
            <div className="flex flex-col items-center gap-5 py-4 max-w-2xl mx-auto text-center w-full">
              <div className="text-5xl animate-bounce">🏆</div>
              <h3 className="text-lg font-black text-[#fee761] uppercase tracking-wider">HOÀN THÀNH BÀI HỌC!</h3>
              <p className="text-xs text-[#c0cbdc] leading-relaxed bg-[#262b44] p-4 border-2 border-[#5a6988]">
                {lesson.recap}
              </p>

              <div className="grid grid-cols-2 gap-4 w-full">
                <div className="bg-[#1a1c2c] p-3 border border-[#3a4466]">
                  <div className="text-[10px] text-[#8b9bb4]">ĐIỂM TRÒ CHƠI HỌC TẬP</div>
                  <div className="font-pixel text-base text-[#38b764]">{Math.round(gameScore * 100)}%</div>
                </div>
                <div className="bg-[#1a1c2c] p-3 border border-[#3a4466]">
                  <div className="text-[10px] text-[#8b9bb4]">ĐIỂM THỰC HÀNH & TRẮC NGHIỆM</div>
                  <div className="font-pixel text-base text-[#2ce8f5]">{Math.round(quizScore * 100)}%</div>
                </div>
              </div>

              <div className="text-xs text-[#8b9bb4] bg-[#181425] p-3 border border-[#3a4466] w-full text-left">
                <span className="text-[#fee761] font-bold">⭐ Hệ thống Leitner Box:</span> Bài học này đã được đưa vào Hộp ôn tập thông minh để củng cố trí nhớ dài hạn theo chu kỳ 1 ngày, 3 ngày, 7 ngày, 21 ngày.
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
