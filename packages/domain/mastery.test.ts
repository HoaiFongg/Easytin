import { describe, it, expect } from 'vitest';
import { LeitnerManager } from './mastery';

describe('Leitner Spaced Repetition Manager', () => {
  it('should initialize a record in box 1', () => {
    const record = LeitnerManager.createInitialRecord('G3-HARD-01');
    expect(record.nodeId).toBe('G3-HARD-01');
    expect(record.box).toBe(1);
    expect(record.stars).toBe(0);
    expect(record.attemptsCount).toBe(0);
    expect(record.isCompleted).toBe(false);
  });

  it('should advance from Box 1 to Box 2 on high score (>= 0.8)', () => {
    const init = LeitnerManager.createInitialRecord('G3-HARD-01');
    const updated = LeitnerManager.processAttempt(init, 0.9, 1000000);
    expect(updated.box).toBe(2);
    expect(updated.consecutiveSuccess).toBe(1);
    expect(updated.stars).toBe(2); // >= 0.85
    expect(updated.isCompleted).toBe(true);
    // Interval for box 2 is 3 days
    expect(updated.nextDueAt).toBe(1000000 + 3 * 24 * 60 * 60 * 1000);
  });

  it('should demote back to Box 1 on failure (< 0.8)', () => {
    const advanced = {
      nodeId: 'G3-HARD-01',
      box: 3 as const,
      consecutiveSuccess: 2,
      stars: 3,
      bestScore: 1.0,
      lastReviewedAt: 1000000,
      nextDueAt: 2000000,
      attemptsCount: 3,
      isCompleted: true,
    };

    const demoted = LeitnerManager.processAttempt(advanced, 0.5, 3000000);
    expect(demoted.box).toBe(1);
    expect(demoted.consecutiveSuccess).toBe(0);
    // Best score and stars are preserved
    expect(demoted.stars).toBe(3);
    expect(demoted.bestScore).toBe(1.0);
  });

  it('should accurately detect due status', () => {
    const rec = {
      nodeId: 'G3-HARD-01',
      box: 2 as const,
      consecutiveSuccess: 1,
      stars: 2,
      bestScore: 0.9,
      lastReviewedAt: 1000,
      nextDueAt: 5000,
      attemptsCount: 1,
      isCompleted: true,
    };

    expect(LeitnerManager.isDueForReview(rec, 4000)).toBe(false);
    expect(LeitnerManager.isDueForReview(rec, 5000)).toBe(true);
    expect(LeitnerManager.isDueForReview(rec, 6000)).toBe(true);
  });
});
