import React from 'react';
import { CurriculumNode, NodeMasteryRecord } from '../../packages/domain/types';
import { LeitnerManager } from '../../packages/domain/mastery';
import { PixelButton } from './PixelButton';
import { sound } from '../../packages/game-core/audio';
import { X, BookOpen, Play } from 'lucide-react';

interface LeitnerReviewModalProps {
  nodes: CurriculumNode[];
  mastery: Record<string, NodeMasteryRecord>;
  onClose: () => void;
  onStartReviewNode: (node: CurriculumNode) => void;
}

export const LeitnerReviewModal: React.FC<LeitnerReviewModalProps> = ({
  nodes,
  mastery,
  onClose,
  onStartReviewNode,
}) => {
  const now = Date.now();

  // Group nodes by Leitner boxes
  const box1Nodes: CurriculumNode[] = [];
  const box2Nodes: CurriculumNode[] = [];
  const box3Nodes: CurriculumNode[] = [];
  const box4Nodes: CurriculumNode[] = [];

  nodes.forEach((n) => {
    const rec = mastery[n.id];
    if (rec?.isCompleted) {
      if (rec.box === 1) box1Nodes.push(n);
      if (rec.box === 2) box2Nodes.push(n);
      if (rec.box === 3) box3Nodes.push(n);
      if (rec.box === 4) box4Nodes.push(n);
    }
  });

  const dueNodes = nodes.filter((n) => {
    const rec = mastery[n.id];
    return rec && LeitnerManager.isDueForReview(rec, now);
  });

  return (
    <div className="fixed inset-0 z-50 bg-black/80 flex items-center justify-center p-3 sm:p-5 overflow-y-auto">
      <div className="bg-[#181425] border-4 border-[#feae34] shadow-pixel-lg w-full max-w-3xl max-h-[90vh] flex flex-col overflow-hidden anim-pixel-pop-in">
        {/* Header */}
        <div className="flex items-center justify-between bg-[#262b44] px-4 py-3 border-b-3 border-[#3a4466]">
          <div className="flex items-center gap-2">
            <BookOpen size={18} className="text-[#feae34]" />
            <span className="text-xs font-black text-[#fee761] uppercase tracking-wider">
              HỘP ÔN TẬP THÔNG MINH (LEITNER 4 HỘP)
            </span>
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

        {/* 4 Hộp Leitner */}
        <div className="p-5 overflow-y-auto flex flex-col gap-6">
          <div className="text-xs text-[#c0cbdc] leading-relaxed bg-[#262b44] p-3 border border-[#3a4466]">
            Phương pháp lặp lại ngắt quãng (Spaced Repetition) giúp em ghi nhớ kiến thức Tin học vào trí nhớ dài hạn mà không cần học vẹt!
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
            {[
              { box: 1, interval: '1 ngày', count: box1Nodes.length, color: '#e43b44' },
              { box: 2, interval: '3 ngày', count: box2Nodes.length, color: '#f77622' },
              { box: 3, interval: '7 ngày', count: box3Nodes.length, color: '#2ce8f5' },
              { box: 4, interval: '21 ngày (Thuần thục)', count: box4Nodes.length, color: '#38b764' },
            ].map((b) => (
              <div
                key={b.box}
                className="bg-[#1a1c2c] border-2 border-[#3a4466] p-3 text-center flex flex-col items-center"
              >
                <div className="text-xs font-black text-[#fee761] uppercase mb-1">Hộp {b.box}</div>
                <div className="font-pixel text-xl my-1" style={{ color: b.color }}>
                  {b.count}
                </div>
                <div className="text-[10px] text-[#8b9bb4]">Lặp lại: {b.interval}</div>
              </div>
            ))}
          </div>

          {/* Các bài đến hạn hôm nay */}
          <div>
            <div className="text-xs font-black text-[#fee761] uppercase tracking-wider mb-3 flex items-center justify-between">
              <span>BÀI HỌC CẦN ÔN TẬP HÔM NAY ({dueNodes.length}):</span>
            </div>

            <div className="flex flex-col gap-2.5">
              {dueNodes.map((node) => (
                <div
                  key={node.id}
                  className="bg-[#262b44] border-2 border-[#5a6988] p-3 flex items-center justify-between hover:border-[#feae34]"
                >
                  <div>
                    <div className="font-bold text-xs text-white">{node.title}</div>
                    <div className="text-[10px] text-[#8b9bb4]">Lớp {node.grade} · {node.standard_domain}</div>
                  </div>
                  <PixelButton
                    variant="accent"
                    size="sm"
                    onClick={() => {
                      sound.playClick();
                      onStartReviewNode(node);
                    }}
                  >
                    Ôn ngay <Play size={12} />
                  </PixelButton>
                </div>
              ))}

              {dueNodes.length === 0 && (
                <div className="text-center py-8 text-xs text-[#8b9bb4] italic border border-dashed border-[#3a4466]">
                  🎉 Tuyệt vời! Em đã hoàn thành mọi lượt ôn tập cho hôm nay rồi!
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
