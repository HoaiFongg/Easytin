import { describe, it, expect } from 'vitest';
import { AVATAR_OPTIONS } from './account';

describe('Pixel Mascot System Unit Tests', () => {
  it('đảm bảo đầy đủ 6 linh vật giáo dục độc đáo', () => {
    expect(AVATAR_OPTIONS.length).toBe(6);
    const ids = AVATAR_OPTIONS.map((a) => a.id);
    expect(ids).toContain('tin_bot');
    expect(ids).toContain('cat_explorer');
    expect(ids).toContain('wizard_algo');
    expect(ids).toContain('astro_coder');
    expect(ids).toContain('fox_clever');
    expect(ids).toContain('owl_scholar');
  });

  it('mỗi linh vật đều có tên sư phạm, vai trò và màu sắc nhận diện', () => {
    AVATAR_OPTIONS.forEach((mascot) => {
      expect(mascot.name).toBeDefined();
      expect(mascot.name.length).toBeGreaterThan(0);
      expect(mascot.role).toBeDefined();
      expect(mascot.badgeColor).toMatch(/^#[0-9a-fA-F]{6}$/);
    });
  });
});
