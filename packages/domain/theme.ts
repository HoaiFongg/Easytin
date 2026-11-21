// packages/domain/theme.ts
export type ThemeMode = 'dark' | 'light' | 'system';

export const STORAGE_THEME_KEY = 'easytin_theme';

const memoryStore = new Map<string, string>();

function safeGetStorage(key: string): string | null {
  try {
    if (typeof window !== 'undefined' && window.localStorage) {
      return window.localStorage.getItem(key);
    }
  } catch {}
  return memoryStore.get(key) || null;
}

function safeSetStorage(key: string, value: string): void {
  try {
    if (typeof window !== 'undefined' && window.localStorage) {
      window.localStorage.setItem(key, value);
      return;
    }
  } catch {}
  memoryStore.set(key, value);
}

export class ThemeManager {
  static getStoredTheme(): ThemeMode {
    const saved = safeGetStorage(STORAGE_THEME_KEY);
    if (saved === 'dark' || saved === 'light' || saved === 'system') {
      return saved;
    }
    return 'dark'; // Mặc định phong cách retro pixel tối
  }

  static setStoredTheme(theme: ThemeMode): void {
    safeSetStorage(STORAGE_THEME_KEY, theme);
    this.applyTheme(theme);
  }

  static getEffectiveTheme(theme: ThemeMode): 'dark' | 'light' {
    if (theme === 'system') {
      if (typeof window !== 'undefined' && window.matchMedia) {
        return window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
      }
      return 'dark';
    }
    return theme;
  }

  static applyTheme(theme: ThemeMode): void {
    if (typeof document === 'undefined') return;
    const effective = this.getEffectiveTheme(theme);
    const root = document.documentElement;

    if (effective === 'light') {
      root.classList.remove('dark');
      root.classList.add('light');
      root.setAttribute('data-theme', 'light');
    } else {
      root.classList.remove('light');
      root.classList.add('dark');
      root.setAttribute('data-theme', 'dark');
    }
  }

  static toggleTheme(current: ThemeMode): ThemeMode {
    const next: ThemeMode = current === 'light' ? 'dark' : 'light';
    this.setStoredTheme(next);
    return next;
  }
}
