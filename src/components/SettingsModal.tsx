import React, { useState } from 'react';
import { UserProgressState } from '../../packages/domain/types';
import { LocalStorageAdapter } from '../../packages/domain/storage';
import { useI18n } from '../i18nContext';
import { useTheme } from '../ThemeContext';
import { PixelButton } from './PixelButton';
import { PixelLogo } from './PixelLogo';
import { sound } from '../../packages/game-core/audio';
import {
  X,
  Settings,
  Globe,
  Volume2,
  VolumeX,
  Share2,
  GraduationCap,
  Sparkles,
  Info,
  CheckCircle2,
  AlertCircle,
  Copy,
  Check,
  Upload,
  Play,
  Key,
  Plus,
  AlertTriangle,
  Sun,
  Moon,
  Monitor,
} from 'lucide-react';

interface SettingsModalProps {
  progress: UserProgressState;
  onImportSuccess: (newProgress: UserProgressState) => void;
  onClose: () => void;
  initialTab?: 'language' | 'sound' | 'backup' | 'teacher' | 'accessibility' | 'about';
}

export const SettingsModal: React.FC<SettingsModalProps> = ({
  progress,
  onImportSuccess,
  onClose,
  initialTab = 'language',
}) => {
  const { language, setLanguage, t } = useI18n();
  const { theme, setTheme } = useTheme();
  const [activeTab, setActiveTab] = useState<'language' | 'sound' | 'backup' | 'teacher' | 'accessibility' | 'about'>(
    initialTab
  );

  // Sound settings
  const [isMuted, setIsMuted] = useState(sound.getMuted());

  // Backup settings
  const backupCode = LocalStorageAdapter.exportProgressCode(progress);
  const [copied, setCopied] = useState(false);
  const [importInput, setImportInput] = useState('');
  const [backupError, setBackupError] = useState<string | null>(null);
  const [backupSuccess, setBackupSuccess] = useState<string | null>(null);

  // Teacher settings
  const [classCode, setClassCode] = useState('TIN402');

  // Accessibility / Motion
  const [reducedMotion, setReducedMotion] = useState(false);
  const [largeFont, setLargeFont] = useState(false);

  // General alert
  const [savedAlert, setSavedAlert] = useState<string | null>(null);

  const showSavedNotification = (msg: string) => {
    setSavedAlert(msg);
    setTimeout(() => setSavedAlert(null), 2500);
  };

  const handleSelectLanguage = (lang: 'vi' | 'en') => {
    sound.playClick();
    setLanguage(lang);
    showSavedNotification(t('settings_saved_msg'));
  };

  const handleToggleSound = () => {
    const next = !isMuted;
    sound.setMuted(next);
    setIsMuted(next);
    if (!next) sound.playClick();
    showSavedNotification(next ? t('settings_sound_off') : t('settings_sound_on'));
  };

  const handleCopyBackup = () => {
    sound.playClick();
    navigator.clipboard.writeText(backupCode);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
    showSavedNotification(t('settings_backup_copied'));
  };

  const handleImportBackup = () => {
    setBackupError(null);
    setBackupSuccess(null);
    if (!importInput.trim()) return;

    const res = LocalStorageAdapter.importProgressCode(importInput, progress);
    if (res) {
      sound.playVictory();
      setBackupSuccess(t('settings_backup_success'));
      onImportSuccess(res);
      setTimeout(() => {
        setBackupSuccess(null);
      }, 3000);
    } else {
      sound.playMistake();
      setBackupError(t('settings_backup_invalid'));
    }
  };

  const generateNewClassCode = () => {
    sound.playClick();
    const randomNum = Math.floor(100 + Math.random() * 900);
    setClassCode(`TIN${randomNum}`);
    showSavedNotification(`Đã tạo mã phòng học mới: TIN${randomNum}`);
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/85 flex items-center justify-center p-2 sm:p-5 overflow-y-auto">
      <div className="bg-[#181425] border-4 border-[#2ce8f5] shadow-pixel-lg w-full max-w-4xl lg:max-w-5xl max-h-[92vh] flex flex-col overflow-hidden my-auto anim-pixel-pop-in">
        {/* Header Modal */}
        <div className="flex items-center justify-between bg-[#262b44] px-4 py-3 border-b-3 border-[#3a4466]">
          <div className="flex items-center gap-2">
            <Settings size={18} className="text-[#2ce8f5]" />
            <span className="text-xs sm:text-sm font-black text-[#fee761] uppercase tracking-wider">
              {t('settings_heading')}
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

        {/* Thông báo thao tác đã lưu */}
        {savedAlert && (
          <div className="bg-[#1a3826] border-b-2 border-[#38b764] text-[#b6f0cd] px-4 py-2 text-xs flex items-center gap-2 animate-fade-in">
            <CheckCircle2 size={15} className="text-[#38b764] shrink-0" />
            <span>{savedAlert}</span>
          </div>
        )}

        {/* Thân Modal: Bố cục 2 cột (Menu Danh sách bên trái · Nội dung chi tiết bên phải) */}
        <div className="flex-1 flex flex-col md:flex-row overflow-hidden">
          {/* CỘT DANH SÁCH MỤC CÀI ĐẶT (LIST MENU) */}
          <div className="w-full md:w-64 bg-[#1a1c2c] border-b-2 md:border-b-0 md:border-r-2 border-[#3a4466] flex flex-row md:flex-col overflow-x-auto md:overflow-y-auto shrink-0">
            <div className="p-3 text-[11px] font-black text-[#8b9bb4] uppercase tracking-wider hidden md:block border-b border-[#262b44]">
              DANH MỤC CÀI ĐẶT:
            </div>

            {/* Mục 1: Ngôn ngữ */}
            <button
              onClick={() => {
                sound.playClick();
                setActiveTab('language');
              }}
              className={`p-3 text-left text-xs font-bold flex items-center gap-2.5 transition-all shrink-0 md:shrink border-b md:border-b border-[#262b44] ${
                activeTab === 'language'
                  ? 'bg-[#262b44] text-[#fee761] border-l-4 border-l-[#fee761] font-black'
                  : 'text-[#c0cbdc] hover:bg-[#202538] hover:text-white'
              }`}
            >
              <Globe size={16} className={activeTab === 'language' ? 'text-[#fee761]' : 'text-[#2ce8f5]'} />
              <span>{t('settings_nav_language')}</span>
            </button>

            {/* Mục 2: Âm thanh */}
            <button
              onClick={() => {
                sound.playClick();
                setActiveTab('sound');
              }}
              className={`p-3 text-left text-xs font-bold flex items-center gap-2.5 transition-all shrink-0 md:shrink border-b md:border-b border-[#262b44] ${
                activeTab === 'sound'
                  ? 'bg-[#262b44] text-[#fee761] border-l-4 border-l-[#fee761] font-black'
                  : 'text-[#c0cbdc] hover:bg-[#202538] hover:text-white'
              }`}
            >
              <Volume2 size={16} className={activeTab === 'sound' ? 'text-[#fee761]' : 'text-[#38b764]'} />
              <span>{t('settings_nav_sound')}</span>
            </button>

            {/* Mục 3: Sao lưu */}
            <button
              onClick={() => {
                sound.playClick();
                setActiveTab('backup');
              }}
              className={`p-3 text-left text-xs font-bold flex items-center gap-2.5 transition-all shrink-0 md:shrink border-b md:border-b border-[#262b44] ${
                activeTab === 'backup'
                  ? 'bg-[#262b44] text-[#fee761] border-l-4 border-l-[#fee761] font-black'
                  : 'text-[#c0cbdc] hover:bg-[#202538] hover:text-white'
              }`}
            >
              <Share2 size={16} className={activeTab === 'backup' ? 'text-[#fee761]' : 'text-[#feae34]'} />
              <span>{t('settings_nav_backup')}</span>
            </button>

            {/* Mục 4: Thầy Cô */}
            <button
              onClick={() => {
                sound.playClick();
                setActiveTab('teacher');
              }}
              className={`p-3 text-left text-xs font-bold flex items-center gap-2.5 transition-all shrink-0 md:shrink border-b md:border-b border-[#262b44] ${
                activeTab === 'teacher'
                  ? 'bg-[#262b44] text-[#fee761] border-l-4 border-l-[#fee761] font-black'
                  : 'text-[#c0cbdc] hover:bg-[#202538] hover:text-white'
              }`}
            >
              <GraduationCap size={16} className={activeTab === 'teacher' ? 'text-[#fee761]' : 'text-[#38b764]'} />
              <span>{t('settings_nav_teacher')}</span>
            </button>

            {/* Mục 5: Trợ năng & Hiển thị */}
            <button
              onClick={() => {
                sound.playClick();
                setActiveTab('accessibility');
              }}
              className={`p-3 text-left text-xs font-bold flex items-center gap-2.5 transition-all shrink-0 md:shrink border-b md:border-b border-[#262b44] ${
                activeTab === 'accessibility'
                  ? 'bg-[#262b44] text-[#fee761] border-l-4 border-l-[#fee761] font-black'
                  : 'text-[#c0cbdc] hover:bg-[#202538] hover:text-white'
              }`}
            >
              <Sparkles size={16} className={activeTab === 'accessibility' ? 'text-[#fee761]' : 'text-[#fca3ca]'} />
              <span>{t('settings_nav_accessibility')}</span>
            </button>

            {/* Mục 6: Giới thiệu */}
            <button
              onClick={() => {
                sound.playClick();
                setActiveTab('about');
              }}
              className={`p-3 text-left text-xs font-bold flex items-center gap-2.5 transition-all shrink-0 md:shrink ${
                activeTab === 'about'
                  ? 'bg-[#262b44] text-[#fee761] border-l-4 border-l-[#fee761] font-black'
                  : 'text-[#c0cbdc] hover:bg-[#202538] hover:text-white'
              }`}
            >
              <Info size={16} className={activeTab === 'about' ? 'text-[#fee761]' : 'text-[#8b9bb4]'} />
              <span>{t('settings_nav_about')}</span>
            </button>
          </div>

          {/* CỘT NỘI DUNG CHI TIẾT CỦA MỤC ĐANG CHỌN */}
          <div className="flex-1 p-5 overflow-y-auto">
            {/* 1. TAB NGÔN NGỮ */}
            {activeTab === 'language' && (
              <div className="flex flex-col gap-4">
                <div className="border-b border-[#3a4466] pb-3">
                  <h3 className="font-bold text-base text-white flex items-center gap-2">
                    <Globe size={18} className="text-[#2ce8f5]" />
                    <span>{t('settings_language_label')}</span>
                  </h3>
                  <p className="text-xs text-[#8b9bb4] mt-1">
                    {t('settings_language_desc')}
                  </p>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-1">
                  {/* Tiếng Việt */}
                  <div
                    onClick={() => handleSelectLanguage('vi')}
                    className={`p-4 border-3 cursor-pointer flex items-center gap-3.5 transition-all ${
                      language === 'vi'
                        ? 'bg-[#262b44] border-[#fee761] shadow-pixel -translate-y-0.5'
                        : 'bg-[#1a1c2c] border-[#3a4466] hover:border-[#5a6988]'
                    }`}
                  >
                    <span className="text-4xl">🇻🇳</span>
                    <div>
                      <div className="text-sm font-black text-white flex items-center gap-2">
                        <span>Tiếng Việt</span>
                        {language === 'vi' && (
                          <span className="text-[10px] bg-[#38b764] text-black px-2 py-0.5 font-bold border border-[#a7f070]">
                            Đang dùng
                          </span>
                        )}
                      </div>
                      <div className="text-xs text-[#8b9bb4] mt-0.5">Vietnamese (Mặc định cho SGK GDPT 2018)</div>
                    </div>
                  </div>

                  {/* English */}
                  <div
                    onClick={() => handleSelectLanguage('en')}
                    className={`p-4 border-3 cursor-pointer flex items-center gap-3.5 transition-all ${
                      language === 'en'
                        ? 'bg-[#262b44] border-[#fee761] shadow-pixel -translate-y-0.5'
                        : 'bg-[#1a1c2c] border-[#3a4466] hover:border-[#5a6988]'
                    }`}
                  >
                    <span className="text-4xl">🇬🇧</span>
                    <div>
                      <div className="text-sm font-black text-white flex items-center gap-2">
                        <span>English</span>
                        {language === 'en' && (
                          <span className="text-[10px] bg-[#38b764] text-black px-2 py-0.5 font-bold border border-[#a7f070]">
                            Active
                          </span>
                        )}
                      </div>
                      <div className="text-xs text-[#8b9bb4] mt-0.5">Tiếng Anh (International Students & Bilingual)</div>
                    </div>
                  </div>
                </div>
              </div>
            )}

            {/* 2. TAB ÂM THANH */}
            {activeTab === 'sound' && (
              <div className="flex flex-col gap-4">
                <div className="border-b border-[#3a4466] pb-3">
                  <h3 className="font-bold text-base text-white flex items-center gap-2">
                    <Volume2 size={18} className="text-[#38b764]" />
                    <span>{t('settings_sound_label')}</span>
                  </h3>
                  <p className="text-xs text-[#8b9bb4] mt-1">
                    {t('settings_sound_desc')}
                  </p>
                </div>

                <div className="bg-[#1a1c2c] border-2 border-[#3a4466] p-4 flex flex-col gap-4">
                  <div className="flex flex-wrap items-center justify-between gap-3">
                    <div>
                      <div className="text-xs font-bold text-white">Trạng thái phát âm thanh:</div>
                      <div className="text-[11px] text-[#8b9bb4] mt-0.5">
                        Công nghệ Web Audio Synthesizer tự sinh nhẹ, không tốn băng thông tải file mp3.
                      </div>
                    </div>
                    <button
                      onClick={handleToggleSound}
                      className={`px-4 py-2 text-xs font-bold border-2 transition-all flex items-center gap-2 cursor-pointer ${
                        !isMuted
                          ? 'bg-[#1a2e22] text-[#38b764] border-[#38b764] shadow-pixel-sm'
                          : 'bg-[#421d26] text-[#e43b44] border-[#e43b44]'
                      }`}
                    >
                      {!isMuted ? <Volume2 size={16} /> : <VolumeX size={16} />}
                      <span>{!isMuted ? t('settings_sound_on') : t('settings_sound_off')}</span>
                    </button>
                  </div>

                  {!isMuted && (
                    <div className="pt-3 border-t border-[#262b44] flex flex-wrap items-center gap-2">
                      <span className="text-xs text-[#8b9bb4]">Nghe thử âm thanh retro:</span>
                      <PixelButton variant="primary" size="sm" onClick={() => sound.playVictory()}>
                        <Play size={12} /> Chiến thắng (Victory)
                      </PixelButton>
                      <PixelButton variant="ghost" size="sm" onClick={() => sound.playJump()}>
                        <Play size={12} /> Nhảy cao (Jump)
                      </PixelButton>
                      <PixelButton variant="ghost" size="sm" onClick={() => sound.playClick()}>
                        <Play size={12} /> Bấm nút (Click)
                      </PixelButton>
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* 3. TAB SAO LƯU & THẺ TIẾN ĐỘ */}
            {activeTab === 'backup' && (
              <div className="flex flex-col gap-4">
                <div className="border-b border-[#3a4466] pb-3">
                  <h3 className="font-bold text-base text-white flex items-center gap-2">
                    <Share2 size={18} className="text-[#feae34]" />
                    <span>{t('settings_backup_title')}</span>
                  </h3>
                  <p className="text-xs text-[#8b9bb4] mt-1">
                    {t('settings_backup_desc')}
                  </p>
                </div>

                {backupError && (
                  <div className="bg-[#421d26] border-2 border-[#e43b44] text-[#ffb6b9] p-3 text-xs flex items-center gap-2">
                    <AlertCircle size={16} className="text-[#e43b44] shrink-0" />
                    <span>{backupError}</span>
                  </div>
                )}
                {backupSuccess && (
                  <div className="bg-[#1a3826] border-2 border-[#38b764] text-[#b6f0cd] p-3 text-xs flex items-center gap-2">
                    <CheckCircle2 size={16} className="text-[#38b764] shrink-0" />
                    <span>{backupSuccess}</span>
                  </div>
                )}

                {/* Xuất mã thẻ tiến độ */}
                <div className="bg-[#1a1c2c] border-2 border-[#3a4466] p-4 flex flex-col gap-2">
                  <div className="text-xs font-bold text-white flex items-center gap-1.5">
                    <span>📤</span> Mã sao lưu tiến độ hiện tại của máy này:
                  </div>
                  <div className="flex items-center gap-2">
                    <input
                      readOnly
                      value={backupCode}
                      className="flex-1 bg-[#181425] border-2 border-[#3a4466] p-2 text-xs font-mono text-[#fee761] outline-none select-all"
                    />
                    <PixelButton variant="primary" size="sm" onClick={handleCopyBackup}>
                      {copied ? <Check size={14} /> : <Copy size={14} />}
                      <span>{copied ? t('settings_backup_copied') : t('settings_backup_copy_btn')}</span>
                    </PixelButton>
                  </div>
                </div>

                {/* Nhập mã thẻ tiến độ */}
                <div className="bg-[#1a1c2c] border-2 border-[#3a4466] p-4 flex flex-col gap-2">
                  <div className="text-xs font-bold text-white flex items-center gap-1.5">
                    <span>📥</span> {t('settings_backup_import_label')}
                  </div>
                  <div className="flex items-center gap-2">
                    <input
                      type="text"
                      placeholder={t('settings_backup_import_placeholder')}
                      value={importInput}
                      onChange={(e) => setImportInput(e.target.value)}
                      className="flex-1 bg-[#181425] border-2 border-[#3a4466] focus:border-[#fee761] p-2 text-xs text-white outline-none"
                    />
                    <PixelButton variant="primary" size="sm" onClick={handleImportBackup}>
                      <Upload size={14} />
                      <span>{t('settings_backup_import_btn')}</span>
                    </PixelButton>
                  </div>
                </div>
              </div>
            )}

            {/* 4. TAB CỔNG DÀNH CHO THẦY CÔ */}
            {activeTab === 'teacher' && (
              <div className="flex flex-col gap-4">
                <div className="border-b border-[#3a4466] pb-3">
                  <h3 className="font-bold text-base text-white flex items-center gap-2">
                    <GraduationCap size={18} className="text-[#38b764]" />
                    <span>{t('settings_teacher_title')}</span>
                  </h3>
                  <p className="text-xs text-[#8b9bb4] mt-1">
                    Công cụ hỗ trợ giáo viên điều phối phòng thực hành Tin học và nắm bắt lỗ hổng kiến thức của học sinh.
                  </p>
                </div>

                {/* Mã phòng Tin học */}
                <div className="bg-[#1a1c2c] border-2 border-[#5a6988] p-4 flex flex-col sm:flex-row items-center justify-between gap-4">
                  <div>
                    <div className="font-bold text-sm text-white flex items-center gap-2">
                      <Key size={16} className="text-[#fee761]" /> {t('settings_teacher_code_title')}
                    </div>
                    <div className="text-xs text-[#8b9bb4] mt-0.5">
                      {t('settings_teacher_code_desc')}
                    </div>
                  </div>
                  <div className="flex items-center gap-3">
                    <div className="font-pixel text-xl text-[#38b764] bg-[#181425] px-4 py-2 border-2 border-[#38b764]">
                      {classCode}
                    </div>
                    <PixelButton variant="primary" size="sm" onClick={generateNewClassCode}>
                      <Plus size={14} /> {t('settings_teacher_change_code')}
                    </PixelButton>
                  </div>
                </div>

                {/* Phân tích lỗ hổng nhận thức */}
                <div>
                  <div className="text-xs font-black text-[#fee761] uppercase tracking-wider mb-2 flex items-center gap-2">
                    <AlertTriangle size={15} /> {t('settings_teacher_heatmap_title')}
                  </div>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    <div className="bg-[#262b44] border-2 border-[#e43b44] p-3 flex items-start gap-2.5">
                      <AlertTriangle className="text-[#e43b44] shrink-0 mt-0.5" size={18} />
                      <div>
                        <div className="text-xs font-bold text-white">Nhầm lẫn thiết bị Vào / Ra</div>
                        <div className="text-[11px] text-[#8b9bb4] mt-0.5">
                          32% học sinh chọn màn hình cảm ứng chỉ là thiết bị xuất hình ảnh.
                        </div>
                      </div>
                    </div>
                    <div className="bg-[#262b44] border-2 border-[#feae34] p-3 flex items-start gap-2.5">
                      <AlertTriangle className="text-[#feae34] shrink-0 mt-0.5" size={18} />
                      <div>
                        <div className="text-xs font-bold text-white">Cấu trúc rẽ nhánh (Nếu ... Thì)</div>
                        <div className="text-[11px] text-[#8b9bb4] mt-0.5">
                          24% học sinh quên điều kiện so sánh ngược lại trong nhánh Else.
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            )}

            {/* 5. TAB HIỂN THỊ & TRỢ NĂNG */}
            {activeTab === 'accessibility' && (
              <div className="flex flex-col gap-4">
                <div className="border-b border-[#3a4466] pb-3">
                  <h3 className="font-bold text-base text-white flex items-center gap-2">
                    <Sparkles size={18} className="text-[#fca3ca]" />
                    <span>{t('settings_nav_accessibility')}</span>
                  </h3>
                  <p className="text-xs text-[#8b9bb4] mt-1">
                    Tùy biến hiển thị và hiệu ứng trực quan phù hợp với thể trạng và sở thích của học sinh.
                  </p>
                </div>

                <div className="bg-[#1a1c2c] border-2 border-[#3a4466] p-4 flex flex-col gap-4">
                  {/* Tùy chọn Giao diện Sáng / Tối / Tự động (Theme Mode) */}
                  <div className="flex flex-col gap-2.5 pb-4 border-b border-[#262b44]">
                    <div>
                      <div className="text-xs font-bold text-white flex items-center gap-1.5">
                        <Sun size={15} className="text-[#fee761]" />
                        <span>{t('settings_theme_label')}</span>
                      </div>
                      <div className="text-[11px] text-[#8b9bb4] mt-0.5">
                        {t('settings_theme_desc')}
                      </div>
                    </div>

                    <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
                      {/* Tối (Dark) */}
                      <button
                        onClick={() => {
                          sound.playClick();
                          setTheme('dark');
                          showSavedNotification(t('theme_dark'));
                        }}
                        className={`p-2.5 text-left border-2 flex items-center gap-2 cursor-pointer transition-all ${
                          theme === 'dark'
                            ? 'bg-[#181425] border-[#fee761] text-[#fee761] shadow-pixel-sm font-bold'
                            : 'bg-[#262b44] border-[#3a4466] text-[#c0cbdc] hover:border-white'
                        }`}
                      >
                        <Moon size={16} className={theme === 'dark' ? 'text-[#fee761]' : 'text-[#8b9bb4]'} />
                        <div className="flex flex-col text-xs">
                          <span className="font-bold">Giao diện Tối</span>
                          <span className="text-[10px] text-[#8b9bb4]">Ban đêm · Retro</span>
                        </div>
                      </button>

                      {/* Sáng (Light) */}
                      <button
                        onClick={() => {
                          sound.playClick();
                          setTheme('light');
                          showSavedNotification(t('theme_light'));
                        }}
                        className={`p-2.5 text-left border-2 flex items-center gap-2 cursor-pointer transition-all ${
                          theme === 'light'
                            ? 'bg-[#ffffff] border-[#38b764] text-[#181425] shadow-pixel-sm font-bold'
                            : 'bg-[#262b44] border-[#3a4466] text-[#c0cbdc] hover:border-white'
                        }`}
                      >
                        <Sun size={16} className={theme === 'light' ? 'text-[#f77622]' : 'text-[#8b9bb4]'} />
                        <div className="flex flex-col text-xs">
                          <span className="font-bold">Giao diện Sáng</span>
                          <span className="text-[10px] text-[#8b9bb4]">Ban ngày · Dễ đọc</span>
                        </div>
                      </button>

                      {/* Tự động (System) */}
                      <button
                        onClick={() => {
                          sound.playClick();
                          setTheme('system');
                          showSavedNotification(t('theme_system'));
                        }}
                        className={`p-2.5 text-left border-2 flex items-center gap-2 cursor-pointer transition-all ${
                          theme === 'system'
                            ? 'bg-[#1f3b5c] border-[#2ce8f5] text-[#2ce8f5] shadow-pixel-sm font-bold'
                            : 'bg-[#262b44] border-[#3a4466] text-[#c0cbdc] hover:border-white'
                        }`}
                      >
                        <Monitor size={16} className={theme === 'system' ? 'text-[#2ce8f5]' : 'text-[#8b9bb4]'} />
                        <div className="flex flex-col text-xs">
                          <span className="font-bold">Tự động</span>
                          <span className="text-[10px] text-[#8b9bb4]">Theo thiết bị</span>
                        </div>
                      </button>
                    </div>
                  </div>

                  {/* Tùy chọn hoạt ảnh linh vật */}
                  <div className="flex items-center justify-between gap-3">
                    <div>
                      <div className="text-xs font-bold text-white">{t('settings_motion_label')}</div>
                      <div className="text-[11px] text-[#8b9bb4] mt-0.5">
                        {t('settings_motion_desc')}
                      </div>
                    </div>
                    <button
                      onClick={() => {
                        sound.playClick();
                        setReducedMotion(!reducedMotion);
                        showSavedNotification(
                          !reducedMotion ? t('settings_motion_off') : t('settings_motion_on')
                        );
                      }}
                      className={`px-3 py-1.5 text-xs font-bold border-2 transition-all cursor-pointer ${
                        !reducedMotion
                          ? 'bg-[#1a2e22] text-[#38b764] border-[#38b764]'
                          : 'bg-[#262b44] text-[#c0cbdc] border-[#3a4466]'
                      }`}
                    >
                      {!reducedMotion ? t('settings_motion_on') : t('settings_motion_off')}
                    </button>
                  </div>

                  {/* Cỡ chữ */}
                  <div className="pt-3 border-t border-[#262b44] flex items-center justify-between gap-3">
                    <div>
                      <div className="text-xs font-bold text-white">{t('settings_font_label')}</div>
                      <div className="text-[11px] text-[#8b9bb4] mt-0.5">
                        Phóng to chữ hiển thị cho học sinh tiểu học hoặc màn hình nhỏ.
                      </div>
                    </div>
                    <div className="flex items-center gap-2">
                      <button
                        onClick={() => {
                          sound.playClick();
                          setLargeFont(false);
                          showSavedNotification(t('font_standard'));
                        }}
                        className={`px-2.5 py-1 text-xs font-bold border ${
                          !largeFont
                            ? 'bg-[#fee761] text-black border-white font-black'
                            : 'bg-[#262b44] text-[#c0cbdc] border-[#3a4466]'
                        }`}
                      >
                        {t('font_standard')}
                      </button>
                      <button
                        onClick={() => {
                          sound.playClick();
                          setLargeFont(true);
                          showSavedNotification(t('font_large'));
                        }}
                        className={`px-2.5 py-1 text-xs font-bold border ${
                          largeFont
                            ? 'bg-[#fee761] text-black border-white font-black'
                            : 'bg-[#262b44] text-[#c0cbdc] border-[#3a4466]'
                        }`}
                      >
                        {t('font_large')}
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            )}

            {/* 6. TAB GIỚI THIỆU & BẢN QUYỀN */}
            {activeTab === 'about' && (
              <div className="flex flex-col gap-4">
                <div className="border-b border-[#3a4466] pb-3">
                  <h3 className="font-bold text-base text-white flex items-center gap-2">
                    <Info size={18} className="text-[#8b9bb4]" />
                    <span>{t('settings_nav_about')}</span>
                  </h3>
                  <p className="text-xs text-[#8b9bb4] mt-1">
                    {t('settings_about_desc')}
                  </p>
                </div>

                <div className="bg-[#1a1c2c] border-2 border-[#3a4466] p-4 flex flex-col gap-4">
                  {/* Logo thương hiệu nổi bật */}
                  <div className="bg-[#181425] p-3.5 border-2 border-[#5a6988] flex items-center justify-center shadow-pixel-sm">
                    <PixelLogo size="lg" />
                  </div>

                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                    <div>
                      <span className="text-[#8b9bb4]">Tên ứng dụng:</span>{' '}
                      <strong className="text-white">EasyTin</strong>
                    </div>
                    <div>
                      <span className="text-[#8b9bb4]">Phiên bản:</span>{' '}
                      <strong className="text-[#fee761]">v1.0.0 (Gold Master)</strong>
                    </div>
                    <div>
                      <span className="text-[#8b9bb4]">Khung chương trình:</span>{' '}
                      <strong className="text-[#38b764]">GDPT 2018 (Lớp 3 – 12)</strong>
                    </div>
                    <div>
                      <span className="text-[#8b9bb4]">Độ phủ SGK:</span>{' '}
                      <strong className="text-white">KNTT · Cánh Diều · CTST (137 bài)</strong>
                    </div>
                    <div>
                      <span className="text-[#8b9bb4]">Kiến trúc dữ liệu:</span>{' '}
                      <strong className="text-[#2ce8f5]">100% Offline PWA Ready</strong>
                    </div>
                    <div>
                      <span className="text-[#8b9bb4]">Hệ thống kiểm thử:</span>{' '}
                      <strong className="text-[#38b764]">Vitest Automated Unit Testing</strong>
                    </div>
                  </div>

                  <div className="pt-2 border-t border-[#262b44] text-[11px] text-[#8b9bb4] leading-relaxed">
                    EasyTin được phát triển với sứ mệnh mang đến trải nghiệm học Tin học thú vị, trực quan và bình đẳng cho mọi học sinh Việt Nam.
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Footer Modal */}
        <div className="bg-[#1a1c2c] border-t-2 border-[#3a4466] px-5 py-3 flex items-center justify-between">
          <span className="text-[11px] text-[#8b9bb4]">EasyTin © 2026 · Cài đặt Hệ thống</span>
          <PixelButton
            variant="primary"
            size="sm"
            onClick={() => {
              sound.playClick();
              onClose();
            }}
          >
            {t('btn_save_settings')}
          </PixelButton>
        </div>
      </div>
    </div>
  );
};
