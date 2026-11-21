import React from 'react';
import { useI18n } from '../i18nContext';
import { useTheme } from '../ThemeContext';
import { PixelLogo } from './PixelLogo';
import { PixelButton } from './PixelButton';
import { PixelMascot } from './PixelMascot';
import {
  PixelElementaryIcon,
  PixelMiddleSchoolIcon,
  PixelHighSchoolIcon,
  PixelMapIcon
} from './PixelIcons';
import { sound } from '../../packages/game-core/audio';
import {
  BookOpen,
  Gamepad2,
  RotateCcw,
  Smile,
  Globe2,
  ShieldCheck,
  Users,
  ArrowRight,
  School,
  CheckCircle2,
  Award
} from 'lucide-react';

interface AboutPageProps {
  onBackToCurriculum: () => void;
}

export const AboutPage: React.FC<AboutPageProps> = ({ onBackToCurriculum }) => {
  const { t } = useI18n();
  const { effectiveTheme } = useTheme();
  const isLight = effectiveTheme === 'light';

  const pillars = [
    {
      icon: BookOpen,
      iconColor: isLight ? 'text-[#047857]' : 'text-[#38b764]',
      badgeColor: isLight ? 'bg-[#dcfce7] text-[#166534]' : 'bg-[#193c3e] text-[#a7f070]',
      title: t('about_pillar_1_title'),
      desc: t('about_pillar_1_desc'),
      stat: '137 ' + t('lessons_suffix'),
    },
    {
      icon: Gamepad2,
      iconColor: isLight ? 'text-[#0284c7]' : 'text-[#2ce8f5]',
      badgeColor: isLight ? 'bg-[#e0f2fe] text-[#0369a1]' : 'bg-[#1f3b5c] text-[#2ce8f5]',
      title: t('about_pillar_2_title'),
      desc: t('about_pillar_2_desc'),
      stat: '8 Game Types',
    },
    {
      icon: RotateCcw,
      iconColor: isLight ? 'text-[#b45309]' : 'text-[#fee761]',
      badgeColor: isLight ? 'bg-[#fef9c3] text-[#854d0e]' : 'bg-[#3a3520] text-[#fee761]',
      title: t('about_pillar_3_title'),
      desc: t('about_pillar_3_desc'),
      stat: '5 Hộp Leitner',
    },
    {
      icon: Smile,
      iconColor: isLight ? 'text-[#9d174d]' : 'text-[#fca3ca]',
      badgeColor: isLight ? 'bg-[#fce7f3] text-[#9d174d]' : 'bg-[#5c2b4e] text-[#fca3ca]',
      title: t('about_pillar_4_title'),
      desc: t('about_pillar_4_desc'),
      stat: '4 Pixel Mascots',
    },
    {
      icon: Globe2,
      iconColor: isLight ? 'text-[#2563eb]' : 'text-[#70a5fd]',
      badgeColor: isLight ? 'bg-[#dbeafe] text-[#1e40af]' : 'bg-[#1e293b] text-[#93c5fd]',
      title: t('about_pillar_5_title'),
      desc: t('about_pillar_5_desc'),
      stat: 'VI · EN & Themes',
    },
    {
      icon: ShieldCheck,
      iconColor: isLight ? 'text-[#059669]' : 'text-[#38b764]',
      badgeColor: isLight ? 'bg-[#ecfdf5] text-[#047857]' : 'bg-[#132d22] text-[#38b764]',
      title: t('about_pillar_6_title'),
      desc: t('about_pillar_6_desc'),
      stat: '100% Offline',
    },
  ];

  const worlds = [
    {
      tier: 'elem',
      badge: 'Lớp 3 · 4 · 5',
      name: t('about_world_elem_title'),
      sub: t('about_world_elem_sub'),
      desc: t('about_world_elem_desc'),
      icon: <PixelElementaryIcon size={30} />,
      borderColor: isLight ? 'border-[#10b981]' : 'border-[#38b764]',
      bgHeader: isLight ? 'bg-[#ecfdf5] text-[#065f46]' : 'bg-[#1a3826] text-[#a7f070]',
      highlight: isLight ? 'text-[#047857]' : 'text-[#38b764]',
    },
    {
      tier: 'mid',
      badge: 'Lớp 6 · 7 · 8 · 9',
      name: t('about_world_mid_title'),
      sub: t('about_world_mid_sub'),
      desc: t('about_world_mid_desc'),
      icon: <PixelMiddleSchoolIcon size={30} />,
      borderColor: isLight ? 'border-[#3b82f6]' : 'border-[#2ce8f5]',
      bgHeader: isLight ? 'bg-[#eff6ff] text-[#1e40af]' : 'bg-[#1f3b5c] text-[#2ce8f5]',
      highlight: isLight ? 'text-[#1d4ed8]' : 'text-[#2ce8f5]',
    },
    {
      tier: 'high',
      badge: 'Lớp 10 · 11 · 12',
      name: t('about_world_high_title'),
      sub: t('about_world_high_sub'),
      desc: t('about_world_high_desc'),
      icon: <PixelHighSchoolIcon size={30} />,
      borderColor: isLight ? 'border-[#ec4899]' : 'border-[#feae34]',
      bgHeader: isLight ? 'bg-[#fdf2f8] text-[#9d174d]' : 'bg-[#3e2731] text-[#fee761]',
      highlight: isLight ? 'text-[#be185d]' : 'text-[#feae34]',
    },
  ];

  const stakeholders = [
    {
      title: t('about_target_student_title'),
      desc: t('about_target_student_desc'),
      mascot: 'tinbot' as const,
      role: 'Người học chủ động',
      color: isLight ? 'border-[#10b981] bg-white' : 'border-[#38b764] bg-[#1a1c2c]',
    },
    {
      title: t('about_target_teacher_title'),
      desc: t('about_target_teacher_desc'),
      mascot: 'owl' as const,
      role: 'Thầy Cô trợ giảng số',
      color: isLight ? 'border-[#3b82f6] bg-white' : 'border-[#2ce8f5] bg-[#1a1c2c]',
    },
    {
      title: t('about_target_parent_title'),
      desc: t('about_target_parent_desc'),
      mascot: 'fox' as const,
      role: 'Phụ huynh đồng hành',
      color: isLight ? 'border-[#f59e0b] bg-white' : 'border-[#feae34] bg-[#1a1c2c]',
    },
  ];

  return (
    <div className="w-full flex flex-col gap-8 pb-12 animate-fade-in">
      {/* 1. HERO SECTION */}
      <section className={`border-4 p-6 sm:p-8 lg:p-10 transition-colors shadow-pixel relative overflow-hidden ${
        isLight
          ? 'bg-white border-[#cbd5e1] text-[#0f172a]'
          : 'bg-[#1a1c2c] border-[#3a4466] text-white'
      }`}>
        {/* Background accent decor */}
        <div className="absolute -top-16 -right-16 w-64 h-64 bg-gradient-to-br from-[#fee761]/10 via-[#38b764]/10 to-transparent rounded-full pointer-events-none blur-2xl" />

        <div className="relative z-10 flex flex-col lg:flex-row items-center justify-between gap-6 lg:gap-10">
          <div className="flex-1 flex flex-col items-center lg:items-start text-center lg:text-left gap-4">
            {/* Tag chuẩn mực */}
            <div className="inline-flex items-center gap-2 px-3 py-1 text-xs font-bold font-mono tracking-wider border uppercase shadow-pixel-sm bg-[#10b981] text-white border-[#059669]">
              <Award size={15} className="text-[#fee761]" />
              <span>{t('about_hero_tag')}</span>
            </div>

            {/* Tiêu đề & Slogan */}
            <h1 className={`text-2xl sm:text-3xl lg:text-4xl font-black tracking-tight leading-tight ${
              isLight ? 'text-[#0f172a]' : 'text-white'
            }`}>
              {t('about_hero_title')}
            </h1>

            <p className={`text-sm sm:text-base max-w-2xl leading-relaxed ${
              isLight ? 'text-[#475569]' : 'text-[#c0cbdc]'
            }`}>
              {t('about_hero_subtitle')}
            </p>

            {/* Thông số nhanh */}
            <div className="flex flex-wrap items-center justify-center lg:justify-start gap-2.5 pt-2">
              <span className={`px-2.5 py-1 text-xs font-bold border ${
                isLight ? 'bg-[#f1f5f9] border-[#cbd5e1] text-[#334155]' : 'bg-[#181425] border-[#3a4466] text-[#a7f070]'
              }`}>
                📚 137 Bài học Chuẩn GDPT 2018
              </span>
              <span className={`px-2.5 py-1 text-xs font-bold border ${
                isLight ? 'bg-[#f1f5f9] border-[#cbd5e1] text-[#334155]' : 'bg-[#181425] border-[#3a4466] text-[#2ce8f5]'
              }`}>
                📖 Phủ trọn 3 bộ: KNTT · Cánh Diều · CTST
              </span>
              <span className={`px-2.5 py-1 text-xs font-bold border ${
                isLight ? 'bg-[#f1f5f9] border-[#cbd5e1] text-[#334155]' : 'bg-[#181425] border-[#3a4466] text-[#fee761]'
              }`}>
                ⚡ 100% Hoạt động Không cần Mạng
              </span>
            </div>

            {/* Nút Call To Action */}
            <div className="pt-3 flex flex-wrap items-center gap-3">
              <PixelButton
                variant="primary"
                size="md"
                onClick={() => {
                  sound.playClick();
                  onBackToCurriculum();
                }}
              >
                <span className="flex items-center gap-2">
                  <PixelMapIcon size={16} />
                  <span>{t('about_btn_explore')}</span>
                  <ArrowRight size={16} />
                </span>
              </PixelButton>

              <button
                onClick={() => {
                  sound.playClick();
                  onBackToCurriculum();
                }}
                className={`flex items-center gap-1.5 px-4 py-2 text-xs font-bold border-2 cursor-pointer transition-all shadow-pixel-sm ${
                  isLight
                    ? 'bg-[#f8fafc] hover:bg-[#e2e8f0] border-[#cbd5e1] text-[#334155]'
                    : 'bg-[#262b44] hover:bg-[#3a4466] border-[#5a6988] text-[#c0cbdc]'
                }`}
              >
                <span>{t('nav_back_to_curriculum')}</span>
              </button>
            </div>
          </div>

          {/* Logo & Mascot Showcase */}
          <div className="flex flex-col items-center gap-3 shrink-0">
            <div className={`p-5 sm:p-7 border-4 shadow-pixel-lg flex flex-col items-center gap-4 ${
              isLight ? 'bg-[#f8fafc] border-[#cbd5e1]' : 'bg-[#181425] border-[#5a6988]'
            }`}>
              <PixelLogo size="lg" />
              <div className="flex items-center justify-center gap-3 pt-2">
                <PixelMascot mascotId="tinbot" size={38} animated={true} />
                <PixelMascot mascotId="cat" size={38} animated={true} />
                <PixelMascot mascotId="owl" size={38} animated={true} />
                <PixelMascot mascotId="fox" size={38} animated={true} />
              </div>
              <div className={`text-[11px] font-mono text-center font-bold px-2 py-0.5 border ${
                isLight ? 'bg-white border-[#cbd5e1] text-[#64748b]' : 'bg-[#1a1c2c] border-[#3a4466] text-[#8b9bb4]'
              }`}>
                EasyTin v1.0.0 · Gold Master Release
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 2. SÁU TRỤ CỘT ĐỘT PHÁ */}
      <section className="flex flex-col gap-4">
        <div className="flex flex-col gap-1 text-center sm:text-left">
          <h2 className={`text-xl sm:text-2xl font-bold uppercase tracking-wide flex items-center justify-center sm:justify-start gap-2 ${
            isLight ? 'text-[#0f172a]' : 'text-white'
          }`}>
            <Award size={22} className={isLight ? 'text-[#d97706]' : 'text-[#fee761]'} />
            <span>{t('about_pillar_title')}</span>
          </h2>
          <p className={`text-xs sm:text-sm ${isLight ? 'text-[#64748b]' : 'text-[#8b9bb4]'}`}>
            {t('about_pillar_desc')}
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {pillars.map((p, idx) => {
            const Icon = p.icon;
            return (
              <div
                key={idx}
                className={`border-2 p-4 sm:p-5 flex flex-col justify-between gap-3 shadow-pixel-sm transition-all hover:-translate-y-0.5 ${
                  isLight
                    ? 'bg-white border-[#cbd5e1] hover:border-[#94a3b8]'
                    : 'bg-[#1a1c2c] border-[#3a4466] hover:border-[#5a6988]'
                }`}
              >
                <div className="flex items-start justify-between gap-2">
                  <div className={`p-2.5 border-2 ${isLight ? 'bg-[#f8fafc] border-[#e2e8f0]' : 'bg-[#181425] border-[#3a4466]'}`}>
                    <Icon size={22} className={p.iconColor} />
                  </div>
                  <span className={`text-[10px] font-bold font-mono px-2 py-0.5 border ${p.badgeColor}`}>
                    {p.stat}
                  </span>
                </div>

                <div>
                  <h3 className={`font-bold text-sm sm:text-base ${isLight ? 'text-[#0f172a]' : 'text-white'}`}>
                    {p.title}
                  </h3>
                  <p className={`text-xs mt-1.5 leading-relaxed ${isLight ? 'text-[#64748b]' : 'text-[#8b9bb4]'}`}>
                    {p.desc}
                  </p>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {/* 3. BA THẾ GIỚI HỌC TẬP KỲ THÚ (CẤP HỌC) */}
      <section className="flex flex-col gap-4">
        <div className="flex flex-col gap-1 text-center sm:text-left">
          <h2 className={`text-xl sm:text-2xl font-bold uppercase tracking-wide flex items-center justify-center sm:justify-start gap-2 ${
            isLight ? 'text-[#0f172a]' : 'text-white'
          }`}>
            <School size={22} className={isLight ? 'text-[#0284c7]' : 'text-[#2ce8f5]'} />
            <span>{t('about_worlds_title')}</span>
          </h2>
          <p className={`text-xs sm:text-sm ${isLight ? 'text-[#64748b]' : 'text-[#8b9bb4]'}`}>
            {t('about_worlds_desc')}
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {worlds.map((w, idx) => (
            <div
              key={idx}
              className={`border-4 shadow-pixel flex flex-col justify-between transition-all ${
                isLight ? 'bg-white' : 'bg-[#1a1c2c]'
              } ${w.borderColor}`}
            >
              {/* Header card thế giới */}
              <div className={`p-4 border-b-2 ${w.borderColor} ${w.bgHeader}`}>
                <div className="flex items-center justify-between">
                  <span className="text-2xl">{w.icon}</span>
                  <span className="text-[11px] font-mono font-bold px-2 py-0.5 bg-white/80 dark:bg-black/40 border border-current">
                    {w.badge}
                  </span>
                </div>
                <h3 className="font-bold text-base mt-2">{w.name}</h3>
                <div className="text-xs font-semibold opacity-90">{w.sub}</div>
              </div>

              {/* Nội dung card thế giới */}
              <div className="p-4 flex flex-col justify-between flex-1 gap-4">
                <p className={`text-xs leading-relaxed ${isLight ? 'text-[#475569]' : 'text-[#c0cbdc]'}`}>
                  {w.desc}
                </p>

                <div className="pt-2 border-t border-dashed border-gray-300 dark:border-gray-700 flex items-center justify-between text-[11px]">
                  <span className={`font-bold ${w.highlight}`}>GDPT 2018</span>
                  <span className={isLight ? 'text-[#64748b]' : 'text-[#8b9bb4]'}>Hoạt động 100%</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* 4. ĐỐI TƯỢNG ĐỒNG HÀNH */}
      <section className="flex flex-col gap-4">
        <div className="flex flex-col gap-1 text-center sm:text-left">
          <h2 className={`text-xl sm:text-2xl font-bold uppercase tracking-wide flex items-center justify-center sm:justify-start gap-2 ${
            isLight ? 'text-[#0f172a]' : 'text-white'
          }`}>
            <Users size={22} className={isLight ? 'text-[#047857]' : 'text-[#38b764]'} />
            <span>{t('about_target_title')}</span>
          </h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {stakeholders.map((s, idx) => (
            <div
              key={idx}
              className={`border-2 p-5 flex flex-col items-center text-center gap-3 shadow-pixel-sm ${s.color}`}
            >
              <div className="p-2 border-2 border-dashed border-gray-400">
                <PixelMascot mascotId={s.mascot} size={48} animated={true} />
              </div>
              <span className={`text-[11px] font-mono font-bold px-2 py-0.5 border ${
                isLight ? 'bg-[#f1f5f9] border-[#cbd5e1] text-[#334155]' : 'bg-[#181425] border-[#3a4466] text-[#fee761]'
              }`}>
                {s.role}
              </span>
              <h3 className={`font-bold text-base ${isLight ? 'text-[#0f172a]' : 'text-white'}`}>
                {s.title}
              </h3>
              <p className={`text-xs leading-relaxed ${isLight ? 'text-[#64748b]' : 'text-[#8b9bb4]'}`}>
                {s.desc}
              </p>
            </div>
          ))}
        </div>
      </section>

      {/* 5. FOOTER BANNER & CAM KẾT SƯ PHẠM */}
      <section className={`border-4 p-6 text-center flex flex-col items-center gap-4 shadow-pixel ${
        isLight ? 'bg-[#ecfdf5] border-[#10b981]' : 'bg-[#181425] border-[#38b764]'
      }`}>
        <div className="flex items-center justify-center gap-2 text-sm font-bold">
          <CheckCircle2 size={18} className={isLight ? 'text-[#047857]' : 'text-[#38b764]'} />
          <span className={isLight ? 'text-[#065f46]' : 'text-[#a7f070]'}>
            {t('about_footer_quote')}
          </span>
        </div>
        <p className={`text-xs max-w-xl leading-relaxed ${isLight ? 'text-[#064e3b]' : 'text-[#c0cbdc]'}`}>
          Bản quyền nội dung sư phạm thuộc Bộ Giáo dục và Đào tạo Việt Nam. EasyTin cam kết phi lợi nhuận cho mục đích học tập cá nhân và giảng dạy trong nhà trường.
        </p>

        <PixelButton
          variant="accent"
          size="md"
          onClick={() => {
            sound.playClick();
            onBackToCurriculum();
          }}
        >
          <span className="flex items-center gap-2">
            <PixelMapIcon size={16} />
            <span>{t('about_btn_explore')}</span>
            <ArrowRight size={16} />
          </span>
        </PixelButton>
      </section>
    </div>
  );
};
export default AboutPage;
