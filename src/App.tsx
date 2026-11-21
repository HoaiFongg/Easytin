import React, { useState, useEffect } from 'react';
import curriculumData from '../curriculum.json';
import { CurriculumNode, CurriculumWorld, Grade, UserAccount, UserProgressState } from '../packages/domain/types';
import { LocalStorageAdapter } from '../packages/domain/storage';
import { AccountManager } from '../packages/domain/account';
import { LeitnerManager } from '../packages/domain/mastery';
import { Header } from './components/Header';
import { WorldMap } from './components/WorldMap';
import { AboutPage } from './components/AboutPage';
import { LessonModal } from './components/LessonModal';
import { LeitnerReviewModal } from './components/LeitnerReviewModal';
import { TeacherDashboardModal } from './components/TeacherDashboardModal';
import { ProgressSyncModal } from './components/ProgressSyncModal';
import { AuthModal } from './components/AuthModal';
import { UserProfileModal } from './components/UserProfileModal';
import { SettingsModal } from './components/SettingsModal';
import { sound } from '../packages/game-core/audio';
import { useI18n } from './i18nContext';
import { useTheme } from './ThemeContext';

export const App: React.FC = () => {
  const { t } = useI18n();
  const { effectiveTheme } = useTheme();
  const isLight = effectiveTheme === 'light';
  const [currentView, setCurrentView] = useState<'curriculum' | 'about'>('curriculum');
  const [currentAccount, setCurrentAccount] = useState<UserAccount | null>(() =>
    AccountManager.getActiveAccount()
  );

  const [progress, setProgress] = useState<UserProgressState>(() => {
    const active = AccountManager.getActiveAccount();
    return active ? active.progress : LocalStorageAdapter.loadProgress();
  });

  const [activeNode, setActiveNode] = useState<CurriculumNode | null>(null);
  const [showReviewModal, setShowReviewModal] = useState<boolean>(false);
  const [showTeacherModal, setShowTeacherModal] = useState<boolean>(false);
  const [showSyncModal, setShowSyncModal] = useState<boolean>(false);
  const [showAuthModal, setShowAuthModal] = useState<boolean>(false);
  const [showProfileModal, setShowProfileModal] = useState<boolean>(false);
  const [showSettingsModal, setShowSettingsModal] = useState<boolean>(false);

  // Lưu tiến độ học tập tương ứng với tài khoản đăng nhập hoặc chế độ khách
  useEffect(() => {
    if (currentAccount) {
      AccountManager.updateAccountProgress(currentAccount.id, progress);
    } else {
      LocalStorageAdapter.saveProgress(progress);
    }
  }, [progress, currentAccount]);

  const worlds = curriculumData.worlds as CurriculumWorld[];
  const nodes = curriculumData.nodes as CurriculumNode[];

  // Tìm thế giới tương ứng với khối lớp đang chọn
  const currentWorld =
    worlds.find((w) => w.grades.includes(progress.selectedGrade)) || worlds[0];

  // Đếm số bài đến hạn ôn tập Leitner hôm nay
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

  const handleAuthSuccess = (account: UserAccount) => {
    setCurrentAccount(account);
    setProgress(account.progress);
    setShowAuthModal(false);
  };

  const handleLogout = () => {
    AccountManager.logout();
    setCurrentAccount(null);
    setProgress(LocalStorageAdapter.loadProgress());
    setShowProfileModal(false);
  };

  const handleSwitchAccount = () => {
    setShowProfileModal(false);
    setShowAuthModal(true);
  };

  const handleProfileUpdate = (updated: UserAccount) => {
    setCurrentAccount(updated);
    if (updated.grade !== progress.selectedGrade) {
      setProgress((prev) => ({
        ...prev,
        selectedGrade: updated.grade,
      }));
    }
  };

  return (
    <div className={`min-h-screen flex flex-col transition-colors duration-150 ${
      isLight ? 'bg-[#f4f6fb] text-[#0f172a]' : 'bg-[#181425] text-white'
    }`}>
      {/* Header */}
      <Header
        progress={progress}
        dueCount={dueCount}
        currentAccount={currentAccount}
        currentView={currentView}
        onNavigate={setCurrentView}
        onGradeChange={handleGradeChange}
        onOpenReview={() => setShowReviewModal(true)}
        onOpenAuth={() => setShowAuthModal(true)}
        onOpenProfile={() => setShowProfileModal(true)}
        onOpenSettings={() => setShowSettingsModal(true)}
      />

      {/* Main Content Area */}
      <main className="flex-1 w-full px-4 sm:px-6 lg:px-8 xl:px-10 py-5 sm:py-7">
        {currentView === 'about' ? (
          <AboutPage onBackToCurriculum={() => setCurrentView('curriculum')} />
        ) : (
          <WorldMap
            currentWorld={currentWorld}
            selectedGrade={progress.selectedGrade}
            nodes={nodes}
            mastery={progress.mastery}
            onSelectNode={(node) => setActiveNode(node)}
            onGradeChange={handleGradeChange}
          />
        )}
      </main>

      {/* Footer */}
      <footer className={`border-t-2 py-4 text-center text-xs w-full transition-colors ${
        isLight
          ? 'bg-white border-[#cbd5e1] text-[#64748b]'
          : 'bg-[#1a1c2c] border-[#3a4466] text-[#8b9bb4]'
      }`}>
        <div className="w-full px-4 sm:px-6 lg:px-8 xl:px-10 flex flex-col sm:flex-row items-center justify-between gap-2">
          <div className="flex items-center gap-2.5">
            <span>{t('footer_copyright')}</span>
            <span className="opacity-40">·</span>
            <button
              onClick={() => {
                sound.playClick();
                setCurrentView((v) => (v === 'about' ? 'curriculum' : 'about'));
              }}
              className={`font-bold hover:underline cursor-pointer ${
                isLight ? 'text-[#0284c7]' : 'text-[#fee761]'
              }`}
            >
              {currentView === 'about' ? t('nav_curriculum') : t('nav_about')}
            </button>
          </div>
          <div className={`text-[11px] ${isLight ? 'text-[#94a3b8]' : 'text-[#5a6988]'}`}>
            {t('footer_standard')}
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

      {showAuthModal && (
        <AuthModal
          onClose={() => setShowAuthModal(false)}
          onAuthSuccess={handleAuthSuccess}
        />
      )}

      {showProfileModal && currentAccount && (
        <UserProfileModal
          account={currentAccount}
          onClose={() => setShowProfileModal(false)}
          onLogout={handleLogout}
          onSwitchAccount={handleSwitchAccount}
          onUpdateSuccess={handleProfileUpdate}
        />
      )}

      {showSettingsModal && (
        <SettingsModal
          progress={progress}
          onImportSuccess={(newProg) => setProgress(newProg)}
          onClose={() => setShowSettingsModal(false)}
        />
      )}
    </div>
  );
};
export default App;
