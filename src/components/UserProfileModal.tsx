import React, { useState } from 'react';
import { Grade, UserAccount } from '../../packages/domain/types';
import { AccountManager, AVATAR_OPTIONS, getRankTitle } from '../../packages/domain/account';
import { PixelButton } from './PixelButton';
import { PixelMascot } from './PixelMascot';
import { PixelXpIcon, PixelFlameIcon, PixelStarIcon } from './PixelIcons';
import { sound } from '../../packages/game-core/audio';
import { X, User, Edit3, Key, LogOut, Users, Award, CheckCircle2, AlertCircle } from 'lucide-react';

interface UserProfileModalProps {
  account: UserAccount;
  onClose: () => void;
  onLogout: () => void;
  onSwitchAccount: () => void;
  onUpdateSuccess: (updated: UserAccount) => void;
}

export const UserProfileModal: React.FC<UserProfileModalProps> = ({
  account,
  onClose,
  onLogout,
  onSwitchAccount,
  onUpdateSuccess,
}) => {
  const [isEditing, setIsEditing] = useState(false);
  const [showPasswordChange, setShowPasswordChange] = useState(false);

  // Edit fields
  const [editFullName, setEditFullName] = useState(account.fullName);
  const [editGrade, setEditGrade] = useState<Grade>(account.grade);
  const [editSchool, setEditSchool] = useState(account.schoolName || '');
  const [editClass, setEditClass] = useState(account.className || '');
  const [editAvatarId, setEditAvatarId] = useState(account.avatarId);

  // Password fields
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  // Alerts
  const [errorMsg, setErrorMsg] = useState<string | null>(null);
  const [successMsg, setSuccessMsg] = useState<string | null>(null);

  const currentAvatar =
    AVATAR_OPTIONS.find((a) => a.id === (isEditing ? editAvatarId : account.avatarId)) ||
    AVATAR_OPTIONS[0];

  const rankTitle = getRankTitle(account.progress.xp, account.grade);

  // Đếm số bài đã hoàn thành
  const completedCount = Object.values(account.progress.mastery).filter(
    (m) => m.isCompleted
  ).length;

  // Đếm số bài đạt 3 sao
  const threeStarCount = Object.values(account.progress.mastery).filter(
    (m) => m.stars === 3
  ).length;

  const handleSaveProfile = (e: React.FormEvent) => {
    e.preventDefault();
    setErrorMsg(null);
    setSuccessMsg(null);

    const res = AccountManager.updateProfile(account.id, {
      fullName: editFullName,
      grade: editGrade,
      schoolName: editSchool,
      className: editClass,
      avatarId: editAvatarId,
    });

    if (res.success && res.account) {
      sound.playVictory();
      setSuccessMsg('Hồ sơ học tập đã được cập nhật thành công!');
      setIsEditing(false);
      onUpdateSuccess(res.account);
    } else {
      sound.playMistake();
      setErrorMsg(res.error || 'Không thể lưu hồ sơ.');
    }
  };

  const handleChangePassword = (e: React.FormEvent) => {
    e.preventDefault();
    setErrorMsg(null);
    setSuccessMsg(null);

    if (newPassword !== confirmPassword) {
      sound.playMistake();
      setErrorMsg('Mật khẩu xác nhận không trùng khớp.');
      return;
    }

    const res = AccountManager.updateProfile(account.id, {
      newPassword,
    });

    if (res.success && res.account) {
      sound.playVictory();
      setSuccessMsg('Mật khẩu đã được đổi thành công!');
      setShowPasswordChange(false);
      setNewPassword('');
      setConfirmPassword('');
      onUpdateSuccess(res.account);
    } else {
      sound.playMistake();
      setErrorMsg(res.error || 'Không thể đổi mật khẩu.');
    }
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/85 flex items-center justify-center p-3 sm:p-5 overflow-y-auto">
      <div className="bg-[#181425] border-4 border-[#2ce8f5] shadow-pixel-lg w-full max-w-xl max-h-[92vh] flex flex-col overflow-hidden my-auto anim-pixel-pop-in">
        {/* Header Modal */}
        <div className="flex items-center justify-between bg-[#262b44] px-4 py-3 border-b-3 border-[#3a4466]">
          <div className="flex items-center gap-2">
            <User size={18} className="text-[#2ce8f5]" />
            <span className="text-xs sm:text-sm font-black text-[#fee761] uppercase tracking-wider">
              HỒ SƠ HỌC SINH · {account.fullName}
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

        {/* Thông báo lỗi / thành công */}
        {(errorMsg || successMsg) && (
          <div className="px-5 pt-4">
            {errorMsg && (
              <div className="bg-[#421d26] border-2 border-[#e43b44] text-[#ffb6b9] p-3 text-xs flex items-start gap-2">
                <AlertCircle size={16} className="text-[#e43b44] shrink-0 mt-0.5" />
                <span>{errorMsg}</span>
              </div>
            )}
            {successMsg && (
              <div className="bg-[#1a3826] border-2 border-[#38b764] text-[#b6f0cd] p-3 text-xs flex items-start gap-2">
                <CheckCircle2 size={16} className="text-[#38b764] shrink-0 mt-0.5" />
                <span>{successMsg}</span>
              </div>
            )}
          </div>
        )}

        {/* Nội dung hồ sơ */}
        <div className="p-5 overflow-y-auto flex-1 flex flex-col gap-4">
          {!isEditing ? (
            <>
              {/* Thẻ định danh học sinh */}
              <div className="bg-[#1a1c2c] border-2 border-[#3a4466] p-4 flex flex-col sm:flex-row items-center gap-4">
                <div className="w-18 h-18 bg-[#262b44] border-2 border-[#fee761] flex items-center justify-center p-1 shadow-pixel-sm shrink-0 overflow-hidden">
                  <PixelMascot mascotId={currentAvatar.id} size={56} animated={true} />
                </div>
                <div className="flex-1 text-center sm:text-left">
                  <div className="flex items-center justify-center sm:justify-start gap-2 flex-wrap">
                    <span className="font-bold text-base text-white">{account.fullName}</span>
                    <span className="bg-[#262b44] text-[#fee761] text-xs px-2 py-0.5 font-mono border border-[#3a4466]">
                      @{account.username}
                    </span>
                  </div>
                  <div className="text-xs text-[#2ce8f5] font-semibold mt-1">
                    Lớp {account.grade} · {account.grade <= 5 ? 'Cấp Tiểu học' : account.grade <= 9 ? 'Cấp THCS' : 'Cấp THPT'}
                    {account.className ? ` · ${account.className}` : ''}
                    {account.schoolName ? ` (${account.schoolName})` : ''}
                  </div>
                  <div className="inline-block bg-[#262b44] border border-[#5a6988] px-2 py-0.5 text-[11px] text-[#fee761] font-bold mt-2">
                    🎖️ Danh hiệu: {rankTitle}
                  </div>
                </div>
              </div>

              {/* Thống kê học tập */}
              <div>
                <div className="text-xs font-black text-[#8b9bb4] uppercase tracking-wider mb-2">
                  📊 THÀNH TÍCH HỌC TẬP TÍCH LŨY:
                </div>
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
                  <div className="bg-[#262b44] border border-[#3a4466] p-2.5 text-center flex flex-col items-center">
                    <PixelXpIcon size={18} className="mb-1" />
                    <div className="font-pixel text-base text-[#fee761]">{account.progress.xp}</div>
                    <div className="text-[10px] text-[#8b9bb4]">Điểm XP</div>
                  </div>
                  <div className="bg-[#262b44] border border-[#3a4466] p-2.5 text-center flex flex-col items-center">
                    <PixelFlameIcon size={18} className="mb-1" />
                    <div className="font-pixel text-base text-[#f77622]">{account.progress.streakDays}</div>
                    <div className="text-[10px] text-[#8b9bb4]">Chuỗi ngày</div>
                  </div>
                  <div className="bg-[#262b44] border border-[#3a4466] p-2.5 text-center flex flex-col items-center">
                    <Award size={18} className="text-[#38b764] mb-1" />
                    <div className="font-pixel text-base text-[#38b764]">{completedCount}</div>
                    <div className="text-[10px] text-[#8b9bb4]">Bài hoàn thành</div>
                  </div>
                  <div className="bg-[#262b44] border border-[#3a4466] p-2.5 text-center flex flex-col items-center">
                    <PixelStarIcon size={18} filled={true} className="mb-1" />
                    <div className="font-pixel text-base text-[#feae34]">{threeStarCount}</div>
                    <div className="text-[10px] text-[#8b9bb4]">Bài đạt 3 sao</div>
                  </div>
                </div>
              </div>

              {/* Form Đổi mật khẩu nếu đang mở */}
              {showPasswordChange && (
                <form onSubmit={handleChangePassword} className="bg-[#262b44] border-2 border-[#fee761] p-3 flex flex-col gap-2.5">
                  <div className="text-xs font-bold text-[#fee761] flex items-center gap-1.5">
                    <Key size={14} /> Đổi mật khẩu mới:
                  </div>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                    <input
                      type="password"
                      required
                      placeholder="Mật khẩu mới (>= 4 ký tự)"
                      value={newPassword}
                      onChange={(e) => setNewPassword(e.target.value)}
                      className="bg-[#181425] border border-[#3a4466] p-2 text-xs text-white outline-none"
                    />
                    <input
                      type="password"
                      required
                      placeholder="Nhập lại mật khẩu mới"
                      value={confirmPassword}
                      onChange={(e) => setConfirmPassword(e.target.value)}
                      className="bg-[#181425] border border-[#3a4466] p-2 text-xs text-white outline-none"
                    />
                  </div>
                  <div className="flex justify-end gap-2">
                    <button
                      type="button"
                      onClick={() => setShowPasswordChange(false)}
                      className="px-2 py-1 text-xs text-[#8b9bb4] hover:text-white"
                    >
                      Hủy
                    </button>
                    <PixelButton variant="primary" size="sm">
                      Lưu mật khẩu
                    </PixelButton>
                  </div>
                </form>
              )}

              {/* Các nút hành động */}
              <div className="pt-2 flex flex-wrap gap-2">
                <PixelButton
                  variant="primary"
                  size="sm"
                  onClick={() => {
                    sound.playClick();
                    setIsEditing(true);
                  }}
                >
                  <Edit3 size={14} /> Chỉnh sửa hồ sơ
                </PixelButton>

                {!showPasswordChange && (
                  <PixelButton
                    variant="ghost"
                    size="sm"
                    onClick={() => {
                      sound.playClick();
                      setShowPasswordChange(true);
                    }}
                  >
                    <Key size={14} /> Đổi mật khẩu
                  </PixelButton>
                )}

                <PixelButton
                  variant="ghost"
                  size="sm"
                  onClick={() => {
                    sound.playClick();
                    onSwitchAccount();
                  }}
                >
                  <Users size={14} /> Đổi tài khoản
                </PixelButton>

                <PixelButton
                  variant="danger"
                  size="sm"
                  onClick={() => {
                    sound.playClick();
                    onLogout();
                  }}
                  className="ml-auto"
                >
                  <LogOut size={14} /> Đăng xuất
                </PixelButton>
              </div>
            </>
          ) : (
            /* Chế độ Chỉnh sửa hồ sơ */
            <form onSubmit={handleSaveProfile} className="flex flex-col gap-4">
              <div className="text-xs text-[#fee761] font-bold">
                ✏️ CẬP NHẬT THÔNG TIN HỒ SƠ HỌC SINH:
              </div>

              {/* Chọn Linh vật mới */}
              <div>
                <label className="block text-xs text-[#8b9bb4] mb-1.5">Linh vật đại diện:</label>
                <div className="grid grid-cols-3 gap-2">
                  {AVATAR_OPTIONS.map((av) => (
                    <div
                      key={av.id}
                      onClick={() => setEditAvatarId(av.id)}
                      className={`p-2 border cursor-pointer flex items-center gap-2 ${
                        editAvatarId === av.id
                          ? 'bg-[#262b44] border-[#fee761]'
                          : 'bg-[#181425] border-[#3a4466]'
                      }`}
                    >
                      <PixelMascot mascotId={av.id} size={28} animated={editAvatarId === av.id} />
                      <span className="text-[11px] font-bold truncate">{av.name}</span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Họ tên */}
              <div>
                <label className="block text-xs text-[#8b9bb4] mb-1">Họ và tên người học:</label>
                <input
                  type="text"
                  required
                  value={editFullName}
                  onChange={(e) => setEditFullName(e.target.value)}
                  className="w-full bg-[#181425] border-2 border-[#3a4466] focus:border-[#fee761] p-2 text-xs text-white outline-none"
                />
              </div>

              {/* Khối lớp */}
              <div>
                <label className="block text-xs text-[#8b9bb4] mb-1">Khối lớp:</label>
                <select
                  value={editGrade}
                  onChange={(e) => setEditGrade(Number(e.target.value) as Grade)}
                  className="w-full bg-[#181425] border-2 border-[#3a4466] focus:border-[#fee761] p-2 text-xs text-white outline-none"
                >
                  {[3, 4, 5, 6, 7, 8, 9, 10, 11, 12].map((g) => (
                    <option key={g} value={g}>
                      Lớp {g} ({g <= 5 ? 'Tiểu học' : g <= 9 ? 'THCS' : 'THPT'})
                    </option>
                  ))}
                </select>
              </div>

              {/* Trường lớp */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div>
                  <label className="block text-xs text-[#8b9bb4] mb-1">Trường học:</label>
                  <input
                    type="text"
                    value={editSchool}
                    onChange={(e) => setEditSchool(e.target.value)}
                    className="w-full bg-[#181425] border-2 border-[#3a4466] p-2 text-xs text-white outline-none"
                  />
                </div>
                <div>
                  <label className="block text-xs text-[#8b9bb4] mb-1">Lớp học:</label>
                  <input
                    type="text"
                    value={editClass}
                    onChange={(e) => setEditClass(e.target.value)}
                    className="w-full bg-[#181425] border-2 border-[#3a4466] p-2 text-xs text-white outline-none"
                  />
                </div>
              </div>

              <div className="flex justify-end gap-2 pt-2">
                <button
                  type="button"
                  onClick={() => setIsEditing(false)}
                  className="px-3 py-1.5 text-xs text-[#8b9bb4] hover:text-white"
                >
                  Hủy bỏ
                </button>
                <PixelButton variant="primary" size="sm">
                  Lưu thay đổi
                </PixelButton>
              </div>
            </form>
          )}
        </div>
      </div>
    </div>
  );
};
