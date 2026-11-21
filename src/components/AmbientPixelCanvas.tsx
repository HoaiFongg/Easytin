import React, { useMemo } from 'react';
import { useTheme } from '../ThemeContext';

interface StarParticle {
  id: number;
  top: number;
  left: number;
  size: number;
  shape: 'bit0' | 'bit1' | 'square' | 'dot';
  delay: number;
  duration: number;
  darkColor: string;
  lightColor: string;
}

export const AmbientPixelCanvas: React.FC = () => {
  const { effectiveTheme } = useTheme();
  const isLight = effectiveTheme === 'light';

  // Deterministic retro computing particles (Binary bits 0/1 & pixel blocks)
  const stars = useMemo<StarParticle[]>(() => {
    const raw: [number, number, number, 'bit0' | 'bit1' | 'square' | 'dot', number, number, string, string][] = [
      [8, 12, 10, 'bit0', 0.2, 3.2, '#fee761', '#f59e0b'],
      [15, 88, 8, 'dot', 1.1, 2.8, '#2ce8f5', '#0284c7'],
      [22, 45, 6, 'square', 2.3, 3.6, '#38b764', '#10b981'],
      [28, 5, 10, 'bit1', 0.8, 4.0, '#fca3ca', '#ec4899'],
      [36, 78, 6, 'dot', 1.7, 3.1, '#fee761', '#d97706'],
      [42, 25, 8, 'square', 2.9, 3.4, '#70a5fd', '#3b82f6'],
      [50, 92, 10, 'bit0', 0.5, 3.8, '#38b764', '#059669'],
      [58, 15, 7, 'dot', 1.4, 2.9, '#fee761', '#f59e0b'],
      [65, 62, 8, 'square', 2.1, 3.5, '#2ce8f5', '#0284c7'],
      [72, 82, 10, 'bit1', 0.9, 4.2, '#fca3ca', '#db2777'],
      [78, 38, 6, 'dot', 1.8, 3.0, '#38b764', '#10b981'],
      [85, 8, 8, 'square', 2.6, 3.7, '#fee761', '#d97706'],
      [90, 70, 7, 'dot', 0.3, 3.3, '#70a5fd', '#2563eb'],
      [94, 28, 10, 'bit0', 1.5, 3.9, '#2ce8f5', '#0284c7'],
      [12, 58, 7, 'dot', 2.0, 3.1, '#38b764', '#16a34a'],
      [48, 4, 8, 'square', 0.7, 3.6, '#fee761', '#f59e0b'],
    ];

    return raw.map(([top, left, size, shape, delay, duration, darkColor, lightColor], id) => ({
      id,
      top,
      left,
      size,
      shape,
      delay,
      duration,
      darkColor,
      lightColor,
    }));
  }, []);

  return (
    <div
      className="fixed inset-0 pointer-events-none z-0 overflow-hidden transition-opacity duration-500 opacity-40 dark:opacity-35"
      aria-hidden="true"
    >
      {stars.map((s) => {
        const color = isLight ? s.lightColor : s.darkColor;

        return (
          <div
            key={s.id}
            className="absolute anim-star-twinkle select-none"
            style={{
              top: `${s.top}%`,
              left: `${s.left}%`,
              animationDelay: `${s.delay}s`,
              animationDuration: `${s.duration}s`,
            }}
          >
            {(s.shape === 'bit0' || s.shape === 'bit1') && (
              <span
                style={{ color, fontSize: `${s.size}px` }}
                className="font-mono font-bold leading-none select-none opacity-80"
              >
                {s.shape === 'bit0' ? '0' : '1'}
              </span>
            )}
            {s.shape === 'square' && (
              <div
                style={{
                  width: `${s.size * 0.75}px`,
                  height: `${s.size * 0.75}px`,
                  backgroundColor: color,
                }}
                className="rotate-45 shadow-sm"
              />
            )}
            {s.shape === 'dot' && (
              <div
                style={{
                  width: `${s.size * 0.6}px`,
                  height: `${s.size * 0.6}px`,
                  backgroundColor: color,
                }}
              />
            )}
          </div>
        );
      })}
    </div>
  );
};
export default AmbientPixelCanvas;
