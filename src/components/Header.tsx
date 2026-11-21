import React from 'react';
import { Grade, UserAccount, UserProgressState } from '../../packages/domain/types';
import { useI18n } from '../i18nContext';
import { useTheme } from '../ThemeContext';
import { PixelLogo } from './PixelLogo';
import { PixelMascot } from './PixelMascot';
import { sound } from '../../packages/game-core/audio';
import { Sparkles, Flame, BookOpen, UserPlus, Settings, Sun, Moon } from 'lucide-react';

interface HeaderProps {
  progress: UserProgressState;
  dueCount: number;
  currentAccount: UserAccount | null;
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
  onOpenReview,
  onOpenAuth,
  onOpenProfile,
  onOpenSettings,
}) => {
  const { t, language } = useI18n();
  const { effectiveTheme, toggleTheme } = useTheme();

  return (
    <header className="sticky top-0 z-30 bg-[#181425] border-b-4 border-[#3a4466] px-4 sm:px-6 lg:px-8 py-2.5 shadow-pixel w-full">
      <div className="w-full flex flex-wrap items-center justify-between gap-3">
        {/* Logo & Slogan */}
        <PixelLogo size="md" />

        {/* Stats & Actions */}
        <div className="flex items-center gap-2">
          {/* Nút Ôn tập Leitner */}
          <button
            onClick={() => {
              sound.playClick();
              onOpenReview();
            }}
            className="flex items-center gap-1.5 bg-[#262b44] hover:bg-[#3a4466] text-white border-2 border-[#feae34] px-2.5 py-1 text-xs font-bold cursor-pointer transition-colors"
            title={t('review_box_title')}
          >
            <BookOpen size={14} className="text-[#feae34]" />
            <span>{t('review_button')}</span>
            {dueCount > 0 && (
              <span className="bg-[#e43b44] text-white text-[10px] px-1.5 rounded-full font-bold animate-pulse">
                {dueCount}
              </span>
            )}
          </button>

          {/* XP */}
          <div className="flex items-center gap-1 bg-[#1a1c2c] border border-[#3a4466] px-2 py-1 text-xs">
            <Sparkles size={14} className="text-[#fee761]" />
            <span className="font-pixel text-[11px] text-[#fee761]">{progress.xp}</span>
            <span className="text-[10px] text-[#8b9bb4]">{t('xp_label')}</span>
          </div>

          {/* Streak */}
          <div className="flex items-center gap-1 bg-[#1a1c2c] border border-[#3a4466] px-2 py-1 text-xs">
            <Flame size={14} className="text-[#f77622]" />
            <span className="font-pixel text-[11px] text-[#f77622]">{progress.streakDays}</span>
            <span className="text-[10px] text-[#8b9bb4]">{t('streak_days')}</span>
          </div>

          {/* Tài khoản Người học */}
          {currentAccount ? (
            <button
              onClick={() => {
                sound.playClick();
                onOpenProfile();
              }}
              className="flex items-center gap-1.5 bg-[#1f263e] hover:bg-[#2b3557] border-2 border-[#2ce8f5] px-2 py-1 text-xs cursor-pointer transition-all shadow-pixel-sm shrink-0"
              title={currentAccount.fullName}
            >
              <PixelMascot mascotId={currentAccount.avatarId} size={24} animated={true} />
              <div className="flex flex-col text-left leading-tight">
                <span className="font-bold text-white text-[11px] max-w-[95px] truncate">
                  {currentAccount.fullName}
                </span>
                <span className="text-[9px] text-[#2ce8f5] font-semibold">
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
              className="flex items-center gap-1.5 bg-[#1a2e22] hover:bg-[#234230] text-[#38b764] hover:text-[#fee761] border-2 border-[#38b764] px-2 py-1 text-xs font-bold cursor-pointer transition-all shadow-pixel-sm shrink-0"
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
            className="flex items-center gap-1.5 bg-[#262b44] hover:bg-[#3a4466] border-2 border-[#2ce8f5] hover:border-[#fee761] px-2.5 py-1 text-xs text-white cursor-pointer shadow-pixel-sm transition-all"
            title={t('settings_title')}
          >
            <Settings size={15} className="text-[#2ce8f5]" />
            <span className="font-bold text-xs">{t('settings_button')}</span>
            <span className="text-[10px] bg-[#181425] text-[#fee761] px-1.5 py-0.2 font-mono border border-[#3a4466]">
              {language === 'vi' ? 'VI' : 'EN'}
            </span>
          </button>

          {/* Nút Chuyển đổi Giao diện Sáng / Tối nhanh */}
          <button
            onClick={() => {
              sound.playClick();
              toggleTheme();
            }}
            className="flex items-center gap-1 bg-[#262b44] hover:bg-[#3a4466] border-2 border-[#5a6988] hover:border-[#fee761] px-2 py-1 text-xs text-white cursor-pointer shadow-pixel-sm transition-all"
            title={t('theme_toggle_title')}
          >
            {effectiveTheme === 'dark' ? (
              <>
                <Sun size={15} className="text-[#fee761]" />
                <span className="hidden sm:inline text-[11px] font-bold text-[#fee761]">Sáng</span>
              </>
            ) : (
              <>
                <Moon size={15} className="text-[#2ce8f5]" />
                <span className="hidden sm:inline text-[11px] font-bold text-[#2ce8f5]">Tối</span>
              </>
            )}
          </button>
        </div>
      </div>
    </header>
  );
};
