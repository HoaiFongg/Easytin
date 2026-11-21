// packages/domain/theme.test.ts
import { describe, it, expect, beforeEach } from 'vitest';
import { ThemeManager } from './theme';

describe('ThemeManager Domain Tests', () => {
  beforeEach(() => {
    ThemeManager.setStoredTheme('dark');
  });

  it('mặc định trả về dark khi khởi tạo', () => {
    expect(ThemeManager.getStoredTheme()).toBe('dark');
  });

  it('lưu và đọc đúng chế độ light và dark', () => {
    ThemeManager.setStoredTheme('light');
    expect(ThemeManager.getStoredTheme()).toBe('light');

    ThemeManager.setStoredTheme('dark');
    expect(ThemeManager.getStoredTheme()).toBe('dark');

    ThemeManager.setStoredTheme('system');
    expect(ThemeManager.getStoredTheme()).toBe('system');
  });

  it('xác định đúng effectiveTheme', () => {
    expect(ThemeManager.getEffectiveTheme('dark')).toBe('dark');
    expect(ThemeManager.getEffectiveTheme('light')).toBe('light');
  });

  it('toggleTheme đảo ngược chuẩn xác giữa light và dark', () => {
    const next1 = ThemeManager.toggleTheme('dark');
    expect(next1).toBe('light');
    expect(ThemeManager.getStoredTheme()).toBe('light');

    const next2 = ThemeManager.toggleTheme('light');
    expect(next2).toBe('dark');
    expect(ThemeManager.getStoredTheme()).toBe('dark');
  });

  it('applyTheme hoạt động an toàn và cập nhật thuộc tính khi có document', () => {
    const mockRoot = {
      classList: {
        classes: new Set<string>(),
        add(c: string) { this.classes.add(c); },
        remove(c: string) { this.classes.delete(c); },
        contains(c: string) { return this.classes.has(c); }
      },
      attributes: {} as Record<string, string>,
      setAttribute(k: string, v: string) { this.attributes[k] = v; },
      getAttribute(k: string) { return this.attributes[k]; }
    };

    (globalThis as any).document = {
      documentElement: mockRoot
    };

    ThemeManager.applyTheme('light');
    expect(mockRoot.classList.contains('light')).toBe(true);
    expect(mockRoot.classList.contains('dark')).toBe(false);
    expect(mockRoot.getAttribute('data-theme')).toBe('light');

    ThemeManager.applyTheme('dark');
    expect(mockRoot.classList.contains('dark')).toBe(true);
    expect(mockRoot.classList.contains('light')).toBe(false);
    expect(mockRoot.getAttribute('data-theme')).toBe('dark');

    delete (globalThis as any).document;
  });
});
