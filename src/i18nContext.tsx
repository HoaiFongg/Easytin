import React, { createContext, useContext, useState, useEffect } from 'react';
import { getStoredLanguage, setStoredLanguage, Language, t as translate, TranslationKey } from '../packages/domain/i18n';

interface I18nContextType {
  language: Language;
  setLanguage: (lang: Language) => void;
  t: (key: TranslationKey) => string;
}

const I18nContext = createContext<I18nContextType>({
  language: 'vi',
  setLanguage: () => {},
  t: (key: TranslationKey) => key,
});

export const I18nProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [language, setLanguageState] = useState<Language>(() => getStoredLanguage());

  const setLanguage = (lang: Language) => {
    setStoredLanguage(lang);
    setLanguageState(lang);
  };

  const t = (key: TranslationKey): string => {
    return translate(key, language);
  };

  useEffect(() => {
    document.documentElement.lang = language;
  }, [language]);

  return (
    <I18nContext.Provider value={{ language, setLanguage, t }}>
      {children}
    </I18nContext.Provider>
  );
};

export const useI18n = (): I18nContextType => {
  return useContext(I18nContext);
};
