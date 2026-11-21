import React, { useState } from 'react';
import { PixelButton } from '../components/PixelButton';
import { sound } from '../../packages/game-core/audio';
import { Play, RotateCcw, ArrowUp, RotateCcw as TurnLeft, RotateCw as TurnRight, Repeat } from 'lucide-react';

interface BlockMazeConfig {
  grid_size?: number;
  start?: { x: number; y: number; dir: 'N' | 'E' | 'S' | 'W' };
  target?: { x: number; y: number };
  walls?: Array<{ x: number; y: number }>;
}

interface BlockMazeGameProps {
  config: BlockMazeConfig;
  onComplete: (score: number) => void;
}

type Command = 'forward' | 'turn_left' | 'turn_right' | 'repeat_2';

export const BlockMazeGame: React.FC<BlockMazeGameProps> = ({ config, onComplete }) => {
  const gridSize = config.grid_size || 4;
  const startPos = config.start || { x: 0, y: 0, dir: 'E' };
  const targetPos = config.target || { x: 2, y: 2 };
  const walls = config.walls || [{ x: 1, y: 0 }, { x: 1, y: 1 }];

  const [commands, setCommands] = useState<Command[]>([]);
  const [robotPos, setRobotPos] = useState(startPos);
  const [isRunning, setIsRunning] = useState(false);
  const [message, setMessage] = useState<string | null>(null);

  const addCommand = (cmd: Command) => {
    if (commands.length >= 8 || isRunning) return;
    sound.playClick();
    setCommands((prev) => [...prev, cmd]);
  };

  const removeCommand = (index: number) => {
    if (isRunning) return;
    sound.playClick();
    setCommands((prev) => prev.filter((_, i) => i !== index));
  };

  const handleReset = () => {
    sound.playClick();
    setRobotPos(startPos);
    setCommands([]);
    setIsRunning(false);
    setMessage(null);
  };

  const runCode = async () => {
    if (commands.length === 0 || isRunning) return;
    setIsRunning(true);
    setMessage('Robot đang thực thi thuật toán...');
    let cur = { ...startPos };
    setRobotPos(cur);

    // Expand repeat_2 if present
    const expanded: Array<'forward' | 'turn_left' | 'turn_right'> = [];
    for (let i = 0; i < commands.length; i++) {
      if (commands[i] === 'repeat_2') {
        const next = commands[i + 1];
        if (next && next !== 'repeat_2') {
          expanded.push(next);
          expanded.push(next);
          i++; // skip next since it's repeated
        }
      } else {
        expanded.push(commands[i] as 'forward' | 'turn_left' | 'turn_right');
      }
    }

    const DIRS = ['N', 'E', 'S', 'W'] as const;

    for (const step of expanded) {
      await new Promise((r) => setTimeout(r, 450));
      sound.playJump();

      if (step === 'turn_left') {
        const idx = DIRS.indexOf(cur.dir);
        cur.dir = DIRS[(idx + 3) % 4];
      } else if (step === 'turn_right') {
        const idx = DIRS.indexOf(cur.dir);
        cur.dir = DIRS[(idx + 1) % 4];
      } else if (step === 'forward') {
        let nx = cur.x;
        let ny = cur.y;
        if (cur.dir === 'N') ny -= 1;
        if (cur.dir === 'S') ny += 1;
        if (cur.dir === 'E') nx += 1;
        if (cur.dir === 'W') nx -= 1;

        // Check boundaries & walls
        const isWall = walls.some((w) => w.x === nx && w.y === ny);
        if (nx < 0 || nx >= gridSize || ny < 0 || ny >= gridSize || isWall) {
          sound.playMistake();
          setMessage('Ôi không! Robot TinTin đã va phải chướng ngại vật!');
          setIsRunning(false);
          return;
        }
        cur.x = nx;
        cur.y = ny;
      }
      setRobotPos({ ...cur });
    }

    // Check target reach
    if (cur.x === targetPos.x && cur.y === targetPos.y) {
      sound.playVictory();
      setMessage('Tuyệt vời! Robot đã đến đích và thu thập viên đá năng lượng!');
      onComplete(1.0);
    } else {
      sound.playMistake();
      setMessage('Robot chưa tới đích. Em hãy bổ sung thêm lệnh nhé!');
      onComplete(0.4);
    }
    setIsRunning(false);
  };

  const getRobotArrow = (dir: 'N' | 'E' | 'S' | 'W') => {
    switch (dir) {
      case 'N': return '▲';
      case 'E': return '▶';
      case 'S': return '▼';
      case 'W': return '◀';
    }
  };

  return (
    <div className="flex flex-col md:flex-row gap-6">
      {/* Mê cung Grid 2D */}
      <div className="flex-1 flex flex-col items-center justify-center bg-[#1a1c2c] p-4 border-3 border-[#5a6988]">
        <div
          className="grid gap-1.5 p-2 bg-[#181425] border-2 border-[#3a4466]"
          style={{
            gridTemplateColumns: `repeat(${gridSize}, minmax(0, 1fr))`,
            width: '260px',
            height: '260px',
          }}
        >
          {Array.from({ length: gridSize * gridSize }).map((_, idx) => {
            const x = idx % gridSize;
            const y = Math.floor(idx / gridSize);
            const isRobot = robotPos.x === x && robotPos.y === y;
            const isTarget = targetPos.x === x && targetPos.y === y;
            const isWall = walls.some((w) => w.x === x && w.y === y);

            return (
              <div
                key={idx}
                className={`relative flex items-center justify-center border transition-all ${
                  isWall
                    ? 'bg-[#3a4466] border-[#181425]'
                    : isTarget
                    ? 'bg-[#193c3e] border-[#38b764]'
                    : 'bg-[#262b44] border-[#3a4466]'
                }`}
              >
                {isWall && <span className="text-base">🧱</span>}
                {isTarget && !isRobot && <span className="text-xl animate-bounce">💎</span>}
                {isRobot && (
                  <div className="flex flex-col items-center">
                    <span className="text-lg">🤖</span>
                    <span className="text-[10px] text-[#fee761] font-bold">
                      {getRobotArrow(robotPos.dir)}
                    </span>
                  </div>
                )}
              </div>
            );
          })}
        </div>

        {message && (
          <div className="mt-3 text-xs font-bold text-[#fee761] bg-[#1f2438] px-3 py-1.5 border border-[#feae34] text-center w-full">
            {message}
          </div>
        )}
      </div>

      {/* Bảng khối lệnh */}
      <div className="flex-1 flex flex-col justify-between gap-4">
        <div>
          <div className="text-xs font-pixel text-[#8b9bb4] mb-2">CÁC KHỐI LỆNH CÓ SẴN:</div>
          <div className="grid grid-cols-2 gap-2">
            <PixelButton
              variant="blue"
              size="sm"
              onClick={() => addCommand('forward')}
              disabled={isRunning}
            >
              <ArrowUp size={14} /> Đi tới (1 ô)
            </PixelButton>
            <PixelButton
              variant="ghost"
              size="sm"
              onClick={() => addCommand('turn_left')}
              disabled={isRunning}
            >
              <TurnLeft size={14} /> Quay trái
            </PixelButton>
            <PixelButton
              variant="ghost"
              size="sm"
              onClick={() => addCommand('turn_right')}
              disabled={isRunning}
            >
              <TurnRight size={14} /> Quay phải
            </PixelButton>
            <PixelButton
              variant="accent"
              size="sm"
              onClick={() => addCommand('repeat_2')}
              disabled={isRunning}
            >
              <Repeat size={14} /> Lặp lại 2 lần
            </PixelButton>
          </div>
        </div>

        {/* Khay chương trình của em */}
        <div className="bg-[#181425] p-3 border-2 border-[#3a4466] min-h-[140px]">
          <div className="flex items-center justify-between mb-2">
            <span className="font-pixel text-[11px] text-[#38b764]">CHƯƠNG TRÌNH CỦA EM:</span>
            <span className="text-[10px] text-[#8b9bb4]">{commands.length}/8 lệnh</span>
          </div>
          <div className="flex flex-wrap gap-1.5">
            {commands.map((cmd, i) => (
              <span
                key={i}
                onClick={() => removeCommand(i)}
                className="bg-[#262b44] border border-[#5a6988] px-2 py-1 text-xs text-white cursor-pointer hover:border-[#e43b44] hover:bg-[#3e2731]"
                title="Bấm để xóa lệnh này"
              >
                {i + 1}. {cmd === 'forward' && '⬆ Đi tới'}
                {cmd === 'turn_left' && '↺ Quay trái'}
                {cmd === 'turn_right' && '↻ Quay phải'}
                {cmd === 'repeat_2' && '🔁 Lặp 2x'}
              </span>
            ))}
            {commands.length === 0 && (
              <span className="text-xs text-[#5a6988] italic py-6 text-center w-full">
                Bấm các nút lệnh ở trên để xếp thuật toán vào đây
              </span>
            )}
          </div>
        </div>

        {/* Nút hành động */}
        <div className="flex items-center justify-end gap-2">
          <PixelButton variant="ghost" size="md" onClick={handleReset} disabled={isRunning}>
            <RotateCcw size={16} /> Đặt lại
          </PixelButton>
          <PixelButton variant="primary" size="md" onClick={runCode} disabled={isRunning || commands.length === 0}>
            <Play size={16} /> Chạy thuật toán
          </PixelButton>
        </div>
      </div>
    </div>
  );
};
