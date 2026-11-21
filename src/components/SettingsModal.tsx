import React, { useState } from 'react';
import { useI18n } from '../i18nContext';
import { PixelButton } from './PixelButton';
import { sound } from '../../packages/game-core/audio';
import { X, Settings, Globe, Volume2, VolumeX, CheckCircle2, Play, Info } from 'lucide-react';

interface SettingsModalProps {
  onClose: () => void;
}

export const SettingsModal: React.FC<SettingsModalProps> = ({ onClose }) => {
  const { language, setLanguage, t } = useI18n();
  const [isMuted, setIsMuted] = useState(sound.getMuted());
  const [savedAlert, setSavedAlert] = useState(false);

  const handleSelectLanguage = (lang: 'vi' | 'en') => {
    sound.playClick();
    setLanguage(lang);
    setSavedAlert(true);
    setTimeout(() => setSavedAlert(false), 2000);
  };

  const handleToggleSound = () => {
    const next = !isMuted;
    sound.setMuted(next);
    setIsMuted(next);
    if (!next) sound.playClick();
    setSavedAlert(true);
    setTimeout(() => setSavedAlert(false), 2000);
  };

  const handleTestAudio = () => {
    sound.playVictory();
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/85 flex items-center justify-center p-3 sm:p-5 overflow-y-auto">
      <div className="bg-[#181425] border-4 border-[#2ce8f5] shadow-pixel-lg w-full max-w-xl max-h-[92vh] flex flex-col overflow-hidden my-auto">
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

        {/* Thông báo đã lưu */}
        {savedAlert && (
          <div className="px-5 pt-3">
            <div className="bg-[#1a3826] border-2 border-[#38b764] text-[#b6f0cd] p-2.5 text-xs flex items-center gap-2">
              <CheckCircle2 size={16} className="text-[#38b764] shrink-0" />
              <span>{t('settings_saved_msg')}</span>
            </div>
          </div>
        )}

        {/* Nội dung cài đặt */}
        <div className="p-5 overflow-y-auto flex-1 flex flex-col gap-6">
          {/* MỤC 1: CHUYỂN ĐỔI NGÔN NGỮ (LANGUAGE) */}
          <div className="bg-[#1a1c2c] border-2 border-[#3a4466] p-4 flex flex-col gap-3">
            <div className="flex items-center gap-2 text-xs font-bold text-white">
              <Globe size={16} className="text-[#2ce8f5]" />
              <span className="uppercase tracking-wider">{t('settings_language_label')}</span>
            </div>
            <div className="text-xs text-[#8b9bb4]">
              {t('settings_language_desc')}
            </div>

            {/* Lựa chọn 2 ngôn ngữ: Tiếng Việt & English */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1">
              {/* Tiếng Việt */}
              <div
                onClick={() => handleSelectLanguage('vi')}
                className={`p-3 border-2 cursor-pointer flex items-center gap-3 transition-all ${
                  language === 'vi'
                    ? 'bg-[#262b44] border-[#fee761] shadow-pixel-sm -translate-y-0.5'
                    : 'bg-[#181425] border-[#3a4466] hover:border-[#5a6988]'
                }`}
              >
                <span className="text-3xl">🇻🇳</span>
                <div>
                  <div className="text-xs font-black text-white flex items-center gap-1.5">
                    <span>Tiếng Việt</span>
                    {language === 'vi' && (
                      <span className="text-[10px] bg-[#38b764] text-black px-1.5 py-0.2 font-bold">
                        Đang chọn
                      </span>
                    )}
                  </div>
                  <div className="text-[11px] text-[#8b9bb4]">Vietnamese (Mặc định)</div>
                </div>
              </div>

              {/* English */}
              <div
                onClick={() => handleSelectLanguage('en')}
                className={`p-3 border-2 cursor-pointer flex items-center gap-3 transition-all ${
                  language === 'en'
                    ? 'bg-[#262b44] border-[#fee761] shadow-pixel-sm -translate-y-0.5'
                    : 'bg-[#181425] border-[#3a4466] hover:border-[#5a6988]'
                }`}
              >
                <span className="text-3xl">🇬🇧</span>
                <div>
                  <div className="text-xs font-black text-white flex items-center gap-1.5">
                    <span>English</span>
                    {language === 'en' && (
                      <span className="text-[10px] bg-[#38b764] text-black px-1.5 py-0.2 font-bold">
                        Active
                      </span>
                    )}
                  </div>
                  <div className="text-[11px] text-[#8b9bb4]">Tiếng Anh</div>
                </div>
              </div>
            </div>
          </div>

          {/* MỤC 2: CÀI ĐẶT ÂM THANH (AUDIO & SOUND EFFECTS) */}
          <div className="bg-[#1a1c2c] border-2 border-[#3a4466] p-4 flex flex-col gap-3">
            <div className="flex items-center gap-2 text-xs font-bold text-white">
              {isMuted ? (
                <VolumeX size={16} className="text-[#e43b44]" />
              ) : (
                <Volume2 size={16} className="text-[#38b764]" />
              )}
              <span className="uppercase tracking-wider">{t('settings_sound_label')}</span>
            </div>
            <div className="text-xs text-[#8b9bb4]">
              {t('settings_sound_desc')}
            </div>

            <div className="flex flex-wrap items-center justify-between gap-3 pt-1">
              <button
                onClick={handleToggleSound}
                className={`px-3 py-2 text-xs font-bold border-2 transition-all flex items-center gap-2 cursor-pointer ${
                  !isMuted
                    ? 'bg-[#1a2e22] text-[#38b764] border-[#38b764]'
                    : 'bg-[#421d26] text-[#e43b44] border-[#e43b44]'
                }`}
              >
                {!isMuted ? <Volume2 size={16} /> : <VolumeX size={16} />}
                <span>{!isMuted ? t('settings_sound_on') : t('settings_sound_off')}</span>
              </button>

              {!isMuted && (
                <PixelButton variant="ghost" size="sm" onClick={handleTestAudio}>
                  <Play size={13} /> Thử âm thanh 8-bit
                </PixelButton>
              )}
            </div>
          </div>

          {/* MỤC 3: THÔNG TIN HỆ THỐNG */}
          <div className="bg-[#1a1c2c] border-2 border-[#3a4466] p-4 flex flex-col gap-2">
            <div className="flex items-center gap-2 text-xs font-bold text-[#fee761]">
              <Info size={15} />
              <span className="uppercase tracking-wider">{t('settings_about_label')}</span>
            </div>
            <div className="text-xs text-[#8b9bb4] leading-relaxed">
              {t('settings_about_desc')}
            </div>
            <div className="text-[11px] text-[#5a6988] mt-1">
              EasyTin v1.0.0 · Chương trình GDPT 2018 (Kết nối tri thức · Cánh Diều · Chân trời sáng tạo)
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="bg-[#1a1c2c] border-t-2 border-[#3a4466] px-5 py-3 flex justify-end">
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
