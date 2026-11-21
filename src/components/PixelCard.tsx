import React from 'react';
import clsx from 'clsx';

interface PixelCardProps {
  children: React.ReactNode;
  variant?: 'default' | 'gold' | 'green';
  className?: string;
  onClick?: () => void;
}

export const PixelCard: React.FC<PixelCardProps> = ({
  children,
  variant = 'default',
  className,
  onClick,
}) => {
  const borderClass = {
    default: 'pixel-border bg-[#262b44]',
    gold: 'pixel-border-gold bg-[#262b44]',
    green: 'pixel-border-green bg-[#262b44]',
  }[variant];

  return (
    <div
      onClick={onClick}
      className={clsx(
        'p-4 transition-all duration-100',
        borderClass,
        onClick && 'cursor-pointer hover:bg-[#3a4466] hover:-translate-y-0.5',
        className
      )}
    >
      {children}
    </div>
  );
};
