import React, { useState } from 'react';
import { PixelButton } from '../components/PixelButton';
import { sound } from '../../packages/game-core/audio';
import { RotateCcw } from 'lucide-react';

interface CardItem {
  id: string;
  pairId: string;
  label: string;
  icon: string;
}

const DEFAULT_CARDS: CardItem[] = [
  { id: '1a', pairId: 'mouse', label: 'Chuột', icon: '🖱️' },
  { id: '1b', pairId: 'mouse', label: 'Thiết bị Vào', icon: '📥' },
  { id: '2a', pairId: 'monitor', label: 'Màn hình', icon: '🖥️' },
  { id: '2b', pairId: 'monitor', label: 'Thiết bị Ra', icon: '📤' },
  { id: '3a', pairId: 'ram', label: 'RAM', icon: '⚡' },
  { id: '3b', pairId: 'ram', label: 'Bộ nhớ tạm', icon: '🧠' },
  { id: '4a', pairId: 'hdd', label: 'Ổ đĩa cứng', icon: '💾' },
  { id: '4b', pairId: 'hdd', label: 'Lưu trữ lâu dài', icon: '🗄️' },
];

export const MatchMemoryGame: React.FC<{ onComplete: (score: number) => void }> = ({ onComplete }) => {
  const [cards, setCards] = useState<CardItem[]>(() => [...DEFAULT_CARDS].sort(() => Math.random() - 0.5));
  const [flipped, setFlipped] = useState<string[]>([]);
  const [matched, setMatched] = useState<string[]>([]);

  const handleCardClick = (card: CardItem) => {
    if (flipped.length >= 2 || flipped.includes(card.id) || matched.includes(card.id)) return;

    sound.playClick();
    const newFlipped = [...flipped, card.id];
    setFlipped(newFlipped);

    if (newFlipped.length === 2) {
      const first = cards.find((c) => c.id === newFlipped[0]);
      const second = cards.find((c) => c.id === newFlipped[1]);

      if (first && second && first.pairId === second.pairId) {
        sound.playCorrect();
        const nextMatched = [...matched, first.id, second.id];
        setMatched(nextMatched);
        setFlipped([]);

        if (nextMatched.length === cards.length) {
          sound.playVictory();
          onComplete(1.0);
        }
      } else {
        setTimeout(() => {
          sound.playMistake();
          setFlipped([]);
        }, 800);
      }
    }
  };

  const handleReset = () => {
    setCards([...DEFAULT_CARDS].sort(() => Math.random() - 0.5));
    setFlipped([]);
    setMatched([]);
  };

  return (
    <div className="flex flex-col items-center gap-5 bg-[#1a1c2c] p-5 border-3 border-[#5a6988]">
      <div className="flex items-center justify-between w-full border-b border-[#3a4466] pb-2">
        <span className="text-xs text-[#8b9bb4]">Lật 2 thẻ có nghĩa tương ứng để ghép cặp:</span>
        <PixelButton variant="ghost" size="sm" onClick={handleReset}>
          <RotateCcw size={14} /> Xáo lại
        </PixelButton>
      </div>

      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 w-full max-w-md">
        {cards.map((card) => {
          const isFlipped = flipped.includes(card.id) || matched.includes(card.id);
          const isMatched = matched.includes(card.id);

          return (
            <div
              key={card.id}
              onClick={() => handleCardClick(card)}
              className={`h-24 border-3 cursor-pointer flex flex-col items-center justify-center p-2 text-center transition-all ${
                isMatched
                  ? 'bg-[#193c3e] border-[#38b764] opacity-80'
                  : isFlipped
                  ? 'bg-[#3a4466] border-[#fee761] shadow-pixel'
                  : 'bg-[#262b44] border-[#5a6988] hover:border-[#8b9bb4]'
              }`}
            >
              {isFlipped ? (
                <>
                  <span className="text-xl mb-1">{card.icon}</span>
                  <span className="text-xs font-bold leading-tight">{card.label}</span>
                </>
              ) : (
                <span className="font-pixel text-xl text-[#5a6988]">?</span>
              )}
            </div>
          );
        })}
      </div>

      {matched.length === cards.length && (
        <div className="text-sm font-bold text-[#38b764] animate-bounce">
          🎉 CHÚC MỪNG! Em đã ghép đúng toàn bộ thẻ thuật ngữ!
        </div>
      )}
    </div>
  );
};
