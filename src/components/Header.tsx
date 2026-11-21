import React from 'react';
import { Grade, UserAccount, UserProgressState } from '../../packages/domain/types';
import { useI18n } from '../i18nContext';
import { useTheme } from '../ThemeContext';
import { PixelLogo } from './PixelLogo';
import { PixelMascot } from './PixelMascot';
import { PixelXpIcon, PixelFlameIcon, PixelMapIcon, PixelInfoIcon } from './PixelIcons';
import { sound } from '../../packages/game-core/audio';
import { BookOpen, UserPlus, Settings, Sun, Moon } from 'lucide-react';

interface HeaderProps {
  progress: UserProgressState;
  dueCount: number;
  currentAccount: UserAccount | null;
  currentView?: 'curriculum' | 'about';
  onNavigate?: (view: 'curriculum' | 'about') => void;
  onGradeChange?: (grade: Grade) => void;
  onOpenReview: () => void;
  onOpenTeacher?: () => void;
  onOpenSync?: () => void;
  onOpenAuth: () => void;
  onOpenProfile: () => void;
  onOpenSettings: () => void;
}

export const Header: React.FC<HeaderProps> = ({
  progress,
  dueCount,
  currentAccount,
  currentView = 'curriculum',
  onNavigate,
  onOpenReview,
  onOpenAuth,
  onOpenProfile,
  onOpenSettings,
}) => {
  const { t, language } = useI18n();
  const { effectiveTheme, toggleTheme } = useTheme();
  const isLight = effectiveTheme === 'light';

  return (
    <header className={`sticky top-0 z-30 border-b-4 px-4 sm:px-6 lg:px-8 py-2.5 w-full transition-colors ${
      isLight
        ? 'bg-white border-[#cbd5e1] shadow-pixel-sm text-[#0f172a]'
        : 'bg-[#181425] border-[#3a4466] shadow-pixel text-white'
    }`}>
      <div className="w-full flex flex-wrap items-center justify-between gap-3">
        {/* Logo & Navigation Tabs */}
        <div className="flex items-center gap-3 sm:gap-4 flex-wrap">
          <div
            className="cursor-pointer transition-transform hover:scale-102"
            onClick={() => {
              if (onNavigate) {
                sound.playClick();
                onNavigate('curriculum');
              }
            }}
            title="EasyTin - Bản đồ học tập"
          >
            <PixelLogo size="md" />
          </div>

          {/* Navigation Tabs */}
          {onNavigate && (
            <nav className={`flex items-center p-0.5 border-2 ${
              isLight ? 'bg-[#f1f5f9] border-[#cbd5e1]' : 'bg-[#181425] border-[#3a4466]'
            }`}>
              <button
                onClick={() => {
                  sound.playClick();
                  onNavigate('curriculum');
                }}
                className={`flex items-center gap-1.5 px-2.5 py-1 text-xs font-bold transition-all cursor-pointer ${
                  currentView === 'curriculum'
                    ? isLight
                      ? 'bg-white text-[#0f172a] shadow-pixel-sm border border-[#94a3b8]'
                      : 'bg-[#262b44] text-[#fee761] border border-[#feae34]'
                    : isLight
                      ? 'text-[#64748b] hover:text-[#0f172a]'
                      : 'text-[#8b9bb4] hover:text-white'
                }`}
                title={t('nav_curriculum')}
              >
                <PixelMapIcon size={14} />
                <span>{t('nav_curriculum')}</span>
              </button>

              <button
                onClick={() => {
                  sound.playClick();
                  onNavigate('about');
                }}
                className={`flex items-center gap-1.5 px-2.5 py-1 text-xs font-bold transition-all cursor-pointer ${
                  currentView === 'about'
                    ? isLight
                      ? 'bg-white text-[#0f172a] shadow-pixel-sm border border-[#94a3b8]'
                      : 'bg-[#262b44] text-[#fee761] border border-[#feae34]'
                    : isLight
                      ? 'text-[#64748b] hover:text-[#0f172a]'
                      : 'text-[#8b9bb4] hover:text-white'
                }`}
                title={t('nav_about')}
              >
                <PixelInfoIcon size={14} />
                <span>{t('nav_about')}</span>
              </button>
            </nav>
          )}
        </div>

        {/* Stats & Actions */}
        <div className="flex items-center gap-2">
          {/* Nút Ôn tập Leitner */}
          <button
            onClick={() => {
              sound.playClick();
              onOpenReview();
            }}
            className={`flex items-center gap-1.5 border-2 px-2.5 py-1 text-xs font-bold cursor-pointer transition-all shadow-pixel-sm ${
              isLight
                ? 'bg-[#fffbeb] hover:bg-[#fef3c7] text-[#92400e] border-[#f59e0b]'
                : 'bg-[#262b44] hover:bg-[#3a4466] text-white border-[#feae34]'
            }`}
            title={t('review_box_title')}
          >
            <BookOpen size={14} className={isLight ? 'text-[#d97706]' : 'text-[#feae34]'} />
            <span>{t('review_button')}</span>
            {dueCount > 0 && (
              <span className="bg-[#e43b44] text-white text-[10px] px-1.5 rounded-full font-bold animate-pulse anim-pulse-glow">
                {dueCount}
              </span>
            )}
          </button>

          {/* XP */}
          <div className={`flex items-center gap-1.5 border px-2 py-1 text-xs shadow-pixel-sm transition-transform hover:scale-105 cursor-default ${
            isLight
              ? 'bg-[#fefce8] border-[#fde047] text-[#854d0e]'
              : 'bg-[#1a1c2c] border-[#3a4466]'
          }`}>
            <PixelXpIcon size={14} />
            <span className={`font-pixel text-[11px] ${isLight ? 'text-[#b45309]' : 'text-[#fee761]'}`}>{progress.xp}</span>
            <span className={`text-[10px] ${isLight ? 'text-[#854d0e]' : 'text-[#8b9bb4]'}`}>{t('xp_label')}</span>
          </div>

          {/* Streak */}
          <div className={`flex items-center gap-1.5 border px-2 py-1 text-xs shadow-pixel-sm transition-transform hover:scale-105 cursor-default ${
            isLight
              ? 'bg-[#fff7ed] border-[#fdba74] text-[#9a3412]'
              : 'bg-[#1a1c2c] border-[#3a4466]'
          }`}>
            <PixelFlameIcon size={14} />
            <span className="font-pixel text-[11px] text-[#f77622]">{progress.streakDays}</span>
            <span className={`text-[10px] ${isLight ? 'text-[#9a3412]' : 'text-[#8b9bb4]'}`}>{t('streak_days')}</span>
          </div>

          {/* Tài khoản Người học */}
          {currentAccount ? (
            <button
              onClick={() => {
                sound.playClick();
                onOpenProfile();
              }}
              className={`flex items-center gap-1.5 border-2 px-2 py-1 text-xs cursor-pointer transition-all shadow-pixel-sm shrink-0 ${
                isLight
                  ? 'bg-[#f0f9ff] hover:bg-[#e0f2fe] border-[#0284c7] text-[#0f172a]'
                  : 'bg-[#1f263e] hover:bg-[#2b3557] border-[#2ce8f5]'
              }`}
              title={currentAccount.fullName}
            >
              <PixelMascot mascotId={currentAccount.avatarId} size={24} animated={true} />
              <div className="flex flex-col text-left leading-tight">
                <span className={`font-bold text-[11px] max-w-[95px] truncate ${isLight ? 'text-[#0f172a]' : 'text-white'}`}>
                  {currentAccount.fullName}
                </span>
                <span className={`text-[9px] font-semibold ${isLight ? 'text-[#0284c7]' : 'text-[#2ce8f5]'}`}>
                  {t('grade_prefix')} {currentAccount.grade}
                </span>
              </div>
            </button>
          ) : (
            <button
              onClick={() => {
                sound.playClick();
                onOpenAuth();
              }}
              className={`flex items-center gap-1.5 border-2 px-2.5 py-1 text-xs font-bold cursor-pointer transition-all shadow-pixel-sm shrink-0 ${
                isLight
                  ? 'bg-[#16a34a] hover:bg-[#15803d] text-white border-[#15803d]'
                  : 'bg-[#1a2e22] hover:bg-[#234230] text-[#38b764] hover:text-[#fee761] border-[#38b764]'
              }`}
              title={t('account_button')}
            >
              <UserPlus size={14} />
              <span className="hidden sm:inline">{t('account_button')}</span>
              <span className="sm:hidden">{t('account_button_short')}</span>
            </button>
          )}

          {/* Nút Cài đặt trang web tổng hợp (Dạng danh sách đầy đủ) */}
          <button
            onClick={() => {
              sound.playClick();
              onOpenSettings();
            }}
            className={`flex items-center gap-1.5 border-2 px-2.5 py-1 text-xs cursor-pointer shadow-pixel-sm transition-all ${
              isLight
                ? 'bg-white hover:bg-[#f8fafc] border-[#0284c7] text-[#0f172a]'
                : 'bg-[#262b44] hover:bg-[#3a4466] border-[#2ce8f5] hover:border-[#fee761] text-white'
            }`}
            title={t('settings_title')}
          >
            <Settings size={15} className={isLight ? 'text-[#0284c7]' : 'text-[#2ce8f5]'} />
            <span className="font-bold text-xs">{t('settings_button')}</span>
            <span className={`text-[10px] px-1.5 py-0.2 font-mono border ${
              isLight
                ? 'bg-[#f1f5f9] text-[#0284c7] border-[#cbd5e1]'
                : 'bg-[#181425] text-[#fee761] border-[#3a4466]'
            }`}>
              {language === 'vi' ? 'VI' : 'EN'}
            </span>
          </button>

          {/* Nút Chuyển đổi Giao diện Sáng / Tối nhanh */}
          <button
            onClick={() => {
              sound.playClick();
              toggleTheme();
            }}
            className={`flex items-center gap-1 border-2 px-2 py-1 text-xs cursor-pointer shadow-pixel-sm transition-all ${
              isLight
                ? 'bg-white hover:bg-[#f8fafc] border-[#cbd5e1] text-[#0f172a]'
                : 'bg-[#262b44] hover:bg-[#3a4466] border-[#5a6988] hover:border-[#fee761] text-white'
            }`}
            title={t('theme_toggle_title')}
          >
            {isLight ? (
              <>
                <Moon size={15} className="text-[#0284c7]" />
                <span className="hidden sm:inline text-[11px] font-bold text-[#0284c7]">Tối</span>
              </>
            ) : (
              <>
                <Sun size={15} className="text-[#fee761]" />
                <span className="hidden sm:inline text-[11px] font-bold text-[#fee761]">Sáng</span>
              </>
            )}
          </button>
        </div>
      </div>
    </header>
  );
};
