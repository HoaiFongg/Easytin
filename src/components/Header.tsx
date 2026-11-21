import React, { useState } from 'react';
import { Grade, UserAccount, UserProgressState } from '../../packages/domain/types';
import { AVATAR_OPTIONS } from '../../packages/domain/account';
import { PixelButton } from './PixelButton';
import { sound } from '../../packages/game-core/audio';
import { Volume2, VolumeX, Sparkles, Flame, BookOpen, GraduationCap, Share2, UserPlus } from 'lucide-react';

interface HeaderProps {
  progress: UserProgressState;
  dueCount: number;
  currentAccount: UserAccount | null;
  onGradeChange: (grade: Grade) => void;
  onOpenReview: () => void;
  onOpenTeacher: () => void;
  onOpenSync: () => void;
  onOpenAuth: () => void;
  onOpenProfile: () => void;
}

export const Header: React.FC<HeaderProps> = ({
  progress,
  dueCount,
  currentAccount,
  onGradeChange,
  onOpenReview,
  onOpenTeacher,
  onOpenSync,
  onOpenAuth,
  onOpenProfile,
}) => {
  const [isMuted, setIsMuted] = useState(sound.getMuted());

  const activeAvatar = currentAccount
    ? AVATAR_OPTIONS.find((a) => a.id === currentAccount.avatarId) || AVATAR_OPTIONS[0]
    : null;

  const toggleSound = () => {
    const next = !isMuted;
    sound.setMuted(next);
    setIsMuted(next);
    if (!next) sound.playClick();
  };

  return (
    <header className="sticky top-0 z-30 bg-[#181425] border-b-4 border-[#3a4466] px-4 py-2.5 shadow-pixel">
      <div className="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
        {/* Logo & Slogan */}
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-2 cursor-pointer" onClick={() => sound.playJump()}>
            <div className="w-9 h-9 bg-[#38b764] border-2 border-white flex items-center justify-center font-pixel text-lg text-black shadow-pixel-sm">
              ET
            </div>
            <div>
              <div className="font-pixel text-base text-[#fee761] tracking-wider flex items-center gap-1.5">
                EasyTin
              </div>
              <div className="text-[11px] text-[#8b9bb4]">Tin học GDPT 2018 · Lớp 3–12</div>
            </div>
          </div>
        </div>

        {/* Khối lớp Selector chia theo 3 Cấp: Tiểu học · THCS · THPT */}
        <div className="flex items-center gap-1.5 overflow-x-auto py-1 max-w-full">
          {/* Nhóm Cấp Tiểu học */}
          <div className="flex items-center gap-1 bg-[#1a2e22] px-2 py-1 border border-[#2b5c3f] shadow-pixel-sm shrink-0">
            <span className="text-[10px] font-black text-[#38b764] uppercase tracking-wider flex items-center gap-1">
              <span>🎒</span> <span className="hidden sm:inline">Tiểu học:</span>
            </span>
            {([3, 4, 5] as Grade[]).map((g) => {
              const isSelected = progress.selectedGrade === g;
              return (
                <button
                  key={g}
                  onClick={() => {
                    sound.playClick();
                    onGradeChange(g);
                  }}
                  className={`px-2 py-0.5 text-xs font-bold transition-all border ${
                    isSelected
                      ? 'bg-[#fee761] text-black border-white shadow-pixel-sm -translate-y-0.5 font-black'
                      : 'bg-[#262b44] text-[#c0cbdc] border-[#3a4466] hover:border-[#5a6988]'
                  }`}
                >
                  Lớp {g}
                </button>
              );
            })}
          </div>

          {/* Nhóm Cấp THCS */}
          <div className="flex items-center gap-1 bg-[#1a2538] px-2 py-1 border border-[#1f3b5c] shadow-pixel-sm shrink-0">
            <span className="text-[10px] font-black text-[#2ce8f5] uppercase tracking-wider flex items-center gap-1">
              <span>🌲</span> <span className="hidden sm:inline">THCS:</span>
            </span>
            {([6, 7, 8, 9] as Grade[]).map((g) => {
              const isSelected = progress.selectedGrade === g;
              return (
                <button
                  key={g}
                  onClick={() => {
                    sound.playClick();
                    onGradeChange(g);
                  }}
                  className={`px-2 py-0.5 text-xs font-bold transition-all border ${
                    isSelected
                      ? 'bg-[#fee761] text-black border-white shadow-pixel-sm -translate-y-0.5 font-black'
                      : 'bg-[#262b44] text-[#c0cbdc] border-[#3a4466] hover:border-[#5a6988]'
                  }`}
                >
                  Lớp {g}
                </button>
              );
            })}
          </div>

          {/* Nhóm Cấp THPT */}
          <div className="flex items-center gap-1 bg-[#321e2f] px-2 py-1 border border-[#5c2b4e] shadow-pixel-sm shrink-0">
            <span className="text-[10px] font-black text-[#fca3ca] uppercase tracking-wider flex items-center gap-1">
              <span>🏛️</span> <span className="hidden sm:inline">THPT:</span>
            </span>
            {([10, 11, 12] as Grade[]).map((g) => {
              const isSelected = progress.selectedGrade === g;
              return (
                <button
                  key={g}
                  onClick={() => {
                    sound.playClick();
                    onGradeChange(g);
                  }}
                  className={`px-2 py-0.5 text-xs font-bold transition-all border ${
                    isSelected
                      ? 'bg-[#fee761] text-black border-white shadow-pixel-sm -translate-y-0.5 font-black'
                      : 'bg-[#262b44] text-[#c0cbdc] border-[#3a4466] hover:border-[#5a6988]'
                  }`}
                >
                  Lớp {g}
                </button>
              );
            })}
          </div>
        </div>

        {/* Stats & Actions */}
        <div className="flex items-center gap-2">
          {/* Nút Ôn tập Leitner */}
          <button
            onClick={() => {
              sound.playClick();
              onOpenReview();
            }}
            className="flex items-center gap-1.5 bg-[#262b44] hover:bg-[#3a4466] text-white border-2 border-[#feae34] px-2.5 py-1 text-xs font-bold cursor-pointer transition-colors"
            title="Hộp ôn tập thông minh (Leitner)"
          >
            <BookOpen size={14} className="text-[#feae34]" />
            <span>Ôn tập</span>
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
            <span className="text-[10px] text-[#8b9bb4]">XP</span>
          </div>

          {/* Streak */}
          <div className="flex items-center gap-1 bg-[#1a1c2c] border border-[#3a4466] px-2 py-1 text-xs">
            <Flame size={14} className="text-[#f77622]" />
            <span className="font-pixel text-[11px] text-[#f77622]">{progress.streakDays}</span>
            <span className="text-[10px] text-[#8b9bb4]">ngày</span>
          </div>

          {/* Tài khoản Người học */}
          {currentAccount ? (
            <button
              onClick={() => {
                sound.playClick();
                onOpenProfile();
              }}
              className="flex items-center gap-1.5 bg-[#1f263e] hover:bg-[#2b3557] border-2 border-[#2ce8f5] px-2 py-1 text-xs cursor-pointer transition-all shadow-pixel-sm shrink-0"
              title="Nhấp để xem hồ sơ và thành tích học tập"
            >
              <span className="text-base">{activeAvatar?.icon || '🤖'}</span>
              <div className="flex flex-col text-left leading-tight">
                <span className="font-bold text-white text-[11px] max-w-[95px] truncate">
                  {currentAccount.fullName}
                </span>
                <span className="text-[9px] text-[#2ce8f5] font-semibold">
                  Lớp {currentAccount.grade}
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
              title="Tạo tài khoản hoặc đăng nhập để lưu thành tích học tập"
            >
              <UserPlus size={14} />
              <span className="hidden sm:inline">Tạo tài khoản / Đăng nhập</span>
              <span className="sm:hidden">Tài khoản</span>
            </button>
          )}

          {/* Thầy Cô / Lớp học */}
          <PixelButton variant="ghost" size="sm" onClick={onOpenTeacher} title="Cổng dành cho Giáo viên">
            <GraduationCap size={15} />
            <span className="hidden sm:inline">Giáo viên</span>
          </PixelButton>

          {/* Sao lưu / Thẻ tiến độ */}
          <PixelButton variant="ghost" size="sm" onClick={onOpenSync} title="Mã thẻ tiến độ">
            <Share2 size={14} />
          </PixelButton>

          {/* Bật/Tắt Âm thanh */}
          <button
            onClick={toggleSound}
            className="p-1.5 bg-[#262b44] border border-[#5a6988] text-[#c0cbdc] hover:text-white cursor-pointer"
            title={isMuted ? 'Bật âm thanh' : 'Tắt âm thanh'}
          >
            {isMuted ? <VolumeX size={16} /> : <Volume2 size={16} />}
          </button>
        </div>
      </div>
    </header>
  );
};
