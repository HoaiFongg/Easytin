import React from 'react';

export type MascotId =
  | 'tin_bot'
  | 'cat_explorer'
  | 'wizard_algo'
  | 'astro_coder'
  | 'fox_clever'
  | 'owl_scholar';

interface PixelMascotProps {
  mascotId: MascotId | string;
  size?: 'xs' | 'sm' | 'md' | 'lg' | 'xl' | number;
  animated?: boolean;
  className?: string;
  title?: string;
  onClick?: () => void;
}

const SIZE_MAP = {
  xs: 24,
  sm: 32,
  md: 48,
  lg: 72,
  xl: 112,
};

export const PixelMascot: React.FC<PixelMascotProps> = ({
  mascotId,
  size = 'md',
  animated = true,
  className = '',
  title,
  onClick,
}) => {
  const pixelSize = typeof size === 'number' ? size : SIZE_MAP[size] || 48;
  const animClass = animated ? 'anim-pixel-idle' : '';

  const renderSvg = () => {
    switch (mascotId) {
      case 'cat_explorer':
        return (
          // MÈO THÁM HIỂM (Explorer Cat) - Nón thám hiểm, râu pixel, đuôi nhúc nhích
          <svg
            viewBox="0 0 32 32"
            width={pixelSize}
            height={pixelSize}
            className={`${animClass} ${className}`}
            style={{ shapeRendering: 'crispEdges' }}
          >
            {/* Đuôi mèo ở góc sau */}
            <g className={animated ? 'anim-pixel-sway' : ''} style={{ transformOrigin: '24px 24px' }}>
              <rect x="23" y="19" width="3" height="3" fill="#d9751e" />
              <rect x="25" y="16" width="3" height="4" fill="#f79e38" />
              <rect x="26" y="13" width="3" height="4" fill="#fee761" />
              <rect x="25" y="11" width="3" height="3" fill="#ffffff" />
            </g>

            {/* Thân mèo */}
            <rect x="9" y="18" width="14" height="11" fill="#f79e38" />
            <rect x="11" y="20" width="10" height="9" fill="#ffffff" />
            <rect x="8" y="27" width="5" height="3" fill="#d9751e" />
            <rect x="19" y="27" width="5" height="3" fill="#d9751e" />

            {/* Tai mèo */}
            <polygon points="6,9 11,9 7,4" fill="#f79e38" />
            <polygon points="7,8 10,8 8,5" fill="#fca3ca" />
            <polygon points="21,9 26,9 25,4" fill="#f79e38" />
            <polygon points="22,8 25,8 24,5" fill="#fca3ca" />

            {/* Đầu mèo */}
            <rect x="6" y="9" width="20" height="12" fill="#f79e38" />
            <rect x="5" y="12" width="22" height="7" fill="#f79e38" />

            {/* Mũ thám hiểm */}
            <rect x="4" y="9" width="24" height="2" fill="#8f563b" />
            <rect x="8" y="4" width="16" height="5" fill="#a06847" />
            <rect x="7" y="7" width="18" height="2" fill="#693c26" />
            <rect x="14" y="6" width="4" height="2" fill="#fee761" />

            {/* Mắt mèo */}
            <rect x="9" y="13" width="3" height="3" fill="#38b764" />
            <rect x="10" y="13" width="1" height="1" fill="#ffffff" />
            <rect x="20" y="13" width="3" height="3" fill="#38b764" />
            <rect x="21" y="13" width="1" height="1" fill="#ffffff" />

            {/* Mũi & Miệng */}
            <rect x="15" y="16" width="2" height="1" fill="#fca3ca" />
            <rect x="14" y="17" width="1" height="1" fill="#181425" />
            <rect x="17" y="17" width="1" height="1" fill="#181425" />

            {/* Râu mèo */}
            <line x1="3" y1="14" x2="7" y2="15" stroke="#181425" strokeWidth="1" />
            <line x1="3" y1="17" x2="7" y2="17" stroke="#181425" strokeWidth="1" />
            <line x1="25" y1="15" x2="29" y2="14" stroke="#181425" strokeWidth="1" />
            <line x1="25" y1="17" x2="29" y2="17" stroke="#181425" strokeWidth="1" />
          </svg>
        );

      case 'wizard_algo':
        return (
          // PHÁP SƯ LOGIC (Algorithm Wizard) - Nón chóp sao, râu bạc, gậy phép
          <svg
            viewBox="0 0 32 32"
            width={pixelSize}
            height={pixelSize}
            className={`${animClass} ${className}`}
            style={{ shapeRendering: 'crispEdges' }}
          >
            {/* Gậy phép thuật & Quả cầu năng lượng phát sáng */}
            <g className={animated ? 'anim-pixel-glow' : ''}>
              <line x1="27" y1="8" x2="27" y2="29" stroke="#8f563b" strokeWidth="2" />
              <rect x="25" y="5" width="4" height="4" fill="#2ce8f5" />
              <rect x="26" y="6" width="2" height="2" fill="#ffffff" />
              <polygon points="27,3 29,5 25,5" fill="#fee761" />
              <circle cx="27" cy="7" r="4" fill="none" stroke="#2ce8f5" strokeWidth="0.5" opacity="0.6" />
            </g>

            {/* Áo choàng pháp sư */}
            <polygon points="8,17 24,17 25,29 7,29" fill="#3b2d54" />
            <rect x="11" y="18" width="10" height="11" fill="#4f3b73" />
            <line x1="16" y1="18" x2="16" y2="29" stroke="#fee761" strokeWidth="1" />

            {/* Mặt pháp sư */}
            <rect x="10" y="11" width="12" height="7" fill="#fbd1a2" />
            {/* Mắt thông thái */}
            <rect x="11" y="13" width="2" height="2" fill="#181425" />
            <rect x="19" y="13" width="2" height="2" fill="#181425" />

            {/* Bộ râu trắng dài uyên bác */}
            <polygon points="9,16 23,16 16,26" fill="#f0f3f8" />
            <polygon points="11,18 21,18 16,24" fill="#ffffff" />

            {/* Nón phù thủy tím viền vàng */}
            <rect x="6" y="11" width="20" height="3" fill="#241a35" />
            <rect x="8" y="9" width="16" height="2" fill="#fee761" />
            <polygon points="9,9 23,9 18,1" fill="#4f3b73" />
            <polygon points="12,7 20,7 18,1" fill="#3b2d54" />
            <polygon points="18,1 21,2 19,4" fill="#fee761" />
            {/* Ngôi sao trên mũ */}
            <rect x="15" y="5" width="2" height="2" fill="#fee761" />
          </svg>
        );

      case 'astro_coder':
        return (
          // PHI HÀNH GIA CODER (Space Coder) - Mũ bảo hiểm vũ trụ phản quang, động cơ phản lực
          <svg
            viewBox="0 0 32 32"
            width={pixelSize}
            height={pixelSize}
            className={`${animClass} ${className}`}
            style={{ shapeRendering: 'crispEdges' }}
          >
            {/* Tia lửa phản lực đẩy ở chân */}
            <g className={animated ? 'anim-pixel-sparkle' : ''}>
              <polygon points="10,28 13,28 11.5,32" fill="#f77622" />
              <polygon points="19,28 22,28 20.5,32" fill="#f77622" />
              <polygon points="11,28 12,28 11.5,30" fill="#fee761" />
              <polygon points="20,28 21,28 20.5,30" fill="#fee761" />
            </g>

            {/* Bình oxy / Ba lô vũ trụ */}
            <rect x="6" y="11" width="20" height="14" fill="#8b9bb4" rx="2" />

            {/* Thân đồ phi hành */}
            <rect x="8" y="18" width="16" height="10" fill="#ffffff" />
            <rect x="11" y="20" width="10" height="6" fill="#262b44" />
            <rect x="13" y="21" width="2" height="2" fill="#2ce8f5" />
            <rect x="17" y="21" width="2" height="2" fill="#38b764" />
            <rect x="13" y="24" width="6" height="1" fill="#fee761" />

            {/* Chân & Tay */}
            <rect x="5" y="19" width="3" height="6" fill="#ffffff" />
            <rect x="24" y="19" width="3" height="6" fill="#ffffff" />
            <rect x="9" y="27" width="5" height="2" fill="#c0cbdc" />
            <rect x="18" y="27" width="5" height="2" fill="#c0cbdc" />

            {/* Nón bảo hiểm tròn */}
            <circle cx="16" cy="11" r="8" fill="#ffffff" stroke="#c0cbdc" strokeWidth="1" />
            {/* Kính nón phi hành gia (Visor) phản chiếu mã code */}
            <rect x="11" y="7" width="10" height="8" rx="2" fill="#181425" />
            <rect x="12" y="8" width="8" height="6" rx="1" fill="#1f2438" />
            {/* Vệt phản chiếu ánh sáng & code pixel */}
            <line x1="13" y1="9" x2="15" y2="9" stroke="#38b764" strokeWidth="1" />
            <line x1="13" y1="11" x2="17" y2="11" stroke="#2ce8f5" strokeWidth="1" />
            <rect x="18" y="9" width="1" height="1" fill="#fee761" />
          </svg>
        );

      case 'fox_clever':
        return (
          // CÁO THÔNG THÁI (Clever Fox) - Đeo kính trí tuệ, đuôi xoè đuôi trắng
          <svg
            viewBox="0 0 32 32"
            width={pixelSize}
            height={pixelSize}
            className={`${animClass} ${className}`}
            style={{ shapeRendering: 'crispEdges' }}
          >
            {/* Đuôi cáo bồng bềnh */}
            <g className={animated ? 'anim-pixel-sway' : ''} style={{ transformOrigin: '23px 25px' }}>
              <polygon points="21,18 27,15 28,24 20,26" fill="#f77622" />
              <polygon points="25,16 28,15 29,20 27,21" fill="#ffffff" />
            </g>

            {/* Thân cáo */}
            <rect x="10" y="18" width="12" height="10" fill="#f77622" />
            <rect x="12" y="19" width="8" height="8" fill="#ffffff" />
            <rect x="9" y="27" width="4" height="3" fill="#262b44" />
            <rect x="19" y="27" width="4" height="3" fill="#262b44" />

            {/* Tai cáo nhọn viền đen */}
            <polygon points="6,4 12,10 6,10" fill="#f77622" />
            <polygon points="6,4 9,4 6,7" fill="#181425" />
            <polygon points="7,6 10,9 7,9" fill="#ffffff" />
            <polygon points="26,4 20,10 26,10" fill="#f77622" />
            <polygon points="26,4 23,4 26,7" fill="#181425" />
            <polygon points="25,6 22,9 25,9" fill="#ffffff" />

            {/* Khuôn mặt cáo */}
            <rect x="7" y="10" width="18" height="8" fill="#f77622" />
            <polygon points="7,14 16,21 7,18" fill="#ffffff" />
            <polygon points="25,14 16,21 25,18" fill="#ffffff" />
            <rect x="15" y="18" width="2" height="2" fill="#181425" />

            {/* Cặp kính tri thức màu vàng gold */}
            <rect x="8" y="12" width="6" height="4" fill="none" stroke="#fee761" strokeWidth="1.2" />
            <rect x="18" y="12" width="6" height="4" fill="none" stroke="#fee761" strokeWidth="1.2" />
            <line x1="14" y1="14" x2="18" y2="14" stroke="#fee761" strokeWidth="1.2" />
            {/* Mắt sáng nháy */}
            <rect x="10" y="13" width="2" height="2" fill="#181425" />
            <rect x="11" y="13" width="1" height="1" fill="#ffffff" />
            <rect x="20" y="13" width="2" height="2" fill="#181425" />
            <rect x="21" y="13" width="1" height="1" fill="#ffffff" />
          </svg>
        );

      case 'owl_scholar':
        return (
          // CÚ TRÍ TUỆ (Scholar Owl) - Mũ cử nhân tốt nghiệp, mắt tròn to, cầm sách
          <svg
            viewBox="0 0 32 32"
            width={pixelSize}
            height={pixelSize}
            className={`${animClass} ${className}`}
            style={{ shapeRendering: 'crispEdges' }}
          >
            {/* Thân cú vạc lông nâu */}
            <ellipse cx="16" cy="18" rx="10" ry="10" fill="#8f563b" />
            <ellipse cx="16" cy="19" rx="7" ry="7" fill="#d9a066" />
            {/* Chân móng bám */}
            <rect x="11" y="27" width="3" height="3" fill="#f77622" />
            <rect x="18" y="27" width="3" height="3" fill="#f77622" />

            {/* Cánh cú khép 2 bên */}
            <path d="M 6 15 Q 5 22 9 24" stroke="#693c26" strokeWidth="2" fill="none" />
            <path d="M 26 15 Q 27 22 23 24" stroke="#693c26" strokeWidth="2" fill="none" />

            {/* Mắt tròn to đặc trưng của Cú học giả */}
            <circle cx="11" cy="14" r="4" fill="#ffffff" stroke="#181425" strokeWidth="1" />
            <circle cx="11" cy="14" r="2" fill="#181425" />
            <circle cx="10" cy="13" r="0.8" fill="#ffffff" />
            <circle cx="21" cy="14" r="4" fill="#ffffff" stroke="#181425" strokeWidth="1" />
            <circle cx="21" cy="14" r="2" fill="#181425" />
            <circle cx="20" cy="13" r="0.8" fill="#ffffff" />

            {/* Mỏ cú nhọn */}
            <polygon points="15,16 17,16 16,19" fill="#f77622" />

            {/* Mũ cử nhân (Mortarboard Cap) */}
            <polygon points="16,4 27,8 16,11 5,8" fill="#181425" />
            <rect x="12" y="8" width="8" height="3" fill="#262b44" />
            {/* Nút mũ & Dây tua rua vàng */}
            <rect x="15" y="6" width="2" height="2" fill="#fee761" />
            <line x1="16" y1="7" x2="25" y2="10" stroke="#fee761" strokeWidth="1" />
            <rect x="24" y="10" width="2" height="3" fill="#fee761" />
          </svg>
        );

      case 'tin_bot':
      default:
        return (
          // TIN BOT (Robot Bạn Nhỏ) - Đèn anten phát sáng, mắt số pixel, màn hình tim
          <svg
            viewBox="0 0 32 32"
            width={pixelSize}
            height={pixelSize}
            className={`${animClass} ${className}`}
            style={{ shapeRendering: 'crispEdges' }}
          >
            {/* Đèn Anten trên đầu nhấp nháy */}
            <g className={animated ? 'anim-pixel-glow' : ''}>
              <line x1="16" y1="1" x2="16" y2="7" stroke="#38b764" strokeWidth="2" />
              <rect x="14" y="0" width="4" height="4" fill="#fee761" />
              <rect x="15" y="1" width="2" height="2" fill="#ffffff" />
            </g>

            {/* Tai bu lông 2 bên */}
            <rect x="4" y="10" width="3" height="5" fill="#5a6988" />
            <rect x="25" y="10" width="3" height="5" fill="#5a6988" />

            {/* Đầu Robot kim loại */}
            <rect x="6" y="6" width="20" height="12" fill="#2ce8f5" />
            <rect x="7" y="7" width="18" height="10" fill="#1a3826" />
            {/* Viền kim loại bóng */}
            <line x1="7" y1="7" x2="24" y2="7" stroke="#a7f070" strokeWidth="1" />

            {/* Mắt số điện tử LED (Digital Pixel Eyes) */}
            <g className={animated ? 'anim-pixel-blink' : ''}>
              <rect x="9" y="10" width="4" height="4" fill="#38b764" />
              <rect x="10" y="11" width="2" height="2" fill="#ffffff" />
              <rect x="19" y="10" width="4" height="4" fill="#38b764" />
              <rect x="20" y="11" width="2" height="2" fill="#ffffff" />
            </g>

            {/* Nụ cười pixel của Robot */}
            <rect x="13" y="15" width="6" height="1" fill="#fee761" />

            {/* Cổ nối */}
            <rect x="13" y="18" width="6" height="2" fill="#5a6988" />

            {/* Thân Robot */}
            <rect x="7" y="20" width="18" height="9" fill="#2ce8f5" />
            <rect x="8" y="21" width="16" height="7" fill="#181425" />

            {/* Lõi tim năng lượng / Monitor ngực */}
            <rect x="11" y="22" width="10" height="5" fill="#262b44" />
            {/* Biểu tượng trái tim / nhịp tim pixel */}
            <g className={animated ? 'anim-pixel-glow' : ''}>
              <polygon points="14,24 16,26 18,24 17,23 16,24 15,23" fill="#e43b44" />
              <rect x="12" y="24" width="2" height="1" fill="#fee761" />
              <rect x="18" y="24" width="2" height="1" fill="#fee761" />
            </g>

            {/* Chân / Bánh xích robot */}
            <rect x="9" y="29" width="4" height="3" fill="#5a6988" />
            <rect x="19" y="29" width="4" height="3" fill="#5a6988" />
          </svg>
        );
    }
  };

  return (
    <div
      onClick={onClick}
      title={title}
      className={`inline-flex items-center justify-center select-none ${
        onClick ? 'cursor-pointer hover:scale-110 transition-transform' : ''
      }`}
      style={{ width: pixelSize, height: pixelSize }}
    >
      {renderSvg()}
    </div>
  );
};
