import { NodeMasteryRecord } from './types';

// Leitner intervals in days: Box 1 (1 day), Box 2 (3 days), Box 3 (7 days), Box 4 (21 days)
export const LEITNER_INTERVALS_DAYS = {
  1: 1,
  2: 3,
  3: 7,
  4: 21,
} as const;

const ONE_DAY_MS = 24 * 60 * 60 * 1000;

export class LeitnerManager {
  /**
   * Tạo bản ghi tiến độ ban đầu cho một node kiến thức
   */
  static createInitialRecord(nodeId: string): NodeMasteryRecord {
    return {
      nodeId,
      box: 1,
      consecutiveSuccess: 0,
      stars: 0,
      bestScore: 0,
      lastReviewedAt: 0,
      nextDueAt: 0,
      attemptsCount: 0,
      isCompleted: false,
    };
  }

  /**
   * Cập nhật kết quả sau một phiên học hoặc ôn tập
   * @param record Bản ghi hiện tại
   * @param score Điểm số đạt được (0.0 đến 1.0)
   * @param now Thời điểm đánh giá (timestamp ms)
   */
  static processAttempt(
    record: NodeMasteryRecord,
    score: number,
    now: number = Date.now()
  ): NodeMasteryRecord {
    const isSuccess = score >= 0.8;
    const attempts = record.attemptsCount + 1;
    let nextBox = record.box;
    let consecutive = record.consecutiveSuccess;

    if (isSuccess) {
      consecutive += 1;
      // Nếu đúng và đang ở hộp < 4, thăng cấp lên hộp kế tiếp
      if (nextBox < 4) {
        nextBox = (nextBox + 1) as 1 | 2 | 3 | 4;
      }
    } else {
      consecutive = 0;
      // Nếu sai, lùi về hộp 1 (hoặc giảm 1 hộp nếu đang ở hộp cao)
      nextBox = 1;
    }

    // Tính số sao (1 sao nếu qua bài, 2 sao nếu >= 85%, 3 sao nếu 100%)
    let starsEarned = 1;
    if (score >= 1.0) starsEarned = 3;
    else if (score >= 0.85) starsEarned = 2;

    const newStars = Math.max(record.stars, starsEarned);
    const intervalDays = LEITNER_INTERVALS_DAYS[nextBox];
    const nextDue = now + intervalDays * ONE_DAY_MS;

    return {
      nodeId: record.nodeId,
      box: nextBox,
      consecutiveSuccess: consecutive,
      stars: newStars,
      bestScore: Math.max(record.bestScore, score),
      lastReviewedAt: now,
      nextDueAt: nextDue,
      attemptsCount: attempts,
      isCompleted: true,
    };
  }

  /**
   * Kiểm tra xem một node đã đến hạn cần ôn tập hay chưa
   */
  static isDueForReview(record: NodeMasteryRecord, now: number = Date.now()): boolean {
    if (!record.isCompleted || record.nextDueAt === 0) return false;
    return now >= record.nextDueAt;
  }

  /**
   * Tính toán tỉ lệ thông thạo tổng thể (Mastery Rate)
   */
  static calculateMasteryPercentage(records: Record<string, NodeMasteryRecord>, totalNodes: number): number {
    if (totalNodes === 0) return 0;
    const values = Object.values(records);
    let totalScore = 0;
    for (const r of values) {
      totalScore += r.box; // Box 1-4
    }
    // Max điểm nếu toàn bộ nodes đạt Box 4
    const maxPossible = totalNodes * 4;
    return Math.min(100, Math.round((totalScore / maxPossible) * 100));
  }
}
