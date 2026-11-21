import React from 'react';
import { useI18n } from '../i18nContext';
import { sound } from '../../packages/game-core/audio';

export interface PixelLogoProps {
  size?: 'sm' | 'md' | 'lg';
  showSubtitle?: boolean;
  animated?: boolean;
  onClick?: () => void;
  className?: string;
}

export const PixelLogo: React.FC<PixelLogoProps> = ({
  size = 'md',
  showSubtitle = true,
  animated = true,
  onClick,
  className = '',
}) => {
  const { t } = useI18n();

  const iconSizes = {
    sm: 30,
    md: 40,
    lg: 58,
  };

  const titleSizes = {
    sm: 'text-sm',
    md: 'text-base sm:text-lg',
    lg: 'text-xl sm:text-2xl',
  };

  const iconPixel = iconSizes[size];

  const handleClick = () => {
    sound.playJump();
    onClick?.();
  };

  return (
    <div
      onClick={handleClick}
      className={`flex items-center gap-2.5 select-none cursor-pointer group transition-transform duration-100 ${className}`}
      title="EasyTin — Nền tảng học Tin học dạng game Pixel"
    >
      {/* 1. BIỂU TƯỢNG PIXEL ART (RETRO CRT MONITOR + GAME CONSOLE + ET CHIP) */}
      <div
        className={`relative shrink-0 flex items-center justify-center transition-transform group-hover:scale-105 ${
          animated ? 'anim-pixel-idle' : ''
        }`}
        style={{ width: iconPixel, height: iconPixel }}
      >
        <svg
          viewBox="0 0 32 32"
          width={iconPixel}
          height={iconPixel}
          className="w-full h-full drop-shadow-[2px_2px_0px_#181425]"
          style={{ shapeRendering: 'crispEdges' }}
        >
          {/* ANTENNA CẶP TAI THỎ MÁY TÍNH RETRO */}
          <rect x="11" y="1" width="2" height="2" fill="#8b9bb4" />
          <rect x="12" y="3" width="2" height="2" fill="#8b9bb4" />
          <rect x="19" y="1" width="2" height="2" fill="#8b9bb4" />
          <rect x="18" y="3" width="2" height="2" fill="#8b9bb4" />
          <rect x="15" y="4" width="2" height="2" fill="#5a6988" />

          {/* VỎ MÁY CRT CHASSIS (y=5..26, x=2..29) */}
          {/* Viền đen bảo vệ pixel ngoài cùng */}
          <rect x="5" y="5" width="22" height="1" fill="#181425" />
          <rect x="3" y="6" width="26" height="1" fill="#181425" />
          <rect x="2" y="7" width="28" height="18" fill="#181425" />
          <rect x="3" y="25" width="26" height="1" fill="#181425" />
          <rect x="5" y="26" width="22" height="1" fill="#181425" />

          {/* Hiệu ứng viền sáng nổi khối 3D (Bevel highlight) */}
          <rect x="6" y="6" width="20" height="1" fill="#8b9bb4" />
          <rect x="3" y="7" width="26" height="1" fill="#5a6988" />
          <rect x="3" y="8" width="2" height="16" fill="#5a6988" />
          <rect x="27" y="8" width="2" height="16" fill="#1f2438" />
          <rect x="5" y="24" width="22" height="1" fill="#1f2438" />

          {/* Thân máy (Chassis body) */}
          <rect x="5" y="8" width="22" height="16" fill="#2b3350" />

          {/* KHUNG GƯƠNG MÀN HÌNH CHÌM (Screen bezel) */}
          <rect x="5" y="8" width="22" height="1" fill="#181425" />
          <rect x="5" y="9" width="1" height="13" fill="#181425" />
          <rect x="26" y="9" width="1" height="13" fill="#3a4466" />
          <rect x="5" y="21" width="22" height="1" fill="#3a4466" />

          {/* MẶT KÍNH ĐÈN HÌNH CRT (Screen glass) */}
          <rect x="6" y="9" width="20" height="12" fill="#0f2628" />
          <rect x="6" y="9" width="20" height="1" fill="#19484a" />
          <rect x="6" y="10" width="1" height="10" fill="#19484a" />

          {/* Ánh phản quang gương kính góc trên */}
          <rect x="7" y="10" width="3" height="1" fill="#2ce8f5" opacity="0.85" />
          <rect x="7" y="11" width="1" height="2" fill="#2ce8f5" opacity="0.85" />

          {/* CHỮ PIXEL "E" - MÀU XANH LỤC TIN HỌC (#38b764) */}
          <rect x="8" y="12" width="6" height="2" fill="#38b764" />
          <rect x="8" y="12" width="5" height="1" fill="#a7f070" />
          <rect x="8" y="14" width="2" height="4" fill="#38b764" />
          <rect x="8" y="15" width="4" height="2" fill="#38b764" />
          <rect x="8" y="15" width="4" height="1" fill="#a7f070" />
          <rect x="8" y="18" width="6" height="2" fill="#38b764" />
          <rect x="9" y="18" width="5" height="1" fill="#a7f070" />
          <rect x="8" y="19" width="6" height="1" fill="#24613b" />

          {/* CHỮ PIXEL "T" - MÀU VÀNG CHIẾN THẮNG (#fee761) */}
          <rect x="16" y="12" width="7" height="2" fill="#fee761" />
          <rect x="16" y="12" width="6" height="1" fill="#ffffff" />
          <rect x="18" y="14" width="3" height="5" fill="#fee761" />
          <rect x="18" y="14" width="1" height="5" fill="#ffffff" opacity="0.7" />
          <rect x="18" y="19" width="3" height="1" fill="#feae34" />
          <rect x="20" y="14" width="1" height="5" fill="#feae34" />

          {/* DẤU NHẮC LỆNH PIXEL NHẤP NHÁY (Cursor prompt) */}
          <rect
            x="22"
            y="18"
            width="2"
            height="1"
            fill="#2ce8f5"
            className={animated ? 'anim-pixel-blink' : ''}
          />

          {/* CẰM ĐIỀU KHIỂN & KHE ĐĨA MỀM (Monitor chin & controls) */}
          <rect x="6" y="22" width="20" height="2" fill="#20273d" />
          <rect x="7" y="23" width="9" height="1" fill="#100c1d" />
          <rect x="7" y="22" width="9" height="1" fill="#181425" />

          {/* Đèn nguồn Power LED xanh lục */}
          <rect x="19" y="23" width="2" height="1" fill="#38b764" className={animated ? 'anim-pixel-glow' : ''} />
          {/* Đèn Turbo LED vàng cam */}
          <rect x="23" y="23" width="2" height="1" fill="#feae34" />

          {/* CHÂN ĐẾ MÀN HÌNH (Pedestal & Base) */}
          <rect x="13" y="26" width="6" height="1" fill="#181425" />
          <rect x="14" y="27" width="4" height="2" fill="#3a4466" />
          <rect x="13" y="27" width="1" height="2" fill="#181425" />
          <rect x="18" y="27" width="1" height="2" fill="#181425" />
          <rect x="10" y="29" width="12" height="1" fill="#181425" />
          <rect x="9" y="30" width="14" height="1" fill="#5a6988" />
          <rect x="9" y="30" width="1" height="1" fill="#8b9bb4" />
          <rect x="9" y="31" width="14" height="1" fill="#181425" />
        </svg>
      </div>

      {/* 2. CHỮ THƯƠNG HIỆU (TYPOGRAPHY: EASY + TIN) */}
      <div className="flex flex-col text-left leading-none">
        <div className={`font-pixel ${titleSizes[size]} tracking-wider flex items-center gap-1`}>
          <span className="text-[#fee761] drop-shadow-[2px_2px_0px_#181425] group-hover:text-white transition-colors">
            EASY
          </span>
          <span className="text-[#38b764] drop-shadow-[2px_2px_0px_#181425] group-hover:text-[#a7f070] transition-colors">
            TIN
          </span>
          <span className="text-[12px] text-[#2ce8f5] drop-shadow-[1px_1px_0px_#181425] font-mono anim-pixel-blink font-bold ml-0.5">
            _
          </span>
        </div>

        {/* 3. KHẨU HIỆU & ĐỊNH HƯỚNG SƯ PHẠM */}
        {showSubtitle && (
          <div className="flex items-center gap-1.5 mt-1">
            <span className="text-[10px] sm:text-[11px] text-[#8b9bb4] group-hover:text-[#c0cbdc] transition-colors font-sans">
              {t('app_subtitle')}
            </span>
          </div>
        )}
      </div>
    </div>
  );
};
