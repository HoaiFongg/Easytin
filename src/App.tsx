import React, { useState, useEffect } from 'react';
import curriculumData from '../curriculum.json';
import { CurriculumNode, CurriculumWorld, Grade, UserProgressState } from '../packages/domain/types';
import { LocalStorageAdapter } from '../packages/domain/storage';
import { LeitnerManager } from '../packages/domain/mastery';
import { Header } from './components/Header';
import { WorldMap } from './components/WorldMap';
import { LessonModal } from './components/LessonModal';
import { LeitnerReviewModal } from './components/LeitnerReviewModal';
import { TeacherDashboardModal } from './components/TeacherDashboardModal';
import { ProgressSyncModal } from './components/ProgressSyncModal';

export const App: React.FC = () => {
  const [progress, setProgress] = useState<UserProgressState>(() => LocalStorageAdapter.loadProgress());
  const [activeNode, setActiveNode] = useState<CurriculumNode | null>(null);
  const [showReviewModal, setShowReviewModal] = useState<boolean>(false);
  const [showTeacherModal, setShowTeacherModal] = useState<boolean>(false);
  const [showSyncModal, setShowSyncModal] = useState<boolean>(false);

  // Save progress changes
  useEffect(() => {
    LocalStorageAdapter.saveProgress(progress);
  }, [progress]);

  const worlds = curriculumData.worlds as CurriculumWorld[];
  const nodes = curriculumData.nodes as CurriculumNode[];

  // Find world corresponding to selected grade
  const currentWorld =
    worlds.find((w) => w.grades.includes(progress.selectedGrade)) || worlds[0];

  // Count due nodes for Leitner spaced repetition today
  const dueCount = nodes.filter((n) => {
    const rec = progress.mastery[n.id];
    return rec && LeitnerManager.isDueForReview(rec, Date.now());
  }).length;

  const handleGradeChange = (grade: Grade) => {
    setProgress((prev) => ({
      ...prev,
      selectedGrade: grade,
    }));
  };

  const handleFinishLesson = (score: number) => {
    if (!activeNode) return;
    const currentRec =
      progress.mastery[activeNode.id] || LeitnerManager.createInitialRecord(activeNode.id);
    const updatedRec = LeitnerManager.processAttempt(currentRec, score, Date.now());

    const gainedXp = Math.round(score * 100);

    setProgress((prev) => ({
      ...prev,
      xp: prev.xp + gainedXp,
      mastery: {
        ...prev.mastery,
        [activeNode.id]: updatedRec,
      },
    }));

    setActiveNode(null);
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#181425] text-white">
      {/* Header */}
      <Header
        progress={progress}
        dueCount={dueCount}
        onGradeChange={handleGradeChange}
        onOpenReview={() => setShowReviewModal(true)}
        onOpenTeacher={() => setShowTeacherModal(true)}
        onOpenSync={() => setShowSyncModal(true)}
      />

      {/* Main Content Area */}
      <main className="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6">
        <WorldMap
          currentWorld={currentWorld}
          selectedGrade={progress.selectedGrade}
          nodes={nodes}
          mastery={progress.mastery}
          onSelectNode={(node) => setActiveNode(node)}
        />
      </main>

      {/* Footer */}
      <footer className="bg-[#1a1c2c] border-t-2 border-[#3a4466] py-4 text-center text-xs text-[#8b9bb4]">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
          <div>
            EasyTin © 2026 — Nền tảng học Tin học dạng game Pixel cho học sinh Việt Nam.
          </div>
          <div className="text-[11px] text-[#5a6988]">
            Đồng bộ chuẩn GDPT 2018 · KNTT · Cánh Diều · Chân trời sáng tạo · 100% Offline PWA Ready
          </div>
        </div>
      </footer>

      {/* Modals */}
      {activeNode && (
        <LessonModal
          node={activeNode}
          onClose={() => setActiveNode(null)}
          onFinishLesson={handleFinishLesson}
        />
      )}

      {showReviewModal && (
        <LeitnerReviewModal
          nodes={nodes}
          mastery={progress.mastery}
          onClose={() => setShowReviewModal(false)}
          onStartReviewNode={(node) => {
            setShowReviewModal(false);
            setActiveNode(node);
          }}
        />
      )}

      {showTeacherModal && (
        <TeacherDashboardModal onClose={() => setShowTeacherModal(false)} />
      )}

      {showSyncModal && (
        <ProgressSyncModal
          progress={progress}
          onImportSuccess={(newProg) => setProgress(newProg)}
          onClose={() => setShowSyncModal(false)}
        />
      )}
    </div>
  );
};
export default App;
