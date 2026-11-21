import React from 'react';

interface PixelIconProps {
  size?: number;
  className?: string;
  color?: string;
}

/**
 * 1. BIỂU TƯỢNG CẤP TIỂU HỌC: MÁY TÍNH HỌC TRÒ & BÀN PHÍM (24x24)
 * Thay thế cho icon balo hoặc các biểu tượng ngẫu nhiên.
 * Đại diện cho giai đoạn làm quen máy tính, chuột và bàn phím (Lớp 3–5).
 */
export const PixelElementaryIcon: React.FC<PixelIconProps> = ({ size = 24, className = '' }) => (
  <svg
    width={size}
    height={size}
    viewBox="0 0 24 24"
    fill="none"
    className={`inline-block shrink-0 ${className}`}
    style={{ shapeRendering: 'crispEdges' }}
  >
    {/* Vỏ màn hình CRT máy tính học trò */}
    <rect x="3" y="2" width="18" height="13" fill="#181425" />
    <rect x="4" y="3" width="16" height="11" fill="#262b44" />
    {/* Mặt gương màn hình xanh ngọc */}
    <rect x="5" y="4" width="14" height="9" fill="#0f2628" />
    <rect x="6" y="5" width="12" height="7" fill="#166534" />
    {/* Nội dung trên màn hình: Chữ "ABC" / Ký hiệu pixel */}
    <rect x="7" y="6" width="3" height="1" fill="#86efac" />
    <rect x="7" y="7" width="1" height="3" fill="#86efac" />
    <rect x="7" y="8" width="3" height="1" fill="#86efac" />
    <rect x="9" y="7" width="1" height="3" fill="#86efac" />
    {/* Dấu nhắc lệnh */}
    <rect x="12" y="8" width="3" height="2" fill="#fee761" />
    {/* Chân đế màn hình */}
    <rect x="10" y="15" width="4" height="2" fill="#5a6988" />
    <rect x="8" y="17" width="8" height="1" fill="#3a4466" />
    {/* Bàn phím & Chuột học sinh */}
    <rect x="4" y="19" width="12" height="3" fill="#181425" />
    <rect x="5" y="20" width="10" height="1" fill="#fee761" />
    {/* Chuột máy tính */}
    <rect x="18" y="19" width="3" height="3" fill="#38b764" />
    <rect x="19" y="19" width="1" height="1" fill="#ffffff" />
  </svg>
);

/**
 * 2. BIỂU TƯỢNG CẤP THCS: MẠNG MÁY TÍNH & DỮ LIỆU SỐ (24x24)
 * Thay thế cho icon cây thông hoặc biểu tượng ngẫu nhiên.
 * Đại diện cho giai đoạn Mạng máy tính, Internet, Bảng tính và Xử lý dữ liệu (Lớp 6–9).
 */
export const PixelMiddleSchoolIcon: React.FC<PixelIconProps> = ({ size = 24, className = '' }) => (
  <svg
    width={size}
    height={size}
    viewBox="0 0 24 24"
    fill="none"
    className={`inline-block shrink-0 ${className}`}
    style={{ shapeRendering: 'crispEdges' }}
  >
    {/* Máy chủ / Server trung tâm ở trên */}
    <rect x="8" y="2" width="8" height="7" fill="#181425" />
    <rect x="9" y="3" width="6" height="5" fill="#1f3b5c" />
    <rect x="10" y="4" width="4" height="1" fill="#2ce8f5" />
    <rect x="10" y="6" width="2" height="1" fill="#38b764" />
    <rect x="13" y="6" width="1" height="1" fill="#fee761" />

    {/* Đường cáp mạng LAN kết nối (Bus topology) */}
    <rect x="11" y="9" width="2" height="4" fill="#0284c7" />
    <rect x="4" y="13" width="16" height="2" fill="#0284c7" />
    <rect x="4" y="15" width="2" height="2" fill="#0284c7" />
    <rect x="18" y="15" width="2" height="2" fill="#0284c7" />

    {/* Nút mạng máy con bên trái (Trạm làm việc) */}
    <rect x="2" y="17" width="6" height="5" fill="#181425" />
    <rect x="3" y="18" width="4" height="3" fill="#3b82f6" />
    <rect x="4" y="19" width="2" height="1" fill="#ffffff" />

    {/* Nút mạng máy con bên phải (Trạm làm việc) */}
    <rect x="16" y="17" width="6" height="5" fill="#181425" />
    <rect x="17" y="18" width="4" height="3" fill="#3b82f6" />
    <rect x="18" y="19" width="2" height="1" fill="#ffffff" />
  </svg>
);

/**
 * 3. BIỂU TƯỢNG CẤP THPT: VI XỬ LÝ (CPU) & LẬP TRÌNH THUẬT TOÁN (24x24)
 * Thay thế cho icon đền thờ Hy Lạp.
 * Đại diện cho giai đoạn Khoa học máy tính chuyên sâu, AI, Cấu trúc dữ liệu & Lập trình (Lớp 10–12).
 */
export const PixelHighSchoolIcon: React.FC<PixelIconProps> = ({ size = 24, className = '' }) => (
  <svg
    width={size}
    height={size}
    viewBox="0 0 24 24"
    fill="none"
    className={`inline-block shrink-0 ${className}`}
    style={{ shapeRendering: 'crispEdges' }}
  >
    {/* Các chân tiếp xúc vàng (Gold connector pins) */}
    <rect x="6" y="1" width="2" height="3" fill="#feae34" />
    <rect x="11" y="1" width="2" height="3" fill="#feae34" />
    <rect x="16" y="1" width="2" height="3" fill="#feae34" />

    <rect x="6" y="20" width="2" height="3" fill="#feae34" />
    <rect x="11" y="20" width="2" height="3" fill="#feae34" />
    <rect x="16" y="20" width="2" height="3" fill="#feae34" />

    <rect x="1" y="6" width="3" height="2" fill="#feae34" />
    <rect x="1" y="11" width="3" height="2" fill="#feae34" />
    <rect x="1" y="16" width="3" height="2" fill="#feae34" />

    <rect x="20" y="6" width="3" height="2" fill="#feae34" />
    <rect x="20" y="11" width="3" height="2" fill="#feae34" />
    <rect x="20" y="16" width="3" height="2" fill="#feae34" />

    {/* Thân vi xử lý silicon */}
    <rect x="3" y="3" width="18" height="18" fill="#181425" />
    <rect x="4" y="4" width="16" height="16" fill="#4a154b" />
    <rect x="5" y="5" width="14" height="14" fill="#3e2731" />

    {/* Ký hiệu mã lệnh lập trình < / > */}
    <rect x="8" y="9" width="1" height="2" fill="#fee761" />
    <rect x="7" y="11" width="1" height="2" fill="#fee761" />
    <rect x="8" y="13" width="1" height="2" fill="#fee761" />

    <rect x="10" y="14" width="1" height="2" fill="#2ce8f5" />
    <rect x="11" y="12" width="1" height="2" fill="#2ce8f5" />
    <rect x="12" y="10" width="1" height="2" fill="#2ce8f5" />
    <rect x="13" y="8" width="1" height="2" fill="#2ce8f5" />

    <rect x="15" y="9" width="1" height="2" fill="#fee761" />
    <rect x="16" y="11" width="1" height="2" fill="#fee761" />
    <rect x="15" y="13" width="1" height="2" fill="#fee761" />
  </svg>
);

/**
 * 4. BIỂU TƯỢNG XP (ĐIỂM KINH NGHIỆM): TIA SÉT NĂNG LƯỢNG RETRO (16x16)
 * Thay thế cho Sparkles AI.
 */
export const PixelXpIcon: React.FC<PixelIconProps> = ({ size = 16, className = '' }) => (
  <svg
    width={size}
    height={size}
    viewBox="0 0 16 16"
    fill="none"
    className={`inline-block shrink-0 ${className}`}
    style={{ shapeRendering: 'crispEdges' }}
  >
    {/* Viền đổ bóng pixel */}
    <rect x="8" y="1" width="4" height="2" fill="#181425" />
    <rect x="6" y="3" width="5" height="2" fill="#181425" />
    <rect x="4" y="5" width="5" height="2" fill="#181425" />
    <rect x="2" y="7" width="12" height="2" fill="#181425" />
    <rect x="7" y="9" width="5" height="2" fill="#181425" />
    <rect x="6" y="11" width="4" height="2" fill="#181425" />
    <rect x="5" y="13" width="3" height="2" fill="#181425" />

    {/* Thân tia sét màu vàng hoàng gia & cam */}
    <rect x="9" y="1" width="3" height="2" fill="#fee761" />
    <rect x="7" y="3" width="4" height="2" fill="#fee761" />
    <rect x="5" y="5" width="4" height="2" fill="#fee761" />
    <rect x="3" y="7" width="10" height="2" fill="#feae34" />
    <rect x="8" y="9" width="4" height="2" fill="#fee761" />
    <rect x="7" y="11" width="3" height="2" fill="#fee761" />
    <rect x="6" y="13" width="2" height="2" fill="#fee761" />
    <rect x="6" y="5" width="1" height="3" fill="#ffffff" />
  </svg>
);

/**
 * 5. BIỂU TƯỢNG CHUỖI NGÀY HỌC (STREAK): NGỌN LỬA PIXEL (16x16)
 * Handcrafted Pixel Flame
 */
export const PixelFlameIcon: React.FC<PixelIconProps> = ({ size = 16, className = '' }) => (
  <svg
    width={size}
    height={size}
    viewBox="0 0 16 16"
    fill="none"
    className={`inline-block shrink-0 ${className}`}
    style={{ shapeRendering: 'crispEdges' }}
  >
    {/* Đáy ngọn lửa */}
    <rect x="4" y="6" width="8" height="8" fill="#181425" />
    <rect x="5" y="7" width="6" height="7" fill="#e43b44" />
    <rect x="6" y="4" width="4" height="4" fill="#181425" />
    <rect x="7" y="3" width="2" height="5" fill="#f77622" />
    <rect x="5" y="8" width="6" height="5" fill="#f77622" />
    {/* Tâm ngọn lửa màu vàng sáng */}
    <rect x="7" y="9" width="2" height="4" fill="#fee761" />
    <rect x="6" y="11" width="4" height="2" fill="#fee761" />
  </svg>
);

/**
 * 6. BIỂU TƯỢNG NGÔI SAO PIXEL ĐÁNH GIÁ (16x16)
 * Chuẩn 8-bit, góc cạnh dứt khoát, không bo tròn giả cầy
 */
interface PixelStarProps extends PixelIconProps {
  filled?: boolean;
}

export const PixelStarIcon: React.FC<PixelStarProps> = ({ size = 14, filled = false, className = '' }) => (
  <svg
    width={size}
    height={size}
    viewBox="0 0 14 14"
    fill="none"
    className={`inline-block shrink-0 ${className}`}
    style={{ shapeRendering: 'crispEdges' }}
  >
    {filled ? (
      <>
        {/* Viền đen bảo vệ */}
        <rect x="6" y="1" width="2" height="1" fill="#b45309" />
        <rect x="5" y="2" width="4" height="1" fill="#b45309" />
        <rect x="1" y="4" width="12" height="1" fill="#b45309" />
        <rect x="2" y="5" width="10" height="1" fill="#b45309" />
        <rect x="3" y="6" width="8" height="1" fill="#b45309" />
        <rect x="4" y="7" width="6" height="2" fill="#b45309" />
        <rect x="3" y="9" width="8" height="1" fill="#b45309" />
        <rect x="2" y="10" width="3" height="2" fill="#b45309" />
        <rect x="9" y="10" width="3" height="2" fill="#b45309" />
        {/* Lõi sao vàng óng */}
        <rect x="6" y="2" width="2" height="1" fill="#fee761" />
        <rect x="5" y="3" width="4" height="2" fill="#fee761" />
        <rect x="2" y="5" width="10" height="1" fill="#fee761" />
        <rect x="3" y="6" width="8" height="1" fill="#fee761" />
        <rect x="4" y="7" width="6" height="2" fill="#feae34" />
        <rect x="3" y="9" width="8" height="1" fill="#feae34" />
        <rect x="2" y="10" width="2" height="2" fill="#feae34" />
        <rect x="10" y="10" width="2" height="2" fill="#feae34" />
      </>
    ) : (
      <>
        {/* Sao rỗng khi chưa hoàn thành */}
        <rect x="6" y="1" width="2" height="1" fill="#5a6988" opacity="0.6" />
        <rect x="1" y="4" width="12" height="1" fill="#5a6988" opacity="0.6" />
        <rect x="3" y="7" width="8" height="1" fill="#5a6988" opacity="0.6" />
        <rect x="2" y="11" width="3" height="1" fill="#5a6988" opacity="0.6" />
        <rect x="9" y="11" width="3" height="1" fill="#5a6988" opacity="0.6" />
      </>
    )}
  </svg>
);

/**
 * 7. BIỂU TƯỢNG BẢN ĐỒ BÀI HỌC (16x16)
 * Thay thế cho Compass AI
 */
export const PixelMapIcon: React.FC<PixelIconProps> = ({ size = 16, className = '' }) => (
  <svg
    width={size}
    height={size}
    viewBox="0 0 16 16"
    fill="none"
    className={`inline-block shrink-0 ${className}`}
    style={{ shapeRendering: 'crispEdges' }}
  >
    {/* Bản đồ giấy gấp 3 nếp */}
    <rect x="1" y="2" width="14" height="12" fill="#181425" />
    <rect x="2" y="3" width="4" height="10" fill="#3b82f6" />
    <rect x="6" y="3" width="4" height="10" fill="#2563eb" />
    <rect x="10" y="3" width="4" height="10" fill="#1d4ed8" />
    {/* Đường mòn phiêu lưu đỏ */}
    <rect x="3" y="5" width="2" height="1" fill="#f87171" />
    <rect x="5" y="7" width="2" height="1" fill="#f87171" />
    <rect x="8" y="6" width="2" height="1" fill="#f87171" />
    <rect x="11" y="8" width="2" height="1" fill="#fee761" />
  </svg>
);

/**
 * 8. BIỂU TƯỢNG GIỚI THIỆU THÔNG TIN (16x16)
 * Dạng thẻ đĩa / chữ i pixel
 */
export const PixelInfoIcon: React.FC<PixelIconProps> = ({ size = 16, className = '' }) => (
  <svg
    width={size}
    height={size}
    viewBox="0 0 16 16"
    fill="none"
    className={`inline-block shrink-0 ${className}`}
    style={{ shapeRendering: 'crispEdges' }}
  >
    {/* Vòng tròn pixel */}
    <rect x="5" y="1" width="6" height="14" fill="#181425" />
    <rect x="2" y="4" width="12" height="8" fill="#181425" />
    <rect x="3" y="3" width="10" height="10" fill="#0284c7" />
    {/* Chấm tròn chữ i */}
    <rect x="7" y="4" width="2" height="2" fill="#ffffff" />
    {/* Thân chữ i */}
    <rect x="7" y="7" width="2" height="5" fill="#ffffff" />
    <rect x="6" y="7" width="1" height="1" fill="#ffffff" />
    <rect x="6" y="11" width="4" height="1" fill="#ffffff" />
  </svg>
);
