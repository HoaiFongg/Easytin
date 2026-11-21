export type Language = 'vi' | 'en';

const STORAGE_LANG_KEY = 'easytin_language_v1';
const memoryStorage = new Map<string, string>();

function getStorageItem(key: string): string | null {
  try {
    if (typeof localStorage !== 'undefined') {
      return localStorage.getItem(key);
    }
  } catch {}
  return memoryStorage.get(key) || null;
}

function setStorageItem(key: string, value: string): void {
  try {
    if (typeof localStorage !== 'undefined') {
      localStorage.setItem(key, value);
      return;
    }
  } catch {}
  memoryStorage.set(key, value);
}

export function getStoredLanguage(): Language {
  const saved = getStorageItem(STORAGE_LANG_KEY);
  if (saved === 'vi' || saved === 'en') {
    return saved;
  }
  return 'vi'; // Mặc định Tiếng Việt
}

export function setStoredLanguage(lang: Language): void {
  setStorageItem(STORAGE_LANG_KEY, lang);
}

export const TRANSLATIONS = {
  vi: {
    // Header & Brand
    app_title: 'EasyTin',
    app_subtitle: 'Tin học GDPT 2018 · Lớp 3–12',
    level_elementary: 'Tiểu học',
    level_middle: 'THCS',
    level_high: 'THPT',
    level_elementary_full: 'Cấp Tiểu học',
    level_middle_full: 'Cấp THCS',
    level_high_full: 'Cấp THPT',
    grade_prefix: 'Lớp',
    review_button: 'Ôn tập',
    review_box_title: 'Hộp ôn tập thông minh (Leitner)',
    xp_label: 'XP',
    streak_days: 'ngày',
    teacher_portal: 'Giáo viên',
    teacher_portal_title: 'Cổng dành cho Giáo viên',
    backup_code: 'Sao lưu',
    backup_code_title: 'Mã thẻ tiến độ',
    sound_enable: 'Bật âm thanh',
    sound_disable: 'Tắt âm thanh',
    account_button: 'Tạo tài khoản / Đăng nhập',
    account_button_short: 'Tài khoản',
    settings_button: 'Cài đặt',
    settings_title: 'Cài đặt trang web',

    // World Map
    world_valley: 'Thung lũng Số hóa',
    world_forest: 'Rừng Mạng & Dữ liệu',
    world_city: 'Thành phố Thuật toán',
    world_description: 'Khám phá thế giới kiến thức Tin học tương tác',
    curriculum_title: 'Chương trình Tin học — Lớp',
    lessons_count: 'bài học',
    lessons_suffix: 'bài',
    filter_all: 'Tất cả SGK',
    filter_kntt: 'Kết nối tri thức',
    filter_canhdieu: 'Cánh Diều',
    filter_ctst: 'Chân trời sáng tạo',
    status_not_started: 'Chưa học',
    status_in_progress: 'Đang học',
    status_mastered: 'Đã hoàn thành',
    status_due_review: 'Cần ôn lại',
    select_lesson: 'Nhấp vào bài để bắt đầu học',
    estimated_time: 'phút',

    // Lesson Modal
    tab_theory: '1. Lí thuyết trọng tâm',
    tab_game: '2. Trò chơi tương tác',
    tab_practice: '3. Thực hành trải nghiệm',
    tab_quiz: '4. Câu hỏi củng cố',
    lesson_goals: 'Mục tiêu bài học',
    lesson_key_points: 'Khái niệm cốt lõi',
    lesson_memorize: 'Ghi nhớ trọng tâm',
    lesson_overview: 'Tóm tắt bài học',
    lesson_practice_steps: 'Các bước thực hành:',
    lesson_practice_challenge: 'Thử thách mở rộng:',
    lesson_practice_checklist: 'Bảng kiểm tự đánh giá:',
    lesson_recap: 'Củng cố kiến thức',
    btn_start_game: 'BẮT ĐẦU TRÒ CHƠI',
    btn_finish_lesson: 'HOÀN THÀNH BÀI HỌC',
    btn_back_to_map: 'Quay lại bản đồ',
    btn_previous: 'Quay lại',
    btn_next: 'Tiếp tục',
    score_label: 'Điểm số đạt được:',

    // Settings Modal
    settings_heading: 'CÀI ĐẶT TRANG WEB',
    settings_nav_language: '1. Ngôn ngữ (Language)',
    settings_nav_sound: '2. Âm thanh & Hiệu ứng',
    settings_nav_backup: '3. Sao lưu & Thẻ tiến độ',
    settings_nav_teacher: '4. Cổng Dành cho Thầy Cô',
    settings_nav_accessibility: '5. Hiển thị & Trợ năng',
    settings_nav_about: '6. Giới thiệu & Bản quyền',
    settings_backup_title: 'MÃ THẺ TIẾN ĐỘ HỌC TẬP (SAO LƯU & PHỤC HỒI)',
    settings_backup_desc: 'Sao chép mã thẻ này để đem sang máy tính khác ở phòng thực hành hoặc khôi phục khi cần:',
    settings_backup_copy_btn: 'Sao chép mã thẻ',
    settings_backup_copied: 'Đã sao chép!',
    settings_backup_import_label: 'Khôi phục tiến độ từ mã thẻ sao lưu:',
    settings_backup_import_btn: 'Khôi phục tiến độ',
    settings_backup_import_placeholder: 'Dán mã thẻ sao lưu vào đây...',
    settings_backup_invalid: 'Mã thẻ sao lưu không hợp lệ. Vui lòng kiểm tra lại!',
    settings_backup_success: 'Khôi phục tiến độ học tập thành công!',
    settings_teacher_title: 'CỔNG QUẢN LÝ DÀNH CHO THẦY CÔ',
    settings_teacher_code_title: 'Mã phòng học Tin học:',
    settings_teacher_code_desc: 'Học sinh chỉ cần nhập mã này + Biệt danh để vào lớp, không cần email phức tạp.',
    settings_teacher_change_code: 'Đổi mã mới',
    settings_teacher_heatmap_title: 'CẢNH BÁO LỖ HỔNG KIẾN THỨC CỦA LỚP:',
    settings_motion_label: 'Hoạt ảnh Linh vật Pixel:',
    settings_motion_desc: 'Bật hoặc giảm bớt chuyển động của các linh vật trên màn hình để tiết kiệm pin.',
    settings_motion_on: 'Đang bật hoạt ảnh đầy đủ',
    settings_motion_off: 'Giảm chuyển động tĩnh',
    settings_language_label: 'Ngôn ngữ hiển thị (Display Language):',
    settings_language_desc: 'Chuyển đổi toàn bộ ngôn ngữ trên giao diện giữa Tiếng Việt và Tiếng Anh.',
    lang_vietnamese: 'Tiếng Việt (Vietnamese)',
    lang_english: 'English (Tiếng Anh)',
    settings_theme_label: 'Chế độ hiển thị Giao diện:',
    settings_theme_desc: 'Tùy chỉnh giao diện Sáng / Tối phù hợp với phòng học ban ngày hoặc môi trường ít ánh sáng.',
    theme_dark: 'Giao diện Tối (Ban đêm · Retro Arcade)',
    theme_light: 'Giao diện Sáng (Ban ngày · Dễ đọc)',
    theme_system: 'Tự động theo thiết bị',
    theme_toggle_title: 'Chuyển đổi Giao diện Sáng / Tối',
    settings_sound_label: 'Âm thanh trò chơi (Sound Effects):',
    settings_sound_desc: 'Bật hoặc tắt âm thanh 8-bit chiptune cổ điển khi học tập.',
    settings_sound_on: 'Đang bật âm thanh',
    settings_sound_off: 'Đang tắt âm thanh',
    settings_font_label: 'Cỡ chữ hiển thị:',
    font_standard: 'Tiêu chuẩn',
    font_large: 'Chữ lớn (dễ đọc)',
    settings_about_label: 'Thông tin hệ thống EasyTin:',
    settings_about_desc: 'Nền tảng học Tin học tương tác chuẩn GDPT 2018 cho học sinh Việt Nam. Sẵn sàng 100% Offline.',
    btn_save_settings: 'LƯU & ĐÓNG CÀI ĐẶT',
    settings_saved_msg: 'Đã lưu cài đặt thành công!',

    // Auth & Profile
    auth_register_title: 'TẠO TÀI KHOẢN HỌC TẬP MỚI',
    auth_login_title: 'ĐĂNG NHẬP VÀO EASYTIN',
    auth_accounts_title: 'DANH SÁCH TÀI KHOẢN TRÊN MÁY NÀY',
    auth_tab_register: 'Tạo tài khoản',
    auth_tab_login: 'Đăng nhập',
    auth_tab_accounts: 'Đổi tài khoản',
    auth_fullname: 'Họ và tên người học:',
    auth_username: 'Tên đăng nhập (không dấu):',
    auth_password: 'Mật khẩu (>= 4 ký tự):',
    auth_confirm_password: 'Xác nhận lại mật khẩu:',
    auth_select_avatar: '1. Chọn Linh vật đại diện của bạn:',
    auth_select_grade: '2. Chọn Cấp học & Khối lớp của bạn:',
    auth_school: 'Trường học (không bắt buộc):',
    auth_class: 'Tên lớp (không bắt buộc):',
    auth_submit_register: 'TẠO TÀI KHOẢN VÀ BẮT ĐẦU HỌC',
    auth_submit_login: 'ĐĂNG NHẬP VÀO HỌC',
    auth_guest_link: 'Tiếp tục học ở chế độ Khách >',
    auth_no_account: 'Chưa có tài khoản?',
    auth_register_now: 'Bấm vào đây để tạo tài khoản mới!',

    // Profile
    profile_title: 'HỒ SƠ HỌC SINH',
    profile_rank: 'Danh hiệu:',
    profile_stats_title: 'THÀNH TÍCH HỌC TẬP TÍCH LŨY:',
    profile_xp: 'Điểm XP',
    profile_streak: 'Chuỗi ngày',
    profile_completed: 'Bài hoàn thành',
    profile_three_stars: 'Bài đạt 3 sao',
    profile_btn_edit: 'Chỉnh sửa hồ sơ',
    profile_btn_change_pass: 'Đổi mật khẩu',
    profile_btn_switch: 'Đổi tài khoản',
    profile_btn_logout: 'Đăng xuất',

    // Footer
    footer_copyright: 'EasyTin © 2026 — Nền tảng học Tin học dạng game Pixel cho học sinh Việt Nam.',
    footer_standard: 'Đồng bộ chuẩn GDPT 2018 · KNTT · Cánh Diều · Chân trời sáng tạo · 100% Offline PWA Ready',
  },
  en: {
    // Header & Brand
    app_title: 'EasyTin',
    app_subtitle: 'Informatics 2018 Curriculum · Grades 3–12',
    level_elementary: 'Elementary',
    level_middle: 'Middle School',
    level_high: 'High School',
    level_elementary_full: 'Elementary School',
    level_middle_full: 'Middle School',
    level_high_full: 'High School',
    grade_prefix: 'Grade',
    review_button: 'Review',
    review_box_title: 'Smart Leitner Review Box',
    xp_label: 'XP',
    streak_days: 'days',
    teacher_portal: 'Teachers',
    teacher_portal_title: 'Teacher Management Dashboard',
    backup_code: 'Backup',
    backup_code_title: 'Progress Backup Code',
    sound_enable: 'Enable Sound',
    sound_disable: 'Disable Sound',
    account_button: 'Sign Up / Log In',
    account_button_short: 'Account',
    settings_button: 'Settings',
    settings_title: 'Website Settings',

    // World Map
    world_valley: 'Digital Valley',
    world_forest: 'Network & Data Forest',
    world_city: 'Algorithm City',
    world_description: 'Explore interactive Informatics worlds',
    curriculum_title: 'Informatics Curriculum — Grade',
    lessons_count: 'lessons',
    lessons_suffix: 'lessons',
    filter_all: 'All Textbooks',
    filter_kntt: 'Knowledge Connection',
    filter_canhdieu: 'Kite Book',
    filter_ctst: 'Creative Horizons',
    status_not_started: 'Not Started',
    status_in_progress: 'In Progress',
    status_mastered: 'Mastered',
    status_due_review: 'Due for Review',
    select_lesson: 'Click any lesson to start learning',
    estimated_time: 'mins',

    // Lesson Modal
    tab_theory: '1. Core Theory',
    tab_game: '2. Interactive Game',
    tab_practice: '3. Hands-on Practice',
    tab_quiz: '4. Knowledge Quiz',
    lesson_goals: 'Learning Goals',
    lesson_key_points: 'Key Concepts',
    lesson_memorize: 'Key Takeaways',
    lesson_overview: 'Lesson Summary',
    lesson_practice_steps: 'Practice Steps:',
    lesson_practice_challenge: 'Extension Challenge:',
    lesson_practice_checklist: 'Self-check Rubric:',
    lesson_recap: 'Knowledge Recap',
    btn_start_game: 'START INTERACTIVE GAME',
    btn_finish_lesson: 'COMPLETE LESSON',
    btn_back_to_map: 'Back to World Map',
    btn_previous: 'Previous',
    btn_next: 'Next',
    score_label: 'Achieved Score:',

    // Settings Modal
    settings_heading: 'WEBSITE SETTINGS',
    settings_nav_language: '1. Language (Ngôn ngữ)',
    settings_nav_sound: '2. Audio & Sound Effects',
    settings_nav_backup: '3. Progress Backup & Sync',
    settings_nav_teacher: '4. Teacher Dashboard',
    settings_nav_accessibility: '5. Display & Motion',
    settings_nav_about: '6. About & System Info',
    settings_backup_title: 'STUDENT PROGRESS CODE (BACKUP & RESTORE)',
    settings_backup_desc: 'Copy this code to transfer your progress to another computer in the lab or restore when needed:',
    settings_backup_copy_btn: 'Copy Progress Code',
    settings_backup_copied: 'Copied!',
    settings_backup_import_label: 'Restore progress from a backup card:',
    settings_backup_import_btn: 'Restore Progress',
    settings_backup_import_placeholder: 'Paste your backup code here...',
    settings_backup_invalid: 'Invalid progress card code. Please verify again!',
    settings_backup_success: 'Progress restored successfully!',
    settings_teacher_title: 'TEACHER MANAGEMENT DASHBOARD',
    settings_teacher_code_title: 'Classroom Code:',
    settings_teacher_code_desc: 'Students only need this code + Nickname to join the lab session without email.',
    settings_teacher_change_code: 'Generate New Code',
    settings_teacher_heatmap_title: 'CLASS MISCONCEPTION & KNOWLEDGE GAPS:',
    settings_motion_label: 'Pixel Mascot Animation:',
    settings_motion_desc: 'Enable or reduce character motion on screen to save battery or improve performance.',
    settings_motion_on: 'Full Motion Animations ON',
    settings_motion_off: 'Reduced Motion (Static)',
    settings_language_label: 'Display Language (Ngôn ngữ):',
    settings_language_desc: 'Switch the entire user interface between Vietnamese and English.',
    lang_vietnamese: 'Tiếng Việt (Vietnamese)',
    lang_english: 'English (Tiếng Anh)',
    settings_theme_label: 'Appearance & Color Theme:',
    settings_theme_desc: 'Switch between Light and Dark mode to suit bright classrooms or low-light environments.',
    theme_dark: 'Dark Theme (Night · Retro Arcade)',
    theme_light: 'Light Theme (Day · High Contrast)',
    theme_system: 'Follow System Default',
    theme_toggle_title: 'Toggle Light / Dark Mode',
    settings_sound_label: 'Game Audio & Sound Effects:',
    settings_sound_desc: 'Toggle 8-bit chiptune sound effects during lessons and games.',
    settings_sound_on: 'Sound is ON',
    settings_sound_off: 'Sound is OFF',
    settings_font_label: 'Font Size:',
    font_standard: 'Standard',
    font_large: 'Large text (easy reading)',
    settings_about_label: 'About EasyTin Platform:',
    settings_about_desc: 'Interactive Informatics learning platform for Vietnamese students. 100% Offline PWA ready.',
    btn_save_settings: 'SAVE & CLOSE SETTINGS',
    settings_saved_msg: 'Settings saved successfully!',

    // Auth & Profile
    auth_register_title: 'CREATE NEW LEARNER ACCOUNT',
    auth_login_title: 'LOG IN TO EASYTIN',
    auth_accounts_title: 'SAVED ACCOUNTS ON THIS DEVICE',
    auth_tab_register: 'Sign Up',
    auth_tab_login: 'Log In',
    auth_tab_accounts: 'Switch Account',
    auth_fullname: 'Learner Full Name:',
    auth_username: 'Username (no spaces/accents):',
    auth_password: 'Password (>= 4 chars):',
    auth_confirm_password: 'Confirm Password:',
    auth_select_avatar: '1. Choose your Pixel Mascot:',
    auth_select_grade: '2. Select School Level & Grade:',
    auth_school: 'School Name (optional):',
    auth_class: 'Class Name (optional):',
    auth_submit_register: 'CREATE ACCOUNT & START LEARNING',
    auth_submit_login: 'LOG IN TO LEARN',
    auth_guest_link: 'Continue learning as Guest >',
    auth_no_account: 'No account yet?',
    auth_register_now: 'Click here to create a new account!',

    // Profile
    profile_title: 'STUDENT PROFILE',
    profile_rank: 'Title:',
    profile_stats_title: 'CUMULATIVE LEARNING ACHIEVEMENTS:',
    profile_xp: 'XP Points',
    profile_streak: 'Day Streak',
    profile_completed: 'Completed',
    profile_three_stars: '3-Star Lessons',
    profile_btn_edit: 'Edit Profile',
    profile_btn_change_pass: 'Change Password',
    profile_btn_switch: 'Switch Account',
    profile_btn_logout: 'Log Out',

    // Footer
    footer_copyright: 'EasyTin © 2026 — Pixel Game-based Informatics Platform for Vietnamese Students.',
    footer_standard: 'GDPT 2018 Standard · Knowledge Connection · Kite · Creative Horizons · 100% Offline PWA Ready',
  },
};

export type TranslationKey = keyof typeof TRANSLATIONS['vi'];

export function t(key: TranslationKey, lang: Language = 'vi'): string {
  const dict = TRANSLATIONS[lang] || TRANSLATIONS.vi;
  return dict[key] || TRANSLATIONS.vi[key] || key;
}
