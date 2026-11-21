import React, { useState } from 'react';
import { Grade, UserAccount } from '../../packages/domain/types';
import { AccountManager, AVATAR_OPTIONS } from '../../packages/domain/account';
import { PixelButton } from './PixelButton';
import { sound } from '../../packages/game-core/audio';
import { X, UserPlus, LogIn, Users, Eye, EyeOff, AlertCircle, CheckCircle2, Trash2 } from 'lucide-react';

interface AuthModalProps {
  initialTab?: 'register' | 'login' | 'accounts';
  onClose: () => void;
  onAuthSuccess: (account: UserAccount) => void;
}

export const AuthModal: React.FC<AuthModalProps> = ({
  initialTab = 'register',
  onClose,
  onAuthSuccess,
}) => {
  const existingAccounts = AccountManager.getAccounts();
  const [tab, setTab] = useState<'register' | 'login' | 'accounts'>(
    existingAccounts.length > 0 && initialTab === 'register' ? 'register' : initialTab
  );

  // Form Đăng ký
  const [regFullName, setRegFullName] = useState('');
  const [regUsername, setRegUsername] = useState('');
  const [regPassword, setRegPassword] = useState('');
  const [regConfirmPass, setRegConfirmPass] = useState('');
  const [regGrade, setRegGrade] = useState<Grade>(3);
  const [regSchool, setRegSchool] = useState('');
  const [regClass, setRegClass] = useState('');
  const [regAvatarId, setRegAvatarId] = useState('tin_bot');

  // Form Đăng nhập
  const [loginUsername, setLoginUsername] = useState('');
  const [loginPassword, setLoginPassword] = useState('');

  // Password visibility
  const [showPassword, setShowPassword] = useState(false);

  // Alerts
  const [errorMsg, setErrorMsg] = useState<string | null>(null);
  const [successMsg, setSuccessMsg] = useState<string | null>(null);

  const resetAlerts = () => {
    setErrorMsg(null);
    setSuccessMsg(null);
  };

  const handleRegister = (e: React.FormEvent) => {
    e.preventDefault();
    resetAlerts();

    if (regPassword !== regConfirmPass) {
      sound.playMistake();
      setErrorMsg('Mật khẩu xác nhận không trùng khớp. Vui lòng kiểm tra lại!');
      return;
    }

    const res = AccountManager.createAccount({
      fullName: regFullName,
      username: regUsername,
      password: regPassword,
      grade: regGrade,
      schoolName: regSchool,
      className: regClass,
      avatarId: regAvatarId,
    });

    if (res.success && res.account) {
      sound.playVictory();
      setSuccessMsg(`Chào mừng ${res.account.fullName}! Tài khoản học tập của bạn đã được tạo thành công.`);
      setTimeout(() => {
        onAuthSuccess(res.account!);
        onClose();
      }, 700);
    } else {
      sound.playMistake();
      setErrorMsg(res.error || 'Không thể tạo tài khoản. Vui lòng thử lại!');
    }
  };

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    resetAlerts();

    const res = AccountManager.login(loginUsername, loginPassword);
    if (res.success && res.account) {
      sound.playVictory();
      setSuccessMsg(`Đăng nhập thành công! Chào mừng bạn trở lại, ${res.account.fullName}.`);
      setTimeout(() => {
        onAuthSuccess(res.account!);
        onClose();
      }, 600);
    } else {
      sound.playMistake();
      setErrorMsg(res.error || 'Tên đăng nhập hoặc mật khẩu không chính xác!');
    }
  };

  const handleQuickSelectAccount = (account: UserAccount) => {
    sound.playClick();
    setLoginUsername(account.username);
    setTab('login');
    resetAlerts();
  };

  const handleDeleteSavedAccount = (e: React.MouseEvent, accountId: string, name: string) => {
    e.stopPropagation();
    if (window.confirm(`Bạn có chắc chắn muốn gỡ tài khoản "${name}" khỏi máy này không?`)) {
      AccountManager.deleteAccount(accountId);
      sound.playClick();
      resetAlerts();
    }
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/85 flex items-center justify-center p-3 sm:p-5 overflow-y-auto">
      <div className="bg-[#181425] border-4 border-[#fee761] shadow-pixel-lg w-full max-w-2xl max-h-[92vh] flex flex-col overflow-hidden my-auto">
        {/* Header Modal */}
        <div className="flex items-center justify-between bg-[#262b44] px-4 py-3 border-b-3 border-[#3a4466]">
          <div className="flex items-center gap-2">
            <span className="text-lg">🎒</span>
            <span className="text-xs sm:text-sm font-black text-[#fee761] uppercase tracking-wider">
              {tab === 'register' && 'TẠO TÀI KHOẢN HỌC TẬP MỚI'}
              {tab === 'login' && 'ĐĂNG NHẬP VÀO EASYTIN'}
              {tab === 'accounts' && 'DANH SÁCH TÀI KHOẢN TRÊN MÁY NÀY'}
            </span>
          </div>
          <button
            onClick={() => {
              sound.playClick();
              onClose();
            }}
            className="text-[#8b9bb4] hover:text-white cursor-pointer p-1"
            title="Đóng cửa sổ"
          >
            <X size={18} />
          </button>
        </div>

        {/* Tab Navigation */}
        <div className="flex border-b-2 border-[#3a4466] bg-[#1a1c2c]">
          <button
            onClick={() => {
              sound.playClick();
              setTab('register');
              resetAlerts();
            }}
            className={`flex-1 py-2.5 px-3 text-xs font-bold flex items-center justify-center gap-1.5 transition-colors border-r border-[#3a4466] ${
              tab === 'register'
                ? 'bg-[#262b44] text-[#fee761] border-b-2 border-[#fee761]'
                : 'text-[#8b9bb4] hover:text-white'
            }`}
          >
            <UserPlus size={14} />
            <span>Tạo tài khoản</span>
          </button>
          <button
            onClick={() => {
              sound.playClick();
              setTab('login');
              resetAlerts();
            }}
            className={`flex-1 py-2.5 px-3 text-xs font-bold flex items-center justify-center gap-1.5 transition-colors border-r border-[#3a4466] ${
              tab === 'login'
                ? 'bg-[#262b44] text-[#fee761] border-b-2 border-[#fee761]'
                : 'text-[#8b9bb4] hover:text-white'
            }`}
          >
            <LogIn size={14} />
            <span>Đăng nhập</span>
          </button>
          {existingAccounts.length > 0 && (
            <button
              onClick={() => {
                sound.playClick();
                setTab('accounts');
                resetAlerts();
              }}
              className={`py-2.5 px-3 text-xs font-bold flex items-center justify-center gap-1.5 transition-colors ${
                tab === 'accounts'
                  ? 'bg-[#262b44] text-[#fee761] border-b-2 border-[#fee761]'
                  : 'text-[#8b9bb4] hover:text-white'
              }`}
            >
              <Users size={14} />
              <span>Đổi tài khoản ({existingAccounts.length})</span>
            </button>
          )}
        </div>

        {/* Thông báo lỗi / thành công */}
        <div className="px-5 pt-4">
          {errorMsg && (
            <div className="bg-[#421d26] border-2 border-[#e43b44] text-[#ffb6b9] p-3 text-xs flex items-start gap-2 animate-shake">
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

        {/* Body Content */}
        <div className="p-5 overflow-y-auto flex-1">
          {/* TAB 1: TẠO TÀI KHOẢN MỚI */}
          {tab === 'register' && (
            <form onSubmit={handleRegister} className="flex flex-col gap-4">
              <div className="text-xs text-[#8b9bb4] bg-[#262b44]/60 p-3 border border-[#3a4466]">
                🌟 <strong>Học sinh thân mến:</strong> Hãy tạo tài khoản để tích lũy điểm kinh nghiệm (XP), nhận huy hiệu và lưu tiến độ học tập trên EasyTin!
              </div>

              {/* Chọn Linh vật / Avatar */}
              <div>
                <label className="block text-xs font-bold text-[#c0cbdc] mb-2 uppercase tracking-wide">
                  1. Chọn Linh vật đại diện của bạn:
                </label>
                <div className="grid grid-cols-2 sm:grid-cols-3 gap-2">
                  {AVATAR_OPTIONS.map((av) => {
                    const isSelected = regAvatarId === av.id;
                    return (
                      <div
                        key={av.id}
                        onClick={() => {
                          sound.playClick();
                          setRegAvatarId(av.id);
                        }}
                        className={`p-2.5 border-2 cursor-pointer flex items-center gap-2.5 transition-all ${
                          isSelected
                            ? 'bg-[#262b44] border-[#fee761] shadow-pixel-sm -translate-y-0.5'
                            : 'bg-[#1a1c2c] border-[#3a4466] hover:border-[#5a6988]'
                        }`}
                      >
                        <span className="text-2xl">{av.icon}</span>
                        <div className="overflow-hidden">
                          <div className="text-xs font-bold text-white truncate">{av.name}</div>
                          <div className="text-[10px] text-[#8b9bb4] truncate">{av.role}</div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>

              {/* Thông tin cá nhân */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div>
                  <label className="block text-xs font-bold text-[#c0cbdc] mb-1">
                    Họ và tên người học: <span className="text-[#e43b44]">*</span>
                  </label>
                  <input
                    type="text"
                    required
                    value={regFullName}
                    onChange={(e) => setRegFullName(e.target.value)}
                    placeholder="Ví dụ: Nguyễn Hoàng Nam"
                    className="w-full bg-[#181425] border-2 border-[#3a4466] focus:border-[#fee761] p-2 text-xs text-white outline-none"
                  />
                </div>

                <div>
                  <label className="block text-xs font-bold text-[#c0cbdc] mb-1">
                    Tên đăng nhập (viết liền, không dấu): <span className="text-[#e43b44]">*</span>
                  </label>
                  <input
                    type="text"
                    required
                    value={regUsername}
                    onChange={(e) => setRegUsername(e.target.value)}
                    placeholder="Ví dụ: hoangnam2015"
                    className="w-full bg-[#181425] border-2 border-[#3a4466] focus:border-[#fee761] p-2 text-xs text-[#2ce8f5] font-mono outline-none"
                  />
                </div>
              </div>

              {/* Mật khẩu */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div>
                  <label className="block text-xs font-bold text-[#c0cbdc] mb-1">
                    Mật khẩu (ít nhất 4 ký tự): <span className="text-[#e43b44]">*</span>
                  </label>
                  <div className="relative">
                    <input
                      type={showPassword ? 'text' : 'password'}
                      required
                      value={regPassword}
                      onChange={(e) => setRegPassword(e.target.value)}
                      placeholder="Nhập mật khẩu"
                      className="w-full bg-[#181425] border-2 border-[#3a4466] focus:border-[#fee761] p-2 pr-8 text-xs text-white outline-none"
                    />
                    <button
                      type="button"
                      onClick={() => setShowPassword(!showPassword)}
                      className="absolute right-2 top-2 text-[#8b9bb4] hover:text-white"
                    >
                      {showPassword ? <EyeOff size={14} /> : <Eye size={14} />}
                    </button>
                  </div>
                </div>

                <div>
                  <label className="block text-xs font-bold text-[#c0cbdc] mb-1">
                    Xác nhận lại mật khẩu: <span className="text-[#e43b44]">*</span>
                  </label>
                  <input
                    type={showPassword ? 'text' : 'password'}
                    required
                    value={regConfirmPass}
                    onChange={(e) => setRegConfirmPass(e.target.value)}
                    placeholder="Nhập lại mật khẩu"
                    className="w-full bg-[#181425] border-2 border-[#3a4466] focus:border-[#fee761] p-2 text-xs text-white outline-none"
                  />
                </div>
              </div>

              {/* Chọn Cấp học & Khối lớp */}
              <div>
                <label className="block text-xs font-bold text-[#c0cbdc] mb-2 uppercase tracking-wide">
                  2. Chọn Cấp học & Khối lớp của bạn:
                </label>
                <div className="flex flex-col gap-2">
                  {/* Cấp Tiểu học */}
                  <div className="flex items-center gap-1 bg-[#1a2e22] p-2 border border-[#2b5c3f]">
                    <span className="text-xs font-bold text-[#38b764] w-24 shrink-0 flex items-center gap-1">
                      <span>🎒</span> Tiểu học:
                    </span>
                    <div className="flex items-center gap-1.5 flex-wrap">
                      {([3, 4, 5] as Grade[]).map((g) => (
                        <button
                          key={g}
                          type="button"
                          onClick={() => {
                            sound.playClick();
                            setRegGrade(g);
                          }}
                          className={`px-3 py-1 text-xs font-bold border transition-all ${
                            regGrade === g
                              ? 'bg-[#fee761] text-black border-white shadow-pixel-sm font-black'
                              : 'bg-[#262b44] text-[#c0cbdc] border-[#3a4466] hover:border-[#5a6988]'
                          }`}
                        >
                          Lớp {g}
                        </button>
                      ))}
                    </div>
                  </div>

                  {/* Cấp THCS */}
                  <div className="flex items-center gap-1 bg-[#1a2538] p-2 border border-[#1f3b5c]">
                    <span className="text-xs font-bold text-[#2ce8f5] w-24 shrink-0 flex items-center gap-1">
                      <span>🌲</span> THCS:
                    </span>
                    <div className="flex items-center gap-1.5 flex-wrap">
                      {([6, 7, 8, 9] as Grade[]).map((g) => (
                        <button
                          key={g}
                          type="button"
                          onClick={() => {
                            sound.playClick();
                            setRegGrade(g);
                          }}
                          className={`px-3 py-1 text-xs font-bold border transition-all ${
                            regGrade === g
                              ? 'bg-[#fee761] text-black border-white shadow-pixel-sm font-black'
                              : 'bg-[#262b44] text-[#c0cbdc] border-[#3a4466] hover:border-[#5a6988]'
                          }`}
                        >
                          Lớp {g}
                        </button>
                      ))}
                    </div>
                  </div>

                  {/* Cấp THPT */}
                  <div className="flex items-center gap-1 bg-[#321e2f] p-2 border border-[#5c2b4e]">
                    <span className="text-xs font-bold text-[#fca3ca] w-24 shrink-0 flex items-center gap-1">
                      <span>🏛️</span> THPT:
                    </span>
                    <div className="flex items-center gap-1.5 flex-wrap">
                      {([10, 11, 12] as Grade[]).map((g) => (
                        <button
                          key={g}
                          type="button"
                          onClick={() => {
                            sound.playClick();
                            setRegGrade(g);
                          }}
                          className={`px-3 py-1 text-xs font-bold border transition-all ${
                            regGrade === g
                              ? 'bg-[#fee761] text-black border-white shadow-pixel-sm font-black'
                              : 'bg-[#262b44] text-[#c0cbdc] border-[#3a4466] hover:border-[#5a6988]'
                          }`}
                        >
                          Lớp {g}
                        </button>
                      ))}
                    </div>
                  </div>
                </div>
              </div>

              {/* Thông tin trường lớp (Tùy chọn) */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div>
                  <label className="block text-xs text-[#8b9bb4] mb-1">
                    Trường học (không bắt buộc):
                  </label>
                  <input
                    type="text"
                    value={regSchool}
                    onChange={(e) => setRegSchool(e.target.value)}
                    placeholder="Ví dụ: TH Chu Văn An"
                    className="w-full bg-[#181425] border-2 border-[#3a4466] p-2 text-xs text-white outline-none"
                  />
                </div>
                <div>
                  <label className="block text-xs text-[#8b9bb4] mb-1">
                    Tên lớp (không bắt buộc):
                  </label>
                  <input
                    type="text"
                    value={regClass}
                    onChange={(e) => setRegClass(e.target.value)}
                    placeholder="Ví dụ: Lớp 4A"
                    className="w-full bg-[#181425] border-2 border-[#3a4466] p-2 text-xs text-white outline-none"
                  />
                </div>
              </div>

              {/* Submit Button */}
              <div className="pt-2">
                <PixelButton variant="primary" size="md" className="w-full justify-center">
                  <UserPlus size={16} />
                  <span>TẠO TÀI KHOẢN VÀ BẮT ĐẦU HỌC</span>
                </PixelButton>
              </div>
            </form>
          )}

          {/* TAB 2: ĐĂNG NHẬP */}
          {tab === 'login' && (
            <form onSubmit={handleLogin} className="flex flex-col gap-4">
              <div className="text-xs text-[#8b9bb4] bg-[#262b44]/60 p-3 border border-[#3a4466]">
                🔑 Nhập tên đăng nhập và mật khẩu để tiếp tục lộ trình học tập của bạn.
              </div>

              <div>
                <label className="block text-xs font-bold text-[#c0cbdc] mb-1">
                  Tên đăng nhập:
                </label>
                <input
                  type="text"
                  required
                  value={loginUsername}
                  onChange={(e) => setLoginUsername(e.target.value)}
                  placeholder="Nhập tên đăng nhập của bạn"
                  className="w-full bg-[#181425] border-2 border-[#3a4466] focus:border-[#fee761] p-2.5 text-xs text-[#2ce8f5] font-mono outline-none"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-[#c0cbdc] mb-1">
                  Mật khẩu:
                </label>
                <div className="relative">
                  <input
                    type={showPassword ? 'text' : 'password'}
                    required
                    value={loginPassword}
                    onChange={(e) => setLoginPassword(e.target.value)}
                    placeholder="Nhập mật khẩu"
                    className="w-full bg-[#181425] border-2 border-[#3a4466] focus:border-[#fee761] p-2.5 pr-8 text-xs text-white outline-none"
                  />
                  <button
                    type="button"
                    onClick={() => setShowPassword(!showPassword)}
                    className="absolute right-2.5 top-2.5 text-[#8b9bb4] hover:text-white"
                  >
                    {showPassword ? <EyeOff size={16} /> : <Eye size={16} />}
                  </button>
                </div>
              </div>

              <div className="pt-2">
                <PixelButton variant="primary" size="md" className="w-full justify-center">
                  <LogIn size={16} />
                  <span>ĐĂNG NHẬP VÀO HỌC</span>
                </PixelButton>
              </div>

              <div className="text-center text-xs text-[#8b9bb4] pt-2">
                Chưa có tài khoản?{' '}
                <button
                  type="button"
                  onClick={() => {
                    sound.playClick();
                    setTab('register');
                    resetAlerts();
                  }}
                  className="text-[#fee761] font-bold hover:underline"
                >
                  Bấm vào đây để tạo tài khoản mới!
                </button>
              </div>
            </form>
          )}

          {/* TAB 3: DANH SÁCH TÀI KHOẢN TRÊN MÁY NÀY */}
          {tab === 'accounts' && (
            <div className="flex flex-col gap-3">
              <div className="text-xs text-[#8b9bb4] mb-1">
                Các bạn học sinh đã lưu tài khoản trên trình duyệt này. Nhấp vào tài khoản để đăng nhập nhanh:
              </div>

              <div className="flex flex-col gap-2 max-h-[360px] overflow-y-auto">
                {existingAccounts.map((acc) => {
                  const avatar = AVATAR_OPTIONS.find((a) => a.id === acc.avatarId) || AVATAR_OPTIONS[0];
                  return (
                    <div
                      key={acc.id}
                      onClick={() => handleQuickSelectAccount(acc)}
                      className="p-3 bg-[#262b44] border-2 border-[#3a4466] hover:border-[#fee761] flex items-center justify-between cursor-pointer transition-all hover:-translate-y-0.5"
                    >
                      <div className="flex items-center gap-3">
                        <span className="text-3xl">{avatar.icon}</span>
                        <div>
                          <div className="text-xs font-bold text-white flex items-center gap-2">
                            <span>{acc.fullName}</span>
                            <span className="bg-[#181425] text-[#fee761] px-1.5 py-0.5 text-[10px] font-mono border border-[#3a4466]">
                              @{acc.username}
                            </span>
                          </div>
                          <div className="text-[11px] text-[#8b9bb4] mt-0.5">
                            Lớp {acc.grade} · {acc.progress.xp} XP · Chuỗi {acc.progress.streakDays} ngày
                            {acc.className ? ` · ${acc.className}` : ''}
                          </div>
                        </div>
                      </div>

                      <div className="flex items-center gap-2">
                        <span className="text-xs font-bold text-[#fee761] bg-[#181425] px-2.5 py-1 border border-[#3a4466]">
                          Đăng nhập
                        </span>
                        <button
                          type="button"
                          onClick={(e) => handleDeleteSavedAccount(e, acc.id, acc.fullName)}
                          className="p-1.5 text-[#8b9bb4] hover:text-[#e43b44] hover:bg-[#181425]"
                          title="Gỡ tài khoản khỏi máy này"
                        >
                          <Trash2 size={15} />
                        </button>
                      </div>
                    </div>
                  );
                })}
              </div>

              <div className="pt-2">
                <PixelButton
                  variant="ghost"
                  size="sm"
                  onClick={() => {
                    sound.playClick();
                    setTab('register');
                  }}
                  className="w-full justify-center"
                >
                  <UserPlus size={14} /> Tạo thêm tài khoản học sinh mới
                </PixelButton>
              </div>
            </div>
          )}
        </div>

        {/* Footer / Chế độ Khách */}
        <div className="bg-[#1a1c2c] border-t-2 border-[#3a4466] px-5 py-2.5 flex items-center justify-between text-xs text-[#8b9bb4]">
          <span>💡 Dành cho học sinh từ Lớp 3 đến Lớp 12</span>
          <button
            onClick={() => {
              sound.playClick();
              onClose();
            }}
            className="text-[#8b9bb4] hover:text-white hover:underline text-[11px]"
          >
            Tiếp tục học ở chế độ Khách &gt;
          </button>
        </div>
      </div>
    </div>
  );
};
