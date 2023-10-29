const colors = require('tailwindcss/colors');

module.exports = {
  content: ['./src/renderer/**/*.{js,jsx,ts,tsx,ejs}'],
  darkMode: 'class', // or 'media' or 'class'
  variants: {},
  content: ['./src/*/.tsx'],
  plugins: [require('daisyui')],
  daisyui: {
    themes: ['light', 'night', 'dark'],
  },
};
