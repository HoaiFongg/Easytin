import React from 'react';
import clsx from 'clsx';
import { sound } from '../../packages/game-core/audio';

interface PixelButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'accent' | 'danger' | 'ghost' | 'blue';
  size?: 'sm' | 'md' | 'lg';
  children: React.ReactNode;
}

export const PixelButton: React.FC<PixelButtonProps> = ({
  variant = 'primary',
  size = 'md',
  className,
  children,
  onClick,
  ...props
}) => {
  const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    sound.playClick();
    if (onClick) onClick(e);
  };

  const variantStyles = {
    primary: 'bg-[#38b764] hover:bg-[#63c74d] text-[#181425] font-bold',
    accent: 'bg-[#feae34] hover:bg-[#fee761] text-[#181425] font-bold',
    danger: 'bg-[#e43b44] hover:bg-[#f77622] text-white font-bold',
    blue: 'bg-[#0099db] hover:bg-[#2ce8f5] text-white font-bold',
    ghost: 'bg-[#262b44] hover:bg-[#3a4466] text-[#c0cbdc] border border-[#5a6988]',
  }[variant];

  const sizeStyles = {
    sm: 'px-2.5 py-1 text-xs',
    md: 'px-4 py-2 text-sm',
    lg: 'px-6 py-3 text-base font-extrabold',
  }[size];

  return (
    <button
      onClick={handleClick}
      className={clsx(
        'pixel-btn inline-flex items-center justify-center gap-2 rounded-none tracking-wide cursor-pointer transition-all disabled:opacity-50 disabled:cursor-not-allowed',
        variantStyles,
        sizeStyles,
        className
      )}
      {...props}
    >
      {children}
    </button>
  );
};
