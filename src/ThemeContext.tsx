import React, { createContext, useContext, useState, useEffect } from 'react';
import { ThemeManager, ThemeMode } from '../packages/domain/theme';

interface ThemeContextType {
  theme: ThemeMode;
  effectiveTheme: 'dark' | 'light';
  setTheme: (theme: ThemeMode) => void;
  toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContextType>({
  theme: 'dark',
  effectiveTheme: 'dark',
  setTheme: () => {},
  toggleTheme: () => {},
});

export const ThemeProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [theme, setThemeState] = useState<ThemeMode>(() => ThemeManager.getStoredTheme());
  const [effectiveTheme, setEffectiveTheme] = useState<'dark' | 'light'>(() =>
    ThemeManager.getEffectiveTheme(ThemeManager.getStoredTheme())
  );

  useEffect(() => {
    ThemeManager.applyTheme(theme);
    setEffectiveTheme(ThemeManager.getEffectiveTheme(theme));

    if (theme === 'system' && typeof window !== 'undefined' && window.matchMedia) {
      const media = window.matchMedia('(prefers-color-scheme: light)');
      const listener = () => {
        ThemeManager.applyTheme('system');
        setEffectiveTheme(ThemeManager.getEffectiveTheme('system'));
      };
      media.addEventListener('change', listener);
      return () => media.removeEventListener('change', listener);
    }
  }, [theme]);

  const setTheme = (newTheme: ThemeMode) => {
    ThemeManager.setStoredTheme(newTheme);
    setThemeState(newTheme);
    setEffectiveTheme(ThemeManager.getEffectiveTheme(newTheme));
  };

  const toggleTheme = () => {
    const currentEffective = ThemeManager.getEffectiveTheme(theme);
    const next: ThemeMode = currentEffective === 'light' ? 'dark' : 'light';
    setTheme(next);
  };

  return (
    <ThemeContext.Provider value={{ theme, effectiveTheme, setTheme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

export const useTheme = () => useContext(ThemeContext);
