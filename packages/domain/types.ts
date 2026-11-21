export type Grade = 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12;

export interface CurriculumWorld {
  id: string;
  name: string;
  grades: number[];
  description: string;
  color_theme: string;
}

export type GameTemplateType =
  | 'sort-drag'
  | 'block-maze'
  | 'logic-puzzle'
  | 'type-run'
  | 'match-memory'
  | 'branch-story'
  | 'bug-hunt'
  | 'boss-quiz';

export interface QuizQuestion {
  question: string;
  options: string[];
  answer: number;
  explanation: string;
}

export interface TheorySection {
  title: string;
  content: string;
  example?: string;
  tip?: string;
}

export interface PracticeMission {
  title: string;
  goal: string;
  steps: string[];
  challenge?: string;
  tip?: string;
}

export interface LessonData {
  hook: string;
  concept: {
    summary: string;
    key_points: string[];
  };
  theory?: {
    overview: string;
    sections: TheorySection[];
    memorize?: string;
  };
  practice?: {
    mission: PracticeMission;
    checklist?: string[];
  };
  game_config: Record<string, unknown>;
  quiz: QuizQuestion[];
  recap: string;
}

export interface CurriculumNode {
  id: string;
  world_id: string;
  grade: number;
  title: string;
  standard_domain: string;
  textbook_mapping?: {
    kntt?: string;
    canhdieu?: string;
    ctst?: string;
  };
  template: GameTemplateType;
  prerequisites: string[];
  estimated_minutes: number;
  learning_goals: string[];
  lesson_data: LessonData;
}

export interface NodeMasteryRecord {
  nodeId: string;
  box: 1 | 2 | 3 | 4; // Leitner boxes: 1 (1 day), 2 (3 days), 3 (7 days), 4 (21 days)
  consecutiveSuccess: number;
  stars: number; // 0 to 3
  bestScore: number; // 0 to 1
  lastReviewedAt: number; // timestamp
  nextDueAt: number; // timestamp
  attemptsCount: number;
  isCompleted: boolean;
}

export interface UserProgressState {
  version: string;
  selectedGrade: Grade;
  xp: number;
  streakDays: number;
  lastActiveDate: string; // YYYY-MM-DD
  avatar: {
    base: string;
    hat: string;
    color: string;
  };
  mastery: Record<string, NodeMasteryRecord>;
  unlockedBadges: string[];
  classCode?: string;
  nickname?: string;
}

export interface UserAccount {
  id: string;
  username: string; // Tên đăng nhập
  passwordHash: string; // Chuỗi mã hóa mật khẩu an toàn trên client
  fullName: string; // Họ và tên học sinh
  grade: Grade; // Khối lớp học
  schoolName?: string; // Tên trường (tùy chọn)
  className?: string; // Tên lớp (tùy chọn)
  avatarId: string; // Mã nhận diện avatar
  createdAt: string; // Thời gian khởi tạo (ISO)
  lastLoginAt: string; // Thời gian đăng nhập gần nhất (ISO)
  progress: UserProgressState; // Dữ liệu tiến độ học tập gắn liền với tài khoản
}

export interface AvatarOption {
  id: string;
  name: string;
  role: string;
  icon: string;
  badgeColor: string;
}
