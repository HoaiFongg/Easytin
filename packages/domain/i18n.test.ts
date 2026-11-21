import { describe, it, expect, beforeEach } from 'vitest';
import { getStoredLanguage, setStoredLanguage, t, TRANSLATIONS, TranslationKey } from './i18n';

describe('i18n Domain Unit Tests', () => {
  beforeEach(() => {
    setStoredLanguage('vi');
  });

  it('mặc định ngôn ngữ khởi tạo là tiếng Việt (vi)', () => {
    expect(getStoredLanguage()).toBe('vi');
    expect(t('app_title', 'vi')).toBe('EasyTin');
    expect(t('level_elementary', 'vi')).toBe('Tiểu học');
  });

  it('chuyển đổi và lưu trữ ngôn ngữ tiếng Anh (en)', () => {
    setStoredLanguage('en');
    expect(getStoredLanguage()).toBe('en');
    expect(t('level_elementary', 'en')).toBe('Elementary');
    expect(t('level_middle', 'en')).toBe('Middle School');
    expect(t('level_high', 'en')).toBe('High School');
    expect(t('settings_heading', 'en')).toBe('WEBSITE SETTINGS');
  });

  it('đảm bảo tất cả các khóa tiếng Việt đều có bản dịch tiếng Anh tương ứng', () => {
    const viKeys = Object.keys(TRANSLATIONS.vi) as TranslationKey[];
    const enKeys = Object.keys(TRANSLATIONS.en) as TranslationKey[];

    expect(viKeys.length).toBeGreaterThan(30);
    expect(enKeys.length).toBe(viKeys.length);

    viKeys.forEach((key) => {
      expect(TRANSLATIONS.en[key]).toBeDefined();
      expect(typeof TRANSLATIONS.en[key]).toBe('string');
      expect(TRANSLATIONS.en[key].length).toBeGreaterThan(0);
    });
  });

  it('xử lý chuyển đổi qua lại giữa tiếng Việt và tiếng Anh mượt mà', () => {
    expect(t('auth_tab_register', 'vi')).toBe('Tạo tài khoản');
    expect(t('auth_tab_register', 'en')).toBe('Sign Up');

    expect(t('btn_start_game', 'vi')).toBe('BẮT ĐẦU TRÒ CHƠI');
    expect(t('btn_start_game', 'en')).toBe('START INTERACTIVE GAME');
  });
});
