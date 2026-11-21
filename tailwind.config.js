/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
    "./packages/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        pixel: ['"Press Start 2P"', 'monospace'],
        sans: ['"Be Vietnam Pro"', 'Inter', 'system-ui', 'sans-serif'],
      },
      colors: {
        pixel: {
          bg: '#181425',
          card: '#262b44',
          cardHover: '#3a4466',
          border: '#5a6988',
          borderLight: '#8b9bb4',
          primary: '#38b764',
          primaryLight: '#a7f070',
          accent: '#feae34',
          accentLight: '#fee761',
          danger: '#e43b44',
          blue: '#124e89',
          cyan: '#2ce8f5',
          purple: '#5d275d',
        }
      },
      boxShadow: {
        'pixel-sm': '2px 2px 0px 0px rgba(0,0,0,0.5)',
        'pixel': '4px 4px 0px 0px rgba(0,0,0,0.6)',
        'pixel-lg': '6px 6px 0px 0px rgba(0,0,0,0.7)',
        'pixel-pressed': 'inset 2px 2px 0px 0px rgba(0,0,0,0.6)',
      }
    },
  },
  plugins: [],
}
