import React, { useState } from 'react';
import { UserProgressState } from '../../packages/domain/types';
import { LocalStorageAdapter } from '../../packages/domain/storage';
import { PixelButton } from './PixelButton';
import { sound } from '../../packages/game-core/audio';
import { X, Copy, Check, Upload } from 'lucide-react';

interface ProgressSyncModalProps {
  progress: UserProgressState;
  onImportSuccess: (newProgress: UserProgressState) => void;
  onClose: () => void;
}

export const ProgressSyncModal: React.FC<ProgressSyncModalProps> = ({
  progress,
  onImportSuccess,
  onClose,
}) => {
  const code = LocalStorageAdapter.exportProgressCode(progress);
  const [copied, setCopied] = useState(false);
  const [importInput, setImportInput] = useState('');
  const [errorMsg, setErrorMsg] = useState<string | null>(null);

  const handleCopy = () => {
    sound.playClick();
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleImport = () => {
    if (!importInput.trim()) return;
    const res = LocalStorageAdapter.importProgressCode(importInput, progress);
    if (res) {
      sound.playVictory();
      onImportSuccess(res);
      onClose();
    } else {
      sound.playMistake();
      setErrorMsg('Mã thẻ không hợp lệ. Vui lòng kiểm tra lại!');
    }
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/80 flex items-center justify-center p-3 sm:p-5 overflow-y-auto">
      <div className="bg-[#181425] border-4 border-[#2ce8f5] shadow-pixel-lg w-full max-w-xl flex flex-col overflow-hidden">
        {/* Header */}
        <div className="flex items-center justify-between bg-[#262b44] px-4 py-3 border-b-3 border-[#3a4466]">
          <span className="text-xs font-black text-[#fee761] uppercase tracking-wider">
            MÃ THẺ TIẾN ĐỘ HỌC TẬP (SAO LƯU)
          </span>
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

        <div className="p-5 flex flex-col gap-5">
          {/* Xuất mã thẻ */}
          <div>
            <div className="text-xs text-[#8b9bb4] mb-2">
              Sao chép mã thẻ này để đem sang máy tính khác ở phòng thực hành:
            </div>
            <div className="flex items-center gap-2">
              <input
                readOnly
                value={code}
                className="flex-1 bg-[#181425] border-2 border-[#3a4466] p-2 text-xs font-mono text-[#fee761] outline-none select-all"
              />
              <PixelButton variant="primary" size="sm" onClick={handleCopy}>
                {copied ? <Check size={14} /> : <Copy size={14} />}
                {copied ? 'Đã chép' : 'Sao chép'}
              </PixelButton>
            </div>
          </div>

          <div className="border-t border-[#3a4466] pt-4">
            <div className="text-xs text-[#8b9bb4] mb-2">
              Hoặc nhập mã thẻ đã lưu để nạp lại sao và kinh nghiệm (XP):
            </div>
            <div className="flex flex-col gap-2">
              <textarea
                rows={3}
                value={importInput}
                onChange={(e) => {
                  setImportInput(e.target.value);
                  setErrorMsg(null);
                }}
                placeholder="Dán mã thẻ vào đây..."
                className="w-full bg-[#181425] border-2 border-[#5a6988] p-2.5 text-xs font-mono text-white outline-none focus:border-[#2ce8f5]"
              />
              {errorMsg && <div className="text-xs text-[#e43b44] font-bold">{errorMsg}</div>}
              <div className="flex justify-end">
                <PixelButton
                  variant="blue"
                  size="sm"
                  onClick={handleImport}
                  disabled={!importInput.trim()}
                >
                  <Upload size={14} /> Nạp tiến độ
                </PixelButton>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
