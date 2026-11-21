import React, { useState } from 'react';
import { PixelButton } from './PixelButton';
import { sound } from '../../packages/game-core/audio';
import { X, GraduationCap, Users, BarChart3, Plus, Key, AlertTriangle } from 'lucide-react';

interface TeacherDashboardModalProps {
  onClose: () => void;
}

export const TeacherDashboardModal: React.FC<TeacherDashboardModalProps> = ({ onClose }) => {
  const [classCode, setClassCode] = useState('TIN402');

  const generateNewCode = () => {
    sound.playClick();
    const randomNum = Math.floor(100 + Math.random() * 900);
    setClassCode(`TIN${randomNum}`);
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/80 flex items-center justify-center p-3 sm:p-5 overflow-y-auto">
      <div className="bg-[#181425] border-4 border-[#38b764] shadow-pixel-lg w-full max-w-3xl max-h-[90vh] flex flex-col overflow-hidden">
        {/* Header */}
        <div className="flex items-center justify-between bg-[#262b44] px-4 py-3 border-b-3 border-[#3a4466]">
          <div className="flex items-center gap-2">
            <GraduationCap size={18} className="text-[#38b764]" />
            <span className="font-pixel text-xs text-[#fee761]">
              CỔNG QUẢN LÝ DÀNH CHO THẦY CÔ
            </span>
          </div>
          <button
            onClick={() => {
              sound.playClick();
              onClose();
            }}
            className="text-[#8b9bb4] hover:text-white cursor-pointer p-1"
          >
            <X size={18} />
          </button>
        </div>

        {/* Nội dung */}
        <div className="p-5 overflow-y-auto flex flex-col gap-6">
          {/* Tạo mã lớp nhanh không cần email */}
          <div className="bg-[#1a1c2c] border-2 border-[#5a6988] p-4 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>
              <div className="font-bold text-sm text-white flex items-center gap-2">
                <Key size={16} className="text-[#fee761]" /> Mã phòng học Tin học
              </div>
              <div className="text-xs text-[#8b9bb4] mt-0.5">
                Học sinh chỉ cần nhập mã này + Biệt danh để vào lớp, không cần tạo tài khoản hay email!
              </div>
            </div>
            <div className="flex items-center gap-3">
              <div className="font-pixel text-xl text-[#38b764] bg-[#181425] px-4 py-2 border-2 border-[#38b764]">
                {classCode}
              </div>
              <PixelButton variant="primary" size="sm" onClick={generateNewCode}>
                <Plus size={14} /> Đổi mã
              </PixelButton>
            </div>
          </div>

          {/* Phân tích lỗ hổng nhận thức (Misconception Heatmap) */}
          <div>
            <div className="font-pixel text-xs text-[#fee761] mb-2 flex items-center gap-2">
              <BarChart3 size={15} /> CẢNH BÁO LỖ HỔNG KIẾN THỨC CỦA LỚP:
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div className="bg-[#262b44] border-2 border-[#e43b44] p-3 flex items-start gap-2.5">
                <AlertTriangle className="text-[#e43b44] shrink-0 mt-0.5" size={18} />
                <div>
                  <div className="text-xs font-bold text-white">Nhầm lẫn giữa Màn hình cảm ứng (Vào/Ra)</div>
                  <div className="text-[11px] text-[#8b9bb4] mt-0.5">
                    35% học sinh chọn màn hình cảm ứng chỉ là thiết bị xuất hình ảnh.
                  </div>
                </div>
              </div>
              <div className="bg-[#262b44] border-2 border-[#feae34] p-3 flex items-start gap-2.5">
                <AlertTriangle className="text-[#feae34] shrink-0 mt-0.5" size={18} />
                <div>
                  <div className="text-xs font-bold text-white">Chuyển đổi số nhị phân có nhớ</div>
                  <div className="text-[11px] text-[#8b9bb4] mt-0.5">
                    28% học sinh quên cộng bit 1 khi giá trị vượt quá 8.
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Danh sách học sinh trong lớp mẫu */}
          <div>
            <div className="font-pixel text-xs text-[#fee761] mb-2 flex items-center gap-2">
              <Users size={15} /> DANH SÁCH HỌC SINH ĐANG HỌC (38/40):
            </div>
            <div className="bg-[#181425] border-2 border-[#3a4466] divide-y divide-[#3a4466]">
              {[
                { name: 'Bảo An (Sóc Nâu)', stars: 3, box: 3, status: 'Hoàn thành' },
                { name: 'Minh Khôi (Robot)', stars: 2, box: 2, status: 'Đang ôn tập' },
                { name: 'Phương Linh (Mèo Con)', stars: 3, box: 4, status: 'Đạt Mastery' },
                { name: 'Huy Hoàng (Chiến Binh)', stars: 1, box: 1, status: 'Cần hỗ trợ' },
              ].map((st, i) => (
                <div key={i} className="p-2.5 flex items-center justify-between text-xs">
                  <span className="font-bold text-white">{st.name}</span>
                  <div className="flex items-center gap-4">
                    <span className="text-[#fee761]">⭐ {st.stars} sao</span>
                    <span className="text-[#2ce8f5]">Hộp Leitner {st.box}</span>
                    <span className="text-[#38b764] font-semibold">{st.status}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
