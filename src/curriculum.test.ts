import { describe, it, expect } from 'vitest';
import curriculumData from '../curriculum.json';

describe('EasyTin Curriculum Schema & Data Integrity', () => {
  it('should contain all 3 primary worlds', () => {
    expect(curriculumData.worlds).toHaveLength(3);
    const worldIds = curriculumData.worlds.map((w) => w.id);
    expect(worldIds).toContain('w1');
    expect(worldIds).toContain('w2');
    expect(worldIds).toContain('w3');
  });

  it('should ensure each node has valid structure and game config', () => {
    expect(curriculumData.nodes.length).toBeGreaterThan(0);

    for (const node of curriculumData.nodes) {
      expect(node.id).toBeDefined();
      expect(node.grade).toBeGreaterThanOrEqual(3);
      expect(node.grade).toBeLessThanOrEqual(12);
      expect(node.title).toBeTruthy();
      expect(node.template).toBeDefined();
      expect(node.lesson_data).toBeDefined();
      expect(node.lesson_data.hook).toBeTruthy();
      expect(node.lesson_data.concept.summary).toBeTruthy();
      expect(node.lesson_data.concept.key_points.length).toBeGreaterThan(0);
      expect(node.lesson_data.game_config).toBeDefined();
      expect(node.lesson_data.quiz.length).toBeGreaterThan(0);

      // Verify quiz structure
      for (const q of node.lesson_data.quiz) {
        expect(q.question).toBeTruthy();
        expect(q.options.length).toBeGreaterThanOrEqual(2);
        expect(q.answer).toBeGreaterThanOrEqual(0);
        expect(q.answer).toBeLessThan(q.options.length);
        expect(q.explanation).toBeTruthy();
      }
    }
  });

  it('should ensure each node contains comprehensive theory and practice lab missions', () => {
    for (const node of curriculumData.nodes) {
      const lesson = node.lesson_data as any;
      expect(lesson.theory).toBeDefined();
      expect(lesson.theory.overview).toBeTruthy();
      expect(lesson.theory.sections.length).toBeGreaterThanOrEqual(2);
      for (const sec of lesson.theory.sections) {
        expect(sec.title).toBeTruthy();
        expect(sec.content).toBeTruthy();
      }
      expect(lesson.theory.memorize).toBeTruthy();

      expect(lesson.practice).toBeDefined();
      expect(lesson.practice.mission).toBeDefined();
      expect(lesson.practice.mission.title).toBeTruthy();
      expect(lesson.practice.mission.goal).toBeTruthy();
      expect(lesson.practice.mission.steps.length).toBeGreaterThanOrEqual(3);
      expect(lesson.practice.checklist.length).toBeGreaterThanOrEqual(2);
    }
  });

  it('should have valid textbook mappings for GDPT 2018 coverage', () => {
    for (const node of curriculumData.nodes) {
      if (node.textbook_mapping) {
        expect(node.textbook_mapping.kntt).toBeDefined();
        expect(node.textbook_mapping.canhdieu).toBeDefined();
        expect(node.textbook_mapping.ctst).toBeDefined();
      }
    }
  });
});
