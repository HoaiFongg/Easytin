import { describe, it, expect, beforeEach } from 'vitest';
import { AccountManager, getRankTitle, hashPassword } from './account';

describe('AccountManager Unit Tests', () => {
  beforeEach(() => {
    AccountManager.clearAll();
  });

  it('bắt đầu với danh sách tài khoản trống và không có tài khoản active', () => {
    expect(AccountManager.getAccounts()).toEqual([]);
    expect(AccountManager.getActiveAccountId()).toBeNull();
    expect(AccountManager.getActiveAccount()).toBeNull();
  });

  it('tạo tài khoản học tập thành công và tự động đặt làm active', () => {
    const res = AccountManager.createAccount({
      username: 'baoan2015',
      password: 'mypassword123',
      fullName: 'Trần Bảo An',
      grade: 4,
      schoolName: 'Tiểu học Chu Văn An',
      className: 'Lớp 4B',
      avatarId: 'cat_explorer',
    });

    expect(res.success).toBe(true);
    expect(res.account).toBeDefined();
    expect(res.account?.username).toBe('baoan2015');
    expect(res.account?.fullName).toBe('Trần Bảo An');
    expect(res.account?.grade).toBe(4);
    expect(res.account?.avatarId).toBe('cat_explorer');
    expect(res.account?.passwordHash).toBe(hashPassword('mypassword123'));
    expect(res.account?.progress.selectedGrade).toBe(4);
    expect(res.account?.progress.nickname).toBe('Trần Bảo An');

    // Kiểm tra active account
    const active = AccountManager.getActiveAccount();
    expect(active?.id).toBe(res.account?.id);
    expect(AccountManager.getAccounts().length).toBe(1);
  });

  it('từ chối tạo tài khoản với tên đăng nhập trùng lặp không phân biệt hoa thường', () => {
    AccountManager.createAccount({
      username: 'nam_tin học',
      password: '123',
      fullName: 'Nam',
      grade: 3,
    }); // Sẽ fail vì username có dấu/khoảng trắng hoặc password < 4

    const first = AccountManager.createAccount({
      username: 'hocsinh_a',
      password: 'pass1234',
      fullName: 'Học sinh A',
      grade: 5,
    });
    expect(first.success).toBe(true);

    const duplicate = AccountManager.createAccount({
      username: 'HocSinh_A',
      password: 'pass5678',
      fullName: 'Học sinh B',
      grade: 6,
    });
    expect(duplicate.success).toBe(false);
    expect(duplicate.error).toContain('đã tồn tại');
  });

  it('kiểm tra tính hợp lệ của mật khẩu và tên đăng nhập', () => {
    const shortUser = AccountManager.createAccount({
      username: 'ab',
      password: 'password123',
      fullName: 'Nguyen A',
      grade: 3,
    });
    expect(shortUser.success).toBe(false);

    const shortPass = AccountManager.createAccount({
      username: 'nguyena',
      password: '123',
      fullName: 'Nguyen A',
      grade: 3,
    });
    expect(shortPass.success).toBe(false);
  });

  it('đăng nhập thành công với đúng mật khẩu và thất bại khi sai mật khẩu', () => {
    AccountManager.createAccount({
      username: 'minhtri_thcs',
      password: 'correct_pass',
      fullName: 'Lê Minh Trí',
      grade: 7,
    });

    AccountManager.logout();
    expect(AccountManager.getActiveAccount()).toBeNull();

    // Sai mật khẩu
    const failLogin = AccountManager.login('minhtri_thcs', 'wrong_pass');
    expect(failLogin.success).toBe(false);
    expect(AccountManager.getActiveAccount()).toBeNull();

    // Đúng mật khẩu
    const successLogin = AccountManager.login('minhtri_thcs', 'correct_pass');
    expect(successLogin.success).toBe(true);
    expect(AccountManager.getActiveAccount()?.fullName).toBe('Lê Minh Trí');
  });

  it('cô lập dữ liệu tiến độ giữa 2 tài khoản độc lập', () => {
    const user1 = AccountManager.createAccount({
      username: 'user_one',
      password: 'pass1234',
      fullName: 'Người Dùng Một',
      grade: 3,
    }).account!;

    // Cập nhật XP cho user 1
    const p1 = { ...user1.progress, xp: 500 };
    AccountManager.updateAccountProgress(user1.id, p1);

    // Tạo user 2
    const user2 = AccountManager.createAccount({
      username: 'user_two',
      password: 'pass1234',
      fullName: 'Người Dùng Hai',
      grade: 8,
    }).account!;

    // Kiểm tra tiến độ user 2 khởi đầu là 0
    expect(user2.progress.xp).toBe(0);
    expect(user2.grade).toBe(8);

    // Đăng nhập lại user 1 và kiểm tra XP vẫn là 500
    AccountManager.login('user_one', 'pass1234');
    const reloadedUser1 = AccountManager.getActiveAccount()!;
    expect(reloadedUser1.progress.xp).toBe(500);
    expect(reloadedUser1.grade).toBe(3);
  });

  it('chỉnh sửa hồ sơ và danh hiệu sư phạm theo XP', () => {
    const user = AccountManager.createAccount({
      username: 'profile_test',
      password: 'pass1234',
      fullName: 'Tên Ban Đầu',
      grade: 4,
    }).account!;

    const updated = AccountManager.updateProfile(user.id, {
      fullName: 'Tên Mới Đổi',
      grade: 5,
      avatarId: 'wizard_algo',
    });

    expect(updated.success).toBe(true);
    expect(updated.account?.fullName).toBe('Tên Mới Đổi');
    expect(updated.account?.grade).toBe(5);
    expect(updated.account?.avatarId).toBe('wizard_algo');

    // Kiểm tra danh hiệu phù hợp sư phạm
    expect(getRankTitle(50, 4)).toBe('Mầm non Công nghệ');
    expect(getRankTitle(500, 4)).toBe('Nhà Thám hiểm Nhí');
    expect(getRankTitle(1200, 7)).toBe('Chiến binh Mã nguồn');
    expect(getRankTitle(8000, 10)).toBe('Đại sứ Tri thức Số');
  });
});
