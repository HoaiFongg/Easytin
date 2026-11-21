import { Grade, UserProgressState } from './types';

const STORAGE_KEY = 'easytin_user_progress_v1';

export const DEFAULT_PROGRESS: UserProgressState = {
  version: '1.0.0',
  selectedGrade: 3,
  xp: 0,
  streakDays: 1,
  lastActiveDate: new Date().toISOString().split('T')[0],
  avatar: {
    base: 'tin_bot',
    hat: 'explorer_cap',
    color: '#38b764',
  },
  mastery: {},
  unlockedBadges: ['welcome_badge'],
};

export class LocalStorageAdapter {
  static loadProgress(): UserProgressState {
    try {
      const data = localStorage.getItem(STORAGE_KEY);
      if (!data) return DEFAULT_PROGRESS;
      const parsed = JSON.parse(data) as UserProgressState;
      // Merge with default to handle new fields safely
      return {
        ...DEFAULT_PROGRESS,
        ...parsed,
        avatar: { ...DEFAULT_PROGRESS.avatar, ...(parsed.avatar || {}) },
        mastery: parsed.mastery || {},
      };
    } catch {
      // Fallback for private mode or storage block
      return DEFAULT_PROGRESS;
    }
  }

  static saveProgress(state: UserProgressState): void {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (e) {
      console.warn('Could not save progress to localStorage', e);
    }
  }

  /**
   * Xuất tiến độ dưới dạng mã thẻ sao lưu ngắn (Base64)
   */
  static exportProgressCode(state: UserProgressState): string {
    const compact = {
      g: state.selectedGrade,
      xp: state.xp,
      m: state.mastery,
      b: state.unlockedBadges,
    };
    return btoa(unescape(encodeURIComponent(JSON.stringify(compact))));
  }

  /**
   * Nhập tiến độ từ mã thẻ sao lưu
   */
  static importProgressCode(code: string, current: UserProgressState): UserProgressState | null {
    try {
      const json = decodeURIComponent(escape(atob(code.trim())));
      const parsed = JSON.parse(json);
      return {
        ...current,
        selectedGrade: (parsed.g as Grade) || current.selectedGrade,
        xp: typeof parsed.xp === 'number' ? parsed.xp : current.xp,
        mastery: parsed.m || current.mastery,
        unlockedBadges: Array.isArray(parsed.b) ? parsed.b : current.unlockedBadges,
      };
    } catch {
      return null;
    }
  }
}
