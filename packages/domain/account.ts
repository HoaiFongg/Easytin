import { AvatarOption, Grade, UserAccount, UserProgressState } from './types';
import { DEFAULT_PROGRESS } from './storage';

export const AVATAR_OPTIONS: AvatarOption[] = [
  {
    id: 'tin_bot',
    name: 'Tin Bot',
    role: 'Robot Bạn Nhỏ',
    icon: '🤖',
    badgeColor: '#38b764',
  },
  {
    id: 'cat_explorer',
    name: 'Miu Thám Hiểm',
    role: 'Nhà Khám Phá',
    icon: '🐱',
    badgeColor: '#feae34',
  },
  {
    id: 'wizard_algo',
    name: 'Pháp Sư Logic',
    role: 'Bậc Thầy Thuật Toán',
    icon: '🧙‍♂️',
    badgeColor: '#2ce8f5',
  },
  {
    id: 'astro_coder',
    name: 'Phi Hành Gia Coder',
    role: 'Du Hành Vũ Trụ',
    icon: '🚀',
    badgeColor: '#fca3ca',
  },
  {
    id: 'fox_clever',
    name: 'Cáo Thông Thái',
    role: 'Tư Duy Nhạy Bén',
    icon: '🦊',
    badgeColor: '#f77622',
  },
  {
    id: 'owl_scholar',
    name: 'Cú Trí Tuệ',
    role: 'Học Giả Uyên Bác',
    icon: '🦉',
    badgeColor: '#eb564b',
  },
];

const STORAGE_ACCOUNTS_KEY = 'easytin_accounts_v1';
const STORAGE_ACTIVE_USER_KEY = 'easytin_active_user_id_v1';

// Hỗ trợ in-memory fallback khi chạy trong môi trường kiểm thử Vitest hoặc Node.js
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

function removeStorageItem(key: string): void {
  try {
    if (typeof localStorage !== 'undefined') {
      localStorage.removeItem(key);
      return;
    }
  } catch {}
  memoryStorage.delete(key);
}

export function hashPassword(password: string): string {
  try {
    return 'et_h$' + btoa(encodeURIComponent('easytin_salt_v1_' + password.trim()));
  } catch {
    return 'et_h$' + password.trim();
  }
}

export function getRankTitle(xp: number, grade: Grade): string {
  const isElementary = grade <= 5;
  const isMiddle = grade >= 6 && grade <= 9;

  if (xp < 300) {
    return isElementary ? 'Mầm non Công nghệ' : 'Tập sự Khởi đầu';
  }
  if (xp < 1000) {
    return isElementary ? 'Nhà Thám hiểm Nhí' : 'Trinh sát Dữ liệu';
  }
  if (xp < 2500) {
    return isElementary ? 'Chiến sĩ Số hóa' : isMiddle ? 'Chiến binh Mã nguồn' : 'Kỹ sư Thuật toán';
  }
  if (xp < 5000) {
    return isElementary ? 'Thợ săn Lỗi Code' : isMiddle ? 'Chuyên gia Thuật toán' : 'Kiến trúc sư Hệ thống';
  }
  return isElementary ? 'Đại hiệp Tin học' : 'Đại sứ Tri thức Số';
}

export class AccountManager {
  /**
   * Xóa toàn bộ dữ liệu tài khoản (Dành cho kiểm thử)
   */
  static clearAll(): void {
    removeStorageItem(STORAGE_ACCOUNTS_KEY);
    removeStorageItem(STORAGE_ACTIVE_USER_KEY);
  }

  /**
   * Lấy danh sách tất cả tài khoản đã lưu trên máy
   */
  static getAccounts(): UserAccount[] {
    try {
      const data = getStorageItem(STORAGE_ACCOUNTS_KEY);
      if (!data) return [];
      const parsed = JSON.parse(data) as UserAccount[];
      return Array.isArray(parsed) ? parsed : [];
    } catch {
      return [];
    }
  }

  /**
   * Lưu danh sách tài khoản vào localStorage
   */
  static saveAccounts(accounts: UserAccount[]): void {
    try {
      setStorageItem(STORAGE_ACCOUNTS_KEY, JSON.stringify(accounts));
    } catch (e) {
      console.warn('Không thể lưu danh sách tài khoản', e);
    }
  }

  /**
   * Lấy ID tài khoản đang đăng nhập hiện tại
   */
  static getActiveAccountId(): string | null {
    try {
      return getStorageItem(STORAGE_ACTIVE_USER_KEY);
    } catch {
      return null;
    }
  }

  /**
   * Đặt ID tài khoản đang đăng nhập (hoặc null nếu đăng xuất / dùng chế độ khách)
   */
  static setActiveAccountId(id: string | null): void {
    try {
      if (id) {
        setStorageItem(STORAGE_ACTIVE_USER_KEY, id);
      } else {
        removeStorageItem(STORAGE_ACTIVE_USER_KEY);
      }
    } catch (e) {
      console.warn('Không thể cập nhật tài khoản đang hoạt động', e);
    }
  }

  /**
   * Lấy đối tượng tài khoản đang đăng nhập hiện tại
   */
  static getActiveAccount(): UserAccount | null {
    const activeId = this.getActiveAccountId();
    if (!activeId) return null;
    const accounts = this.getAccounts();
    return accounts.find((a) => a.id === activeId) || null;
  }

  /**
   * Tạo tài khoản học tập mới
   */
  static createAccount(params: {
    username: string;
    password: string;
    fullName: string;
    grade: Grade;
    schoolName?: string;
    className?: string;
    avatarId?: string;
  }): { success: boolean; account?: UserAccount; error?: string } {
    const username = params.username.trim();
    const fullName = params.fullName.trim();
    const password = params.password.trim();

    if (!fullName || fullName.length < 2) {
      return { success: false, error: 'Họ và tên người học phải có ít nhất 2 ký tự.' };
    }

    if (!username || username.length < 3) {
      return { success: false, error: 'Tên đăng nhập phải có ít nhất 3 ký tự.' };
    }

    const usernameRegex = /^[a-zA-Z0-9_.-]+$/;
    if (!usernameRegex.test(username)) {
      return {
        success: false,
        error: 'Tên đăng nhập chỉ chứa chữ cái tiếng Anh không dấu, số, dấu gạch dưới hoặc gạch ngang.',
      };
    }

    if (!password || password.length < 4) {
      return { success: false, error: 'Mật khẩu bảo vệ tài khoản phải có ít nhất 4 ký tự.' };
    }

    if (!params.grade || params.grade < 3 || params.grade > 12) {
      return { success: false, error: 'Vui lòng chọn khối lớp học hợp lệ từ Lớp 3 đến Lớp 12.' };
    }

    const accounts = this.getAccounts();
    const existing = accounts.find(
      (a) => a.username.toLowerCase() === username.toLowerCase()
    );

    if (existing) {
      return {
        success: false,
        error: `Tên đăng nhập "${username}" đã tồn tại trên máy này. Vui lòng chọn tên khác!`,
      };
    }

    const now = new Date().toISOString();
    const avatarId = params.avatarId || 'tin_bot';
    const avatarChoice = AVATAR_OPTIONS.find((a) => a.id === avatarId) || AVATAR_OPTIONS[0];

    const initialProgress: UserProgressState = {
      ...DEFAULT_PROGRESS,
      selectedGrade: params.grade,
      nickname: fullName,
      avatar: {
        base: avatarId,
        hat: 'explorer_cap',
        color: avatarChoice.badgeColor,
      },
    };

    const newAccount: UserAccount = {
      id: 'usr_' + Date.now() + '_' + Math.random().toString(36).substring(2, 7),
      username,
      passwordHash: hashPassword(password),
      fullName,
      grade: params.grade,
      schoolName: params.schoolName?.trim() || undefined,
      className: params.className?.trim() || undefined,
      avatarId,
      createdAt: now,
      lastLoginAt: now,
      progress: initialProgress,
    };

    accounts.push(newAccount);
    this.saveAccounts(accounts);
    this.setActiveAccountId(newAccount.id);

    return { success: true, account: newAccount };
  }

  /**
   * Đăng nhập vào tài khoản
   */
  static login(
    username: string,
    password: string
  ): { success: boolean; account?: UserAccount; error?: string } {
    const cleanUsername = username.trim().toLowerCase();
    const cleanPassword = password.trim();

    if (!cleanUsername || !cleanPassword) {
      return { success: false, error: 'Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu.' };
    }

    const accounts = this.getAccounts();
    const account = accounts.find((a) => a.username.toLowerCase() === cleanUsername);

    if (!account) {
      return {
        success: false,
        error: `Không tìm thấy tài khoản "${username}". Bạn có thể tạo tài khoản mới nếu chưa có!`,
      };
    }

    const targetHash = hashPassword(cleanPassword);
    if (account.passwordHash !== targetHash) {
      return { success: false, error: 'Mật khẩu không chính xác. Vui lòng thử lại!' };
    }

    account.lastLoginAt = new Date().toISOString();
    this.saveAccounts(accounts);
    this.setActiveAccountId(account.id);

    return { success: true, account };
  }

  /**
   * Đăng xuất chuyển về chế độ khách
   */
  static logout(): void {
    this.setActiveAccountId(null);
  }

  /**
   * Cập nhật tiến độ của tài khoản người học hiện tại
   */
  static updateAccountProgress(accountId: string, progress: UserProgressState): void {
    const accounts = this.getAccounts();
    const idx = accounts.findIndex((a) => a.id === accountId);
    if (idx !== -1) {
      accounts[idx].progress = progress;
      accounts[idx].grade = progress.selectedGrade;
      this.saveAccounts(accounts);
    }
  }

  /**
   * Chỉnh sửa thông tin hồ sơ tài khoản
   */
  static updateProfile(
    accountId: string,
    updates: {
      fullName?: string;
      grade?: Grade;
      schoolName?: string;
      className?: string;
      avatarId?: string;
      newPassword?: string;
    }
  ): { success: boolean; account?: UserAccount; error?: string } {
    const accounts = this.getAccounts();
    const account = accounts.find((a) => a.id === accountId);
    if (!account) {
      return { success: false, error: 'Không tìm thấy tài khoản cần chỉnh sửa.' };
    }

    if (updates.fullName !== undefined) {
      const cleanName = updates.fullName.trim();
      if (cleanName.length < 2) {
        return { success: false, error: 'Họ và tên phải có ít nhất 2 ký tự.' };
      }
      account.fullName = cleanName;
      account.progress.nickname = cleanName;
    }

    if (updates.grade !== undefined) {
      account.grade = updates.grade;
      account.progress.selectedGrade = updates.grade;
    }

    if (updates.schoolName !== undefined) {
      account.schoolName = updates.schoolName.trim() || undefined;
    }

    if (updates.className !== undefined) {
      account.className = updates.className.trim() || undefined;
    }

    if (updates.avatarId !== undefined) {
      account.avatarId = updates.avatarId;
      const avatarChoice = AVATAR_OPTIONS.find((a) => a.id === updates.avatarId);
      if (avatarChoice) {
        account.progress.avatar.base = updates.avatarId;
        account.progress.avatar.color = avatarChoice.badgeColor;
      }
    }

    if (updates.newPassword) {
      const cleanPass = updates.newPassword.trim();
      if (cleanPass.length < 4) {
        return { success: false, error: 'Mật khẩu mới phải có ít nhất 4 ký tự.' };
      }
      account.passwordHash = hashPassword(cleanPass);
    }

    this.saveAccounts(accounts);
    return { success: true, account };
  }

  /**
   * Xóa một tài khoản khỏi máy
   */
  static deleteAccount(accountId: string): void {
    const accounts = this.getAccounts().filter((a) => a.id !== accountId);
    this.saveAccounts(accounts);
    if (this.getActiveAccountId() === accountId) {
      this.setActiveAccountId(null);
    }
  }
}
