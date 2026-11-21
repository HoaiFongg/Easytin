import React, { useState } from 'react';
import { PixelButton } from '../components/PixelButton';
import { sound } from '../../packages/game-core/audio';
import { CheckCircle2, Zap } from 'lucide-react';

interface LogicPuzzleGameProps {
  config: {
    bits_count?: number;
    weights?: number[];
    target_values?: number[];
    puzzle_type?: string;
  };
  onComplete: (score: number) => void;
}

export const LogicPuzzleGame: React.FC<LogicPuzzleGameProps> = ({ config, onComplete }) => {
  const isGateType = config.puzzle_type === 'gate_circuit';

  // --- Logic for Binary Switches ---
  const weights = config.weights || [8, 4, 2, 1];
  const targets = config.target_values || [5, 9, 13];
  const [currentTargetIndex, setCurrentTargetIndex] = useState(0);
  const [bits, setBits] = useState<number[]>([0, 0, 0, 0]);
  const [solvedCount, setSolvedCount] = useState(0);

  // --- Logic for Logic Gates Circuit ---
  const [gateA, setGateA] = useState(1);
  const [gateB, setGateB] = useState(0);
  const [selectedGate, setSelectedGate] = useState<'AND' | 'OR' | 'NOT'>('AND');

  const toggleBit = (idx: number) => {
    sound.playJump();
    setBits((prev) => {
      const next = [...prev];
      next[idx] = next[idx] === 1 ? 0 : 1;
      return next;
    });
  };

  const currentSum = bits.reduce((acc, val, i) => acc + val * (weights[i] || 0), 0);
  const targetVal = targets[currentTargetIndex] || 5;

  const checkBinary = () => {
    if (currentSum === targetVal) {
      sound.playCorrect();
      const nextSolved = solvedCount + 1;
      setSolvedCount(nextSolved);

      if (currentTargetIndex + 1 < targets.length) {
        setCurrentTargetIndex((c) => c + 1);
        setBits([0, 0, 0, 0]);
      } else {
        sound.playVictory();
        onComplete(1.0);
      }
    } else {
      sound.playMistake();
    }
  };

  // Logic Gate Evaluation
  const computeGateOutput = () => {
    if (selectedGate === 'AND') return gateA && gateB ? 1 : 0;
    if (selectedGate === 'OR') return gateA || gateB ? 1 : 0;
    if (selectedGate === 'NOT') return gateA ? 0 : 1;
    return 0;
  };

  return (
    <div className="flex flex-col gap-6">
      {!isGateType ? (
        // Chế độ 1: Bật tắt 4-bit Nhị phân
        <div className="flex flex-col items-center gap-5 bg-[#1a1c2c] p-6 border-3 border-[#5a6988]">
          <div className="text-center">
            <span className="text-xs text-[#8b9bb4]">MÃ SỐ BÍ MẬT CẦN MỞ KHÓA:</span>
            <div className="font-pixel text-4xl text-[#fee761] mt-1">{targetVal}</div>
            <div className="text-xs text-[#38b764] mt-1">
              Đã mở được: {solvedCount} / {targets.length} mã
            </div>
          </div>

          {/* 4 Công tắc nhị phân */}
          <div className="grid grid-cols-4 gap-3 w-full max-w-sm">
            {weights.map((w, idx) => {
              const isOn = bits[idx] === 1;
              return (
                <div
                  key={idx}
                  onClick={() => toggleBit(idx)}
                  className={`p-3 border-3 cursor-pointer flex flex-col items-center justify-center transition-all ${
                    isOn
                      ? 'bg-[#2b5c3f] border-[#38b764] -translate-y-1 shadow-pixel'
                      : 'bg-[#181425] border-[#3a4466] hover:border-[#5a6988]'
                  }`}
                >
                  <span className="font-pixel text-xs text-[#8b9bb4] mb-1">+{w}</span>
                  <div className={`w-8 h-8 rounded-full flex items-center justify-center font-pixel text-sm font-bold ${
                    isOn ? 'bg-[#38b764] text-[#181425]' : 'bg-[#262b44] text-[#5a6988]'
                  }`}>
                    {bits[idx]}
                  </div>
                  <span className="text-[10px] mt-1 text-[#fee761] uppercase font-bold">
                    {isOn ? 'BẬT (1)' : 'TẮT (0)'}
                  </span>
                </div>
              );
            })}
          </div>

          {/* Tổng hiện tại & Nút kiểm tra */}
          <div className="flex items-center gap-4">
            <div className="text-sm font-bold">
              Tổng hiện tại: <span className="font-pixel text-[#2ce8f5]">{currentSum}</span>
            </div>
            <PixelButton variant="primary" size="md" onClick={checkBinary}>
              <CheckCircle2 size={16} /> Xác nhận mã
            </PixelButton>
          </div>
        </div>
      ) : (
        // Chế độ 2: Mô phỏng Cổng Logic AND, OR, NOT
        <div className="flex flex-col items-center gap-5 bg-[#1a1c2c] p-6 border-3 border-[#5a6988]">
          <div className="text-xs text-[#8b9bb4]">MÔ PHỎNG MẠCH LOGIC ĐIỆN TỬ:</div>

          {/* Sơ đồ mạch */}
          <div className="flex items-center gap-4 bg-[#181425] p-5 border-2 border-[#3a4466]">
            {/* Đầu vào A & B */}
            <div className="flex flex-col gap-3">
              <button
                onClick={() => { sound.playClick(); setGateA(gateA ? 0 : 1); }}
                className={`px-3 py-1 font-pixel text-xs border-2 ${
                  gateA ? 'bg-[#38b764] text-black border-[#a7f070]' : 'bg-[#262b44] text-[#8b9bb4] border-[#3a4466]'
                }`}
              >
                Đầu vào A: {gateA}
              </button>
              {selectedGate !== 'NOT' && (
                <button
                  onClick={() => { sound.playClick(); setGateB(gateB ? 0 : 1); }}
                  className={`px-3 py-1 font-pixel text-xs border-2 ${
                    gateB ? 'bg-[#38b764] text-black border-[#a7f070]' : 'bg-[#262b44] text-[#8b9bb4] border-[#3a4466]'
                  }`}
                >
                  Đầu vào B: {gateB}
                </button>
              )}
            </div>

            <div className="text-[#feae34] font-bold">──▶</div>

            {/* Khối Cổng Logic */}
            <div className="flex flex-col items-center gap-2">
              <div className="font-pixel text-sm bg-[#5d275d] border-2 border-[#ea57b2] px-4 py-2 text-white">
                CỔNG {selectedGate}
              </div>
              <div className="flex gap-1">
                {(['AND', 'OR', 'NOT'] as const).map((g) => (
                  <button
                    key={g}
                    onClick={() => { sound.playClick(); setSelectedGate(g); }}
                    className={`px-2 py-0.5 text-[10px] font-bold border ${
                      selectedGate === g ? 'bg-[#feae34] text-black border-white' : 'bg-[#262b44] text-[#8b9bb4]'
                    }`}
                  >
                    {g}
                  </button>
                ))}
              </div>
            </div>

            <div className="text-[#feae34] font-bold">──▶</div>

            {/* Đầu ra bóng đèn */}
            <div className="flex flex-col items-center">
              <div className={`w-12 h-12 rounded-full border-3 flex items-center justify-center text-xl transition-all ${
                computeGateOutput() === 1
                  ? 'bg-[#fee761] border-white shadow-[0_0_15px_#fee761] text-black'
                  : 'bg-[#262b44] border-[#3a4466] text-[#5a6988]'
              }`}>
                <Zap size={22} />
              </div>
              <span className="text-[10px] font-pixel text-[#8b9bb4] mt-1">
                Đầu ra: {computeGateOutput()}
              </span>
            </div>
          </div>

          <PixelButton
            variant="primary"
            size="md"
            onClick={() => {
              sound.playVictory();
              onComplete(1.0);
            }}
          >
            <CheckCircle2 size={16} /> Hoàn thành bài thí nghiệm
          </PixelButton>
        </div>
      )}
    </div>
  );
};
